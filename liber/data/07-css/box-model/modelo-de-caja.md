---
tags: [css, box-model, layout]
aliases: [box model]
---
# Modelo de Caja

Todo elemento HTML es un rectangular compuesto por: **content**, **padding**, **border** y **margin**.

```text
┌─────────────────────────┐
│         margin          │
│  ┌───────────────────┐  │
│  │      border       │  │
│  │  ┌─────────────┐  │  │
│  │  │   padding    │  │  │
│  │  │  ┌───────┐  │  │  │
│  │  │  │content│  │  │  │
│  │  │  └───────┘  │  │  │
│  │  └─────────────┘  │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

## Componentes

| Componente | Descripción |
|------------|-------------|
| **content** | El área donde se muestra el texto e imágenes |
| **padding** | Espacio entre el contenido y el borde |
| **border** | Línea que rodea el padding |
| **margin** | Espacio exterior que separa el elemento de otros |

## box-sizing

Controla cómo se calcula el ancho y alto total.

```css
/* Valor por defecto: width/height = solo content */
box-sizing: content-box;

/* Width/height = content + padding + border */
box-sizing: border-box;
```

> [!tip] Recomendación universal
> Aplicar `border-box` globalmente simplifica los cálculos:
> ```css
> *, *::before, *::after { box-sizing: border-box; }
> ```

## Cálculo de dimensiones

Con `content-box` el ancho total incluye padding y border:

```
ancho total = width + padding-left + padding-right + border-left + border-right
```

Con `border-box` el ancho total ya incluye padding y border:

```
ancho total = width
```

## Colapsado de márgenes

Los márgenes verticales adyacentes se **colapsan** tomando el mayor de ambos, no se suman. Esto ocurre entre:

- Elementos hermanos (`margin-bottom` del primero con `margin-top` del segundo)
- Elemento padre e hijo (cuando el padre no tiene padding/border que los separe)

Los márgenes **no colapsan** horizontalmente ni con elementos flotantes.

## Ver también

- [[margenes-relleno]] — Propiedades de margin y padding
- [[html-theming]] — Aplicación del modelo de caja en Quarto
- [[scss-variables]] — Variables para espaciado y dimensiones
