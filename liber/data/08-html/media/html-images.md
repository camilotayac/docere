---
up:: [[html]]
tags:
  - html
---

# Imágenes en HTML

Las imágenes son uno de los elementos multimedia más utilizados en la web. HTML proporciona varias formas de incluir y controlar imágenes de manera semántica y eficiente.

## Etiqueta `<img>`

La etiqueta `<img>` es un elemento **vacío** (sin cierre) que inserta una imagen en el documento.

```html
<img src="foto.jpg" alt="Descripción de la imagen">
```

El atributo `alt` es **obligatorio** y describe el contenido de la imagen para lectores de pantalla y cuando la imagen no se puede cargar.

## Atributos de tamaño

Se pueden definir dimensiones explícitas para evitar saltos de diseño durante la carga:

```html
<img src="diagrama.png" alt="Diagrama de flujo" width="600" height="400">
```

Definir `width` y `height` permite al navegador reservar el espacio correcto antes de cargar la imagen.

## Carga diferida

El atributo `loading="lazy"` retrasa la carga de imágenes que no están visibles en el viewport:

```html
<img src="imagen-grande.jpg" alt="Paisaje" loading="lazy">
```

Esto mejora significativamente el rendimiento en páginas con muchas imágenes.

## Imágenes responsivas con `<picture>`

La etiqueta `<picture>` permite servir diferentes版本 de una imagen según el dispositivo:

```html
<picture>
  <source srcset="foto.avif" type="image/avif">
  <source srcset="foto.webp" type="image/webp">
  <img src="foto.jpg" alt="Foto responsiva">
</picture>
```

El navegador selecciona el formato más optimizado que soporte. AVIF y WebP ofrecen mejor compresión que JPEG o PNG.

## Formatos modernos

- **WebP**: Compresión superior a JPEG con soporte amplio en navegadores actuales.
- **AVIF**: Compresión aún mejor, ideal para fotografías de alta calidad.
- **SVG**: Formato vectorial para iconos y gráficos escalables.

## En Quarto

Quarto simplifica la inserción de imágenes con sintaxis markdown extendida:

```markdown
![alt](imagen.png){width=50%}
```

Esto genera una etiqueta `<img>` con el atributo `width` calculado como porcentaje del contenedor.

## Buenas prácticas

- Siempre incluir `alt` descriptivo y conciso.
- Especificar `width` y `height` para evitar layout shift.
- Usar `loading="lazy"` en imágenes fuera del viewport inicial.
- Preferir WebP o AVIF cuando sea posible.
- Utilizar `<picture>` para compatibilidad multi-formato.

## Relación con otros elementos

Las imágenes se combinan frecuentemente con [[html-elements]] para crear layouts complejos y con atributos HTML para control fino del comportamiento.

Ver también: [[html-elements]] para la referencia completa de etiquetas HTML.
