-- icfes-tables.lua
-- Transforms ICFES 2x2 option tables into styled grids
-- PDF: tcbraster with tcolorbox per option
-- HTML/EPUB: Div.icfes-grid with Span.icfes-letra circles

local in_evaluacion = false

-- ── Section tracking ──────────────────────────

function Header(el)
  if el.level ~= 2 then return el end
  in_evaluacion = false
  for _, cls in ipairs(el.classes) do
    if cls == "evaluacion" then in_evaluacion = true end
  end
  return el
end

-- ── Letter extraction ──────────────────────────

local function extract_letter(blocks)
  if #blocks == 0 then return nil, blocks end
  local plain = blocks[1]
  if plain.t ~= "Plain" and plain.t ~= "Para" then return nil, blocks end

  local inlines = plain.content
  if #inlines < 3 then return nil, blocks end

  local first, second, third = inlines[1], inlines[2], inlines[3]

  -- Case 1: "A. " as three separate tokens: Str("A"), Str("."), Space()
  if first.t == "Str" and #first.text == 1
     and first.text:match("^[A-D]$")
     and second.t == "Str" and second.text == "."
     and third.t == "Space" then
    local remaining = {}
    for i = 4, #inlines do table.insert(remaining, inlines[i]) end
    return first.text, {pandoc.Plain(remaining)}
  end

  -- Case 2: "A. " as two tokens: Str("A."), Space()
  if first.t == "Str" and first.text:match("^([A-D])%.$")
     and second.t == "Space" then
    local letter = first.text:match("^([A-D])%.$")
    local remaining = {}
    for i = 3, #inlines do table.insert(remaining, inlines[i]) end
    return letter, {pandoc.Plain(remaining)}
  end

  return nil, blocks
end

-- ── LaTeX conversion ──────────────────────────

