---
title: "Tablas"
subtitle: "Creación y formato de tablas en Quarto"
categories:
  - "authoring"
  - "tablas"
tags:
  - "pipe-tables"
  - "grid-tables"
  - "cross-references"
---

Quarto soporta múltiples formatos de tablas con opciones avanzadas de estilo y referencias.

## Pipe tables (tablas de tubería)

La sintaxis más común para tablas simples:

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Celda 1   | Celda 2   | Celda 3   |
| Celda 4   | Celda 5   | Celda 6   |
```

### Alineación

```markdown
| Izquierda | Centro | Derecha |
|:----------|:------:|--------:|
| Texto     | Texto  | Texto   |
```

## Grid tables (tablas de cuadrícula)

Para tablas más complejas con bordes:

```markdown
+-----------+-----------+-----------+
| Columna 1 | Columna 2 | Columna 3 |
+===========+===========+===========+
| Celda 1   | Celda 2   | Celda 3   |
+-----------+-----------+-----------+
| Celda 4   | Celda 5   | Celda 6   |
+-----------+-----------+-----------+
```

### Celdas combinadas

```markdown
+-----------+-----------+-----------+
| Columna 1 | Columna 2 | Columna 3 |
+===========+===========+===========+
| Celda combinada                    |
+-----------+-----------+-----------+
| Celda 4   | Celda 5   | Celda 6   |
+-----------+-----------+-----------+
```

## Referencias cruzadas de tablas

### Sintaxis de referencia

```markdown
Como se muestra en @tbl-datos, los valores...

::: {#tbl-datos}
| Variable | Valor |
|----------|-------|
| A        | 1     |
| B        | 2     |

Tabla de ejemplo.
:::
```

### Con prefijo

```markdown
Ver la @tbl-resultados para los detalles.
```

## Tablas desde código

### R

````markdown
```{r}
#| label: tbl-datos
#| tbl-cap: "Datos del ejemplo"
knitr::kable(head(mtcars))
```
````

### Python

````markdown
```{python}
#| label: tbl-python
#| tbl-cap: "Tabla desde Python"
import pandas as pd
pd.DataFrame({'A': [1,2], 'B': [3,4]})
```
````

## Opciones de formato de tabla

### Anchos de columna

```{r}
#| label: tbl-ancho
#| tbl-cap: "Tabla con anchos personalizados"
#| tbl-colwidths: [30, 40, 30]
knitr::kable(head(mtcars[, 1:3]))
```

### Estilo de tabla

```{r}
#| label: tbl-estilo
#| tbl-cap: "Tabla con estilo kableExtra"
#| tbl-cap-location: top
library(kableExtra)
kable(head(mtcars), format = "html") %>%
  kable_styling(bootstrap_options = c("striped", "hover"))
```

## Tablas anchas con scroll

Para tablas que exceden el ancho de la página:

### En HTML

```markdown
::: {style="overflow-x: auto;"}
| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
|-------|-------|-------|-------|-------|-------|-------|
| 1     | 2     | 3     | 4     | 5     | 6     | 7     |
:::
```

### En código

```{r}
#| label: tbl-scroll
#| tbl-cap: "Tabla con scroll horizontal"
#| column: page
#| code-fold: true
kable(head(mtcars), format = "html", scrollable = TRUE)
```

## Opciones avanzadas

### Ubicación de leyenda

```yaml
#| tbl-cap-location: top
#| tbl-cap-location: bottom
#| tbl-cap-location: margin
```

### Notas de tabla

```markdown
::: {#tbl-notas}
| Datos |
|-------|
| 1     |

Tabla con notas.^[Nota al pie de tabla]
:::
```

### Tablas en márgenes

```{r}
#| label: tbl-margen
#| tbl-cap: "Tabla en el margen"
#| column: margin
knitr::kable(head(mtcars[, 1:2]))
```

## Tablas LaTeX

Para tablas en formato PDF con control fino:

```markdown
::: {#tbl-latex}
|   | A | B | C |
|:-:|:-:|:-:|:-:|
| 1 | 1 | 2 | 3 |
| 2 | 4 | 5 | 6 |

Tabla con formato LaTeX.
:::
```

## Buenas prácticas

1. **Usa etiquetas consistentes** para referencias
2. **Incluye leyendas descriptivas**
3. **Considera el formato de salida** al diseñar
4. **Mantén las tablas simples** cuando sea posible

## Véase también

- [[cross-references]] - Referencias cruzadas
- [[figures]] - Figuras y gráficos
- [[customizing-output]] - Opciones de formato