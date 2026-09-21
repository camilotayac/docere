# CSS para Sincronización Visual y TTS

En entornos educativos, sincronizar visualmente el texto que se lee en voz alta (karaoke-style highlighting) es de gran ayuda cognitiva. 

## 1. Estilizado del Resaltado (Highlighting)
Se recomienda el uso de **CSS Custom Properties (Variables)** para controlar los temas de resaltado y mantener el código mantenible.

```css
:root {
  --tts-highlight-bg: #fff3cd; /* Amarillo suave */
  --tts-highlight-color: #000000;
  --tts-highlight-transition: background-color 0.2s ease;
}

.tts-reading-active {
  background-color: var(--tts-highlight-bg);
  color: var(--tts-highlight-color);
  border-radius: 2px;
  transition: var(--tts-highlight-transition);
}
```

## 2. Problemas de Reflow y DOM Mutation
El método tradicional para resaltar palabras es usar JavaScript para envolver cada palabra o frase en una etiqueta `<span>` temporal. 
**Peligro:** Mutar el DOM en tiempo real inyectando miles de `<span>` causa graves problemas de rendimiento (*Layout Thrashing* y *Reflow*), y puede reiniciar el búfer de los Screen Readers tradicionales.
**Solución Científica:** Pre-renderizar el texto con los `<span>` estructurales ya creados semánticamente, o en navegadores modernos, utilizar la **CSS Custom Highlight API** (`::highlight()`) que permite resaltar rangos de texto usando JavaScript `Range` y `Highlight` sin mutar el árbol DOM.

## 3. El Patrón `.sr-only` (Screen Reader Only)
Para texto que necesita ser leído por un Screen Reader pero debe estar oculto visualmente (como instrucciones extra para formularios):

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0); /* Sintaxis Legacy */
  clip-path: inset(50%); /* Sintaxis Moderna */
  white-space: nowrap;
  border: 0;
}
```
**Importante:** Nunca uses `display: none` o `visibility: hidden` para esto, ya que eliminan el elemento completamente del Árbol de Accesibilidad.