local function esc(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("{", "\\{")
  s = s:gsub("}", "\\}")
  s = s:gsub("&", "\\&")
  s = s:gsub("%%", "\\%%")
  s = s:gsub("#", "\\#")
  s = s:gsub("_", "\\_")
  s = s:gsub("%^", "\\^{}")
  s = s:gsub("~", "\\textasciitilde{}")
  return s
end

local function inlines_to_latex(inlines)
  local parts = {}
  for _, inl in ipairs(inlines) do
    if inl.t == "Str" then
      table.insert(parts, esc(inl.text))
    elseif inl.t == "Space" or inl.t == "SoftBreak" then
      table.insert(parts, " ")
    elseif inl.t == "LineBreak" then
      table.insert(parts, "\\\\")
    elseif inl.t == "Math" then
      local delim = inl.mathtype == "InlineMath" and "$" or "$$"
      table.insert(parts, delim .. inl.text .. delim)
    elseif inl.t == "Strong" then
      table.insert(parts, "\\textbf{" .. inlines_to_latex(inl.content) .. "}")
    elseif inl.t == "Emph" then
      table.insert(parts, "\\emph{" .. inlines_to_latex(inl.content) .. "}")
    elseif inl.t == "Code" then
      table.insert(parts, "\\texttt{" .. esc(inl.text) .. "}")
    elseif inl.t == "Subscript" then
      table.insert(parts, "\\textsubscript{" .. inlines_to_latex(inl.content) .. "}")
    elseif inl.t == "Superscript" then
      table.insert(parts, "\\textsuperscript{" .. inlines_to_latex(inl.content) .. "}")
    elseif inl.t == "SmallCaps" then
      table.insert(parts, "\\textsc{" .. inlines_to_latex(inl.content) .. "}")
    elseif inl.t == "Strikeout" then
      table.insert(parts, "\\sout{" .. inlines_to_latex(inl.content) .. "}")
    elseif inl.t == "RawInline" and (inl.format == "tex" or inl.format == "latex") then
      table.insert(parts, inl.text)
    elseif inl.t == "Quoted" then
      local inner = inlines_to_latex(inl.content)
      local q = inl.quotetype == "SingleQuote" and {"`", "'"} or {"``", "''"}
      table.insert(parts, q[1] .. inner .. q[2])
    elseif inl.t == "Link" then
      table.insert(parts, "\\href{" .. inl.target .. "}{" .. inlines_to_latex(inl.content) .. "}")
    elseif inl.t == "Cite" then
      local ids = {}
      for _, c in ipairs(inl.citations) do table.insert(ids, c.id) end
      table.insert(parts, "\\cite{" .. table.concat(ids, ",") .. "}")
    else
      table.insert(parts, pandoc.utils.stringify(inl))
    end
  end
  return table.concat(parts)
end

local function blocks_to_latex(blocks)
  local parts = {}
  for _, b in ipairs(blocks) do
    if b.t == "Plain" or b.t == "Para" then
      table.insert(parts, inlines_to_latex(b.content))
    elseif b.t == "Math" and b.mathtype == "DisplayMath" then
      table.insert(parts, "$$" .. b.text .. "$$")
    elseif b.t == "RawBlock" and (b.format == "tex" or b.format == "latex") then
      table.insert(parts, b.text)
    end
  end
  return table.concat(parts)
end

-- ── Iterate all cells from a Table ─────────────

local function each_cell(tbl, fn)
  local rows = tbl.body and tbl.body.rows or tbl.rows
  for _, row in ipairs(rows) do
    local cs = row.cells or row
    for _, cell in ipairs(cs) do
      fn(cell.content or cell)
    end
  end
end

-- ── LaTeX: tcbraster ──────────────────────────

local function latex_grid(tbl)
  local lines = {"\\begin{tcbraster}[raster columns=2, raster equal height, raster column skip=6pt, raster row skip=6pt]"}
  each_cell(tbl, function(content)
    local letter, rest = extract_letter(content)
    local line = "  \\begin{tcolorbox}[colback=white, colframe=icfesletra, arc=4pt, boxrule=0.6pt, left=8pt, right=8pt, top=6pt, bottom=6pt, valign=center]\n    "
    if letter then
      line = line .. "\\circletter{" .. letter .. "} " .. blocks_to_latex(rest)
    else
      line = line .. blocks_to_latex(content)
    end
    line = line .. "\n  \\end{tcolorbox}"
    table.insert(lines, line)
  end)
  table.insert(lines, "\\end{tcbraster}")
  return pandoc.RawBlock("latex", table.concat(lines, "\n"))
end

-- ── HTML/EPUB: Div grid ───────────────────────

local grid_style = "display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin: 1em 0;"
local opcion_style = "display: flex; align-items: center; gap: 8px; padding: 8px 10px; border: 0.6pt solid #000000; border-radius: 4px; background: white;"
local letra_style = "display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border: 1.5px solid #000000; border-radius: 50%; font-weight: bold; font-size: 0.9em; color: #000000; flex-shrink: 0;"
local texto_style = "flex: 1;"

local function html_grid(tbl)
  local grid_attrs = {class = "icfes-grid", style = grid_style}
  local grid = pandoc.Div({}, grid_attrs)
  each_cell(tbl, function(content)
    local letter, rest = extract_letter(content)
    local opcion = pandoc.Div({}, {class = "icfes-opcion", style = opcion_style})
    if letter then
      local letra = pandoc.Span({pandoc.Str(letter)}, {class = "icfes-letra", style = letra_style})
      local rest_inlines = {}
      for _, b in ipairs(rest) do
        if b.content then
          for _, inl in ipairs(b.content) do
            table.insert(rest_inlines, inl)
          end
        end
      end
      local texto = pandoc.Span(rest_inlines, {class = "icfes-texto", style = texto_style})
      opcion.content = {letra, texto}
    else
      for _, b in ipairs(content) do
        table.insert(opcion.content, b)
      end
    end
    table.insert(grid.content, opcion)
  end)
  return grid
end

-- ── LineBlock parsing (backward compat) ────────
-- Handles tables written as line blocks (no separator line).

local function trim_trailing(inlines)
  while #inlines > 0 and inlines[#inlines].t == "Space" do
    inlines[#inlines] = nil
  end
end

local function trim_leading(inlines)
  while #inlines > 0 and inlines[1].t == "Space" do
    table.remove(inlines, 1)
  end
end

local emdash = "\226\128\148"
local endash  = "\226\128\147"

local function line_is_separator(inlines)
  local parts = {}
  for _, inl in ipairs(inlines) do
    if inl.t == "Str" then table.insert(parts, inl.text) end
  end
  local s = table.concat(parts)
  -- Remove expected characters: |, :, -, whitespace, and Unicode dashes
  s = s:gsub("[%|:%-]", "")
  s = s:gsub("%s", "")
  s = s:gsub(emdash, "")
  s = s:gsub(endash, "")
  return #s == 0
end

local function parse_lineblock_cells(el)
  local cells = {}
  for _, line in ipairs(el.content) do
    -- Skip separator lines (| --- |, | :--- |, etc.)
    if line_is_separator(line) then goto continue end

    local cell = {}
    for _, inl in ipairs(line) do
      if inl.t == "Str" and inl.text == "|" then
        trim_trailing(cell)
        if #cell > 0 then
          table.insert(cells, cell)
        end
        cell = {}
      else
        table.insert(cell, inl)
      end
    end
    trim_trailing(cell)
    if #cell > 0 then
      table.insert(cells, cell)
    end
    ::continue::
  end
  for _, c in ipairs(cells) do trim_leading(c) end
  return cells
end

local function latex_grid_from_lineblock(el)
  local cells = parse_lineblock_cells(el)
  local lines = {"\\begin{tcbraster}[raster columns=2, raster equal height, raster column skip=6pt, raster row skip=6pt]"}
  for _, cinlines in ipairs(cells) do
    local blocks = {pandoc.Plain(cinlines)}
    local letter, rest = extract_letter(blocks)
    local line = "  \\begin{tcolorbox}[colback=white, colframe=icfesletra, arc=4pt, boxrule=0.6pt, left=8pt, right=8pt, top=6pt, bottom=6pt, valign=center]\n    "
    if letter then
      line = line .. "\\circletter{" .. letter .. "} " .. blocks_to_latex(rest)
    else
      line = line .. blocks_to_latex(blocks)
    end
    line = line .. "\n  \\end{tcolorbox}"
    table.insert(lines, line)
  end
  table.insert(lines, "\\end{tcbraster}")
  return pandoc.RawBlock("latex", table.concat(lines, "\n"))
end

local function html_grid_from_lineblock(el)
  local cells = parse_lineblock_cells(el)
  local grid = pandoc.Div({}, {class = "icfes-grid", style = grid_style})
  for _, cinlines in ipairs(cells) do
    local blocks = {pandoc.Plain(cinlines)}
    local letter, rest = extract_letter(blocks)
    local opcion = pandoc.Div({}, {class = "icfes-opcion", style = opcion_style})
    if letter then
      local letra = pandoc.Span({pandoc.Str(letter)}, {class = "icfes-letra", style = letra_style})
      local rest_inlines = {}
      for _, b in ipairs(rest) do
        if b.content then
          for _, inl in ipairs(b.content) do
            table.insert(rest_inlines, inl)
          end
        end
      end
      local texto = pandoc.Span(rest_inlines, {class = "icfes-texto", style = texto_style})
      opcion.content = {letra, texto}
    else
      for _, b in ipairs(blocks) do
        table.insert(opcion.content, b)
      end
    end
    table.insert(grid.content, opcion)
  end
  return grid
end

-- ── Entry points ───────────────────────────────

function Table(el)
  if not in_evaluacion then return el end
  if FORMAT == "latex" then return latex_grid(el)
  else return html_grid(el) end
end

function LineBlock(el)
  if not in_evaluacion then return el end
  if FORMAT == "latex" then return latex_grid_from_lineblock(el)
  else return html_grid_from_lineblock(el) end
end
