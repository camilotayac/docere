---
name: bibliotheca
description: >-
  Busca temas en libros científicos clasificados por materia (Física, Química,
  Biología, Matemáticas, Computación, Filosofía) y extrae las secciones relevantes
  como PDF fragmento (copia exacta del original). Usa agentes AI para analizar TOCs,
  validar calidad, y retroalimentar iterativamente. Sin modelos ML pesados, solo fitz.
compatibility: Requiere Python 3.10+, PyMuPDF, y los libros en la carpeta Bibliotheca/
license: MIT
metadata:
  author: bibliotheca
  version: "2.0"
---

# Bibliotheca — Skill de extracción de libros

Esta skill permite buscar un tema en los libros de la biblioteca y extraer las
secciones relevantes como PDF fragmento. **Los agentes AI hacen todo el razonamiento**
(leer TOC, identificar contenido vs preguntas, validar, retroalimentar). El único
script es puramente mecánico y ultraligero.

## Arquitectura

```
Usuario → extractor.md (orquesta)
  │
  ▼
toc_matcher.md (analiza TOC con fitz + previsualiza + identifica páginas)
  │
  ├── extraer_pdf.py (extrae páginas como PDF fragmento)
  │
  ▼
validador.md (verifica PDFs con fitz inline)
  │
  ├── ¿Aceptado? → Presentar al usuario
  └── NO → retroalimentador.md → re-ejecutar (máx 3)
```

Sin modelos ML, sin conversión a Markdown, sin consumo elevado de RAM.
Todo se lee con fitz (<50MB RAM).

## Estructura de archivos

```
Docere/
├── Bibliotheca/
│   ├── SKILL.md
│   ├── agents/
│   │   ├── extractor.md          ← Agente principal (orquesta)
│   │   ├── toc_matcher.md        ← Analiza TOC, identifica páginas
│   │   ├── validador.md          ← Verifica calidad
│   │   └── retroalimentador.md   ← Diagnóstico y mejora
│   ├── scripts/
│   │   └── extraer_pdf.py        ← Extrae páginas como PDF fragmento
│   └── Física/, Química/, …/    ← Libros por materia/idioma
├── artifex/input/                ← Output de extracciones (PDFs fragmento)
└── liber/
```

## Script

### extraer_pdf.py

Extrae un rango de páginas de un PDF como un nuevo PDF fragmento.

```bash
python3 Bibliotheca/scripts/extraer_pdf.py \
  --libro "Bibliotheca/Química/Español/Chang.pdf" \
  --paginas 129-132 \
  --output "artifex/input/reactivo_limite/CONT_001_Chang_129-132.pdf"
```

Consume <50MB RAM.

## Agentes

| Archivo | Rol | RAM |
|---|---|---|
| `agents/extractor.md` | Orquesta el flujo completo | - |
| `agents/toc_matcher.md` | Lee TOCs con fitz, previsualiza páginas, distingue contenido vs preguntas, ejecuta scripts | <50MB |
| `agents/validador.md` | Inspecciona los PDFs con fitz, verifica keywords, decide si acepta | <50MB |
| `agents/retroalimentador.md` | Diagnostica causas de baja calidad, sugiere nuevos parámetros | - |

## Convenciones

- Archivos CONT_* = páginas de contenido teórico
- Archivos PREG_* = páginas de preguntas/ejercicios
- `informe.json` contiene los matches con `contenido_paginas` y `preguntas_paginas` separados
- Los agentes ejecutan comandos Python inline con `python3 -c` + fitz para inspeccionar PDFs
- Máximo 3 iteraciones por tema en el bucle de retroalimentación
- Todo el razonamiento vive en agentes .md; los scripts son puramente mecánicos
