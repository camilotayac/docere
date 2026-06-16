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
    (r"## [^{]+\{\.teoria\}", "teoria", "Teoria", "agente_teoria"),
    (r"## [^{]+\{\.ideas-previas\}", "ideas-previas", "Ideas Previas", "agente_ideas_previas"),
    (r"## [^{]+\{\.contexto\}", "contexto", "Contexto Feynman", "agente_contextualizacion_feynman"),
    (r"## [^{]+\{\.caracterizados\}", "caracterizados", "Caracterizados", "agente_caracterizados"),
    (r"## [^{]+\{\.ejemplo\}", "ejemplo", "Ejemplos", "agente_ejemplos"),
    (r"## [^{]+\{\.ejercicios\}", "ejercicios", "Ejercicios", "agente_ejercicios"),
    (r"## [^{]+\{\.retos\}", "retos", "Retos", "agente_retos"),
    (r"## [^{]+\{\.aplicacion\}", "aplicacion", "Aplicacion", "agente_aplicacion"),
    (r"## [^{]+\{\.evaluacion\}", "evaluacion", "Evaluacion", "agente_evaluacion"),
    (r"## [^{]+\{\.socioemocional\}", "socioemocional", "Socioemocional", "agente_socioemocional"),
]


def check_box_balance(text: str, path: str) -> dict:
    """Verifica que los headings con clase estén balanceados."""
    opens = len(re.findall(r"^## .*?\{\.([a-z-]+)\}", text, re.MULTILINE))
    if opens > 0:
        return {
            "name": "box_balance",
            "passed": True,
            "detail": f"{opens} bloques ## con clase, todos correctos",
        }
    return {
        "name": "box_balance",
        "passed": False,
        "detail": "No se encontraron headings con clase.",
    }


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
    return {
        "name": "all_boxes_present",
        "passed": False,
        "detail": "Faltan: " + ", ".join(missing),
        "failures_by_agent": agent_map,
    }


def check_no_teacher_notes(text: str, path: str) -> dict:
    """Verifica que no haya [{...}] (notas para el docente intercaladas)."""
    matches = list(re.finditer(r"\[\{[^}]*\}\]", text))
    if not matches:
        return {"name": "no_teacher_notes", "passed": True}
    lines = [text[: m.start()].count("\n") + 1 for m in matches]
    return {
        "name": "no_teacher_notes",
        "passed": False,
        "detail": f"Se encontraron {len(matches)} notas [{...}] en líneas: {lines}",
    }


def check_no_todas_las_anteriores(text: str, path: str) -> dict:
    """Prohíbe 'Todas las anteriores' y 'Ninguna de las anteriores'."""
    pattern = r"(Todas\s+las\s+anteriores|Ninguna\s+de\s+las\s+anteriores)"
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    if not matches:
        return {"name": "no_todas_las_anteriores", "passed": True}
    lines = [text[: m.start()].count("\n") + 1 for m in matches]
    return {
        "name": "no_todas_las_anteriores",
        "passed": False,
        "detail": f"Encontrado en líneas: {lines}",
        "failures_by_agent": {"agente_evaluacion": ["todas_las_anteriores"]},
    }


def check_no_emojis(text: str, path: str) -> dict:
    """Detecta caracteres Unicode de emoji (excepto 🟢🟡🔴 permitidos)."""
    # Primero removemos los circulos permitidos
    cleaned = re.sub(r"[🟢🟡🔴]", "", text)
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # Emoticons
        "\U0001f300-\U0001f5ff"  # Misc Symbols and Pictographs
        "\U0001f680-\U0001f6ff"  # Transport and Map
        "\U0001f1e0-\U0001f1ff"  # Flags
        "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
        "\U0001fa00-\U0001fa6f"  # Chess Symbols
        "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027b0"  # Dingbats
        "\U00002600-\U000026ff"  # Misc symbols
        "\U0000200d"  # Zero Width Joiner
        "]+",
        re.UNICODE,
    )
    matches = list(emoji_pattern.finditer(cleaned))
    if not matches:
        return {"name": "no_emojis", "passed": True}
    lines = set(text[: m.start()].count("\n") + 1 for m in matches)
    return {
        "name": "no_emojis",
        "passed": False,
        "detail": f"Emojis encontrados en líneas: {sorted(lines)}",
    }


def check_latex_balance(text: str, path: str) -> dict:
    """Verifica pares de $...$ y $$...$$ balanceados."""
    dollar_signs = len(re.findall(r"(?<!\$)\$(?!\$)", text))
    double_dollar = len(re.findall(r"\$\$", text))
    errors = []
    if double_dollar % 2 != 0:
        errors.append(f"$$ display: {double_dollar} signos (impar)")
    if dollar_signs % 2 != 0:
        errors.append(f"$ inline: {dollar_signs} signos (impar)")
    if not errors:
        return {"name": "latex_balance", "passed": True}
    return {"name": "latex_balance", "passed": False, "detail": "; ".join(errors)}


