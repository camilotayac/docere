#!/usr/bin/env python3
"""
Valida la calidad de las extracciones generadas por extraer.py.

Uso:
  python3 validar.py output/reactivo_limite/
  python3 validar.py output/reactivo_limite/ --tema "reactivo limite"

Salida JSON con puntuaciones de cada extracto y puntuación promedio.
"""

import argparse
import json
import pathlib
import re
import sys

import yaml


def extraer_keywords(tema):
    words = tema.lower().split()
    stopwords = {"el", "la", "los", "las", "de", "del", "en", "un", "una",
                 "y", "e", "o", "a", "para", "por", "con", "que", "es", "se"}
    return [w for w in words if w not in stopwords and len(w) > 1]


def validar(output_dir, tema=None):
    output_path = pathlib.Path(output_dir)

    resumen_path = output_path / "resultados.json"
    resumen = None
    if resumen_path.exists():
        with open(resumen_path, "r", encoding="utf-8") as f:
            resumen = json.load(f)

    if tema is None and resumen:
        tema = resumen.get("tema", "")

    keywords = extraer_keywords(tema) if tema else []

    md_files = sorted(output_path.glob("extracto_*.md"))
    if not md_files:
        return {"error": "No se encontraron archivos .md en el directorio",
                "directorio": str(output_path)}

    validaciones = []

    for md_path in md_files:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        md_metadata = {}
        md_body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    md_metadata = yaml.safe_load(parts[1]) or {}
                except Exception:
                    md_metadata = {}
                md_body = parts[2]

        body_lower = md_body.lower()
        detalles = {}

        if keywords:
            found = sum(1 for kw in keywords if kw in body_lower)
            detalles["cobertura_keywords"] = round(found / len(keywords), 3)
        else:
            detalles["cobertura_keywords"] = 0.5

        char_count = len(md_body.strip())
        detalles["longitud_caracteres"] = char_count
        detalles["score_longitud"] = round(min(1.0, char_count / 800), 3)

        img_count = md_body.count("_[imagen]_")
        detalles["imagenes"] = img_count

        page_count = len(md_metadata.get("fuente", {}).get("paginas", []))
        detalles["paginas_extraidas"] = page_count

        puntuacion = (
            detalles["cobertura_keywords"] * 0.5 +
            detalles["score_longitud"] * 0.3 +
            min(1.0, page_count / 5) * 0.1 +
            (0 if img_count > page_count * 2 else 0.1)
        )
        puntuacion = round(min(1.0, max(0.0, puntuacion)), 3)

        validaciones.append({
            "archivo": md_path.name,
            "puntuacion": puntuacion,
            "detalles": detalles,
            "metadata": {
                "libro": md_metadata.get("fuente", {}).get("libro", "?"),
                "paginas": md_metadata.get("fuente", {}).get("paginas", []),
                "materia": md_metadata.get("fuente", {}).get("materia", "?"),
                "idioma": md_metadata.get("fuente", {}).get("idioma", "?"),
            }
        })

    promedio = round(sum(v["puntuacion"] for v in validaciones) / len(validaciones), 3)

    resultado = {
        "tema": tema,
        "directorio": str(output_path),
        "total_archivos": len(validaciones),
        "puntuacion_promedio": promedio,
        "valido": promedio >= 0.6,
        "validaciones": validaciones,
    }

    with open(output_path / "validacion.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    return resultado


def main():
    parser = argparse.ArgumentParser(
        description="Valida la calidad de las extracciones")
    parser.add_argument("directorio", help="Directorio de salida de extraer.py")
    parser.add_argument("--tema", "-t", help="Tema buscado (para validar keywords)")
    parser.add_argument("--umbral", "-u", type=float, default=0.6,
                        help="Umbral mínimo de puntuación (default: 0.6)")
    args = parser.parse_args()

    resultado = validar(args.directorio, args.tema)
    if "error" in resultado:
        print(f"Error: {resultado['error']}")
        sys.exit(1)

    print(f"\nValidación de: {args.directorio}")
    print(f"Tema: {resultado['tema'] or 'N/E'}")
    print(f"Archivos: {resultado['total_archivos']}")
    print(f"Puntuación promedio: {resultado['puntuacion_promedio']}")
    print(f"Válido: {'✅' if resultado['valido'] else '❌'} (umbral: {args.umbral})\n")

    for v in resultado["validaciones"]:
        status = "✅" if v["puntuacion"] >= args.umbral else "⚠️"
        print(f"  {status} [{v['puntuacion']}] {v['archivo']}")
        print(f"       Libro: {v['metadata']['libro'][:60]}")
        print(f"       Keywords: {v['detalles']['cobertura_keywords']} | "
              f"Long: {v['detalles']['score_longitud']}")

    print("\n---JSON_START---")
    print(json.dumps(resultado))
    print("---JSON_END---")


if __name__ == "__main__":
    main()
