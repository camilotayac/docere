## Entrada de Retroalimentacion (Opcional)

Si el orquestador incluye un bloque `## Feedback de QA` al final de este
prompt, el agente DEBE:
1. Leer los errores reportados que le corresponden (indicados en el campo
   "Agente" del feedback).
2. Identificar que parte de su output genero el error.
3. Corregir especificamente esa parte, sin modificar lo que ya esta correcto.
4. Si no hay feedback o no hay errores asignados a este agente, comportarse
   normalmente.
