---
title: Tu primer documento Quarto
description: Cómo crear, configurar y renderizar tu primer documento .qmd
---

# Tu primer documento Quarto

## Crear un archivo `.qmd`

Un documento Quarto tiene extensión `.qmd` (Quarto Markdown). Es un archivo de texto plano que combina **Markdown**, **YAML** y **bloques de código ejecutable**.

Crea un archivo llamado `hola.qmd`:

```bash
touch hola.qmd
```

## YAML front matter

El YAML front matter va al inicio del archivo, delimitado por `---`. Define metadatos y opciones de renderizado:

```yaml
---
title: Mi primer documento
author: Tu nombre
date: today
format: html
---
```

### Campos esenciales

| Campo | Descripción |
|---|---|
| `title` | Título del documento |
| `author` | Nombre del autor |
| `date` | Fecha (`today` para fecha automática) |
| `format` | Formato de salida (`html`, `pdf`, `epub`) |
| `lang` | Idioma del documento (ej. `es`) |
| `toc` | Tabla de contenidos (`true` / `false`) |
| `number-sections` | Numeración de secciones |

### Múltiples formatos

Puedes especificar varios formatos a la vez:

```yaml
---
title: Mi documento
format:
  html:
    toc: true
    theme: cosmo
  pdf:
    documentclass: article
    geometry: margin=1in
  epub:
    toc: true
---
```

Ver [[html-theming]] para opciones de personalización visual.

## Contenido Markdown

Debajo del YAML, escribe en Markdown estándar con algunas extensiones de Quarto:

```markdown
## Introducción

Este es un párrafo con **negrita** y *cursiva*.

### Subsección

- Lista con viñetas
- Segundo elemento
  - Elemento anidado

> Una cita en bloque

Un enlace a [Quarto](https://quarto.org).
```

### Llamadas (Callouts)

```markdown
::: {.callout-note}
Esto es una nota informativa.
:::

::: {.callout-warning}
Esto es una advertencia.
:::
```

## Bloques de código

Los bloques de código se crean con triples backticks y la opción `#|` para cabeceras de chunk:

````markdown
```{{python}}
import pandas as pd
pd.read_csv("datos.csv").head()
```
````

O en R:

````markdown
```{{r}}
summary(mtcars)
```
````

> **Natura Docens:** Los documentos de este proyecto pueden incluir código ejecutable o no. Si el código no necesita ejecutarse, simplemente omite el chunk de ejecución.

## Renderizar con `quarto render`

```bash
quarto render hola.qmd
```

Este comando:

1. Lee el YAML front matter
2. Ejecuta los bloques de código (si existen)
3. Procesa el Markdown
4. Genera el archivo de salida en el formato especificado

El resultado se guarda en el mismo directorio: `hola.html`, `hola.pdf` o `hola.epub`.

### Renderizar a un formato específico

```bash
quarto render hola.qmd --to html
quarto render hola.qmd --to pdf
```

### Renderizar todo el proyecto

Si existe un `_quarto.yml`, puedes renderizar todo el proyecto desde la raíz:

```bash
quarto render
```

## Vista previa con `quarto preview`

```bash
quarto preview hola.qmd
```

Abre el navegador con una vista previa en vivo. Cada vez que guardas el archivo `.qmd`, el navegador se actualiza automáticamente. Presiona `Ctrl+C` en la terminal para detenerlo.

## Formatos de salida

Ver [[output-formats]] para una guía completa. En resumen:

- **HTML** — ideal para publicación web, rápido y flexible
- **PDF** — requiere una instalación de LaTeX (Quarto puede instalar TinyTeX automáticamente)
- **EPUB** — formato para lectores electrónicos

## Ejemplo completo

Un documento mínimo pero funcional:

```yaml
---
title: Notas de Física Cuántica
author: María García
date: today
lang: es
format:
  html:
    toc: true
    theme: cosmo
  pdf:
    documentclass: article
  epub:
    toc: true
---
```

```markdown
## Ondas electromagnéticas

Las ondas electromagnéticas se propagan a la velocidad de la luz en el vacío.

::: {.callout-tip}
Recuerda: $c = 3 \times 10^8$ m/s
:::

## Referencias

- Griffiths, D. J. *Introduction to Quantum Mechanics*.
```

## El `_quarto.yml` de Natura Docens

El archivo de configuración del proyecto define cómo se construyen todos los documentos:

```yaml
project:
  type: book

book:
  title: "Natura Docens"
  author: "Colectivo Natura Docens"
  date: today
  language: es
  chapters:
    - index.qmd
    - part: "Introducción"
      chapters:
        - 01-getting-started/instalacion.qmd
        - 01-getting-started/primer-documento.qmd

format:
  html:
    theme:
      light: cosmo
      dark: darkly
    toc: true
    number-sections: true
  pdf:
    documentclass: scrreprt
    papersize: a4
    geometry:
      - margin=2.5cm
  epub:
    toc: true
```

Este `_quarto.yml` hace varias cosas:

- **`type: book`** — define el proyecto como un libro con múltiples capítulos
- **`chapters`** — lista el índice de capítulos en orden
- **`format`** — configura los tres formatos de salida simultáneamente
- **`theme`** — establece temas para claro y oscuro en HTML (ver [[html-theming]])
- **`geometry`** — ajusta márgenes para el PDF

Con esta configuración, ejecutar `quarto render` desde la raíz del proyecto genera el libro completo en HTML, PDF y EPUB.
