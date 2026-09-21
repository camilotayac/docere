# Filtros en Quarto

Los filtros son transformaciones que se aplican al documento durante la compilación. Modifican el contenido del documento en distintas etapas del pipeline de procesamiento.

## ¿Qué son los filtros?

Un filtro en Quarto es un programa (normalmente escrito en Lua o Python) que recibe el documento en formato **Pandoc AST** (Abstract Syntax Tree) y lo transforma antes de generar la salida final.

```
Documento → [Filtro 1] → [Filtro 2] → ... → Salida final
```

## Pre-filtros vs Post-filters

Quarto distingue dos momentos de ejecución:

| Tipo | Momento | Uso típico |
|------|---------|-------------|
| **Pre-filtro** | Antes del procesamiento de Quarto | Transformaciones generales del AST |
| **Post-filtro** | Después del procesamiento de Quarto | Modificaciones finales antes de la salida |

Se especifican así en el encabezado YAML:

```yaml
filters:
  - mi-filtro.lua        # post-filtro (por defecto)

pre-filters:
  - filtro-previo.lua    # se ejecuta antes
```

## Orden de ejecución

El orden de ejecución es:

1. **Pre-filtros** (en orden de definición)
2. **Procesamiento principal de Quarto** (callouts, crossrefs, etc.)
3. **Post-filtros** (en orden de definición)

Si un filtro aparece en `filters:`, se ejecuta después del procesamiento de Quarto.

## Filtros integrados

Quarto incluye varios filtros predefinidos que se cargan automáticamente:

- `quarto` — el filtro principal de Quarto
- `crossref` — referencias cruzadas
- `citeproc` — procesamiento de citas bibliográficas
- `tablenoteals` — notas de tablas

## Filtros Lua personalizados

Los filtros Lua son la forma más común de crear filtros en Quarto. Son rápidos, portátiles y fáciles de escribir.

Ejemplo básico de un filtro Lua:

```lua
-- filtro-ejemplo.lua
function Pandoc(doc)
  for i, block in ipairs(doc.blocks) do
    if block.t == "Para" then
      -- transformar el párrafo
    end
  end
  return doc
end
```

Los filtros se colocan normalmente en la carpeta `_filters/` del proyecto.

## En Natura Docens

Natura Docens utiliza los siguientes filtros personalizados para el formateado de tablas y secciones:

```yaml
filters:
  - _filters/icfes-tables.lua
  - _filters/wide-tables.lua
  - _filters/table-styling.lua
  - _filters/table-zebra.lua
  - _filters/color-sections.lua
```

- **icfes-tables.lua** — Aplica estilos específicos a las tablas del ICFES
- **wide-tables.lua** — Permite tablas anchas que se desbordan del contenido
- **table-styling.lua** — Estilos generales de tablas (bordes, padding, alineación)
- **table-zebra.lua** — Aplica filas alternas de colores (zebra striping)
- **color-sections.lua** — Colorea las secciones según su nivel
