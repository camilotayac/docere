# Selectores Básicos de CSS

Los selectores son patrones que se usan para seleccionar los elementos de una página web que queremos dar estilo.

## Selector de elemento

Selecciona todos los elementos de un tipo dado.

```css
h1 {
  color: blue;
}

p {
  font-size: 16px;
}

div {
  margin: 0 auto;
}
```

## Selector de clase

Selecciona todos los elementos con un atributo `class` específico. Se escribe con un punto `.` antes del nombre.

```css
.resaltado {
  background-color: yellow;
  font-weight: bold;
}

.texto-pequeño {
  font-size: 12px;
}
```

En [[html-theming]], las clases se usan ampliamente para aplicar estilos específicos sin afectar a todos los elementos de un tipo.

## Selector de ID

Selecciona un elemento único con un atributo `id` específico. Se escribe con una almohadilla `#` antes del nombre.

```css
#cabecera {
  background-color: #333;
  color: white;
}

#contenido-principal {
  max-width: 800px;
}
```

> [!warning] Especificidad
> Los selectores de ID tienen mayor especificidad que los de clase. Un solo elemento solo puede tener un `id`, mientras que múltiples elementos pueden compartir la misma clase.

## Selector universal

Selecciona todos los elementos del documento.

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

Útil para un [[reset-css]] o normalización básica de estilos entre navegadores.

## Selector de agrupación

Permite aplicar los mismos estilos a múltiples selectores separándolos con comas.

```css
h1, h2, h3 {
  font-family: 'Inter', sans-serif;
  color: #2c3e50;
}

button, input, select {
  border: 1px solid #ccc;
  border-radius: 4px;
}
```

## Combinadores

Los combinadores expresan la relación entre selectores.

### Descendiente (espacio)

Selecciona todos los elementos anidados dentro de otro, sin importar la profundidad.

```css
article p {
  line-height: 1.6;
}

nav a {
  text-decoration: none;
  color: inherit;
}
```

### Hijo directo (`>`)

Selecciona solo los elementos hijos directos.

```css
ul > li {
  list-style: disc;
}

.nav > .item {
  padding: 10px;
}
```

### Hermano adyacente (`+`)

Selecciona el elemento hermano que sigue inmediatamente al primero.

```css
h2 + p {
  font-size: 18px;
  font-weight: bold;
}

label + input {
  margin-left: 8px;
}
```

### Hermanos generales (`~`)

Selecciona todos los hermanos que siguen al primero.

```css
h2 ~ p {
  color: #555;
}

.active ~ .item {
  opacity: 0.6;
}
```

## Conexión con Quarto

En los proyectos de [[html-theming]] de [[Quarto]], los selectores básicos son fundamentales para:

- Estilizar bloques de código generados por [[quarto-highlighting]]
- Aplicar estilos a elementos creados por [[filters]]
- Personalizar la apariencia de salidas computacionales

```css
/* Estilizar outputs de code cells en Quarto */
div.cell {
  border-left: 3px solid #007acc;
  padding: 1em;
}

div.cell-output {
  background-color: #f8f9fa;
}
```

## Ver también

- [[pseudo-clases]]
- [[pseudo-elementos]]
- [[especificidad]]
- [[cascade-layer]]
