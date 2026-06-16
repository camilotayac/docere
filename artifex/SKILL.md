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
dentro del libro Quarto `liber/`. El agente orquestador lee este archivo,
ejecuta cada paso en orden y llama al agente especializado indicado.

> [!IMPORTANT]
> **Paso 0 (Input)** usa un script Python para convertir PDF/DOCX a MD.
> **Paso 0.5** pregunta al usuario qué referencias bibliográficas usar.
> **Paso 11** coloca o mejora el .qmd generado dentro de `liber/`.
> Todos los demas pasos son ejecutados por el agente leyendo el archivo
> de instrucciones correspondiente en `references/`.

---

## Protocolo de Ejecucion del Agente (Obligatorio)

Cuando el usuario invoque esta Skill (por ejemplo, colocando un archivo en
`input/` y solicitando generar un plan de clase), el agente **DEBE** seguir
este protocolo de forma estricta:

0. **Limpiar directorios:** Eliminar `input/texto_teorico.md` y todo
   `output/*.qmd` generados en la ejecucion anterior.
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
│       ├── agente_socializacion.md      → Paso 8.6
│       ├── agente_socioemocional.md     → Paso 9
│       ├── agente_qa.md                 → Paso 10 (Verificacion)
│       ├── bibliografia.md              → Paso 0.5 (seleccion de refs)
│       └── estructura_libro.md          → Paso 11 (colocacion en liber/)
├── liber/                            → Libro Quarto Natura Docens
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

- [ ] **Paso -1:** Limpiar `input/` y `output/` de archivos generados previamente
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
- [ ] **Paso 8.5:** Evaluacion tipo ICFES — 5 preguntas (`references/agente_evaluacion.md`)
- [ ] **Paso 8.6:** Socializacion — claves de respuesta (`references/agente_socializacion.md`)
- [ ] **Paso 9:** Socioemocional (`references/agente_socioemocional.md`)
- [ ] **Paso 10:** QA Final — validacion mecanica + semantica (`references/agente_qa.md`)
- [ ] **Paso 10b:** Bucle de Retroalimentacion (si QA fallo, repetir pasos)
- [ ] **Paso 11:** Colocar o mejorar en liber/ (`references/estructura_libro.md`)
- [ ] **Paso 12:** Desplegar — commit, push y verificar GitHub Pages

---

## Protocolo de Validacion entre Pasos (Obligatorio)

Despues de CADA paso (incluyendo Paso 0), el agente DEBE:

1. **Verificar** que el output contiene el heading con clase esperado
   (ej: tras Paso 1 debe haber un `## Teoría {.teoria}`, tras Paso 5
   deben aparecer 3 headings `## Ejemplo 🟢/🟡/🔴 {.ejemplo}`).
2. **Verificar** que el contenido respeta el formato definido en
   `_estilo_salida.md` para esa sección (tabla pipe 2×2 para ICFES,
   estructura de cada perfil caracterizados, etc.).
3. **Verificar** que el contenido no es placeholder ni esta vacio.
4. **Si el output no es valido:** re-ejecutar el paso inmediatamente,
   indicando al agente que su output anterior fue rechazado y por que.
   No avanzar al siguiente paso hasta obtener un output valido.
5. **Maximo 2 reintentos por paso.** Si falla, detener el proceso y
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
**Entrada:** `liber/references.bib`
**Accion:**

1. Leer `liber/references.bib` y extraer las referencias disponibles.
2. Presentar al usuario las referencias en formato legible.
3. Preguntar cuales desea usar:
   - "Todas" (por defecto)
   - "Ninguna"
   - Seleccion individual
4. Inyectar las referencias seleccionadas a todos los agentes downstream
   como `## Referencias disponibles` al final de cada prompt.
5. Incluir `bibliography: ../../liber/references.bib` en el YAML del .qmd
   (o la ruta relativa correcta segun destino final).
   **Verificacion:** Las referencias seleccionadas se documentan para los pasos
   siguientes.

---

### Paso 1 — Teoria

**El agente lee:** `references/agente_teoria.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.1 para el formato exacto del bloque Teoría.
**Entrada:** `input/texto_teorico.md`
**Accion:** Extrae y estructura el contenido teorico.
**Verificacion:** Existe exactamente 1 `## Teoría {.teoria}` con contenido no vacio.

---

### Paso 2 — Ideas Previas

