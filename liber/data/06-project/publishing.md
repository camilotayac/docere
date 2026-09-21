# Publicación de proyectos Quarto

Quarto facilita la publicación de libros y documentos en diversas plataformas. Esta guía cubre las opciones más comunes.

## GitHub Pages

### Configuración básica

1. **Habilita GitHub Pages** en la configuración del repositorio (Settings → Pages → Source: GitHub Actions)

2. **Crea el workflow de GitHub Actions** en `.github/workflows/publish.yml`:

```yaml
name: Publish Book
on:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: quarto-dev/quarto-actions/setup@v2
      - uses: quarto-dev/quarto-actions/render@v2
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: _output
```

3. **Publica** haciendo push a la rama `main`.

### Configuración de _output-dir

En `_quarto.yml`, define el directorio de salida:

```yaml
project:
  type: book
  output-dir: _output
```

El directorio `_output` contiene todos los archivos generados. GitHub Actions lo publica directamente.

### Archivo .nojekyll

Quarto genera automáticamente un archivo `.nojekyll` en el directorio de salida. Este archivo evita que GitHub Pages use Jekyll para procesar el sitio, lo cual es necesario porque Quarto ya genera HTML estático.

Si necesitas crearlo manualmente:

```bash
touch _output/.nojekyll
```

### Dominios personalizados

Para usar un dominio personalizado:

1. Crea un archivo `CNAME` en la raíz del repositorio:

```
tudominio.com
```

2. Configura los registros DNS de tu dominio para apuntar a GitHub Pages:

```
类型    名称    值
CNAME   www     tudominio.github.io
A       @       185.199.108.153
A       @       185.199.109.153
A       @       185.199.110.153
A       @       185.199.111.153
```

3. En GitHub, ve a Settings → Pages y escribe tu dominio personalizado.

## Netlify

### Configuración básica

1. Conecta tu repositorio a Netlify

2. Configura los comandos de construcción:

```
Build command: quarto render
Publish directory: _output
```

3. O usa un `netlify.toml` en la raíz del repositorio:

```toml
[build]
  command = "quarto render"
  publish = "_output"

[build.environment]
  QUARTO_VERSION = "1.4.554"
```

### Despliegue automático

Netlify despliega automáticamente cada push a la rama `main`. Puedes configurar ramas de previsualización para PRs.

## Otros servicios

### Vercel

Crea un `vercel.json`:

```json
{
  "buildCommand": "quarto render",
  "outputDirectory": "_output",
  "framework": null
}
```

### Cloudflare Pages

1. Conecta el repositorio
2. Build command: `quarto render`
3. Build output directory: `_output`

### Render

Crea un `render.yaml`:

```yaml
services:
  - type: web
    name: natura-docens
    runtime: static
    buildCommand: quarto render
    staticPublishPath: _output
```

## Publicación local

Para vista previa local:

```bash
quarto preview
```

Para renderizar sin servidor:

```bash
quarto render
```

Los archivos se generan en el directorio especificado en `output-dir`.

## Consideraciones

- **Ruta base**: Si el libro se publica en una subruta (ej. `tudominio.com/libro/`), configura `base-url` en `_quarto.yml`
- **Recursos**: Asegúrate de que las imágenes y recursos estén en el directorio correcto
- **Caché**: Usa `--cache` para acelerar compilaciones sucesivas
- **Incremental**: Usa `--incremental` para renderizar solo archivos modificados
