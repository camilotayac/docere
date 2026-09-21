---
up:: [[html]]
tags:: [html]
---

# Listas en HTML

Las listas organizan contenido en ítems relacionados. HTML ofrece tres tipos
con un propósito semántico diferente.

## Lista ordenada: `<ol>`

Se usa cuando el orden importa. `start` define el número inicial y `type`
cambia la numeración: `A`, `a`, `I`, `i`.

```html
<ol start="5" type="A">
  <li>Ítem cinco</li>
  <li>Ítem seis</li>
</ol>
```

## Lista desordenada: `<ul>`

Items sin orden específico, con viñetas por defecto.

```html
<ul>
  <li>Elemento uno</li>
  <li>Elemento dos</li>
</ul>
```

## Lista de definición: `<dl>`

Asocia términos `<dt>` con definiciones `<dd>`.

```html
<dl>
  <dt>HTML</dt>
  <dd>Lenguaje de marcado para estructurar contenido web.</dd>
</dl>
```

## Anidamiento y estilos

Las listas se anidan colocando una dentro de un `<li>` y se personalizan
con `list-style-type`, `list-style-position` e `list-style-image` en CSS.

```html
<ol><li>Paso <ul><li>Subtarea</li></ul></li></ol>
```

Ver también: [[html-elements]]