**El agente lee:** `references/agente_ideas_previas.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.2–10.4 para los formatos de Cuento, Preguntas y Contextualización.
**Entrada:** `input/texto_teorico.md` + bloque de Teoria generado
**Accion:** Genera 3 bloques: Cuento con preguntas referidas al cuento,
Preguntas generativas independientes, y Contextualizacion (caso
sociocultural colombiano).
**Verificacion:** Existen exactamente 3 headings `## Ideas Previas — {...} {.ideas-previas}`
con títulos "Cuento", "Preguntas", "Contextualización".

---

### Paso 3 — Contextualizacion Feynman

**El agente lee:** `references/agente_contextualizacion_feynman.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.5 para el formato exacto del bloque Feynman.
**Entrada:** Bloque de Teoria generado (Paso 1) + cuento y contextualizacion
de Ideas Previas (Paso 2, opcional)
**Accion:** Aplica el metodo Feynman para explicar el concepto en terminos
simples. Usa el cuento o la contextualizacion de Ideas Previas para crear
continuidad narrativa si estan disponibles.
**Verificacion:** Existe exactamente 1 `## Contextualización — Método Feynman {.contexto}`.

---

### Paso 4 — Caracterizados (DUA)

**El agente lee:** `references/agente_caracterizados.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.6–10.11 para el formato exacto de cada perfil (TDAH, Visual, Dislexia, Autismo, Accesibilidad Sensorial, Socioemocional).
**Entrada:** Bloque de Teoria (Paso 1) + Bloque de Contextualizacion Feynman
(Paso 3)
**Accion:** Genera 6 miniclases DUA, una por perfil. Cada miniclase DEBE
contener:

1. **Texto teorico adaptado** construido DESDE la barrera cognitiva del
   perfil (no solo adaptacion de formato).
2. **Un ejemplo resuelto paso a paso** con **autoinstrucciones ACTIVAS**
   (el estudiante produce: "tapa y explica", no solo lee dialogo interno).
3. **Dos ejercicios de practica** con **opcion de formato de respuesta
   alternativo** (oral, grafico, seleccion, manipulativo).
4. **Un momento de metacognicion** que verifique comprension CONCEPTUAL
   (no solo procesal: "explica la relacion entre X e Y").
5. **Un glosario** de 3-5 terminos clave en lenguaje sencillo.

Ademas, CADA miniclase debe:
- Activar las **3 redes neuronales** (afectiva, reconocimiento, estrategica).
- Incluir el **nivel submicro/particulas** de Johnstone (antes o durante
  la explicacion simbolica, no solo al final).
- Incluir al menos una **autoinstruccion activa** que requiera produccion
  del estudiante ("tapa y explica", "reconstruye el diagrama", etc.).
- La **metacognicion** debe verificar comprension conceptual, no solo
  reflexion sobre el proceso.
- Ofrecer al menos una **eleccion** entre 2 opciones en algun ejercicio.
- Usar **lenguaje que afirma capacidades** (prohibido capacitismo/sobreproteccion).
- Respetar las estrategias especificas del perfil (ej: 25x5 para TDAH,
  OpenDyslexic/pictogramas para Dislexia, agenda visual para Autismo,
  ARASAAC/ATbar para Accesibilidad Sensorial, validacion emocional para
  Socioemocional).
- Pasar el **swap test**: cambiar el heading del perfil debe "romper"
  el contenido (no debe funcionar para otro perfil).

Los datos de ejemplos y ejercicios DUA deben ser distintos a los de los
bloques generales (Pasos 5 y 6). El orden pedagogico es:
Teoria -> Ideas Previas -> Feynman -> DUA -> Ejemplos -> Ejercicios -> ...
**Verificacion:** Existen exactamente 6 headings `## Contextualización — {perfil} {.caracterizados}`.
Cada bloque contiene teoria construida desde la barrera, **Ejemplo:** (con
autoinstrucciones activas), **Ejercicios:** (2, con opcion de formato),
**Metacognicion conceptual:** y **Glosario:**. Verificar que incluye nivel
submicro/particulas, que la metacognicion verifica concepto (no solo proceso),
que las autoinstrucciones son activas (no solo modeladas), y que el bloque
pasa el swap test.

---

### Paso 5 — Ejemplos

