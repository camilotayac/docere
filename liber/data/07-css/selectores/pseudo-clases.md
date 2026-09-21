# Pseudo-clases de CSS

Una pseudo-clase es una palabra clave agregada a un selector que define un estado especial del elemento seleccionado. Se escriben con dos puntos `:` seguidos del nombre de la pseudo-clase.

## Pseudo-clases de interacción

Estas pseudo-clases responden a las acciones del usuario.

### `:hover`

Se aplica cuando el cursor del ratón está sobre un elemento.

```css
boton:hover {
  background-color: #0056b3;
  cursor: pointer;
}

enlace:hover {
  text-decoration: underline;
}
```

### `:active`

Se aplica cuando el elemento está siendo activado (clic mantenido).

```css
boton:active {
  background-color: #003d80;
  transform: scale(0.98);
}
```

### `:focus`

Se aplica cuando el elemento tiene el foco del teclado (usualmente inputs y botones).

```css
input:focus {
  outline: 2px solid #007acc;
  border-color: #007acc;
}

textarea:focus {
  box-shadow: 0 0 0 3px rgba(0, 122, 204, 0.25);
}
```

> [!tip] Accesibilidad
> Nunca elimines el `outline` sin proporcionar una alternativa visual de foco. Es esencial para la navegación por teclado.

### `:focus-within`

Se aplica al elemento padre cuando cualquier descendiente tiene foco.

```css
.form-group:focus-within {
  border-color: #007acc;
  box-shadow: 0 0 0 2px rgba(0, 122, 204, 0.3);
}
```

## Pseudo-clases estructurales

Estas pseudo-clases seleccionan elementos según su posición en el DOM.

### `:first-child` y `:last-child`

```css
li:first-child {
  font-weight: bold;
}

li:last-child {
  border-bottom: none;
}

section:first-child {
  margin-top: 0;
}
```

### `:nth-child()`

Selecciona elementos según su posición usando una fórmula An+B.

```css
/* Filas pares con fondo alternado */
tr:nth-child(even) {
  background-color: #f2f2f2;
}

/* Filas impares */
tr:nth-child(odd) {
  background-color: #ffffff;
}

/* Cada tercer elemento */
li:nth-child(3n) {
  color: #e74c3c;
}

/* El segundo elemento */
li:nth-child(2) {
  list-style-type: lower-roman;
}
```

### `:nth-of-type()`

Similar a `:nth-child()` pero considera solo elementos del mismo tipo.

```css
p:nth-of-type(2) {
  font-size: 1.2em;
}

div:nth-of-type(odd) {
  background-color: #fafafa;
}
```

## Pseudo-clases funcionales

### `:not()`

Excluye elementos que coincidan con el selector dado.

```css
/* Todos los párrafos excepto los que tienen la clase especial */
p:not(.especial) {
  color: #333;
}

/* Todos los botones excepto el deshabilitado */
button:not(:disabled) {
  opacity: 1;
}

/* Selectores compuestos (CSS4) */
p:not(.titulo, .subtitulo) {
  font-size: 16px;
}
```

### `:is()`

Agrupa selectores con la menor especificidad posible del selector más específico dentro de él.

```css
/* En lugar de escribir múltiples reglas */
:is(header, footer, main) a {
  color: #007acc;
}

/* Equivale a */
header a, footer a, main a {
  color: #007acc;
}
```

### `:where()`

Similar a `:is()` pero siempre tiene especificidad cero, lo que facilita la sobreescritura.

```css
:where(h1, h2, h3) {
  margin-bottom: 0.5em;
  font-weight: 600;
}
```

> [!note] Especificidad
> `:where()` siempre tiene especificidad `0,0,0`, mientras que `:is()` hereda la especificidad del selector más alto dentro de sus argumentos.

## Pseudo-clases de estado

### `:target`

Se aplica al elemento cuyo `id` coincide con la fragmento de la URL.

```css
:target {
  background-color: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 1em;
}
```

Útil para implementar navegación por secciones en [[html-theming]].

### `:checked`

Se aplica a checkboxes y radios cuando están seleccionados.

```css
input:checked + label {
  font-weight: bold;
  color: #007acc;
}

input[type="checkbox"]:checked::before {
  content: "✓";
}
```

### `:disabled`

Se aplica a elementos deshabilitados.

```css
input:disabled {
  background-color: #e9ecef;
  cursor: not-allowed;
  opacity: 0.7;
}

button:disabled {
  border-color: #dee2e6;
  color: #6c757d;
}
```

### `:enabled`

El estado opuesto a `:disabled`.

```css
input:enabled {
  border: 1px solid #ced4da;
}
```

## Conexión con Quarto

En [[html-theming]], las pseudo-clases son especialmente útiles para:

- Interactividad en componentes de UI generados por [[quarto-shortcodes]]
- Estilos de navegación en sitios web de Quarto
- Feedback visual en formularios de [[filters]]
- Comportamiento hover en [[quarto-callouts]]

```css
/* Hover en callouts de Quarto */
.callout-note:hover {
  border-left-color: #0c5460;
}

/* Foco en search box del tema */
.search-input:focus {
  border-color: var(--quarto-primary-color);
}
```

## Ver también

- [[pseudo-elementos]]
- [[selectores-basicos]]
- [[especificidad]]
- [[variables-css]]
