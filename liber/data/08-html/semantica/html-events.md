---
up:: [[html]]
tags:
  - html
---

# Eventos en HTML

Los eventos HTML permiten responder a acciones del usuario o del navegador. Cada interacción — un clic, una pulsación de tecla, un cambio de formulario — puede desencadenar una respuesta JavaScript.

## Tipos de eventos comunes

### `onclick`

Se ejecuta al hacer clic en un elemento:

```html
<button onclick="alert('Hola')">Saludar</button>
```

### `onkeydown` y `onkeyup`

Responden a pulsaciones de tecla:

```html
<input onkeydown="procesarTecla(event)" onkeyup="validarEntrada()">
```

`onkeydown` captura la tecla antes de que se procese, mientras que `onkeyup` lo hace después.

### `onmouseover` y `onmouseout`

Se activan al entrar o salir del área de un elemento con el cursor:

```html
<div onmouseover="resaltar(this)" onmouseout="restaurar(this)">
  Pasa el cursor por aquí
</div>
```

### `onfocus` y `onblur`

Gestionan el enfoque de elementos interactivos:

```html
<input onfocus="destacarCampo(this)" onblur="validarCampo(this)">
```

### `onsubmit`

Se dispara al enviar un formulario:

```html
<form onsubmit="return validarFormulario(event)">
  <input type="email" required>
  <button type="submit">Enviar</button>
</form>
```

## Eventos de formulario

Los formularios generan múltiples tipos de eventos:

- `onchange`: Se activa cuando el valor de un campo cambia y pierde el enfoque.
- `oninput`: Se dispara cada vez que el valor cambia en tiempo real.
- `onreset`: Cuando se restablece un formulario.

```html
<select onchange="cambiarTema(this.value)">
  <option value="claro">Tema claro</option>
  <option value="oscuro">Tema oscuro</option>
</select>
```

## Manejadores inline vs `addEventListener`

### Manejadores inline

```html
<button onclick="hacerAlgo()">Clic</button>
```

Son directos pero mezclan HTML con JavaScript, dificultando el mantenimiento.

### `addEventListener` (recomendado)

```javascript
const boton = document.getElementById('mi-boton');
boton.addEventListener('click', function(event) {
  console.log('Clic en:', event.target);
});
```

Ventajas de `addEventListener`:

- Separa la estructura del comportamiento.
- Permite múltiples listeners en el mismo elemento.
- Ofrece control fino sobre la fase de captura o burbujeo.
- Facilita la removal con `removeEventListener`.

## El objeto evento

Todo manejador recibe un objeto `event` con información útil:

```javascript
function manejarClic(event) {
  console.log(event.type);        // "click"
  console.log(event.target);      // Elemento que disparó el evento
  console.log(event.clientX);     // Posición X del cursor
  console.log(event.preventDefault()); // Evita acción por defecto
}
```

`event.preventDefault()` es esencial en formularios para evitar el envío por defecto y validarlo con JavaScript.

## En Natura Docens

En Natura Docens, los eventos manejan el toggle de modo oscuro y el botón TTS. El botón de tema usa `onclick` con `aria-pressed` para mantener el estado accesible, y el lector de texto se activa con `addEventListener` para controlar la síntesis de voz.

## Relación con otros elementos

Los eventos son fundamentales para el comportamiento interactivo de los [[html-forms]] y se combinan con [[html-attributes]] para crear interfaces dinámicas y accesibles.

Ver también: [[html-forms]], [[html-attributes]].