**El agente lee:** `references/agente_ejemplos.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.12–10.14 para el formato exacto de los 3 niveles (Bajo 🟢, Medio 🟡, Alto 🔴).
**Entrada:** Bloque de Teoria generado (Paso 1) + bloque de
Contextualizacion Feynman (Paso 3)
**Accion:** Crea 3 ejemplos guiados paso a paso (🟢, 🟡, 🔴).
Cada nivel con enunciado, justificacion, pasos con razonamiento y resultado.
Referencia la explicacion de Feynman sin repetir la analogia.
**Verificacion:** Existen exactamente 3 headings `## Ejemplo 🟢 {.ejemplo}`,
`## Ejemplo 🟡 {.ejemplo}`, `## Ejemplo 🔴 {.ejemplo}`.

---

### Paso 6 — Ejercicios

**El agente lee:** `references/agente_ejercicios.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.15–10.17 para el formato exacto de los 3 niveles de ejercicios.
**Entrada:** Bloque de Teoria + Ejemplos generados
**Accion:** Disena ejercicios organizados en 3 niveles (🟢, 🟡, 🔴).
Nivel 🟢: 2-3 ejercicios de recuperacion. Nivel 🟡: 2-3 de aplicacion.
Nivel 🔴: 1-2 de analisis.
**Verificacion:** Existen exactamente 3 headings `## Ejercicios 🟢 {.ejercicios}`,
`## Ejercicios 🟡 {.ejercicios}`, `## Ejercicios 🔴 {.ejercicios}`.

---

### Paso 7 — Retos

**El agente lee:** `references/agente_retos.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.18 para el formato exacto del bloque de retos.
**Entrada:** Toda la clase construida hasta el momento
**Accion:** Crea una actividad desafiante.
**Verificacion:** Existe exactamente 1 `## Retos {.retos}` con contenido no vacio.

---

### Paso 8 — Aplicacion

**El agente lee:** `references/agente_aplicacion.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.19–10.20 para el formato exacto de Aplicación en vida real y en laboratorio.
**Entrada:** Bloque de Teoria
**Accion:** Genera aplicacion en vida real y en laboratorio.
**Verificacion:** Existen exactamente 2 headings `## Aplicación — Vida real {.aplicacion}`
y `## Aplicación — Laboratorio {.aplicacion}`.

---

### Paso 8.5 — Evaluacion tipo ICFES

**El agente lee:** `references/agente_evaluacion.md`
**También DEBE leer:** `references/_estilo_salida.md` §9 (Formato ICFES completo: tabla pipe 2×2, distribución 5 reactivos, competencias) y §10.21 para el template exacto del bloque.
**Entrada:** Bloque de Teoria (Paso 1) + Bloque de Ideas Previas -
Contextualizacion (Paso 2, opcional) + **Bloque de Ejemplos (Paso 5)** +
**Bloque de Ejercicios (Paso 6)** — los errores tipicos de estudiantes
en cada nivel (Bajo/Medio/Alto) sirven como materia prima para los
distractores.
**Accion:** Disena 5 reactivos tipo ICFES con opciones A, B, C, D (1
correcta, 3 distractores) escalonados por nivel de dificultad ICFES:
2 🟢, 2 🟡, 1 🔴. Distribucion de competencias: Interpretacion (2),
Argumentacion (2), Proposicion (1). Cada reactivo incluye Contexto,
Enunciado y opciones en tabla 2×2. Sin incluir claves de respuesta
(va en Paso 8.6).
**Verificacion:** Existe 1 `## Evaluación — Tipo ICFES {.evaluacion}`
con 5 reactivos (2 🟢 + 2 🟡 + 1 🔴).

---

### Paso 8.6 — Socializacion

**El agente lee:** `references/agente_socializacion.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.22 para el formato exacto del bloque de Socialización (usa clase `.evaluacion`).
**Entrada:** Bloque `## Evaluación — Tipo ICFES {.evaluacion}` generado en Paso 8.5 (las 5 preguntas ICFES)
**Accion:** Genera un segundo bloque con heading `## Socialización {.evaluacion}`
conteniendo las claves de respuesta: para cada pregunta, Competencia,
Afirmacion, Evidencia, Nivel, Respuesta correcta y Explicacion.
**Verificacion:** Existe `## Socialización {.evaluacion}` con 5 entradas,
cada una con Competencia, Afirmacion, Evidencia, Respuesta correcta y
Explicacion.

---

### Paso 9 — Socioemocional

