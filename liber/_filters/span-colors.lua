local function hex_from_style(style)
  if not style then return nil end
  return style:match("color:%s*#(%x%x%x%x%x%x)")
end

function Span(el)
  local hex = hex_from_style(el.attributes and el.attributes["style"])
  if not hex then return el end

  if quarto.doc.is_format("latex") then
    local result = { pandoc.RawInline("latex", "\\textcolor[HTML]{" .. hex .. "}{") }
    for _, inline in ipairs(el.content) do
      table.insert(result, inline)
    end
    table.insert(result, pandoc.RawInline("latex", "}"))
    return result
  elseif quarto.doc.is_format("typst") then
    local result = { pandoc.RawInline("typst", "#text(fill: rgb(\"" .. hex .. "\"))[") }
    for _, inline in ipairs(el.content) do
      table.insert(result, inline)
    end
    table.insert(result, pandoc.RawInline("typst", "]"))
    return result
  end

  return el
end
