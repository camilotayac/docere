#!/usr/bin/env python3
"""
Extrae un rango de páginas de un PDF como un nuevo PDF fragmento.

Uso:
  python3 extraer_pdf.py --libro "Chang.pdf" --paginas 164-169 --output "CONT_001.pdf"
  python3 extraer_pdf.py --libro "Chang.pdf" --paginas 331-334 --output "PREG_001.pdf"

Salida: PDF fragmento con solo las páginas solicitadas.
"""

import argparse
import contextlib
import os
import pathlib
import sys

import fitz


@contextlib.contextmanager
def _silenciar_mupdf():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    os.dup2(devnull, 2)
    os.close(devnull)
    try:
        yield
    finally:
        os.dup2(old_stderr, 2)
        os.close(old_stderr)


def extraer_paginas(libro_path, rangos, output_path):
    output_path = pathlib.Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with _silenciar_mupdf():
        doc = fitz.open(str(libro_path))
        if doc.page_count == 0:
            doc.close()
            print("Error: documento vacío", file=sys.stderr)
            sys.exit(1)

        nuevo = fitz.open()
        for inicio, fin in rangos:
            p0 = max(0, min(inicio - 1, doc.page_count - 1))
            p1 = max(p0, min(fin - 1, doc.page_count - 1))
            try:
                nuevo.insert_pdf(doc, from_page=p0, to_page=p1)
            except Exception:
                for p in range(p0, p1 + 1):
                    page = doc[p]
                    pix = page.get_pixmap(dpi=150)
                    img_bytes = pix.tobytes("png")
                    img_page = nuevo.new_page(width=pix.width, height=pix.height)
                    img_page.insert_image(img_page.rect, stream=img_bytes)

        nuevo.save(str(output_path))
        nuevo.close()
        doc.close()

    total = sum(fin - inicio + 1 for inicio, fin in rangos)
    print(f"✓ Extraídas {total} páginas → {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Extrae páginas de un PDF como PDF fragmento")
    parser.add_argument("--libro", "-l", required=True,
                        help="Ruta al PDF original")
    parser.add_argument("--paginas", "-p", nargs="+", required=True,
                        help='Rangos 1-indexed: 164-169 331-334')
    parser.add_argument("--output", "-o", required=True,
                        help="Ruta del PDF de salida")

    args = parser.parse_args()

    libro_path = pathlib.Path(args.libro)
    if not libro_path.exists():
        print(f"Error: archivo no encontrado: {libro_path}", file=sys.stderr)
        sys.exit(1)

    rangos = []
    for p in args.paginas:
        if "-" in p:
            partes = p.split("-", 1)
            try:
                inicio, fin = int(partes[0]), int(partes[1])
            except ValueError:
                print(f"Error: rango inválido: {p}", file=sys.stderr)
                sys.exit(1)
            if inicio < 1 or fin < 1 or fin < inicio:
                print(f"Error: rango inválido: {p}", file=sys.stderr)
                sys.exit(1)
            rangos.append((inicio, fin))
        else:
            try:
                pag = int(p)
            except ValueError:
                print(f"Error: página inválida: {p}", file=sys.stderr)
                sys.exit(1)
            if pag < 1:
                print(f"Error: página inválida: {p}", file=sys.stderr)
                sys.exit(1)
            rangos.append((pag, pag))

    extraer_paginas(libro_path, rangos, args.output)


if __name__ == "__main__":
    main()
