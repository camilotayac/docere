# Salida EPUB en Quarto

Quarto puede generar archivos EPUB, el formato estándar para libros electrónicos. EPUB es compatible con la mayoría de lectores digitales excepto Kindle (que usa formato proprietary).

## Opciones de salida EPUB

```yaml
format:
  epub:
    css: epub-style.css
    toc: true
    toc-depth: 3
    number-sections: true
    cover-image: cover.jpg
    fig-width: 8
    fig-height: 5
```

## CSS personalizado para EPUB

El CSS para EPUB tiene limitaciones diferente al CSS web. No soporta JavaScript, animaciones ni layouts complejos.

```css
/* epub-style.css */

body {
  font-family: Georgia, serif;
  line-height: 1.6;
  color: #333;
  margin: 1em;
}

h1 {
  font-size: 1.8em;
  margin-top: 2em;
  page-break-before: always;
}

h2 {
  font-size: 1.4em;
  margin-top: 1.5em;
}

p {
  text-align: justify;
  margin-bottom: 0.8em;
}

img {
  max-width: 100%;
  height: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
}

th, td {
  border: 1px solid #ccc;
  padding: 0.5em;
  text-align: left;
}

th {
  background-color: #f5f5f5;
}
```

### Consideraciones de CSS para EPUB

- **Evita `position: fixed`** — No funciona en todos los lectores
- **Evita `flexbox` y `grid`** — Soporte limitado
- **Usa `page-break-before`** — Para controlar saltos de página
- **Imágenes relativas** — Usa `max-width: 100%` para imágenes responsivas

## Matemáticas en EPUB

Quarto procesa ecuaciones matemáticas en EPUB usando MathJax o KaTeX. Sin embargo, algunos lectores EPUB no soportan matemáticas bien.

Para habilitar matemáticas:

```yaml
format:
  epub:
    math-method: mathjax
```

Opciones disponibles:

| Método | Descripción |
|--------|-------------|
| `mathjax` | Renderiza como HTML/CSS (recomendado) |
| `katex` | Alternativa más ligera |
| `webtex` | Convierte a imágenes SVG |
| `plain` | No procesa matemáticas |

**Recomendación**: Usa `mathjax` para la mejor compatibilidad.

## Metadatos EPUB

Los metadatos se configuran en `_quarto.yml`:

```yaml
book:
  title: "Natura Docens"
  subtitle: "Libro de conocimiento"
  author: "Autor Principal"
  date: today
  lang: es
  publisher: "Editorial"
  description: "Una descripción del libro"
  subject: "Ciencia, Educación"
  rights: "© 2024 Autores"
  cover-image: cover.jpg
  cover-image-alt: "Portada de Natura Docens"
```

### Metadatos Dublin Core

Quarto genera automáticamente metadatos Dublin Core en el EPUB:

| Campo | YAML | Descripción |
|-------|------|-------------|
| `dc:title` | `title` | Título del libro |
| `dc:creator` | `author` | Autor principal |
| `dc:language` | `lang` | Idioma (ISO 639-1) |
| `dc:publisher` | `publisher` | Editorial |
| `dc:date` | `date` | Fecha de publicación |
| `dc:description` | `description` | Descripción |
| `dc:subject` | `subject` | Tema/categoría |
| `dc:rights` | `rights` | Derechos de autor |
| `dc:identifier` | Generado automáticamente | Identificador único |

### Archivo OPF generado

Quarto genera un archivo `.opf` (Open Packaging Format) que contiene:

```xml
<metadata>
  <dc:title>Natura Docens</dc:title>
  <dc:creator>Autor Principal</dc:creator>
  <dc:language>es</dc:language>
  <dc:publisher>Editorial</dc:publisher>
  <dc:date>2024-01-15</dc:date>
  <dc:identifier id="BookId">urn:uuid:...</dc:identifier>
</metadata>
```

## Compatibilidad con lectores EPUB

### Lectores compatibles

| Lector | Compatibilidad | Notas |
|--------|----------------|-------|
| Apple Books | ✅ Excelente | Soporte completo de EPUB 3 |
| Google Play Books | ✅ Bueno | Soporte completo |
| Kobo | ✅ Bueno | Soporte completo |
| Calibre | ✅ Excelente | Mejor para pruebas |
| Adobe Digital Editions | ✅ Bueno | Soporte completo |
| Nook | ⚠️ Parcial | Soporte limitado de CSS |
| Kindle | ❌ No compatible | Usa formato proprietary |

### Kindle

Para Kindle, necesitas convertir EPUB a formato KF8/MOBI usando herramientas como:

- [Kindle Comic Creator](https://www.amazon.com/b?nodeId=24429665011)
- Calibre con plugin KFX
- Amazon Kindle Previewer

## Estructura de un archivo EPUB

Un archivo EPUB es esencialmente un archivo ZIP con esta estructura:

```
libro.epub/
├── mimetype
├── META-INF/
│   └── container.xml
└── OEBPS/
    ├── content.opf
    ├── toc.ncx
    ├── toc.xhtml
    ├── chapter1.xhtml
    ├── chapter2.xhtml
    ├── styles/
    │   └── style.css
    └── images/
        └── cover.jpg
```

## Configuración completa de ejemplo

```yaml
book:
  title: "Natura Docens"
  author: "Autores"
  date: today
  lang: es
  publisher: "Editorial"
  cover-image: cover.jpg
  cover-image-alt: "Portada del libro"

format:
  epub:
    css: epub-style.css
    toc: true
    toc-depth: 3
    number-sections: true
    math-method: mathjax
    fig-width: 8
    fig-height: 5
    fig-dpi: 150
```

## Errores comunes

1. **Imágenes muy grandes** — Redimensiona las imágenes antes de incluirlas
2. **CSS web en EPUB** — Evita propiedades CSS que no son soportadas
3. **Matemáticas no renderizadas** — Verifica que `math-method` esté configurado
4. **Portada no aparece** — Asegúrate de que `cover-image` apunta a un archivo válido
5. **Encoding incorrecto** — Asegúrate de que `lang` esté en formato ISO 639-1 (`es`, no `spanish`)
