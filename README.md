# Docere

<br>

<div align="center">

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-camilotayac.github.io/docere-2ea44f?style=flat&logo=githubpages&logoColor=white)](https://camilotayac.github.io/docere)
[![Quarto](https://img.shields.io/badge/Quarto-1.4%2B-39729E?style=flat&logo=quarto&logoColor=white)]()
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat)]()
[![opencode](https://img.shields.io/badge/powered%20by-opencode-7B2FF7?style=flat)]()

</div>

<br>

> **Docendō discimus** — *Enseñando aprendemos* (Séneca)

<br>

**Docēre** (latín: *enseñar*) — Libro Quarto **Natura Docens** de Ciencias Naturales para
educación básica y media en Colombia (grados 6–11). Genera HTML, PDF y EPUB.

---

## Structūra

```
Docere/
├── liber/                          ← Libro Quarto
│   ├── _quarto.yml                 ← Configuración del libro
│   ├── _filters/                   ← Filtros Lua (icfes-tables, wide-tables, color-sections)
│   ├── _styles/headings.css        ← Estilos HTML
│   ├── _scripts/collapse.html      ← Accordion JS para HTML
│   ├── preamble.tex                ← Estilos PDF (tcolorbox, KOMA-Script)
│   ├── references.bib              ← Bibliografía BibTeX
│   ├── 01_Generalidades/           ← Generalidades
│   ├── 02_Sexto/ … 07_Once/       ← Planes de clase por grado
│   └── *.qmd                       ← Portada, índice, bibliografía, 404
├── .github/workflows/publish.yml   ← CI/CD → GitHub Pages
└── README.md
```

---

## Primi passūs

### Requisitos

- [Quarto 1.4+](https://quarto.org/docs/get-started/)

### Compilar el libro

```bash
quarto render liber/
quarto render liber/ --to html    # solo HTML
quarto render liber/ --to pdf     # solo PDF
quarto render liber/ --to epub    # solo EPUB
```

---

## Agregar una clase

1. Crear el archivo `.qmd` en `liber/<grado>/` (ej: `06_Decimo/mi-tema.qmd`)
2. Registrar el archivo en `liber/_quarto.yml` bajo `book.chapters` del grado correspondiente
3. Ejecutar `quarto render liber/`

### Formato del `.qmd`

Cada plan de clase usa fenced divs (`:::`) con clases que se transforman en:
- **HTML**: estilos CSS coloreados (`edu-boxes.css`)
- **PDF**: entornos `tcolorbox` (`preamble.tex`)
- **EPUB**: herencia de CSS

```markdown
---
title: "Nombre de la clase"
---

## Teoría {.teoria}
Contenido...

## Ideas Previas {.ideas-previas}
Contenido...

## Contextualización {.contexto}
Contenido...

## Caracterizados {.caracterizados}
Contenido...

## Ejemplo {.ejemplo}
Contenido...

## Ejercicios {.ejercicios}
Contenido...

## Retos {.retos}
Contenido...

## Aplicación {.aplicacion}
Contenido...

## Evaluación {.evaluacion}
Contenido...

## Socioemocional {.socioemocional}
Contenido...
```

---

## Fōrma — Formato de salida

| Formato | Configuración clave |
|---------|-------------------|
| **HTML** | Theme Flatly, accordion collapse, Mermaid, code-copy |
| **PDF** | KOMA-Script scrbook, tcolorbox, microtype, secciones coloreadas |
| **EPUB** | MathML, toc-depth 2, EPUB3 metadata |

---

## Personalización

| Componente | Archivo | Qué editar |
|-----------|---------|------------|
| Colores headings (HTML) | `liber/_styles/headings.css` | Clases CSS `.teoria`, `.ejemplo`, etc. |
| Colores headings (PDF) | `liber/_filters/color-sections.lua` | Tabla `sectionColors` |
| Estilos PDF | `liber/preamble.tex` | Paquetes LaTeX, tcolorbox |
| Estilos ICFES grid | `liber/_filters/icfes-tables.lua` | Grid options |
| Bibliografía | `liber/references.bib` | Entradas BibTeX |
| Contenido | `liber/<grado>/*.qmd` | Archivos de planes de clase |

---

## Publicación

El libro se despliega automáticamente a GitHub Pages con cada push a `main`.

```
https://camilotayac.github.io/docere
```

---

> **Nōn scholae, sed vītae discimus** — *No aprendemos para la escuela, sino para la vida* (Séneca)
