#!/usr/bin/env python3
"""
Busca un tema en los libros de la biblioteca y extrae las secciones relevantes
como PDF exacto + Markdown con metadatos.

Uso:
  python3 extraer.py --tema "reactivo limite"
  python3 extraer.py --tema "reactivo limite" --materia Química
  python3 extraer.py --list-libros
  python3 extraer.py (modo interactivo)

Salida en output/<tema>/:
  extracto_NNN_libro_pag_ini-fin.pdf
  extracto_NNN_libro_pag_ini-fin.md
  resultados.json
"""

import argparse
import json
import os
import re
import sys
import pathlib
from datetime import date

import fitz
import yaml


# Silence MuPDF C-level stderr noise (CSS parse errors from EPUBs)
_DEVNULL_FD = os.open(os.devnull, os.O_WRONLY)
os.dup2(_DEVNULL_FD, 2)
os.close(_DEVNULL_FD)


BIBLIOTECA_DIR = pathlib.Path(__file__).parent.parent.resolve()
MATERIAS = ["Física", "Química", "Biología", "Matemáticas", "Computación", "Filosofía"]
OUTPUT_DIR = BIBLIOTECA_DIR.parent / "artifex" / "input"
CONTEXTO_DEFAULT = 3
EXTENSIONES = (".pdf", ".epub")
MAX_RESULTADOS_DEFAULT = 0  # 0 = sin límite


def buscar_en_libro(path, query, contexto=CONTEXTO_DEFAULT):
    doc = fitz.open(str(path))
    if doc.page_count == 0:
        doc.close()
        return [], "Documento vacío"

    paginas_match = []
    query_lower = query.lower()
    for i in range(doc.page_count):
        try:
            text = doc[i].get_text("text")
            if query_lower in text.lower():
                paginas_match.append(i)
        except Exception:
            continue

    if not paginas_match:
        doc.close()
        return [], None

    grupos = []
    grupo_actual = [paginas_match[0]]
    for i in range(1, len(paginas_match)):
        if paginas_match[i] - paginas_match[i-1] <= contexto * 2:
            grupo_actual.append(paginas_match[i])
        else:
            grupos.append(grupo_actual)
            grupo_actual = [paginas_match[i]]
    grupos.append(grupo_actual)

    secciones = []
    for g in grupos:
        inicio = max(0, g[0] - contexto)
        fin = min(doc.page_count - 1, g[-1] + contexto)
        secciones.append({
            "paginas": list(range(inicio, fin + 1)),
            "paginas_match": g,
        })

    doc.close()
    return secciones, None


def extraer_pdf(origen, paginas, destino):
    doc = fitz.open(str(origen))
    nuevo = fitz.open()
    try:
        nuevo.insert_pdf(doc, from_page=paginas[0], to_page=paginas[-1])
    except Exception:
        for p in paginas:
            page = doc[p]
            pix = page.get_pixmap(dpi=150)
            img_bytes = pix.tobytes("png")
            img_page = nuevo.new_page(width=pix.width, height=pix.height)
            img_page.insert_image(img_page.rect, stream=img_bytes)
    nuevo.save(str(destino))
    nuevo.close()
    doc.close()


def extraer_texto_para_md(origen, paginas):
    doc = fitz.open(str(origen))
    contenido_paginas = []
    for num in paginas:
        page = doc[num]
        blocks = page.get_text("dict")["blocks"]
        bloque_textos = []
        for block in blocks:
            if block["type"] == 0:
                lineas = []
                for line in block["lines"]:
                    texto_linea = ""
                    for span in line["spans"]:
                        t = span["text"]
                        font = span.get("font", "")
                        if "Courier" in font or "Mono" in font or "mono" in font.lower():
                            t = f"`{t}`"
                        if "Bold" in font:
                            t = f"**{t}**"
                        if "Italic" in font or "Oblique" in font:
                            t = f"*{t}*"
                        texto_linea += t
                    lineas.append(texto_linea)
                bloque_textos.append(" ".join(lineas))
            elif block["type"] == 1:
                bloque_textos.append("_[imagen]_")
        contenido_paginas.append("\n\n".join(bloque_textos))
    doc.close()
    return contenido_paginas


def normalizar_tema(tema):
    tema = tema.strip().lower()
    tema = re.sub(r'[^\w\s-]', '', tema)
    tema = re.sub(r'[\s_]+', '_', tema)
    return tema[:60]


