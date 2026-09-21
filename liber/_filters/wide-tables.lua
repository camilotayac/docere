-- =============================================================================
-- wide-tables.lua
-- Wide tables (≥6 cols) → landscape PDF / scrollable HTML
-- =============================================================================
--
-- PURPOSE:
--   Any table with 6 or more columns is automatically:
--     • Typst  — wrapped in a flipped A4 page with reduced font size.
--     • LaTeX  — wrapped in a {landscape} environment (requires pdflscape).
--     • HTML   — wrapped in a scrollable .wide-table div with sticky headers.
--
-- COLUMN-WIDTH PRESETS (proportional, sum to 1.0):
--   6-col  → WIDTHS_6COL  (used for Plan de Área without DBA)
--   7-col  → WIDTHS_7COL  (Plan de Área with DBA column)
--   8-col  → WIDTHS_8COL  (extended tables)
--
-- ICFES ZEBRA/HEADER STYLING (LaTeX only):
--   When converting the wide table for PDF, this filter also injects the
--   ICFES colour palette (icfesheader / icfeveryodd / icfeveryeven) so that
--   Plan de Área tables match the ICFES aesthetic without needing a separate pass.
--
-- SINGLE-RESPONSIBILITY: Only handles wide (≥6-col) structural tables.
--   ICFES option grids → icfes-tables.lua  |  Callout boxes → custom-questions.lua
-- =============================================================================


local MIN_COLS_FOR_LANDSCAPE = 6
local WIDTHS_6COL = {0.03, 0.03, 0.28, 0.28, 0.28, 0.10}
local WIDTHS_7COL = {0.03, 0.03, 0.22, 0.22, 0.22, 0.21, 0.07}
local WIDTHS_8COL = {0.03, 0.03, 0.16, 0.28, 0.24, 0.08, 0.08, 0.10}

-- Detect empty rows (all cells empty/whitespace) — used to remove separator rows
local function is_empty_row(row)
  local cells = row.cells or row
  for _, cell in ipairs(cells) do
    local content = cell.contents or cell.content or cell
    if content and type(content) == "table" and #content > 0 then
      local text = pandoc.utils.stringify(content)
      if text:match("%S") then return false end
    end
  end
  return true
end

local function remove_empty_rows(tbl)
  if tbl.bodies then
    for _, body in ipairs(tbl.bodies) do
      local rows = body.body or body.rows
      if rows then
        local filtered = {}
        for _, row in ipairs(rows) do
          if not is_empty_row(row) then
            filtered[#filtered + 1] = row
          end
        end
        body.body = filtered
      end
    end
  elseif tbl.body and tbl.body.rows then
    local filtered = {}
    for _, row in ipairs(tbl.body.rows) do
      if not is_empty_row(row) then
        filtered[#filtered + 1] = row
      end
    end
    tbl.body.rows = filtered
  end
  return tbl
end

function Pandoc(doc)
  if quarto.doc.is_format("html") then
    local css = [[<style>
.wide-table table thead th{position:sticky;top:0;background:var(--quarto-body-bg,#fff);z-index:1}
#TOC .header-section-number{display:none}
</style>]]
    doc.blocks:insert(1, pandoc.RawBlock("html", css))
  end

  return doc:walk({
    Table = function(el)
  local ncols
  if el.colspecs then
    ncols = #el.colspecs
  elseif el.columns then
    ncols = el.columns
  else
    return el
  end

  if ncols < MIN_COLS_FOR_LANDSCAPE then
    return el
  end

  if quarto.doc.is_format("typst") then
    local widths
    if ncols == 6 then
      widths = WIDTHS_6COL
    elseif ncols == 7 then
      widths = WIDTHS_7COL
    elseif ncols == 8 then
      widths = WIDTHS_8COL
    end
    if widths and el.colspecs then
      for i, w in ipairs(widths) do
        if el.colspecs[i] then
          el.colspecs[i][2] = w
        end
      end
    end

    return {
      pandoc.RawBlock("typst", "#page(paper: \"a4\", flipped: true, margin: (x: 1.8cm, y: 1.8cm))[\n#set text(size: 8pt)\n#set par(leading: 0.55em)\n"),
      el,
      pandoc.RawBlock("typst", "]\n")
    }
  elseif quarto.doc.is_format("pdf") then
    quarto.doc.use_latex_package("pdflscape")
    quarto.doc.use_latex_package("colortbl")
    local doc = pandoc.Pandoc({el})
    local latex_str = pandoc.write(doc, "latex")

    local widths
    if ncols == 6 then
      widths = WIDTHS_6COL
    elseif ncols == 7 then
      widths = WIDTHS_7COL
    elseif ncols == 8 then
      widths = WIDTHS_8COL
    end
    if widths then
      local equal = string.format("%.4f", 1.0 / ncols)
      for i, w in ipairs(widths) do
        local old = "\\real{" .. equal .. "}"
        local new = "\\real{" .. string.format("%.4f", w) .. "}"
        latex_str = latex_str:gsub(old, new, 1)
      end
    end

    -- Inject ICFES color styling
    -- 1. Color header row after \toprule (background + text color)
    latex_str = latex_str:gsub(
      "(\\toprule\\noalign%{%})\n(\\begin{minipage})",
      "%1\n\\rowcolor{icfesheader}\\color{icfestext}\\bfseries\n%2"
    )
    -- 2. Set body text color and zebra striping after \endlastfoot
    latex_str = latex_str:gsub(
      "(\\endlastfoot)\n",
      "%1\n\\rowcolors{2}{icfeveryodd}{icfeveryeven}\n\\color{icfestabletext}\\mdseries\n"
    )
    -- 3. Wrap in color scope (no \rowcolors — conflicts with booktabs \noalign)
    local styled = "\\begingroup\n"
      .. "\\arrayrulecolor{icfesborder}\n"
      .. latex_str
      .. "\\arrayrulecolor{black}\n"
      .. "\\endgroup\n"

    local wrapped = "\\begin{landscape}\n\\centering\n\\small\n"
                  .. styled
                  .. "\\normalsize\n\\end{landscape}"
    return pandoc.RawBlock("latex", wrapped)
  else
    local widths
    if ncols == 6 then
      widths = WIDTHS_6COL
    elseif ncols == 7 then
      widths = WIDTHS_7COL
    elseif ncols == 8 then
      widths = WIDTHS_8COL
    end
    if widths then
      for i, w in ipairs(widths) do
        el.colspecs[i][2] = w
      end
    end
    return pandoc.Div({el}, pandoc.Attr("", {"wide-table"}, {style = "overflow: auto; max-height: 80vh;"}))
  end
    end
  })
end
