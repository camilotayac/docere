-- table-styling.lua
-- Injects ICFES color styling into non-wide data tables for PDF output.
-- Wide tables (>=6 cols) are handled by wide-tables.lua.
-- HTML tables are styled via headings.css.
-- Tables inside .evaluacion sections are skipped (data tables in MC questions).

local MIN_COLS = 6
local in_evaluacion = false

return {
  {
    Header = function(el)
      if el.level == 2 then
        in_evaluacion = false
        for _, cls in ipairs(el.classes) do
          if cls == "evaluacion" then in_evaluacion = true end
        end
      end
      return el
    end,

    Table = function(el)
      if not quarto.doc.is_format("latex") then
        return el
      end

      -- Skip tables inside .evaluacion sections (data tables in MC questions)
      if in_evaluacion then
        return el
      end

      local ncols
      if el.colspecs then
        ncols = #el.colspecs
      elseif el.columns then
        ncols = el.columns
      else
        return el
      end

      -- Skip wide tables (handled by wide-tables.lua)
      if ncols >= MIN_COLS then
        return el
      end

      quarto.doc.use_latex_package("colortbl")

      local doc = pandoc.Pandoc({el})
      local latex_str = pandoc.write(doc, "latex")

      -- Inject header row color after \toprule (background + text color)
      latex_str = latex_str:gsub(
        "(\\toprule\\noalign%{%})\n(.)",
        "%1\n\\rowcolor{icfesheader}\\color{icfestext}\\bfseries\n%2"
      )

      -- Set body text color and zebra striping after \endlastfoot
      latex_str = latex_str:gsub(
        "(\\endlastfoot)\n",
        "%1\n\\rowcolors{2}{icfeveryodd}{icfeveryeven}\n\\color{icfestabletext}\\mdseries\n"
      )

      local styled = "\\begingroup\n"
        .. "\\arrayrulecolor{icfesborder}\n"
        .. latex_str
        .. "\\arrayrulecolor{black}\n"
        .. "\\endgroup\n"

      return pandoc.RawBlock("latex", styled)
    end
  }
}
