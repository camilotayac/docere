#!/usr/bin/env python3
"""Convierte PDF, DOCX o MD a Markdown plano para el generador de plan de clase.

Uso:
    python3 convert_input_to_md.py input/archivo.pdf -o input/texto_teorico.md
    python3 convert_input_to_md.py input/archivo.docx -o input/texto_teorico.md
    python3 convert_input_to_md.py input/archivo.md -o input/texto_teorico.md

Dependencias (instalar segun necesidad):
    pip install pymupdf       # para PDF
    pip install python-docx   # para DOCX
"""

import argparse
import sys
from pathlib import Path


def convert_pdf(path: Path) -> str:
    import fitz
    doc = fitz.open(str(path))
    text = []
    for page in doc:
        text.append(page.get_text())
    doc.close()
    return "\n\n".join(text)


def convert_docx(path: Path) -> str:
    from docx import Document
    doc = Document(str(path))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


def convert_md(path: Path) -> str:
    return path.read_text(encoding="utf-8")


CONVERTERS = {
    ".pdf": convert_pdf,
    ".docx": convert_docx,
    ".md": convert_md,
}


def main():
    parser = argparse.ArgumentParser(description="Convierte PDF/DOCX/MD a Markdown")
    parser.add_argument("input", type=Path, help="Archivo de entrada (.pdf, .docx, .md)")
    parser.add_argument("-o", "--output", type=Path, default=Path("input/texto_teorico.md"),
                        help="Ruta de salida (default: input/texto_teorico.md)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: el archivo '{args.input}' no existe.")
        sys.exit(1)

    ext = args.input.suffix.lower()
    if ext not in CONVERTERS:
        print(f"Error: formato '{ext}' no soportado. Usa .pdf, .docx o .md")
        sys.exit(1)

    print(f"Convirtiendo {args.input}...")
    text = CONVERTERS[ext](args.input)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"Listo. Salida: {args.output.resolve()}")


if __name__ == "__main__":
    main()
