---
up:: [[html]]
tags:: [html]
---

# Enlaces en HTML

El elemento `<a>` crea hipervínculos entre documentos o recursos. El atributo
`href` especifica el destino y el contenido visible es el texto del enlace.

## URLs absolutas y relativas

Las absolutas incluyen el dominio. Las relativas se resuelven respecto a la
ubicación del documento actual.

```html
<a href="https://example.com">Externo</a>
<a href="capitulo-2.html">Siguiente capítulo</a>
<a href="../imagenes/diagrama.png">Diagrama</a>
```

En Quarto, los enlaces internos usan rutas relativas: `[texto](capitulo.qmd)`.

## Objetivos y descarga

`target="_blank"` abre en nueva pestaña. Se recomienda `rel="noopener noreferrer"`.

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Nueva pestaña</a>
<a href="datos.csv" download="datos-exportados.csv">Descargar datos</a>
```

## Correo y teléfono

```html
<a href="mailto:correo@ejemplo.com?subject=Consulta">Enviar correo</a>
<a href="tel:+34600123456">Llamar</a>
```

## Enlaces de ancla

Permiten saltar a secciones de la misma página usando el `id` del destino:

```html
<a href="#conclusiones">Ir a conclusiones</a>
<h2 id="conclusiones">Conclusiones</h2>
```

Ver también: [[html-attributes]]
