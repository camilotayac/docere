# Pseudo-elementos de CSS

Un pseudo-elemento es una palabra clave que permite stylizar partes específicas de un elemento, como fragmentos de texto o contenido generado. Se escriben con doble dos puntos `::`.

> [!note] Notación
> Los pseudo-elementos se escriben con `::` (doble dos punto), mientras que las [[pseudo-clases]] usan `:` (un solo dos puntos). Sin embargo, por compatibilidad, los navegadores modernos también aceptan `:` para pseudo-elementos.

## `::before` y `::after`

Crean elementos virtuales como hijos del elemento seleccionado. Requieren la propiedad `content`.

```css
.enlace-externo::after {
  content: " ↗";
  font-size: 0.8em;
}

.titulo::before {
  content: "§ ";
  color: #999;
}

.cita::before {
  content: open-quote;
  font-size: 2em;
  line-height: 0;
  vertical-align: -0.4em;
  margin-right: 4px;
}
```

### Ejemplo práctico: tooltips

```css
.tooltip {
  position: relative;
}

.tooltip::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 125%;
  left: 50%;
  transform: translateX(-50%);
  background-color: #333;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}

.tooltip:hover::after {
  opacity: 1;
}
```

### Ejemplo práctico: indicadores de lista

```css
li::before {
  content: "▸";
  color: #007acc;
  margin-right: 8px;
}
```

## `::first-line`

Estiliza solo la primera línea de un elemento de bloque. Es dinámico: cambia si el navegador redimensiona la ventana.

```css
p::first-line {
  font-weight: bold;
  text-transform: uppercase;
}

article::first-line {
  color: #2c3e50;
  font-size: 1.1em;
}
```

> [!warning] Limitaciones
> Solo se pueden aplicar un subconjunto de propiedades de texto: `font-*`, `color`, `text-decoration`, `word-spacing`, `letter-spacing`, `line-height`.

## `::first-letter`

Estiliza la primera letra del elemento. Ideal para estilos tipográficos tipo *drop cap*.

```css
p::first-letter {
  font-size: 3em;
  float: left;
  line-height: 1;
  margin-right: 8px;
  color: #e74c3c;
  font-weight: bold;
}

article > p:first-of-type::first-letter {
  font-family: Georgia, serif;
  font-size: 3.5em;
  float: left;
  margin: 0 8px 0 0;
}
```

## `::selection`

Estiliza la porción de texto seleccionada por el usuario.

```css
::selection {
  background-color: #007acc;
  color: white;
}

h1::selection {
  background-color: #e74c3c;
  color: white;
}
```

> [!tip] Marcado en texto
> Solo se pueden aplicar propiedades de color: `color`, `background-color`, `text-decoration`, `text-shadow`.

## `::placeholder`

Estiliza el texto de placeholder de inputs y textareas.

```css
input::placeholder {
  color: #adb5bd;
  font-style: italic;
  opacity: 0.8;
}

textarea::placeholder {
  color: #6c757d;
  font-size: 14px;
}
```

## `::marker`

Estiliza el marcador de puntos de listas o números de listas numeradas.

```css
li::marker {
  color: #007acc;
  font-weight: bold;
  font-size: 1.2em;
}

ol li::marker {
  color: #e74c3c;
}
```

## `::file-selector-button`

Estiliza el botón nativo de selector de archivos.

```css
input[type="file"]::file-selector-button {
  background-color: #007acc;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

input[type="file"]::file-selector-button:hover {
  background-color: #0056b3;
}
```

## La propiedad `content`

Es obligatoria para `::before` y `::after`. Acepta varios valores:

```css
/* Texto literal */
.especial::before {
  content: "Importante: ";
  font-weight: bold;
  color: #e74c3c;
}

/* Contenido de un atributo */
.enlace::after {
  content: " (" attr(href) ")";
  font-size: 0.8em;
  color: #999;
}

/* Contadores */
.lista-numerada {
  counter-reset: mi-contador;
}

.lista-numerada li {
  counter-increment: mi-contador;
}

.lista-numerada li::before {
  content: counter(mi-contador) ". ";
  font-weight: bold;
  color: #007acc;
}

/* Valor vacío (necesario para pseudo-elementos con estilo) */
.icono::before {
  content: "";
  display: inline-block;
  width: 16px;
  height: 16px;
  background-image: url('icono.svg');
  background-size: contain;
}
```

## Combinación de pseudo-elementos

Se pueden combinar pseudo-clases con pseudo-elementos:

```css
p:hover::first-letter {
  color: #e74c3c;
  font-size: 1.5em;
}

a::before {
  content: "→ ";
  transition: transform 0.2s;
}

a:hover::before {
  transform: translateX(4px);
}

input:focus::placeholder {
  color: transparent;
}
```

## Conexión con Quarto

En proyectos de [[html-theming]], los pseudo-elementos son fundamentales para:

- Agregar indicadores visuales a [[quarto-callouts]] sin modificar el HTML
- Crear decoraciones en [[quarto-shortcodes]] personalizados
- Implementar estilos tipográficos en contenido de [[filters]]
- Diseñar tooltips y elementos interactivos en el tema

```css
/* Indicador visual para callouts de Quarto */
.callout-tip::before {
  content: "💡";
  position: absolute;
  top: -12px;
  left: 12px;
  font-size: 1.5em;
}

/* Contador automático para notas al pie */
.footnote-ref::before {
  content: "[";
}

.footnote-ref::after {
  content: "]";
}
```

## Ver también

- [[pseudo-clases]]
- [[selectores-basicos]]
- [[variables-css]]
- [[tipografia]]
