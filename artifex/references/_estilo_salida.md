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

### 6.1 Código de color para bloques Caracterizados

Usar este código fijo para guiar visualmente al estudiante:

- <span style="color:blue">**Azul**</span> → Primer dato / variable A
- <span style="color:red">**Rojo**</span> → Segundo dato / variable B / comparación
- <span style="color:green">**Verde**</span> → Resultado final

En HTML: `<span style="color:blue">texto</span>`.
En LaTeX dentro de `$$`: `\color{blue}texto`, `\color{red}texto`, `\color{green}texto`.
Aplicar dentro de los párrafos cortos de la teoría y dentro de las fórmulas en display math.

**Mapeo por dominio:**

| Dominio | <span style="color:blue">Azul (A)</span> | <span style="color:red">Rojo (B)</span> | <span style="color:green">Verde</span> | Relación |
|---------|:----:|:----:|:----:|:----:|
| Química | Reactivo A (CO) | Reactivo B (H₂) | Producto | Coeficientes |
| Física | Masa (kg) | Aceleración (m/s²) | Fuerza (N) | F = m × a |
| Biología | CO₂ | H₂O | Glucosa + O₂ | 6 : 6 → 1 |
| Matemáticas | Primer término | Segundo término | Solución (x) | Proporción |

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

---

#### Química: Reactivo limitante

Vamos paso a paso. Tú puedes.

Imagina una receta de sándwiches. Cada sándwich necesita 1 pan y 2 tajadas de queso. Si tienes 10 panes y 12 tajadas de queso, ¿cuántos sándwiches armas? Solo 6 — el queso se acaba primero.

En química funciona igual. La ecuación dice: <span style="color:blue">CO</span> + 2 <span style="color:red">H₂</span> → producto. Por cada 1 de <span style="color:blue">CO</span> necesitas 2 de <span style="color:red">H₂</span>.

Te dan la masa de <span style="color:blue">CO</span> y los moles de <span style="color:red">H₂</span>. Convierte la masa de <span style="color:blue">CO</span> a moles usando su masa molar. Luego compara usando los coeficientes.

$$
n_{\color{blue}CO} = \frac{m}{M_{\color{blue}CO}}, \qquad
\frac{n_{\color{blue}CO}}{1} \ : \ \frac{\color{red}n_{H_2}}{2}
$$

El cociente más pequeño te dice quién se acaba primero. Ese es tu reactivo limitante.

**Movimiento 1:** Anota la masa de CO y los moles de H₂ que te dan.  
**Movimiento 2:** Calcula moles de CO: masa ÷ masa molar del CO.  
**Movimiento 3:** Divide cada cantidad entre su coeficiente en la ecuación.  
**Movimiento 4:** El menor es el limitante. Úsalo para lo que pida el problema.

---

#### Física: Segunda Ley de Newton

Imagina que empujas una caja. Si es pesada, cuesta más moverla. Si empujas más fuerte, acelera más. Fuerza, masa y aceleración están conectadas.

Newton lo resumió en una fórmula. <span style="color:blue">La masa</span> se mide en kilogramos. <span style="color:red">La aceleración</span> se mide en metros por segundo al cuadrado. <span style="color:green">La fuerza</span> es el empujón, en newtons.

Multiplicas masa por aceleración y obtienes fuerza. Es así de directo.

$$
\color{green}F = \color{blue}m \times \color{red}a
$$

Tú puedes resolverlo. Solo identifica qué dato falta y despeja.

**Movimiento 1:** Lee el problema. ¿Te piden fuerza, masa o aceleración?  
**Movimiento 2:** Escribe los datos con sus unidades: kg para masa, m/s² para aceleración.  
**Movimiento 3:** Aplica F = m × a. Si falta F, multiplica. Si falta m o a, divide.  
**Movimiento 4:** Revisa la unidad del resultado. Los newtons son kg·m/s².

---

#### Biología: Fotosíntesis

Las plantas son pequeñas fábricas de comida. Toman dióxido de carbono del aire, agua del suelo y luz del sol. Con eso producen su alimento.

La ecuación es esta: 6 de <span style="color:blue">CO₂</span> y 6 de <span style="color:red">H₂O</span>, con luz solar, producen <span style="color:green">glucosa y oxígeno</span>.

La relación es 6 a 6. Por cada 6 moléculas de <span style="color:blue">CO₂</span> necesitas 6 de <span style="color:red">H₂O</span>. Es uno a uno.

