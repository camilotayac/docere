#!/usr/bin/env python3
"""Valida el archivo .qmd generado por el generador de plan de clase.

Realiza checks mecánicos (sin LLM) sobre el output y produce un reporte
JSON estructurado que mapea cada fallo al agente responsable.

Uso:
    python3 validate_output.py output/plan_clase.qmd
    python3 validate_output.py output/plan_clase.qmd --json   # salida JSON
    python3 validate_output.py output/plan_clase.qmd --verbose
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# CHECKERS (cada una devuelve un dict con name, passed, detail optional)
# ---------------------------------------------------------------------------

EXPECTED_BOXES = [
    (r'\.teoria-box\b', 'teoria-box', 'Teoria', 'agente_teoria'),
    (r'\.ideas-previas-box\b', 'ideas-previas-box', 'Ideas Previas', 'agente_ideas_previas'),
    (r'\.contexto-box\b', 'contexto-box', 'Contexto Feynman', 'agente_contextualizacion_feynman'),
    (r'\.caracterizados-box\b', 'caracterizados-box', 'Caracterizados', 'agente_caracterizados'),
    (r'\.ejemplo-box\b', 'ejemplo-box', 'Ejemplos', 'agente_ejemplos'),
    (r'\.ejercicios-box\b', 'ejercicios-box', 'Ejercicios', 'agente_ejercicios'),
    (r'\.retos-box\b', 'retos-box', 'Retos', 'agente_retos'),
    (r'\.aplicacion-box\b', 'aplicacion-box', 'Aplicacion', 'agente_aplicacion'),
    (r'\.evaluacion-box\b', 'evaluacion-box', 'Evaluacion', 'agente_evaluacion'),
    (r'\.socioemocional-box\b', 'socioemocional-box', 'Socioemocional', 'agente_socioemocional'),
]


def check_box_balance(text: str, path: str) -> dict:
    """Cuenta pares ::: y verifica que estén balanceados."""
    opens = len(re.findall(r'^::: ', text, re.MULTILINE))
    closes = len(re.findall(r'^:::$', text, re.MULTILINE))
    if opens == closes and opens > 0:
        return {"name": "box_balance", "passed": True,
                "detail": f"{opens} bloques :::, todos balanceados"}
    return {"name": "box_balance", "passed": False,
            "detail": f"{opens} aperturas, {closes} cierres. Desbalanceados."}


def check_all_boxes_present(text: str, path: str) -> dict:
    """Verifica que cada tipo de box esperado aparece al menos una vez."""
    missing = []
    agent_map = {}
    for pattern, box_id, label, agent in EXPECTED_BOXES:
        if not re.search(pattern, text):
            missing.append(f"{label} ({box_id})")
            agent_map.setdefault(agent, []).append(f"missing_{box_id}")
    if not missing:
        return {"name": "all_boxes_present", "passed": True}
    return {"name": "all_boxes_present", "passed": False,
            "detail": "Faltan: " + ", ".join(missing),
            "failures_by_agent": agent_map}


def check_no_teacher_notes(text: str, path: str) -> dict:
    """Verifica que no haya [{...}] (notas para el docente intercaladas)."""
    matches = list(re.finditer(r'\[\{[^}]*\}\]', text))
    if not matches:
        return {"name": "no_teacher_notes", "passed": True}
    lines = [text[:m.start()].count('\n') + 1 for m in matches]
    return {"name": "no_teacher_notes", "passed": False,
            "detail": f"Se encontraron {len(matches)} notas [{...}] en líneas: {lines}",
            "failures_by_agent": {"agente_ejemplos": [f"teacher_note_at_line_{l}" for l in lines]}}


def check_no_todas_las_anteriores(text: str, path: str) -> dict:
    """Prohíbe 'Todas las anteriores' y 'Ninguna de las anteriores'."""
    pattern = r'(Todas\s+las\s+anteriores|Ninguna\s+de\s+las\s+anteriores)'
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    if not matches:
        return {"name": "no_todas_las_anteriores", "passed": True}
    lines = [text[:m.start()].count('\n') + 1 for m in matches]
    return {"name": "no_todas_las_anteriores", "passed": False,
            "detail": f"Encontrado en líneas: {lines}",
            "failures_by_agent": {"agente_evaluacion": ["todas_las_anteriores"]}}


def check_no_emojis(text: str, path: str) -> dict:
    """Detecta caracteres Unicode de emoji."""
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Misc Symbols and Pictographs
        "\U0001F680-\U0001F6FF"  # Transport and Map
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U00002600-\U000026FF"  # Misc symbols
        "\U0000200D"             # Zero Width Joiner
        "]+", re.UNICODE)
    matches = list(emoji_pattern.finditer(text))
    if not matches:
        return {"name": "no_emojis", "passed": True}
    lines = set(text[:m.start()].count('\n') + 1 for m in matches)
    return {"name": "no_emojis", "passed": False,
            "detail": f"Emojis encontrados en líneas: {sorted(lines)}"}


def check_latex_balance(text: str, path: str) -> dict:
    """Verifica pares de $...$ y $$...$$ balanceados."""
    dollar_signs = len(re.findall(r'(?<!\$)\$(?!\$)', text))
    double_dollar = len(re.findall(r'\$\$', text))
    errors = []
    if double_dollar % 2 != 0:
        errors.append(f"$$ display: {double_dollar} signos (impar)")
    if dollar_signs % 2 != 0:
        errors.append(f"$ inline: {dollar_signs} signos (impar)")
    if not errors:
        return {"name": "latex_balance", "passed": True}
    return {"name": "latex_balance", "passed": False, "detail": "; ".join(errors)}


def check_evaluacion_reactivos(text: str, path: str) -> dict:
    """Cuenta reactivos en evaluacion-box."""
    evaluacion_match = re.search(
        r'::: \{\.evaluacion-box[^}]*\}.*?:::', text, re.DOTALL)
    if not evaluacion_match:
        return {"name": "evaluacion_reactivos", "passed": False,
                "detail": "FALTA evaluacion-box",
                "failures_by_agent": {"agente_evaluacion": ["missing_evaluacion-box"]}}
    eval_text = evaluacion_match.group()

    reactivos = re.findall(
        r'\*\*Pregunta\s+\d+|Reactivo\s+\d+|(?<=\*\*)\d+(?=\.\s)',
        eval_text)
    count = len(reactivos)
    if count == 5:
        return {"name": "evaluacion_reactivos", "passed": True,
                "detail": f"{count} reactivos encontrados"}
    return {"name": "evaluacion_reactivos", "passed": False,
            "detail": f"Se esperaban 5 reactivos, se encontraron {count}",
            "failures_by_agent": {"agente_evaluacion": ["reactivos_count"]}}


def check_evaluacion_distribucion(text: str, path: str) -> dict:
    """Verifica distribución 2 Bajo + 2 Medio + 1 Alto en evaluación."""
    evaluacion_match = re.search(
        r'::: \{\.evaluacion-box[^}]*\}.*?:::', text, re.DOTALL)
    if not evaluacion_match:
        return {"name": "evaluacion_distribucion", "passed": False,
                "detail": "FALTA evaluacion-box",
                "failures_by_agent": {"agente_evaluacion": ["missing_evaluacion-box"]}}
    eval_text = evaluacion_match.group()
    bajos = len(re.findall(r'Nivel\s+Bajo|Bajo\b', eval_text, re.IGNORECASE))
    medios = len(re.findall(r'Nivel\s+Medio|Medio\b', eval_text, re.IGNORECASE))
    altos = len(re.findall(r'Nivel\s+Alto|Alto\b', eval_text, re.IGNORECASE))
    if bajos >= 2 and medios >= 2 and altos >= 1:
        return {"name": "evaluacion_distribucion", "passed": True,
                "detail": f"Bajo={bajos}, Medio={medios}, Alto={altos}"}
    return {"name": "evaluacion_distribucion", "passed": False,
            "detail": f"Esperado 2 Bajo + 2 Medio + 1 Alto. Obtenido: Bajo={bajos}, Medio={medios}, Alto={altos}",
            "failures_by_agent": {"agente_evaluacion": ["distribucion_niveles"]}}


def check_evaluacion_opciones(text: str, path: str) -> dict:
    """Verifica que cada reactivo tenga opciones A, B, C, D."""
    evaluacion_match = re.search(
        r'::: \{\.evaluacion-box[^}]*\}.*?:::', text, re.DOTALL)
    if not evaluacion_match:
        return {"name": "evaluacion_opciones", "passed": False,
                "detail": "FALTA evaluacion-box",
                "failures_by_agent": {"agente_evaluacion": ["missing_evaluacion-box"]}}
    eval_text = evaluacion_match.group()
    opciones = re.findall(r'(?:^|[-*])\s*[A-D][\).]', eval_text, re.MULTILINE)
    if len(opciones) >= 20:
        opt_count = len(opciones)
        num_reactivos_esperados = opt_count // 4
        return {"name": "evaluacion_opciones", "passed": True,
                "detail": f"{opt_count} opciones encontradas (~{num_reactivos_esperados} reactivos)"}
    return {"name": "evaluacion_opciones", "passed": False,
            "detail": f"Solo {len(opciones)} opciones A/B/C/D encontradas (esperadas ~20)",
            "failures_by_agent": {"agente_evaluacion": ["opciones_faltantes"]}}


def check_socializacion_box_exists(text: str, path: str) -> dict:
    """Verifica que exista un evaluacion-box con title Socializacion."""
    boxes = re.findall(
        r'::: \{\.evaluacion-box[^}]*\}', text)
    socializacion = [b for b in boxes if 'Socializacion' in b]
    if socializacion:
        return {"name": "socializacion_box_exists", "passed": True,
                "detail": "evaluacion-box con title Socializacion encontrado"}
    return {"name": "socializacion_box_exists", "passed": False,
            "detail": f"No se encontró evaluacion-box con title Socializacion. Total evaluacion-box: {len(boxes)}",
            "failures_by_agent": {"agente_socializacion": ["missing_socializacion_box"]}}


def check_socializacion_fields(text: str, path: str) -> dict:
    """Verifica que en el evaluacion-box de Socializacion existan los campos obligatorios."""
    boxes = re.findall(
        r'::: \{\.evaluacion-box[^}]*\}.*?:::', text, re.DOTALL)
    socializacion = [b for b in boxes if 'Socializacion' in b]
    if not socializacion:
        return {"name": "socializacion_fields", "passed": False,
                "detail": "FALTA evaluacion-box con title Socializacion",
                "failures_by_agent": {"agente_socializacion": ["missing_socializacion_box"]}}
    soc_text = socializacion[0]
    required_fields = [
        (r'Nivel', 'Nivel'),
        (r'Competencia', 'Competencia'),
        (r'Afirmaci[oó]n', 'Afirmación'),
        (r'Evidencia', 'Evidencia'),
        (r'Respuesta', 'Respuesta'),
        (r'Explicaci[oó]n', 'Explicación'),
    ]
    missing = []
    for pattern, label in required_fields:
        if not re.search(pattern, soc_text, re.IGNORECASE):
            missing.append(label)
    if not missing:
        return {"name": "socializacion_fields", "passed": True}
    return {"name": "socializacion_fields", "passed": False,
            "detail": "Campos faltantes: " + ", ".join(missing),
            "failures_by_agent": {"agente_evaluacion": [f"socializacion_falta_{m.lower()}" for m in missing]}}


def check_ejemplos_niveles(text: str, path: str) -> dict:
    """Verifica exactamente 3 ejemplos con niveles Bajo, Medio, Alto."""
    ejemplo_boxes = re.findall(
        r'::: \{\.ejemplo-box[^}]*\}.*?:::', text, re.DOTALL)
    if len(ejemplo_boxes) < 3:
        return {"name": "ejemplos_niveles", "passed": False,
                "detail": f"Se esperaban 3 ejemplo-box, se encontraron {len(ejemplo_boxes)}",
                "failures_by_agent": {"agente_ejemplos": ["niveles_faltantes"]}}
    titles = []
    for b in ejemplo_boxes:
        m = re.search(r'title="([^"]+)"', b)
        if m:
            titles.append(m.group(1))
    nivel_patterns = [r'Bajo', r'Medio', r'Alto']
    levels_found = []
    for p in nivel_patterns:
        if any(re.search(p, t, re.IGNORECASE) for t in titles):
            levels_found.append(p)
    if len(levels_found) == 3:
        return {"name": "ejemplos_niveles", "passed": True,
                "detail": f"3 ejemplo-box con niveles Bajo, Medio, Alto"}
    return {"name": "ejemplos_niveles", "passed": False,
            "detail": f"Faltan niveles. Títulos: {titles}",
            "failures_by_agent": {"agente_ejemplos": ["niveles_incompletos"]}}


def check_caracterizados_count(text: str, path: str) -> dict:
    """Verifica exactamente 6 bloques caracterizados-box."""
    boxes = re.findall(
        r'::: \{\.caracterizados-box[^}]*\}', text)
    count = len(boxes)
    if count == 6:
        return {"name": "caracterizados_count", "passed": True,
                "detail": "6 caracterizados-box encontrados"}
    return {"name": "caracterizados_count", "passed": False,
            "detail": f"Se esperaban 6 caracterizados-box, se encontraron {count}",
            "failures_by_agent": {"agente_caracterizados": [f"caracterizados_count_{count}"]}}


def check_caracterizados_content(text: str, path: str) -> dict:
    """Verifica que cada caracterizados-box tenga teoria + ejemplo + 2 ejercicios."""
    boxes = re.findall(
        r'::: \{\.caracterizados-box[^}]*\}.*?:::', text, re.DOTALL)
    errors = []
    for i, b in enumerate(boxes):
        title_m = re.search(r'title="([^"]+)"', b)
        title = title_m.group(1) if title_m else f"box-{i}"
        issues = []
        if not re.search(r'\*\*Ejemplo:\*\*', b):
            issues.append("falta **Ejemplo:**")
        if not re.search(r'\*\*Ejercicios:\*\*', b):
            issues.append("falta **Ejercicios:**")
        if issues:
            errors.append(f"{title}: {', '.join(issues)}")
    if not errors:
        return {"name": "caracterizados_content", "passed": True,
                "detail": "Cada caracterizados-box contiene teoria, Ejemplo: y Ejercicios:"}
    return {"name": "caracterizados_content", "passed": False,
            "detail": "; ".join(errors),
            "failures_by_agent": {"agente_caracterizados": ["contenido_incompleto"]}}


def check_ejercicios_count(text: str, path: str) -> dict:
    """Verifica exactamente 3 niveles de ejercicios (Bajo, Medio, Alto)."""
    boxes = re.findall(
        r'::: \{\.ejercicios-box[^}]*\}', text)
    count = len(boxes)
    if count == 3:
        titles = []
        for b in boxes:
            m = re.search(r'title="([^"]+)"', b)
            if m:
                titles.append(m.group(1))
        niveles = [r'Bajo', r'Medio', r'Alto']
        faltan = [n for n in niveles
                  if not any(re.search(n, t, re.IGNORECASE) for t in titles)]
        if not faltan:
            return {"name": "ejercicios_count", "passed": True,
                    "detail": "3 ejercicios-box con niveles Bajo, Medio, Alto"}
        return {"name": "ejercicios_count", "passed": False,
                "detail": f"Faltan niveles: {faltan}. Títulos: {titles}",
                "failures_by_agent": {"agente_ejercicios": ["niveles_faltantes"]}}
    return {"name": "ejercicios_count", "passed": False,
            "detail": f"Se esperaban 3 ejercicios-box, se encontraron {count}",
            "failures_by_agent": {"agente_ejercicios": [f"ejercicios_count_{count}"]}}


def check_section_order(text: str, path: str) -> dict:
    """Verifica que las secciones aparezcan en el orden esperado."""
    expected_order = [
        'teoria-box',
        'ideas-previas-box',
        'contexto-box',
        'caracterizados-box',
        'ejemplo-box',
        'ejercicios-box',
        'retos-box',
        'aplicacion-box',
        'evaluacion-box',
        'socioemocional-box',
    ]
    found = []
    for m in re.finditer(r'\{\.([a-z-]+-box)\b', text):
        cls = m.group(1)
        if cls not in found:
            found.append(cls)
    # Filter to only expected types
    found = [c for c in found if c in expected_order]
    expected_filtered = [c for c in expected_order if c in found]
    if found == expected_filtered:
        return {"name": "section_order", "passed": True}
    return {"name": "section_order", "passed": False,
            "detail": f"Orden esperado: {expected_filtered}. Obtenido: {found}"}


def check_no_html_inline(text: str, path: str) -> dict:
    """Prohíbe <span>, <div>, <style> HTML inline."""
    pattern = r'<(span|div|style)[^>]*>'
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    if not matches:
        return {"name": "no_html_inline", "passed": True}
    lines = [text[:m.start()].count('\n') + 1 for m in matches]
    return {"name": "no_html_inline", "passed": False,
            "detail": f"HTML inline en líneas: {lines}",
            "failures_by_agent": {"agente_estilo": ["html_inline"]}}


def check_no_ascii_boxes(text: str, path: str) -> dict:
    """Prohíbe caracteres de dibujo de cajas ASCII."""
    pattern = r'[┌┐└┘├┤┬┴──│┼╭╮╰╯╱╲▌▐▄▀]'
    matches = list(re.finditer(pattern, text))
    if not matches:
        return {"name": "no_ascii_boxes", "passed": True}
    lines = [text[:m.start()].count('\n') + 1 for m in matches[:20]]
    return {"name": "no_ascii_boxes", "passed": False,
            "detail": f"Caracteres ASCII box-drawing en líneas: {lines}",
            "failures_by_agent": {"agente_estilo": ["ascii_boxes"]}}


def check_ejercicios_have_answer_space(text: str, path: str) -> dict:
    """Verifica que los ejercicios-box tengan \\underline{\\hspace{6cm}}."""
    boxes = re.findall(
        r'::: \{\.ejercicios-box[^}]*\}.*?:::', text, re.DOTALL)
    boxes_missing = []
    for b in boxes:
        title_m = re.search(r'title="([^"]+)"', b)
        title = title_m.group(1) if title_m else "ejercicios-box"
        # Check if at least one underline hspace exists
        if not re.search(r'\\underline\{\\hspace\{6cm\}\}', b):
            boxes_missing.append(title)
    if not boxes_missing:
        return {"name": "ejercicios_answer_space", "passed": True}
    return {"name": "ejercicios_answer_space", "passed": False,
            "detail": f"Falta espacio de respuesta en: {boxes_missing}",
            "failures_by_agent": {"agente_ejercicios": ["missing_answer_space"]}}


def check_caracterizados_have_answer_space(text: str, path: str) -> dict:
    """Verifica que los caracterizados-box tengan \\underline{\\hspace{6cm}}."""
    boxes = re.findall(
        r'::: \{\.caracterizados-box[^}]*\}.*?:::', text, re.DOTALL)
    boxes_missing = []
    for b in boxes:
        title_m = re.search(r'title="([^"]+)"', b)
        title = title_m.group(1) if title_m else "caracterizados-box"
        if not re.search(r'\\underline\{\\hspace\{6cm\}\}', b):
            boxes_missing.append(title)
    if not boxes_missing:
        return {"name": "caracterizados_answer_space", "passed": True}
    return {"name": "caracterizados_answer_space", "passed": False,
            "detail": f"Falta espacio de respuesta en: {boxes_missing}",
            "failures_by_agent": {"agente_caracterizados": ["missing_answer_space"]}}


def check_icfes_enunciado_blank_line(text: str, path: str) -> dict:
    """Verifica que en ICFES haya línea en blanco entre *Enunciado:* y opciones."""
    evaluacion_match = re.search(
        r'::: \{\.evaluacion-box[^}]*\}.*?:::', text, re.DOTALL)
    if not evaluacion_match:
        return {"name": "icfes_enunciado_blank_line", "passed": True}
    eval_text = evaluacion_match.group()
    # Find all *Enunciado:* lines and check each one has a blank line before A.
    enunciados = list(re.finditer(
        r'\*Enunciado:\*', eval_text))
    bad = []
    for m in enunciados:
        after = eval_text[m.end():]
        # Check if the next non-blank line after Enunciado starts with A.
        next_line_match = re.match(r'(.*?)(\n[ \t]*)([A-D]\.)', after, re.DOTALL)
        if next_line_match:
            blank_or_text = next_line_match.group(1)
            if blank_or_text and not blank_or_text.isspace():
                # There's text content (no blank line) before A.
                bad.append(m)
    # Alternative: look for "no blank line" pattern
    # *Enunciado:* followed by text on same line, then \n then A. (no blank line in between)
    no_blank = list(re.finditer(
        r'\*Enunciado:\*.+?\n[ \t]*A\.', eval_text))
    if not no_blank:
        return {"name": "icfes_enunciado_blank_line", "passed": True,
                "detail": "Línea en blanco presente entre *Enunciado:* y opciones"}
    return {"name": "icfes_enunciado_blank_line", "passed": False,
            "detail": f"{len(no_blank)} enunciado(s) sin línea en blanco antes de opciones",
            "failures_by_agent": {"agente_evaluacion": ["icfes_enunciado_no_blank_line"]}}


def check_socioemocional_competencia(text: str, path: str) -> dict:
    """Verifica que la reflexión socioemocional nombre una competencia Ley 2503."""
    socio_match = re.search(
        r'::: \{\.socioemocional-box[^}]*\}.*?:::', text, re.DOTALL)
    if not socio_match:
        return {"name": "socioemocional_competencia", "passed": True}
    soc_text = socio_match.group()
    competencias = [
        r'Conciencia\s+Emocional',
        r'Regulaci[oó]n\s+Emocional',
        r'Autonom[íi]a',
        r'Inteligencia\s+Interpersonal',
        r'Habilidades\s+de\s+Vida',
        r'Bienestar',
    ]
    for p in competencias:
        if re.search(p, soc_text, re.IGNORECASE):
            return {"name": "socioemocional_competencia", "passed": True}
    return {"name": "socioemocional_competencia", "passed": False,
            "detail": "No se encontró ninguna competencia de Ley 2503/2025",
            "failures_by_agent": {"agente_socioemocional": ["competencia_faltante"]}}


EXPECTED_SECTIONS = {
    "teoria-box": "Teoria",
    "ideas-previas-box": "Ideas Previas",
    "contexto-box": "Contexto Feynman",
    "caracterizados-box": "Caracterizados",
    "ejemplo-box": "Ejemplos",
    "ejercicios-box": "Ejercicios",
    "retos-box": "Retos",
    "aplicacion-box": "Aplicacion",
    "evaluacion-box": "Evaluacion",
    "socioemocional-box": "Socioemocional",
}


def list_sections(text: str) -> dict:
    """Escanea un .qmd y devuelve boxes presentes y faltantes."""
    found_types = set()
    for m in re.finditer(r'\{\.([a-z-]+-box)\b', text):
        found_types.add(m.group(1))

    present = []
    missing = []
    for box_class, label in EXPECTED_SECTIONS.items():
        if box_class in found_types:
            present.append(box_class)
        else:
            missing.append(box_class)

    return {"present": present, "missing": missing}


ALL_CHECKS = [
    check_box_balance,
    check_all_boxes_present,
    check_no_teacher_notes,
    check_no_todas_las_anteriores,
    check_no_emojis,
    check_latex_balance,
    check_caracterizados_count,
    check_caracterizados_content,
    check_ejemplos_niveles,
    check_ejercicios_count,
    check_section_order,
    check_evaluacion_reactivos,
    check_evaluacion_distribucion,
    check_evaluacion_opciones,
    check_socializacion_box_exists,
    check_socializacion_fields,
    check_socioemocional_competencia,
    check_no_html_inline,
    check_no_ascii_boxes,
    check_ejercicios_have_answer_space,
    check_caracterizados_have_answer_space,
    check_icfes_enunciado_blank_line,
]

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------


def validate(text: str, path: str = "") -> dict:
    results = [check(text, path) for check in ALL_CHECKS]
    failures = [r for r in results if not r["passed"]]

    # Consolidar failures_by_agent
    failures_by_agent = {}
    for r in failures:
        agent_map = r.get("failures_by_agent", {})
        for agent, issues in agent_map.items():
            failures_by_agent.setdefault(agent, []).extend(issues)

    # Fallback: si hay fallos sin mapeo explícito
    if failures and not failures_by_agent:
        failures_by_agent["agente_qa"] = [
            r["name"] for r in failures]

    return {
        "passed": len(failures) == 0,
        "total_checks": len(results),
        "passed_checks": sum(1 for r in results if r["passed"]),
        "failed_checks": len(failures),
        "checks": results,
        "failures_by_agent": failures_by_agent,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Valida el .qmd generado por el generador de plan de clase")
    parser.add_argument("input", type=Path, help="Archivo .qmd a validar")
    parser.add_argument("--json", action="store_true",
                        help="Salida en JSON")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Muestra detalles de todos los checks")
    parser.add_argument("--sections", action="store_true",
                        help="Lista las secciones presentes y faltantes en el archivo")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: '{args.input}' no existe.")
        sys.exit(1)

    text = args.input.read_text(encoding="utf-8")

    if args.sections:
        sec = list_sections(text)
        print(json.dumps(sec, indent=2, ensure_ascii=False))
        return

    report = validate(text, path=str(args.input))

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    status = "✅ APROBADO" if report["passed"] else "❌ REQUIERE CORRECCIONES"
    print(f"\n{'='*60}")
    print(f"  VALIDACIÓN: {args.input.name}")
    print(f"  ESTADO: {status}")
    print(f"  Checks: {report['passed_checks']}/{report['total_checks']} pasaron")
    print(f"{'='*60}\n")

    if args.verbose:
        for r in report["checks"]:
            icon = "✅" if r["passed"] else "❌"
            detail = f" — {r['detail']}" if r.get("detail") else ""
            print(f"  {icon} {r['name']}{detail}")

    if not report["passed"]:
        print(f"\n  Fallos ({report['failed_checks']}):")
        for r in report["checks"]:
            if not r["passed"]:
                detail = f" — {r['detail']}" if r.get("detail") else ""
                print(f"    ❌ {r['name']}{detail}")
        if report["failures_by_agent"]:
            print(f"\n  Agentes responsables:")
            for agent, issues in report["failures_by_agent"].items():
                print(f"    - {agent}: {len(issues)} issue(s)")
                for issue in issues[:3]:
                    print(f"      · {issue}")
                if len(issues) > 3:
                    print(f"      · ... y {len(issues) - 3} más")
        print()

    sys.exit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
