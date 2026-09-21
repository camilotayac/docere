---
title: "Llamadas y notas"
subtitle: "Callouts para contenido destacado"
categories:
  - "authoring"
  - "callouts"
tags:
  - "notas"
  - "advertencias"
  - "callouts"
---

Los callouts son bloques de contenido destacado para notas, advertencias y información importante.

## Tipos de callouts estándar

### Nota

```markdown
::: {.callout-note}
Esta es una nota informativa.
:::
```

### Consejo

```markdown
::: {.callout-tip}
Este es un consejo útil.
:::
```

### Advertencia

```markdown
::: {.callout-warning}
Esta es una advertencia importante.
:::
```

### Precaución

```markdown
::: {.callout-caution}
Esto requiere precaución.
:::
```

### Importante

```markdown
::: {.callout-important}
Esto es muy importante.
:::
```

## Opciones de callouts

### Título personalizado

```markdown
::: {.callout-note title="Mi Nota"}
Contenido con título personalizado.
:::
```

### Colapso

```markdown
::: {.callout-note collapse="true" title="Nota colapsable"}
Este contenido se puede expandir o contraer.
:::
```

### Icono

```markdown
::: {.callout-note icon="false"}
Sin icono en el callout.
:::
```

## Callouts con contenido avanzado

### Con Markdown interno

```markdown
::: {.callout-tip title="Consejo avanzado"}
Puedes usar **negrita**, *cursiva* y `código`.

- Listas
- También funcionan

```r
# Y bloques de código
plot(1:10)
```
:::
```

### Con referencias cruzadas

```markdown
::: {.callout-note}
Ver @fig-resultado para más detalles.
:::
```

## Callouts en diferentes formatos

### HTML

Los callouts se renderizan con iconos y colores automáticamente.

### PDF

Los callouts usan entornos LaTeX personalizados.

### EPUB

Los callouts se formatean como bloques especiales.

## Callouts personalizados

### Crear tipo personalizado

```yaml
# En _quarto.yml
callout-type:
  custom-note:
    title: "Mi Nota"
    icon: "info-circle"
    color: "blue"
```

### Uso del callout personalizado

```markdown
::: {.custom-note}
Este es mi callout personalizado.
:::
```

## Ejemplos prácticos

### Para documentación técnica

```markdown
::: {.callout-warning title="Requisitos"}
Antes de continuar, asegúrate de tener:
- R versión 4.0 o superior
- Paquetes instalados
:::
```

### Para tutoriales

```markdown
::: {.callout-tip title="Atajo"}
Usa `Ctrl+Shift+P` para abrir la paleta de comandos.
:::
```

### Para errores comunes

```markdown
::: {.callout-caution title="Error común"}
No olvides cerrar el paréntesis en la función.
:::
```

## Opciones de formato por callout

```{r}
#| label: callout-ejemplo
#| callout-note:
#|   title: "Nota con opciones"
#|   collapse: true
#|   icon: true
#| eval: false
```

## Buenas prácticas

1. **Usa el tipo apropiado** para el contexto
2. **Incluye títulos descriptivos**
3. **No exageres** con los callouts
4. **Mantén el contenido conciso**

## Véase también

- [[markdown-basics]] - Sintaxis básica de Markdown
- [[cross-references]] - Referencias cruzadas
- [[customizing-output]] - Formatos de salida