---
up:: [[html]]
tags:: [html]
---

# Tablas HTML

## Estructura basica

```html
<table>
  <caption>Ventas trimestrales</caption>
  <thead>
    <tr>
      <th scope="col">Trimestre</th>
      <th scope="col">Ingresos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Q1</td>
      <td>$10,000</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>$30,000</td>
    </tr>
  </tfoot>
</table>
```

## Elementos

| Elemento | Proposito |
|----------|-----------|
| `<table>` | Contenedor de la tabla |
| `<thead>` | Encabezados |
| `<tbody>` | Cuerpo de datos |
| `<tfoot>` | Pie o resumen |
| `<tr>` | Fila |
| `<th>` | Celda de encabezado |
| `<td>` | Celda de dato |

## Atributos de union

- `colspan` — fusiona columnas
- `rowspan` — fusiona filas
- `scope` — define alcance del encabezado (`col`, `row`, `colgroup`, `rowgroup`)

## Accesibilidad

- Usar `<caption>` para describir la tabla
- `scope` en `<th>` para lectores de pantalla
- Evitar tablas para maquetacion

## Tablas en Quarto

En Quarto, las tablas Markdown se convierten a `<table>` HTML automaticamente.

## Enlaces

- [[html-semantic]]
- [[html-attributes]]
