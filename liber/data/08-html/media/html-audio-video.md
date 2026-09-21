---
up:: [[html]]
tags:
  - html
---

# Audio y Video en HTML

HTML5 introdujo soporte nativo para audio y video, eliminando la dependencia de plugins externos como Flash. Las etiquetas `<audio>` y `<video>` permiten incrustar medios de forma semántica y accesible.

## Etiqueta `<audio>`

Reproduce contenido de audio directamente en el navegador:

```html
<audio controls autoplay loop muted>
  <source src="cancion.mp3" type="audio/mpeg">
  <source src="cancion.ogg" type="audio/ogg">
  Tu navegador no soporta el elemento de audio.
</audio>
```

### Atributos principales

| Atributo | Función |
|----------|---------|
| `controls` | Muestra los controles de reproducción |
| `autoplay` | Inicia la reproducción automáticamente |
| `loop` | Repite el audio continuamente |
| `muted` | Silencia el audio por defecto |

## Etiqueta `<video>`

Reproduce contenido de video con controles nativos:

```html
<video controls poster="miniatura.jpg" preload="metadata" width="720">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  Tu navegador no soporta el elemento de video.
</video>
```

### Atributos específicos

- `poster`: Imagen mostrada antes de iniciar la reproducción.
- `preload`: Indica cómo precargar el contenido (`none`, `metadata`, `auto`).
- `width` / `height`: Dimensiones del reproductor.

## Múltiples formatos con `<source>`

La etiqueta `<source>` anidada permite ofrecer múltiples formatos. El navegador usa el primero que soporte:

```html
<video controls>
  <source src="pelicula.mp4" type="video/mp4">
  <source src="pelicula.webm" type="video/webm">
  <source src="pelicula.ogv" type="video/ogg">
</video>
```

## Subtítulos con `<track>`

La etiqueta `<track>` añade subtítulos o pistas de texto:

```html
<video controls>
  <source src="clase.mp4" type="video/mp4">
  <track src="subtitulos_es.vtt" kind="subtitles" srclang="es" label="Español" default>
  <track src="subtitulos_en.vtt" kind="subtitles" srclang="en" label="English">
</video>
```

Los archivos `.vtt` (WebVTT) contienen el texto sincronizado con el video.

## Incrustación con `<iframe>`

Para contenido de plataformas externas se usa `<iframe>`:

```html
<iframe width="560" height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  frameborder="0"
  allowfullscreen>
</iframe>
```

YouTube, Vimeo y otras plataformas proporcionan el código de incrustación directamente.

## Consejos de accesibilidad

- Ofrecer siempre subtítulos cuando sea posible.
- No usar `autoplay` con sonido para evitar experiencias disruptivas.
- Incluir controles visibles para que el usuario pueda pausar o silenciar.
- Proporcionar transcripciones de audio como contenido alternativo.

## Relación con otros elementos

El manejo multimedia se complementa con [[html-elements]] para la estructura del documento y con atributos HTML para el control preciso de cada componente multimedia.

Ver también: [[html-elements]] para la referencia completa de etiquetas HTML.
