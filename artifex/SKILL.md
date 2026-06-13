---
name: Docere
description: >
  Monorepo que combina el motor generativo Artifex de planes de clase (AI agents)
  con el libro Quarto de Ciencias Naturales para grados 6-11 en Colombia.
  El orquestador coordina agentes especializados para construir cada seccion
  del plan: Teoria, Ideas Previas, Feynman, Caracterizados, Ejemplos,
  Ejercicios, Retos, Aplicacion, Evaluacion ICFES y Socioemocional.
  Un agente QA final verifica consistencia y formato, y el resultado se
  coloca o integra en el libro Quarto.
license: MIT
metadata:
  version: "2.0"
  author: Camilo Tayac
---

# Docere — Artifex: Generador de Plan de Clase

Artifex: 13 pasos para generar y colocar planes de clase estructurados
dentro del libro Quarto `book/`. El agente orquestador lee este archivo,
ejecuta cada paso en orden y llama al agente especializado indicado.

> [!IMPORTANT]
> **Paso 0 (Input)** usa un script Python para convertir PDF/DOCX a MD.
> **Paso 0.5** pregunta al usuario qué referencias bibliográficas usar.
> **Paso 11** coloca o mejora el .qmd generado dentro de `book/`.
> Todos los demas pasos son ejecutados por el agente leyendo el archivo
> de instrucciones correspondiente en `references/`.

---

## Protocolo de Ejecucion del Agente (Obligatorio)

Cuando el usuario invoque esta Skill (por ejemplo, colocando un archivo en
`input/` y solicitando generar un plan de clase), el agente **DEBE** seguir
este protocolo de forma estricta:

1. **Escaneo de Input:** Revisar la carpeta `input/` para identificar
   archivos `.pdf`, `.docx` o `.md` nuevos.
2. **Presentar Plan:** Listar los pasos a ejecutar y solicitar confirmacion.
3. **Ejecucion Secuencial:** Correr cada paso marcado, en orden.
4. **Verificacion:** Al finalizar, ejecutar el agente QA para validar el
   resultado.

---

## Estructura de Directorios

```
Docere/                              ← Raiz del monorepo
├── .github/workflows/publish.yml    → GitHub Pages deploy (Quarto)
├── artifex/                        → Motor generativo Artifex
│   ├── SKILL.md                     → Este archivo (orquestador)
│   ├── input/                       → Colocar PDF, DOCX o MD aqui
│   ├── output/                      → .qmd generados (historial)
│   ├── scripts/
│   │   ├── convert_input_to_md.py   → Convierte PDF/DOCX a MD (Paso 0)
│   │   └── validate_output.py       → Valida .qmd generado (Paso 10)
│   └── references/
│       ├── agente_teoria.md             → Paso 1
│       ├── agente_ideas_previas.md      → Paso 2
│       ├── agente_contextualizacion_feynman.md → Paso 3
│       ├── agente_caracterizados.md     → Paso 4
│       ├── agente_ejemplos.md           → Paso 5
│       ├── agente_ejercicios.md         → Paso 6
│       ├── agente_retos.md              → Paso 7
│       ├── agente_aplicacion.md         → Paso 8
│       ├── agente_evaluacion.md         → Paso 8.5
│       ├── agente_socioemocional.md     → Paso 9
│       ├── agente_qa.md                 → Paso 10 (Verificacion)
│       ├── bibliografia.md              → Paso 0.5 (seleccion de refs)
│       └── estructura_libro.md          → Paso 11 (colocacion en book/)
├── book/                            → Libro Quarto Natura Docens
│   ├── _quarto.yml
│   ├── references.bib
│   ├── preamble.tex
│   ├── _extensions/
│   ├── index.qmd
│   ├── 02_Sexto/ ... 07_Once/
│   └── ...
├── output/                          → .qmd generados (carpeta compartida)
├── .gitignore
└── README.md
```

---

## Checklist de Ejecucion

El agente marca cada paso al completarlo.

