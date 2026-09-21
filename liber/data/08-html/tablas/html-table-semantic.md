---
up:: [[html]]
tags:: [html]
---

# Marcado Semantico de Tablas

## `<colgroup>` y `<col>`

Permiten aplicar estilos a columnas completas sin repetir en cada celda.

```html
<table>
  <colgroup>
    <col class="producto">
    <col class="precio">
  </colgroup>
  <tr>
    <th>Producto</th>
    <th>Precio</th>
  </tr>
</table>
```

## Atributo `scope`

Indica a que celdas aplica un encabezado:

- `scope="col"` — encabezado de columna
- `scope="row"` — encabezado de fila
- `scope="colgroup"` — encabezado de grupo de columnas
- `scope="rowgroup"` — encabezado de grupo de filas

## Atributo `headers`

Asocia celdas de datos con uno o mas encabezados por ID:

```html
<th id="nombre">Nombre</th>
<td headers="nombre">Ana</td>
```

## ARIA para tablas complejas

- `role="table"` — explicita el rol
- `role="rowgroup"` — grupo de filas
- `role="row"` — fila
- `role="columnheader"` / `role="rowheader"` — encabezados
- `role="cell"` — celda

## Mejores practicas

- Usar `scope` antes que `headers`
- Probar con lector de pantalla
- Tablas anidadas solo si es estrictamente necesario

## Enlaces

- [[html-tables]]
- [[html-semantic]]
