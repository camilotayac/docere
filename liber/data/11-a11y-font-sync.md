# Sincronización de variables CSS y JavaScript para redimensionamiento de fuentes accesible

Para lograr un diseño accesible (cumpliendo con WCAG 1.4.4, que exige que el texto pueda ser escalado hasta un 200% sin pérdida de legibilidad ni funcionalidad) y un código limpio, la industria del desarrollo web sigue un modelo declarativo donde el CSS es la fuente de verdad y el JS actúa como controlador.

## Mejores Prácticas

1. **Uso exclusivo de unidades relativas (`rem`)**: 
   - Se debe abandonar por completo el uso de `px` para los tamaños de fuente. Usar `px` sobrescribe la preferencia de tamaño que el usuario haya definido a nivel sistema en su navegador.
   - Definir los tamaños de jerarquía (`h1`, `h2`, `h3`, `body`) en base a proporciones (escalas modulares) sobre el `rem`.

2. **JavaScript como puente (Helper), no como dictador**:
   - Una mala práctica es iterar por el DOM usando JS para inyectar estilos en línea como `element.style.fontSize = "20px"`. Esto causa severos problemas de rendimiento y rompe cascadas (CSS Specificity).
   - **La forma óptima:** JS solo debe manipular una (1) variable CSS (ej. `--body-font-size`) a nivel del `:root` (`document.documentElement`). El CSS distribuirá este cambio por todo el árbol del DOM automáticamente.

3. **Flujo de Resiliencia en el Load**:
   - Al cargar la página, JS debe leer el tamaño de `localStorage` y aplicarlo inmediatamente a la variable `--body-font-size` del `:root`.
   - Si no hay un tamaño guardado, JS no debe hacer nada, dejando que el CSS maneje el valor por defecto nativamente.

## Implementación Estándar

### CSS (El modelo)
```css
:root {
  /* Este es el único punto de anclaje para JS */
  --base-font-size: 1rem; /* Equivalente a 16px por defecto */
}

body {
  font-size: var(--base-font-size);
}

h1 {
  /* Escala relativa: el doble del body */
  font-size: calc(var(--base-font-size) * 2);
}
```

### JavaScript (El controlador)
```javascript
const STORAGE_KEY = 'a11y-fontsize';
const BASE_SIZE = 1.0;

function applySize(remValue) {
    // Solo tocamos el :root, CSS se encarga del resto
    document.documentElement.style.setProperty('--base-font-size', remValue + 'rem');
    localStorage.setItem(STORAGE_KEY, remValue);
}

// En el Load:
const saved = localStorage.getItem(STORAGE_KEY);
if (saved) {
    applySize(parseFloat(saved));
}
```

## Beneficios
- **Performance:** Al cambiar una sola variable CSS, el navegador recalcula el layout eficientemente. Evitamos iterar nodos `querySelectorAll('h1, h2, ...')`.
- **Mantenibilidad (Clean Code):** Toda la lógica tipográfica vive en SCSS/CSS. El JS queda liberado de reglas visuales (`HEADING_SCALES`).
- **Resiliencia (FOUC):** Al cargar la página, el navegador tiene el tamaño nativo por defecto en CSS sin depender de cálculos asíncronos.

## Aislamiento de Capas (UI vs. Contenido)
Un error común es atar **toda la interfaz** (menús, sidebars, toolbars) a la misma variable que controla el zoom del usuario (`--a11y-base-size`). Cuando el usuario hace zoom para leer mejor, rompe la navegación.
**Solución:** Se deben mantener dos escalas distintas:
1. `--theme-base-size`: Fija el tamaño base estático del entorno (ej. `1.25rem` o 20px). Las sidebars y menús consumen esta variable para mantenerse estables.
2. `--a11y-base-size`: Controlada por JS, permite zoom dinámico. Solo la consume el bloque principal de contenido (`#quarto-document-content` y los Headings `$h1-$h6`).

Límites Accesibles: WCAG recomienda permitir hasta un 200% o escalas holgadas (ej. máximo `40px` o `2.5rem`).