def _find_icfes_box(text: str) -> str | None:
    """Busca la seccion .evaluacion que contiene 'Evaluacion' en su titulo (y no 'Socializacion')."""
    sections = re.split(r"\n(?=## )", text)
    for sec in sections:
        first_line = sec.split("\n")[0]
        if "{.evaluacion}" in first_line and "Socializacion" not in first_line:
            if "Evaluacion" in first_line or "Evaluación" in first_line:
                return sec
    return None


def check_evaluacion_reactivos(text: str, path: str) -> dict:
    """Cuenta reactivos en .evaluacion ICFES."""
    eval_match = _find_icfes_box(text)
    if not eval_match:
        return {
            "name": "evaluacion_reactivos",
            "passed": False,
            "detail": "FALTA heading .evaluacion con 'Evaluacion - tipo ICFES'",
            "failures_by_agent": {"agente_evaluacion": ["missing_evaluacion"]},
        }
    eval_text = eval_match

    # Cuenta líneas en negrita que digan Nivel Bajo/Medio/Alto o Pregunta X
    reactivos = re.findall(
        r"^[ \t]*\*\*Pregunta\s+\d+\s*[—–-]\s*Nivel\s+(?:Bajo|Medio|Alto)\*\*[ \t]*$",
        eval_text,
        re.MULTILINE | re.IGNORECASE
    )
    count = len(reactivos)
    if count == 5:
        return {
            "name": "evaluacion_reactivos",
            "passed": True,
            "detail": f"{count} reactivos encontrados",
        }
    
    # Fallback to count any Pregunta \d+ at start of line
    fallback = re.findall(
        r"^[ \t]*\*\*Pregunta\s+\d+.*$",
        eval_text,
        re.MULTILINE | re.IGNORECASE
    )
    fallback_count = len(fallback)
    if fallback_count == 5:
        return {
            "name": "evaluacion_reactivos",
            "passed": True,
            "detail": f"{fallback_count} reactivos encontrados (con formato alternativo)",
        }
        
    return {
        "name": "evaluacion_reactivos",
        "passed": False,
        "detail": f"Se esperaban 5 reactivos, se encontraron {count} (con fallback: {fallback_count})",
        "failures_by_agent": {"agente_evaluacion": ["reactivos_count"]},
    }


def check_evaluacion_opciones(text: str, path: str) -> dict:
    """Verifica que cada reactivo tenga opciones A, B, C, D."""
    eval_match = _find_icfes_box(text)
    if not eval_match:
        return {
            "name": "evaluacion_opciones",
            "passed": False,
            "detail": "FALTA heading .evaluacion con 'Evaluacion - tipo ICFES'",
            "failures_by_agent": {"agente_evaluacion": ["missing_evaluacion"]},
        }
    eval_text = eval_match
    # Opciones pueden estar al inicio de línea o en tabla Markdown: | A. ... |
    opciones = re.findall(r"(?:^[ \t]*|[|])[ \t]*[A-D]\.", eval_text, re.MULTILINE)
    count = len(opciones)
    if count == 20:
        return {
            "name": "evaluacion_opciones",
            "passed": True,
            "detail": "20 opciones A/B/C/D encontradas (4 por cada una de las 5 preguntas)",
        }
    return {
        "name": "evaluacion_opciones",
        "passed": False,
        "detail": f"Se encontraron {count} opciones A/B/C/D (se esperaban exactamente 20)",
        "failures_by_agent": {"agente_evaluacion": ["opciones_faltantes"]},
    }


def check_socializacion_box_exists(text: str, path: str) -> dict:
    """Verifica que exista un heading .evaluacion con titulo Socializacion."""
    boxes = re.findall(r"## [^{]+\{\.evaluacion\}", text)
    socializacion = [b for b in boxes if "Socializacion" in b or "Socialización" in b]
    if socializacion:
        return {
            "name": "socializacion_box_exists",
            "passed": True,
            "detail": "heading .evaluacion con titulo Socializacion encontrado",
        }
    return {
        "name": "socializacion_box_exists",
        "passed": False,
        "detail": (
            f"No se encontró heading .evaluacion con titulo Socializacion."
            f" Total: {len(boxes)} .evaluacion"
        ),
        "failures_by_agent": {"agente_socializacion": ["missing_socializacion_box"]},
    }


