---
title: Fondos y bordes en CSS
tags: [css, colores, fondos, bordes]
aliases: [fondos, bordes, background, border]
---

## background-color

Define el color de fondo de un elemento:

```css
body {
  background-color: #f8fafc;
}

.card {
  background-color: white;
}

.hero {
  background-color: hsl(217, 91%, 60%);
}
```

Acepta cualquier formato de color: nombre, HEX, RGB, HSL, con o sin transparencia.

## background-image

Aplica una imagen como fondo de un elemento:

```css
.hero {
  background-image: url('/images/hero.webp');
}

.pattern {
  background-image: url('/images/pattern.svg');
}

.gradient {
  background-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Degradados

```css
/* Degradado lineal */
.card {
  background: linear-gradient(to right, #f97316, #ea580c);
}

/* Degradado radial */
.bubble {
  background: radial-gradient(circle, #fff 0%, #ddd 100%);
}

/* Degradado cónico */
.conic {
  background: conic-gradient(red, orange, yellow, red);
}
```

> [!tip] Múltiples fondos
> Se pueden superponer varias imágenes separadas por comas. La primera se dibuja encima:

```css
.layered {
  background-image: url('overlay.png'), url('base.jpg');
  background-position: center, center;
  background-size: contain, cover;
}
```

## background-size

Controla el tamaño de la imagen de fondo:

```css
.hero {
  background-size: cover;          /* cubre todo el contenedor */
}

.avatar {
  background-size: contain;        /* ajusta sin recortar */
}

.tile {
  background-size: 100px 100px;    /* tamaño fijo */
}

.stretch {
  background-size: 100% 100%;      /* estira al contenedor */
}
```

| Valor | Descripción |
|---|---|
| `cover` | Cubre todo el área, puede recortar |
| `contain` | Ajusta sin recortar, puede dejar espacios |
| `<length>` | Tamaño fijo (px, em, rem) |
| `<percentage>` | Porcentaje del contenedor |

## background-position

Posiciona la imagen de fondo dentro del contenedor:

```css
.hero {
  background-position: center center;
}

.corner {
  background-position: top right;
}

.custom {
  background-position: 30% 70%;
}
```

Valores comunes: `center`, `top`, `bottom`, `left`, `right`, combinaciones de ellos, o valores absolutos/porcentuales.

## background-repeat

Controla si la imagen se repite:

```css
.pattern {
  background-repeat: repeat;       /* repite en ambas direcciones (default) */
}

.no-repeat {
  background-repeat: no-repeat;    /* no repite */
}

.horizontal {
  background-repeat: repeat-x;    /* repite solo horizontalmente */
}

.vertical {
  background-repeat: repeat-y;    /* repite solo verticalmente */
}

.mosaic {
  background-repeat: round;        /* ajusta el tamaño para encajar sin cortar */
}
```

## shorthand: background

Combinación de todas las propiedades de fondo en una sola declaración:

```css
.hero {
  background: url('/images/hero.webp') center/cover no-repeat;
}

.gradient-bg {
  background: linear-gradient(135deg, #667eea, #764ba2) center/cover no-repeat;
}
```

Formato: `background: color image position / size repeat attachment;`

## Propiedades de borde

### border-width, border-style, border-color

Las tres propiedades fundamentales de un borde:

```css
.card {
  border-width: 1px;
  border-style: solid;
  border-color: #e5e7eb;
}
```

> [!warning] Requisito mínimo
> Sin `border-style`, el borde no se muestra. `border-style: solid` es el más usado.

Estilos de borde disponibles:
- `solid` — línea continua
- `dashed` — guiones
- `dotted` — puntos
- `double` — línea doble
- `groove` / `ridge` — efecto 3D
- `inset` / `outset` — efecto de relieve

### border shorthand

```css
.card {
  border: 1px solid #e5e7eb;
}
```

Formato: `border: width style color;`

### Bordes individuales por lado

```css
.card {
  border-top: 2px solid #2563eb;
  border-right: 1px solid #e5e7eb;
  border-bottom: 2px solid #2563eb;
  border-left: 1px solid #e5e7eb;
}
```

O con la propiedad lógica:

```css
.card {
  border-inline: 1px solid #e5e7eb;    /* left + right en LTR */
  border-block: 2px solid #2563eb;     /* top + bottom */
}
```

## border-radius

Redondea las esquinas de un elemento:

```css
.card {
  border-radius: 8px;
}

.badge {
  border-radius: 9999px;    /* forma de pastilla */
}

.circle {
  width: 100px;
  height: 100px;
  border-radius: 50%;       /* círculo perfecto */
}
```

Valores individuales por esquina:

```css
.card {
  border-radius: 12px 12px 0 0;   /* solo esquinas superiores */
}
```

Shorthand completo: `border-radius: top-left top-right bottom-right bottom-left;`

### Radios elípticos

```css
.elipse {
  border-radius: 50% / 25%;   /* horizontal / vertical */
}
```

## box-shadow

Agrega sombras a un elemento para crear profundidad:

```css
.card {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.card-elevated {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
              0 2px 4px -2px rgba(0, 0, 0, 0.1);
}

.floating {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
              0 8px 10px -6px rgba(0, 0, 0, 0.1);
}
```

Sintaxis: `offset-x offset-y blur-radius spread-radius color`

| Parámetro | Descripción |
|---|---|
| `offset-x` | Desplazamiento horizontal (requerido) |
| `offset-y` | Desplazamiento vertical (requerido) |
| `blur-radius` | Desenfoque (mayor = sombra más difusa) |
| `spread-radius` | Expansión de la sombra |
| `inset` | Sombra interna |

### Sombras internas

```css
.inset-card {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.15);
}
```

### Múltiples sombras

Se apilan declaraciones para efectos realistas:

```css
.realistic-shadow {
  box-shadow:
    0 1px 1px rgba(0,0,0,0.08),
    0 2px 2px rgba(0,0,0,0.08),
    0 4px 4px rgba(0,0,0,0.08),
    0 8px 8px rgba(0,0,0,0.08);
}
```

## outline

Similar a `border` pero no ocupa espacio en el layout. Se usa principalmente para **estados de foco**:

```css
a:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}
```

> [!tip] outline-offset
> Separa el outline del borde del elemento. Útil para indicadores de accesibilidad sin alterar el diseño.

## Conexión con Quarto

Los fondos y bordes se integran en el sistema de theming de Quarto:

- **[[html-theming]]**: El theming de Quarto usa variables de Bootstrap para controlar fondos, bordes y sombras a nivel de sitio.
- **[[scss-variables]]**: Variables como `$card-bg`, `$card-border-color`, `$border-radius` y `$box-shadow` configuran estos estilos globalmente.

```scss
// Variables Quarto para fondos y bordes
$body-bg: #ffffff;
$card-bg: #f8fafc;
$card-border-color: #e5e7eb;
$border-radius: 8px;
$box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
```

> [!note] Bootstrap 5
> Quarto usa Bootstrap 5 como base. Las variables SCSS de Bootstrap pueden redefinirse en el custom SCSS del proyecto.
