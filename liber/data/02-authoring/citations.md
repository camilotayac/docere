---
title: "Citas y bibliografía"
subtitle: "Gestión de referencias bibliográficas"
categories:
  - "authoring"
  - "citas"
tags:
  - "bibliografía"
  - "citas"
  - "notas al pie"
---

Quarto integra un sistema completo de citación bibliográfica compatible con múltiples formatos.

## Archivo de bibliografía (`.bib`)

### Formato BibTeX

```bibtex
@article{smith2024,
  author = {Smith, John and Doe, Jane},
  title = {Título del artículo},
  journal = {Revista Científica},
  year = {2024},
  volume = {10},
  pages = {100-120},
  doi = {10.1000/ejemplo}
}

@book{johnson2023,
  author = {Johnson, Robert},
  title = {Libro de Ejemplo},
  publisher = {Editorial Universitaria},
  year = {2023},
  address = {Madrid}
}
```

### Especificar en `_quarto.yml`

```yaml
bibliography: references.bib
```

Múltiples archivos:

```yaml
bibliography:
  - references.bib
  - more-refs.bib
```

## Sintaxis de citas

### Cita entre corchetes

```markdown
Según @smith2024, el método es efectivo.
```

### Cita en texto

```markdown
Smith (2024) demostró que el método es efectivo.
```

### Múltiples citas

```markdown
Varios estudios confirman esto [@smith2024; @johnson2023].
```

### Cita con página

```markdown
Ver @smith2024, p. 45.
```

### Cita en negrita

```markdown
**@smith2024** es el estudio principal.
```

## Estilos de citación

### Estilo estándar

```yaml
csl: apa.csl
```

### Estilos comunes

| Estilo | Archivo |
|--------|---------|
| APA 7ª ed. | `apa.csl` |
| MLA | `mla.csl` |
| Chicago | `chicago.csl` |
| IEEE | `ieee.csl` |
| Vancouver | `vancouver.csl` |

### Descargar estilos

Los estilos CSL se descargan de [Zotero Style Repository](https://www.zotero.org/styles).

## Configuración de bibliografía

### En `_quarto.yml`

```yaml
bibliography: references.bib
csl: apa.csl
link-citations: true
```

### Opciones de formato

```yaml
bibliography:
  title: "Referencias"
  section-title: "Bibliografía"
```

## Notas al pie

### Sintaxis básica

```markdown
Texto con nota al pie.[^1]

[^1]: Esta es la nota al pie.
```

### Nota al pie en línea

```markdown
Texto con nota.[^NOTA]

[^NOTA]: Definición de la nota.
```

### Notas al pie automáticas

```markdown
Texto con nota^[\ Esta es una nota rápida].
```

## Cita de figuras y tablas

### Cita de fuente

```markdown
![Gráfico de ventas](ventas.png){#fig-ventas}

::: {#fig-ventas}
Fuente: @smith2024
:::
```

## Referencias cruzadas con citas

Combinar referencias cruzadas con citas:

```markdown
Como se muestra en @fig-resultado y descrito por @smith2024...
```

## Gestión de referencias

### Plantilla Zotero

1. Exportar desde Zotero en formato BibTeX
2. Guardar como `references.bib`
3. Citar usando las claves de Zotero

### Plantilla Mendeley

1. Exportar选中 referencias en BibTeX
2. Unir en un solo archivo `.bib`
3. Importar en Quarto

## Notas al pie avanzadas

### Notas al pie en tablas

```markdown
| Dato | Valor |
|------|-------|
| 1    | 2^[\ Nota en tabla] |
```

### Notas al pie en figure captions

```markdown
![Descripción^[\ Nota de pie de figura]](imagen.png)
```

## Opciones de formato de bibliografía

### Para HTML

```yaml
format:
  html:
    bibliography: references.bib
    link-citations: true
    cite-style: inline
```

### Para PDF

```yaml
format:
  pdf:
    bibliography: references.bib
    cite-style: authoryear
```

## Buenas prácticas

1. **Usa claves consistentes** en el archivo `.bib`
2. **Mantén el archivo actualizado**
3. **Verifica el estilo** antes de publicar
4. **Incluye DOI cuando sea posible**

## Véase también

- [[markdown-basics]] - Sintaxis básica
- [[cross-references]] - Referencias cruzadas
- [[customizing-output]] - Formatos de salida