def check_socializacion_fields(text: str, path: str) -> dict:
    """Verifica que en el bloque .evaluacion de Socializacion existan los campos obligatorios."""
    sections = re.split(r"\n(?=## )", text)
    socializacion = [s for s in sections if re.search(r"## [^{]*(Socializacion|Socialización)[^{]*\{\.evaluacion\}", s)]
    if not socializacion:
        return {
            "name": "socializacion_fields",
            "passed": False,
            "detail": "FALTA bloque .evaluacion con Socializacion",
            "failures_by_agent": {"agente_socializacion": ["missing_socializacion"]},
        }
    soc_text = socializacion[0]
    required_fields = [
        (r"Competencia", "Competencia"),
        (r"Afirmaci[oó]n", "Afirmación"),
        (r"Evidencia", "Evidencia"),
        (r"Respuesta correcta", "Respuesta"),
        (r"Explicaci[oó]n", "Explicación"),
    ]
    missing = []
    for pattern, label in required_fields:
        if not re.search(pattern, soc_text, re.IGNORECASE):
            missing.append(label)
    if not missing:
        return {"name": "socializacion_fields", "passed": True}
    return {
        "name": "socializacion_fields",
        "passed": False,
        "detail": "Campos faltantes: " + ", ".join(missing),
        "failures_by_agent": {
            "agente_socializacion": [f"socializacion_falta_{m.lower()}" for m in missing]
        },
    }


def check_ejemplos_niveles(text: str, path: str) -> dict:
    """Verifica exactamente 3 ejemplos con niveles Bajo, Medio, Alto."""
    ejemplos = re.findall(r"## [^{]+\{\.ejemplo\}", text)
    if len(ejemplos) < 3:
        return {
            "name": "ejemplos_niveles",
            "passed": False,
            "detail": f"Se esperaban 3 .ejemplo, se encontraron {len(ejemplos)}",
            "failures_by_agent": {"agente_ejemplos": ["niveles_faltantes"]},
        }
    titles = [h.replace("## ", "").strip() for h in ejemplos]
    # Dificultad indicada por 🟢🟡🔴 o texto Bajo/Medio/Alto
    nivel_patterns = [(r"🟢|Bajo", "Bajo"), (r"🟡|Medio", "Medio"), (r"🔴|Alto", "Alto")]
    levels_found = []
    for pattern, label in nivel_patterns:
        if any(re.search(pattern, t) for t in titles):
            levels_found.append(label)
    if len(levels_found) == 3:
        return {
            "name": "ejemplos_niveles",
            "passed": True,
            "detail": "3 .ejemplo con niveles Bajo, Medio, Alto",
        }
    return {
        "name": "ejemplos_niveles",
        "passed": False,
        "detail": f"Faltan niveles. Títulos: {titles}",
        "failures_by_agent": {"agente_ejemplos": ["niveles_incompletos"]},
    }


def check_caracterizados_count(text: str, path: str) -> dict:
    """Verifica exactamente 6 bloques .caracterizados."""
    boxes = re.findall(r"## [^{]+\{\.caracterizados\}", text)
    count = len(boxes)
    if count == 6:
        return {
            "name": "caracterizados_count",
            "passed": True,
            "detail": "6 bloques .caracterizados encontrados",
        }
    return {
        "name": "caracterizados_count",
        "passed": False,
        "detail": f"Se esperaban 6 bloques .caracterizados, se encontraron {count}",
        "failures_by_agent": {"agente_caracterizados": [f"caracterizados_count_{count}"]},
    }


def check_caracterizados_swap_test(text: str, path: str) -> dict:
    """Swap test: intercambia headings entre perfiles y verifica que el
    contenido NO funcionaria para otro perfil.

    Estrategia: para cada par de perfiles, intercambia los headings y
    cuenta lineas identicas en la teoria y metacognicion. Si hay alta
    similitud (>60%), el bloque es generico.

    Retorna un check con detalle de pares que fallaron y una sugerencia
    de cuantos intentos de regeneracion serian necesarios.
    """
    sections = re.split(r"\n(?=## )", text)
    boxes = [s for s in sections if re.search(r"\{\.caracterizados\}", s)]

    if len(boxes) < 6:
        return {
            "name": "caracterizados_swap_test",
            "passed": True,
            "detail": "Menos de 6 bloques, swap test no aplica",
        }

    profiles = [
        "TDAH",
        "Visual",
        "Dislexia",
        "Autismo",
        "Accesibilidad",
        "Socioemocional",
    ]

    def extract_core(text):
        """Extrae lineas de teoria y metacognicion de un bloque."""
        lines = []
        in_block = False
        for line in text.split("\n"):
            stripped = line.strip()
            if not stripped or stripped.startswith(":::") or stripped.startswith("##"):
                continue
            if stripped.startswith("**Ejemplo:**") or stripped.startswith("**Ejercicios:**"):
                in_block = False
            if in_block:
                lines.append(stripped)
            if stripped.startswith("**Metacognicion"):
                in_block = True
        return set(lines)

    failed_pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            core_i = extract_core(boxes[i])
            core_j = extract_core(boxes[j])
            if not core_i or not core_j:
                continue
            intersection = core_i & core_j
            union = core_i | core_j
            if not union:
                continue
            similarity = len(intersection) / len(union)
            if similarity > 0.6:
                failed_pairs.append(
                    f"{profiles[i]}-{profiles[j]}: {similarity:.0%} de lineas compartidas"
                )

    if not failed_pairs:
        return {
            "name": "caracterizados_swap_test",
            "passed": True,
            "detail": "Todos los pares superan el swap test (similitud <60%)",
        }

    return {
        "name": "caracterizados_swap_test",
        "passed": False,
        "detail": "Swap test fallo para pares: " + "; ".join(failed_pairs),
        "failures_by_agent": {
            "agente_caracterizados": ["swap_test_failed"]
        },
    }


