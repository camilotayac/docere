"""Utility functions for PDF processing shared across Bibliotheca and Artifex."""

import contextlib
import logging
import os

import fitz

log = logging.getLogger(__name__)


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


def open_pdf(path: str) -> fitz.Document:
    """Open a PDF with MuPDF stderr suppressed."""
    with _silenciar_mupdf():
        return fitz.open(path)


def extract_text_from_pdf(path: str) -> str:
    """Extract all text from a PDF, returning as Markdown-style plain text."""
    try:
        doc = open_pdf(path)
    except Exception as e:
        log.error(f"Error al abrir PDF: {e}")
        raise

    if doc.page_count == 0:
        doc.close()
        log.error("PDF vacio (0 paginas)")
        raise ValueError("PDF vacio")

    text = []
    for i, page in enumerate(doc):
        try:
            page_text = page.get_text()
            if page_text.strip():
                text.append(page_text)
        except Exception as e:
            log.warning(f"Error extrayendo pagina {i + 1}: {e}")

    doc.close()

    if not text:
        log.error("No se pudo extraer texto del PDF (posiblemente escaneado)")
        raise ValueError("PDF sin texto extraible")

    return "\n\n".join(text)


def parsear_paginas(expr: str) -> list[tuple[int, int]]:
    """Convierte '1,3-5,7' en [(1,1), (3,5), (7,7)]."""
    rangos = []
    for parte in expr.split(","):
        parte = parte.strip()
        if not parte:
            continue
        if "-" in parte:
            partes = parte.split("-", 1)
            try:
                inicio, fin = int(partes[0]), int(partes[1])
            except ValueError:
                log.error(f"Rango invalido: {parte}")
                raise
            if inicio < 1 or fin < 1 or fin < inicio:
                log.error(f"Rango invalido: {parte} (debe ser 1-indexed, inicio <= fin)")
                raise ValueError(f"Rango invalido: {parte}")
            rangos.append((inicio, fin))
        else:
            try:
                pag = int(parte)
            except ValueError:
                log.error(f"Pagina invalida: {parte}")
                raise
            if pag < 1:
                log.error(f"Pagina invalida: {pag} (debe ser >= 1)")
                raise ValueError(f"Pagina invalida: {parte}")
            rangos.append((pag, pag))
    if not rangos:
        log.error("No se especificaron paginas validas")
        raise ValueError("Sin paginas validas")
    return rangos
