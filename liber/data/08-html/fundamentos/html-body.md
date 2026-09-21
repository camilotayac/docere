---
up:: [[html]]
tags:: [html]
---

# El elemento `<body>` en HTML

El `<body>` contiene todo el contenido visible de una pagina web. Es donde se organizan los textos, imagenes, enlaces, formularios y demas elementos que el usuario puede ver e interactuar.

## Estructura basica

```html
<body>
  <header>
    <h1>Mi sitio</h1>
    <nav>
      <a href="#inicio">Inicio</a>
      <a href="#acerca">Acerca</a>
    </nav>
  </header>

  <main>
    <article>
      <h2>Articulo principal</h2>
      <p>Contenido del articulo.</p>
    </article>
  </main>

  <footer>
    <p>&copy; 2026 Mi sitio</p>
  </footer>
</body>
```

## Elementos de bloque vs inline

HTML clasifica los elementos segun su comportamiento de display.

### Elementos de bloque

Ocupan todo el ancho disponible y saltan de linea antes y despues. Apilan verticalmente por defecto.

```html
<div>Contenedor generico de bloque</div>
<p>Parrafo de texto</p>
<h1>Titulo de nivel 1</h1>
<section>Seccion de contenido</section>
<ul>
  <li>Elemento de lista</li>
</ul>
```

### Elementos inline

Ocupan solo el ancho de su contenido y fluyen dentro del texto sin saltos de linea.

```html
<span>Texto en linea</span>
<a href="#">Enlace</a>
<strong>Negrita</strong>
<em>Cursiva</em>
<img src="foto.jpg" alt="Descripcion">
```

## Contenido fluyente (flow content)

El contenido fluyente es el conjunto de elementos que pueden aparecer dentro del `<body>`. Incluye tanto elementos de bloque como inline, asi como elementos interactivos. La mayoria de los elementos HTML son contenido fluyente.

## Contenido de fraseado (phrasing content)

El contenido de fraseado incluye los elementos que pueden aparecer dentro de un `<p>` o de un `<h1>`-`<h6>`. Son los elementos que componen el texto a nivel inline:

```html
<p>
  Este es un <strong>parrafo</strong> con <em>varios</em> elementos
  de <code>fraseado</code> integrados.
</p>
```

## Organizacion semantica

El `<body>` se organiza usando elementos semanticos que dan estructura y significado al contenido. Ver [[html-semantic]] para mas informacion sobre la estructura semantica.

## Relacion con elementos HTML

Cada tipo de elemento dentro del `<body>` tiene un proposito especifico y reglas de anidado. Ver [[html-elements]] para una referencia completa de los elementos disponibles.