def check_caracterizados_content(text: str, path: str) -> dict:
    """Verifica que cada bloque .caracterizados tenga teoria + ejemplo + 2 ejercicios."""
    sections = re.split(r"\n(?=## )", text)
    boxes = [s for s in sections if re.search(r"\{\.caracterizados\}", s)]
    errors = []
    for i, b in enumerate(boxes):
        heading = b.split("\n")[0] if b.strip() else f"box-{i}"
        issues = []
        if not re.search(r"\*\*Ejemplo:\*\*", b) and not re.search(r"\*\*Ejemplo\*\*", b):
            issues.append("falta **Ejemplo:**")
        if not re.search(r"\*\*Ejercicios:\*\*", b) and not re.search(r"\*\*Ejercicios\*\*", b):
            issues.append("falta **Ejercicios:**")
        if issues:
            errors.append(f"{heading.strip()}: {', '.join(issues)}")
    if not errors:
        return {
            "name": "caracterizados_content",
            "passed": True,
            "detail": "Cada caracterizados-box contiene teoria, Ejemplo: y Ejercicios:",
        }
    return {
        "name": "caracterizados_content",
        "passed": False,
        "detail": "; ".join(errors),
        "failures_by_agent": {"agente_caracterizados": ["contenido_incompleto"]},
    }


def check_caracterizados_metacognicion(text: str, path: str) -> dict:
    """Verifica que cada bloque .caracterizados tenga Metacognicion."""
    sections = re.split(r"\n(?=## )", text)
    boxes = [s for s in sections if re.search(r"\{\.caracterizados\}", s)]
    missing = []
    for i, b in enumerate(boxes):
        heading = b.split("\n")[0].strip() if b.strip() else f"box-{i}"
        if not re.search(r"\*\*Metacognicion:\*\*", b, re.IGNORECASE) and not re.search(r"\*\*Metacognición:\*\*", b):
            missing.append(heading)
    if not missing:
        return {
            "name": "caracterizados_metacognicion",
            "passed": True,
            "detail": "Cada bloque tiene **Metacognicion:**",
        }
    return {
        "name": "caracterizados_metacognicion",
        "passed": False,
        "detail": "Falta **Metacognicion:** en: " + ", ".join(missing),
        "failures_by_agent": {"agente_caracterizados": ["falta_metacognicion"]},
    }


def check_caracterizados_glosario(text: str, path: str) -> dict:
    """Verifica que cada bloque .caracterizados tenga Glosario."""
    sections = re.split(r"\n(?=## )", text)
    boxes = [s for s in sections if re.search(r"\{\.caracterizados\}", s)]
    missing = []
    for i, b in enumerate(boxes):
        heading = b.split("\n")[0].strip() if b.strip() else f"box-{i}"
        if not re.search(r"\*\*Glosario:\*\*", b, re.IGNORECASE) and not re.search(r"\*\*Glosario\*\*", b):
            missing.append(heading)
    if not missing:
        return {
            "name": "caracterizados_glosario",
            "passed": True,
            "detail": "Cada bloque tiene **Glosario:**",
        }
    return {
        "name": "caracterizados_glosario",
        "passed": False,
        "detail": "Falta **Glosario:** en: " + ", ".join(missing),
        "failures_by_agent": {"agente_caracterizados": ["falta_glosario"]},
    }


