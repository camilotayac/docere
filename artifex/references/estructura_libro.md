# Estructura del Libro — Docere/liber/

Mapa de grados, archivos .qmd y secciones existentes en el proyecto Quarto.

## Directorios por grado

| Carpeta | Grados | Archivos |
|:---|:---|:---|
| `02_Sexto` | 6° | Biologia.qmd |
| `03_Septimo` | 7° | Fisica.qmd, Quimica.qmd |
| `04_Octavo` | 8° | Biologia.qmd, Quimica.qmd |
| `05_Noveno` | 9° | Quimica.qmd |
| `06_Decimo` | 10° | Biologia.qmd, Quimica.qmd |
| `07_Once` | 11° | QUIMICA.qmd |

## Ruta base

Todos los archivos están en `liber/<carpeta>/<archivo>.qmd` relativo a la raíz de Docere/.

## Formato de cada archivo

Cada .qmd contiene bloques educativos secuenciales usando la convención de boxes:

```markdown
::: {.teoria-box title="Teoria"}
:::
::: {.ideas-previas-box title="Ideas Previas - Cuento"}
:::
::: {.ideas-previas-box title="Ideas Previas - Preguntas"}
:::
::: {.ideas-previas-box title="Ideas Previas - Contextualizacion"}
:::
::: {.contexto-box title="Contextualizacion - Metodo Richard Feynman"}
:::
::: {.caracterizados-box title="Contextualizacion - Apoyo Cognitivo y TDAH"}
:::
::: {.caracterizados-box title="Contextualizacion - Visual"}
:::
::: {.caracterizados-box title="Contextualizacion - Dislexia y Dificultades Lectoras"}
:::
::: {.caracterizados-box title="Contextualizacion - Autismo y Pensamiento Concreto"}
:::
::: {.caracterizados-box title="Contextualizacion - Accesibilidad Sensorial"}
:::
::: {.caracterizados-box title="Contextualizacion - Socioemocional y Psicosocial"}
:::
::: {.ejemplo-box title="Ejemplo Guiado - Nivel Bajo"}
:::
::: {.ejemplo-box title="Ejemplo Guiado - Nivel Medio"}
:::
::: {.ejemplo-box title="Ejemplo Guiado - Nivel Alto"}
:::
::: {.ejercicios-box title="Nivel Bajo"}
:::
::: {.ejercicios-box title="Nivel Medio"}
:::
::: {.ejercicios-box title="Nivel Alto"}
:::
::: {.retos-box title="Retos"}
:::
::: {.aplicacion-box title="Aplicacion - Vida real"}
:::
::: {.aplicacion-box title="Aplicacion - Laboratorio"}
:::
::: {.evaluacion-box title="Evaluacion - tipo ICFES"}
:::
::: {.evaluacion-box title="Socializacion"}
:::
::: {.socioemocional-box title="Socioemocional"}
:::
```

No todos los archivos contienen todos los boxes; algunos son parciales o usan variantes (existen boxes de nivel básico, medio, alto de ejemplo en lugar de los tres separados, etc.).

## Uso en el proceso

El orquestador usa este archivo para:
1. Preguntar al usuario qué grado corresponde al plan de clase generado.
2. Listar los archivos .qmd existentes en ese grado.
3. Preguntar si crear archivo nuevo o modificar existente.
4. Si modificar: detectar boxes presentes vs faltantes con `validate_output.py --sections`.
5. Mostrar menú de mejora/agregación al usuario.
