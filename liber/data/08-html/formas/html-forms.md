---
up:: [[html]]
tags:: [html]
---

# Formularios HTML

## Estructura basica

```html
<form action="/enviar" method="post">
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre" required>
  <button type="submit">Enviar</button>
</form>
```

## Elementos principales

- `<form>` — contenedor del formulario. Atributos `action` (URL destino) y `method` (GET o POST).
- `<input>` — campo de entrada. El atributo `type` define el comportamiento.
- `<textarea>` — area de texto multilinea.
- `<select>` / `<option>` — menu desplegable.
- `<button>` — boton dentro del formulario.
- `<label>` — etiqueta asociada a un control. Mejora accesibilidad.
- `<fieldset>` / `<legend>` — agrupacion visual de campos.

## Tipos de input

- `text` — texto libre
- `email` — correo electronico (validacion nativa)
- `password` — texto oculto
- `number` — valores numericos
- `checkbox` — casilla multiple
- `radio` — seleccion unica
- `submit` — boton de envio

## Validacion nativa

- `required` — campo obligatorio
- `pattern` — expresion regular de validacion
- `minlength` / `maxlength` — longitud minima y maxima
- `min` / `max` — rango numerico

## GET vs POST

| Metodo | Uso |
|--------|-----|
| GET | Datos visibles en URL, para busquedas |
| POST | Datos en el cuerpo, para envio seguro |

## Enlaces

- [[html-attributes]]
- [[html-events]]