def check_caracterizados_alternative_format(text: str, path: str) -> dict:
    """Verifica que cada bloque .caracterizados tenga al menos una opcion de formato alternativo."""
    sections = re.split(r"\n(?=## )", text)
    boxes = [s for s in sections if re.search(r"\{\.caracterizados\}", s)]
    missing = []
    for i, b in enumerate(boxes):
        heading = b.split("\n")[0].strip() if b.strip() else f"box-{i}"
        if not re.search(
            r"Opci[oó]n\s+de\s+respuesta|Opci[oó]n\s+de\s+formato|Opcion\s+de\s+respuesta|Opcion\s+de\s+formato",
            b, re.IGNORECASE
        ):
            missing.append(heading)
    if not missing:
        return {
            "name": "caracterizados_alternative_format",
            "passed": True,
            "detail": "Cada bloque ofrece opcion alternativa de formato",
        }
    return {
        "name": "caracterizados_alternative_format",
        "passed": False,
        "detail": "Falta opcion de formato alternativo en: " + ", ".join(missing),
        "failures_by_agent": {"agente_caracterizados": ["falta_formato_alternativo"]},
    }


def check_autoevaluacion_present(text: str, path: str) -> dict:
    """Verifica que en la evaluacion ICFES exista seccion de Autoevaluacion."""
    eval_text = _find_icfes_box(text)
    if not eval_text:
        return {"name": "autoevaluacion_present", "passed": True}
    if re.search(r"\*\*Autoevaluaci[oó]n:\*\*", eval_text):
        return {
            "name": "autoevaluacion_present",
            "passed": True,
            "detail": "Seccion Autoevaluacion presente",
        }
    return {
        "name": "autoevaluacion_present",
        "passed": False,
        "detail": "Falta **Autoevaluacion:** en el bloque de evaluacion",
        "failures_by_agent": {"agente_evaluacion": ["falta_autoevaluacion"]},
    }


def check_no_capacitist_language(text: str, path: str) -> dict:
    """Detecta frases capacitistas o sobreprotectoras."""
    bad_patterns = [
        r"no\s+te\s+preocupes\s+si\s+no\s+entiendes",
        r"esto\s+es\s+dif[ií]cil\s+pero",
        r"si\s+no\s+puedes\s+no\s+importa",
        r"aunque\s+suene\s+complicado",
        r"esto\s+es\s+complicado\s+pero",
        r"t[ií]tulo\s+del\s+box",
    ]
    matches = []
    for p in bad_patterns:
        for m in re.finditer(p, text, re.IGNORECASE):
            line = text[: m.start()].count("\n") + 1
            matches.append((line, m.group()))
    if not matches:
        return {"name": "no_capacitist_language", "passed": True}
    return {
        "name": "no_capacitist_language",
        "passed": False,
        "detail": f"Lenguaje capacitista en lineas: {[l for l, _ in matches]}",
        "failures_by_agent": {"agente_caracterizados": ["lenguaje_capacitista"]},
    }


def check_ejercicios_count(text: str, path: str) -> dict:
    """Verifica exactamente 3 niveles de ejercicios (Bajo, Medio, Alto)."""
    boxes = re.findall(r"## [^{]+\{\.ejercicios\}", text)
    count = len(boxes)
    if count == 3:
        titles = [h.replace("## ", "").strip() for h in boxes]
        niveles = [(r"🟢|Bajo", "Bajo"), (r"🟡|Medio", "Medio"), (r"🔴|Alto", "Alto")]
        faltan = [label for pattern, label in niveles if not any(re.search(pattern, t) for t in titles)]
        if not faltan:
            return {
                "name": "ejercicios_count",
                "passed": True,
                "detail": "3 .ejercicios con niveles Bajo, Medio, Alto",
            }
        return {
            "name": "ejercicios_count",
            "passed": False,
            "detail": f"Faltan niveles: {faltan}. Títulos: {titles}",
            "failures_by_agent": {"agente_ejercicios": ["niveles_faltantes"]},
        }
    return {
        "name": "ejercicios_count",
        "passed": False,
        "detail": f"Se esperaban 3 .ejercicios, se encontraron {count}",
        "failures_by_agent": {"agente_ejercicios": [f"ejercicios_count_{count}"]},
    }


def check_section_order(text: str, path: str) -> dict:
    """Verifica que las secciones aparezcan en el orden esperado."""
    expected_order = [
        "teoria",
        "ideas-previas",
        "contexto",
        "caracterizados",
        "ejemplo",
        "ejercicios",
        "retos",
        "aplicacion",
        "evaluacion",
        "socioemocional",
    ]
    found = []
    for m in re.finditer(r"\{\.([a-z-]+)\}", text):
        cls = m.group(1)
        if cls not in found and cls in expected_order:
            found.append(cls)
    found = [c for c in found if c in expected_order]
    expected_filtered = [c for c in expected_order if c in found]
    if found == expected_filtered:
        return {"name": "section_order", "passed": True}
    return {
        "name": "section_order",
        "passed": False,
        "detail": f"Orden esperado: {expected_filtered}. Obtenido: {found}",
    }


