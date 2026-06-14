local boxes = {
  ['teoria-box']             = { h='box-teoria-h',             f='box-teoria-f',             heading='Teoría', sub=false },
  ['ideas-previas-box']      = { h='box-ideas-previas-h',      f='box-ideas-previas-f',      heading='Ideas previas', sub=false },
  ['sub-ideas-previas-box']  = { h='box-ideas-previas-h',      f='box-sub-ideas-previas-f',  heading='', sub=true },
  ['contexto-box']           = { h='box-contexto-h',           f='box-contexto-f',           heading='Contextualización', sub=false },
  ['sub-contexto-box']       = { h='box-contexto-h',           f='box-sub-contexto-f',       heading='', sub=true },
  ['caracterizados-box']     = { h='box-caracterizados-h',     f='box-caracterizados-f',     heading='Contextualización para caracterizados', sub=false },
  ['sub-caracterizados-box'] = { h='box-caracterizados-h',     f='box-sub-caracterizados-f', heading='', sub=true },
  ['retos-box']              = { h='box-retos-h',              f='box-retos-f',              heading='Retos', sub=false },
  ['socioemocional-box']     = { h='box-socioemocional-h',     f='box-socioemocional-f',     heading='Socioemocional', sub=false },
  ['ejercicios-box']         = { h='box-ejercicios-h',         f='box-ejercicios-f',         heading='Ejercicios', sub=false },
  ['aplicacion-box']         = { h='box-aplicacion-h',         f='box-aplicacion-f',         heading='Aplicación', sub=false },
  ['sub-aplicacion-box']     = { h='box-aplicacion-h',         f='box-sub-aplicacion-f',     heading='', sub=true },
  ['ejemplo-box']            = { h='box-ejemplo-h',            f='box-ejemplo-f',            heading='Ejemplo', sub=false },
  ['evaluacion-box']         = { h='box-evaluacion-h',         f='box-evaluacion-f',         heading='Evaluación', sub=false },
  ['sub-evaluacion-box']     = { h='box-evaluacion-h',         f='box-sub-evaluacion-f',     heading='Socialización', sub=true },
  ['notas-docente-box']      = { h='box-notas-docente-h',      f='box-notas-docente-f',      heading='Notas para el docente', sub=false },
}

local function slugify(text)
  if text == '' then return '' end
  return text:lower()
    :gsub('[áàäâã]', 'a'):gsub('[éèëê]', 'e')
    :gsub('[íìïî]', 'i'):gsub('[óòöôõ]', 'o')
    :gsub('[úùüû]', 'u'):gsub('[ñ]', 'n')
    :gsub('[^%w%s%-]', ''):gsub('%s+', '-')
    :gsub('%-+', '-'):gsub('^%-+', ''):gsub('%-+$', '')
end

local box_counter = 0

local function make_heading_collapsible(div, cls, box, collapse_id, start_collapsed)
  local title_text = div.attributes['title'] or box.heading or ''
  local anchor_id = slugify(title_text)
  local heading_cls = cls .. '-heading'
  
  local classes = { heading_cls, 'unlisted' }
  if start_collapsed then
    table.insert(classes, 'collapsed')
  end
  
  local attributes = {
    ['data-bs-toggle'] = 'collapse',
    ['data-bs-target'] = '#' .. collapse_id,
    ['aria-expanded'] = start_collapsed and 'false' or 'true',
    ['aria-controls'] = collapse_id
  }
  
  local attr = pandoc.Attr(anchor_id, classes, attributes)
  local level = box.sub and 3 or 2
  return pandoc.Header(level, {pandoc.Str(title_text)}, attr)
end

local function make_heading(div, cls, box)
  local title_text = div.attributes['title'] or box.heading or ''
  local anchor_id = slugify(title_text)
  local heading_cls = cls .. '-heading'
  local attr = pandoc.Attr(anchor_id, {heading_cls, 'unlisted'}, {})
  local level = box.sub and 3 or 2
  return pandoc.Header(level, {pandoc.Str(title_text)}, attr)
end

function Div(div)
  for _, cls in ipairs(div.classes) do
    local box = boxes[cls]
    if box then
      local title = div.attributes['title'] or box.heading or ''

      if FORMAT:match('latex') then
        local cmd = string.format(
          '\\begin{educativebox}[title={%s}]{%s}{%s}',
          title, box.h, box.f
        )
        local begin_raw = pandoc.RawBlock('latex', cmd)
        local end_raw = pandoc.RawBlock('latex', '\\end{educativebox}')
        div.content:insert(1, begin_raw)
        div.content:insert(end_raw)
        return div.content
      end

      if FORMAT:match('html') then
        box_counter = box_counter + 1
        local collapse_id = 'box-collapse-' .. box_counter
        
        local collapse_attr = div.attributes['collapse']
        local start_collapsed = true
        if collapse_attr == 'false' then
          start_collapsed = false
        end
        
        local heading = make_heading_collapsible(div, cls, box, collapse_id, start_collapsed)
        
        local original_content = {}
        for _, block in ipairs(div.content) do
          table.insert(original_content, block)
        end
        
        local body_classes = { 'collapse' }
        if not start_collapsed then
          table.insert(body_classes, 'show')
        end
        
        local body_attr = pandoc.Attr(collapse_id, body_classes, {})
        local body_div = pandoc.Div(original_content, body_attr)
        
        div.content = pandoc.List()
        div.content:insert(heading)
        div.content:insert(body_div)
        
        div.classes:insert(cls .. '-section')
        return div
      end

      local heading = make_heading(div, cls, box)
      div.classes:insert(cls .. '-section')
      div.content:insert(1, heading)
      return div
    end
  end
end