$$
\color{blue}6CO_2 + \color{red}6H_2O \xrightarrow{luz} \color{green}C_6H_{12}O_6 + 6O_2
$$

Los coeficientes te guían. Tú puedes usarlos para relacionar las cantidades.

**Movimiento 1:** Identifica los reactivos: CO₂ y H₂O. Anota sus coeficientes.  
**Movimiento 2:** Identifica los productos: glucosa (C₆H₁₂O₆) y oxígeno (O₂).  
**Movimiento 3:** Usa la proporción 6:6:1:6 para conectar las cantidades.  
**Movimiento 4:** Convierte entre moléculas, moles o masas según lo que pidan.

---

#### Matemáticas: Proporciones

Imagina una receta de limonada. Por cada 2 limones usas 3 cucharadas de azúcar. Si tienes 6 limones, ¿cuánta azúcar necesitas? Es una regla de tres.

Las proporciones comparan dos razones iguales. <span style="color:blue">El primer término (A)</span> se relaciona con <span style="color:red">el segundo (B)</span>. Buscas <span style="color:green">el valor de x</span> que mantiene la misma relación.

Planteas dos fracciones iguales y multiplicas en cruz.

$$
\frac{\color{blue}A}{\color{red}B} = \frac{\color{green}x}{C}
$$

Multiplica en cruz y despeja. Tú puedes hacerlo en tres pasos.

**Movimiento 1:** Escribe la proporción conocida: A sobre B.  
**Movimiento 2:** Iguala a la otra fracción. Coloca x arriba y el valor conocido abajo.  
**Movimiento 3:** Multiplica en cruz: x × B = A × C.  
**Movimiento 4:** Despeja x dividiendo. Revisa si el resultado tiene sentido.

---

**Ejemplo:** {Enunciado con datos. Autoinstrucciones ACTIVAS: "Ahora tapa el siguiente paso y explica en voz alta por qué haces esa operación." Pasos numerados con operación y resultado.}

**Ejercicios:**

1. {Ejercicio 1. **Opción de respuesta:** escrito | oral. Checklist: [ ] Dato 1 [ ] Dato 2 [ ] Cálculo [ ] Resultado. Incluir: "Después de resolver, tapa el resultado y explicaselo a un compañero imaginario."}
2. {Ejercicio 2. **Opción de respuesta:** escrito | oral.}

**Metacognición (verificación conceptual):** "Explica con tus palabras la relación entre A y B. ¿Qué cambiaría si la proporción fuera 3:1?"

**Glosario:** {3-5 términos con definiciones en 1 oración.}
```

### 10.7 Contextualización — Visual

```markdown
## Contextualización — Visual {.caracterizados}

{Voz de guía visual: "observa cómo", "mira la tabla", "nota los colores".
Cada color te dice qué papel juega cada elemento.}

---
#### Química: Reactivo limitante

<span style="color:blue">Observa cómo</span> el reactivo limitante determina cuánto producto se forma. <span style="color:red">Mira la tabla</span> con los datos iniciales. <span style="color:green">Como puedes ver</span>, el reactivo que se consume primero marca el final de la reacción.

| Dato | Cantidad | Valor clave |
|:-----|:--------:|:-----------:|
| <span style="color:blue">CO (A)</span> | 4 mol | 4 ÷ 1 = **4** |
| <span style="color:red">H₂ (B)</span> | 6 mol | 6 ÷ 2 = **3** |

Cada uno produce:

$$\frac{\color{blue}4}{1} = 4,\qquad \frac{\color{red}6}{2} = 3$$

<span style="color:green">**Resultado:** El H₂ es el reactivo limitante.</span>

---
#### Física: Segunda Ley de Newton

<span style="color:blue">Observa cómo</span> la fuerza relaciona masa y aceleración. <span style="color:red">Mira la tabla</span> con las variables. <span style="color:green">Como puedes ver</span>, la fuerza es el producto de ambas.

| Dato | Cantidad | Operación |
|:-----|:--------:|:---------:|
| <span style="color:blue">Masa (m)</span> | 4 kg | — |
| <span style="color:red">Aceleración (a)</span> | 3 m/s² | — |

Aplica la fórmula:

$${\color{green}F} = {\color{blue}4\ \text{kg}} \times {\color{red}3\ \text{m/s}^2} = {\color{green}12\ \text{N}}$$