**El agente lee:** `references/agente_socioemocional.md`
**También DEBE leer:** `references/_estilo_salida.md` §10.23 para el formato exacto del bloque socioemocional.
**Entrada:** Toda la clase construida
**Accion:** Redacta una reflexion que trabaje una de las 5 competencias
de la Catedra de Educacion Emocional (Ley 2503 de 2025): Conciencia
Emocional, Regulacion Emocional, Autonomia, Inteligencia Interpersonal,
o Habilidades de Vida y Bienestar.
**Verificacion:** Existe exactamente 1 `## Socioemocional {.socioemocional}`.
El contenido nombra explicitamente una de las 5 competencias de la Ley
2503/2025.

---

### Paso 10 — QA Final

**El agente lee:** `references/agente_qa.md`
**Entrada:** Archivo .qmd completo generado
**Accion:** 

1. Ejecuta `scripts/validate_output.py` para checks mecánicos (headings, emojis,
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

### Paso 11 — Colocar o mejorar en liber/

**El agente lee:** `references/estructura_libro.md`
**Entrada:** Archivo .qmd aprobado por QA + `liber/` existente
**Accion:**

1. **Preguntar grado:** `{Sexto, Septimo, Octavo, Noveno, Decimo, Once}`
   y mapear a carpeta `{02_Sexto, 03_Septimo, 04_Octavo, 05_Noveno,
   06_Decimo, 07_Once}`.

2. **Listar archivos** .qmd existentes en `liber/<carpeta>/`.

3. **Preguntar al usuario:**
   
   - Si el archivo NO existe: `"¿Qué nombre para el nuevo archivo?"`
     → Copiar el .qmd completo a `liber/<carpeta>/<nombre>.qmd`.
   - Si el archivo SI existe: entrar en modo MEJORA.

4. **Modo MEJORA:**
   a. Ejecutar `python3 scripts/validate_output.py --sections liber/<ruta>.qmd`
      para detectar boxes presentes vs faltantes.
   b. Mostrar menu al usuario:
   
   ```
    MEJORAR (existentes):    AGREGAR (faltantes):
      ✓ Teoría                 ✗ Evaluación ICFES
      ✓ Ideas Previas          ✗ Socialización
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

**Salida:** Archivo .qmd colocado o modificado en `liber/`.
**Verificacion:** El archivo destino existe y QA pasa.

---

### Paso 12 — Desplegar a GitHub Pages

**Entrada:** Archivo .qmd aprobado por QA y colocado en `liber/`.

**Accion:**

1. **Inspeccionar cambios** — Ejecutar para listar archivos modificados:
   
   ```bash
   git diff --name-only
   ```
   
   Esto devuelve la lista de archivos tocados desde el ultimo commit.

2. **Generar mensaje de commit** — El agente DEBE construir un mensaje
   descriptivo basado en los archivos reales que cambiaron. Ejemplo:
   
   ```
   feat(clase): {tema} - {grado}
   
   Cambios:
   - liber/{grado}/{archivo}.qmd: plan de clase completo con 23 cajas
   - artifex/scripts/validate_output.py: fix emoji regex y opciones
   - artifex/SKILL.md: agregado Paso 12 (deploy)
   ```

3. **Commit y push:**
   
   ```bash
   git add -A
   git commit -m "<mensaje generado>"
   git push origin main
   ```

4. **CI/CD automatico:** El workflow `.github/workflows/publish.yml`
   detecta el push a `main`, renderiza el libro con Quarto y despliega
   a GitHub Pages automaticamente.

5. **Verificacion:** Sugerir al usuario que revise el sitio en
   `https://camilotayac.github.io/docere/` y confirme que la nueva
   clase aparece en el grado correspondiente.

**Salida:** Cambios publicados en GitHub y desplegados en GitHub Pages.
**Verificacion:** El push se completa sin errores.

---

## Formato de Salida

El formato exacto de salida está definido en **`references/_estilo_salida.md`**.

**TODO agente** DEBE leer ese archivo antes de generar cualquier contenido.
Contiene:

- Reglas de formato LaTeX, colores, tablas y ortografía
- Formato ICFES (encabezado con 🟢🟡🔴, tabla 2×2 de opciones, distribución)
- Template completo con los 23 headings, sus clases y títulos exactos
- Tabla resumen de secciones por tipo (11 clases, 23 bloques)
- Prohibiciones globales y casos borde
- Convención de emojis: 🟢 = Bajo, 🟡 = Medio, 🔴 = Alto

> Este archivo (`_estilo_salida.md`) es la única fuente de verdad para el
> formato de salida. Cualquier cambio de estilo debe hacerse allí.
