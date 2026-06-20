-- wide-tables.lua
-- Wraps wide tables (>=6 columns) in landscape for PDF and scrollable div for HTML/EPUB
-- For 8-column tables (PlanDeArea), post-processes LaTeX to set proportional column widths

local MIN_COLS_FOR_LANDSCAPE = 6
local WIDTHS_8COL = {0.04, 0.04, 0.16, 0.28, 0.24, 0.08, 0.06, 0.10}

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

    if ncols == 8 then
      local equal = string.format("%.4f", 1.0 / ncols)
      for i, w in ipairs(WIDTHS_8COL) do
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
    return pandoc.Div({el}, pandoc.Attr("", {}, {style = "overflow-x: auto;"}))
  end
end
