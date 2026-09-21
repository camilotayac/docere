---
title: "Creando libros con Quarto"
subtitle: "Configuración y estructura de proyectos de tipo libro"
categories:
  - "libros"
  - "proyectos"
tags:
  - "book"
  - "_quarto.yml"
  - "proyecto"
---

Los libros en Quarto son proyectos que combinan múltiples documentos en una obra coherente, con navegación estructurada y formato profesional.

## Tipo de proyecto de libro

Para crear un libro, configura el tipo de proyecto en `_quarto.yml`:

```yaml
project:
  type: book
```

Este tipo de proyecto genera automáticamente una estructura de navegación y maneja la compilación secuencial de capítulos.

## Estructura de `_quarto.yml`

Un archivo `_quarto.yml` para libros incluye secciones específicas:

```yaml
project:
  type: book

book:
  title: "Mi Libro"
  subtitle: "Un ejemplo con Quarto"
  author: "Autor Ejemplo"
  date: "2024"
  chapters:
    - index.qmd
    - intro.qmd
    - methods.qmd
    - results.qmd
    - conclusion.qmd
  appendices:
    - references.qmd
    - glossary.qmd

format:
  html:
    theme: cosmo
  pdf: default
```

## Clave `book:` de configuración

La sección `book:` controla todas las opciones específicas del libro:

| Opción | Descripción |
|--------|-------------|
| `title` | Título principal del libro |
| `subtitle` | Subtítulo |
| `author` | Nombre del autor |
| `date` | Fecha de publicación |
| `doi` | Identificador DOI |
| `isbn` | Número ISBN |
| `url` | URL del libro |
| `repository-url` | URL del repositorio |
| `cover-image` | Ruta a la imagen de portada |
| `downloads` | Formatos disponibles para descarga |

## Capítulos (`chapters:`)

Los capítulos son la unidad principal de contenido:

```yaml
book:
  chapters:
    - index.qmd
    - part: "Introducción"
      chapters:
        - intro.qmd
        - background.qmd
    - part: "Métodos"
      chapters:
        - methods.qmd
        - analysis.qmd
```

Cada archivo `.qmd` se renderiza como un capítulo independiente.

## Apéndices (`appendices:`)

Los apéndices contienen material complementario al final del libro:

```yaml
book:
  appendices:
    - references.qmd
    - data-sources.qmd
    - glossary.qmd
```

## Partes (`parts:`)

Las partes agrupan capítulos en secciones temáticas:

```yaml
book:
  chapters:
    - index.qmd
    - part: "Fundamentos"
      chapters:
        - conceptos.qmd
        - teoria.qmd
      content: ""
    - part: "Aplicaciones"
      chapters:
        - practica.qmd
        - ejemplos.qmd
```

## Imagen de portada

La imagen de portada se especifica en la configuración:

```yaml
book:
  cover-image: "images/cover.png"
  cover-image-alt: "Descripción de la portada"
  cover-image-height: "800px"
  cover-image-width: "600px"
```

## Opciones de descarga

Quarto genera automáticamente botones de descarga para múltiples formatos:

```yaml
book:
  downloads:
    - pdf
    - epub
    - docx
```

Los formatos disponibles dependen de las opciones de formato configuradas en el proyecto.

## Configuración de idioma

Para libros en español, configura el idioma en `_quarto.yml`:

```yaml
lang: es

book:
  title: "Mi Libro en Español"
```

Esto afecta la generación de elementos como el índice, tablas de contenido y elementos de navegación.

## Elementos incluidos automáticamente

El tipo de proyecto `book` genera automáticamente:

- Página de título
- Tabla de contenido
- Índice
- Lista de figuras
- Lista de tablas
- Navegación entre capítulos
- Numeración de páginas

## Véase también

- [[book-structure]] - Estructura detallada de libros
- [[customizing-output]] - Personalización de formatos de salida
- [[html-theming]] - Temas HTML para libros