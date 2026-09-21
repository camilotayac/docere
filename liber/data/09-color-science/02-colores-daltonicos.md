# Reporte de Investigación: Accesibilidad Visual y Colores para Daltónicos en Contextos Educativos

## 1. Introducción a la Accesibilidad Visual Educativa
En el ámbito educativo, los materiales visuales como gráficos, diagramas, presentaciones y libros de texto dependen fuertemente del color para clasificar, enfatizar y organizar información. Sin embargo, cuando se diseña sin considerar la accesibilidad, se levantan barreras cognitivas significativas para los estudiantes con deficiencias en la visión del color (DVC), coloquialmente conocido como daltonismo. El diseño universal (CUD) exige metodologías sistemáticas para que la información transmitida por el color se perciba equitativamente, independientemente del tipo de fotorreceptores (conos) del estudiante. Este reporte analiza profundamente los fundamentos biológicos, estadísticos, estándares de la industria (WCAG 3.0), implementaciones de código (CSS `forced-colors`) y paletas validadas científicamente para entornos de aprendizaje.

## 2. Tipos de Daltonismo, Fisiología y Estadísticas de Frecuencia
El daltonismo no es una ceguera total, sino una anomalía en la percepción del color causada por mutaciones genéticas que afectan a los conos en la retina. Existen tres familias principales:

### Protanopía y Protanomalía
Afectan a los conos "L" (sensibles a longitudes de onda largas, correspondientes al rojo). En la protanopía, los conos L están completamente ausentes (dicromatismo). En la protanomalía, los conos están presentes pero mutados, con un pico de sensibilidad desplazado (tricromatismo anómalo).
- **Frecuencia (Hombres):** ~1% protanopía, ~1% protanomalía.
- **Frecuencia (Mujeres):** Muy rara (<0.1%).
- **Efecto visual:** Los colores rojos se ven considerablemente más oscuros, perdiendo luminosidad. Un rojo intenso puede percibirse como negro o marrón muy oscuro, dificultando la lectura de alertas o errores marcados en rojo.

### Deuteranopía y Deuteranomalía
Afectan a los conos "M" (sensibles a longitudes de onda medias, verde). La deuteranopía es la ausencia total, mientras que la deuteranomalía es la mutación de estos conos. Es el tipo más frecuente en el mundo.
- **Frecuencia (Hombres):** ~5% deuteranomalía, ~1.5% deuteranopía.
- **Frecuencia (Mujeres):** ~0.35%.
- **Efecto visual:** Es la principal causa del clásico "daltonismo rojo-verde". A diferencia de los protanopes, los deuteranopes no sufren oscurecimiento del canal rojo, pero confunden los mismos ejes cromáticos al perder la dimensión verde.

### Tritanopía y Tritanomalía
Afectan a los conos "S" (sensibles a longitudes de onda cortas, azul). Es una condición autosómica (cromosoma 7), no ligada al cromosoma X, por lo que su prevalencia es idéntica en hombres y mujeres.
- **Frecuencia (Global):** <0.01% - 0.05%.
- **Efecto visual:** El eje azul-amarillo queda inhabilitado. El espectro se reduce a tonos de rojo, cian y verde.

### Monocromatismo y Acromatopsia
Condición extremadamente rara (<0.003%) donde el individuo no tiene conos funcionales, viendo el mundo en escala de grises. Estos estudiantes dependen 100% del contraste de luminancia.

**Prevalencia Total:** En una clase de 30 estudiantes (15 hombres, 15 mujeres), hay una probabilidad superior al 60% de tener al menos un estudiante (casi siempre varón) con algún grado de DVC. Aproximadamente el 8% de los hombres y 0.5% de las mujeres a nivel mundial nacen con daltonismo.

---

## 3. Tabla de Confusión de Colores y Zonas de Riesgo

Para garantizar que el material educativo sea seguro, es crítico evitar codificar información exclusivamente usando pares de colores situados en las mismas "líneas de confusión". 

| Tipo de DVC | Eje Afectado | Pares Problemáticos (Colores Confundidos) |
| :--- | :--- | :--- |
| **Deuteranopía** | Verde | Rojo ↔ Verde; Naranja ↔ Amarillo ↔ Verde; Morado ↔ Azul; Rojo ↔ Marrón; Rosa ↔ Gris. |
| **Protanopía** | Rojo | Rojo oscuro ↔ Negro; Rojo ↔ Verde; Naranja ↔ Verde claro; Cian ↔ Gris; Rosa ↔ Azul/Gris. |
| **Tritanopía** | Azul | Azul ↔ Verde; Amarillo ↔ Violeta/Rosa claro; Naranja ↔ Rojo. |

*Notas sobre colores críticos:* El rojo puro contra el verde puro es la pesadilla del diseño. Un gráfico de barras donde el rendimiento positivo es verde y el negativo es rojo será indescifrable para casi el 6% del alumnado masculino, siendo ambos colores percibidos como un tono caqui o marrón amarillento, variando solo ligeramente en brillo.

