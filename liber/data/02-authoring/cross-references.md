---
title: "Referencias cruzadas"
subtitle: "Sistema de enlaces a figuras, tablas, ecuaciones y secciones"
categories:
  - "authoring"
  - "referencias"
tags:
  - "figuras"
  - "tablas"
  - "ecuaciones"
  - "secciones"
---

El sistema de referencias cruzadas de Quarto permite enlazar elementos del documento de forma automática.

## Figuras (`@fig-`)

### Sintaxis básica

```markdown
Como se muestra en @fig-ejemplo, la tendencia es clara.
```

### Etiquetado de figuras

```{r}
#| label: fig-ejemplo
#| fig-cap: "Gráfico de ejemplo"
plot(1:10)
```

### Referencia a subfiguras

```markdown
Ver @fig-subfiguras-a y @fig-subfiguras-b.
```

Con subfiguras:

```{r}
#| label: fig-subfiguras
#| fig-cap: "Subfiguras"
#| fig-subcap:
#|   - "Parte A"
#|   - "Parte B"
#| layout-ncol: 2
plot(cars)
plot(pressure)
```

## Tablas (`@tbl-`)

### Sintaxis básica

```markdown
La @tbl-datos muestra los resultados.
```

### Etiquetado de tablas

```{r}
#| label: tbl-datos
#| tbl-cap: "Tabla de datos"
knitr::kable(head(mtcars))
```

### Tablas con múltiples columnas

```{r}
#| label: tbl-compleja
#| tbl-cap: "Tabla compleja"
knitr::kable(head(mtcars[, 1:4]))
```

## Secciones (`@sec-`)

### Sintaxis básica

```markdown
Ver [[#metodos]] para más detalles.
```

### Etiquetado de secciones

```markdown
## Métodos {#metodos}
```

### Referencia con prefijo

```markdown
En la Sección [[#resultados]], se discuten...
```

## Ecuaciones

### Etiquetado de ecuaciones

```markdown
$$
E = mc^2
$$ {#eq-einstein}
```

### Referencia a ecuaciones

```markdown
De acuerdo con @eq-einstein, la energía...
```

### Ecuaciones en bloques de código

````markdown
```{math}
#| label: eq-formula
: f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
```
````

## Opciones de formato de referencia

### Prefijos personalizados

```markdown
Ver la Figura @fig-resultado.
Ver la Tabla @tbl-datos.
Ver la Ecuación @eq-formula.
```

### Cambiar formato de referencia

En `_quarto.yml`:

```yaml
crossref:
  fig-prefix: "Figura"
  tbl-prefix: "Tabla"
  eq-prefix: "Ec."
  sec-prefix: "Sec."
```

## Referencias a contenido externo

### A archivos markdown

```markdown
Ver [[conceptos-basicos]] para la definición.
```

### A secciones de otros archivos

```markdown
Ver [[libro-conceptos#seccion-especifica]].
```

## Referencias en callouts

```markdown
::: {.callout-note}
Como se mostró en @fig-anterior, el patrón...
:::
```

## Numeración automática

Quarto numera automáticamente:
- **Figuras**: Fig. 1, Fig. 2...
- **Tablas**: Tabla 1, Tabla 2...
- **Ecuaciones**: (1), (2)...
- **Secciones**: Según numeración del documento

## Opciones avanzadas

### Desactivar numeración

```yaml
crossref:
  fig-numbers: false
  tbl-numbers: false
```

### Prefijos vacíos

```yaml
crossref:
  fig-prefix: ""
  tbl-prefix: ""
```

### Formato personalizado

```yaml
crossref:
  title: "Lista de"
  fig-title: "Figuras"
  tbl-title: "Tablas"
```

## Buenas prácticas

1. **Etiqueta todos los elementos** que quieras referenciar
2. **Usa nombres descriptivos** para las etiquetas
3. **Mantén consistencia** en el formato
4. **Verifica las referencias** antes de publicar

## Véase también

- [[figures]] - Figuras y gráficos
- [[tables]] - Formato de tablas
- [[markdown-basics]] - Sintaxis de Markdown