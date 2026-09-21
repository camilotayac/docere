---
title: "Opciones básicas de HTML en Quarto"
description: "Configuración fundamental para documentos HTML: TOC, numeración, código y gráficos"
---

## Tabla de contenidos

### `toc`

Activa o desactiva la tabla de contenidos lateral:

```yaml
format:
  html:
    toc: true  # activa el TOC
```

### `toc-depth`

Controla hasta qué nivel de encabezados se incluye en el TOC:

```yaml
format:
  html:
    toc: true
    toc-depth: 3  # incluye h1, h2 y h3
```

El valor por defecto es `3`.

### `toc-location`

Ubicación del TOC. Opciones disponibles:

| Valor | Descripción |
|-------|-------------|
| `left` | Sidebar izquierda (por defecto) |
| `right` | Sidebar derecha |

```yaml
format:
  html:
    toc: true
    toc-location: right
```

## Numeración de secciones

### `number-sections`

Numera automáticamente las secciones:

```yaml
format:
  html:
    number-sections: true
```

## Código

### `code-fold`

Permite plegar/desplegar bloques de código:

```yaml
format:
  html:
    code-fold: true
```

Opciones de `code-fold`:

| Valor | Descripción |
|-------|-------------|
| `true` | Código plegado por defecto, usuario puede desplegar |
| `false` | Código siempre visible (por defecto) |
| `show` | Código siempre visible con botón de plegar |

### `code-summary`

Texto que se muestra cuando el código está plegado:

```yaml
format:
  html:
    code-fold: true
    code-summary: "Ver código"
```

Por defecto muestra "Code".

## Gráficos

### `fig-width` y `fig-height`

Tamaño de las figuras generadas por código (en pulgadas):

```yaml
format:
  html:
    fig-width: 8    # ancho en pulgadas
    fig-height: 5   # alto en pulgadas
```

### `fig-cap`

Pie de figura por defecto:

```yaml
format:
  html:
    fig-cap: true  # muestra los pies de figura
```

## Inclusión de contenido externo

### `include-after-body`

Incluye contenido HTML después del `<body>`:

```yaml
format:
  html:
    include-after-body: _includes/footer.html
```

Útil para scripts o elementos que deben cargarse al final.

### `include-in-header`

Incluye contenido en el `<head>` del documento:

```yaml
format:
  html:
    include-in-header: _includes/meta.html
```

Útil para meta tags, scripts externos o estilos adicionales.

## Ejemplo completo de configuración básica

```yaml
---
title: "Mi documento"
author: "Autor"
date: today
format:
  html:
    toc: true
    toc-depth: 3
    toc-location: left
    number-sections: true
    code-fold: true
    code-summary: "Ver código"
    fig-width: 10
    fig-height: 6
    include-in-header: _styles/custom-head.html
    include-after-body: _includes/footer.html
---
```
