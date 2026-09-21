---
aliases: [CSS, Cascading Style Sheets]
tags: [css, fundamentos, estilos]
created: 2026-07-19
---

# Introducción a CSS

## ¿Qué es CSS?

CSS (*Cascading Style Sheets* o Hojas de Estilo en Cascada) es un lenguaje de diseño gráfico que define cómo se presentan los elementos HTML en pantalla, papel u otros medios. CSS separa la estructura del documento (HTML) de su presentación visual.

## Versiones de CSS

| Versión | Año | Características principales |
|---------|-----|-----------------------------|
| **CSS1** | 1996 | Selectores básicos, propiedades de tipografía, colores y márgenes |
| **CSS2** | 1998 | Posicionamiento, capas (`z-index`), plantillas de medios, fuentes web |
| **CSS2.1** | 2011 | Corrección de errores de CSS2, especificación más estable |
| **CSS3** | 2011+ | Modularizado: flexbox, grid, animaciones, gradientes, sombras, transiciones, media queries avanzadas |

> [!note]
> No existe un "CSS4" como especificación standalone. CSS3 se mantiene evolucionando a través de módulos independientes (CSS Grid Level 2, CSS Nesting, etc.).

## Cómo funciona CSS con HTML

HTML proporciona la **estructura** y el **contenido**. CSS define la **apariencia visual**:

```html
<!-- Estructura HTML -->
<h1>Título de la página</h1>
<p class="intro">Texto introductorio</p>

<!-- CSS controla cómo se ve -->
```

```
┌─────────────────────────────────┐
│  HTML → Estructura + Contenido  │
│  CSS  → Presentación Visual     │
│  JS   → Comportamiento          │
└─────────────────────────────────┘
```

## Tres formas de añadir CSS

### 1. CSS Externo (recomendado)

Archivo `.css` separado enlazado desde el HTML:

```html
<link rel="stylesheet" href="estilos.css">
```

**Ventajas:** reutilización, cacheo del navegador, separación de responsabilidades.

### 2. CSS Interno

Dentro de una etiqueta `<style>` en el `<head>`:

```html
<head>
  <style>
    h1 { color: navy; }
  </style>
</head>
```

**Uso típico:** estilos únicos para una sola página.

### 3. CSS Inline

Directamente en el atributo `style` del elemento:

```html
<h1 style="color: navy; font-size: 2em;">Título</h1>
```

> [!warning]
> El CSS inline tiene la máxima prioridad (excepto `!important`) y dificulta el mantenimiento. Evítalo salvo para pruebas rápidas.

## Sintaxis básica de CSS

```css
selector {
  propiedad: valor;
  otra-propiedad: otro-valor;
}
```

- **Selector:** identifica qué elementos se estilan
- **Propiedad:** qué aspecto visual se modifica
- **Valor:** la configuración aplicada

Ejemplo:

```css
p {
  color: #333333;
  font-size: 1rem;
  line-height: 1.6;
}
```

## Conexión con Quarto

CSS en Quarto se gestiona principalmente a través de:

- **[[html-theming]]**: configuración de temas visuales en proyectos Quarto HTML
- **[[scss-variables]]**: variables SCSS que permiten personalizar colores, tipografía y espaciado de forma parametrizada

```yaml
# En _quarto.yml
format:
  html:
    theme:
      - cosmo
      - custom.scss
```

---

**Ver también:** [[sintaxis]] · [[unidades]] · [[cascada-especificidad]]
