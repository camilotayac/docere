---
up:: [[html]]
tags:
  - html
---

# HTML Semántico

El HTML semántico utiliza etiquetas que describen el **propósito** del contenido, no solo su apariencia. Esto mejora la accesibilidad, el SEO y la mantenibilidad del código.

## Por qué importa

- Los lectores de pantalla interpretan correctamente la estructura.
 Los motores de búsqueda indexan el contenido de forma más precisa.
- El código es más legible para desarrolladores.
- Se cumple mejor con los estándares web (WCAG).

## Elementos de seccionado

### `<header>`

Encabezado de una página o sección. Suele contener logo, título y navegación.

```html
<header>
  <h1>Mi Sitio Web</h1>
  <nav>...</nav>
</header>
```

### `<footer>`

Pie de página con información complementaria como derechos de autor o enlaces.

```html
<footer>
  <p>&copy; 2026 Mi Sitio</p>
</footer>
```

### `<nav>`

Contiene los enlaces de navegación principales del sitio.

### `<main>`

Representa el contenido principal del documento. Solo debe haber uno por página.

### `<article>`

Contenido autónomo que tiene sentido por sí mismo, como una entrada de blog o una noticia.

### `<aside>`

Contenido complementario separado del flujo principal, como barras laterales.

### `<section>`

Sección temática genérica que agrupa contenido relacionado.

### `<address>`

Proporciona información de contacto del autor o propietario del contenido.

## Contraste con `<div>` y `<span>`

`<div>` y `<span>` son elementos **genéricos** sin significado semántico:

```html
<!-- Sin semántica -->
<div class="header">...</div>
<span class="label">...</span>

<!-- Con semántica -->
<header>...</header>
<strong>...</strong>
```

Siempre que exista un elemento semántico apropiado, se debe preferir sobre `<div>` o `<span>`.

## Ejemplo visual de layout

```
+------------------------------------------+
|              <header>                    |
|  Logo    |    <nav> Enlaces              |
+------------------------------------------+
|              <main>                      |
|  +------------------+  +-------------+  |
|  |   <article>      |  |  <aside>    |  |
|  |   Contenido      |  |  Sidebar    |  |
|  |   principal      |  |             |  |
|  +------------------+  +-------------+  |
+------------------------------------------+
|              <footer>                    |
|  Contacto: <address>                     |
+------------------------------------------+
```

## Buenas prácticas

- Usar `<main>` una sola vez por documento.
- Anidar `<section>` dentro de `<article>` cuando hay subsecciones temáticas.
- Reservar `<div>` solo para contenedores de estilo sin significado semántico.
- Combinar con ARIA cuando la semántica nativa no sea suficiente, como se describe en [[html-accessibility]].

## Relación con otros elementos

El HTML semántico es la base sobre la que se construyen [[html-elements]] y se apoya en [[html-accessibility]] para garantizar que todos los usuarios puedan interactuar con el contenido.

Ver también: [[html-elements]], [[html-accessibility]].
