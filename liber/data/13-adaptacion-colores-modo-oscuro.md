# Guía de Adaptación de Colores para Modo Oscuro (Dark Mode)

El diseño de interfaces en **Modo Oscuro (Dark Mode)** no consiste simplemente en invertir los colores (pasar el fondo a negro y el texto a blanco). Las directrices de **Material Design** y los estándares de accesibilidad **WCAG (Web Content Accessibility Guidelines)** establecen reglas estrictas sobre el manejo del color, la saturación y el contraste para proteger la salud visual del usuario y garantizar la legibilidad.

---

## 1. El Problema: Vibración Visual y Fatiga Ocular

En un tema claro (Light Mode), los colores primarios y de acento suelen ser muy saturados y vibrantes (alta saturación en el modelo HSL) para destacar sobre fondos blancos o grises claros. 

Sin embargo, cuando estos mismos colores de alta saturación se aplican sobre fondos muy oscuros (negros o grises oscuros profundos), ocurre un fenómeno óptico conocido como **"vibración visual"**.

### ¿Qué causa la vibración visual?
El contraste simultáneo entre un fondo oscuro absoluto y un color brillante y altamente saturado hace que los bordes del color parezcan difuminarse, "sangrar" o vibrar. Esto obliga al ojo humano a reenfocar constantemente, provocando:
- **Tensión ocular (Eye Strain):** Contrarresta directamente los beneficios ergonómicos del modo oscuro.
- **Dificultad de lectura:** El texto coloreado o los iconos con colores vibrantes pierden nitidez.
- **Sobrecarga cognitiva:** Un diseño que debería sentirse relajante termina siendo visualmente agresivo.

---

## 2. La Regla de Oro: Desaturar Colores (Ajuste HSL)

Para evitar la vibración visual y cumplir con los criterios de accesibilidad, Material Design recomienda **desaturar los colores primarios** cuando se usan en superficies oscuras.

En el modelo de color **HSL (Hue, Saturation, Lightness / Tono, Saturación, Luminosidad)**, la conversión segura de un color de Modo Claro a Modo Oscuro implica:

1. **Mantener el Tono (Hue):** Para conservar la identidad visual de la marca.
2. **Reducir la Saturación (Saturation):** Disminuir drásticamente la intensidad del color para evitar que vibre.
3. **Aumentar la Luminosidad (Lightness):** Elevar la cantidad de blanco en el color para que mantenga un buen contraste de legibilidad contra el fondo oscuro.

### Ejemplo de Conversión HSL
Supongamos que nuestro color primario (Modo Claro) es un azul vibrante:
- **Light Mode:** `HSL(220, 80%, 50%)` (Alta saturación, luminosidad media)

Para pasarlo a **Dark Mode**, debemos ajustarlo:
- **Dark Mode:** `HSL(220, 40%, 70%)` (Saturación reducida a la mitad, luminosidad aumentada)

El resultado es un tono azul más suave, pastel (desaturado), que es claramente visible sobre un fondo oscuro, pero sin ser agresivo para la vista.

---

## 3. Criterios de Accesibilidad WCAG (Contraste)

Al ajustar la saturación y la luminosidad, es obligatorio verificar que los colores sigan cumpliendo con las pautas WCAG (nivel AA como mínimo):

- **4.5:1** – Relación de contraste mínima requerida para **texto normal** (menor a 18pt o 14pt en negrita).
- **3.0:1** – Relación de contraste mínima para **textos grandes** y **componentes de interfaz de usuario** (como bordes de campos de entrada, botones o iconos).

Los colores pastel desaturados en modo oscuro logran fácilmente estas proporciones métricas frente a un gris oscuro (como `#121212`), mientras que los colores muy saturados suelen fallar las pruebas de contraste WCAG porque, paradójicamente, no tienen suficiente luminancia.

---

## 4. Buenas Prácticas y Resumen de Directrices

1. **Evita el negro puro:** Material Design sugiere usar gris oscuro (ej. `#121212`) como color de superficie (surface color) en lugar de negro puro (`#000000`). Esto reduce el contraste extremo, minimizando la fatiga visual, y permite expresar elevación a través de sombras ligeras.
2. **Usa paletas tonales 200/50:** Si tu sistema de diseño (como Material 2 o 3) usa escalas tonales del 0 al 1000, los tonos alrededor del 500 a 700 son comunes en modo claro. En modo oscuro, deberías recurrir a los tonos **200**, que son naturalmente más desaturados y luminosos.
3. **Fichas Semánticas (Design Tokens):** Implementa variables como `color-primary` que automáticamente apunten a `color-blue-500` en modo claro y a `color-blue-200` en modo oscuro.

**Conclusión:**
Adaptar colores al modo oscuro es un ejercicio matemático de reducción de saturación e incremento de luminancia. Un color desaturado garantiza legibilidad (aprobando WCAG) y protege los ojos del usuario de vibraciones ópticas molestas.
