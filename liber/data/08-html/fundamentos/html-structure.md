---
up:: [[html]]
tags:: [html]
---

# Estructura de un documento HTML

Todo documento HTML sigue una estructura base que el navegador interpreta para renderizar la página. Esta estructura es el esqueleto sobre el que se construye cualquier sitio web.

## Estructura básica

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi página</title>
  <link rel="stylesheet" href="estilos.css">
</head>
<body>
  <h1>Hola mundo</h1>
  <p>Contenido de la página.</p>
</body>
</html>
```

## Componentes principales

### `<!DOCTYPE html>`

Declara que el documento es HTML5. Debe ser la primera línea del archivo. No es una etiqueta HTML, sino una instrucción al navegador.

### `<html>`

Elemento raíz que envuelve todo el contenido. El atributo `lang="es"` define el idioma del documento, lo cual es importante para accesibilidad y SEO.

### `<head>`

Contiene metadatos que no se muestran directamente en la página. Incluye información sobre el documento como título, codificación de caracteres, hojas de estilo y scripts. Ver [[html-head]] para más detalles.

### `<body>`

Contiene todo el contenido visible de la página: textos, imágenes, enlaces, formularios, etc. Ver [[html-body]] para más detalles.

## Metadatos comunes

Dentro de `<head>` se encuentran elementos `<meta>` que definen propiedades del documento:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Descripción de la página para buscadores">
<meta name="author" content="Nombre del autor">
```

## Enlaces y scripts

Los elementos `<link>` y `<script>` conectan el documento con recursos externos:

```html
<link rel="stylesheet" href="css/estilos.css">
<link rel="icon" href="favicon.ico">
<script src="js/app.js" defer></script>
```

## Relación con Quarto

Quarto genera esta estructura automáticamente. Cuando escribes un archivo `.qmd`, Quarto construye el `<!DOCTYPE>`, `<html>`, `<head>` y `<body>` sin que tengas que escribirlos manualmente. Tú solo defines el contenido y los metadatos en el encabezado YAML.

## Relación con atributos HTML

Cada elemento puede tener atributos que modifican su comportamiento o añaden información. Ver [[html-attributes]] para una referencia completa de atributos globales.
