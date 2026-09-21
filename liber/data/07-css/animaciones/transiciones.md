---
tags:
  - css
  - animaciones
  - transiciones
  - hover
aliases:
  - CSS Transitions
  - transition property
created: 2025-01-01
---

# Transiciones CSS

Las transiciones CSS permiten animar cambios entre dos estados de un elemento de forma suave. A diferencia de las [[animaciones-css]], las transiciones requieren un disparador (como `:hover`, `:focus` o cambio de clase).

## La propiedad `transition`

La propiedad `transition` es el atajo para las cuatro propiedades individuales:

```css
.elemento {
  transition: all 0.3s ease-in-out;
}
```

## Propiedades individuales

### `transition-property`

Define qué propiedades CSS se animarán.

```css
.elemento {
  transition-property: opacity, transform;
  /* Otras opciones: */
  /* all — anima todas las propiedades transicionables */
  /* none — no anima nada */
}
```

### `transition-duration`

Establece la duración de la transición.

```css
.elemento {
  transition-duration: 0.3s;
  /* También en ms: */
  transition-duration: 300ms;
}
```

### `transition-timing-function`

Controla la curva de aceleración de la transición.

```css
.elemento {
  transition-timing-function: ease;
  /* Opciones: linear | ease | ease-in | ease-out | ease-in-out */
}
```

Valores comunes de `timing-function`:

| Función | Descripción |
|---|---|
| `linear` | Velocidad constante |
| `ease` | Inicio lento, rápido al final, lento al final (predeterminado) |
| `ease-in` | Inicio lento, aceleración gradual |
| `ease-out` | Desaceleración gradual |
| `ease-in-out` | Inicio y final lentos |
| `cubic-bezier(x1, y1, x2, y2)` | Curva personalizada |

### `transition-delay`

Retraso antes de que la transición comience.

```css
.elemento {
  transition-delay: 0.1s;
}
```

## Shorthand

La forma abreviada sigue el orden:

```css
/* property | duration | timing-function | delay */
.elemento {
  transition: opacity 0.3s ease 0s, transform 0.4s ease-in-out 0.1s;
}
```

## Efectos hover comunes

### Fade in/out

```css
.boton {
  background-color: #3498db;
  transition: opacity 0.3s ease;
}
.boton:hover {
  opacity: 0.8;
}
```

### Escalado

```css
.tarjeta {
  transform: scale(1);
  transition: transform 0.3s ease;
}
.tarjeta:hover {
  transform: scale(1.05);
}
```

### Desplazamiento vertical

```css
.boton {
  transform: translateY(0);
  transition: transform 0.2s ease;
}
.boton:hover {
  transform: translateY(-3px);
}
```

### Cambio de color de fondo

```css
.enlace {
  background-color: transparent;
  transition: background-color 0.3s ease;
}
.enlace:hover {
  background-color: rgba(52, 152, 219, 0.1);
}
```

### Sombra apareciendo

```css
.tarjeta {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}
.tarjeta:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
```

### Subrayado animado

```css
.enlace {
  text-decoration: none;
  background-image: linear-gradient(#3498db, #3498db);
  background-size: 0% 2px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size 0.3s ease;
}
.enlace:hover {
  background-size: 100% 2px;
}
```

## Conexión con Quarto

- [[html-theming]]: Las transiciones se usan en los temas de Quarto para animar cambios de color, modo oscuro/claro, y estilos de componentes interactivos.
- [[animaciones-css]]: Las transiciones son un subconjunto más simple de las animaciones CSS. Para secuencias complejas de fotogramas, usar `@keyframes`.
- Las transiciones son útiles en Quarto para suavizar cambios de tema en modos oscuro/claros, ya que Quarto aplica clases como `body.dark-mode` que cambian variables CSS.