- [ ] **Paso 0:** Convertir input a MD (`scripts/convert_input_to_md.py`)
- [ ] **Paso 0.5:** Seleccionar bibliografía (`references/bibliografia.md`)
- [ ] **Paso 1:** Teoria (`references/agente_teoria.md`)
- [ ] **Paso 2:** Ideas Previas (`references/agente_ideas_previas.md`)
- [ ] **Paso 3:** Contextualizacion Feynman (`references/agente_contextualizacion_feynman.md`)
- [ ] **Paso 4:** Caracterizados (`references/agente_caracterizados.md`)
- [ ] **Paso 5:** Ejemplos (`references/agente_ejemplos.md`)
- [ ] **Paso 6:** Ejercicios (`references/agente_ejercicios.md`)
- [ ] **Paso 7:** Retos (`references/agente_retos.md`)
- [ ] **Paso 8:** Aplicacion (`references/agente_aplicacion.md`)
- [ ] **Paso 8.5:** Evaluacion tipo ICFES (`references/agente_evaluacion.md`)
- [ ] **Paso 9:** Socioemocional (`references/agente_socioemocional.md`)
- [ ] **Paso 10:** QA Final — validacion mecanica + semantica (`references/agente_qa.md`)
- [ ] **Paso 10b:** Bucle de Retroalimentacion (si QA fallo, repetir pasos)
- [ ] **Paso 11:** Colocar o mejorar en book/ (`references/estructura_libro.md`)

---

## Protocolo de Validacion entre Pasos (Obligatorio)

Despues de CADA paso (incluyendo Paso 0), el agente DEBE:

1. **Verificar** que el output contiene el box-type esperado para ese paso
   (ej: tras Paso 1 debe haber un `{.teoria-box}`, tras Paso 5 deben
   aparecer 3 `{.ejemplo-box}`).
2. **Verificar** que el contenido no es placeholder ni esta vacio.
3. **Si el output no es valido:** re-ejecutar el paso inmediatamente,
   indicando al agente que su output anterior fue rechazado y por que.
   No avanzar al siguiente paso hasta obtener un output valido.
4. **Maximo 2 reintentos por paso.** Si falla, detener el proceso y
   reportar al usuario que ese paso no pudo completarse.

Esto evita que errores tempranos se propaguen a pasos downstream y
reduce las iteraciones del bucle de QA final.

### Paso 0 — Convertir Input a Markdown

Convierte cualquier archivo en `input/` a texto plano Markdown.

```bash
python3 scripts/convert_input_to_md.py \
  input/archivo.ext -o input/texto_teorico.md
```

**Entrada:** `input/{archivo}.{pdf|docx|md}`
**Salida:** `input/texto_teorico.md`
**Verificacion:** El archivo `input/texto_teorico.md` existe y no esta vacio.

> Los pasos 1 al 9 (incluyendo 8.5) leen `input/texto_teorico.md` como fuente teorica.

---

### Paso 0.5 — Seleccionar Bibliografia

**El agente lee:** `references/bibliografia.md`
**Entrada:** `book/references.bib`
**Accion:**
1. Leer `book/references.bib` y extraer las referencias disponibles.
2. Presentar al usuario las referencias en formato legible.
3. Preguntar cuales desea usar:
   - "Todas" (por defecto)
   - "Ninguna"
   - Seleccion individual
4. Inyectar las referencias seleccionadas a todos los agentes downstream
   como `## Referencias disponibles` al final de cada prompt.
5. Incluir `bibliography: ../../book/references.bib` en el YAML del .qmd
   (o la ruta relativa correcta segun destino final).
**Verificacion:** Las referencias seleccionadas se documentan para los pasos
siguientes.

---

### Paso 1 — Teoria

**El agente lee:** `references/agente_teoria.md`
**Entrada:** `input/texto_teorico.md`
**Accion:** Extrae y estructura el contenido teorico en un bloque teoria-box.
**Verificacion:** Existe exactamente 1 `{.teoria-box}` con contenido no vacio.

---

### Paso 2 — Ideas Previas

**El agente lee:** `references/agente_ideas_previas.md`
**Entrada:** `input/texto_teorico.md` + bloque de Teoria generado
**Accion:** Genera 3 bloques: Cuento con preguntas referidas al cuento,
Preguntas generativas independientes, y Contextualizacion (caso
sociocultural colombiano).
**Verificacion:** Existen exactamente 3 `{.ideas-previas-box}` con
titles "Ideas Previas - Cuento", "Ideas Previas - Preguntas",
"Ideas Previas - Contextualizacion".

---

### Paso 3 — Contextualizacion Feynman