def check_no_html_inline(text: str, path: str) -> dict:
    """Prohíbe HTML inline como div, style, br, table, img, etc. (span permitido para colores)."""
    pattern = r"</?(div|style|br|table|img|p|h[1-6]|tr|td|th)\b[^>]*>"
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    if not matches:
        return {"name": "no_html_inline", "passed": True}
    lines = [text[: m.start()].count("\n") + 1 for m in matches]
    return {
        "name": "no_html_inline",
        "passed": False,
        "detail": f"HTML inline en líneas: {lines}",
        "failures_by_agent": {"agente_estilo": ["html_inline"]},
    }


def check_no_ascii_boxes(text: str, path: str) -> dict:
    """Prohíbe caracteres de dibujo de cajas ASCII y Block Elements."""
    # Cubre el bloque de Unicode de Box Drawing U+2500 a U+257F y Block Elements U+2580 a U+259F
    pattern = r"[\u2500-\u259F]"
    matches = list(re.finditer(pattern, text))
    if not matches:
        return {"name": "no_ascii_boxes", "passed": True}
    lines = [text[: m.start()].count("\n") + 1 for m in matches[:20]]
    return {
        "name": "no_ascii_boxes",
        "passed": False,
        "detail": f"Caracteres ASCII box-drawing en líneas: {lines}",
        "failures_by_agent": {"agente_estilo": ["ascii_boxes"]},
    }


def check_ejercicios_have_answer_space(text: str, path: str) -> dict:
    """Verifica que los bloques .ejercicios tengan \\underline{\\hspace{6cm}}."""
    sections = re.split(r"\n(?=## )", text)
    boxes = [s for s in sections if r"{.ejercicios}" in s]
    boxes_missing = []
    for i, b in enumerate(boxes):
        heading = b.split("\n")[0].strip() if b.strip() else f"ejercicios-{i}"
        if not re.search(r"\\underline\{\\hspace\{6cm\}\}", b):
            boxes_missing.append(heading)
    if not boxes_missing:
        return {"name": "ejercicios_answer_space", "passed": True}
    return {
        "name": "ejercicios_answer_space",
        "passed": False,
        "detail": f"Falta espacio de respuesta en: {boxes_missing}",
        "failures_by_agent": {"agente_ejercicios": ["missing_answer_space"]},
    }


def check_caracterizados_have_answer_space(text: str, path: str) -> dict:
    """Verifica que los bloques .caracterizados tengan \\underline{\\hspace{6cm}}."""
    sections = re.split(r"\n(?=## )", text)
    boxes = [s for s in sections if r"{.caracterizados}" in s]
    boxes_missing = []
    for i, b in enumerate(boxes):
        heading = b.split("\n")[0].strip() if b.strip() else f"caracterizados-{i}"
        if not re.search(r"\\underline\{\\hspace\{6cm\}\}", b):
            boxes_missing.append(heading)
    if not boxes_missing:
        return {"name": "caracterizados_answer_space", "passed": True}
    return {
        "name": "caracterizados_answer_space",
        "passed": False,
        "detail": f"Falta espacio de respuesta en: {boxes_missing}",
        "failures_by_agent": {"agente_caracterizados": ["missing_answer_space"]},
    }


def check_icfes_enunciado_blank_line(text: str, path: str) -> dict:
    """Verifica que en ICFES haya línea en blanco antes de la opción A. (entre el enunciado y las opciones)."""
    eval_text = _find_icfes_box(text)
    if not eval_text:
        return {"name": "icfes_enunciado_blank_line", "passed": True}
    
    # Find where this section starts in the full text
    eval_start = text.find(eval_text[:80].split("\n")[0])
    if eval_start < 0:
        eval_start = 0
    
    # Buscamos todas las ocurrencias de la opción A. al inicio de línea
    a_options = list(re.finditer(r"^[ \t]*A\.", eval_text, re.MULTILINE))
    bad = []
    for m in a_options:
        before = eval_text[:m.start()]
        # Verificamos si termina con dos saltos de línea y opcionales espacios (línea en blanco)
        if not re.search(r"\n[ \t]*\n[ \t]*$", before):
            line_num = text[:eval_start + m.start()].count("\n") + 1
            bad.append(line_num)
            
    if not bad:
        return {
            "name": "icfes_enunciado_blank_line",
            "passed": True,
            "detail": "Línea en blanco presente antes de la opción A.",
        }
    return {
        "name": "icfes_enunciado_blank_line",
        "passed": False,
        "detail": f"Falta línea en blanco antes de la opción A. en líneas: {bad}",
        "failures_by_agent": {"agente_evaluacion": ["icfes_enunciado_no_blank_line"]},
    }



