---
title: "Estructura de libros"
subtitle: "Organización de partes, capítulos y navegación"
categories:
  - "libros"
  - "estructura"
tags:
  - "sidebar"
  - "navegación"
  - "cross-references"
---

La estructura de un libro en Quarto determina cómo se organiza el contenido y cómo los lectores navegan entre secciones.

## Partes vs Capítulos vs Apéndices

| Elemento | Propósito | Numeración |
|----------|-----------|------------|
| **Parte** | Agrupa capítulos temáticos |罗马 numerals (I, II, III) |
| **Capítulo** | Unidad principal de contenido | Cap. 1, 2, 3... |
| **Apéndice** | Material complementario | App. A, B, C... |

### Ejemplo de jerarquía

```yaml
book:
  chapters:
    - index.qmd
    - part: "Primera Parte"
      chapters:
        - cap1.qmd
        - cap2.qmd
    - part: "Segunda Parte"
      chapters:
        - cap3.qmd
        - cap4.qmd
  appendices:
    - apendice-a.qmd
```

## Configuración de la barra lateral (`sidebar:`)

La barra lateral controla la navegación en libros HTML:

```yaml
book:
  sidebar:
    style: "floating"
    collapse-level: 2
    search: true
```

### Opciones de estilo de sidebar

| Estilo | Descripción |
|--------|-------------|
| `floating` | Se mantiene visible al hacer scroll |
| `docked` | Se adjunta al lado de la página |
| `none` | Sin barra lateral |

### Nivel de colapso (`collapse-level`)

Controla cuántos niveles de secciones se muestran colapsados:

```yaml
sidebar:
  collapse-level: 2  # Colapsa subsecciones de nivel 2
```

- `1`: Muestra solo títulos principales
- `2`: Muestra títulos y subsecciones
- `3`: Muestra hasta tres niveles de profundidad

## Estructura de navegación

La navegación incluye automáticamente:

- **Anterior/Siguiente**: Enlaces entre capítulos
- **Índice**: Volver a la tabla de contenido
- **Barra de búsqueda**: Para libros HTML con `search: true`
- **Números de página**: En formatos PDF

### Navegación personalizada

```yaml
book:
  navbar:
    logo: "images/logo.png"
    logo-alt: "Logo del libro"
    right:
      - href: "https://github.com/usuario/libro"
        text: "GitHub"
```

## Cross-references entre capítulos

Quarto permite referencias cruzadas entre capítulos de un libro:

### Referencias a secciones

```markdown
Ver la [[#metodos]] para más detalles.

## Métodos {#metodos}
```

### Referencias a figuras

```markdown
Como se muestra en @fig-resultados-1, los resultados...

```{r}
#| label: fig-resultados-1
#| fig-cap: "Resultados del análisis"
plot(1:10)
```
```

### Referencias a tablas

```markdown
La @tbl-datos muestra los datos recopilados.

```{r}
#| label: tbl-datos
#| tbl-cap: "Datos del estudio"
knitr::kable(head(mtcars))
```
```

## Capítulos de tipo `index.qmd`

El archivo `index.qmd` funciona como página de inicio del libro:

```markdown
---
title: "Mi Libro"
subtitle: "Una introducción práctica"
---

# Bienvenido

Este libro cubre los fundamentos de...
```

## Partes con contenido

Las partes pueden incluir contenido introductorio:

```yaml
book:
  chapters:
    - part: "Fundamentos"
      content: ""
      chapters:
        - intro.qmd
        - conceptos.qmd
```

Esto genera una página de título para cada parte.

## Organización de archivos

La estructura recomendada de archivos para un libro:

```
libro/
├── _quarto.yml
├── index.qmd
├── chapters/
│   ├── 01-intro.qmd
│   ├── 02-fundamentos.qmd
│   └── 03-aplicaciones.qmd
├── images/
│   ├── cover.png
│   └── figuras/
└── references.bib
```

## Véase también

- [[creating-books]] - Creación inicial de libros
- [[cross-references]] - Sistema de referencias cruzadas
- [[customizing-output]] - Personalización de formatos