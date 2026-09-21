---
title: Formatos de color en CSS
tags: [css, colores, accesibilidad]
aliases: [colores-css, formatos-color]
---

## Formatos de color

CSS ofrece múltiples formas de definir colores. Cada formato tiene ventajas según el caso de uso.

### Colores con nombre

Son 148 colores nombrados estandarizados:

```css
body { background-color: white; }
a { color: tomato; }
.error { color: crimson; }
```

> [!note] Limitación
> Solo cubren una paleta fija. No permiten matices intermedios. Útiles para prototipado rápido.

### HEX (hexadecimal)

Representa colores usando valores hexadecimales. Formato: `#RRGGBB` o abreviado `#RGB`:

```css
:root {
  --primary: #2563eb;       /* azul */
  --text: #1f2937;          /* gris oscuro */
  --accent: #f59e0b;        /* ámbar */
  --transparent: #00000080; /* negro con 50% opacidad (8 dígitos) */
}
```

El canal alfa (8º dígito) permite controlar la transparencia: `#RRGGBBAA`.

### RGB / RGBA

Usa valores decimales (0–255) para cada canal. RGBA incluye canal alfa para transparencia:

```css
:root {
  --primary-rgb: rgb(37, 99, 235);
  --overlay: rgba(0, 0, 0, 0.6);
  --card-bg: rgb(255 255 255 / 0.9);  /* sintaxis moderna con / */
}
```

La sintaxis moderna usa espacios en vez de comas y `/` para el alfa.

### HSL / HSLA

Modelo basado en Matiz (Hue), Saturación (Saturation) y Luminosidad (Lightness). Más intuitivo para ajustar tonos:

```css
:root {
  --primary: hsl(217, 91%, 60%);
  --success: hsl(142, 71%, 45%);
  --danger: hsl(0, 84%, 60%);
  --overlay: hsla(0, 0%, 0%, 0.5);
}
```

| Componente | Rango | Descripción |
|---|---|---|
| Hue | 0–360 | Matiz en el círculo cromático |
| Saturation | 0%–100% | Intensidad del color (0% = gris) |
| Lightness | 0%–100% | Brillo (0% = negro, 100% = blanco) |

> [!tip] Ventaja de HSL
> Es fácil generar variaciones de un color ajustando solo la luminosidad o saturación. Ideal para paletas de diseño.

```css
/* Variaciones de un mismo tono */
--color-100: hsl(217, 91%, 95%);
--color-300: hsl(217, 91%, 75%);
--color-500: hsl(217, 91%, 60%);
--color-700: hsl(217, 91%, 40%);
--color-900: hsl(217, 91%, 20%);
```

## opacity

Controla la opacidad de un elemento completo (incluyendo hijos):

```css
.overlay {
  background-color: black;
  opacity: 0.5;    /* 50% transparente */
}

.card {
  opacity: 0.9;
}
```

> [!warning] Diferencia con rgba/hsla
> `opacity` afecta todo el elemento y sus hijos. Para transparencia solo en el fondo, usar `rgba()` o `hsla()`.

| Valor | Efecto |
|---|---|
| `0` | Completamente invisible |
| `0.5` | 50% transparente |
| `1` | Completamente opaco (valor por defecto) |

## Color y contraste — WCAG

Las pautas de accesibilidad web (WCAG 2.1) establecen ratios mínimos de contraste:

| Nivel | Ratio mínimo | Uso |
|---|---|---|
| AA (normal) | 4.5:1 | Texto regular |
| AA (grande) | 3:1 | Texto ≥ 18px o ≥ 14px bold |
| AAA (normal) | 7:1 | Contraste alto |
| AAA (grande) | 4.5:1 | Contraste alto, texto grande |

### Herramientas de verificación

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/)
- Chrome DevTools: inspect → pestaña "Accessibility" → muestra el ratio calculado

## Accesibilidad de colores

> [!important] Regla fundamental
> El color **nunca** debe ser el único medio para transmitir información.

Buenas prácticas:
- Combinar color con **texto, iconos o patrones** para indicar estados
- No usar solo color rojo para errores: acompañar con texto descriptivo
- Probar la interfaz en modo escala de grises (DevTools → Rendering → Emulate vision deficiency)
- Usar herramientas de simulación de daltonismo

```css
/* Ejemplo: indicador de error accesible */
.error-field {
  border: 2px solid var(--danger);
}

.error-field::after {
  content: "Este campo es obligatorio";
  /* Texto explícito además del borde rojo */
}
```

### Paletas accesibles

- Usar colores con suficiente contraste entre sí
- Verificar todos los estados: normal, hover, focus, disabled
- Incluir indicadores de foco visibles para navegación por teclado

## Conexión con Quarto

Los colores en CSS se integran en Quarto mediante:

- **[[html-theming]]**: El sistema de theming de Quarto acepta colores personalizados para fondo, texto, enlaces y más.
- **[[scss-variables]]**: Variables como `$body-bg`, `$body-color`, `$link-color` definen la paleta del sitio.

```scss
// Paleta Quarto
$body-bg: #ffffff;
$body-color: #1f2937;
$link-color: #2563eb;
$danger: hsl(0, 84%, 60%);
```

> [!tip] Tema oscuro
> Quarto permite definir temas claros y oscuros con `_quarto.yml`. Las variables SCSS se redefinen con `[data-bs-theme="dark"]`.
