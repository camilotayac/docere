# Tutorial: Implementación de Text-to-Speech (TTS) con HTML, CSS y JS

Crear un convertidor de Texto-a-Voz (TTS) es sencillo gracias a la Web Speech API. A continuación, se detalla la metodología basada en HTML, CSS y JavaScript para integrar esta funcionalidad en una aplicación web.

## Paso 1: Estructura HTML (Interfaz de Usuario)
El HTML requiere elementos básicos para la interacción del usuario:
- Un campo de entrada (`<input>` o `<textarea>`) donde el usuario escribe el texto.
- Un botón (`<button>`) para iniciar la lectura.
- Un menú desplegable (`<select>`) para permitir al usuario elegir la voz preferida.

```html
<div class="tts-container">
    <input type="text" id="text-input" placeholder="Escribe el texto a leer..." />
    <select id="voice-select"></select>
    <button id="speak-button">Leer Texto</button>
</div>
```

## Paso 2: Funcionalidad JavaScript
El núcleo del TTS se basa en las interfaces `SpeechSynthesis` y `SpeechSynthesisUtterance`.

1. **Inicializar la síntesis y obtener elementos del DOM:**
   ```javascript
   const textInput = document.getElementById('text-input');
   const speakButton = document.getElementById('speak-button');
   const voiceSelect = document.getElementById('voice-select');
   const synth = window.speechSynthesis;
   ```

2. **Cargar la lista de voces disponibles:**
   Dependiendo del navegador y sistema operativo, las voces pueden tardar en cargar, por lo que es vital escuchar el evento `voiceschanged` si es necesario, aunque en implementaciones básicas se hace al cargar la ventana.
   ```javascript
   function populateVoiceList() {
       const voices = synth.getVoices();
       voices.forEach((voice, index) => {
           const option = document.createElement('option');
           option.textContent = `${voice.name} (${voice.lang})`;
           option.value = index;
           voiceSelect.appendChild(option);
       });
   }
   window.addEventListener('load', populateVoiceList);
   ```

3. **Ejecutar la lectura al hacer clic:**
   ```javascript
   speakButton.addEventListener('click', () => {
       const text = textInput.value;
       if (text) {
           const utterance = new SpeechSynthesisUtterance(text);
           const voices = synth.getVoices();
           utterance.voice = voices[voiceSelect.value];
           synth.speak(utterance);
       }
   });
   ```

## Buenas Prácticas y Manejo de Errores
- **Compatibilidad Cross-Browser**: Siempre verificar que `window.speechSynthesis` esté disponible antes de ejecutar funciones, mostrando un mensaje de error elegante si el navegador no lo soporta.
- **Limpieza de la Cola de Reproducción**: Si el usuario presiona "Leer" repetidas veces, las frases se acumularán en la cola. Es una buena práctica usar `synth.cancel()` antes de emitir un nuevo `utterance` si se desea detener la lectura actual.
- **Accesibilidad**: Asegurar que los botones tengan atributos semánticos (`aria-label`) y que el foco (focus state) sea visible para navegación por teclado.
- **Optimización**: Reutilizar el objeto `synth` y no recargar las voces innecesariamente.

*(Fuente: [TutorialPedia - Text-to-Speech Converter](https://www.tutorialpedia.org/blog/text-to-speech-converter-using-html-css-and-javascript/))*
