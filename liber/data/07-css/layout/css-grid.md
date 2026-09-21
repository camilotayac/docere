---
tags: [css, grid, layout]
---
# CSS Grid

Sistema de layout bidimensional para controlar filas y columnas simultáneamente.

## Contenedor grid

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1rem;  /* shorthand para row-gap y column-gap */
}
```

### Unidades útiles

| Unidad | Ejemplo | Descripción |
|--------|---------|-------------|
| `fr` | `1fr 2fr` | Fracción del espacio disponible |
| `repeat()` | `repeat(3, 1fr)` | Repetir patrón |
| `auto-fill` | `repeat(auto-fill, minmax(250px, 1fr))` | Columnas automáticas |
| `minmax()` | `minmax(200px, 1fr)` | Tamaño mínimo y máximo |

### Columnas con auto-fill

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}
```

> [!tip] Responsive sin media queries
> `auto-fill` con `minmax()` crea un layout que se adapta automáticamente al ancho del contenedor.

## Items grid

```css
.item {
  grid-column: 1 / 3;     /* columna inicial / final */
  grid-row: span 2;        /* ocupa 2 filas */
}
```

### Sintaxis abreviada

```css
.item {
  grid-column: 1 / -1;     /* de la primera a la última columna */
  grid-row: 1 / 3;         /* de la fila 1 a la 3 */
}
```

## Áreas con nombre

```css
.layout {
  display: grid;
  grid-template-areas:
    "header  header  header"
    "sidebar content content"
    "footer  footer  footer";
  grid-template-columns: 250px 1fr 1fr;
  grid-template-rows: auto 1fr auto;
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.content { grid-area: content; }
.footer  { grid-area: footer; }
```

## Auto-posicionamiento

Grid coloca automáticamente los items que no tienen posición explícita, llenando celdas vacías de izquierda a derecha.

```css
/* Forzar un item a la siguiente línea */
.item {
  grid-column-start: auto;
}
```

## Ver también

- [[flexbox]] — Layout unidimensional
- [[html-theming]] — Aplicación de grid en plantillas Quarto
- [[modelo-de-caja]] — Modelo de caja subyacente
