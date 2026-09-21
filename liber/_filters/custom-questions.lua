-- =============================================================================
-- custom-questions.lua
-- Visual help / difficulty callout boxes for Natura Docens
-- =============================================================================
--
-- PURPOSE:
--   Translates fenced-div callouts into styled boxes with a color-coded
--   difficulty indicator.  Three levels are supported:
--
--     ::: {.pregunta-basica title="Título opcional"}
--     Contenido de la pregunta...
--     :::
--
--     ::: {.pregunta-media   title="..."}   → amarillo
--     ::: {.pregunta-dificil title="..."}  → rojo
--
-- FORMAT SUPPORT:
--   • HTML  — Quarto's native callouts + CSS (no transformation needed).
--   • LaTeX — tcolorbox environments defined in preamble.tex.
--   • Typst — #block() with colored left border and badge, rendered inline.
--
-- SINGLE-RESPONSIBILITY: Only handles `.pregunta-*` divs.
--   Tables → icfes-tables.lua   |   Wide tables → wide-tables.lua
-- =============================================================================

-- ── Typst color palette ──────────────────────────────────────────────────────
local TYPST_STYLES = {
  ["pregunta-basica"]  = { fill = "#eef7ee", border = "#4caf50", label = "Básica",   label_fill = "#4caf50" },
  ["pregunta-media"]   = { fill = "#fff8e1", border = "#f9a825", label = "Media",    label_fill = "#f9a825" },
  ["pregunta-dificil"] = { fill = "#fdecea", border = "#e53935", label = "Difícil",  label_fill = "#e53935" },
}

-- ── LaTeX environment names ───────────────────────────────────────────────────
local LATEX_ENVS = {
  ["pregunta-basica"]  = "preguntabasica",
  ["pregunta-media"]   = "preguntamedia",
  ["pregunta-dificil"] = "preguntadificil",
}

-- ── Helper: build LaTeX tcolorbox environment ─────────────────────────────────
local function make_latex_env(env_name, title, content)
  local blocks = {}
  local begin_str = "\\begin{" .. env_name .. "}"
  if title and title ~= "" then
    begin_str = begin_str .. "[title={" .. title .. "}]"
  end
  table.insert(blocks, pandoc.RawBlock("latex", begin_str))
  for _, b in ipairs(content) do
    table.insert(blocks, b)
  end
  table.insert(blocks, pandoc.RawBlock("latex", "\\end{" .. env_name .. "}"))
  return blocks
end

-- ── Helper: build Typst styled block ─────────────────────────────────────────
local function make_typst_block(style, title, content)
  -- Serialize the inner content to Typst markup
  local inner_doc  = pandoc.Pandoc(content)
  local inner_typst = pandoc.write(inner_doc, "typst"):gsub("^%s+", ""):gsub("%s+$", "")

  local label_str = ""
  if title and title ~= "" then
    label_str = title
  else
    label_str = style.label
  end

  -- Badge (top-right corner)
  local badge = string.format(
    "#box(inset: (x: 6pt, y: 2.5pt), radius: 3pt, fill: rgb(\"%s\"))[#text(size: 7.5pt, weight: \"bold\", fill: white)[%s]]",
    style.label_fill, label_str
  )

  local typst_code = string.format(
    "#block(width: 100%%, inset: (left: 4pt, rest: 10pt), radius: (left: 2pt, rest: 4pt), fill: rgb(\"%s\"), stroke: (left: 2.5pt + rgb(\"%s\"), rest: 0pt))[\n#grid(columns: (1fr, auto), gutter: 0pt,\n  [%s],\n  [%s]\n)\n]",
    style.fill, style.border,
    inner_typst, badge
  )

  return pandoc.RawBlock("typst", typst_code)
end

-- ── Main filter ───────────────────────────────────────────────────────────────
function Div(el)
  -- HTML: let Quarto render natively (CSS handles .pregunta-* classes)
  if quarto.doc.is_format("html") or quarto.doc.is_format("epub") then
    return nil
  end

  for _, cls in ipairs(el.classes) do
    -- LaTeX path
    if quarto.doc.is_format("latex") then
      local env = LATEX_ENVS[cls]
      if env then
        return make_latex_env(env, el.attributes.title, el.content)
      end
    end

    -- Typst path
    if quarto.doc.is_format("typst") then
      local style = TYPST_STYLES[cls]
      if style then
        return make_typst_block(style, el.attributes.title, el.content)
      end
    end
  end
end
