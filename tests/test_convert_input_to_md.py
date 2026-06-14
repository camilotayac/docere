"""Tests for artifex/scripts/convert_input_to_md.py."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "artifex" / "scripts" / "convert_input_to_md.py"


def _run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
    )


class TestConvertPDF:
    def test_pdf_to_md(self, test_pdf: Path, tmp_path: Path):
        out = tmp_path / "output.md"
        result = _run([str(test_pdf), "-o", str(out)])
        assert result.returncode == 0
        assert out.exists()
        content = out.read_text()
        assert "Pagina" in content
        assert "Quimica" in content

    def test_md_to_md(self, test_md: Path, tmp_path: Path):
        out = tmp_path / "output.md"
        result = _run([str(test_md), "-o", str(out)])
        assert result.returncode == 0
        assert out.exists()
        content = out.read_text()
        assert "Prueba" in content

    def test_output_dir_creado(self, test_pdf: Path, tmp_path: Path):
        nested = tmp_path / "sub" / "dir" / "out.md"
        result = _run([str(test_pdf), "-o", str(nested)])
        assert result.returncode == 0
        assert nested.exists()

    def test_default_output(self, test_pdf: Path):
        result = _run([str(test_pdf)])
        assert result.returncode == 0
        assert "Listo. Salida:" in result.stderr

    def test_error_archivo_inexistente(self):
        result = _run(["/no/existe.pdf"])
        assert result.returncode == 1
        assert "no encontrado" in result.stderr

    def test_error_formato_no_soportado(self, tmp_path: Path):
        fake = tmp_path / "test.xyz"
        fake.write_text("hola")
        result = _run([str(fake)])
        assert result.returncode == 1
        assert "no soportado" in result.stderr
