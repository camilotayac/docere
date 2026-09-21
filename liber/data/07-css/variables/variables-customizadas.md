---
tags:
  - css
  - variables
  - custom-properties
  - quarto
  - scss
aliases:
  - CSS Custom Properties
  - var()
  - Propiedades CSS personalizadas
created: 2025-01-01
---

# Variables CSS personalizadas

Las variables CSS (también llamadas *custom properties*) permiten definir valores reutilizables en hojas de estilo. A diferencia de las [[scss-variables]], las variables CSS existen en tiempo de ejecución y pueden modificarse dinámicamente.

## Definición con `--variable-name`

Las variables se definen con el prefijo `--`:

```css
:root {
  --color-primario: #3498db;
  --color-texto: #2c3e50;
  --espaciado-base: 1rem;
  --fuente-principal: 'Inter', sans-serif;
}
```

## Uso con `var()`

La función `var()` lee el valor de una variable:

```css
.enlace {
  color: var(--color-primario);
  font-family: var(--fuente-principal);
  padding: var(--espaciado-base);
}
```

## Valores por defecto

Se puede proporcionar un valor de respaldo como segundo argumento:

```css
.elemento {
  color: var(--color-secundario, #e74c3c);
  /* Si --color-secundario no está definido, usa #e74c3c */
}
```

Se pueden encadenar múltiples fallbacks:

```css
.elemento {
  background: var(--bg-personalizado, var(--color-base, #fff));
}
```

## Escoping: global vs local

### Global (`:root`)

Las variables en `:root` están disponibles en todo el documento:

```css
:root {
  --color-primario: #3498db;
}
```

### Local (bloque o clase)

Las variables pueden limitarse a un contexto:

```css
.seccion-oscuro {
  --color-texto: #ecf0f1;
  --color-fondo: #2c3e50;
  color: var(--color-texto);
  background-color: var(--color-fondo);
}

.seccion-claro {
  --color-texto: #2c3e50;
  --color-fondo: #ecf0f1;
  color: var(--color-texto);
  background-color: var(--color-fondo);
}
```

### Herencia

Las variables CSS se heredan. Un elemento hijo puede usar la variable definida en su padre, o redefinirla localmente:

```css
:root {
  --color-primario: blue;
}

.padre {
  --color-primario: green;
}

.hijo {
  /* hereda --color-primario: green del padre */
  color: var(--color-primario);
}
```

## Interacción con JavaScript

Las variables CSS se pueden leer y modificar en tiempo de ejecución:

```javascript
// Leer una variable
const color = getComputedStyle(document.documentElement)
  .getPropertyValue('--color-primario');

// Establecer una variable
document.documentElement.style.setProperty('--color-primario', '#e74c3c');
```

### Ejemplo: cambio de tema dinámico

```css
:root {
  --bg-color: #ffffff;
  --text-color: #2c3e50;
  --transition-speed: 0.3s;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: background-color var(--transition-speed), color var(--transition-speed);
}
```

```javascript
function toggleDarkMode() {
  const root = document.documentElement;
  const isDark = root.classList.toggle('dark');
  
  if (isDark) {
    root.style.setProperty('--bg-color', '#1a1a2e');
    root.style.setProperty('--text-color', '#ecf0f1');
  } else {
    root.style.setProperty('--bg-color', '#ffffff');
    root.style.setProperty('--text-color', '#2c3e50');
  }
}
```

## Variables CSS en Quarto

> **Sección crítica**: Las variables CSS son el puente entre el sistema de [[scss-variables]] de Quarto y el CSS que llega al navegador.

### CSS Custom Properties vs SCSS Variables

| Característica | Variables CSS (`--var`) | SCSS Variables (`$var`) |
|---|---|---|
| Momento de evaluación | Tiempo de ejecución (navegador) | Tiempo de compilación (SCSS → CSS) |
| Modificables en JS | Sí | No |
| Soporte de herencia | Sí, natural por cascada | No (compilan a valores estáticos) |
| Alcance | Global (`:root`) o local por bloque | Global por defecto, local con `{}` |
| Uso en Quarto | En `style.css` y en `:root` | En archivos `_quarto.yml` y `.scss` |

### Cómo Quarto compila SCSS a CSS

Quarto usa un sistema de compilación SCSS para generar CSS:

1. **Archivo SCSS del tema**: `theme.scss` (o `custom.scss`) contiene variables SCSS (`$variable`) y mixins
2. **Compilación**: Quarto compila el SCSS a CSS estándar, resolviendo todas las variables SCSS
3. **Resultado**: El CSS generado contiene valores estáticos (colores hex, tamaños, etc.)
4. **Custom properties en `:root`**: Quarto inyecta las variables CSS al inicio del CSS generado

```scss
// theme.scss — Esto es SCSS
$primary: #3498db;
$font-size-base: 1rem;

// Compila a CSS:
// :root {
//   --color-primary: #3498db;
//   --font-size-base: 1rem;
// }
```

### La sección `:root` en Quarto

En los temas de Quarto, la sección `:root` es donde se definen las variables CSS que el navegador usa:

```css
:root {
  /* Colores del tema */
  --color-primary: #3498db;
  --color-secondary: #2ecc71;
  --color-background: #ffffff;
  --color-text: #2c3e50;
  
  /* Tipografía */
  --font-family-sans: 'Inter', sans-serif;
  --font-family-mono: 'Fira Code', monospace;
  --font-size-base: 1rem;
  
  /* Espaciado */
  --spacing-unit: 1rem;
  --border-radius: 0.5rem;
  
  /* Animaciones */
  --transition-speed: 0.3s;
}
```

Cuando un usuario personaliza un tema en Quarto, sobreescribe estas variables en su propio SCSS:

```scss
// _extensions/mi-tema/_quarto.scss
$primary: #8e44ad;  // cambia el color primario

// Quarto genera:
// :root { --color-primary: #8e44ad; }
```

### Cómo `body.theme-colorblind` sobreescribe custom properties

Quarto soporta modos de accesibilidad que sobreescriben variables CSS en el `<body>`:

```css
/* Valores por defecto en :root */
:root {
  --color-primary: #3498db;
  --color-secondary: #2ecc71;
  --color-danger: #e74c3c;
  --color-success: #27ae60;
}

/* Modo daltónico: colores ajustados para daltonismo */
body.theme-colorblind {
  --color-primary: #0077bb;
  --color-secondary: #009988;
  --color-danger: #cc3311;
  --color-success: #009988;
}

/* Modo alto contraste */
body.theme-high-contrast {
  --color-primary: #0000ff;
  --color-text: #000000;
  --color-background: #ffffff;
}
```

El mecanismo funciona por **cascada CSS**:

1. `:root` define los valores por defecto
2. `body.theme-colorblind` redefine las mismas variables a nivel de `<body>`
3. Todos los elementos hijos heredan los nuevos valores
4. No se necesita redefinir cada propiedad individualmente — `var()` automáticamente usa el valor más cercano en la cascada

Esto es más eficiente que alternativas como crear reglas completas para cada modo:

```css
/* ❌ Ineficiente — hay que redefinir cada propiedad */
body.theme-colorblind .boton-primario {
  background-color: #0077bb;
}
body.theme-colorblind .enlace {
  color: #0077bb;
}

/* ✅ Eficiente — se cambia una variable y todo se actualiza */
body.theme-colorblind {
  --color-primary: #0077bb;
}
.boton-primario { background-color: var(--color-primary); }
.enlace { color: var(--color-primary); }
```

### Ejemplo completo: tema Quarto con variables CSS

```scss
// mi-tema.scss
$primary: #2563eb;

@mixin theme-variables {
  :root {
    --color-primary: #{$primary};
    --color-primary-light: #{ lighten($primary, 15%) };
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  body.theme-colorblind {
    --color-primary: #0077bb;
    --color-primary-light: #33aadd;
  }
}

@include theme-variables;
```

## Conexión con Quarto

- [[scss-variables]]: Las variables SCSS (`$var`) se compilan a CSS. Las custom properties (`--var`) son el resultado final que el navegador ejecuta. SCSS es la entrada, CSS custom properties son la salida.
- [[html-theming]]: El sistema de temas de Quarto depende de variables CSS para colores, tipografía, espaciado, y modos de accesibilidad. Sobreescribir `:root` o `body.theme-*` es la forma principal de personalizar la apariencia.
- [[transiciones]] y [[animaciones-css]]: Las variables CSS se usan para parametrizar duraciones y otros valores en animaciones, permitiendo cambiar el ritmo de animaciones desde un solo lugar.
