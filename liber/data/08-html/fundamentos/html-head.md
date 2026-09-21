---
up:: [[html]]
tags:: [html]
---

# El elemento `<head>` en HTML

El `<head>` es una sección del documento que contiene metadatos y recursos asociados a la página. No se renderiza visualmente en el navegador, pero es fundamental para el funcionamiento correcto del sitio.

## Estructura típica del `<head>`

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Aprende los fundamentos de HTML">
  <title>Fundamentos de HTML</title>
  <link rel="stylesheet" href="css/estilos.css">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <style>
    body { font-family: sans-serif; }
  </style>
  <script src="js/app.js" defer></script>
</head>
```

## Elementos principales

### `<meta charset>`

Define la codificación de caracteres del documento. UTF-8 es el estándar actual y soporta caracteres especiales del español y otros idiomas.

```html
<meta charset="UTF-8">
```

### `<meta name="viewport">`

Controla cómo se comporta la página en dispositivos móviles. Sin esta etiqueta, los navegadores móviles pueden renderizar la página a escala completa en lugar de adaptarla al ancho de la pantalla.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### `<title>`

Define el título que aparece en la pestaña del navegador y en los resultados de búsqueda. Es un factor importante para SEO.

```html
<title>Mi sitio web - Página principal</title>
```

### `<link rel="stylesheet">`

Conecta una hoja de estilos CSS externa. Es la forma más común de aplicar estilos a una página.

```html
<link rel="stylesheet" href="css/estilos.css">
```

### `<style>`

Permite escribir CSS directamente dentro del `<head>`. Útil para estilos específicos de una sola página.

```html
<style>
  .destacado { color: blue; font-weight: bold; }
</style>
```

### `<script>`

Incluye JavaScript. El atributo `defer` retrasa la ejecución hasta que se carga el DOM completo.

```html
<script src="js/app.js" defer></script>
```

## SEO básico

Los elementos del `<head>` influyen directamente en cómo los motores de busqueda indexan y muestran la pagina:

- `<title>` es el texto que aparece como enlace en los resultados de busqueda.
- `<meta name="description">` se muestra como fragmento descriptivo.
- Un `charset` correcto evita problemas de visualizacion de caracteres.

## Relación con la estructura general

El `<head>` es una de las dos secciones principales de todo documento HTML. Ver [[html-structure]] para una vision completa de la estructura del documento.
