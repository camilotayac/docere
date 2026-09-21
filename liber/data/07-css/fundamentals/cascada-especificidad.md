---
aliases: [cascade, specificity, especificidad]
tags: [css, fundamentos, cascada, especificidad]
created: 2026-07-19
---

# Cascada y Especificidad en CSS

La cascada y la especificidad son los mecanismos que determinan **qué regla CSS se aplica** cuando múltiples declaraciones compiten por el mismo elemento y la misma propiedad.

## La Cascada (Cascade)

El algoritmo de cascada resuelve conflictos siguiendo este orden de precedencia (de menor a mayor):

```
1. Hojas de estilo del navegador (user-agent)
2. Hojas de estilo del usuario
3. Hojas de estilo del autor (desarrollador)
4. !important del usuario
5. !important del autor
6. Transiciones CSS
```

### Orden de resolución paso a paso

```
┌─────────────────────────────────────────┐
│  Reglas aplicables al mismo elemento    │
│                                         │
│  1. ¿Cuántas reglas coinciden?          │
│  2. ¿Cuál tiene mayor especificidad?    │
│  3. ¿Cuál aparece después en el código? │
│                                         │
│  → Gana la de mayor especificidad       │
│  → En empate, gana la última declarada  │
└─────────────────────────────────────────┘
```

```css
/* Regla 1 — específica pero temprana */
#header { color: blue; }

/* Regla 2 — menos específica pero posterior */
div { color: red; }

/* Resultado: #header gana → color: blue (0-1-0 > 0-0-1) */
```

## Especificidad (Specificity)

### Sistema de pesos

La especificidad se calcula como un sistema de tres niveles (o cuatro con inline):

```
(a, b, c)
```

| Nivel | Tipo | Ejemplo | Peso |
|-------|------|---------|------|
| a | Inline style | `style="..."` | 1,000 |
| b | ID | `#main-title` | 100 por cada ID |
| c | Clase, atributo, pseudo-clase | `.card`, `[data-id]`, `:hover` | 10 por cada uno |
| d | Elemento, pseudo-elemento | `p`, `::before` | 1 por cada uno |

> [!note]
> El selector universal `*` y combinadores `>`, `+`, `~` tienen especificidad 0.

### Ejemplos de cálculo

```css
/* Especificidad: (0, 0, 1) = 1 */
p { color: black; }

/* Especificidad: (0, 1, 0) = 10 */
.intro { color: navy; }

/* Especificidad: (0, 0, 2) = 2 */
p.intro { color: teal; }

/* Especificidad: (0, 1, 1) = 11 */
.intro.special { color: purple; }

/* Especificidad: (1, 0, 0) = 100 */
#main-title { color: darkred; }

/* Especificidad: (1, 1, 0) = 110 */
#main-title.highlight { color: orange; }
```

> [!warning]
> **No se suma como números decimales.** (0, 1, 0) es mayor que (0, 0, 99) porque un ID siempre supera a cualquier cantidad de clases.

### Visualización práctica

```css
/* (0, 0, 1) — gana sobre nada más específico */
a { color: blue; }

/* (0, 1, 0) — gana sobre el anterior */
.nav-link { color: teal; }

/* (0, 1, 1) — gana sobre ambos */
.nav-link.active { color: green; }

/* (1, 0, 0) — gana sobre todos los anteriores */
#logo { color: red; }
```

## `!important`

La declaración `!important` sobreescribe cualquier especificidad (excepto otro `!important` de igual o mayor especificidad):

```css
/* Sin importar la especificidad */
秘!important { color: purple !important; }

/* Especificidad más alta pero pierde */
#header { color: blue; }  /* pierde contra !important */
```

### Reglas de `!important`

1. `!important` del autor vs normal del usuario → gana `!important`
2. `!important` del autor vs `!important` del usuario → gana el usuario
3. `!important` en misma capa → resuelve por especificidad
4. Última declaración `!important` en el archivo gana en empate

> [!warning]
> `!important` es un último recurso. Su uso excesivo crea especificidad innecesaria y dificulta el mantenimiento. Preferir selectores específicos o [[scss-variables]] con arquitectura limpia.

### Alternativas a `!important`

```css
/* ❌ Evitar */
.sidebar .widget p { font-size: 14px !important; }

/* ✅ Preferir — aumentar especificidad de forma controlada */
.sidebar .widget p { font-size: 14px; }

/* ✅ O usar una clase más específica */
.sidebar-widget-text { font-size: 14px; }
```

## Herencia

### Propiedades heredables

```css
/* Se heredan a los hijos */
body {
  color: #333;
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  text-align: left;
  visibility: visible;
  cursor: default;
}
```

### Propiedades NO heredables

```css
/* No se heredan — cada elemento necesita declararlas */
.bloque {
  border: 1px solid #ccc;
  padding: 1rem;
  margin: 2rem;
  background: white;
  width: 100%;
  overflow: hidden;
}
```

### Valores de herencia

```css
/* Hereda el valor del padre */
h1 { color: inherit; }

/* Valor inicial del navegador (resetea) */
h1 { color: initial; }

/* Resetea según CSS o UA si no está definido */
h1 { color: unset; }

/* Respeta la cascade normalmente */
h1 { color: revert; }
```

## Estrategias para manejar especificidad

### 1. Arquitectura por capas

```css
@layer base, components, utilities;

@layer base {
  p { line-height: 1.6; }
}

@layer components {
  .card { padding: 1.5rem; }
}

@layer utilities {
  .hidden { display: none; }
}
```

### 2. Metodología BEM (Block Element Modifier)

```css
/* BEM reduce conflictos de especificidad */
.block { }
.block__element { }
.block--modifier { }
.block__element--modifier { }
```

### 3. Evitar IDs para estilos

```css
/* ❌ Alta especificidad, difícil de sobreescribir */
#sidebar .widget p { }

/* ✅ Clases, especificidad predecible */
.sidebar-widget p { }
```

## Conexión con Quarto

### [[html-theming]] — orden de carga

En Quarto, los estilos se cargan en este orden (de menor a mayor precedencia):

1. Estilos del tema base (ej: `cosmo`)
2. Estilos del SCSS personalizado
3. Estilos CSS inline

Esto permite personalizar sin `!important`:

```scss
// custom.scss — sobreescribe el tema base
$primary: #2c3e50;

body {
  font-family: 'Inter', sans-serif;  // gana sobre el tema base
}

.sidebar {
  background: $primary;
}
```

### [[scss-variables]] — gestión de especificidad

```scss
// Variables permiten consistencia sin especificidad excesiva
$color-texto: #333;
$color-fondo: #fff;
$espaciado-base: 1rem;

// Todas las reglas usan las mismas variables
// → misma especificidad, fácil de mantener
```

### [[introduccion]] — cascade en acción

```yaml
# _quarto.yml — temas en cascada
format:
  html:
    theme:
      - cosmo          # tema base
      - custom.scss    # sobreescribe parcialmente
    css: styles.css    # sobreescribe completamente
```

---

**Ver también:** [[introduccion]] · [[sintaxis]] · [[unidades]]
