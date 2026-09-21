---
title: "Figuras"
subtitle: "Inclusión, formato y referencias de figuras"
categories:
  - "authoring"
  - "figuras"
tags:
  - "imágenes"
  - "subfigures"
  - "cross-references"
---

Las figuras en Quarto soportan imágenes estáticas y gráficos generados por código, con opciones avanzadas de formato.

## Sintaxis básica de figuras

### Imagen estática

```markdown
![Descripción de la imagen](imagen.png){#fig-ejemplo}
```

### Figura desde código

````markdown
```{r}
#| label: fig-grafico
#| fig-cap: "Título de la figura"
#| fig-width: 8
#| fig-height: 5
library(ggplot2)
ggplot(mtcars, aes(wt, mpg)) + geom_point()
```
````

## Subfiguras

Las subfiguras se crean usando la sintaxis `panel`:

````markdown
```{r}
#| label: fig-subfiguras
#| fig-cap: "Ejemplo de subfiguras"
#| fig-subcap:
#|   - "Subfigura A"
#|   - "Subfigura B"
#| layout-ncol: 2
plot(cars)
plot(pressure)
```
````

### Subfiguras con imágenes estáticas

```markdown
::: {#fig-subfiguras layout-ncol="2"}
![Subfigura A](imagen-a.png){#fig-a}

![Subfigura B](imagen-b.png){#fig-b}

Ejemplo de subfiguras usando paneles.
:::
```

## Referencias cruzadas de figuras

### Sintaxis de referencia

```markdown
Como se muestra en @fig-ejemplo, los datos...
```

### Con prefijo personalizado

```markdown
Ver la Figura 1 en @fig-resultado.
```

### Referencia a subfiguras

```markdown
Como se ve en @fig-subfiguras-a y @fig-subfiguras-b...
```

## Ancho y alineación

### Ancho de figura

```markdown
![Imagen](foto.png){ width=75% }

![Imagen](foto.png){ width=500px }
```

### Alineación

```markdown
![Imagen centrada](foto.png){ fig-align="center" }

![Imagen a la izquierda](foto.png){ fig-align="left" }

![Imagen a la derecha](foto.png){ fig-align="right" }
```

### Opciones de ancho en código

```{r}
#| label: fig-ancho
#| fig-cap: "Figura con ancho personalizado"
#| fig-width: 10
#| fig-height: 6
#| fig-dpi: 300
#| column: page
plot(1:10)
```

## Layout de figuras

### Disposición en columnas

```markdown
::: {layout-ncol="2}
![Figura 1](fig1.png)
![Figura 2](fig2.png)
:::
```

### Disposición personalizada

```markdown
::: {layout="[[1, 1], [2]]"}
![Figura 1](fig1.png)
![Figura 2](fig2.png)
![Figura 3 ancha](fig3.png)
:::
```

## Opciones avanzadas

### Leyenda personalizada

```markdown
![Leyenda personalizada](imagen.png){#fig-custom}
```

### Posición de figura

```yaml
#| label: fig-posicion
#| fig-cap: "Figura con posición específica"
#| fig-pos: "H"  # Posición LaTeX (H = aquí)
```

### Subtítulo de figura

```markdown
::: {#fig-subtitulo}
![Título principal](imagen.png)

Subtítulo de la figura con más detalles.
:::
```

## Figuras en diferentes formatos

### Para HTML

```markdown
![Figura optimizada](imagen.png){ width=100% }
```

### Para PDF

```markdown
![Figura vectorial](imagen.pdf){ width=0.8\textwidth }
```

## Buenas prácticas

1. **Nombra siempre las figuras** para referencias cruzadas
2. **Incluye leyendas descriptivas**
3. **Usa formato consistente** de ancho
4. **Optimiza para el formato de salida**

## Véase también

- [[cross-references]] - Sistema de referencias cruzadas
- [[tables]] - Formato de tablas
- [[customizing-output]] - Opciones de formato