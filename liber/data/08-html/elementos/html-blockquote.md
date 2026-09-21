---
up:: [[html]]
tags:: [html]
---

# Citas y bloques en HTML

HTML proporciona elementos semánticos para representar citas, referencias
y otras formas de contenido citado.

## Blockquote: `<blockquote>`

Bloque de contenido citado. El atributo `cite` contiene la URL de la fuente,
no visible en la página.

```html
<blockquote cite="https://example.com/fuente">
  <p>La semiótica estudia los signos en cuanto tales.</p>
</blockquote>
```

## Cita inline: `<q>`

Para citas cortas dentro de un párrafo. Los navegadores agregan comillas
según la locale.

```html
<p>Como señaló Peirce: <q>El pensamiento es un signo</q>.</p>
```

## Elemento `<cite>`

Indica el título de una obra citada, no el nombre de la persona.

```html
<p>Según <cite>Semiótica y filosofía del lenguaje</cite> de Eco...</p>
```

## Abreviatura, dirección y tiempo

`<abbr>` define una abreviatura con su expansión en `title`. `<address>`
proporciona información de contacto. `<time>` marca fechas con formato
ISO 8601 en el atributo `datetime`.

```html
<p>Trabajamos con <abbr title="HyperText Markup Language">HTML</abbr>.</p>
<address>Escrito por <a href="mailto:autor@ejemplo.com">Autor</a>.</address>
<p>Publicado el <time datetime="2026-03-15">15 de marzo de 2026</time>.</p>
```

Ver también: [[html-semantic]]
