# Docere

<br>

<div align="center">

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-camilotayac.github.io/docere-2ea44f?style=flat&logo=githubpages&logoColor=white)](https://camilotayac.github.io/docere)
[![Quarto](https://img.shields.io/badge/Quarto-1.4%2B-39729E?style=flat&logo=quarto&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)]()
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat)]()
[![opencode](https://img.shields.io/badge/powered%20by-opencode-7B2FF7?style=flat)]()
[![Repo](https://img.shields.io/badge/repo-camilotayac/docere-181717?style=flat&logo=github&logoColor=white)](https://github.com/camilotayac/docere)

</div>

<br>

> **Docendō discimus** — *Enseñando aprendemos* (Séneca)

<br>

**Docēre** (latín: *enseñar*) — Monorepo que une **Bibliotheca**, un skill opencode
para buscar y extraer contenido de libros científicos; **Artifex**, un motor multi-agente
generador de planes de clase; y el libro Quarto **Natura Docens** de Ciencias Naturales para
educación básica y media en Colombia (grados 6–11).

---

### Significado de los nombres

| Nombre | Lengua | Significado | Rol en el proyecto |
|--------|--------|-------------|--------------------|
| **Docēre** | Latina | *enseñar, instruir, educar* | Nombre del proyecto completo |
| **Artifex** | Latina | *artesano, creador, el que construye con maestría* | Motor generador de planes de clase |
| **Bibliothēca** | Latina | *biblioteca, depósito de libros* | Skill de búsqueda y extracción de libros científicos |
| **Natura Docens** | Latina | *La naturaleza que enseña / Enseñando naturaleza* | Libro Quarto de Ciencias Naturales |

---

## Architectūra — Arquitectura

```
     ┌─────────────────────────────┐
     │      Bibliotheca            │
     │  Busca y extrae secciones   │
     │  de libros científicos      │
     │  ─────────────────────────  │
     │  python3 extraer.py         │
     │  --tema "reactivo límite"   │
     └──────────┬──────────────────┘
                │ output: .md + .pdf
                ▼
     ┌────────────────────────────────────────────────────┐
     │                   Artifex                          │
     │                                                     │
     │   opencode + 11 agentes LLM + QA híbrido           │
     │                                                     │
     │   0 → 0.5 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 →      │
     │   8.5 → 9 → 10 → 10b (feedback) → 11               │
     │                                                     │
     │   Validación mecánica entre cada paso               │
     └────────────────────────────────────────────────────┘
                              │
                              ▼
                       .qmd estructurado
                              │
                              ▼
         ┌─────────────────────────────────────┐
         │  liber/  (Libro Quarto)              │
         │  Natura Docens                      │
         │                                     │
         │  quarto render → HTML / PDF / EPUB  │
         └─────────────────────────────────────┘
                              │
                              ▼
               GitHub Pages (automático)
         https://camilotayac.github.io/docere
```

---

## Structūra — Estructura del proyecto

```
Docere/
├── Bibliotheca/                       ← Skill de biblioteca científica
│   ├── SKILL.md                       ← Orquestador (cargado por opencode)
│   ├── agents/
│   │   ├── extractor.md               ← Workflow de extracción
│   │   ├── validador.md               ← Workflow de validación
│   │   └── retroalimentador.md        ← Workflow de mejora continua
│   ├── scripts/
│   │   ├── extraer.py                 → Busca y extrae por tema
│   │   └── validar.py                 → Valida calidad de extracciones
│   └── Física/, Química/, Biología/,
│       Matemáticas/, Computación/,
│       Filosofía/                     ← Libros por materia (PDF/EPUB)
│         └── Español/, English/       ← Subcarpeta por idioma
├── artifex/                           ← Motor generativo Artifex
│   ├── SKILL.md                       ← Orquestador (cargado por opencode)
│   ├── input/                         ← Input para planes (incluye output de Bibliotheca)
│   ├── output/                        ← .qmd generados (histórico)
│   ├── scripts/
│   │   ├── convert_input_to_md.py     → PDF/DOCX → MD  (Paso 0)
│   │   └── validate_output.py         → 15 checks mecánicos (Paso 10)
│   └── references/
│       ├── agente_teoria.md                    → Paso 1
│       ├── agente_ideas_previas.md             → Paso 2
│       ├── agente_contextualizacion_feynman.md → Paso 3
│       ├── agente_caracterizados.md            → Paso 4 (DUA)
│       ├── agente_ejemplos.md                  → Paso 5
│       ├── agente_ejercicios.md                → Paso 6
│       ├── agente_retos.md                     → Paso 7
│       ├── agente_aplicacion.md                → Paso 8
│       ├── agente_evaluacion.md                → Paso 8.5 (ICFES)
│       ├── agente_socioemocional.md            → Paso 9
│       ├── agente_qa.md                        → Paso 10
│       ├── bibliografia.md                     → Paso 0.5
│       └── estructura_libro.md                 → Paso 11
├── liber/                             ← Libro Quarto
│   ├── _quarto.yml                   ← Configuración del libro
│   ├── _extensions/                  ← edu-boxes.lua + edu-boxes.css
│   ├── preamble.tex                  ← tcolorbox para PDF
│   ├── references.bib                ← Bibliografía única (BibTeX)
│   ├── 02_Sexto/ … 07_Once/          ← Planes de clase por grado
│   └── *.qmd                         ← Portada, índice, generalidades, 404
├── output/                           ← .qmd nuevos generados
├── .github/workflows/publish.yml     ← GitHub Actions → GitHub Pages
└── README.md
```

---

## Initium — Primeros pasos

### Requisitos

- Python 3.10+ (con `pip`)
- Quarto 1.4+
- [opencode](https://opencode.ai)

### Instalación

```bash
git clone git@github.com:camilotayac/docere.git
cd docere

pip install pymupdf python-docx pyyaml

quarto --version   # verificar instalación
```

---

## Usus — Uso con opencode

### Flujo completo (Artifex)

```bash
# 1. Colocar el archivo fuente
cp ~/mi-tema.pdf artifex/input/

# 2. Abrir el proyecto
opencode .
```

Al iniciar, opencode carga `artifex/SKILL.md` y el orquestador ejecuta:

| # | Paso | Acción |
|---|------|--------|
| 1 | Escanea `input/` | Detecta archivos PDF, DOCX o MD |
| 2 | Presenta plan | Lista pasos disponibles y pide confirmación |
| 3 | **Paso 0** | Convierte el input a MD (`convert_input_to_md.py`) |
| 4 | **Paso 0.5** | Lee `liber/references.bib` y pregunta qué referencias usar |
| 5 | **Pasos 1–9** | Ejecuta el agente de cada sección (Teoría → Socioemocional) |
| 6 | **Paso 10** | QA: validación mecánica (`validate_output.py --json`) + revisión semántica LLM |
| 7 | **Paso 10b** | Si QA falla, retroalimenta al agente responsable (máx 3 iteraciones) |
| 8 | **Paso 11** | Coloca el `.qmd` en `liber/<grado>/` o mejora uno existente |
| — | *Entre pasos* | Valida que el box-type esperado esté presente (máx 2 reintentos) |

### Bibliotheca — Extraer secciones de libros

Bibliotheca busca un tema en los libros almacenados en `Bibliotheca/<Materia>/`
y extrae las secciones relevantes como PDF + Markdown en `artifex/input/`.

```bash
# Listar libros disponibles
python3 Bibliotheca/scripts/extraer.py --list-libros

# Extraer secciones sobre un tema
python3 Bibliotheca/scripts/extraer.py --tema "reactivo limite" --materia Química

# Validar calidad de las extracciones
python3 Bibliotheca/scripts/validar.py "artifex/input/reactivo_limite/" --tema "reactivo limite"
```

El output se guarda directamente en `artifex/input/<tema>/`, listo para que
Artifex lo use como fuente del plan de clase. Al abrir opencode, el skill
se carga desde `Bibliotheca/SKILL.md`.

### Modo mejora

Si el archivo `.qmd` destino ya existe, Artifex detecta secciones
presentes vs faltantes con `validate_output.py --sections`, pregunta
al usuario qué sección mejorar y ejecuta solo ese agente.

### Compilar el libro

```bash
quarto render liber/
quarto render liber/ --to html   # solo HTML
```

---

## Gradūs Artificis — Los 15 pasos de Artifex

| Paso | Nombre | Referencia | Genera |
|------|--------|------------|--------|
| 0 | Convertir input | `scripts/convert_input_to_md.py` | `input/texto_teorico.md` |
| 0.5 | Bibliografía | `references/bibliografia.md` | Referencias seleccionadas |
| 1 | Teoría | `agente_teoria.md` | Texto teórico (estudiante + docente) |
| 2 | Ideas Previas | `agente_ideas_previas.md` | Cuento + 4 preguntas + 3 generativas + contextualización |
| 3 | Explicación Feynman | `agente_contextualizacion_feynman.md` | Analogía y explicación Feynman |
| 4 | Caracterizados (DUA) | `agente_caracterizados.md` | 6 versiones adaptadas (Decreto 1421/2017) |
| 5 | Ejemplos Guiados | `agente_ejemplos.md` | 3 ejemplos (Bajo / Medio / Alto) |
| 6 | Ejercicios | `agente_ejercicios.md` | 3 niveles de ejercicios |
| 7 | Retos | `agente_retos.md` | Actividad desafío |
| 8 | Aplicación | `agente_aplicacion.md` | Contexto real + laboratorio |
| 8.5 | Evaluación ICFES | `agente_evaluacion.md` | 5 reactivos (2 Bajo + 2 Medio + 1 Alto) |
| 9 | Socioemocional | `agente_socioemocional.md` | Cierre reflexivo (Ley 2503/2025) |
| 10 | QA | `agente_qa.md` | Validación mecánica + semántica |
| 10b | Feedback loop | — | Re-ejecuta agente si QA falla (máx 3) |
| 11 | Colocar / mejorar | `estructura_libro.md` | `.qmd` en `liber/<grado>/` |

---

## Recognitiō — Validación (QA)

El Paso 10 ejecuta `validate_output.py` con **15 checks mecánicos** agrupados
por categoría:

### Estructura general
| # | Check | Detecta |
|---|-------|---------|
| 1 | `check_box_balance` | Pares `:::` desbalanceados |
| 2 | `check_all_boxes_present` | Falta de alguno de los 11 box types |
| 3 | `check_section_order` | Secciones fuera del orden esperado |

### Calidad de contenido
| # | Check | Detecta |
|---|-------|---------|
| 4 | `check_no_teacher_notes` | Notas `[{...}]` intercaladas en contenido del estudiante |
| 5 | `check_no_todas_las_anteriores` | Opciones "Todas las anteriores" / "Ninguna de las anteriores" |
| 6 | `check_no_emojis` | Emojis en el contenido |
| 7 | `check_latex_balance` | `$` o `$$` desbalanceados |

### Conteo de secciones
| # | Check | Esperado |
|---|-------|----------|
| 8 | `check_caracterizados_count` | 6 boxes de caracterización |
| 9 | `check_ejemplos_niveles` | 3 ejemplos (Bajo, Medio, Alto) |
| 10 | `check_ejercicios_count` | 3 ejercicios |

### Evaluación ICFES
| # | Check | Esperado |
|---|-------|----------|
| 11 | `check_evaluacion_reactivos` | 5 reactivos |
| 12 | `check_evaluacion_distribucion` | 2 Bajo + 2 Medio + 1 Alto |
| 13 | `check_evaluacion_opciones` | Opciones A/B/C/D por reactivo |
| 14 | `check_socializacion_fields` | Nivel, Competencia, Afirmación, Evidencia, Respuesta, Explicación |

### Socioemocional
| # | Check | Esperado |
|---|-------|----------|
| 15 | `check_socioemocional_competencia` | Competencia de Ley 2503/2025 nombrada explícitamente |

> Si algún check falla, el Paso 10b retroalimenta al agente específico
> (el JSON de salida incluye `failures_by_agent`) y re-ejecuta.
> Máximo 3 iteraciones del bucle de retroalimentación.

---

## Fōrma — Formato de salida

Cada plan de clase usa Quarto fenced divs (`:::`) con **23 secciones**
distribuidas en **11 tipos de box**:

```
teoria-box · ideas-previas-box · feynman-box · caracterizado-box (×6)
ejemplo-box (×3) · ejercicio-box (×3) · reto-box · aplicacion-box
laboratorio-box · evaluacion-box · sub-evaluacion-box · socioemocional-box
```

La extensiones en `liber/_extensions/` convierten estos divs en:
- **HTML**: `edu-boxes.css` (clases CSS con colores pastel)
- **PDF**: `preamble.tex` (entornos `tcolorbox`)
- **EPUB**: herencia de CSS

---

## Instrūmenta — Personalización

| Componente | Dónde | Qué hacer |
|------------|-------|-----------|
| **Referencias** | `liber/references.bib` | Agregar entradas BibTeX |
| **Agentes (Artifex)** | `artifex/references/*.md` | Modificar prompts y criterios |
| **Agentes (Bibliotheca)** | `Bibliotheca/agents/*.md` | Modificar prompts y criterios |
| **Libros** | `Bibliotheca/<Materia>/<Idioma>/` | Colocar PDF/EPUB (no se suben a GitHub) |
| **Grados / materias** | `liber/<grado>/` + `_quarto.yml` | Crear carpeta y registrar |
| **Estilos HTML** | `liber/_extensions/edu-boxes.css` | Editar colores, bordes, tipografía |
| **Estilos PDF** | `liber/preamble.tex` | Editar definiciones `tcolorbox` |

---

## Ēditiō — Publicación

El libro se despliega automáticamente a GitHub Pages con cada push a `main`.

```
https://camilotayac.github.io/docere
```

Workflow (`.github/workflows/publish.yml`):
```
push a main → quarto render --to html → upload _liber/ → GitHub Pages
```

---

## Instrūmentārium — Stack tecnológico

| Componente | Tecnología |
|------------|-----------|
| Biblioteca científica | Bibliotheca skill + Python (PyMuPDF + PyYAML) |
| Motor generativo | opencode + Python + LLM |
| Formato de libro | Quarto (QMD → HTML / PDF / EPUB) |
| Despliegue | GitHub Actions → GitHub Pages |
| Repositorio | [github.com/camilotayac/docere](https://github.com/camilotayac/docere) |

<br>

> **Nōn scholae, sed vītae discimus** — *No aprendemos para la escuela, sino para la vida* (Séneca)