---

## 4. Paletas Científicamente Validadas y Seguras

Para evitar las zonas de confusión, la comunidad científica ha desarrollado diversas paletas estándar que maximizan las distancias perceptuales para observadores con DVC, manteniendo al mismo tiempo un aspecto profesional y balanceado para aquellos con visión normal.

### Paleta de Masataka Okabe y Kei Ito (CUD / Wong Palette)
Diseñada originalmente bajo los principios del Diseño Universal de Color (CUD) en Japón, fue popularizada en la revista *Nature Methods* (2011) por Bang Wong. Es el estándar de oro para datos categóricos en educación STEM (matemáticas, biología, química).

| Nombre de Color | HEX | RGB | Recomendación de Uso |
| :--- | :--- | :--- | :--- |
| Negro | `#000000` | (0, 0, 0) | Textos principales, contornos, ejes de gráficas. |
| Naranja | `#E69F00` | (230, 159, 0) | Categoría A (Excelente sustituto del rojo). |
| Azul Cielo | `#56B4E9` | (86, 180, 233) | Categoría B. |
| Verde Azulado | `#009E73` | (0, 158, 115) | Categoría C (Sustituto seguro del verde puro). |
| Amarillo | `#F0E442` | (240, 228, 66) | Resaltados, advertencias. |
| Azul | `#0072B2` | (0, 114, 178) | Categoría D (Contrasta fuerte con el Naranja). |
| Bermellón | `#D55E00` | (213, 94, 0) | Alertas de error, valores negativos. |
| Púrpura Rojizo | `#CC79A7` | (204, 121, 167) | Categoría F. |

### Paletas de Paul Tol (Scientific Visualization)
Paul Tol (SRON) creó paletas extensas, ideales para mapas térmicos, secuencias continuas e información divergente (Ej. mapas climáticos o atlas anatómicos).

**Paul Tol Bright (Cualitativa):** Muy distintiva para líneas y puntos.
- Azul: `#4477AA`
- Rojo: `#EE6677`
- Verde: `#228833`
- Amarillo: `#CCBB44`
- Cian: `#66CCEE`
- Morado: `#AA3377`
- Gris: `#BBBBBB`

**Paul Tol High Contrast:** Ideal para UI/UX y destacar máximo tres estados.
- Azul Oscuro: `#004488`
- Oro/Mostaza: `#DDAA33`
- Carmesí: `#BB5566`

---

## 5. Simulación de Daltonismo y Pruebas Ishihara: Directrices de Diseño

Para verificar si un material educativo es accesible, los desarrolladores utilizan simulaciones basadas en las placas de Ishihara. Las placas pseudoisocromáticas de Ishihara funcionan mediante la eliminación del contraste de luminosidad (brillo). En estas placas, los puntos que forman un número tienen la misma luminosidad que los puntos del fondo, diferenciándose exclusivamente por el tono (hue). Si un diseñador construye basándose únicamente en el tono (como sucede en Ishihara), los alumnos con DVC perderán la información.

**Directriz de Diseño de Contraste (La regla de oro del doble cifrado):**
1. **Nunca dependas únicamente del color:** Todo color debe estar respaldado por un indicador secundario. En química, si usas colores para tipos de átomos (rojo oxígeno, gris carbono), incluye letras u opciones de texturas y patrones (rayado, punteado).
2. **Garantiza diferencias de Luminancia (Lightness):** Usa herramientas HSL (Hue, Saturation, Lightness). El secreto para un diseño accesible es variar fuertemente el canal "L" (Lightness). Un rojo oscuro (`#8B0000`, L: 27%) y un verde muy claro (`#90EE90`, L: 75%) se distinguirán perfectamente incluso en monocromacia debido a su diferencia de brillo.
3. **Revisión en Escala de Grises:** El filtro más rápido; si la interfaz o gráfico se entiende en blanco y negro, entonces supera las barreras del daltonismo.

---

## 6. WCAG 3.0, APCA y el Futuro del Contraste de Color
Las WCAG 2.1 actuales exigen contrastes de luminancia relativa matemática (4.5:1 para texto normal, 3:1 para grandes textos y UI). Sin embargo, este método falla en percibir cómo el ojo humano procesa los colores en diferentes contextos de pantalla y polaridades (texto claro sobre oscuro vs oscuro sobre claro).

**La Revolución de WCAG 3.0 (APCA):**
El Advanced Perceptual Contrast Algorithm (APCA) cambia la evaluación estática por una dinámica. APCA calcula una puntuación basada en la sensibilidad visual humana real al contraste espacial.
- Es muy beneficioso para estudiantes con DVC y baja visión porque tiene en cuenta el peso y tamaño de la tipografía.
- Un texto fino rojo sobre fondo negro podría pasar en WCAG 2.1, pero APCA lo penalizaría severamente porque el rojo oscuro es prácticamente invisible para la protanopía (carece de luminosidad).
- **Implicación Educativa:** Los componentes clave (botones de "Siguiente lección", respuestas de exámenes) deberán asegurar contrastes de luminancia perceptual superior (Lc 75 o Lc 90) para prevenir frustración y fallos por clics equivocados.

