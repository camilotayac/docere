# Web Speech API vs. Screen Readers: Diferencias y Casos de Uso en Educación

Comprender la diferencia entre la **Web Speech API** y los **Screen Readers** (Lectores de Pantalla) tradicionales es fundamental para diseñar experiencias web verdaderamente accesibles y eficaces en entornos educativos.

## 1. Naturaleza Tecnológica
- **Screen Readers (NVDA, VoiceOver, JAWS):** Son aplicaciones de asistencia a nivel de sistema operativo (o extensiones profundas). Interpretan el Árbol de Accesibilidad (Accessibility Tree) del DOM. Su objetivo principal es permitir la **navegación integral** de la interfaz.
- **Web Speech API (SpeechSynthesis):** Es una interfaz de JavaScript nativa del navegador que permite a los desarrolladores programar la síntesis de voz (Text-to-Speech) dentro de la página. Es una **herramienta de desarrollo**, no una tecnología de asistencia configurada por el usuario a nivel de sistema.

## 2. Casos de Uso en Educación
- **Web Speech API:** Es ideal para **discapacidades cognitivas o de aprendizaje** (ej. dislexia, TDAH, o estudiantes de idiomas). Permite implementar botones de "Escuchar este artículo", brindando a los estudiantes una capa de conveniencia auditiva sincronizada con el contenido visual, sin alterar la navegación visual de la página.
- **Screen Readers:** Son imprescindibles para **discapacidades visuales**. Un botón de TTS creado con la Web Speech API *nunca* debe considerarse un reemplazo para la compatibilidad con Screen Readers. 

## 3. Limitaciones de la Web Speech API
- **Conflicto de Audio:** Puede entrar en conflicto y superponerse con los Screen Readers si ambos intentan hablar al mismo tiempo.
- **Falta de Control del Usuario:** A menudo, las voces, velocidades y acentos están dictados por el navegador o el sistema operativo del usuario subyacente de maneras que el desarrollador no puede predecir completamente, limitando la personalización frente a un Screen Reader tradicional.
- **Sin Navegación Estructural:** No permite al usuario saltar entre encabezados, formularios o regiones landmark por sí sola.
