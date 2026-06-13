# Docere

**Docēre** (latín: *enseñar*). Monorepo que unifica un pipeline generativo de
planes de clase con un libro Quarto de Ciencias Naturales para educación básica
y media en Colombia (grados 6–11).

## Estructura

```
Docere/
├── pipeline/          → Pipeline de IA multi-agente para generar .qmd
│   ├── SKILL.md       → Orquestador (13 pasos)
│   ├── references/    → 11 agentes + bibliografia.md + estructura_libro.md
│   └── scripts/       → convert_input_to_md.py + validate_output.py
├── book/              → Libro Quarto "Plan para docentes de Ciencias Naturales"
│   ├── _quarto.yml    → Configuración del libro
│   ├── _extensions/   → edu-boxes.lua + edu-boxes.css
│   ├── preamble.tex   → tcolorbox definitions para PDF
│   ├── references.bib → Bibliografía BibTeX
│   └── 02_Sexto/ … 07_Once/ → Planes de clase por grado
├── output/            → .qmd generados por el pipeline
├── .github/workflows/ → GitHub Actions para Quarto → GitHub Pages
└── README.md
```

## Pipeline (13 pasos)

1. **Paso 0** — Convertir input (PDF/DOCX/MD) a texto plano
2. **Paso 0.5** — Seleccionar referencias bibliográficas
3. **Pasos 1–9** — Generar secciones del plan (Teoría → Socioemocional)
4. **Paso 10** — QA final (validación mecánica + revisión semántica)
5. **Paso 10b** — Bucle de retroalimentación si QA falla
6. **Paso 11** — Colocar o mejorar en book/

## Requisitos

- Python 3.10+ con `pymupdf` y `python-docx` (para conversión de PDF/DOCX)
- Quarto 1.4+ (para compilar el libro)
- opencode (para ejecutar el pipeline multi-agente)

## Publicación

El libro se despliega automáticamente a GitHub Pages con cada push a `main`
via `.github/workflows/publish.yml`.

Sitio: https://camilotayac.github.io/docere
