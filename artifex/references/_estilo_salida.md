# Estilo de Salida — Formato Único para Planes de Clase

Fuente de verdad para TODO el formato de salida del pipeline Artifex.
Todos los agentes DEBEN leer este archivo antes de generar contenido.
Las reglas aquí definidas reemplazan y unifican `_reglas_comunes.md` y `agente_estilo.md`.

---

## 1. Espaciado entre Párrafos

- Todo párrafo debe separarse con **una línea en blanco** (doble espacio).
- No escribir párrafos seguidos sin separación.

---

## 2. Prohibiciones Globales

- No incluir **emojis** en ningún bloque. Excepción: los círculos 🟢🟡🔴 están permitidos para indicar dificultad.
- No usar **HTML inline** (`<div>`, `<style>`, `<font>`, etc.). Excepción: `<span style="color:...">` está permitido para colores (ver sección 6).
- No usar **tablas ASCII** con caracteres de dibujo de cajas (`┌ ┐ └ ┘ ├ ┤ ┬ ┴ ─ │` y similares).
- No poner tablas dentro de bloques de código (```` ``` ````).
- No usar **notas** `[{...}]` para el docente intercaladas en el contenido.
- No usar **"Todas las anteriores"** ni **"Ninguna de las anteriores"** en opciones ICFES.
- No usar las etiquetas literales `*Contexto:*` ni `*Enunciado:*` en el contenido de las preguntas ICFES.
- Usar círculos 🟢🟡🔴 para indicar dificultad (Bajo → 🟢, Medio → 🟡, Alto → 🔴).
- No usar **flecha Unicode** (`→`) fuera de LaTeX; usar `$\rightarrow$` dentro de inline math.
- No usar **subíndices/superíndices Unicode** (`₂`, `³`, `²⁺`) fuera de LaTeX.
- No usar el símbolo `\div` en LaTeX; usar `\frac{A}{B}` para divisiones.
- No escribir pasos numerados en **párrafo corrido** (`**1.** text **2.** text`).

---

## 3. Ortografía

- **Ortografía perfecta en español** en todo el contenido (tildes, ñ).

---

## 4. Formato de Encabezados (Headings)

- Cada sección del plan de clase se marca con **`## Título {.clase}`** (heading level 2 con clase).
- No se usan fenced divs (`::: {.tipo-box}`). En su lugar, cada bloque es un `##` heading seguido de su contenido.
- Las clases deben coincidir **EXACTAMENTE** con las definidas en este archivo.
- Los títulos de los headings **llevan acentos** ortográficos normales del español.

---

## 5. Formato LaTeX

- **Inline** (dentro de texto): `$...$` — para valores, símbolos, fórmulas cortas.
- **Display** (separado del texto): `$$...$$` — para fórmulas principales, ecuaciones, reacciones.

### 5.1 Valores numéricos y unidades

- **TODO valor numérico** en LaTeX inline `$...$`: `$5.0$`, `$55.85$`, `$2$`.
- **Toda unidad** dentro de `\text{}` con `\,` (thin space): `$55.85\,\text{g}$`, `$2\,\text{mol}$`, `$30\,\text{mL}$`.
- **Porcentajes**: `$75\%$`, `$39.1\%$`.
- **Cocientes y divisiones**: usar `\frac{}{}`, nunca `÷`: `$\frac{55.85}{55.85} = 1.00$`.
- **Operadores relacionales** (`<`, `>`, `=`) dentro de `$...$`.

### 5.2 Fórmulas importantes

- Fórmulas principales en **display math** `$$...$$` en su propia línea.
- Fórmulas referenciadas desde el texto usar `\tag{N}`:
  `$$n = \frac{m}{M}\tag{1}$$`
  Referenciar como "Ecuación N" o "(N)".
- Fórmulas secundarias y cálculos paso a paso pueden ir inline con `$...$`.

### 5.3 Reacciones químicas

- En **display math** `$$...$$`: `$$2H_2 + O_2 \rightarrow 2H_2O$$`.
- Prohibido en texto plano: `Fe + S → FeS`.
- Usar `$\rightarrow$` (inline) o `$$\rightarrow$$` (display), siempre dentro de math mode.

### 5.4 Símbolos y fórmulas químicas

- **TODO símbolo de elemento químico** en LaTeX inline `$...$`: `$Fe$`, `$Na$`, `$Cl$`, `$H$`, `$O$`, `$C$`, `$N$`, `$Ca$`, `$Mg$`, `$S$`, `$P$`, `$K$`.
- Prohibido en texto plano: `Fe`, `Na`, `Cl`, `H2O`, `CO2`.
- **Subíndices** con `_`: `$H_2O$`, `$C_6H_{12}O_6$`, `$Fe_2O_3$`, `$H_2SO_4$`.
- **Superíndices** (cargas iónicas, isótopos): `$Ca^{2+}$`, `$SO_4^{2-}$`, `$^{14}C$`, `$^{235}U$`.
- **Estados de agregación**: `$(s)$`, `$(l)$`, `$(g)$`, `$(ac)$` dentro del math mode.
- **Accesibilidad**: mantener texto descriptivo junto a la fórmula:
  `$Fe + S \rightarrow FeS$ (hierro más azufre produce sulfuro de hierro)`.

---

## 6. Colores

Usar HTML inline con `<span style="color:...">` para que los colores se vean reflejados en el markdown renderizado:

- `<span style="color:blue">texto</span>`
- `<span style="color:red">texto</span>`
- `<span style="color:green">texto</span>`

También se puede combinar con negrita: **<span style="color:blue">texto</span>**
Aplicar solo cuando el color aporte información (diagramas, tablas, clasificaciones).

---

## 7. Tablas

- Usar **tablas Markdown**: `| col1 | col2 |` con `|---|---|`.
- Prohibido tablas ASCII o tablas dentro de bloques de código.
- Las tablas deben tener encabezados claros y estar separadas del texto circundante por líneas en blanco.

---

## 8. Pasos Numerados

Usar **lista numerada Markdown**:

```markdown
1. **Acción.** Explicación de la acción.
2. **Acción.** Explicación de la acción.
```

Cada paso en su propia línea. El texto en negrita es la acción/operación. Tras la negrita va un punto y la explicación.

---

## 9. Formato ICFES (Evaluación)

### 9.1 Estructura de cada reactivo

```markdown
**Pregunta N 🟢/🟡/🔴**

{Contexto con situación real o de laboratorio, datos organizados, 3-5 líneas o tabla}

{Enunciado o pregunta concreta que exige aplicar la teoría al contexto dado}

| :--- | :--- |
| A. {opción} | B. {opción} |
| C. {opción} | D. {opción} |
```

Las opciones se escriben como **tabla pipe Markdown 2×2** con línea separadora
(`| :--- | :--- |`) para que Pandoc la reconozca como tabla. El pipeline de
renderizado (**Lua filter** `icfes-tables.lua`) transforma automáticamente esta
tabla en un grid estilizado con letras en círculo, sin bordes de rejilla visibles,
con columnas equitativas (50/50). Funciona en PDF, HTML y EPUB.

### 9.2 Reglas ICFES

- **Línea en blanco** obligatoria antes de la tabla de opciones (opciones no pegadas al enunciado).
- Opciones en **tabla pipe 2×2** con línea separadora (IMPORTANTE: Sin la línea
  `| :--- | :--- |` Pandoc no la reconoce como tabla y la interpreta como line block):
  `| :--- | :--- |` / `| A. {opción} | B. {opción} |` / `| C. {opción} | D. {opción} |`.
  La tabla se transforma automáticamente en un grid estilizado al renderizar.
- **`---`** entre reactivos.
- Sin "Todas las anteriores" ni "Ninguna de las anteriores".
- Sin etiquetas literales `*Contexto:*` o `*Enunciado:*`.
- Encabezado: `**Pregunta N 🟢/🟡/🔴**` en negrita, según dificultad.

### 9.3 Distribución por reactivo

| Reactivo | Dificultad | Competencia    |
|:-------- |:----------:|:-------------- |
| 1        | 🟢         | Interpretación |
| 2        | 🟢         | Argumentación  |
| 3        | 🟡         | Interpretación |
| 4        | 🟡         | Proposición    |
| 5        | 🔴         | Argumentación  |

Total: 5 reactivos (2 🟢 + 2 🟡 + 1 🔴).

---

## 9.4 Reglas DUA para Bloques Caracterizados

### 9.4.1 Glosario obligatorio

Cada bloque caracterizados DEBE incluir un **Glosario** con 3-5 términos
clave definidos en lenguaje sencillo. Formato:

```markdown
**Glosario:**
- **{Término}:** {Definición en 1-2 oraciones}
```

### 9.4.2 Metacognición obligatoria

Cada bloque caracterizados DEBE incluir un momento de **Metacognición**.
Formato:

```markdown
**Metacognición:** {Pregunta(s) reflexiva(s) sobre el proceso de aprendizaje}
```

### 9.4.3 Formato de expresión alternativo

Cada ejercicio DEBE ofrecer al menos una opción alternativa al formato
escrito. Opciones: oral (grabación de audio), gráfico (dibujo, diagrama),
selección (emparejamiento, opción múltiple), manipulativo (señalar, trazar,
construir). Formato en el enunciado:
`**Opción de respuesta:** {escrito | oral}`, o
`**Opción de respuesta:** {completar la tabla | dibujar un diagrama}`.

### 9.4.4 Elección del estudiante

Cada bloque DEBE contener al menos una actividad donde el estudiante pueda
elegir entre 2 opciones. Ejemplo: `Resuelve por escrito O explica en voz
alta los pasos`.

### 9.4.5 Lectura fácil y accesibilidad tipográfica

- Perfil **Dislexia**: oraciones máx. 15 palabras, estructura S+V+O, sin
  dobles negaciones, sin voz pasiva. Sugerir tipografía sans-serif u
  **OpenDyslexic**. Incluir **pictogramas ARASAAC** de apoyo.
- Perfil **TDAH**: pasos numerados verticales, frases cortas (1-2 líneas
  por párrafo), microestructura **25×5** (25 min trabajo + 5 min pausa
  activa), temporizador sugerido.
- Perfil **Accesibilidad Sensorial**: descripciones textuales compatibles
  con lectores de pantalla. Alternativas multisensoriales (auditiva,
  kinestésica, táctil). Herramientas: **ATbar**, **JAWS**, **SpeakIt**,
  **ARASAAC**, **SpeechTexter**, **e-Mintza**.
- Perfil **Autismo**: regla fija al inicio, agenda visual con pasos,
  checklist de verificación, lenguaje 100% literal sin metáforas.

### 9.4.6 Activación de las 3 redes neuronales

Cada bloque DEBE activar las 3 redes cerebrales del aprendizaje (CAST UDL
3.0, 2024):

- **Red afectiva** (el POR QUÉ): relevancia, motivación, conexión con la
  vida del estudiante, validación emocional, autonomía.
- **Red de reconocimiento** (el QUÉ): múltiples canales sensoriales
  (visual, auditivo, kinestésico, táctil).
- **Red estratégica** (el CÓMO): funciones ejecutivas, planificación,
  autorregulación, metacognición, autoinstrucciones.

### 9.4.7 Lenguaje que afirma capacidades

Prohibido lenguaje capacitista, sobreprotector o que refleje bajas
expectativas:

- Usar "puedes", "logra paso a paso", "vas bien", "tú puedes lograr esto".
- NUNCA: "no te preocupes si no entiendes", "esto es difícil", "si no
  puedes, no importa".
- Primero persona: "estudiante con TDAH" (no "el TDAH"), "persona con
  autismo" (no "autista" como etiqueta).
- No usar metáforas, ironía, sarcasmo o lenguaje figurado en perfiles
  Autismo, TDAH y Dislexia.

---

## 10. Template Completo de Salida

El archivo `.qmd` generado debe seguir esta estructura exacta con **23 bloques** (11 tipos de box), cada uno documentado en su propia subsección. Respetar class y title al pie de la letra.

### 10.1 Teoría

```markdown
## Teoría {.teoria}

{Contenido teórico estructurado. Fórmulas importantes con $$...\\tag{N}$$.}
```

### 10.2 Ideas Previas — Cuento

```markdown
## Ideas Previas — Cuento {.ideas-previas}

{Narrativa de 3-6 líneas}

- {Pregunta 1: conexión personal referida al cuento}
- {Pregunta 2: especulación referida al cuento}
- {Pregunta 3: contraste referido al cuento}
- {Pregunta 4: reflexión referida al cuento}
```

### 10.3 Ideas Previas — Preguntas

```markdown
## Ideas Previas — Preguntas {.ideas-previas}

- {Pregunta 1: saber previo}
- {Pregunta 2: experiencia}
- {Pregunta 3: especulación}
- {Pregunta 4: curiosidad}
```

### 10.4 Ideas Previas — Contextualización

```markdown
## Ideas Previas — Contextualización {.ideas-previas}

{Caso sociocultural colombiano de 3-6 líneas. Termina con frase-puente hacia la teoría.}
```

### 10.5 Contextualización — Método Feynman

```markdown
## Contextualización — Método Feynman {.contexto}

{Explicación Feynman del concepto. Sin fórmulas ni procedimientos.}
```

### 10.6 Contextualización — Apoyo Cognitivo y TDAH

```markdown
## Contextualización — Apoyo Cognitivo y TDAH {.caracterizados}

{Voz de entrenador: directa, "tú puedes", "vamos paso a paso". Temporizador: 25 min. Estructura 25×5.}

{Nivel submicro/partículas: analogía concreta de partículas ANTES de la fórmula (ej: moléculas como objetos, coeficientes como cantidad).}

{Teoría construida DESDE la barrera de impulsividad: pasos numerados verticales, 1-2 líneas por párrafo, autoinstrucciones ACTIVAS integradas. Nunca párrafo corrido.}

**Ejemplo:** {Enunciado con datos. Autoinstrucciones ACTIVAS: "Ahora tapa el siguiente paso y explica en voz alta por qué haces esa operación." Pasos numerados con operación y resultado.}

**Ejercicios:**

1. {Ejercicio 1. **Opción de respuesta:** escrito | oral. Checklist: [ ] Dato 1 [ ] Dato 2 [ ] Cálculo [ ] Resultado. Incluir: "Después de resolver, tapa el resultado y explicaselo a un compañero imaginario."}
2. {Ejercicio 2. **Opción de respuesta:** escrito | oral.}

**Metacognición (verificación conceptual):** "Explica con tus palabras la relación entre los coeficientes de la ecuación y las moléculas. ¿Qué cambiaría si la proporción fuera 3:1?"

**Glosario:** {3-5 términos con definiciones en 1 oración.}
```

### 10.7 Contextualización — Visual

```markdown
## Contextualización — Visual {.caracterizados}

{Voz de guía visual: "observa cómo", "mira la tabla", "nota los colores".}

{Nivel submicro/partículas: diagrama de partículas con colores, tabla que muestre la proporción visualmente.}

{Teoría construida DESDE la barrera comunicativa: arrancar con representación visual (tabla, diagrama), después la fórmula. Prohibido recuadros ASCII.}

**Ejemplo:** {Datos en tabla Markdown. Diagrama de flujo: entrada -> paso 1 -> paso 2 -> resultado. Autoinstrucción activa visual: "Cubre los valores y reconstruye el diagrama desde tu memoria."}

**Ejercicios:**

1. {Tabla incompleta. **Opción de respuesta:** completar tabla | dibujar diagrama.}
2. {Crear tu propio organizador visual del concepto.}

**Metacognición (verificación conceptual):** "Dibuja o describe el nivel de partículas de lo que aprendiste. ¿Cómo se ven las moléculas antes y después de la reacción?" Tabla 2 columnas: ¿Qué aprendí? / ¿Cómo lo representaría visualmente?

**Glosario:** {3-5 términos con definiciones + referente visual entre paréntesis.}
```

### 10.8 Contextualización — Dislexia y Dificultades Lectoras

```markdown
## Contextualización — Dislexia y Dificultades Lectoras {.caracterizados}

{Voz conversacional: "tú", "ahora haz esto", "esto significa". Sin metaforas ni dobles negaciones.}

{Nivel submicro/partículas con vocabulario mínimo: "el número que dice cuántas moléculas hay" en vez de "coeficiente estequiométrico".}

{Teoría construida DESDE la barrera de sobrecarga de memoria de trabajo: oraciones máx. 15 palabras, S+V+O, cada término técnico con definición entre paréntesis. Sugerir OpenDyslexic. Pictogramas ARASAAC.}

**Ejemplo:** {Enunciado en 1-2 oraciones. Pasos con -> entre cálculo y resultado. Autoinstrucción activa: "Ahora tapa los pasos y explica en voz alta el primer paso. ¿Qué tenés que hacer primero?"}

**Ejercicios:**

1. {Enunciado corto. **Opción de respuesta:** escribir | grabar audio.}
2. {Enunciado corto. Verificación activa: "Explica con tus palabras lo que hiciste como si se lo contaras a un amigo de 10 años."}

**Metacognición (verificación conceptual):** "Sin leer la teoría otra vez, explica cuál es la relación entre los coeficientes y las moléculas. Usa tu voz."

**Glosario:** {3-5 términos con pictograma ARASAAC + definición en 1 oración.}
```

### 10.9 Contextualización — Autismo y Pensamiento Concreto

```markdown
## Contextualización — Autismo y Pensamiento Concreto {.caracterizados}

{Voz de manual de instrucciones: literal, predecible, misma estructura siempre. Sin metaforas, sin ironia, sin lenguaje figurado.}

**Regla fija:** {Regla explícita que incluye el nivel submicro: "cada ecuación dice cuántas moléculas de cada tipo participan".}

{Agenda visual: [1] Regla [2] Ejemplo [3] Ejercicios.} {Desarrollo literal. Apoyos visuales persistentes (fórmula o tabla en recuadro fijo). No asumir inferencia.}

**Ejemplo:** {Enunciado literal. Checklist de pasos. Autoinstrucción activa literal: "Ahora aplica la regla al revés: si te doy el resultado, reconstruí los pasos."}

**Ejercicios:**

1. {Aplica la regla fija. **Opción de respuesta:** resolver | emparejar pasos con resultados.}
2. {¿Aplica la regla? SI/NO (decidir, no solo aplicar mecánicamente).}

**Metacognición (verificación conceptual):** "Sin mirar el bloque, escribí la regla fija con tus palabras. ¿Qué dice sobre la relación entre coeficientes y moléculas?"

**Glosario:** {3-5 términos con definición literal + ejemplo concreto.}
```

### 10.10 Contextualización — Accesibilidad Sensorial

```markdown
## Contextualización — Accesibilidad Sensorial {.caracterizados}

{Voz de audiodescriptor: "localiza", "desplázate a", "señala con el dedo", "traza la línea". Cada instrucción ejecutable sin depender de la vista.}

{Nivel submicro/partículas en formato multi-canal: descripción textual de la partícula + alternativa kinestésica ("tomá 2 objetos que sean H y 1 que sea O y juntalos") + alternativa auditiva.}

[Formato accesible: descripciones textuales + alternativas multisensoriales (auditiva, kinestésica, táctil). Herramientas: ATbar, JAWS, SpeakIt, ARASAAC, SpeechTexter, e-Mintza.]

{Teoría con descripción textual para lectores de pantalla. Fórmula LaTeX + descripción textual entre paréntesis.}

**Ejemplo:** {Descripción textual de cada paso. Alternativa kinestésica. Autoinstrucción activa multi-canal: "Cerrá los ojos y describí en voz alta el paso que sigue. Después, señalalo con el dedo."}

**Ejercicios:**

1. {Instrucciones con pictograma ARASAAC. **Opción de respuesta:** escrito | por voz | selección.}
2. {Alternativa kinestésica: "ordená estas tarjetas con los pasos" (descrito textualmente).}

**Metacognición (verificación conceptual):** "Explica el concepto usando SOLO tu voz (sin leer, sin escribir). Grabalo si querés."

**Glosario:** {3-5 términos con pictograma ARASAAC + descripción textual.}
```

### 10.11 Contextualización — Socioemocional y Psicosocial

```markdown
## Contextualización — Socioemocional y Psicosocial {.caracterizados}

{Voz cálida y contenedora: "vamos a", "juntos", "está bien si...", "respira". Validar antes de instruir. Cerrar con afirmación positiva.}

{Nivel submicro/partículas como historia accesible: "imaginá que las moléculas son ingredientes de una receta. No da miedo."}

{Frase de validación emocional. Ejercicio de regulación: "Respira profundo 3 veces antes de empezar".}

{Teoría con conexión cotidiana y lenguaje tranquilizador. "Vamos a", "puedes", "observa que". Cierre positivo.}

**Ejemplo:** {Validación del proceso. Autoinstrucción activa convalidante: "Explicá en voz alta el paso que entendiste mejor. No importa si no es perfecto." Pasos con pausas emotivas. Apoyo de pares.}

**Ejercicios:**

1. {Mensaje de ánimo. **Opción de respuesta:** individual | en pareja (cooperativo).}
2. {Mensaje de ánimo. Autoevaluación emocional: escala 1-5 ¿cómo te sentiste? Autoinstrucción activa afectiva: "Reconocé lo que lograste. ¿Qué fue lo que más te costó? Bien, ya pasaste eso."}

**Metacognición (verificación conceptual):** "Explicá con tus palabras y SIN apuro lo que entendiste. Si no te sale perfecto, está bien. ¿Qué parte del concepto te parece más clara ahora?"

**Glosario:** {3-5 términos con ejemplos de la vida cotidiana.}
```

### 10.12 Ejemplo 🟢

```markdown
## Ejemplo — Nivel Bajo 🟢 {.ejemplo}

**Enunciado:** ... **Justificación Teórica:** ... **Ejecución:** **Paso 1:** ... ← (razonamiento) **Resultado:**

{Fórmulas en $$...$$ display. Colores como **<span style="color:blue">texto</span>** si aplica.}
```

### 10.13 Ejemplo 🟡

```markdown
## Ejemplo — Nivel Medio 🟡 {.ejemplo}

...
```

### 10.14 Ejemplo 🔴

```markdown
## Ejemplo — Nivel Alto 🔴 {.ejemplo}

...
```

### 10.15 Ejercicios 🟢

```markdown
## Ejercicios — Nivel Bajo 🟢 {.ejercicios}

- {Ejercicio de recuperación}
- {V/F o identificación}
```

### 10.16 Ejercicios 🟡

```markdown
## Ejercicios — Nivel Medio 🟡 {.ejercicios}

- {Respuesta corta o aplicación}
- {Aplicación simple}
```

### 10.17 Ejercicios 🔴

```markdown
## Ejercicios — Nivel Alto 🔴 {.ejercicios}

- {Problema abierto o análisis de errores}
```

### 10.18 Retos

```markdown
## Retos {.retos}

{Actividad desafiante con 3-5 requisitos}
```

### 10.19 Aplicación — Vida real

```markdown
## Aplicación — Vida real {.aplicacion}

{Fenómeno cotidiano explicado con el concepto.}
```

### 10.20 Aplicación — Laboratorio

```markdown
## Aplicación — Laboratorio {.aplicacion}

**Objetivo:** ... **Materiales:** ... **Procedimiento:**

1. ... **Resultados:** {tabla Markdown} **Conclusión:**
```

### 10.21 Evaluación — Tipo ICFES

```markdown
## Evaluación — Tipo ICFES {.evaluacion}

**Pregunta 1 🟢**

{Contexto con situación real o de laboratorio, datos organizados, 3-5 líneas o tabla.}

{Enunciado que exige aplicar la teoría al contexto dado.}

| :--- | :--- |
| A. {opción} | B. {opción} |
| C. {opción} | D. {opción} |

---

**Pregunta 2 🟢**

...

(5 reactivos total: 2 🟢, 2 🟡, 1 🔴. Línea en blanco obligatoria antes de la tabla.)
(La tabla 2×2 con `| :--- | :--- |` se transforma automáticamente en grid estilizado con letras en círculo.)
```

### 10.22 Socialización

```markdown
## Socialización {.evaluacion}

**Pregunta 1 🟢**

*Competencia:* ... *Afirmación:* ... *Evidencia:* ... *Respuesta correcta:* ... *Explicación:* ...
```

### 10.23 Socioemocional

```markdown
## Socioemocional {.socioemocional}

{Reflexión de 3-6 líneas que nombra la competencia de la Ley 2503/2025 que trabaja y conecta con el tema científico.}
```

---

## 11. Resumen de Secciones por Tipo

| Tipo               | Clase             | Cantidad | Títulos (Heading)                                                                                                                                                                                                                                                                                             |
|:------------------ | -----------------:|:--------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Teoría             | `.teoria`         | 1        | `## Teoría`                                                                                                                                                                                                                                                                                                   |
| Ideas Previas      | `.ideas-previas`  | 3        | `## Ideas Previas — Cuento`, `## Ideas Previas — Preguntas`, `## Ideas Previas — Contextualización`                                                                                                                                                                                                           |
| Feynman            | `.contexto`       | 1        | `## Contextualización — Método Feynman`                                                                                                                                                                                                                                                                       |
| Caracterizados DUA | `.caracterizados` | 6        | `## Contextualización — Apoyo Cognitivo y TDAH`, `## Contextualización — Visual`, `## Contextualización — Dislexia y Dificultades Lectoras`, `## Contextualización — Autismo y Pensamiento Concreto`, `## Contextualización — Accesibilidad Sensorial`, `## Contextualización — Socioemocional y Psicosocial` |
| Ejemplos           | `.ejemplo`        | 3        | `## Ejemplo — Nivel Bajo 🟢`, `## Ejemplo — Nivel Medio 🟡`, `## Ejemplo — Nivel Alto 🔴`                                                                                                                                                                                                                     |
| Ejercicios         | `.ejercicios`     | 3        | `## Ejercicios — Nivel Bajo 🟢`, `## Ejercicios — Nivel Medio 🟡`, `## Ejercicios — Nivel Alto 🔴`                                                                                                                                                                                                            |
| Retos              | `.retos`          | 1        | `## Retos`                                                                                                                                                                                                                                                                                                    |
| Aplicación         | `.aplicacion`     | 2        | `## Aplicación — Vida real`, `## Aplicación — Laboratorio` |
| Evaluación ICFES   | `.evaluacion`     | 1        | `## Evaluación — Tipo ICFES`                                                                                                                                                                                                                                                                                  |
| Socialización      | `.evaluacion`     | 1        | `## Socialización`                                                                                                                                                                                                                                                                                            |
| Socioemocional     | `.socioemocional` | 1        | `## Socioemocional`                                                                                                                                                                                                                                                                                           |

**Total: 23 bloques, 11 tipos de box.**

> Los 6 bloques Caracterizados DUA ahora incluyen internamente: teoría
> adaptada + ejemplo con autoinstrucciones + 2 ejercicios con opción de
> formato alternativo + metacognición + glosario (ver sección 9.4).

---

## 12. Referencias Bibliográficas

- Usar formato `[@autor año]` dentro del texto.
- Incluir `bibliography: ../../liber/references.bib` en el YAML del .qmd.

---

## 13. Casos Borde

| Situación                         | Acción                                               |
|:--------------------------------- |:---------------------------------------------------- |
| Entrada insuficiente o incompleta | Detener ejecución y reportar al orquestador          |
| Error en paso anterior            | No inventar datos faltantes; reportar                |
| Formato incompatible              | Usar Markdown estándar; evitar formatos propietarios |
