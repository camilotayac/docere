-- wide-tables.lua
-- Wraps wide tables (>=6 columns) in landscape for PDF and scrollable div for HTML/EPUB
-- For 7/8-column tables (PlanDeArea), post-processes LaTeX to set proportional column widths

local MIN_COLS_FOR_LANDSCAPE = 6
local WIDTHS_7COL = {0.05, 0.05, 0.20, 0.20, 0.20, 0.20, 0.10}
local WIDTHS_8COL = {0.04, 0.04, 0.16, 0.28, 0.24, 0.08, 0.06, 0.10}

function Pandoc(doc)
  if quarto.doc.is_format("html") then
    local css = [[<style>
.wide-table table thead th{position:sticky;top:0;background:var(--quarto-body-bg,#fff);z-index:1}
#TOC .header-section-number{display:none}
</style>]]
    doc.blocks:insert(1, pandoc.RawBlock("html", css))
  end
  return doc
end

function Table(el)
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

  if quarto.doc.is_format("pdf") then
    quarto.doc.use_latex_package("pdflscape")
    local doc = pandoc.Pandoc({el})
    local latex_str = pandoc.write(doc, "latex")

    local widths
    if ncols == 7 then
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

    local wrapped = "\\begin{landscape}\n\\centering\n\\small\n"
                  .. latex_str
                  .. "\\normalsize\n\\end{landscape}"
    return pandoc.RawBlock("latex", wrapped)
  else
    local widths
    if ncols == 7 then
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