**El agente lee:** `references/agente_contextualizacion_feynman.md`
**Entrada:** Bloque de Teoria generado (Paso 1) + cuento y contextualizacion
de Ideas Previas (Paso 2, opcional)
**Accion:** Aplica el metodo Feynman para explicar el concepto en terminos
simples. Usa el cuento o la contextualizacion de Ideas Previas para crear
continuidad narrativa si estan disponibles.
**Verificacion:** Existe exactamente 1 `{.contexto-box}` con title
"Contextualizacion - Metodo Richard Feynman".

---

### Paso 4 — Caracterizados

**El agente lee:** `references/agente_caracterizados.md`
**Entrada:** Bloque de Teoria
**Accion:** Genera 6 versiones de texto adaptado (DUA Colombia - Decreto 1421):
Apoyo Cognitivo/TDAH, Visual, Dislexia/Dificultades Lectoras,
Autismo/Pensamiento Concreto, Accesibilidad Sensorial,
Socioemocional/Psicosocial.
**Verificacion:** Existen exactamente 6 `{.caracterizados-box}` con
los titles definidos en `agente_caracterizados.md`.

---

### Paso 5 — Ejemplos

**El agente lee:** `references/agente_ejemplos.md`
**Entrada:** Bloque de Teoria generado (Paso 1) + bloque de
Contextualizacion Feynman (Paso 3)
**Accion:** Crea 3 ejemplos guiados paso a paso (Nivel Bajo, Medio, Alto).
Cada nivel con enunciado, justificacion, pasos con razonamiento y resultado.
Referencia la explicacion de Feynman sin repetir la analogia.
**Verificacion:** Existen exactamente 3 `{.ejemplo-box}` con titles
"Ejemplo Guiado - Nivel Bajo", "Ejemplo Guiado - Nivel Medio",
"Ejemplo Guiado - Nivel Alto".

---

### Paso 6 — Ejercicios

**El agente lee:** `references/agente_ejercicios.md`
**Entrada:** Bloque de Teoria + Ejemplos generados
**Accion:** Disena ejercicios organizados en 3 niveles (Bajo, Medio, Alto).
Nivel Bajo: 2-3 ejercicios de recuperacion. Nivel Medio: 2-3 de aplicacion.
Nivel Alto: 1-2 de analisis.
**Verificacion:** Existen exactamente 3 `{.ejercicios-box}` con titles
"Nivel Bajo", "Nivel Medio", "Nivel Alto".

---

### Paso 7 — Retos

**El agente lee:** `references/agente_retos.md`
**Entrada:** Toda la clase construida hasta el momento
**Accion:** Crea una actividad desafiante.
**Verificacion:** Existe exactamente 1 `{.retos-box}` con title "Retos"
y contenido no vacio.

---

### Paso 8 — Aplicacion

**El agente lee:** `references/agente_aplicacion.md`
**Entrada:** Bloque de Teoria
**Accion:** Genera aplicacion en vida real y en laboratorio.
**Verificacion:** Existen exactamente 2 `{.aplicacion-box}` con titles
"Aplicacion - Vida real" y "Aplicacion - Laboratorio".

---

### Paso 8.5 — Evaluacion tipo ICFES

**El agente lee:** `references/agente_evaluacion.md`
**Entrada:** Bloque de Teoria (Paso 1) + Bloque de Ideas Previas -
Contextualizacion (Paso 2, opcional) + **Bloque de Ejemplos (Paso 5)** +
**Bloque de Ejercicios (Paso 6)** — los errores tipicos de estudiantes
en cada nivel (Bajo/Medio/Alto) sirven como materia prima para los
distractores.
**Accion:** Disena 5 reactivos tipo ICFES con opciones A, B, C, D (1
correcta, 3 distractores) escalonados por nivel de dificultad ICFES:
2 Bajo, 2 Medio, 1 Alto. Distribucion de competencias: Interpretacion (2),
Argumentacion (2), Proposicion (1). Cada reactivo incluye Contexto,
Enunciado y opciones. Ademas genera un bloque de Socializacion con
Competencia, Afirmacion, Evidencia, Nivel, Respuesta correcta y
Explicacion para cada reactivo.
**Verificacion:** Existen 1 `{.evaluacion-box}` y 1 `{.sub-evaluacion-box}`.
Dentro del evaluacion-box: 5 reactivos, 2 Bajo + 2 Medio + 1 Alto.

---

### Paso 9 — Socioemocional