def abreviar_libro(path):
    nombre = path.stem
    nombre = re.sub(r'^\[.*?\]\s*', '', nombre)
    nombre = re.sub(r'\s*[-–—]\s*libgen.*$', '', nombre)
    nombre = re.sub(r'\{.*?\}', '', nombre)
    nombre = re.sub(r'\s*\[.*?\]', '', nombre)
    nombre = re.sub(r'\s+', ' ', nombre).strip()
    if len(nombre) > 45:
        nombre = nombre[:45]
    return nombre


def generar_md(destino, metadatos, textos_paginas):
    with open(destino, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(metadatos, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        src = metadatos["fuente"]
        f.write(f"# {metadatos['tema']}\n\n")
        f.write(f"- **Libro:** {src['libro']}\n")
        f.write(f"- **Materia:** {src['materia']}\n")
        f.write(f"- **Idioma:** {src.get('idioma', 'N/E')}\n")
        f.write(f"- **Páginas:** {src['paginas'][0]}–{src['paginas'][-1]} ({len(src['paginas'])} págs)\n")
        f.write(f"- **Query:** `{metadatos['extraccion']['query']}`\n")
        f.write(f"- **Iteración:** {metadatos['extraccion']['iteracion']}\n\n")
        f.write("---\n\n")
        for i, (num, texto) in enumerate(zip(src["paginas"], textos_paginas)):
            f.write(f"### Página {num}\n\n")
            f.write(texto.strip() if texto.strip() else "_(sin texto extraíble)_")
            f.write("\n\n")


def escanear_biblioteca(materia_filtrar=None, skip_epub=False):
    libros = []
    exts = [".pdf"] if skip_epub else EXTENSIONES
    for materia in MATERIAS:
        if materia_filtrar and materia != materia_filtrar:
            continue
        materia_path = BIBLIOTECA_DIR / materia
        if not materia_path.exists():
            continue

        encontrados = set()

        for idioma in ["Español", "English"]:
            idioma_path = materia_path / idioma
            if not idioma_path.exists():
                continue
            for ext in exts:
                for libro_path in sorted(idioma_path.glob(f"*{ext}")):
                    if libro_path not in encontrados:
                        encontrados.add(libro_path)
                        libros.append({
                            "ruta": libro_path,
                            "materia": materia,
                            "idioma": idioma,
                            "nombre": libro_path.name,
                        })

        for ext in exts:
            for libro_path in sorted(materia_path.glob(f"*{ext}")):
                if libro_path not in encontrados:
                    encontrados.add(libro_path)
                    libros.append({
                        "ruta": libro_path,
                        "materia": materia,
                        "idioma": "N/E",
                        "nombre": libro_path.name,
                    })
    return libros


def procesar(tema, materia=None, contexto=CONTEXTO_DEFAULT,
             output_dir=None, iteracion=1, query_override=None,
             max_resultados=0, skip_epub=False):
    query = query_override if query_override else tema
    output_dir = output_dir or OUTPUT_DIR
    tema_folder = output_dir / normalizar_tema(tema)
    tema_folder.mkdir(parents=True, exist_ok=True)

    libros = escanear_biblioteca(materia, skip_epub)

    resultados = []
    errores = []
    contador = 0

    for libro in libros:
        if max_resultados > 0 and contador >= max_resultados:
            break
        path = libro["ruta"]
        secciones, error = buscar_en_libro(path, query, contexto)
        if error:
            errores.append({"libro": str(path), "error": error})
            continue
        if not secciones:
            continue

        libro_abrev = abreviar_libro(path)
        for sec in secciones:
            if max_resultados > 0 and contador >= max_resultados:
                break
            contador += 1
            paginas = sec["paginas"]
            pag_str = f"p{paginas[0]+1}-{paginas[-1]+1}"
            eid = f"{contador:03d}"

            pdf_name = f"extracto_{eid}_{libro_abrev}_{pag_str}.pdf"
            md_name = f"extracto_{eid}_{libro_abrev}_{pag_str}.md"
            pdf_path = tema_folder / pdf_name
            md_path = tema_folder / md_name

            extraer_pdf(path, paginas, pdf_path)
            textos = extraer_texto_para_md(path, paginas)

            metadatos = {
                "id": contador,
                "tema": tema,
                "fuente": {
                    "libro": libro["nombre"],
                    "ruta": str(path.relative_to(BIBLIOTECA_DIR)),
                    "paginas": [p + 1 for p in paginas],
                    "paginas_match": [p + 1 for p in sec["paginas_match"]],
                    "materia": libro["materia"],
                    "idioma": libro["idioma"],
                },
                "extraccion": {
                    "fecha": str(date.today()),
                    "query": query,
                    "contexto_paginas": contexto,
                    "iteracion": iteracion,
                },
                "calidad": {
                    "puntuacion": None,
                    "validado_por": None,
                },
            }

            generar_md(md_path, metadatos, textos)

            resultados.append({
                "id": contador,
                "pdf": pdf_name,
                "md": md_name,
                "libro": libro["nombre"],
                "materia": libro["materia"],
                "paginas": [p + 1 for p in paginas],
                "paginas_match": [p + 1 for p in sec["paginas_match"]],
            })

    resumen = {
        "tema": tema,
        "query": query,
        "materia_filtro": materia,
        "iteracion": iteracion,
        "total_extracciones": contador,
        "libros_procesados": len(libros),
        "resultados": resultados,
        "errores": errores,
    }

    with open(tema_folder / "resultados.json", "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=2, ensure_ascii=False)

    return resumen


def main():
    parser = argparse.ArgumentParser(
        description="Busca un tema en los libros y extrae secciones como PDF + MD")
    parser.add_argument("--tema", "-t", help="Tema a buscar")
    parser.add_argument("--materia", "-m", help="Filtrar por materia")
    parser.add_argument("--contexto", "-c", type=int, default=CONTEXTO_DEFAULT)
    parser.add_argument("--output-dir", "-o", default=str(OUTPUT_DIR))
    parser.add_argument("--iteracion", "-i", type=int, default=1)
    parser.add_argument("--query", "-q", help="Query de búsqueda (si difiere del tema)")
    parser.add_argument("--max-resultados", "-n", type=int, default=0,
                        help="Máximo de secciones a extraer (0 = sin límite)")
    parser.add_argument("--skip-epub", action="store_true",
                        help="Omitir archivos EPUB (más rápido, solo PDF)")
    parser.add_argument("--list-libros", action="store_true",
                        help="Listar libros disponibles")

    args = parser.parse_args()
    output_dir = pathlib.Path(args.output_dir)

    if args.list_libros:
        libros = escanear_biblioteca(args.materia, args.skip_epub)
        print(f"\nLibros disponibles ({len(libros)}):\n")
        for lib in sorted(libros, key=lambda x: (x["materia"], x["idioma"], x["nombre"])):
            print(f"  [{lib['materia']}/{lib['idioma']}] {lib['nombre']}")
        print()
        return

    tema = args.tema
    if not tema:
        print("=== EXTRACTOR DE LIBROS ===\n")
        tema = input("Tema a buscar: ").strip()
        if not tema:
            print("Tema requerido.")
            return
        m = input("Materia (opcional, Enter = todas): ").strip()
        args.materia = m if m else None
        c = input(f"Contexto en páginas [default {CONTEXTO_DEFAULT}]: ").strip()
        if c:
            args.contexto = int(c)

    print(f"\nBuscando «{tema}» en los libros...\n")
    resumen = procesar(tema=tema, materia=args.materia, contexto=args.contexto,
                       output_dir=output_dir, iteracion=args.iteracion,
                       query_override=args.query,
                       max_resultados=args.max_resultados,
                       skip_epub=args.skip_epub)

    print(f"Resultados: {resumen['total_extracciones']} sección(es) extraída(s)")
    for r in resumen["resultados"]:
        print(f"  [{r['id']}] {r['materia']} › {r['libro'][:60]} — págs {r['paginas'][0]}-{r['paginas'][-1]}")

    if resumen["errores"]:
        print(f"\nErrores ({len(resumen['errores'])}):")
        for e in resumen["errores"]:
            print(f"  - {e['libro']}: {e['error']}")

    output_rel = output_dir / normalizar_tema(tema)
    print(f"\n📁 {output_rel}/\n")

    print("---JSON_START---")
    print(json.dumps({
        "tema": tema,
        "query": resumen["query"],
        "output_dir": str(output_rel),
        "total": resumen["total_extracciones"],
        "resultados": [{ "id": r["id"], "archivo": r["md"], "materia": r["materia"], "libro": r["libro"] }
                       for r in resumen["resultados"]],
    }))
    print("---JSON_END---")


if __name__ == "__main__":
    main()
