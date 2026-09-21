---
up:: [[html]]
tags:
  - html
---

# Accesibilidad en HTML

La accesibilidad web garantiza que todas las personas, independientemente de sus capacidades, puedan percibir, navegar e interactuar con el contenido. HTML ofrece herramientas nativas y el estándar ARIA para lograrlo.

## ¿Qué es ARIA?

ARIA (Accessible Rich Internet Applications) es un conjunto de atributos que complementan la semántica HTML cuando los elementos nativos no son suficientes para describir el estado o la función de un componente.

## Roles ARIA

El atributo `role` define la función de un elemento:

```html
<div role="button" tabindex="0">Aceptar</div>
<div role="alert">Ha ocurrido un error</div>
<div role="tablist">
  <button role="tab">Pestaña 1</button>
  <button role="tab">Pestaña 2</button>
</div>
```

> [!tip] Preferir elementos nativos
> Siempre que exista un elemento HTML semántico, usarlo en lugar de ARIA. Un `<button>` real es superior a un `<div role="button">`.

## Atributos ARIA esenciales

### `aria-label`

Proporciona una etiqueta de texto accesible cuando no hay texto visible:

```html
<button aria-label="Cerrar menú">X</button>
<nav aria-label="Navegación principal">...</nav>
```

### `aria-describedby`

Asocia un elemento con una descripción más detallada:

```html
<input type="password" aria-describedby="pwd-hint">
<span id="pwd-hint">Mínimo 8 caracteres con una mayúscula.</span>
```

### `aria-hidden`

Oculta un elemento de los lectores de pantalla:

```html
<span aria-hidden="true">*</span>
```

## Navegación por teclado

### `tabindex`

Controla si un elemento es enfocable y en qué orden:

- `tabindex="0"`: Añade al orden natural de tabulación.
- `tabindex="-1"`: Enfocable programáticamente, pero no por Tab.
- `tabindex="1"` o superior: Fuerza una posición específica (evitar).

```html
<div tabindex="0" role="button">Acción</div>
```

### Saltos de navegación (skip links)

Permiten a los usuarios de teclado saltar secciones repetitivas:

```html
<a href="#contenido" class="skip-link">Saltar al contenido principal</a>
<!-- ...header y nav... -->
<main id="contenido">
  <!-- contenido principal -->
</main>
```

## Contraste de color

WCAG 2.1 requiere una proporción de contraste mínima:

- **Texto normal**: 4.5:1 (nivel AA).
- **Texto grande** (18px+ o 14px+ negrita): 3:1.
- **Elementos gráficos**: 3:1 contra el fondo.

## Consideraciones para lectores de pantalla

- Usar HTML semántico como base (ver [[html-semantic]]).
- Incluir `alt` en todas las imágenes significativas.
- Estructurar encabezados en orden jerárquico (h1 > h2 > h3).
- Etiquetar formularios correctamente con `<label>`.

## En Natura Docens

En Natura Docens, usamos ARIA para el TTS y los toggles de accesibilidad. Los atributos `aria-pressed` controlan el estado de los botones de modo oscuro y lectura, mientras que `aria-live` anuncia los cambios de contenido a los lectores de pantalla.

## Relación con otros elementos

La accesibilidad se apoya en [[html-semantic]] para la estructura del documento y utiliza [[html-attributes]] para los atributos ARIA y de comportamiento.

Ver también: [[html-semantic]], [[html-attributes]].