<span style="color:green">**Resultado:** La fuerza neta es 12 N.</span>

---
#### Biología: Fotosíntesis

<span style="color:blue">Observa cómo</span> la fotosíntesis convierte energía lumínica en química. <span style="color:red">Mira la tabla</span> con reactivos y productos. <span style="color:green">Como puedes ver</span>, la relación estequiométrica es 6:6:1.

| Reactivo | Cantidad | Coeficiente |
|:---------|:--------:|:-----------:|
| <span style="color:blue">CO₂ (A)</span> | 6 moléculas | 6 |
| <span style="color:red">H₂O (B)</span> | 6 moléculas | 6 |
| <span style="color:green">Glucosa</span> | 1 molécula | 1 |

La ecuación completa:

$$6{\color{blue}CO_2} + 6{\color{red}H_2O} \xrightarrow{luz} {\color{green}C_6H_{12}O_6} + 6O_2$$

<span style="color:green">**Resultado:** Se produce 1 glucosa y 6 oxígeno.</span>

---
#### Matemáticas: Proporciones

<span style="color:blue">Observa cómo</span> las proporciones relacionan dos términos. <span style="color:red">Mira la tabla</span> con los valores conocidos. <span style="color:green">Como puedes ver</span>, se resuelve despejando la incógnita.

| Dato | Valor |
|:-----|:-----:|
| <span style="color:blue">Término A</span> | 2 |
| <span style="color:red">Término B</span> | 3 |
| <span style="color:green">Solución x</span> | ? |

Plantea la proporción:

$$\frac{\color{blue}2}{\color{red}3} = \frac{x}{6},\qquad x = \frac{2 \times 6}{3} = {\color{green}4}$$

<span style="color:green">**Resultado:** x = 4.</span>

---
**Ejemplo:** {Datos en tabla Markdown. Diagrama de flujo: entrada -> paso 1 -> paso 2 -> resultado. Autoinstrucción activa visual: "Cubre los valores y reconstruye el diagrama desde tu memoria."}

**Ejercicios:**

1. {Tabla incompleta. **Opción de respuesta:** completar tabla | dibujar diagrama.}
2. {Crear tu propio organizador visual del concepto.}

**Metacognición (verificación conceptual):** "Dibuja o describe lo que aprendiste. ¿Cómo se ven los elementos A y B antes y después?" Tabla 2 columnas: ¿Qué aprendí? / ¿Cómo lo representaría visualmente?

**Glosario:** {3-5 términos con definiciones + referente visual entre paréntesis.}
```

### 10.8 Contextualización — Dislexia y Dificultades Lectoras

```markdown
## Contextualización — Dislexia y Dificultades Lectoras {.caracterizados}

{Voz conversacional: "tú", "ahora haz esto". Frases cortas.
Sin metaforas. Sin dobles negaciones. Max 15 palabras por oracion.}

---
#### Quimica

El numero <span style="color:blue">azul</span> dice cuantas moleculas de A tenes.
A es <span style="color:blue">CO</span>.
El numero <span style="color:red">rojo</span> dice cuantas moleculas de B tenes.
B es <span style="color:red">H₂</span>.
La proporcion entre A y B es 1 a 2.
El que se acaba primero es la respuesta.

$${\color{blue}n_{CO}} = 4\ \text{mol},\quad {\color{red}n_{H_2}} = 6\ \text{mol}$$
$${\color{blue}4} \div {\color{blue}1} = 4,\quad {\color{red}6} \div {\color{red}2} = 3$$

El que da menos es el limitante.

---
#### Fisica

La segunda ley de Newton relaciona fuerza, masa y aceleracion.
<span style="color:blue">Masa</span> es cuanto pesa algo.
<span style="color:red">Aceleracion</span> es el cambio de velocidad.
<span style="color:green">Fuerza</span> es el resultado.

$${\color{blue}m} = 4\ \text{kg},\quad {\color{red}a} = 3\ \text{m/s}^2$$
$${\color{green}F} = {\color{blue}m} \times {\color{red}a} = 12\ \text{N}$$

Multiplica masa por aceleracion.

---
#### Biologia

La fotosintesis convierte <span style="color:blue">CO₂</span> y <span style="color:red">H₂O</span>
en <span style="color:green">glucosa</span> y oxigeno.
La planta usa energia solar para esto.

