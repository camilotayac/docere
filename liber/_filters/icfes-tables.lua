-- =============================================================================
-- icfes-tables.lua
-- ICFES multiple-choice option tables → styled 2×2 grids
-- =============================================================================
--
-- PURPOSE:
--   Transforms any table or lineblock inside ::: {.icfes-opciones} into a
--   colour-coded 2×2 answer grid.  Works across all three render targets:
--
--     • LaTeX  — tcbraster with tcolorbox per option (needs preamble.tex).
--     • Typst  — native #table() with fill/stroke styling.
--     • HTML   — Div.icfes-grid with Span.icfes-letra circles (styled via CSS).
--     • EPUB   — same as HTML.
--
-- USAGE (inside a ## {.evaluacion} section):
--
--   ::: {.icfes-opciones data-correct="B"}
--   | A. Option 1 | B. Option 2 |
--   | C. Option 3 | D. Option 4 |
--   :::
--
-- RULES:
--   • Exactly 4 cells expected (A B C D).  Mismatches fall back gracefully.
--   • `data-correct` is optional; valid values: A B C D.
--   • ARIA labels are added automatically for screen-reader accessibility.
--
-- SINGLE-RESPONSIBILITY: Only handles `.icfes-opciones` grids.
--   Wide tables → wide-tables.lua  |  Callout boxes → custom-questions.lua
-- =============================================================================

local in_evaluacion = false
local question_counter = 0

-- ── Section tracking ──────────────────────────

local competencyNames = {
  ["competencia-1"] = "Comprensión",
  ["competencia-2"] = "Interpretación",
  ["competencia-3"] = "Evaluación",
}

function Header(el)
  if el.level == 2 then
    in_evaluacion = false
    question_counter = 0
    for _, cls in ipairs(el.classes) do
      if cls == "evaluacion" then in_evaluacion = true end
    end
    return el
  end
  -- Level 3: increment question counter, emit competency badge for LaTeX
  if el.level == 3 then
    if in_evaluacion then
      -- Skip incrementing for clave-respuestas heading
      local is_clave = false
      for _, cls in ipairs(el.classes) do
        if cls == "clave-respuestas" then is_clave = true end
      end
      if not is_clave then
        question_counter = question_counter + 1
      end
    end
    -- Competency badges (PDF and Typst)
    if quarto.doc.is_format("latex") then
      for _, cls in ipairs(el.classes) do
        local name = competencyNames[cls]
        if name then
          return {
            el,
            pandoc.RawBlock("latex", "\\hfill{\\small\\colorframe{icfesbg}{icfesborder}{" .. name .. "}}")
          }
        end
      end
    elseif quarto.doc.is_format("typst") then
      for _, cls in ipairs(el.classes) do
        local name = competencyNames[cls]
        if name then
          return {
            el,
            pandoc.RawBlock("typst", "#align(right)[#box(inset: (x: 8pt, y: 3.5pt), radius: 3pt, fill: rgb(\"#f4e8e4\"), stroke: 0.6pt + rgb(\"#a06050\"))[#text(size: 8.5pt, weight: \"bold\", fill: rgb(\"#a06050\"))[" .. name .. "]]]")
          }
        end
      end
    end
    -- Clave respuestas details wrapper (HTML and EPUB only)
    -- Only emit the <details> opening; JS in collapse.html closes it properly
    if quarto.doc.is_format("html") or quarto.doc.is_format("epub") then
      for _, cls in ipairs(el.classes) do
        if cls == "clave-respuestas" then
          local details = pandoc.RawBlock("html",
            '<details class="icfes-respuesta"><summary>Ver clave de respuestas</summary>')
          return {details, el}
        end
      end
    end
  end
  return el
end

-- ── Utility: safely iterate Pandoc Blocks ─────

local function blocks_to_table(blks)
  if not blks then return {} end
  if type(blks) ~= "table" then return {blks} end
  local out = {}
  for _, v in ipairs(blks) do
    out[#out + 1] = v
  end
  return out
end

-- ── Letter extraction ─────────────────────────

local function extract_letter(blks)
  local blocks = blocks_to_table(blks)
  if #blocks == 0 then return nil, blocks end
  local plain = blocks[1]
  if not plain or not plain.t then return nil, blocks end
  if plain.t ~= "Plain" and plain.t ~= "Para" then return nil, blocks end

  local inlines = plain.content
  if not inlines or #inlines < 2 then return nil, blocks end

  local first = inlines[1]

  -- Case 1: Str("A"), Str("."), Space()
  if first.t == "Str" and #first.text == 1 and first.text:match("^[A-D]$") then
    local second = inlines[2]
    if second and second.t == "Str" and second.text == "." then
      local rest_start = 3
      if #inlines >= 3 and inlines[3].t == "Space" then rest_start = 4 end
      local remaining = {}
      for i = rest_start, #inlines do remaining[#remaining + 1] = inlines[i] end
      return first.text, {pandoc.Plain(remaining)}
    end
  end

  -- Case 2: Str("A."), Space()
  if first.t == "Str" then
    local letter = first.text:match("^([A-D])%.$")
    if letter then
      local rest_start = 2
      if #inlines >= 2 and inlines[2].t == "Space" then rest_start = 3 end
      local remaining = {}
      for i = rest_start, #inlines do remaining[#remaining + 1] = inlines[i] end
      return letter, {pandoc.Plain(remaining)}
    end
  end

  -- Case 3: Str("A. texto") as single token
  if first.t == "Str" then
    local letter, rest_text = first.text:match("^([A-D])%.%s+(.+)$")
    if letter then
      local remaining = {pandoc.Str(rest_text)}
      for i = 2, #inlines do remaining[#remaining + 1] = inlines[i] end
      return letter, {pandoc.Plain(remaining)}
    end
  end

  -- Case 4: Emph/Strong wrapping letter
  if (first.t == "Emph" or first.t == "Strong") and first.content and #first.content == 1 then
    local inner = first.content[1]
    if inner.t == "Str" and #inner.text == 1 and inner.text:match("^[A-D]$") then
      local rest_start = 2
      if #inlines >= 3 and inlines[2].t == "Str" and inlines[2].text == "." then
        rest_start = 3
        if #inlines >= 4 and inlines[3].t == "Space" then rest_start = 4 end
      elseif #inlines >= 2 and inlines[2].t == "Space" then
        rest_start = 3
      end
      local remaining = {}
      for i = rest_start, #inlines do remaining[#remaining + 1] = inlines[i] end
      return inner.text, {pandoc.Plain(remaining)}
    end
  end

  return nil, blocks
end

-- ── LaTeX conversion ──────────────────────────

local function esc(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("{", "\\{")
  s = s:gsub("}", "\\}")
  s = s:gsub("%%", "%%%%")
  s = s:gsub("#", "\\#")
  s = s:gsub("_", "\\_")
  s = s:gsub("%^", "\\^{}")
  s = s:gsub("~", "\\textasciitilde{}")
  s = s:gsub("&", "\\&")
  s = s:gsub("<", "\\textless{}")
  s = s:gsub(">", "\\textgreater{}")
  return s
end

local function inlines_to_latex(inlines)
  local parts = {}
  for _, inl in ipairs(inlines) do
    if inl.t == "Str" then
      parts[#parts + 1] = esc(inl.text)
    elseif inl.t == "Space" or inl.t == "SoftBreak" then
      parts[#parts + 1] = " "
    elseif inl.t == "LineBreak" then
      parts[#parts + 1] = "\\\\"
    elseif inl.t == "Math" then
      local delim = inl.mathtype == "InlineMath" and "$" or "$$"
      parts[#parts + 1] = delim .. inl.text .. delim
    elseif inl.t == "Strong" then
      parts[#parts + 1] = "\\textbf{" .. inlines_to_latex(inl.content) .. "}"
    elseif inl.t == "Emph" then
      parts[#parts + 1] = "\\emph{" .. inlines_to_latex(inl.content) .. "}"
    elseif inl.t == "Code" then
      parts[#parts + 1] = "\\texttt{" .. esc(inl.text) .. "}"
    elseif inl.t == "Subscript" then
      parts[#parts + 1] = "\\textsubscript{" .. inlines_to_latex(inl.content) .. "}"
    elseif inl.t == "Superscript" then
      parts[#parts + 1] = "\\textsuperscript{" .. inlines_to_latex(inl.content) .. "}"
    elseif inl.t == "SmallCaps" then
      parts[#parts + 1] = "\\textsc{" .. inlines_to_latex(inl.content) .. "}"
    elseif inl.t == "Strikeout" then
      parts[#parts + 1] = "\\sout{" .. inlines_to_latex(inl.content) .. "}"
    elseif inl.t == "RawInline" and (inl.format == "tex" or inl.format == "latex") then
      parts[#parts + 1] = inl.text
    elseif inl.t == "Quoted" then
      local inner = inlines_to_latex(inl.content)
      local q = inl.quotetype == "SingleQuote" and {"`", "'"} or {"``", "''"}
      parts[#parts + 1] = q[1] .. inner .. q[2]
    elseif inl.t == "Link" then
      parts[#parts + 1] = "\\href{" .. inl.target .. "}{" .. inlines_to_latex(inl.content) .. "}"
    elseif inl.t == "Cite" then
      local ids = {}
      for _, c in ipairs(inl.citations) do ids[#ids + 1] = c.id end
      parts[#parts + 1] = "\\cite{" .. table.concat(ids, ",") .. "}"
    else
      parts[#parts + 1] = pandoc.utils.stringify(inl)
    end
  end
  return table.concat(parts)
end

local function blocks_to_latex(blks)
  local blocks = blocks_to_table(blks)
  local parts = {}
  for _, b in ipairs(blocks) do
    if b and b.t then
      if b.t == "Plain" or b.t == "Para" then
        parts[#parts + 1] = inlines_to_latex(b.content)
      elseif b.t == "Math" and b.mathtype == "DisplayMath" then
        parts[#parts + 1] = "$$" .. b.text .. "$$"
      elseif b.t == "RawBlock" and (b.format == "tex" or b.format == "latex") then
        parts[#parts + 1] = b.text
      end
    end
  end
  return table.concat(parts)
end

-- ── Cell collection ───────────────────────────

local function collect_cells(tbl)
  local cells = {}
  local simple = pandoc.utils.to_simple_table(tbl)
  if not simple then return cells end
  for _, cell in ipairs(simple.header) do
    if #cell > 0 and pandoc.utils.stringify(cell):match("%S") then
      cells[#cells + 1] = cell
    end
  end
  for _, row in ipairs(simple.rows) do
    for _, cell in ipairs(row) do
      if #cell > 0 and pandoc.utils.stringify(cell):match("%S") then
        cells[#cells + 1] = cell
      end
    end
  end
  return cells
end

-- ── Shared grid rendering ─────────────────────

local function make_latex_grid(cells)
  local lines = {
    "\\begin{tcbraster}[raster columns=2, raster equal height, raster column skip=8pt, raster row skip=8pt]"
  }
  for _, content in ipairs(cells) do
    local letter, rest = extract_letter(content)
    local inner
    if letter then
      inner = "\\circletter{" .. letter .. "} " .. blocks_to_latex(rest)
    else
      inner = blocks_to_latex(content)
    end
    lines[#lines + 1] = "  \\begin{tcolorbox}[colback=icfesbg, colframe=icfesborder, arc=4pt, boxrule=0.6pt, left=10pt, right=10pt, top=8pt, bottom=8pt, valign=center]\n    " .. inner .. "\n  \\end{tcolorbox}"
  end
  lines[#lines + 1] = "\\end{tcbraster}"
  return pandoc.RawBlock("latex", table.concat(lines, "\n"))
end

local function blocks_to_inlines(blks)
  local blocks = blocks_to_table(blks)
  local out = {}
  for _, b in ipairs(blocks) do
    if b and b.t then
      if b.t == "Plain" or b.t == "Para" then
        if b.content then
          for _, inl in ipairs(b.content) do
            out[#out + 1] = inl
          end
        end
      elseif b.t == "Math" then
        out[#out + 1] = pandoc.Math(b.mathtype, b.text)
      elseif b.t == "RawBlock" and (b.format == "tex" or b.format == "latex") then
        out[#out + 1] = pandoc.RawInline(b.format, b.text)
      end
    end
  end
  return out
end

local function make_html_grid(cells, qid, correct)
  local attrs = {class = "icfes-grid", role = "group", ["aria-label"] = "Opciones de respuesta"}
  if qid then
    attrs["data-question-id"] = qid
  end
  if correct then
    attrs["data-correct"] = correct
  end
  local grid = pandoc.Div({}, attrs)
  for _, content in ipairs(cells) do
    local letter, rest = extract_letter(content)
    local opcion = pandoc.Div({}, {class = "icfes-opcion", ["aria-label"] = "Opción " .. (letter or "?")})
    if letter then
      local letra = pandoc.Span({pandoc.Str(letter)}, {class = "icfes-letra", ["aria-hidden"] = "true"})
      local texto = pandoc.Span(blocks_to_inlines(rest), {class = "icfes-texto"})
      opcion.content = {letra, texto}
    else
      opcion.content = blocks_to_table(content)
    end
    grid.content[#grid.content + 1] = opcion
  end
  return grid
end

-- ── LineBlock parsing ─────────────────────────

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
  local s = pandoc.utils.stringify(inlines)
  s = s:gsub("[%|:%-]", "")
  s = s:gsub("%s", "")
  s = s:gsub(emdash, "")
  s = s:gsub(endash, "")
  return #s == 0
end

local function collect_lineblock_cells(el)
  local cells = {}
  for _, line in ipairs(el.content) do
    if line_is_separator(line) then goto continue end
    local cell = {}
    for _, inl in ipairs(line) do
      if inl.t == "Str" and inl.text == "|" then
        trim_trailing(cell)
        if #cell > 0 then cells[#cells + 1] = cell end
        cell = {}
      else
        cell[#cell + 1] = inl
      end
    end
    trim_trailing(cell)
    if #cell > 0 then cells[#cells + 1] = cell end
    ::continue::
  end
  for _, c in ipairs(cells) do trim_leading(c) end
  return cells
end

local function lineblock_to_blocks(cells)
  local blocks = {}
  for _, cinlines in ipairs(cells) do
    blocks[#blocks + 1] = pandoc.Plain(cinlines)
  end
  return blocks
end

-- ── Entry points ───────────────────────────────
-- Tables are only transformed when explicitly wrapped in
-- ::: {.icfes-opciones} in the source .qmd.  This prevents
-- non-ICFES data tables inside .evaluacion from receiving
-- the grid layout.

local function blocks_to_typst(blks)
  local doc = pandoc.Pandoc(blocks_to_table(blks))
  local str = pandoc.write(doc, "typst")
  str = str:gsub("^%s+", ""):gsub("%s+$", "")
  return str
end

local function make_typst_grid(cells)
  local lines = {
    "#v(0.3em)",
    "#table(",
    "  columns: (1fr, 1fr),",
    "  column-gutter: 10pt,",
    "  row-gutter: 8pt,",
    "  stroke: 0.6pt + rgb(\"#a06050\"),",
    "  fill: rgb(\"#faf7f5\"),",
    "  align: left + horizon,",
    "  inset: (x: 9pt, y: 7pt),",
  }
  for _, content in ipairs(cells) do
    local letter, rest = extract_letter(content)
    local inner = blocks_to_typst(rest)
    if letter then
      lines[#lines + 1] = "  [\n    #text(weight: \"bold\", fill: rgb(\"#a06050\"))[" .. letter .. ".] " .. inner .. "\n  ],"
    else
      lines[#lines + 1] = "  [\n    " .. inner .. "\n  ],"
    end
  end
  lines[#lines + 1] = ")"
  lines[#lines + 1] = "#v(0.3em)"
  return pandoc.RawBlock("typst", table.concat(lines, "\n"))
end

local function transform_icfes_table(tbl, correct)
  local cells = collect_cells(tbl)
  if #cells ~= 4 then
    quarto.log.warning("icfes-opciones: expected 4 cells, got " .. #cells .. " — falling back to original table")
    return tbl
  end
  -- Validate data-correct value
  if correct and not (correct == "A" or correct == "B" or correct == "C" or correct == "D") then
    quarto.log.warning("icfes-opciones: invalid data-correct value '" .. correct .. "' — ignoring")
    correct = nil
  end
  if quarto.doc.is_format("latex") then
    return make_latex_grid(cells)
  elseif quarto.doc.is_format("typst") then
    return make_typst_grid(cells)
  else
    return make_html_grid(cells, "q-" .. question_counter, correct)
  end
end

local function transform_icfes_lineblock(lb, correct)
  local cells = collect_lineblock_cells(lb)
  if #cells ~= 4 then
    quarto.log.warning("icfes-opciones: expected 4 cells, got " .. #cells .. " — falling back to original lineblock")
    return lb
  end
  -- Validate data-correct value
  if correct and not (correct == "A" or correct == "B" or correct == "C" or correct == "D") then
    quarto.log.warning("icfes-opciones: invalid data-correct value '" .. correct .. "' — ignoring")
    correct = nil
  end
  if quarto.doc.is_format("latex") then
    return make_latex_grid(lineblock_to_blocks(cells))
  elseif quarto.doc.is_format("typst") then
    return make_typst_grid(lineblock_to_blocks(cells))
  else
    return make_html_grid(lineblock_to_blocks(cells), "q-" .. question_counter, correct)
  end
end

function Div(el)
  if not in_evaluacion then return el end
  local has_icfes = false
  local correct_letter = nil
  for _, cls in ipairs(el.classes) do
    if cls == "icfes-opciones" then has_icfes = true; break end
  end
  if not has_icfes then return el end

  -- Extract data-correct attribute if present (optional)
  if el.attributes and el.attributes["data-correct"] then
    correct_letter = el.attributes["data-correct"]
  end

  local new_content = {}
  for _, block in ipairs(el.content) do
    if block.t == "Table" then
      new_content[#new_content + 1] = transform_icfes_table(block, correct_letter)
    elseif block.t == "LineBlock" then
      new_content[#new_content + 1] = transform_icfes_lineblock(block, correct_letter)
    else
      new_content[#new_content + 1] = block
    end
  end
  el.content = new_content
  return el
end
