---
aliases: [sintaxis CSS, reglas CSS]
tags: [css, fundamentos, sintaxis]
created: 2026-07-19
---

# Sintaxis de CSS

## Estructura de una regla CSS

Toda regla CSS sigue esta estructura:

```css
selector {
  propiedad: valor;
}
```

Una regla compuesta:

```css
h1, h2, h3 {
  font-family: 'Georgia', serif;
  color: #2c3e50;
  margin-bottom: 1em;
}
```

**Componentes:**
- **Selector(es):** qué elementos se afectan (pueden ser múltiples, separados por coma)
- **Bloque de declaraciones:** entre llaves `{}`
- **Declaración:** `propiedad: valor;` (terminada en punto y coma)
- **Propiedad:** nombre del aspecto a modificar
- **Valor:** configuración asignada a la propiedad

## Comentarios

```css
/* Comentario de una línea */

/*
  Comentario
  de múltiples líneas
*/
```

> [!note]
> CSS no soporta comentarios anidados. `/* /* anidado */ */` no es válido.

## Reglas de selectores

### Selectores básicos

| Selector | Ejemplo | Selecciona |
|----------|---------|------------|
| Elemento | `p` | Todos los párrafos |
| Clase | `.destacado` | Elementos con `class="destacado"` |
| ID | `#titulo-principal` | Elemento con `id="titulo-principal"` |
| Universal | `*` | Todos los elementos |
| Atributo | `[data-type="nota"]` | Elementos con ese atributo |

### Selectores combinadores

```css
/* Descendiente (espacio) */
article p { }

/* Hijo directo (>) */
article > p { }

/* Hermano adyacente (+) */
h2 + p { }

/* Hermanos generales (~) */
h2 ~ p { }
```

### Pseudo-clases y pseudo-elementos

```css
/* Pseudo-clases */
a:hover { }
input:focus { }
li:first-child { }
p:nth-child(2n) { }

/* Pseudo-elementos */
p::first-line { }
p::before { content: "→ "; }
p::after { content: " ★"; }
```

## At-rules (reglas de at)

Las at-rules son instrucciones especiales que controlan el comportamiento de CSS:

### `@import`

Importa otros archivos CSS o librerías:

```css
@import url('base.css');
@import 'variables.css';
```

### `@media`

Aplica estilos condicionalmente según características del dispositivo:

```css
@media (max-width: 768px) {
  .sidebar { display: none; }
  .content { width: 100%; }
}
```

### `@keyframes`

Define animaciones CSS:

```css
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

.card {
  animation: fade-in 0.3s ease-out;
}
```

### `@font-face`

Declara fuentes web personalizadas:

```css
@font-face {
  font-family: 'MiFuente';
  src: url('mifuente.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
}
```

### Otras at-rules relevantes

```css
@charset 'UTF-8';
@namespace url(http://www.w3.org/1999/xhtml);
@layer base, components, utilities;

@layer base {
  body { margin: 0; }
}
```

## Especificidad y cascada

La especificidad determina qué regla se aplica cuando varias compiten por el mismo elemento. Se calcula con un sistema de pesos:

```
Inline (1000) > ID (100) > Clase (10) > Elemento (1)
```

```css
/* Especificidad: 0-1-0 (1 clase) */
.card { padding: 1rem; }

/* Especificidad: 0-2-0 (2 clases) */
.card.highlight { padding: 2rem; }

/* Especificidad: 1-0-0 (1 ID) */
#main-card { padding: 3rem; }
```

Ver detalles completos en [[cascada-especificidad]].

## Herencia

Ciertas propiedades se heredan automáticamente de padre a hijo:

- **Se heredan:** `color`, `font-family`, `font-size`, `line-height`, `text-align`, `visibility`
- **No se heredan:** `border`, `padding`, `margin`, `width`, `height`, `background`

```css
body {
  font-family: sans-serif;  /* Se hereda a todos los hijos */
  border: 1px solid black;   /* No se hereda */
}
```

> [!tip]
> Para forzar la herencia se usa `inherit`. Para resetear, `initial` o `unset`.

## Conexión con Quarto

- **[[scss-variables]]**: SCSS extiende la sintaxis CSS con variables, nesting y mixins. Quarto procesa SCSS antes de generar el CSS final.

```scss
// SCSS — se compila a CSS
$color-principal: #2c3e50;

h1 {
  color: $color-principal;
  
  &.subtitle {
    font-size: 1.2rem;
    opacity: 0.8;
  }
}
```

- Las at-rules `@media` son fundamentales para el diseño responsive en [[html-theming]].
- `@font-face` permite incluir tipografías personalizadas en temas Quarto.

---

**Ver también:** [[introduccion]] · [[unidades]] · [[cascada-especificidad]]