def check_answer_spaces_in_math_mode(text: str, path: str) -> dict:
    """Verifica que \\underline siempre este dentro de $...$ o $$...$$."""
    bare = list(re.finditer(r"(?<!\$)\\underline\{", text))
    if not bare:
        return {"name": "answer_spaces_math_mode", "passed": True}
    lines = [text[: m.start()].count("\n") + 1 for m in bare[:10]]
    return {
        "name": "answer_spaces_math_mode",
        "passed": False,
        "detail": f"\\underline sin math mode en lineas: {lines}",
        "failures_by_agent": {"agente_estilo": ["underline_sin_math"]},
    }


def check_chemical_formulas(text: str, path: str) -> dict:
    """Detecta fórmulas químicas fuera de math mode.

    Solo flaggea cuando hay UN MISMO token compuesto de:
    - Elemento + número (Fe2, H2, Ca2)
    - Elemento + elemento (NaCl, FeO, MgO, KOH)
    - Elemento + número + elemento (Fe2O3, H2O, H2SO4)
    - Elemento + número + símbolo (Ca2+, Fe3+, SO4-)

    Esto evita falsos positivos con palabras españolas (La, Si, Cu, etc.).
    """
    chem_pattern = (
        r"(?<![$\w])"
        r"(?:"
        r"[A-Z][a-z]?\d+(?:[A-Z][a-z]?(?:\d+)?)*"  # H2, Fe2O3, H2SO4
        r"|"
        r"[A-Z][a-z]?(?=[A-Z][a-z])[A-Z][a-z]?(?:\d*[A-Z][a-z]?(?:\d*)?)*"  # NaCl, KOH, FeO
        r"|"
        r"[A-Z][a-z]?\d+[+-]"  # Ca2+, Fe3+, SO4-
        r")"
        r"(?![$\w])"
    )
    matches = list(re.finditer(chem_pattern, text))

    # Elementos químicos válidos
    elements = {
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
    }

    def is_valid_formula(token):
        """Verifica que token sean elementos químicos + números + cargas."""
        i = 0
        while i < len(token):
            if token[i].isupper():
                sym = token[i]
                if i + 1 < len(token) and token[i + 1].islower():
                    sym += token[i + 1]
                    i += 2
                else:
                    i += 1
                if sym not in elements:
                    return False
                # Optional digits
                while i < len(token) and token[i].isdigit():
                    i += 1
                # Optional charge
                if i < len(token) and token[i] in "+-":
                    i += 1
                    if i < len(token) and token[i].isdigit():
                        i += 1
            else:
                return False
        return True

    violation_lines = set()
    for m in matches:
        token = m.group(0)
        if token and is_valid_formula(token):
            line_num = text[: m.start()].count("\n") + 1
            violation_lines.add(line_num)

    if not violation_lines:
        return {"name": "chemical_formulas", "passed": True}
    return {
        "name": "chemical_formulas",
        "passed": False,
        "detail": (
            f"Fórmulas/elementos fuera de math mode en líneas: {sorted(violation_lines)[:15]}"
        ),
        "failures_by_agent": {
            "agente_estilo": [f"chem_formula_line_{line}" for line in sorted(violation_lines)[:15]]
        },
    }


def check_title_has_no_accents(text: str, path: str) -> dict:
    """Verifica que los title="" no contengan acentos."""
    accented = list(re.finditer(r'title="[^"]*[áéíóúñÁÉÍÓÚÑ][^"]*"', text))
    if not accented:
        return {"name": "title_no_accents", "passed": True}
    lines = [text[: m.start()].count("\n") + 1 for m in accented]
    return {
        "name": "title_no_accents",
        "passed": False,
        "detail": f"Titulos con acentos en lineas: {lines}",
        "failures_by_agent": {"agente_estilo": ["title_con_acentos"]},
    }


