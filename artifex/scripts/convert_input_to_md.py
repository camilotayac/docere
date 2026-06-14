#!/usr/bin/env python3
"""Convierte PDF, DOCX, MD o TXT a Markdown plano para el generador de plan de clase.
La salida por defecto es input/texto_teorico.md relativo a artifex/.

Uso:
    python3 convert_input_to_md.py input/archivo.pdf -o input/texto_teorico.md
    python3 convert_input_to_md.py input/archivo.docx -o input/texto_teorico.md
    python3 convert_input_to_md.py input/archivo.md -o input/texto_teorico.md
    python3 convert_input_to_md.py input/archivo.txt -o input/texto_teorico.md

Dependencias (instalar segun necesidad):
    pip install pymupdf       # para PDF
    pip install python-docx   # para DOCX
"""

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from docere.pdf_utils import extract_text_from_pdf

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)


def convert_pdf(path: Path) -> str:
    try:
        return extract_text_from_pdf(str(path))
    except (ValueError, Exception) as e:
        log.error(str(e))
        sys.exit(1)


def convert_docx(path: Path) -> str:
    try:
        from docx import Document
    except ImportError:
        log.error("python-docx no instalado. Ejecuta: pip install python-docx")
        sys.exit(1)
    try:
        doc = Document(str(path))
    except Exception as e:
        log.error(f"Error al abrir DOCX: {e}")
        sys.exit(1)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    if not paragraphs:
        log.warning("El DOCX no contiene texto en parrafos")
    return "\n\n".join(paragraphs)


def convert_md(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        log.warning("UTF-8 fallo, intentando latin-1...")
        return path.read_text(encoding="latin-1")


def convert_txt(path: Path) -> str:
    return convert_md(path)


CONVERTERS = {
    ".pdf": convert_pdf,
    ".docx": convert_docx,
    ".md": convert_md,
    ".txt": convert_txt,
}

SUPPORTED = ", ".join(sorted(CONVERTERS))


def main():
    parser = argparse.ArgumentParser(description="Convierte PDF/DOCX/MD/TXT a Markdown")
    parser.add_argument("input", type=Path, help=f"Archivo de entrada ({SUPPORTED})")
    default_output = Path(__file__).parent.parent / "input" / "texto_teorico.md"
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=default_output,
        help="Ruta de salida (default: artifex/input/texto_teorico.md)",
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="Modo silencioso (solo errores)")
    args = parser.parse_args()

    if args.quiet:
        logging.getLogger().setLevel(logging.ERROR)

    if not args.input.exists():
        log.error(f"Archivo no encontrado: '{args.input}'")
        sys.exit(1)

    if not args.input.is_file():
        log.error(f"'{args.input}' no es un archivo regular")
        sys.exit(1)

    ext = args.input.suffix.lower()
    if ext not in CONVERTERS:
        log.error(f"Formato '{ext}' no soportado. Usa: {SUPPORTED}")
        sys.exit(1)

    log.info(f"Convirtiendo {args.input}...")
    text = CONVERTERS[ext](args.input)

    if not text.strip():
        log.warning("El texto convertido esta vacio")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    log.info(f"Listo. Salida: {args.output.resolve()}")


if __name__ == "__main__":
    main()