$$6{\color{blue}CO_2} + 6{\color{red}H_2O} \rightarrow {\color{green}C_6H_{12}O_6} + 6{\color{green}O_2}$$

Seis de cada uno producen una glucosa.

---
#### Matematicas

Las proporciones tienen dos terminos.
<span style="color:blue">Azul</span> es el primer termino.
<span style="color:red">Rojo</span> es el segundo termino.
<span style="color:green">X</span> es el resultado.

$$\frac{\color{blue}2}{\color{red}3} = \frac{x}{6},\qquad {\color{green}x} = 4$$

Multiplica cruzado para hallar x.

---
**Ejemplo:** {Enunciado en 1-2 oraciones. Pasos con -> entre cálculo y resultado. Autoinstrucción activa: "Ahora tapa los pasos y explica en voz alta el primer paso. ¿Qué tenés que hacer primero?"}

**Ejercicios:**

1. {Enunciado corto. **Opción de respuesta:** escribir | grabar audio.}
2. {Enunciado corto. Verificación activa: "Explica con tus palabras lo que hiciste como si se lo contaras a un amigo de 10 años."}

**Metacognición (verificación conceptual):** "Sin leer la teoría otra vez, explica cuál es la relación entre A y B. Usa tu voz."

**Glosario:** {3-5 términos con pictograma ARASAAC + definición en 1 oración.}
```

### 10.9 Contextualización — Autismo y Pensamiento Concreto

```markdown
## Contextualización — Autismo y Pensamiento Concreto {.caracterizados}

{Voz de manual de instrucciones: literal, predecible, misma estructura
siempre. Sin metaforas, sin ironia, sin lenguaje figurado.}

---
#### Quimica

**Regla fija:** la ecuacion balanceada indica la proporcion exacta entre sustancias.
[1] Regla: la ecuacion dice cuantas moleculas de cada tipo participan.
[2] Formula: compara la cantidad disponible con la necesaria.
[3] Calculo: divide los moles disponibles entre el coeficiente de cada reactivo.

<span style="color:blue">CO</span> + 2<span style="color:red">H₂</span> → producto.
<span style="color:blue">1</span> de CO y <span style="color:red">2</span> de H₂.
<span style="color:blue">4 moles de CO</span> y <span style="color:red">6 moles de H₂</span>.

$${\color{blue}n_{CO}} = 4,\quad {\color{red}n_{H_2}} = 6$$
$$\frac{\color{blue}4}{\color{blue}1} = 4,\quad \frac{\color{red}6}{\color{red}2} = 3$$

<span style="color:red">H₂</span> da 3. Es el limitante.

---
#### Fisica

**Regla fija:** la fuerza se calcula multiplicando masa por aceleracion.
[1] Regla: F = m × a.
[2] Formula: F = m · a.
[3] Calculo: multiplicar kg por m/s².

<span style="color:blue">Masa (m)</span> = 4 kg.
<span style="color:red">Aceleracion (a)</span> = 3 m/s².

$${\color{blue}m} = 4\ \text{kg},\quad {\color{red}a} = 3\ \text{m/s}^2$$
$${\color{green}F} = {\color{blue}4} \times {\color{red}3} = 12\ \text{N}$$

<span style="color:green">Fuerza</span> = 12 newtons.

---
#### Biologia

**Regla fija:** 6 moleculas de CO₂ y 6 de H₂O producen 1 glucosa.
[1] Regla: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.
[2] Formula: glucosa = min(CO₂/6, H₂O/6).
[3] Calculo: dividir las moleculas de cada reactivo entre 6.

<span style="color:blue">12 moleculas de CO₂</span>.
<span style="color:red">18 moleculas de H₂O</span>.

$${\color{blue}n_{CO_2}} = 12,\quad {\color{red}n_{H_2O}} = 18$$
$$\frac{\color{blue}12}{6} = 2,\quad \frac{\color{red}18}{6} = 3$$

El <span style="color:blue">CO₂</span> da 2. Es el limitante.

---
#### Matematicas

**Regla fija:** dos razones iguales forman una proporcion.
[1] Regla: a/b = c/x → x = (b · c) / a.
[2] Formula: a/b = c/x.
[3] Calculo: multiplicar en cruz y despejar.

<span style="color:blue">a = 2</span>, <span style="color:red">b = 4</span>, <span style="color:green">c = 5</span>.

