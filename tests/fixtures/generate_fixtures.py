"""Generate test fixtures for the test suite."""

from pathlib import Path

import fitz

FIXTURES = Path(__file__).parent


def create_test_pdf():
    doc = fitz.open()
    for i in range(1, 4):
        page = doc.new_page()
        page.insert_text((50, 50), f"Pagina {i} - Contenido de prueba")
        page.insert_text((50, 100), "Esto es una prueba del extractor PDF.")
        page.insert_text((50, 150), "Seccion de Quimica - Reacciones Quimicas")
    doc.save(str(FIXTURES / "test_input.pdf"))
    doc.close()
    print("PDF creado: test_input.pdf")


def create_test_md():
    path = FIXTURES / "test_input.md"
    path.write_text("# Prueba\n\nContenido de prueba en markdown.")
    print("MD creado: test_input.md")


def create_passing_qmd():
    qmd = """---
title: Reacciones Quimicas - Decimo
bibliography: ../../liber/references.bib
---

# Reacciones Quimicas

::: {.teoria-box title="Teoria"}
Contenido teorico sobre reacciones quimicas.
$$E = mc^2$$
:::

::: {.ideas-previas-box title="Ideas Previas - Cuento"}
Un cuento sobre reacciones quimicas.
:::

::: {.ideas-previas-box title="Ideas Previas - Preguntas"}
Preguntas generativas.
:::

::: {.ideas-previas-box title="Ideas Previas - Contextualizacion"}
Caso sociocolombiano.
:::

::: {.contexto-box title="Contextualizacion - Metodo Richard Feynman"}
Explicacion sencilla del concepto.
:::

::: {.caracterizados-box title="Contextualizacion - Apoyo Cognitivo y TDAH"}
Teoria adaptada.
**Ejemplo:** Un ejemplo resuelto.
**Ejercicios:** Practica.
$\\underline{\\hspace{6cm}}$
:::

::: {.caracterizados-box title="Contextualizacion - Visual"}
Teoria visual.
**Ejemplo:** Ejemplo visual.
**Ejercicios:** Practica visual.
$\\underline{\\hspace{6cm}}$
:::

::: {.caracterizados-box title="Contextualizacion - Dislexia y Dificultades Lectoras"}
Teoria en oraciones cortas.
**Ejemplo:** Ejemplo simple.
**Ejercicios:** Practica simple.
$\\underline{\\hspace{6cm}}$
:::

::: {.caracterizados-box title="Contextualizacion - Autismo y Pensamiento Concreto"}
Regla fija.
**Ejemplo:** Ejemplo concreto.
**Ejercicios:** Practica concreta.
$\\underline{\\hspace{6cm}}$
:::

::: {.caracterizados-box title="Contextualizacion - Accesibilidad Sensorial"}
Formato accesible.
**Ejemplo:** Ejemplo accesible.
**Ejercicios:** Practica accesible.
$\\underline{\\hspace{6cm}}$
:::

::: {.caracterizados-box title="Contextualizacion - Socioemocional y Psicosocial"}
Frase de validacion.
**Ejemplo:** Ejemplo socioemocional.
**Ejercicios:** Practica socioemocional.
$\\underline{\\hspace{6cm}}$
:::

::: {.ejemplo-box title="Ejemplo Guiado - Nivel Bajo"}
**Enunciado:** Enunciado bajo.
**Resultado:** Resultado.
:::

::: {.ejemplo-box title="Ejemplo Guiado - Nivel Medio"}
**Enunciado:** Enunciado medio.
**Resultado:** Resultado.
:::

::: {.ejemplo-box title="Ejemplo Guiado - Nivel Alto"}
**Enunciado:** Enunciado alto.
**Resultado:** Resultado.
:::

::: {.ejercicios-box title="Nivel Bajo"}
Ejercicio de recuperacion.
$\\underline{\\hspace{6cm}}$
:::

::: {.ejercicios-box title="Nivel Medio"}
Ejercicio de aplicacion.
$\\underline{\\hspace{6cm}}$
:::

::: {.ejercicios-box title="Nivel Alto"}
Ejercicio de analisis.
$\\underline{\\hspace{6cm}}$
:::

::: {.retos-box title="Retos"}
Actividad desafiante.
:::

::: {.aplicacion-box title="Aplicacion - Vida real"}
Aplicacion cotidiana.
:::

::: {.aplicacion-box title="Aplicacion - Laboratorio"}
**Objetivo:** Objetivo del laboratorio.
:::

::: {.evaluacion-box title="Evaluacion - tipo ICFES"}
**Pregunta 1** - Nivel Bajo

*Contexto:* Contexto de la pregunta.

*Enunciado:* Enunciado de prueba.

A. Opcion A
B. Opcion B
C. Opcion C
D. Opcion D

**Pregunta 2** - Nivel Bajo

*Contexto:* Contexto 2.

*Enunciado:* Enunciado 2.

A. Opcion A
B. Opcion B
C. Opcion C
D. Opcion D

**Pregunta 3** - Nivel Medio

*Contexto:* Contexto 3.

*Enunciado:* Enunciado 3.

A. Opcion A
B. Opcion B
C. Opcion C
D. Opcion D

**Pregunta 4** - Nivel Medio

*Contexto:* Contexto 4.

*Enunciado:* Enunciado 4.

A. Opcion A
B. Opcion B
C. Opcion C
D. Opcion D

**Pregunta 5** - Nivel Alto

*Contexto:* Contexto 5.

*Enunciado:* Enunciado 5.

A. Opcion A
B. Opcion B
C. Opcion C
D. Opcion D
:::

::: {.evaluacion-box title="Socializacion"}
**Pregunta 1** - Nivel Bajo
*Nivel:* Bajo
*Competencia:* Interpretacion
*Afirmacion:* Afirmacion 1
*Evidencia:* Evidencia 1
*Respuesta correcta:* A
*Explicacion:* Explicacion 1
:::

::: {.socioemocional-box title="Socioemocional"}
Reflexion que trabaja la **Conciencia Emocional** segun Ley 2503/2025.
:::
"""
    (FIXTURES / "passing.qmd").write_text(qmd)
    print("QMD creado: passing.qmd")


def create_failing_qmd():
    qmd = """---
title: Mala Clase
---

::: {.teoria-box title="Teoria"}
Contenido [{nota para docente}]
:::

::: {.evaluacion-box title="Evaluacion - tipo ICFES"}
**Pregunta 1** - Nivel Bajo

*Enunciado:* {text without blank line}
A. Opcion A
B. Opcion B
:::
"""
    (FIXTURES / "failing.qmd").write_text(qmd)
    print("QMD creado: failing.qmd")


if __name__ == "__main__":
    create_test_pdf()
    create_test_md()
    create_passing_qmd()
    create_failing_qmd()
    print("Todos los fixtures generados exitosamente.")
