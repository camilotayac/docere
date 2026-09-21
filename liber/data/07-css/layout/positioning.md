---
tags: [css, positioning, layout, float]
---
# Posicionamiento

Controla cómo se ubican los elementos en la página y su relación con otros elementos.

## Valores de position

### static (por defecto)

El elemento sigue el flujo normal del documento. `top`, `right`, `bottom`, `left` no tienen efecto.

### relative

Se desplaza desde su posición original **sin** afectar a otros elementos.

```css
.card {
  position: relative;
  top: -10px;  /* se mueve 10px arriba de su posición original */
}
```

### absolute

Se posiciona respecto al contenedor padre con `position: relative` más cercano. Se retira del flujo normal.

```css
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 0;
  right: 0;
}
```

### fixed

Se posiciona respecto al **viewport**. Se retira del flujo y no se mueve al hacer scroll.

```css
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
}
```

### sticky

Funciona como `relative` hasta que alcanza un umbral de scroll, entonces se comporta como `fixed` dentro de su contenedor.

```css
.header {
  position: sticky;
  top: 0;
}
```

## z-index y contexto de apilamiento

`z-index` controla el orden de apilamiento de elementos posicionados (`position` distinto de `static`).

```css
.overlay {
  position: absolute;
  z-index: 10;  /* se muestra por encima */
}
```

> [!note] Contexto de apilamiento
> Un `z-index` solo compara dentro del mismo contexto de apilamiento. Crear un contexto nuevo: `isolation: isolate;`.

## Offset properties

| Propiedad | Efecto |
|-----------|--------|
| `top` | Desplaza desde arriba del contenedor |
| `right` | Desplaza desde la derecha |
| `bottom` | Desplaza desde abajo |
| `left` | Desplaza desde la izquierda |

## Float y clear

`float` saca un elemento del flujo y lo alinea a la izquierda o derecha. Históricamente se usó para layouts, pero ahora se prefiere [[flexbox]] o [[css-grid]].

```css
.image-left {
  float: left;
  margin-right: 1rem;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

> [!tip] Modernidad
> `float` sigue siendo útil para envolver texto alrededor de imágenes, pero no para layouts de página.

## Ver también

- [[html-theming]] — Uso del posicionamiento en plantillas Quarto
- [[flexbox]] — Alternativa moderna para layouts
- [[css-grid]] — Alternativa moderna para layouts complejos
- [[modelo-de-caja]] — Modelo de caja subyacente
