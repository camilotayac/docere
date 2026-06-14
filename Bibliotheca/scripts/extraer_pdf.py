#!/usr/bin/env python3
"""
Extrae rangos de paginas de un PDF como un nuevo PDF fragmento.

Uso:
  python3 extraer_pdf.py --libro "Chang.pdf" --paginas 164-169 --output "CONT_001.pdf"
  python3 extraer_pdf.py --libro "Chang.pdf" --paginas 331-334 --output "PREG_001.pdf"
  python3 extraer_pdf.py --libro "Chang.pdf" --paginas 1,3-5,7 --output "mezcla.pdf"

Salida: PDF fragmento con solo las paginas solicitadas.
"""

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from docere.pdf_utils import _silenciar_mupdf, parsear_paginas

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)


def extraer_paginas(libro_path, rangos, output_path, dpi=150):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with _silenciar_mupdf():
        import fitz

        doc = fitz.open(str(libro_path))
        if doc.page_count == 0:
            doc.close()
            log.error("Documento vacio (0 paginas)")
            sys.exit(1)

        num_paginas = doc.page_count
        nuevo = fitz.open()
        for inicio, fin in rangos:
            p0 = max(0, min(inicio - 1, num_paginas - 1))
            p1 = max(p0, min(fin - 1, num_paginas - 1))
            if p0 > p1:
                log.warning(f"Rango {inicio}-{fin} fuera de los limites ({num_paginas} paginas)")
                continue
            try:
                nuevo.insert_pdf(doc, from_page=p0, to_page=p1)
            except Exception as e:
                log.warning(f"Insercion directa fallo ({e}), usando rasterizado...")
                for p in range(p0, p1 + 1):
                    page = doc[p]
                    pix = page.get_pixmap(dpi=dpi)
                    img_bytes = pix.tobytes("png")
                    img_page = nuevo.new_page(width=pix.width, height=pix.height)
                    img_page.insert_image(img_page.rect, stream=img_bytes)

        total_extraidas = nuevo.page_count
        if total_extraidas == 0:
            nuevo.close()
            doc.close()
            log.error("No se pudo extraer ninguna pagina")
            sys.exit(1)

        nuevo.save(str(output_path))
        nuevo.close()
        doc.close()

    log.info(f"Extraidas {total_extraidas} paginas → {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Extrae paginas de un PDF como PDF fragmento")
    parser.add_argument("--libro", "-l", required=True, help="Ruta al PDF original")
    parser.add_argument(
        "--paginas",
        "-p",
        required=True,
        help='Rangos 1-indexed: "164-169", "1,3-5,7", "164-169 331-334"',
    )
    parser.add_argument("--output", "-o", required=True, help="Ruta del PDF de salida")
    parser.add_argument(
        "--dpi", type=int, default=150, help="DPI para rasterizado de fallback (default: 150)"
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="Modo silencioso")

    args = parser.parse_args()

    if args.quiet:
        logging.getLogger().setLevel(logging.ERROR)

    libro_path = Path(args.libro)
    if not libro_path.exists():
        log.error(f"Archivo no encontrado: {libro_path}")
        sys.exit(1)

    if not libro_path.suffix.lower() == ".pdf":
        log.warning(f"El archivo '{libro_path}' no tiene extension .pdf")

    try:
        rangos = parsear_paginas(args.paginas)
    except (ValueError, SystemExit):
        sys.exit(1)

    extraer_paginas(libro_path, rangos, args.output, dpi=args.dpi)


if __name__ == "__main__":
    main()
