---
tags:
  - css
  - animaciones
  - keyframes
  - motion
aliases:
  - CSS Animations
  - @keyframes
created: 2025-01-01
---

# Animaciones CSS

Las animaciones CSS permiten definir secuencias de cambios de estilo mediante fotogramas claves (`@keyframes`). A diferencia de las [[transiciones]], las animaciones pueden ejecutarse automáticamente sin un disparador externo.

## La regla `@keyframes`

Define los estados intermedios de la animación:

```css
@keyframes deslizar-derecha {
  0% {
    transform: translateX(-100%);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}
```

Se pueden usar porcentajes o palabras clave `from` y `to`:

```css
@keyframes girar {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
```

## Propiedades de animación

### `animation-name`

Referencia el nombre del `@keyframes` definido:

```css
.elemento {
  animation-name: deslizar-derecha;
}
```

### `animation-duration`

Duración total de un ciclo de animación:

```css
.elemento {
  animation-duration: 1s;
  /* También en ms */
  animation-duration: 800ms;
}
```

### `animation-iteration-count`

Número de veces que se repite la animación:

```css
.elemento {
  animation-iteration-count: infinite;
  /* O un número específico: */
  animation-iteration-count: 3;
}
```

### `animation-direction`

Dirección de la animación:

```css
.elemento {
  animation-direction: normal;     /* 0% → 100% */
  animation-direction: reverse;    /* 100% → 0% */
  animation-direction: alternate;  /* alterna en cada ciclo */
  animation-direction: alternate-reverse;
}
```

### `animation-fill-mode`

Controla el estado del elemento antes/después de la animación:

```css
.elemento {
  animation-fill-mode: forwards;  /* mantiene el estado final */
  animation-fill-mode: backwards; /* aplica el estado inicial durante el delay */
  animation-fill-mode: both;      /* ambos */
  animation-fill-mode: none;      /* predeterminado */
}
```

### `animation-play-state`

Pausa o reanuda la animación:

```css
.elemento {
  animation-play-state: running;
}
.elemento:hover {
  animation-play-state: paused;
}
```

## Shorthand

El orden del atajo es:

```css
/* name | duration | timing-function | delay | iteration-count | direction | fill-mode | play-state */
.elemento {
  animation: deslizar-derecha 1s ease-in-out 0.2s infinite alternate forwards running;
}
```

## Funciones de tiempo para animaciones

Las mismas que en [[transiciones]] (`ease`, `linear`, `cubic-bezier`), pero también se pueden usar funciones escalonadas:

```css
.elemento {
  animation-timing-function: steps(4, end);
}
```

## Ejemplo práctico: loader giratorio

```css
@keyframes girar {
  to {
    transform: rotate(360deg);
  }
}

.loader {
  width: 40px;
  height: 40px;
  border: 4px solid #eee;
  border-top-color: #3498db;
  border-radius: 50%;
  animation: girar 0.8s linear infinite;
}
```

## Ejemplo práctico: fade in staggered

```css
@keyframes aparecer {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.lista-item {
  opacity: 0;
  animation: aparecer 0.5s ease forwards;
}

.lista-item:nth-child(1) { animation-delay: 0s; }
.lista-item:nth-child(2) { animation-delay: 0.1s; }
.lista-item:nth-child(3) { animation-delay: 0.2s; }
.lista-item:nth-child(4) { animation-delay: 0.3s; }
```

## Conexión con Quarto

- [[html-theming]]: Las animaciones CSS se usan en los temas de Quarto para transiciones de modo oscuro/claro, loaders de contenido, y efectos visuales en componentes como tablas y código.
- [[transiciones]]: Para cambios simples entre dos estados, las transiciones son más eficientes. Las animaciones son preferibles para secuencias complejas o auto-repetidas.
- Quarto SCSS: Cuando se personalizan temas con [[scss-variables]], las animaciones se pueden parametrizar con variables CSS, como `--animation-duration`.
