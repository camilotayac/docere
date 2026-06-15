local sectionColors = {
  teoria          = { bg = "e8e8e8", fg = "d0d0d0" },
  ["ideas-previas"] = { bg = "f9ebaf", fg = "e8d68a" },
  contexto        = { bg = "f2c6a0", fg = "e0b088" },
  caracterizados  = { bg = "d6c7e7", fg = "c0b0d8" },
  retos           = { bg = "f6d5a8", fg = "e8c490" },
  socioemocional  = { bg = "f4c8d8", fg = "e0b0c4" },
  ejercicios      = { bg = "b2e0d8", fg = "98ccc4" },
  aplicacion      = { bg = "c5e8d8", fg = "a8d4c4" },
  ejemplo         = { bg = "b3d9f0", fg = "94c4e0" },
  evaluacion      = { bg = "f0c4b8", fg = "dcb0a4" },
}

function Header(el)
  if el.level == 2 then
    for _, cls in ipairs(el.classes) do
      local c = sectionColors[cls]
      if c then
        return {
          pandoc.RawBlock('latex', '\\setcolorsection{' .. c.bg .. '}{' .. c.fg .. '}'),
          el
        }
      end
    end
  end
  return el
end
