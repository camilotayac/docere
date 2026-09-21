---
title: "Personalización de salida"
subtitle: "Opciones específicas para HTML, PDF y EPUB"
categories:
  - "libros"
  - "formatos"
tags:
  - "html"
  - "pdf"
  - "epub"
  - "filtros"
---

Cada formato de salida en libros Quarto tiene opciones específicas de configuración en `_quarto.yml`.

## Opciones específicas por formato

### Formato HTML

```yaml
format:
  html:
    theme:
      light: cosmo
      dark: darkly
    css: styles.css
    toc: true
    toc-depth: 3
    number-sections: true
    code-fold: true
    code-tools: true
    code-line-numbers: true
    highlight-style: github
    fig-width: 8
    fig-height: 5
    fig-dpi: 150
```

### Formato PDF

```yaml
format:
  pdf:
    documentclass: scrbook
    classoption:
      - 12pt
      - a4paper
      - openright
    colorlinks: true
    linkcolor: blue
    urlcolor: blue
    citecolor: green
    include-in-header:
      - preamble.tex
    header-includes:
      - \usepackage{fancyhdr}
      - \pagestyle{fancy}
```

### Formato EPUB

```yaml
format:
  epub:
    css: epub.css
    math-method: mathjax
    toc: true
    toc-depth: 2
    fig-width: 6
    fig-height: 4
    metadata:
      description: "Descripción del libro para tiendas"
      subject: "Categoría del libro"
```

## Opciones PDF detalladas

### Clase de documento (`documentclass`)

| Clase | Descripción |
|-------|-------------|
| `book` | Clase estándar para libros |
| `scrbook` | KOMA-Script, más opciones |
| `memoir` | Clase versátil con muchas funciones |

### Opciones de clase (`classoption`)

```yaml
classoption:
  - 12pt          # Tamaño de fuente
  - a4paper       # Tamaño de papel
  - openright      # Capítulos en páginas impares
  - twoside        # Formato a dos páginas
  - landscape      # Orientación apaisada
```

### Colores de enlaces

```yaml
colorlinks: true
linkcolor: red
urlcolor: blue
citecolor: olive
filecolor: magenta
```

### Archivo preámbulo (`preamble.tex`)

Incluye definiciones LaTeX personalizadas:

```tex
% preamble.tex
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{hyperref}

\newcommand{\vect}[1]{\mathbf{#1}}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}
  {\chaptertitlename\ \thechapter}
  {20pt}
  {\Huge}
```

## Opciones EPUB detalladas

### Hoja de estilo personalizada (`css`)

```css
/* epub.css */
body {
  font-family: Georgia, serif;
  line-height: 1.6;
  margin: 1em;
}

h1 {
  text-align: center;
  margin-top: 2em;
}

img {
  max-width: 100%;
  height: auto;
}
```

### Métodos matemáticos

```yaml
math-method:
  mathjax: true        # MathJax para HTML
  webtex: true         # WebTeX como alternativa
  katex: true          # KaTeX para renderizado rápido
```

### Metadatos del libro

```yaml
metadata:
  title: "Mi Libro"
  author: "Autor"
  language: es
  date: "2024-01-01"
  description: "Descripción para tiendas de ebooks"
  subject: "Categoría"
  rights: "© 2024 Autor"
```

## Filtros por formato

Los filtros se aplican selectivamente por formato:

```yaml
filters:
  - filter1.lua
  - filter2.lua

format:
  pdf:
    filters:
      - filter-pdf.lua
  html:
    filters:
      - filter-html.lua
```

### Ejemplo de filtro Lua para PDF

```lua
-- filter-pdf.lua
function Pandoc(doc)
  -- Agregar paquetes LaTeX
  if FORMAT == "pdf" then
    table.insert(doc.meta.header_includes, 
      pandoc.MetaBlocks("\\usepackage{booktabs}"))
  end
  return doc
end
```

## Archivos de inclusión

### Para PDF

```yaml
format:
  pdf:
    include-in-header:
      - preamble.tex
    include-before-body:
      - header.tex
    include-after-body:
      - footer.tex
```

### Para HTML

```yaml
format:
  html:
    include-in-header:
      - analytics.html
    include-before-body:
      - navbar.html
    include-after-body:
      - footer.html
```

## Configuración de figuras y tablas

```yaml
format:
  pdf:
    fig-width: 6
    fig-height: 4
    fig-dpi: 300
    table-width: "0.8\\textwidth"
  html:
    fig-width: 8
    fig-height: 5
    fig-dpi: 96
```

## Véase también

- [[creating-books]] - Configuración inicial del libro
- [[html-theming]] - Temas para formato HTML
- [[markdown-basics]] - Sintaxis de Markdown