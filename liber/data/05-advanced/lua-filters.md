# Filtros Lua en Quarto

Los filtros Lua permiten manipular el **AST de Pandoc** de forma eficiente. Son scripts que se ejecutan durante la compilación y transforman el contenido del documento.

## Sintaxis básica de un filtro Lua

Un filtro Lua es un archivo `.lua` que define funciones con nombres que corresponden a tipos de elementos del AST:

```lua
-- Esta función se ejecuta para cada elemento "Div"
function Div(el)
  -- transformar el elemento
  return el
end

-- Esta función se ejecuta una sola vez al final
function Pandoc(doc)
  return doc
end
```

## Manipulación del AST de Pandoc

### Tipos de elementos comunes

| Tipo | Descripción |
|------|-------------|
| `Pandoc` | Documento completo |
| `BlockQuote` | Cita en bloque |
| `BulletList` | Lista con viñetas |
| `CodeBlock` | Bloque de código |
| `Div` | Elemento `<div>` |
| `Header` | Encabezado (h1-h6) |
| `LineBlock` | Bloque de líneas |
| `OrderedList` | Lista numerada |
| `Para` | Párrafo |
| `RawBlock` | Contenido crudo (HTML, LaTeX) |
| `Table` | Tabla |
| `Span` | Elemento `<span>` inline |

### Estructura de un elemento

Cada elemento del AST tiene:

- `t` — el tipo del elemento (string)
- `attr` — atributos (id, clases, atributos clave-valor)
- `content` — contenido del elemento (varía según el tipo)

## Patrones comunes

### Transformar un Div

```lua
function Div(el)
  -- Verificar si tiene una clase específica
  if el.classes:includes("mi-clase") then
    -- Agregar una clase adicional
    el.classes:insert("clase-extra")
    
    -- Modificar atributos
    el.attr = pandoc.Attr("nuevo-id", el.classes, {{"key", "value"}})
  end
  return el
end
```

### Transformar un Span

```lua
function Span(el)
  if el.classes:includes("resaltado") then
    -- Envolver en negrita
    return pandoc.Span(
      pandoc.Inline({pandoc.Strong(el.content)}),
      el.attr
    )
  end
  return el
end
```

### Transformar una Tabla

```lua
function Table(el)
  -- Agregar una clase a la tabla
  el.attr = pandoc.Attr("", {"tabla-estilizada"}, {})
  
  -- Recorrer filas
  for _, row in ipairs(el.rows) do
    for _, cell in ipairs(row) do
      -- Modificar cada celda
    end
  end
  
  return el
end
```

### Transformar un Header

```lua
function Header(el)
  -- Cambiar el nivel del encabezado
  if el.level == 1 then
    el.level = 2
  end
  return el
end
```

## Filtrado condicional

```lua
function Para(el)
  -- Solo procesar párrafos dentro de cierto div
  if el.classes:includes("solo-para-web") then
    if FORMAT == "latex" then
      return {}  -- eliminar en PDF
    end
  end
  return el
end
```

La variable `FORMAT` permite detectar el formato de salida: `"html"`, `"latex"`, `"epub"`, etc.

## Funciones auxiliares de Pandoc

```lua
-- Crear nuevos elementos
pandoc.Str("texto")
pandoc.Strong({pandoc.Str("negrita")})
pandoc.Emph({pandoc.Str("cursiva")})
pandoc.Code("código en línea")
pandoc.Span({pandoc.Str("contenido")}, pandoc.Attr("", {"clase"}))
pandoc.Div({pandoc.Para({pandoc.Str("contenido")})}, pandoc.Attr("id", {"clase"}))

-- Crear atributos
pandoc.Attr("id", {"clase1", "clase2"}, {{"atributo", "valor"}})
```

## Ejemplo: icfes-tables.lua

El filtro `icfes-tables.lua` de Natura Docens transforma las tablas del ICFES para aplicar estilos específicos. Aquí se muestra la lógica general:

```lua
-- icfes-tables.lua
-- Transforma tablas del ICFES con estilos específicos

function Table(el)
  -- Verificar si la tabla tiene la clase "icfes"
  if el.attr and el.attr.classes:includes("icfes") then
    -- Agregar clase de estilizado
    el.attr.classes:insert("tabla-icfes")
    
    -- Estilizar encabezados
    if el.head then
      for _, row in ipairs(el.head.rows) do
        for _, cell in ipairs(row) do
          cell.attr = cell.attr or pandoc.Attr("", {"th-icfes"}, {})
        end
      end
    end
    
    -- Estilizar filas del cuerpo
    if el.bodies and #el.bodies > 0 then
      for _, body in ipairs(el.bodies) do
        for i, row in ipairs(body.rows) do
          -- Aplicar clase de fila alternada
          local clase = i % 2 == 0 and "fila-par" or "fila-impar"
          for _, cell in ipairs(row) do
            cell.attr = cell.attr or pandoc.Attr("", {clase}, {})
          end
        end
      end
    end
  end
  return el
end

return {
  {Table = Table}
}
```

## Errores comunes

1. **Olvidar `return el`** — Si no devuelves el elemento, se elimina del documento
2. **No verificar el tipo** — Asegúrate de que el elemento es del tipo esperado antes de manipularlo
3. **Mutación incorrecta** — Algunas propiedades son inmutables; crea nuevos elementos en su lugar
4. **Olvidar `return` al final** — El archivo debe retornar la tabla de funciones

## Recursos

- [Documentación de filtros Lua de Pandoc](https://pandoc.org/lua-filters.html)
- [Guía de Quarto sobre filtros](https://quarto.org/docs/extensions/lua-filters.html)
