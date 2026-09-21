---
up:: [[html]]
tags:: [html]
---

# Tipos de Input HTML

## text

```html
<input type="text" placeholder="Nombre completo">
```
Texto libre de una linea. Uso: nombres, direcciones.

## email

```html
<input type="email" placeholder="correo@ejemplo.com">
```
Validacion automatica de formato email. Uso: correos electronicos.

## password

```html
<input type="password">
```
Caracteres ocultos. Uso: contrasenas.

## number

```html
<input type="number" min="0" max="100" step="1">
```
Solo valores numericos. Uso: edades, cantidades.

## checkbox

```html
<input type="checkbox" id="susc" checked>
<label for="susc">Suscribirse</label>
```
Casilla multiple. Uso: preferencias, terminos.

## radio

```html
<input type="radio" name="color" value="rojo">
<input type="radio" name="color" value="azul">
```
Seleccion unica dentro de un grupo (`name` compartido).

## submit / button

```html
<input type="submit" value="Enviar">
<button type="submit">Enviar</button>
```
Ambos envian el formulario. `<button>` permite HTML interno.

## Enlaces

- [[html-forms]]
