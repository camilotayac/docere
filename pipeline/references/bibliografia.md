# Gestión de Bibliografía — Docere/book/references.bib

El archivo `book/references.bib` contiene las referencias bibliográficas
disponibles para todos los planes de clase. Está en formato BibTeX estándar.

## Referencias disponibles

Clave: `oriakhi2021chemistry`
Título: Chemistry in Quantitative Language
Autor: Oriakhi, Christopher O
Año: 2021
Editorial: Oxford University Press

Clave: `audesirk2017biologia`
Título: Biología: La vida en la Tierra con Fisiología
Autores: Audesirk, Teresa; Audesirk, Gerald; Byers, Bruce E.
Año: 2017
Editorial: Pearson Educación (10ª ed.)

Clave: `young2018fisica`
Título: Física universitaria con física moderna 1
Autores: Young, Hugh D.; Freedman, Roger A.
Año: 2018
Editorial: Pearson Educación (14ª ed.)

## Instrucciones para el orquestador

Al inicio del pipeline (Paso 0.5), el orquestador DEBE:

1. **Leer** `book/references.bib` y extraer la lista de referencias.
2. **Presentar** al usuario las referencias disponibles en formato legible.
3. **Preguntar** cuáles desea usar para este plan de clase:
   - Opción "Todas" (por defecto)
   - Opción "Ninguna"
   - Selección individual
4. **Inyectar** las referencias seleccionadas a todos los agentes downstream
   como parte del contexto, en la sección `## Referencias disponibles` al
   final de cada prompt:

   ```
   ## Referencias disponibles para este plan de clase

   Las siguientes referencias bibliográficas están disponibles para usar
   en el contenido (citas, ejemplos, ejercicios):

   - Oriakhi (2021) — Chemistry in Quantitative Language
   - Young & Freedman (2018) — Física universitaria

   Puedes citarlas explícitamente si es relevante para el concepto.
   ```

5. **Incluir** en el YAML front matter del .qmd generado la línea:
   ```yaml
   bibliography: ../../book/references.bib
   ```
   (ruta relativa desde `output/` hasta `book/references.bib`)

## Notas

- La ruta en el YAML debe ser relativa al archivo .qmd generado. Si el .qmd
  se coloca en `book/<grado>/`, usar `../references.bib`. Si se coloca en
  `output/`, usar `../book/references.bib`.
- Las referencias se renderizan automáticamente al compilar con Quarto
  usando el formato de citación estándar.
