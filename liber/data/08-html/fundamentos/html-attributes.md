---
up:: [[html]]
tags:: [html]
---

# Atributos HTML

Los atributos proporcionan informacion adicional sobre los elementos HTML. Se escriben como pares nombre-valor dentro de la etiqueta de apertura.

## Sintaxis basica

```html
<tagname attribute="value">Contenido</tagname>
```

## Atributos globales

Estos atributos pueden usarse en cualquier elemento HTML.

### `id`

Identifica un elemento de forma unica dentro del documento. Solo puede haber un elemento con un `id` dado.

```html
<div id="principal">Contenido principal</div>
<p id="intro">Parrafo de introduccion</p>
```

### `class`

Define una o mas clases CSS para el elemento. A diferencia de `id`, un elemento puede tener varias clases y un nombre de clase puede repetirse en multiples elementos.

```html
<div class="card destacado">Tarjeta destacada</div>
<p class="texto-gris texto-peq">Parrafo pequeno y gris</p>
```

### `style`

Permite aplicar estilos CSS inline directamente al elemento.

```html
<p style="color: rojo; font-size: 18px;">Texto rojo</p>
```

### `title`

Proporciona informacion consultable, generalmente mostrada como tooltip al pasar el cursor sobre el elemento.

```html
<abbr title="Organizacion de las Naciones Unidas">ONU</abbr>
```

### `data-*`

Atributos personalizados para almacenar datos privados en el DOM. El prefijo `data-` indica que es un atributo de datos.

```html
<article data-id="42" data-categoria="ciencia">Articulo</article>
```

Se acceden con JavaScript:

```javascript
const articulo = document.querySelector('article');
console.log(articulo.dataset.id);        // "42"
console.log(articulo.dataset.categoria); // "ciencia"
```

### `aria-*`

Atributos de accesibilidad que mejoran la experiencia para usuarios con tecnologias asistivas como lectores de pantalla.

```html
<button aria-label="Cerrar ventana" aria-expanded="false">X</button>
<div role="alert" aria-live="polite">Mensaje importante</div>
```

## Atributos de manejadores de eventos

Permiten ejecutar JavaScript ante acciones del usuario.

```html
<button onclick="alert('Hola')">Click me</button>
<input type="text" onfocus="this.style.borderColor='blue'">
```

En la practica, es preferible adjuntar eventos con JavaScript en lugar de usar atributos inline.

## Atributos standard vs custom

Los atributos standard estan definidos en la especificacion HTML y tienen un proposito明确o. Los atributos custom (como `data-*`) son extensiones propias del desarrollador.

```html
<!-- Atributo standard -->
<a href="https://ejemplo.com" target="_blank">Enlace</a>

<!-- Atributo custom -->
<div data-tooltip="Informacion adicional">Elemento</div>
```

## Relacion con Quarto

En Quarto, los `class` e `id` se usan para CSS y JavaScript. Cuando escribes en un archivo `.qmd`, las clases e identificadores que defines se aplican al HTML generado.

## Atributos y elementos

Cada elemento tiene sus propios atributos disponibles ademas de los globales. Ver [[html-elements]] para ver los atributos especificos de cada elemento.

## Atributos y semantica

Los atributos como `role` y `aria-*` contribuyen a la semantica del documento. Ver [[html-semantic]] para mas contexto sobre la estructura semantica de HTML.
