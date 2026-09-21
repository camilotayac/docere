---
title: "Variables SCSS disponibles en Quarto"
description: "Referencia completa de variables SCSS que Quarto expone para personalizar temas HTML"
---

Quarto expone un conjunto de variables SCSS que puedes sobreescribir en la sección `/*-- scss:defaults --*/` de tu archivo de tema. A continuación, la referencia completa organizada por categoría.

## Colores generales

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$body-bg` | color | Color de fondo del body | `#ffffff` |
| `$body-color` | color | Color del texto principal | `#333333` |
| `$link-color` | color | Color de los enlaces | `#2c7be5` |
| `$secondary` | color | Color secundario (botones, etc.) | `#6c757d` |

## Tipografías

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$font-family-sans-serif` | font-stack | Fuente principal | `("Source Sans Pro", sans-serif)` |
| `$font-family-monospace` | font-stack | Fuente para código | `("Fira Code", monospace)` |
| `$font-size-root` | length | Tamaño base de fuente | `1rem` |
| `$font-size-base` | length | Tamaño base relativo | `1rem` |
| `$line-height-base` | number | Altura de línea base | `1.5` |

## Títulos (Headings)

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$h1-font-size` | length | Tamaño de h1 | `2.5rem` |
| `$h2-font-size` | length | Tamaño de h2 | `2rem` |
| `$h3-font-size` | length | Tamaño de h3 | `1.75rem` |
| `$h4-font-size` | length | Tamaño de h4 | `1.5rem` |
| `$h5-font-size` | length | Tamaño de h5 | `1.25rem` |
| `$h6-font-size` | length | Tamaño de h6 | `1rem` |
| `$headings-font-weight` | weight | Peso de los títulos | `700` |
| `$headings-color` | color | Color de los títulos | `inherit` |

## Tabla de contenidos (TOC)

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$toc-color` | color | Color del texto del TOC | `rgba(0,0,0,.65)` |
| `$toc-font-size` | length | Tamaño de fuente del TOC | `0.875rem` |
| `$toc-active-border` | color | Borde del item activo | `$primary` |
| `$toc-active-color` | color | Color del item activo | `$body-color` |

## Sidebar (barras laterales)

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$sidebar-bg` | color | Fondo de la sidebar | `#f8f9fa` |
| `$sidebar-fg` | color | Texto de la sidebar | `$body-color` |
| `$sidebar-font-size` | length | Tamaño de fuente de la sidebar | `0.875rem` |
| `$sidebar-font-size-section` | length | Tamaño de fuente de las secciones | `0.875rem` |

### Variables internas de sidebar (no documentadas oficialmente)

Quarto define internamente variables adicionales para la sidebar que no aparecen en la documentación oficial pero son utilizadas por el CSS generado:

| Variable | Default | Descripción |
|----------|---------|-------------|
| `$sidebar-font-size-section` | `0.875rem` | Tamaño de fuente de las secciones de la sidebar |
| `$sidebar-font-size-collapse` | `1rem` | Tamaño de fuente cuando la sidebar está colapsada |
| `$sidebar-font-size-section-collapse` | `1.1rem` | Tamaño de fuente de las secciones cuando colapsada |

> **Nota**: Estas variables son internas de Quarto y pueden cambiar entre versiones. Úsalas con precaución.

## Navbar (barra de navegación)

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$navbar-bg` | color | Fondo del navbar | `$primary` |
| `$navbar-fg` | color | Texto del navbar | `contrast-color($navbar-bg)` |
| `$navbar-hl` | color | Color de highlight del navbar | `$navbar-fg` |
| `$navbar-padding-y` | length | Padding vertical del navbar | `0.5rem` |

## Footer

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$footer-bg` | color | Fondo del footer | `$body-bg` |
| `$footer-fg` | color | Texto del footer | `$body-color` |

## Código

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$code-block-bg` | color | Fondo de bloques de código | `lighten($body-bg, 5%)` |
| `$code-block-border-left` | color | Borde izquierdo del código | `3px solid $primary` |
| `$code-color` | color | Color del código inline | `#e83e8c` |
| `$code-bg` | color | Fondo del código inline | `rgba(0,0,0,.075)` |

## Layout y espaciado

| Variable | Tipo | Descripción | Ejemplo |
|----------|------|-------------|---------|
| `$content-padding-top` | length | Padding superior del contenido | `3rem` |
| `$content-padding-right` | length | Padding derecho del contenido | `4rem` |
| `$border-radius` | length | Radio de bordes generales | `0.375rem` |
| `$border-radius-lg` | length | Radio de bordes grandes | `0.5rem` |

## Ejemplo de uso completo

```scss
/*-- scss:defaults --*/

// Colores
$body-bg: #fafbfc;
$body-color: #2d3748;
$link-color: #3182ce;

// Tipografía
$font-family-sans-serif: ("Inter", "Source Sans Pro", sans-serif);
$font-size-root: 17px;

// Títulos
$h1-font-size: 2.25rem;
$h2-font-size: 1.75rem;
$h3-font-size: 1.5rem;

// TOC
$toc-font-size: 0.8125rem;
$toc-active-border: #3182ce;

// Sidebar
$sidebar-bg: #f7fafc;
$sidebar-fg: #4a5568;
$sidebar-font-size: 0.8125rem;

// Navbar
$navbar-bg: #2d3748;
$navbar-fg: #ffffff;

// Footer
$footer-bg: #2d3748;
$footer-fg: #e2e8f0;

// Código
$code-block-bg: #f7fafc;
$code-block-border-left: 3px solid #3182ce;

// Layout
$content-padding-top: 2rem;

/*-- scss:rules --*/

// Reglas adicionales personalizadas
.sidebar-title {
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
}
```
