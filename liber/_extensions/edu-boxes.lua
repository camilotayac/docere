-- edu-boxes.lua
-- Convierte fenced divs con clases específicas a entornos tcolorbox en PDF
-- y aplica clases CSS personalizadas en HTML.
-- También genera headings (h2/h3) para que los boxes aparezcan en el TOC.

local mapping = {
  ['teoria-box']              = 'teoriabox',
  ['ideas-previas-box']       = 'ideaspreviasbox',
  ['sub-ideas-previas-box']   = 'subideaspreviasbox',
  ['contexto-box']            = 'contextobox',
  ['sub-contexto-box']        = 'subcontextobox',
  ['caracterizados-box']      = 'caracterizacioncaracterizadosbox',
  ['sub-caracterizados-box']  = 'subcaracterizadosbox',
  ['retos-box']               = 'retosbox',
  ['socioemocional-box']      = 'socioemocionalbox',
  ['ejercicios-box']          = 'ejerciciosbox',
  ['aplicacion-box']          = 'aplicacionbox',
  ['sub-aplicacion-box']      = 'subaplicacionbox',
  ['ejemplo-box']             = 'ejemplobox',
  ['evaluacion-box']          = 'evaluacionbox',
  ['sub-evaluacion-box']      = 'subevaluacionbox',
  ['notas-docente-box']       = 'notasdocente',
}

local box_headings = {
  ['teoria-box']             = 'Teoría',
  ['ideas-previas-box']      = 'Ideas previas',
  ['contexto-box']           = 'Contextualización',
  ['caracterizados-box']     = 'Contextualización para caracterizados',
  ['retos-box']              = 'Retos',
  ['socioemocional-box']     = 'Socioemocional',
  ['ejercicios-box']         = 'Ejercicios',
  ['aplicacion-box']         = 'Aplicación',
  ['ejemplo-box']            = 'Ejemplo',
  ['evaluacion-box']         = 'Evaluación',
  ['sub-evaluacion-box']     = 'Socialización',
  ['notas-docente-box']      = 'Notas para el docente',
}

-- Genera un ID de ancla válido desde el texto del título
local function slugify(text)
  return text:lower()
    :gsub('[áàäâã]', 'a'):gsub('[éèëê]', 'e')
    :gsub('[íìïî]', 'i'):gsub('[óòöôõ]', 'o')
    :gsub('[úùüû]', 'u'):gsub('[ñ]', 'n')
    :gsub('[^%w%s%-]', ''):gsub('%s+', '-')
    :gsub('%-+', '-'):gsub('^%-+', ''):gsub('%-+$', '')
end

local function make_heading(div, cls, text)
  local title_text = div.attributes['title'] or text or ''
  local heading_class = cls .. '-heading'
  local anchor_id = slugify(title_text)
  local attr = pandoc.Attr(anchor_id, {heading_class}, {})
  if cls:match('^sub%-') then
    return pandoc.Header(3, {pandoc.Str(title_text)}, attr)
  end
  return pandoc.Header(2, {pandoc.Str(title_text)}, attr)
end

function Div(div)
  for _, cls in ipairs(div.classes) do
    local env = mapping[cls]
    if env then
      local heading = make_heading(div, cls, box_headings[cls])

      if FORMAT:match('latex') then
        local title = div.attributes['title']
        local begin_cmd
        if title then
          begin_cmd = '\\begin{' .. env .. '}[title={' .. title .. '}]'
        else
          begin_cmd = '\\begin{' .. env .. '}'
        end
        local begin_raw = pandoc.RawBlock('latex', begin_cmd)
        local end_raw   = pandoc.RawBlock('latex', '\\end{' .. env .. '}')
        div.content:insert(1, begin_raw)
        div.content:insert(end_raw)
        return div.content  -- Solo la caja, el título ya está en el tcolorbox
      end

      return {heading, div}
    end
  end
end