$${\color{blue}a} = 2,\quad {\color{red}b} = 4,\quad {\color{green}c} = 5$$
$$x = \frac{{\color{red}4} \times {\color{green}5}}{\color{blue}2} = {\color{green}10}$$

<span style="color:green">x = 10</span>. Se cumple que 2/4 = 5/10.

---
**Ejemplo:** {Enunciado literal. Checklist de pasos. Autoinstrucción activa literal: "Ahora aplica la regla al revés: si te doy el resultado, reconstruí los pasos."}

**Ejercicios:**

1. {Aplica la regla fija. **Opción de respuesta:** resolver | emparejar pasos con resultados.}
2. {¿Aplica la regla? SI/NO (decidir, no solo aplicar mecánicamente).}

**Metacognición (verificación conceptual):** "Sin mirar el bloque, escribí la regla fija con tus palabras. ¿Qué dice sobre la relación entre A y B?"

**Glosario:** {3-5 términos con definición literal + ejemplo concreto.}
```

### 10.10 Contextualización — Accesibilidad Sensorial

```markdown
## Contextualización — Accesibilidad Sensorial {.caracterizados}

{Voz de audiodescriptor: "localiza", "desplázate a", "señala con el dedo".
Cada instrucción funciona sin depender de la vista.}

---
#### Quimica

Desliza el dedo sobre las fichas.
Las rugosas son <span style="color:blue">CO</span> (color azul).
Las suaves son <span style="color:red">H₂</span> (color rojo).
Forma dos montones: 4 azules rugosas a la izquierda, 6 rojas suaves a la derecha.

Toma una azul y escucha: necesitas 2 rojas para armar un par.
Arma los pares uno por uno. Con 4 azules ocupas 8 rojas, pero solo hay 6.
Las rojas suaves se terminan primero. El movimiento se detiene.

$${\color{blue}4} \div {\color{blue}1} = 4,\qquad {\color{red}6} \div {\color{red}2} = 3$$

<span style="color:red">B</span> da 3. Es la respuesta.
Señala con el dedo el numero mas pequeño. Ese es.

---
#### Fisica

Apoya las palmas sobre las fichas.
Las <span style="color:blue">pesadas</span> son la masa (azul).
Las <span style="color:red">ligeras</span> son la aceleracion (rojo).
La azul pesa 4 kg y resiste el movimiento.
La roja se desliza a 3 m/s².

La fuerza que sientes en las manos combina ambas.
Mientras mas pesada la ficha o mas rapido empujes, mas fuerza necesitas.

$${\color{blue}m} = 4\ \text{kg},\quad {\color{red}a} = 3\ \text{m/s}^2$$
$${\color{green}F} = {\color{blue}4} \times {\color{red}3} = {\color{green}12\ \text{N}}$$

<span style="color:green">12 newtons</span> de fuerza. Señala el resultado con el dedo.

---
#### Biologia

Imagina burbujas que suben.
Las <span style="color:blue">azules</span> son CO₂, burbujas de aire livianas al tocarlas.
Las <span style="color:red">rojas</span> son H₂O, gotas que mojan la yema del dedo.
Junta 6 burbujas azules y 6 gotas rojas.
Escucha el burbujeo mientras se mezclan.

Agrega luz. La energia mueve las moleculas.
Las burbujas azules de CO₂ y las gotas rojas de H₂O se transforman.

$$6{\color{blue}CO_2} + 6{\color{red}H_2O} \rightarrow {\color{green}C_6H_{12}O_6} + 6{\color{green}O_2}$$

Toca cada molecula: el CO₂ azul se consume, el H₂O rojo desaparece,
y la glucosa verde aparece.

---
#### Matematicas

Pasa el dedo por las fichas numeradas.
Las <span style="color:blue">azules</span> tienen el 2 y textura rayada.
Las <span style="color:red">rojas</span> tienen el 3 y textura punteada.
La relacion entre ellas dice: 2 es a 3 como x es a 6.

Señala cada par mientras los contas.
Multiplica en cruz: 2 × 6 = 3 × x.

$$\frac{\color{blue}2}{\color{red}3} = \frac{x}{\color{green}6}$$
$${\color{green}x} = 4$$

Escucha: 2 es a 3 como 4 es a 6.

---
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

{Voz cálida y contenedora: "vamos a", "juntos", "está bien si...",
"respira". Validar antes de instruir. Cerrar con afirmación positiva.}