---

## 7. Accesibilidad CSS: `forced-colors` y High Contrast
En un aula diversa, algunos estudiantes no dependerán de nuestra paleta, sino que activarán modos de alto contraste a nivel de Sistema Operativo (como el Windows High Contrast Mode). Cuando el usuario activa esto, el navegador sobreescribe forzosamente los colores de la página.

La media query `@media (forced-colors: active)` detecta este estado. El error más común de los desarrolladores es tratar de restaurar su diseño original (`forced-color-adjust: none`), lo cual arruina la experiencia de accesibilidad de este usuario.

**Recomendaciones CSS para Modos Educativos:**
```css
/* Modo normal */
.boton-examen {
  background-color: #0072B2; /* Azul seguro Okabe */
  color: white;
  border: none;
  box-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Sombra que se perderá en forced-colors */
}

/* Modo forzado: Preservando semántica */
@media (forced-colors: active) {
  .boton-examen {
    /* Agregamos un borde porque los fondos y sombras se eliminarán */
    border: 2px solid ButtonText; 
    /* El sistema controla colores como ButtonText, Canvas, Highlight */
  }
  
  .grafica-svg-linea {
    /* Forzamos a que las líneas sean de colores de sistema para asegurar contraste */
    stroke: CanvasText;
  }
}
```
*Es vital emplear los "System Colors" (como CanvasText, Highlight, LinkText) para asegurar que la interfaz responda exactamente a la configuración neuroatípica o visual del alumno.*

---

## 8. Análisis de la Paleta Actual: `#7A6858` (Sepia)

Desde la perspectiva de la accesibilidad y el daltonismo, evaluemos nuestra paleta basada en el color `#7A6858` (un tono sepia pardo, RGB: 122, 104, 88). 

**Diagnóstico Perceptual:**
El color sepia o marrón es un amarillo-naranja de baja luminosidad (Hue: 28°, Saturation: ~16%, Lightness: ~41%). 
- **Para Deuteranopes/Protanopes:** Este color es extremadamente susceptible a confundirse con un **verde oliva oscuro** (ej. `#5F7354`) o un **rojo muy desaturado** (ej. `#8A6060`). Al situarse en la mitad exacta del espectro de luminosidad, carece del brillo necesario para destacar sobre fondos blancos u oscuros con efectividad.
- **Riesgo Educativo:** Si `#7A6858` se usa como color primario para marcar enlaces, resaltar respuestas incorrectas o codificar conceptos (ej. historia vs geografía), será ineficaz. No generará suficiente tensión visual frente al texto negro y se mezclará en el fondo si se usa con grises medios.

**Recomendación de Adaptación (Claro / Oscuro):**
1. **Modo Claro (Light Mode):** El sepia actual (`#7A6858`) tiene un contraste pasable pero monótono frente al blanco. Si se va a usar como acento o texto primario, se recomienda oscurecerlo a un marrón profundo como `#53463B`. Si se acompaña con otros colores, se deben inyectar tonos opuestos (enfriar la paleta) añadiendo el Azul Okabe (`#0072B2`) para lograr una distinción complementaria que resista el daltonismo.
2. **Modo Oscuro (Dark Mode):** El sepia `#7A6858` frente a un fondo muy oscuro (ej. `#121212`) fallará catastróficamente en la prueba APCA de contraste y empeorará la legibilidad para estudiantes con protanopía. Se debe usar una versión altamente luminosa, como `#D4BAA3` o un naranja/dorado cálido del estilo `#E69F00` (Okabe-Ito). El modo oscuro para daltonismo debe enfocarse puramente en la luminosidad (Lightness en HSL, arriba del 70%) más que en retener el tono exacto.

## 9. Conclusión General
El diseño de plataformas educativas no es un ejercicio estético; es una ciencia de transferencia de información. Un estudiante con deuteranopía o protanopía gasta valiosos recursos cognitivos tratando de descifrar qué curva es la de "ventas" y cuál la de "costos" en un gráfico rojo/verde mal diseñado, en lugar de comprender el concepto subyacente de la clase. Adoptando los estándares Okabe-Ito o Paul Tol, adhiriéndonos a WCAG 3.0 (APCA), utilizando CSS `forced-colors` adecuadamente y abandonando matices sepia sin suficiente luminosidad contrastante, no solo hacemos que la educación sea accesible para el 8% de la población daltónica; mejoramos la legibilidad y la experiencia didáctica global para absolutamente todos los estudiantes.
