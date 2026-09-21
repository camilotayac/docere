---
title: Instalación de Quarto
description: Guía completa para instalar Quarto en cualquier sistema operativo
---

# Instalación de Quarto

Quarto es un sistema de publicación científica y técnica de próxima generación. Se ejecuta sobre Pandoc y está disponible como una herramienta de línea de comandos independiente.

## Descarga e instalación

### macOS

1. Descarga el instalador `.pkg` desde [quarto.org/docs/get-started](https://quarto.org/docs/get-started)
2. Ejecuta el instalador y sigue las instrucciones
3. Quarto se instala en `/usr/local/bin/quarto`

```bash
# Alternativa con Homebrew
brew install --cask quarto
```

### Windows

1. Descarga el instalador `.msi` desde la página oficial
2. Ejecuta el instalador y completa la configuración
3. Quarto se añade al PATH automáticamente

### Linux

Descarga el `.deb` (Debian/Ubuntu), `.rpm` (Fedora/RHEL) o extrae el tarball manualmente:

```bash
# Debian / Ubuntu
sudo dpkg -i quarto-<version>-linux-amd64.deb

# Fedora / RHEL
sudo rpm -i quarto-<version>-linux-amd64.rpm

# Tarball genérico
tar -xzf quarto-<version>-linux-amd64.tar.gz
export PATH=$PATH:$(pwd)/quarto-<version>/bin
```

## Comandos CLI esenciales

| Comando | Descripción |
|---|---|
| `quarto --version` | Muestra la versión instalada |
| `quarto render` | Renderiza documentos a formato de salida |
| `quarto preview` | Abre una vista previa en vivo con recarga automática |
| `quarto inspect` | Muestra información detallada de un documento |
| `quarto install` | Instala extensiones y temas |
| `quarto new` | Crea un proyecto o documento nuevo |

### Renderizar un documento

```bash
quarto render documento.qmd
```

Renderiza el documento a todos los formatos definidos en el YAML o en `_quarto.yml`.

### Vista previa en vivo

```bash
quarto preview documento.qmd
```

Abre un navegador con vista previa que se actualiza automáticamente al guardar cambios. Ideal durante la escritura.

### Renderizar a un formato específico

```bash
quarto render documento.qmd --to html
quarto render documento.qmd --to pdf
quarto render documento.qmd --to epub
```

Ver [[output-formats]] para más detalles sobre formatos disponibles.

## Editores y entornos

### VS Code

La extensión oficial de Quarto para VS Code proporciona:

- Resaltado de sintaxis para `.qmd`
- Renderizado inline de código
- Comandos de renderizado y preview integrados
- Previsualización de ecuaciones LaTeX
- Fold management para bloques de código

Instálala desde el marketplace buscando **"Quarto"**.

### RStudio

Quarto se integra nativamente con RStudio (versión 2022.07 o superior):

- Botón de **Render** en la barra de herramientas
- Configuración de formato de salida desde el menú desplegable
- Completado automático para YAML y chunks de código
- Integración con proyectos R existentes

> **Nota:** No se requiere R para usar Quarto. Los documentos `.qmd` pueden contener código en Python, Julia, Observable o ningún lenguaje.

## Verificación

Para confirmar que la instalación es correcta:

```bash
# Verificar versión
quarto --version

# Crear un documento de prueba
quarto new test.qmd --no-browser

# Renderizar
quarto render test.qmd

# Verificar que se generó la salida
ls test.html
```

Si `quarto --version` retorna un número de versión (por ejemplo `1.4.x`), la instalación es correcta.

## Notas para Natura Docens

Este proyecto utiliza Quarto como sistema de publicación. El flujo de trabajo es:

1. Los autores escriben en formato `.qmd` (ver [[primer-documento]])
2. El proyecto se construye con `quarto render`, que genera archivos **HTML**, **PDF** y **EPUB** a partir de un mismo origen
3. La configuración central se encuentra en `_quarto.yml`, que define el motor de renderizado, los formatos de salida y las opciones de[[html-theming]] y plantillas

Para contribuir a Natura Docens, asegúrate de tener Quarto instalado y ejecuta `quarto render` desde la raíz del proyecto para verificar que todo compila correctamente antes de enviar cambios.
