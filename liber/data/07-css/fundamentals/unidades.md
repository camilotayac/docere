---
aliases: [unidades CSS, medidas CSS]
tags: [css, fundamentos, unidades, diseño]
created: 2026-07-19
---

# Unidades en CSS

Las unidades de CSS definen las magnitudes de las propiedades: tamaños, espaciados, posiciones y más.

## Unidades absolutas

Miden valores fijos, independientes del contexto:

| Unidad | Símbolo | Equivalencia |
|--------|---------|--------------|
| Píxel | `px` | 1/96 de pulgada |
| Punto | `pt` | 1/72 de pulgada |
| Centímetro | `cm` | 1cm = 37.8px |
| Milímetro | `mm` | 1mm = 3.78px |
| Pulgada | `in` | 1in = 96px = 2.54cm |

```css
.titulo {
  font-size: 24px;
}

.borde {
  border-width: 1pt;
}

.impreso {
  width: 21cm;  /* A4 width */
}
```

> [!warning]
> Las unidades absolutas no se adaptan al contexto del usuario (tamaño de fuente, zoom). Úsalas con moderación en diseño web.

### Cuándo usar unidades absolutas

- **`px`**: bordes finos, sombras, tamaños de iconos, diseño gráfico de precisión
- **`pt`**: documentos impresos (CSS para `@media print`)
- **`cm`, `mm`, `in`**: contextos de impresión

## Unidades relativas

Cambian según el contexto del elemento padre, del usuario o del viewport:

| Unidad | Basada en |
|--------|-----------|
| `em` | Tamaño de fuente del elemento padre |
| `rem` | Tamaño de fuente del elemento raíz (`<html>`) |
| `%` | Ancho del elemento padre |
| `vw` | Ancho del viewport (1vw = 1% del ancho) |
| `vh` | Alto del viewport (1vh = 1% del alto) |
| `vmin` | Dimensión menor del viewport |
| `vmax` | Dimensión mayor del viewport |
| `ch` | Ancho del carácter "0" de la fuente actual |
| `ex` | Altura de la "x" de la fuente actual |

```css
.contenedor {
  width: 80%;           /* 80% del padre */
  max-width: 1200px;    /* tope absoluto */
}

.hero {
  height: 100vh;        /* altura completa del viewport */
}

.texto {
  font-size: 1.2em;     /* 1.2 × fuente del padre */
  max-width: 65ch;      /* óptimo para legibilidad */
}
```

## rem vs em: la diferencia clave

### `em` — relativo al padre

```css
/* Fuente base del body: 16px */
body { font-size: 16px; }

/* Fuente del padre (.card): 20px (1.25em × 16px) */
.card {
  font-size: 1.25em;  /* = 20px */
}

/* Fuente del hijo (.card p): 1.5em × 20px = 30px */
.card p {
  font-size: 1.5em;   /* = 30px (¡más grande de lo esperado!) */
}
```

El problema de `em` es la **acumulación**: cada nivel multiplica el valor del padre.

### `rem` — relativo a la raíz

```css
/* Fuente raíz: 16px */
html { font-size: 16px; }

/* .card p siempre será: 1.5rem × 16px = 24px */
.card p {
  font-size: 1.5rem;  /* = 24px (predictible) */
}
```

> [!tip]
> **En Quarto, `rem` es la unidad recomendada para tipografía.** Permite escalar todo el sitio cambiando solo el `font-size` de `:root`. Ver [[scss-variables]] para implementación.

## Unidades para diferentes contextos

### Tipografía

```css
:root {
  font-size: 16px;           /* base del sitio */
}

body {
  font-size: 1rem;           /* = 16px */
  line-height: 1.6;          /* adimensional (sin unidad) */
}

h1 {
  font-size: 2.5rem;         /* = 40px */
  letter-spacing: -0.02em;   /* ajuste fino con em */
}

p {
  font-size: 1rem;
  max-width: 65ch;           /* 65 caracteres ≈ óptimo de lectura */
}
```

### Espaciado y layout

```css
.espaciado {
  padding: 1.5rem;           /* consistente con la tipografía */
  margin-bottom: 2em;        /* proporcional al contexto */
}

.columna {
  width: 33.333%;            /* un tercio del padre */
  gap: 2vw;                  /* proporcional al viewport */
}
```

### Responsive

```css
.imagen {
  width: 100%;               /* del contenedor */
  max-width: min(80vw, 800px); /* condicional */
  aspect-ratio: 16/9;        /* proporción fija */
}
```

## Unidad `ch` para legibilidad

```css
/* Longitud óptima para lectura: 45-75 caracteres */
.articulo {
  max-width: 70ch;
  font-size: 1rem;
}

/* Código */
pre {
  max-width: 80ch;
  overflow-x: auto;
}
```

## Conexión con Quarto

### [[scss-variables]] — unidades parametrizadas

```scss
// Definición de unidades en SCSS
$font-size-base: 1rem;
$spacing-unit: 1rem;
$breakpoint-tablet: 768px;
$breakpoint-desktop: 1024px;

// Uso consistente
.sidebar {
  width: 300px;
  padding: $spacing-unit * 1.5;
}

@media (min-width: $breakpoint-desktop) {
  .content { max-width: 75ch; }
}
```

### [[html-theming]] — responsive con unidades relativas

Quarto usa unidades relativas en sus temas por defecto para garantizar accesibilidad:

```scss
// En custom.scss para Quarto
$theme-font-size-base: 1rem;
$theme-font-family-sans: "Inter", sans-serif;

body {
  font-size: $theme-font-size-base;
}

.sidebar {
  width: min(250px, 30vw);
}
```

> [!note]
> Los temas de Quarto usan `rem` como unidad base. Cambiar el `font-size` del `:root` en la configuración del tema escala toda la interfaz.

---

**Ver también:** [[introduccion]] · [[sintaxis]] · [[cascada-especificidad]]
