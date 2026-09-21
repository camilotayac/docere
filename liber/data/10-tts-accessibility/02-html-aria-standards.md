# Estándares HTML y ARIA para Lectura por Voz

La accesibilidad TTS depende directamente de la semántica del HTML y del uso quirúrgico de los atributos ARIA (Accessible Rich Internet Applications).

## 1. Atributos Clave HTML y ARIA
- **Atributo `lang`:** Crítico para la síntesis de voz. Los Screen Readers y la Web Speech API utilizan el atributo `lang` en la etiqueta `<html>` (ej. `<html lang="es">`) para cargar el motor de pronunciación adecuado. Si cambia el idioma en un párrafo, debe indicarse (ej. `<blockquote lang="en">`).
- **`role="region"` y Etiquetas Semánticas:** Utilizar `<main>`, `<nav>`, `<aside>`, y `<article>`. Para secciones genéricas importantes, usar `role="region"` junto con `aria-labelledby` para crear "landmarks" navegables.
- **`aria-label` y `aria-labelledby`:** Proporcionan o sobrescriben el "nombre accesible" de un elemento (útil para iconos que no tienen texto visible, ej. `<button aria-label="Reproducir texto">`).
- **`aria-live`:** Se utiliza para anunciar cambios dinámicos (ej. un mensaje de error). `aria-live="polite"` espera a que el usuario termine su tarea actual, mientras que `aria-live="assertive"` interrumpe inmediatamente.
- **`aria-hidden="true"`:** Oculta elementos decorativos o redundantes al Árbol de Accesibilidad para no saturar al usuario del lector de voz.

## 2. Qué NO Hacer (Antipatrones)
- **Sobrecarga ARIA:** *No ARIA es mejor que mal ARIA.* ARIA no cambia el comportamiento de un elemento, solo su semántica. Usar `<button>` es mejor que `<div role="button">`.
- **`aria-hidden` en elementos enfocables:** Nunca apliques `aria-hidden="true"` a enlaces o botones en el flujo de tabulación. Esto crea "fantasmas" que reciben el foco pero son invisibles para el Screen Reader.
- **Secuestro del foco:** Mover el foco del DOM programáticamente de forma inesperada rompe la experiencia de lectura.
