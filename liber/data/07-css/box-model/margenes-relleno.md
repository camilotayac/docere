---
tags: [css, margin, padding, espaciado]
---
# Márgenes y Relleno

Controlan el espaciado exterior e interior de un elemento dentro del [[modelo-de-caja]].

## Propiedades de margin

```css
margin-top: 1rem;
margin-right: 0;
margin-bottom: 1rem;
margin-left: auto;
```

| Valor | Resultado |
|-------|-----------|
| Longitud (`px`, `rem`, `em`) | Espacio fijo |
| `%` | Relativo al ancho del contenedor padre |
| `auto` | Distribuye el espacio disponible |

## Propiedades de padding

```css
padding-top: 1rem;
padding-right: 1.5rem;
padding-bottom: 1rem;
padding-left: 1.5rem;
```

> [!warning] No acepta `auto`
> `padding` no puede ser `auto`. Solo acepta longitudes y porcentajes.

## Sintaxis abreviada

Una sola línea para las cuatro direcciones:

```css
/* top right bottom left (sentido horario) */
margin: 10px 20px 10px 20px;

/* top/bottom left/right */
margin: 10px 20px;

/* todas las direcciones iguales */
margin: 10px;

/* top auto, left/right 20px, bottom 10px */
margin: auto 20px 10px;
```

La misma lógica aplica para `padding`.

## Centrado con margin auto

```css
.container {
  width: 800px;
  margin-left: auto;
  margin-right: auto;
}

/* shorthand */
.container {
  width: 800px;
  margin: 0 auto;
}
```

> [!note]
> Para centrar verticalmente con `margin: auto`, el elemento necesita `display: flex` o `display: grid` en el padre.

## Colapsado de márgenes

Ver [[modelo-de-caja#Colapsado de márgenes]].

## Ver también

- [[modelo-de-caja]] — Modelo de caja completo
- [[scss-variables]] — Variables Sass para espaciado consistente
- [[flexbox]] — Centrado alternativo con flexbox
