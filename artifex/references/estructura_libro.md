# Estructura del Libro — Docere/liber/

Mapa de grados, archivos .qmd y secciones existentes en el proyecto Quarto.

## Directorios por grado

| Carpeta | Grados | Archivos |
|:---|:---|:---|
| `02_Sexto` | 6° | Biologia.qmd |
| `03_Septimo` | 7° | Fisica.qmd, Quimica.qmd |
| `04_Octavo` | 8° | Biologia.qmd, Quimica.qmd |
| `05_Noveno` | 9° | Quimica.qmd |
| `06_Decimo` | 10° | Biologia.qmd, Quimica.qmd |
| `07_Once` | 11° | QUIMICA.qmd |

## Ruta base

Todos los archivos están en `liber/<carpeta>/<archivo>.qmd` relativo a la raíz de Docere/.

## Formato de cada archivo

Cada .qmd contiene bloques educativos secuenciales usando la convención de boxes.
La lista completa de secciones (23 bloques, 11 tipos) y sus titulos exactos esta
definida en `agente_qa.md` — **ese es el unico source of truth** para todos los
agentes del pipeline.

> **Nota:** Las reglas de formato estan en `_reglas_comunes.md`. No todos los
> archivos .qmd contienen todos los boxes; algunos son parciales.

## Uso en el proceso

El orquestador usa este archivo para:
1. Preguntar al usuario qué grado corresponde al plan de clase generado.
2. Listar los archivos .qmd existentes en ese grado.
3. Preguntar si crear archivo nuevo o modificar existente.
4. Si modificar: detectar boxes presentes vs faltantes con `validate_output.py --sections`.
5. Mostrar menú de mejora/agregación al usuario.