**El agente lee:** `references/agente_socioemocional.md`
**Entrada:** Toda la clase construida
**Accion:** Redacta una reflexion que trabaje una de las 5 competencias
de la Catedra de Educacion Emocional (Ley 2503 de 2025): Conciencia
Emocional, Regulacion Emocional, Autonomia, Inteligencia Interpersonal,
o Habilidades de Vida y Bienestar.
**Verificacion:** Existe exactamente 1 `{.socioemocional-box}`. El
contenido nombra explicitamente una de las 5 competencias de la Ley
2503/2025.

---

### Paso 10 — QA Final

**El agente lee:** `references/agente_qa.md`
**Entrada:** Archivo .qmd completo generado
**Accion:** 
1. Ejecuta `scripts/validate_output.py` para checks mecánicos (boxes, emojis,
   distribución ICFES, etc.)
2. Revisión semántica LLM (consistencia conceptual, calidad pedagógica)
3. Combina ambos reportes en un informe único
**Salida:** Informe de calidad con estado APROBADO / REQUIERE CORRECCIONES.
En caso de REQUIERE CORRECCIONES, incluye `## Feedback de QA` con la lista
detallada de errores y el agente responsable de cada uno.

---

### Paso 10b — Bucle de Retroalimentación

**Condición:** Ejecutar SOLO si el Paso 10 arrojó REQUIERE CORRECCIONES.

**Protocolo:**

1. Leer el `## Feedback de QA` del informe de calidad.
2. Para cada error en el feedback, identificar el agente responsable
   (usar `failures_by_agent` del JSON de `validate_output.py` si está disponible).
3. Para cada agente con errores:
   a. Re-leer el archivo del agente en `references/` (para tener sus instrucciones
      en contexto).
   b. Re-ejecutar ese paso específico, INYECTANDO el `## Feedback de QA` como
      entrada adicional. El texto del feedback debe colocarse al final del prompt
      del agente, después de sus instrucciones regulares.
4. Reconstruir el archivo .qmd con las secciones corregidas.
5. Volver al **Paso 10** (QA Final).
6. Repetir hasta 3 iteraciones máximo.
7. Si después de 3 iteraciones persisten errores, mostrar al usuario:
   - El informe de QA final
   - Los errores que no pudieron resolverse
   - Preguntar si desea continuar manualmente

**Reglas:**
- En cada iteración, solo re-ejecutar los pasos que tuvieron errores.
- No re-ejecutar pasos que ya están correctos.
- El feedback debe adjuntarse textualmente al prompt del agente, no resumido.
- Si un agente recibe feedback en más de una iteración, incluir todo el
  historial de feedback acumulado.

---

### Paso 11 — Colocar o mejorar en book/

**El agente lee:** `references/estructura_libro.md`
**Entrada:** Archivo .qmd aprobado por QA + `book/` existente
**Accion:**

1. **Preguntar grado:** `{Sexto, Septimo, Octavo, Noveno, Decimo, Once}`
   y mapear a carpeta `{02_Sexto, 03_Septimo, 04_Octavo, 05_Noveno,
   06_Decimo, 07_Once}`.

2. **Listar archivos** .qmd existentes en `book/<carpeta>/`.

3. **Preguntar al usuario:**
   - Si el archivo NO existe: `"¿Qué nombre para el nuevo archivo?"`
     → Copiar el .qmd completo a `book/<carpeta>/<nombre>.qmd`.
   - Si el archivo SI existe: entrar en modo MEJORA.

4. **Modo MEJORA:**
   a. Ejecutar `python3 scripts/validate_output.py --sections book/<ruta>.qmd`
      para detectar boxes presentes vs faltantes.
   b. Mostrar menu al usuario:
      ```
      MEJORAR (existentes):    AGREGAR (faltantes):
        ✓ Teoria                 ✗ Evaluacion ICFES
        ✓ Ideas Previas          ✗ Socializacion
        ✓ Ejemplos
      0. Salir
      ```
   c. Segun la eleccion:
      - **MEJORAR:** extraer el bloque actual del .qmd + solicitud del
        usuario → pasar al agente original como
        `## Entrada de Retroalimentacion — Mejora de seccion`
      - **AGREGAR:** ejecutar el agente normalmente → insertar en la
        posicion correcta dentro del archivo
   d. Reemplazar solo esa seccion en el archivo.
   e. Ejecutar QA completo (Paso 10) sobre el archivo modificado.
   f. Preguntar: `"¿Deseas mejorar otra seccion?"`
      → si si, repetir desde 4a; si no, salir.

