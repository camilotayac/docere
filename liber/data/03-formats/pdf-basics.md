# Salida PDF en Quarto

Quarto genera documentos PDF utilizando LaTeX como motor de renderizado. Esta guía cubre la configuración esencial para la salida PDF.

## Motor PDF

Quarto soporta varios motores LaTeX:

| Motor | Descripción | Uso recomendado |
|-------|-------------|-----------------|
| `pdflatex` | El más rápido, soporte limitado de Unicode | Documentos en inglés sin caracteres especiales |
| `xelatex` | Soporte completo de Unicode y fuentes del sistema | **Recomendado** para la mayoría de proyectos |
| `lualatex` | Similar a xelatex, mejor manejo de fuentes | Alternativa a xelatex |

Para documentos en español, se recomienda **xelatex**:

```yaml
format:
  pdf:
    pdf-engine: xelatex
```

## Opciones de documentclass

```yaml
format:
  pdf:
    documentclass: scrreprt
    papersize: letter
    fontsize: 11pt
```

### Clases de documento comunes

| Clase | Tipo | Descripción |
|-------|------|-------------|
| `article` | Artículo | Documento corto, sin capítulos |
| `report` | Reporte | Documento largo con capítulos |
| `book` | Libro | Libro completo con partes |
| `scrreprt` | KOMA-Script | Reporte moderno, flexible |
| `scrbook` | KOMA-Script | Libro moderno, flexible |

### Opciones de tamaño de papel

```yaml
papersize: letter    # 216 x 279 mm
papersize: a4        # 210 x 297 mm
papersize: legal     # 216 x 356 mm
```

### Opciones de tamaño de fuente

```yaml
fontsize: 10pt
fontsize: 11pt      # Recomendado
fontsize: 12pt
```

## Preámbulo LaTeX (include-in-header)

El preámbulo LaTeX permite personalizar el documento antes del contenido:

```yaml
format:
  pdf:
    header-includes:
      - \usepackage{fancyhdr}
      - \pagestyle{fancy}
      - \fancyhead[L]{\leftmark}
      - \fancyhead[R]{\thepage}
      - \fancyfoot[C]{}
      - \usepackage{xeCJK}
      - \setCJKmainfont{Noto Sans CJK SC}
```

También puedes usar archivos externos:

```yaml
header-includes:
  - preamble.tex
```

Donde `preamble.tex` contiene:

```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[L]{\leftmark}
\fancyhead[R]{\thepage}
```

## Enlaces de color

```yaml
format:
  pdf:
    colorlinks: true
    linkcolor: NavyBlue      # Enlaces internos (crossrefs)
    urlcolor: OliveGreen     # Enlaces URL
    citecolor: Brown         # Citas bibliográficas
    toccolor: Black          # Tabla de contenido
```

Si no se configuran colores, los enlaces aparecen con recuadros negros por defecto.

## keep-tex para depuración

```yaml
format:
  pdf:
    keep-tex: true
```

Esto conserva el archivo `.tex` generado después de la compilación. Es útil para:

1. **Depurar errores de LaTeX** — Ver el código LaTeX generado
2. **Personalizar** — Modificar el `.tex` directamente
3. **Aprender** — Entender cómo Quarto traduce markdown a LaTeX

El archivo `.tex` se guarda en el mismo directorio que el PDF.

## Geometría de página

```yaml
format:
  pdf:
    geometry:
      - top=2.5cm
      - bottom=2.5cm
      - left=2.5cm
      - right=2.5cm
```

O en una sola línea:

```yaml
geometry: "margin=2.5cm"
```

## Configuración completa de ejemplo

```yaml
format:
  pdf:
    pdf-engine: xelatex
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
    citecolor: Brown
    toccolor: Black
    keep-tex: true
    header-includes:
      - \usepackage{fancyhdr}
      - \pagestyle{fancy}
      - \fancyhead[L]{\leftmark}
      - \fancyhead[R]{\thepage}
```

## Errores comunes

1. **No instalar LaTeX** — Instala [TinyTeX](https://yihui.org/tinytex/) o una distribución completa
2. **Caracteres especiales** — Usa `xelatex` para soporte de Unicode
3. **Imágenes no encontradas** — Verifica las rutas relativas
4. **Paquetes faltantes** — TinyTeX instala paquetes bajo demanda, pero a veces falla
