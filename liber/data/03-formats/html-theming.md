---
title: "Temas HTML en Quarto"
description: "Cómo funcionan los temas HTML en Quarto: Bootstrap 5, SCSS, Bootswatch y modo oscuro"
---

## Cómo funcionan los temas HTML

Quarto genera HTML output usando **Bootstrap 5** como base. El sistema de temas se controla con la opción YAML `theme:`, **no** con `css:`.

La opción `theme:` acepta:

- Un tema built-in (ej. `flatly`)
- Un archivo SCSS personalizado
- Una lista combinada: `[tema-base, archivo.scss]`
- Modo claro/oscuro con la sintaxis `light:` / `dark:`

## Temas built-in (Bootswatch)

Quarto incluye todos los temas de Bootswatch para Bootstrap 5:

```
flatly, cosmo, lumen, paper, sandstone, simplex, united, cerulean, 
darkly, journal, readable, sketchy, spacelab, superhero, vapor, 
yeti, morph, quartz, solar, zephyr
```

Ejemplo mínimo:

```yaml
---
title: "Mi documento"
theme: flatly
---
```

## Temas SCSS personalizados

Para personalizar sobre un tema base, se pasa como array:

```yaml
theme:
  - flatly
  - custom.scss
```

El archivo SCSS se carga después del tema base, así que las variables que definas **sobreescriben** los valores por defecto de Bootstrap/Bootswatch.

## Modo oscuro

Quarto soporta modo claro y oscuro con la sintaxis `light:` / `dark:`:

```yaml
theme:
  light:
    - flatly
    - _styles/custom.scss
  dark:
    - flatly
    - _styles/custom-dark.scss
```

### `respect-user-color-scheme`

Para que Quarto respete la preferencia del sistema operativo del usuario (claro/oscuro):

```yaml
format:
  html:
    theme:
      light:
        - flatly
        - _styles/custom.scss
      dark:
        - flatly
        - _styles/custom-dark.scss
    respect-user-color-scheme: true
```

Cuando `respect-user-color-scheme: true`, Quarto usa `prefers-color-scheme` del navegador para elegir automáticamente el tema claro o oscuro. Sin esto, el usuario debe cambiar manualmente con el interruptor del navbar.

## Estructura de un archivo SCSS

Un archivo SCSS para Quarto tiene dos secciones delimitadas por comentarios especiales:

```scss
/*-- scss:defaults --*/

// Aquí van las variables de Bootstrap/Quarto que sobreescribes
$body-bg: #ffffff;
$body-color: #333333;
$link-color: #2c7be5;
$font-family-sans-serif: "Inter", sans-serif;

/*-- scss:rules --*/

// Aquí van reglas CSS/SCSS adicionales
.sidebar-title {
  text-transform: uppercase;
}
```

### Secciones

| Sección | Propósito |
|---------|-----------|
| `/*-- scss:defaults --*/` | Variables SCSS que sobreescriben valores de Bootstrap |
| `/*-- scss:rules --*/` | Reglas CSS/SCSS adicionales que se añaden al final |

### Cómo funcionan las variables

Las variables SCSS en la sección `defaults` sobreescriben los valores por defecto de Bootstrap. Por ejemplo:

```scss
/*-- scss:defaults --*/

// Cambia el color de fondo del body
$body-bg: #f8f9fa;

// Cambia la fuente principal
$font-family-sans-serif: "Source Sans Pro", sans-serif;

// Cambia el tamaño de los títulos
$h1-font-size: 2.5rem;
$h2-font-size: 2rem;
```

Esto funciona porque Quarto compila el SCSS en este orden: primero Bootstrap/Bootswatch, luego tus overrides.

## Problema común: `css:` en vez de `theme:`

**El error más frecuente** es usar la opción `css:` para intentar tematizar el documento:

```yaml
# ❌ INCORRECTO — esto NO aplica el tema
format:
  html:
    css: _styles/headings.css
```

```yaml
# ✅ CORRECTO — esto SÍ aplica el tema
format:
  html:
    theme:
      - flatly
      - _styles/custom.scss
```

### ¿Por qué `css:` no funciona para temas?

La opción `css:` simplemente añade un archivo CSS como `<link>` en el `<head>` del HTML. Esto **no** interactúa con el sistema de temas de Quarto ni con Bootstrap.

En cambio, `theme:` alimenta el pipeline de compilación SCSS de Quarto, que:

1. Carga Bootstrap 5 como base
2. Aplica el tema Bootswatch (si se especifica)
3. Aplica tus overrides SCSS
4. Genera el CSS final

Por lo tanto, `css: _styles/headings.css` solo añade un link al CSS — no sobreescribe variables de Bootstrap ni activa el sistema de temas.

### Regla práctica

- Si necesitas **sobreescribir variables de Bootstrap** o que Quarto genere el CSS → usa `theme:` con archivos `.scss`
- Si solo necesitas **añadir reglas CSS adicionales** que no dependen de Bootstrap → puedes usar `css:` (pero `theme:` con sección `rules` es más limpio)

## En Natura Docens

La configuración actual del proyecto usa este esquema de temas:

```yaml
format:
  html:
    theme:
      light:
        - flatly
        - _styles/natura-docens.scss
      dark:
        - flatly
        - _styles/natura-docens-dark.scss
    respect-user-color-scheme: true
```

Esto significa:

- **Tema base**: Flatly (de Bootswatch) para ambos modos
- **Override claro**: `_styles/natura-docens.scss` personaliza variables para el modo claro
- **Override oscuro**: `_styles/natura-docens-dark.scss` personaliza variables para el modo oscuro
- **Respeto del sistema**: Quarto detecta si el usuario tiene modo oscuro activo en su SO y aplica el tema correspondiente