5. **Confirmar** los cambios y mostrar la ruta final del archivo.

**Salida:** Archivo .qmd colocado o modificado en `book/`.
**Verificacion:** El archivo destino existe y QA pasa.

---

## Formato de Salida

El archivo `.qmd` generado sigue esta estructura:

```markdown
# {Titulo del tema} - {Grado}

::: {.teoria-box title="Teoria"}
{Contenido teorico estructurado}
:::

::: {.ideas-previas-box title="Ideas Previas - Cuento"}
{Narrativa de 3-6 lineas}
- {Pregunta 1: conexion personal referida al cuento}
- {Pregunta 2: especulacion referida al cuento}
- {Pregunta 3: contraste referido al cuento}
- {Pregunta 4: reflexion referida al cuento}
:::

::: {.ideas-previas-box title="Ideas Previas - Preguntas"}
- {Pregunta 1: saber previo}
- {Pregunta 2: experiencia}
- {Pregunta 3: especulacion}
- {Pregunta 4: curiosidad}
:::

::: {.ideas-previas-box title="Ideas Previas - Contextualizacion"}
{Caso sociocultural colombiano de 3-6 lineas. Termina con frase-puente
hacia la teoria.}
:::

::: {.contexto-box title="Contextualizacion - Metodo Richard Feynman"}
{Explicacion simple con analogia}
:::

::: {.caracterizados-box title="Contextualizacion - Apoyo Cognitivo y TDAH"}
{Texto adaptado con pasos numerados, frases cortas y negritas}
:::

::: {.caracterizados-box title="Contextualizacion - Visual"}
{Texto adaptado como tabla, diagrama de flujo o mapa conceptual}
:::

::: {.caracterizados-box title="Contextualizacion - Dislexia y Dificultades Lectoras"}
{Texto adaptado con oraciones cortas, sintaxis clara y separacion visual}
:::

::: {.caracterizados-box title="Contextualizacion - Autismo y Pensamiento Concreto"}
{Texto adaptado con regla explicita y lenguaje literal}
:::

::: {.caracterizados-box title="Contextualizacion - Accesibilidad Sensorial"}
{Texto adaptado con descripciones textuales y formato accesible}
:::

::: {.caracterizados-box title="Contextualizacion - Socioemocional y Psicosocial"}
{Texto adaptado con validacion, acompañamiento y cierre positivo}
:::

::: {.ejemplo-box title="Ejemplo Guiado - Nivel Bajo"}
{Ejemplo simple, 2-4 pasos, nota docente}
:::

::: {.ejemplo-box title="Ejemplo Guiado - Nivel Medio"}
{Ejemplo con 2 variables, 3-5 pasos, nota docente}
:::

::: {.ejemplo-box title="Ejemplo Guiado - Nivel Alto"}
{Ejemplo complejo, 4-7 pasos, nota docente}
:::

::: {.ejercicios-box title="Nivel Bajo"}
{Ejercicios de recuperacion: completar, V/F, identificar}
:::

::: {.ejercicios-box title="Nivel Medio"}
{Ejercicios de aplicacion: respuesta corta, aplicacion}
:::

::: {.ejercicios-box title="Nivel Alto"}
{Ejercicios de analisis: problema abierto, detectar errores}
:::

::: {.retos-box title="Retos"}
{Actividad desafiante}
:::

::: {.aplicacion-box title="Aplicacion - Vida real"}
{Aplicacion cotidiana}
:::

::: {.aplicacion-box title="Aplicacion - Laboratorio"}
{Experimento o demostracion}
:::

::: {.evaluacion-box title="Evaluacion - tipo ICFES"}
{5 reactivos ICFES escalonados por dificultad (2 Bajo, 2 Medio, 1 Alto).
Cada uno: Contexto + Enunciado + opciones A, B, C, D. 1 correcta,
3 distractores.}
:::

::: {.sub-evaluacion-box title="Socializacion"}
{Clave de respuestas para el docente. Cada pregunta: Nivel (Bajo/Medio/Alto),
Competencia, Afirmacion, Evidencia, Respuesta correcta, Explicacion.}
:::

::: {.socioemocional-box title="Socioemocional"}
{Reflexion de 3-6 lineas que nombra la competencia de la Ley 2503/2025
que trabaja y conecta con el tema cientifico}
:::
```
