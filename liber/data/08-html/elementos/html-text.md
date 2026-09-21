---
up:: [[html]]
tags:: [html]
---

# Elementos de texto en HTML

HTML ofrece elementos para estructurar el contenido textual, comunicando
significado semántico al navegador y a los lectores de pantalla.

## Encabezados

`h1` a `h6` definen jerarquías de secciones. Solo un `h1` por página.

```html
<h1>Título principal</h1>
<h2>Sección</h2>
<h3>Subsección</h3>
```

## Párrafos y saltos

`<p>` define un bloque de texto. `<br>` inserta un salto de línea.
`<hr>` representa una división temática.

```html
<p>Primer párrafo.</p>
<p>Segundo párrafo con un<br>salto.</p>
<hr>
```

## Formato inline

- `<em>` — énfasis (cursiva semántica).
- `<strong>` — importancia (negrita semántica).
- `<mark>` — texto resaltado.
- `<small>` — texto reducido.
- `<sub>` — subíndice: H<sub>2</sub>O.
- `<sup>` — superíndice: x<sup>2</sup>.

```html
<p><em>Énfasis</em> y <strong>importante</strong>.</p>
<p><mark>Resaltado</mark> y <small>pequeño</small>.</p>
```

Estos elementos comunican significado. Para efectos visuales se usa CSS,
no etiquetas como `<b>` o `<i>`.

Ver también: [[html-structure]]
