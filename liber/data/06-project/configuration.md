# Configuración del proyecto Quarto

El archivo `_quarto.yml` es el archivo de configuración principal de un proyecto Quarto. Define el tipo de proyecto, los formatos de salida, el tema y todas las opciones de compilación.

## Estructura de `_quarto.yml`

```yaml
project:
  type: book
  output-dir: _output

book:
  title: "Natura Docens"
  author: "Autores"
  date: today
  chapters:
    - index.qmd
    - part: "Introducción"
      chapters:
        - intro.qmd
    - part: "Contenido"
      chapters:
        - cap1.qmd
        - cap2.qmd
  references: references.qmd

format:
  html:
    theme:
      light: theme-light.scss
      dark: theme-dark.scss
    css: styles.css
    toc: true
    toc-depth: 3
    number-sections: true
    code-fold: false
    code-tools: false
    embed-resources: true
    fig-width: 8
    fig-height: 5
    fig-dpi: 150
  pdf:
    documentclass: scrreprt
    papersize: letter
    fontsize: 11pt
    geometry:
      - top=2.5cm
      - bottom=2.5cm
      - left=2.5cm
      - right=2.5cm
    colorlinks: true
    linkcolor: NavyBlue
    urlcolor: OliveGreen
    toccolor: Black
    header-includes:
      - \usepackage{fancyhdr}
      - \pagestyle{fancy}
    keep-tex: true
  epub:
    css: epub-style.css

filters:
  - _filters/icfes-tables.lua
  - _filters/wide-tables.lua
  - _filters/table-styling.lua
  - _filters/table-zebra.lua
  - _filters/color-sections.lua

include-after-body:
  - _includes/after-body.html

include-in-header:
  - _includes/header.html
  - _includes/analytics.html

execute:
  echo: false
  warning: false
  message: false

mermaid:
  theme: default
```

## Tipo de proyecto: book

```yaml
project:
  type: book
```

El tipo `book` permite organizar el contenido en capítulos, partes y secciones. Quarto genera automáticamente una tabla de contenido y navegación.

## Formatos de salida

### HTML

```yaml
format:
  html:
    theme:
      light: theme-light.scss
      dark: theme-dark.scss
    css: styles.css
    toc: true
    number-sections: true
```

### PDF

```yaml
format:
  pdf:
    documentclass: scrreprt
    papersize: letter
    fontsize: 11pt
```

### EPUB

```yaml
format:
  epub:
    css: epub-style.css
```

## Configuración del tema (LIGHT vs DARK)

Quarto soporta temas claros y oscuros mediante archivos SCSS separados:

```yaml
format:
  html:
    theme:
      light: theme-light.scss
      dark: theme-dark.scss
```

Los archivos SCSS deben contener los marcadores especiales:

```scss
/*-- scss:defaults --*/
// Variables por defecto del tema

$font-family-serif: "Georgia", serif;
$font-family-sans: "Helvetica Neue", sans-serif;
$primary: #2c5282;
$secondary: #2c5282;

/*-- scss:rules --*/
// Reglas CSS personalizadas

body {
  font-family: $font-family-serif;
}
```

### include-after-body e include-in-header

```yaml
include-after-body:
  - _includes/after-body.html   # Se inserta antes del cierre </body>

include-in-header:
  - _includes/header.html       # Se inserta en <head>
  - _includes/analytics.html    # Scripts de analytics, etc.
```

## Filtros

```yaml
filters:
  - _filters/icfes-tables.lua
  - _filters/wide-tables.lua
  - _filters/table-styling.lua
  - _filters/table-zebra.lua
  - _filters/color-sections.lua
```

Los filtros se ejecutan en el orden en que aparecen en la lista.

## Configuración de Mermaid

```yaml
mermaid:
  theme: default    # default, dark, forest, neutral
```

Los diagramas de Mermaid se escriben en el documento así:

````markdown
```{mermaid}
graph LR
    A[Inicio] --> B[Proceso]
    B --> C[Fin]
```
````

## Errores comunes

### Usar `css:` en lugar de `theme:` para SCSS

❌ **Incorrecto:**
```yaml
format:
  html:
    css: theme-light.scss
```

✅ **Correcto:**
```yaml
format:
  html:
    theme:
      light: theme-light.scss
      dark: theme-dark.scss
```

El archivo SCSS va en `theme:`, no en `css:`. La propiedad `css:` es solo para archivos CSS puros.

### Olvidar los marcadores SCSS

❌ **Incorrecto:**
```scss
// Sin marcadores
$primary: #2c5282;

body {
  color: $primary;
}
```

✅ **Correcto:**
```scss
/*-- scss:defaults --*/
$primary: #2c5282;

/*-- scss:rules --*/
body {
  color: $primary;
}
```

Los marcadores `/*-- scss:defaults --*/` y `/*-- scss:rules --*/` son **obligatorios**. Sin ellos, Quarto no puede procesar el archivo SCSS correctamente.

### No entender la cadena de sobrescritura de variables SCSS

El orden de sobrescritura es:

```
flatly (tema base) → quarto (configuración por defecto) → tu archivo SCSS
```

1. **flatly** — El tema base proporciona valores por defecto
2. **quarto** — Quarto aplica su propia configuración
3. **Tu SCSS** — Tus valores sobreescriben los anteriores

Para sobrescribir una variable, debes definirla en la sección `/*-- scss:defaults --*/`:

```scss
/*-- scss:defaults --*/
// Esto sobreescribe el valor de flatly y quarto
$primary: #1a365d;
$font-family-serif: "Literata", serif;
```

### Usar `css:` para temas claros/oscuros

❌ **Incorrecto:**
```yaml
format:
  html:
    css:
      light: theme-light.scss
      dark: theme-dark.scss
```

✅ **Correcto:**
```yaml
format:
  html:
    theme:
      light: theme-light.scss
      dark: theme-dark.scss
```

## Referencia completa de Natura Docens

```yaml
project:
  type: book
  output-dir: _output

book:
  title: "Natura Docens"
  subtitle: "Libro de conocimiento"
  author: "Autores"
  date: today
  chapters:
    - index.qmd
  references: references.qmd

format:
  html:
    theme:
      light: theme-light.scss
      dark: theme-dark.scss
    css: styles.css
    toc: true
    toc-depth: 3
    number-sections: true
    code-fold: false
    embed-resources: true
    fig-width: 8
    fig-height: 5
    fig-dpi: 150
  pdf:
    documentclass: scrreprt
    papersize: letter
    fontsize: 11pt
    geometry:
      - top=2.5cm
      - bottom=2.5cm
      - left=2.5cm
      - right=2.5cm
    colorlinks: true
    linkcolor: NavyBlue
    urlcolor: OliveGreen
    toccolor: Black
    header-includes:
      - \usepackage{fancyhdr}
      - \pagestyle{fancy}
    keep-tex: true
  epub:
    css: epub-style.css

filters:
  - _filters/icfes-tables.lua
  - _filters/wide-tables.lua
  - _filters/table-styling.lua
  - _filters/table-zebra.lua
  - _filters/color-sections.lua

include-after-body:
  - _includes/after-body.html

include-in-header:
  - _includes/header.html
  - _includes/analytics.html

execute:
  echo: false
  warning: false
  message: false

mermaid:
  theme: default
```