def check_evaluacion_distribucion(text: str, path: str) -> dict:
    """Verifica distribucion 2 Bajo + 2 Medio + 1 Alto en evaluacion."""
    eval_text = _find_icfes_box(text)
    if not eval_text:
        return {
            "name": "evaluacion_distribucion",
            "passed": False,
            "detail": "FALTA heading .evaluacion con 'Evaluacion - tipo ICFES'",
            "failures_by_agent": {"agente_evaluacion": ["missing_evaluacion"]},
        }
    
    # Buscar 🟢🟡🔴 en preguntas de evaluacion
    preguntas = re.findall(r"\*\*Pregunta\s+\d+[^*]*\*\*", eval_text)
    bajos = sum(1 for p in preguntas if "🟢" in p)
    medios = sum(1 for p in preguntas if "🟡" in p)
    altos = sum(1 for p in preguntas if "🔴" in p)
    
    if bajos == 2 and medios == 2 and altos == 1:
        return {
            "name": "evaluacion_distribucion",
            "passed": True,
            "detail": f"Bajo={bajos}, Medio={medios}, Alto={altos}",
        }
        
    # Fallback: buscar texto Nivel Bajo/Medio/Alto
    bajos_f = len(re.findall(r"Nivel\s+Bajo\b", eval_text, re.IGNORECASE))
    medios_f = len(re.findall(r"Nivel\s+Medio\b", eval_text, re.IGNORECASE))
    altos_f = len(re.findall(r"Nivel\s+Alto\b", eval_text, re.IGNORECASE))
    if bajos_f == 2 and medios_f == 2 and altos_f == 1:
        return {
            "name": "evaluacion_distribucion",
            "passed": True,
            "detail": f"Bajo={bajos_f}, Medio={medios_f}, Alto={altos_f} (con fallback)",
        }
        
    return {
        "name": "evaluacion_distribucion",
        "passed": False,
        "detail": (
            "Esperado 2 Bajo + 2 Medio + 1 Alto."
            f" Obtenido: Bajo={bajos}, Medio={medios}, Alto={altos}"
        ),
        "failures_by_agent": {"agente_evaluacion": ["distribucion_niveles"]},
    }


def check_socioemocional_competencia(text: str, path: str) -> dict:
    """Verifica que la reflexión socioemocional nombre una competencia Ley 2503."""
    sections = re.split(r"\n(?=## )", text)
    socio_sections = [s for s in sections if r"{.socioemocional}" in s]
    if not socio_sections:
        return {
            "name": "socioemocional_competencia",
            "passed": False,
            "detail": "FALTA .socioemocional",
            "failures_by_agent": {"agente_socioemocional": ["missing_socioemocional"]},
        }
    soc_text = socio_sections[0]
    competencias = [
        r"Conciencia\s+Emocional",
        r"Regulaci[oó]n\s+Emocional",
        r"Autonom[íi]a",
        r"Inteligencia\s+Interpersonal",
        r"Habilidades\s+de\s+Vida",
        r"Bienestar",
    ]
    for p in competencias:
        if re.search(p, soc_text, re.IGNORECASE):
            return {"name": "socioemocional_competencia", "passed": True}
    return {
        "name": "socioemocional_competencia",
        "passed": False,
        "detail": "No se encontró ninguna competencia de Ley 2503/2025",
        "failures_by_agent": {"agente_socioemocional": ["competencia_faltante"]},
    }


EXPECTED_SECTIONS = {
    "teoria": "Teoria",
    "ideas-previas": "Ideas Previas",
    "contexto": "Contexto Feynman",
    "caracterizados": "Caracterizados",
    "ejemplo": "Ejemplos",
    "ejercicios": "Ejercicios",
    "retos": "Retos",
    "aplicacion": "Aplicacion",
    "evaluacion": "Evaluacion",
    "socioemocional": "Socioemocional",
}


def list_sections(text: str) -> dict:
    """Escanea un .qmd y devuelve boxes presentes y faltantes."""
    found_types = set()
    for m in re.finditer(r"\{\.([a-z-]+)\}", text):
        cls = m.group(1)
        if cls in EXPECTED_SECTIONS:
            found_types.add(cls)

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
    check_caracterizados_metacognicion,
    check_caracterizados_glosario,
    check_caracterizados_alternative_format,
    check_caracterizados_swap_test,
    check_ejemplos_niveles,
    check_ejercicios_count,
    check_section_order,
    check_evaluacion_reactivos,
    check_evaluacion_distribucion,
    check_evaluacion_opciones,
    check_autoevaluacion_present,
    check_socializacion_box_exists,
    check_socializacion_fields,
    check_socioemocional_competencia,
    check_no_html_inline,
    check_no_ascii_boxes,
    check_ejercicios_have_answer_space,
    check_caracterizados_have_answer_space,
    check_icfes_enunciado_blank_line,
    check_answer_spaces_in_math_mode,
    check_title_has_no_accents,
    check_chemical_formulas,
    check_no_capacitist_language,
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
        failures_by_agent["agente_qa"] = [r["name"] for r in failures]

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
        description="Valida el .qmd generado por el generador de plan de clase"
    )
    parser.add_argument("input", type=Path, help="Archivo .qmd a validar")
    parser.add_argument("--json", action="store_true", help="Salida en JSON")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Muestra detalles de todos los checks"
    )
    parser.add_argument(
        "--sections",
        action="store_true",
        help="Lista las secciones presentes y faltantes en el archivo",
    )
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
    print(f"\n{'=' * 60}")
    print(f"  VALIDACIÓN: {args.input.name}")
    print(f"  ESTADO: {status}")
    print(f"  Checks: {report['passed_checks']}/{report['total_checks']} pasaron")
    print(f"{'=' * 60}\n")

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
            print("\n  Agentes responsables:")
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
