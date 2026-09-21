---
title: Fuentes y tipografía en CSS
tags: [css, tipografia, fuentes]
aliases: [tipografia, fuentes]
---

## font-family

Define la familia tipográfica de un elemento. Se recomienda siempre incluir un **fallback** (tipografía de reserva) por si el navegador no puede cargar la fuente principal.

```css
h1 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

Las fuentes genéricas son: `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`.

## Web safe fonts

Son fuentes instaladas en la mayoría de sistemas operativos. Garantizan una apariencia consistente:

- **Serif**: Times New Roman, Georgia, Palatino
- **Sans-serif**: Arial, Helvetica, Verdana, Tahoma
- **Monospace**: Courier New, Consolas, Monaco

Usar varias opciones en cascade mejora la compatibilidad entre plataformas.

## Google Fonts

Google Fonts permite cargar fuentes optimizadas desde su CDN. Se añaden en el HTML o en una hoja de estilo:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

body {
  font-family: 'Inter', sans-serif;
}
```

> [!tip] Precaución de rendimiento
> Limitar los pesos y estilos cargados reduce el tiempo de carga. Solo importar lo necesario.

## @font-face

Permite definir tipografías personalizadas alojadas localmente o en servidores propios:

```css
@font-face {
  font-family: 'MiFuente';
  src: url('/fonts/mifuente.woff2') format('woff2'),
       url('/fonts/mifuente.woff') format('woff');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}
```

- `font-display: swap` muestra texto con la fuente de reserva hasta que cargue la personalizada.
- WOFF2 es el formato con mejor compresión; WOFF sirve como fallback.

## font shorthand

Propiedad abreviada que combina varias propiedades de fuente:

```css
/* formato: font: estilo peso tamaño/altura fuente; */
body {
  font: normal 400 1rem/1.5 'Inter', sans-serif;
}
```

> [!warning] El orden importa
> `font-size` y `line-height` son obligatorios en el shorthand. Sin ellos la declaración se ignora.

| Propiedad | Descripción | Valores comunes |
|---|---|---|
| `font-style` | Inclinación | `normal`, `italic`, `oblique` |
| `font-weight` | Grosor | `normal` (400), `bold` (700), 100–900 |
| `font-size` | Tamaño | `rem`, `em`, `px`, `%`, `clamp()` |
| `line-height` | Altura de línea | `1.5`, `1.6`, `normal` |

## font-size

Controla el tamaño del texto. Las unidades relativas son preferibles para la accesibilidad:

- `rem` — relativo al tamaño raíz (`<html>`)
- `em` — relativo al elemento padre
- `clamp(min, preferred, max)` — tamaño fluido entre límites

```html
html { font-size: 16px; }
p { font-size: 1rem; }      /* 16px */
h1 { font-size: clamp(2rem, 5vw, 3.5rem); }
```

## font-weight

Determina el grosor del trazo tipográfico:

| Valor numérico | Equivalente |
|---|---|
| 100–300 | Thin / Light |
| 400 | Normal |
| 500 | Medium |
| 600 | Semibold |
| 700 | Bold |
| 800–900 | ExtraBold / Black |

> [!note] Disponibilidad
> No todas las fuentes incluyen todos los pesos. Si un peso no existe, el navegador usa el más cercano.

## font-style

Alterna entre texto normal e inclinado:

- `normal` — estilo regular
- `italic` — cursiva nativa de la tipografía
- `oblique` — inclinación sintética del navegador

```css
em { font-style: italic; }
```

## line-height

Espacio vertical entre líneas de texto. Afecta directamente la legibilidad:

```css
body {
  line-height: 1.6;    /* recomendado para texto largo */
}

h1, h2, h3 {
  line-height: 1.2;    /* más compacto para encabezados */
}
```

> [!tip] Unidad sin unidad
> Usar `line-height` sin unidad (número puro) es la mejor práctica: hereda correctamente y es proporcional al `font-size`.

## letter-spacing

Controla el espacio entre caracteres:

```css
h1 {
  letter-spacing: 0.02em;
}

small-caps {
  letter-spacing: 0.05em;
}
```

Útil para:
- Ajustar la legibilidad de textos en mayúsculas
- Crear efectos tipográficos decorativos
- Mejorar la estética de encabezados

## Conexión con Quarto

La tipografía en CSS se relaciona con el ecosistema Quarto a través de:

- **[[scss-variables]]**: Variables SCSS como `$font-family-sans-serif` o `$font-size-base` controlan la tipografía global del sitio Quarto.
- **[[html-theming]]**: El theming de Quarto permite redefinir fuentes a nivel de sitio mediante `theme` y custom SCSS.

```scss
// Ejemplo en Quarto custom SCSS
$font-family-sans-serif: "Inter", sans-serif;
$font-family-monospace: "Fira Code", monospace;
```
