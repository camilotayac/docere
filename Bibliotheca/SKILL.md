---
name: bibliotheca
description: >-
  Busca temas en libros científicos clasificados por materia (Física, Química,
  Biología, Matemáticas, Computación, Filosofía) y extrae las secciones relevantes
  como PDF exacto + Markdown con metadatos. También valida la calidad de las
  extracciones y mejora iterativamente los resultados.
  Activar cuando el usuario mencione buscar, extraer, exportar, analizar o
  consultar contenido de libros, textos científicos, manuales o referencias académicas.
compatibility: Requiere Python 3.13+, PyMuPDF, PyYAML, y los libros en la carpeta Biblioteca/
license: MIT
metadata:
  author: bibliotheca
  version: "1.0"
---

# Bibliotheca — Skill de extracción de libros

Esta skill permite buscar un tema en los libros de la biblioteca y extraer las
secciones relevantes como PDF (copia exacta del original) + Markdown con
metadatos (fuente, páginas, materia, idioma).

## Estructura de archivos

```
Docere/                              ← Raíz del monorepo
├── Bibliotheca/                     ← Skill de biblioteca
│   ├── SKILL.md                     ← Instrucciones (este archivo)
│   ├── agents/
│   │   ├── extractor.md             ← Workflow de extracción
│   │   ├── validador.md             ← Workflow de validación
│   │   └── retroalimentador.md      ← Workflow de mejora continua
│   ├── scripts/
│   │   ├── extraer.py               ← Script de extracción
│   │   └── validar.py               ← Script de validación
│   └── Física/, Química/, …/       ← Libros por materia (PDF/EPUB)
│       └── Español/                 ← Subcarpeta por idioma
├── artifex/                         ← Motor generativo de planes de clase
│   └── input/                       ← Output de extracciones va aquí
└── liber/                           ← Libro Quarto Natura Docens
```

## Flujo de trabajo

### 1. Extraer — `scripts/extraer.py`

Busca un tema en los libros y extrae secciones como PDF + MD.

```bash
python3 Bibliotheca/scripts/extraer.py --tema "reactivo limite" [--materia Química]
```

Argumentos principales:
- `--tema` / `-t`: tema a buscar (ej: "reactivo limite", "activation energy")
- `--materia` / `-m`: filtrar por materia (Física, Química, etc.)
- `--contexto` / `-c`: páginas de contexto alrededor de cada match (default: 3)
- `--max-resultados` / `-n`: máximo de secciones a extraer (0 = sin límite)
- `--skip-epub`: omitir EPUBs (más rápido, solo PDF)
- `--query` / `-q`: query de búsqueda si difiere del tema (útil para sinónimos)
- `--iteracion` / `-i`: número de iteración (para control de calidad)
- `--list-libros`: lista todos los libros disponibles

Salida: `artifex/input/<tema>/` con archivos `extracto_NNN_libro_pag_ini-fin.pdf` y
`extracto_NNN_libro_pag_ini-fin.md` (con frontmatter YAML de metadatos). Estas
extracciones quedan listas para que Artifex las use como fuente del plan de clase.

### 2. Validar — `scripts/validar.py`

Valida la calidad de las extracciones (cobertura de keywords, longitud,
coherencia). Puntúa de 0 a 1.

```bash
python3 Bibliotheca/scripts/validar.py "artifex/input/reactivo_limite/" --tema "reactivo limite"
```

Salida JSON con puntuación por cada extracto y promedio general.

### 3. Mejora iterativa

Si la puntuación de validación es menor a 0.6:
1. Analizar la causa raíz (query muy específica, contexto insuficiente, etc.)
2. Ajustar parámetros (nueva query, más contexto, filtrar materia)
3. Re-ejecutar extracción con `--iteracion N+1`
4. Re-validar
5. Máximo 3 iteraciones

Ver `agents/retroalimentador.md` para una guía detallada de diagnóstico.

## Formato de salida (Markdown)

Cada archivo `.md` generado contiene:

```yaml
---
id: 1
tema: "reactivo limite"
fuente:
  libro: "Raymond Chang - QUÍMICA 12 ED.pdf"
  ruta: "Química/Español/Raymond Chang - QUÍMICA 12 ED.pdf"
  paginas: [50, 51, 52, 53, 54, 55]
  materia: Química
  idioma: Español
extraccion:
  fecha: 2026-06-13
  query: "reactivo limite"
  contexto_paginas: 3
  iteracion: 1
calidad:
  puntuacion: 0.92
  validado_por: validador
---
```

## Agentes de workflow

Los archivos en `agents/` describen los roles y flujos de trabajo:

| Archivo | Rol |
|---|---|
| `agents/extractor.md` | Agente principal: recibe el tema, ejecuta extracción, coordina validación y mejora |
| `agents/validador.md` | Agente de validación: revisa calidad, ejecuta validar.py, reporta problemas |
| `agents/retroalimentador.md` | Agente de diagnóstico: analiza causas de baja calidad, sugiere parámetros mejorados |

## Consejos prácticos

- Para términos muy comunes (ej: "electrón", "energía"), usar `--max-resultados 5`
  para limitar la salida.
- Si la búsqueda no encuentra resultados, probar con sinónimos, traducción al
  inglés, o términos más cortos.
- Los errores "MuPDF error: syntax error" en stderr son inofensivos y no afectan
  la extracción.
- Para libros en español, la query también funciona en español.
