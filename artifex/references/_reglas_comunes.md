# Reglas Comunes para Todos los Agentes

Este archivo define las reglas de formato y estilo que DEBEN seguir todos los agentes del pipeline Artifex. Los agentes individuales pueden agregar reglas especificas, pero NUNCA deben contradecir estas.

## Prohibiciones globales

- No incluir emojis en ningun bloque.
- No usar HTML inline (`<span>`, `<div>`, `<style>`).
- No usar tablas ASCII (``` ┌ ┐ └ ┘ ```).
- No usar notas `[{...}]` para el docente intercaladas en el contenido.
- No usar "Todas las anteriores" ni "Ninguna de las anteriores" en opciones ICFES.
- No usar las etiquetas literales `*Contexto:*` ni `*Enunciado:*` en el contenido de las preguntas. Cada pregunta ICFES debe iniciar con el encabezado indicando el número de pregunta y el nivel de dificultad en negrita (ej. `**Pregunta 1 — Nivel Bajo**`), seguido directamente de los párrafos de contexto y de pregunta.
- **Ortografía en Español:** Se DEBE escribir con ortografía perfecta en español (incluyendo todas las tildes y la letra ñ) en todo el contenido de los bloques. Los atributos `title="..."` de las cajas son la única excepción y nunca deben llevar acentos.


## Formato LaTeX

- **Todo valor numerico** en LaTeX inline `$...$`: `$5.0$`, `$55.85$`.
- **Toda unidad** dentro de `\text{}` con `\,` thin space: `$55.85\,\text{g}$`, `$2\,\text{mol}$`.
- **Compuestos quimicos** en LaTeX: `$H_2O$`, `$CH_3COOH$`, `$NaHCO_3$`.
- **Division** usar `\frac{}{}`, nunca `÷`.
- **Tags** en formulas importantes: `$$\...\tag{1}$$`.

## Espacios de respuesta

Siempre usar math mode para que funcionen en HTML y PDF:

- **Lineas independientes:** `$$\underline{\hspace{6cm}}$$` (indentadas 2 espacios).
- **En linea dentro de texto:** `$\underline{\hspace{3cm}}$`.

## Formato de cajas

- Cada bloque dentro de `::: {.tipo-box title="Titulo"}`.
- Los `title` deben coincidir EXACTAMENTE (caracter por caracter) con los definidos en `agente_qa.md`.
- Los títulos NO usan acentos (ej: `"Contextualizacion"`, no `"Contextualización"`).
- `:::` debe cerrarse correctamente (balanceados).

## Colores en contenido

Usar `**(color)**` en negrita: `**(rojo)**`, `**(azul)**`, `**(verde)**`.
Prohibido `<span style="color:...">`.

## Casos borde comunes

| Situacion | Accion |
|:---|:---|
| Entrada insuficiente o incompleta | Detener ejecucion y reportar al orquestador |
| Error en paso anterior | No inventar datos faltantes; reportar |
| Formato incompatible | Usar Markdown estandar; evitar formatos propietarios |
