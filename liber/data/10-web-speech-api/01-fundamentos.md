# Web Speech API: Fundamentos y Arquitectura

La **Web Speech API** permite incorporar datos de voz en aplicaciones web, ofreciendo nuevas e interesantes posibilidades para accesibilidad y otros mecanismos interactivos. Esta API se divide principalmente en dos funcionalidades clave:

## 1. Síntesis de Voz (Text-to-Speech o TTS)
La síntesis de voz permite a las aplicaciones web convertir texto escrito en palabras habladas. Esto resulta fundamental para:
- Personas con discapacidades visuales o dificultades de lectura.
- Usuarios que prefieren consumir contenido auditivo.
- Situaciones donde leer en una pantalla no es conveniente o seguro (e.g., conduciendo).

La arquitectura de TTS en el navegador se maneja mediante dos interfaces principales:
- `SpeechSynthesis`: Es el controlador principal. Se encarga de gestionar la lista de voces disponibles en el dispositivo y la cola de fragmentos de texto (utterances) que se van a leer.
- `SpeechSynthesisUtterance`: Representa un fragmento de texto único que será hablado. Permite configurar propiedades como el texto en sí, el idioma (`lang`), la voz específica (`voice`), el tono (`pitch`) y la velocidad de lectura (`rate`).

## 2. Reconocimiento de Voz (Asynchronous Speech Recognition)
El reconocimiento de voz permite convertir audio (voz humana) en texto escrito. Utiliza la interfaz `SpeechRecognition`, que recopila el audio a través del micrófono del dispositivo, lo procesa (generalmente mediante un servicio de reconocimiento del servidor asociado al navegador) y devuelve resultados transcritos junto con un nivel de confianza. 

### Consideraciones Generales
- **Soporte de Navegadores**: Aunque la API es un estándar web, su implementación puede variar. Por ejemplo, Chrome utiliza su propio motor en la nube para el reconocimiento, mientras que las voces de síntesis dependen del sistema operativo subyacente.
- **Permisos**: El reconocimiento de voz requiere permiso explícito del usuario para usar el micrófono (capturado mediante HTTPS). La síntesis de voz, por otro lado, puede requerir que el usuario interactúe primero con la página (como un clic) antes de que el navegador permita reproducir audio, para evitar spam acústico.

*(Fuente: [MDN Web Docs - Web Speech API](https://developer.mozilla.org/es/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API))*
