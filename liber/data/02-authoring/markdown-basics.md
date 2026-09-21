---
title: "Conceptos básicos de Markdown"
subtitle: "Sintaxis fundamental para documentos Quarto"
categories:
  - "authoring"
  - "markdown"
tags:
  - "sintaxis"
  - "básico"
---

Markdown es el formato de autoría principal en Quarto, con extensiones específicas para contenido técnico y científico.

## Encabezados

Los encabezados usan almohadillas (`#`):

```markdown
# Encabezado nivel 1
## Encabezado nivel 2
### Encabezado nivel 3
#### Encabezado nivel 4
##### Encabezado nivel 5
###### Encabezado nivel 6
```

## Énfasis

| Sintaxis | Resultado |
|----------|-----------|
| `*cursiva*` | *cursiva* |
| `**negrita**` | **negrita** |
| `***negrita cursiva***` | ***negrita cursiva*** |
| `~~tachado~~` | ~~tachado~~ |

## Listas

### Lista desordenada

```markdown
- Elemento 1
- Elemento 2
  - Subelemento 2a
  - Subelemento 2b
- Elemento 3
```

### Lista ordenada

```markdown
1. Primer paso
2. Segundo paso
3. Tercer paso
```

## Enlaces e imágenes

### Enlaces

```markdown
[Texto del enlace](https://ejemplo.com)
[Enlace con título](https://ejemplo.com "Título")
[[wikilink]]  # Estilo Obsidian
```

### Imágenes

```markdown
![Texto alternativo](imagen.png)
![Imagen con tamaño](imagen.png){ width=50% }
![Imagen alineada](imagen.png){ fig-align="center" }
```

## Bloques de código

### Código en línea

```markdown
Usa `print()` para mostrar valores.
```

### Bloques de código con opciones

````markdown
```{r}
#| label: fig-ejemplo
#| fig-cap: "Una figura de ejemplo"
#| echo: false
library(ggplot2)
ggplot(mtcars, aes(wt, mpg)) + geom_point()
```
````

Opciones comunes:
- `echo`: Mostrar código fuente
- `eval`: Evaluar el código
- `output`: Mostrar resultados
- `warning`: Mostrar advertencias
- `message`: Mostrar mensajes

## Divs y vallas (:::)

Las divs crean bloques con clases personalizadas:

```markdown
::: {.callout-note}
Esto es una nota informativa.
:::

::: {.callout-warning}
Esto es una advertencia.
:::
```

### Ejemplo con estilos

```markdown
::: {.panel-tabset}
## Pestaña 1
Contenido de la pestaña 1.

## Pestaña 2
Contenido de la pestaña 2.
:::
```

## Front matter YAML

El encabezado YAML al inicio del archivo configura metadatos:

```yaml
---
title: "Mi Documento"
subtitle: "Una introducción"
author: "Autor Ejemplo"
date: "2024-01-15"
categories:
  - "categoría1"
  - "categoría2"
tags:
  - "etiqueta1"
  - "etiqueta2"
format:
  html:
    theme: cosmo
  pdf: default
---
```

### Metadatos comunes

| Campo | Descripción |
|-------|-------------|
| `title` | Título del documento |
| `subtitle` | Subtítulo |
| `author` | Autor(es) |
| `date` | Fecha de publicación |
| `categories` | Categorías temáticas |
| `tags` | Etiquetas |
| `format` | Formatos de salida |
| `lang` | Idioma del documento |

## Tablas simples

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |
```

## Citas

```markdown
> Esto es una cita en bloque.
> 
> -- Autor Ejemplo
```

## Reglas horizontales

```markdown
---
***
___
```

## Comentarios HTML

```markdown
<!-- Esto es un comentario que no se muestra -->
```

## Véase también

- [[figures]] - Inclusión y formato de figuras
- [[tables]] - Tablas avanzadas
- [[callouts]] - Llamadas y notas
- [[cross-references]] - Referencias cruzadas