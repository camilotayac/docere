# Quarto — Mapa del Conocimiento

Referencia completa de Quarto para el proyecto Natura Docens.

## Navegación

### [[instalacion|Instalación]]
Cómo instalar Quarto y configurar el entorno de desarrollo.

### [[primer-documento|Primer Documento]]
Crear y renderizar tu primer documento Quarto.

---

## Authoring (Escritura)

| Nota | Descripción |
|------|-------------|
| [[markdown-basics]] | Sintaxis Markdown básica |
| [[figures]] | Figuras, imágenes y subfiguras |
| [[tables]] | Tablas HTML y PDF |
| [[callouts]] | Bloques de llamada (note, tip, warning, etc.) |
| [[cross-references]] | Referencias cruzadas a figuras, tablas, ecuaciones |
| [[citations]] | Citas bibliográficas y bibliografía |

---

## Formats (Formatos de salida)

| Nota | Descripción |
|------|-------------|
| [[html-basics]] | Formato HTML básico |
| [[html-theming]] | **CRÍTICO** — Temas, SCSS, modo dark/light |
| [[pdf-basics]] | Formato PDF con LaTeX |
| [[epub]] | Formato EPUB para e-readers |

---

## Books (Libros)

| Nota | Descripción |
|------|-------------|
| [[creating-books]] | Crear un libro Quarto |
| [[book-structure]] | Estructura: partes, capítulos, apéndices |
| [[customizing-output]] | Personalización de salida HTML/PDF |

---

## Advanced (Avanzado)

| Nota | Descripción |
|------|-------------|
| [[filters]] | Filtros Quarto (pre y post-procesamiento) |
| [[lua-filters]] | Filtros Lua personalizados |
| [[scss-variables]] | **CRÍTICO** — Variables SCSS para temas |

---

## Project (Proyecto)

| Nota | Descripción |
|------|-------------|
| [[configuration]] | **CRÍTICO** — Cómo funciona `_quarto.yml` |
| [[publishing]] | Publicar en GitHub Pages, Netlify, etc. |

---

## HTML

| Nota | Descripción |
|------|-------------|
| [[html]] | **CRÍTICO** — Referencia HTML completa |
| [[html-structure]] | Estructura del documento HTML |
| [[html-attributes]] | Atributos globales, data-*, aria-* |
| [[html-text]] | Encabezados, párrafos, formato |
| [[html-links]] | Enlaces absolutos, relativos, anclas |
| [[html-tables]] | Tablas HTML |
| [[html-forms]] | Formularios e inputs |
| [[html-semantic]] | HTML semántico: nav, main, article |
| [[html-accessibility]] | ARIA, roles, accesibilidad |
| [[html-events]] | Eventos onclick, onkeydown |
| [[html-images]] | Imágenes, responsive, lazy loading |

---

## Conexiones clave para Natura Docens

```
configuration.md → html-theming.md → scss-variables.md
creating-books.md → book-structure.md → customizing-output.md
customizing-output.md → html-theming.md → filters.md
```

## Referencia oficial
- https://quarto.org/docs/guide/
- https://quarto.org/docs/output-formats/html-themes.html
