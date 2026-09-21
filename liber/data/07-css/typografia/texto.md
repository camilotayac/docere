---
title: Propiedades de texto en CSS
tags: [css, tipografia, texto]
aliases: [texto-css, propiedades-texto]
---

## text-align

Alinea el contenido en línea dentro de su contenedor:

```css
p { text-align: justify; }
h1 { text-align: center; }
.subtitle { text-align: left; }
```

| Valor | Descripción |
|---|---|
| `left` | Alinea a la izquierda |
| `right` | Alinea a la derecha |
| `center` | Centra el texto |
| `justify` | Justifica (rellena ambos bordes) |
| `start` / `end` | Según la dirección del texto (LTR/RTL) |

## text-decoration

Agrega decoración al texto:

```css
a { text-decoration: none; }
a:hover { text-decoration: underline; }
del { text-decoration: line-through; }
```

Combinaciones posibles:
- `text-decoration: underline wavy red;`
- `text-decoration-thickness: 2px;`
- `text-underline-offset: 3px;` — separa la línea del texto

## text-transform

Controla la capitalización del texto sin alterar el HTML:

```css
h1 { text-transform: uppercase; }
.nav-link { text-transform: capitalize; }
.tag { text-transform: lowercase; }
```

| Valor | Resultado |
|---|---|
| `uppercase` | TODO EN MAYÚSCULAS |
| `lowercase` | todo en minúsculas |
| `capitalize` | Primera Letra De Cada Palabra |
| `none` | Sin transformación |

## text-shadow

Agrega sombra al texto:

```css
h1 {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
```

Sintaxis: `offset-x offset-y blur-radius color`

Efectos comunes:
- **Texto incrustado**: `1px 1px 0 #000`
- **Neón**: `0 0 10px #fff, 0 0 20px #ff00de`
- **Relieve suave**: `1px 1px 1px rgba(0,0,0,0.5)`

## text-overflow

Controla qué se muestra cuando el texto se desborda de su contenedor:

```css
.truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 200px;
}
```

> [!tip] Requisitos
> `text-overflow: ellipsis` solo funciona cuando `white-space: nowrap` y `overflow: hidden` están activos.

## word-spacing

Ajusta el espacio entre palabras:

```css
p { word-spacing: 0.1em; }
.poetry { word-spacing: 0.3em; }
```

Útil para ajustar la densidad visual de párrafos o mejorar la legibilidad en textos grandes.

## letter-spacing

Ajusta el espacio entre caracteres individuales:

```css
.uppercase-label {
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.75rem;
}
```

> [!note] Diferencia con word-spacing
> `letter-spacing` afecta caracteres; `word-spacing` afecta palabras. Ambos trabajan en conjunto para la densidad tipográfica.

## white-space

Controla cómo se manejan los espacios en blanco y los saltos de línea:

```css
pre {
  white-space: pre-wrap;      /* respeta saltos, pero ajusta al contenedor */
}

.no-wrap {
  white-space: nowrap;        /* no permite saltos de línea */
}

.paragraph {
  white-space: normal;        /* comportamiento por defecto */
}
```

| Valor | Comportamiento |
|---|---|
| `normal` | Colapsa espacios, permite saltos |
| `nowrap` | Colapsa espacios, sin saltos |
| `pre` | Respeta espacios y saltos del HTML |
| `pre-wrap` | Respeta espacios, pero ajusta al ancho |
| `pre-line` | Colapsa espacios, respeta saltos |

## word-wrap / overflow-wrap

Propiedades que controlan la rotura de palabras largas:

```css
.container {
  overflow-wrap: break-word;
  word-wrap: break-word;  /* alias obsoleto, mantener por compatibilidad */
}
```

- **`overflow-wrap: break-word`** — rompe palabras largas solo si no caben en el contenedor.
- **`overflow-wrap: anywhere`** — permite romper en cualquier punto de la palabra.

> [!warning] word-wrap está obsoleto
> `word-wrap` es un alias de `overflow-wrap` para compatibilidad con navegadores antiguos. Preferir `overflow-wrap` en código nuevo.

## Hyphens

Habilita la partición silábica automática del idioma:

```css
p {
  hyphens: auto;
  lang: es;  /* se define en el HTML para indicar el idioma */
}
```

Requiere el atributo `lang` en el elemento `<html>` o en el propio elemento para funcionar correctamente.

## Conexión con Quarto

Las propiedades de texto se gestionan en Quarto a través de:

- **[[scss-variables]]**: Variables como `$headings-font-weight`, `$line-height-base` y `$font-family-monospace` controlan el estilo tipográfico global del sitio.

```scss
// Ejemplo de variables Quarto para texto
$line-height-base: 1.6;
$headings-font-weight: 700;
$code-font-family: "Fira Code", monospace;
```
