"""Tests for Bibliotheca/scripts/extraer_pdf.py."""

import subprocess
import sys
from pathlib import Path

import fitz

SCRIPT = Path(__file__).resolve().parent.parent / "Bibliotheca" / "scripts" / "extraer_pdf.py"


def _run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
    )


class TestExtraerPaginas:
    def test_extraer_rango_simple(self, test_pdf: Path, tmp_output: Path):
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "1-1",
                "--output",
                str(tmp_output),
            ]
        )
        assert result.returncode == 0
        assert tmp_output.exists()
        doc = fitz.open(str(tmp_output))
        assert doc.page_count == 1
        doc.close()

    def test_extraer_multiple_rangos(self, test_pdf: Path, tmp_output: Path):
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "1-1,3-3",
                "--output",
                str(tmp_output),
            ]
        )
        assert result.returncode == 0
        doc = fitz.open(str(tmp_output))
        assert doc.page_count == 2
        doc.close()

    def test_extraer_pagina_unica(self, test_pdf: Path, tmp_output: Path):
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "2",
                "--output",
                str(tmp_output),
            ]
        )
        assert result.returncode == 0
        doc = fitz.open(str(tmp_output))
        assert doc.page_count == 1
        doc.close()

    def test_output_dir_creado(self, test_pdf: Path, tmp_path: Path):
        nested = tmp_path / "sub" / "dir" / "out.pdf"
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "1-2",
                "--output",
                str(nested),
            ]
        )
        assert result.returncode == 0
        assert nested.exists()

    def test_error_libro_inexistente(self):
        result = _run(
            [
                "--libro",
                "/no/existe.pdf",
                "--paginas",
                "1-1",
                "--output",
                "/tmp/out.pdf",
            ]
        )
        assert result.returncode == 1
        assert "no encontrado" in result.stderr

    def test_error_rango_invalido_texto(self, test_pdf: Path, tmp_output: Path):
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "abc-def",
                "--output",
                str(tmp_output),
            ]
        )
        assert result.returncode == 1
        assert "invalido" in result.stderr

    def test_error_rango_invertido(self, test_pdf: Path, tmp_output: Path):
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "5-3",
                "--output",
                str(tmp_output),
            ]
        )
        assert result.returncode == 1
        assert "invalido" in result.stderr

    def test_error_pagina_negativa(self, test_pdf: Path, tmp_output: Path):
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "-1",
                "--output",
                str(tmp_output),
            ]
        )
        assert result.returncode == 1
        assert "invalida" in result.stderr or "invalido" in result.stderr

    def test_mensaje_exito(self, test_pdf: Path, tmp_output: Path):
        result = _run(
            [
                "--libro",
                str(test_pdf),
                "--paginas",
                "2-3",
                "--output",
                str(tmp_output),
            ]
        )
        assert result.returncode == 0
        assert "Extraidas" in result.stderr
        assert str(tmp_output) in result.stderr