---
#### Quimica

Vamos a hacerlo juntos, como cuando preparamos una receta en comunidad.
Para hacer un pastel necesitas 2 tazas de harina y 1 huevo.
Tienes 4 tazas de harina pero solo 3 huevos.
El ingrediente que se acaba primero decide cuánto alcanza.

<span style="color:blue">CO</span> y <span style="color:red">H₂</span>
son como la harina y los huevos de nuestra receta.
Cada uno necesita una cantidad específica del otro para reaccionar.

Respira hondo 3 veces. Cierra los ojos un momento y suelta el aire despacio.

$${\color{blue}CO} + 2{\color{red}H_2} \rightarrow {\color{green}CH_3OH}$$

<span style="color:blue">4 moles de CO</span> y <span style="color:red">6 moles de H₂</span>.
Por cada mol de CO necesitas 2 de H₂.

$$\frac{\color{blue}4}{\color{blue}1} = 4,\qquad \frac{\color{red}6}{\color{red}2} = 3$$

<span style="color:red">H₂</span> da 3. Es el reactivo limitante.
Lo lograste. Cada problema que resuelves te fortalece. Tú puedes.

---
#### Fisica

Vamos paso a paso, como cuando en tu comunidad se organizan para mover algo pesado.
Imagina que entre todas las personas del salón empujan un carro.
<span style="color:blue">El carro tiene cierta masa</span> y logran que se mueva
con cierta <span style="color:red">aceleracion</span>.

La <span style="color:green">fuerza</span> que aplican juntas depende de esas dos cosas.
Entre mas pesado, mas fuerza se necesita. Entre mas rapido quieren moverlo, mas fuerza tambien.

Respira profundo. Siente el aire llenar tus pulmones. Suelta despacio.

$${\color{green}F} = {\color{blue}m} \cdot {\color{red}a}$$

<span style="color:blue">Masa</span> = 500 kg. <span style="color:red">Aceleracion</span> = 2 m/s².

$${\color{green}F} = {\color{blue}500} \times {\color{red}2} = {\color{green}1000\ \text{N}}$$

Cada persona pone su fuerza y juntas logran moverlo.
Tu conocimiento crece cada vez que aplicas lo que aprendes. Vas muy bien.

---
#### Biologia

Vamos a descubrirlo juntos, con la misma paciencia con la que una planta crece.
<span style="color:blue">CO₂</span> del aire y <span style="color:red">H₂O</span>
del suelo son los ingredientes. La planta los transforma
en <span style="color:green">glucosa</span>, su alimento, y libera oxigeno.

Es un intercambio hermoso: la planta nos da oxigeno y nosotros CO₂.
Todo esta conectado.

Respira profundo. El aire que entra tiene oxigeno que las plantas produjeron.
El aire que sale tiene CO₂ que las plantas necesitan.

$$6{\color{blue}CO_2} + 6{\color{red}H_2O} \rightarrow {\color{green}C_6H_{12}O_6} + 6O_2$$

<span style="color:blue">6 de CO₂</span> y <span style="color:red">6 de agua</span>
producen <span style="color:green">1 glucosa</span>.

Asi como la planta crece con cuidados, tu conocimiento tambien brota. Sigue asi.

---
#### Matematicas

Vamos a hacerlo juntos, como cuando en tu comunidad reparten recursos de manera justa.
Acordaron que por cada 2 lapices se necesitan 3 hojas.
Si un grupo tiene 6 lapices, ¿cuantas hojas le corresponden?

<span style="color:blue">Un termino</span> se relaciona con <span style="color:red">el otro</span>
de la misma forma en ambos lados. Es como cuando en tu casa reparten las tareas:
si todos ponen la misma dedicacion, el trabajo se distribuye equitativamente.

Respira hondo 3 veces. Suelta la tension de los hombros.

$$\frac{\color{blue}2}{\color{red}3} = \frac{6}{\color{green}x}$$
$${\color{blue}2} \cdot {\color{green}x} = {\color{red}3} \cdot 6$$
$${\color{green}x} = \frac{18}{2} = {\color{green}9}$$

<span style="color:green">9 hojas</span> le corresponden al grupo. La proporcion se mantiene.

Lo hiciste. Cada proporcion que resuelves usa el mismo razonamiento
que en comunidad para repartir recursos de manera equitativa.

---
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
