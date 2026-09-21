---
tags: [css, flexbox, layout]
---
# Flexbox

Sistema de layout unidimensional para distribuir y alinear elementos dentro de un contenedor.

## Contenedor flex

```css
.container {
  display: flex;
  flex-direction: row;       /* row | row-reverse | column | column-reverse */
  justify-content: center;   /* eje principal */
  align-items: stretch;      /* eje transversal */
  flex-wrap: nowrap;         /* nowrap | wrap | wrap-reverse */
  gap: 1rem;                 /* espacio entre items */
}
```

### justify-content (eje principal)

| Valor | Descripción |
|-------|-------------|
| `flex-start` | Agrupa al inicio |
| `flex-end` | Agrupa al final |
| `center` | Centra los items |
| `space-between` | Espacio igual entre items |
| `space-around` | Espacio igual alrededor |
| `space-evenly` | Espacio uniforme |

### align-items (eje transversal)

| Valor | Descripción |
|-------|-------------|
| `stretch` | Estira para llenar el contenedor |
| `flex-start` | Alinea al inicio |
| `flex-end` | Alinea al final |
| `center` | Centra verticalmente |
| `baseline` | Alinea por la línea de texto |

## Items flex

```css
.item {
  flex-grow: 1;    /* factor de crecimiento */
  flex-shrink: 1;  /* factor de encogimiento */
  flex-basis: 0;   /* tamaño base antes de crecer/encoger */
  order: 0;         /* orden visual */
}
```

Abreviación: `flex: <grow> <shrink> <basis>;`

## Patrones comunes

### Centrado perfecto

```css
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### Navegación horizontal

```css
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

### Tarjetas distribuidas

```css
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.card {
  flex: 1 1 300px; /* crece, encoge, base mínima 300px */
}
```

### Columnas iguales

```css
.columns {
  display: flex;
}

.column {
  flex: 1;
}
```

## Ver también

- [[css-grid]] — Layout bidimensional
- [[html-theming]] — Uso de flexbox en plantillas Quarto
- [[modelo-de-caja]] — Modelo de caja subyacente
