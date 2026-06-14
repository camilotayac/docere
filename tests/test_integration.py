"""Integration test: extraer -> convert -> validate."""

import json
import subprocess
import sys
from pathlib import Path

import fitz

EXTRACTION_SCRIPT = (
    Path(__file__).resolve().parent.parent / "Bibliotheca" / "scripts" / "extraer_pdf.py"
)
CONVERT_SCRIPT = (
    Path(__file__).resolve().parent.parent / "artifex" / "scripts" / "convert_input_to_md.py"
)
VALIDATE_SCRIPT = (
    Path(__file__).resolve().parent.parent / "artifex" / "scripts" / "validate_output.py"
)


def test_extraer_y_convertir(test_pdf: Path, tmp_path: Path):
    fragment = tmp_path / "fragmento.pdf"
    r1 = subprocess.run(
        [
            sys.executable,
            str(EXTRACTION_SCRIPT),
            "--libro",
            str(test_pdf),
            "--paginas",
            "1-2",
            "--output",
            str(fragment),
        ],
        capture_output=True,
        text=True,
    )
    assert r1.returncode == 0, r1.stderr
    assert fragment.exists()
    doc = fitz.open(str(fragment))
    assert doc.page_count == 2
    doc.close()

    md = tmp_path / "texto_teorico.md"
    r2 = subprocess.run(
        [sys.executable, str(CONVERT_SCRIPT), str(fragment), "-o", str(md)],
        capture_output=True,
        text=True,
    )
    assert r2.returncode == 0, r2.stderr
    assert md.exists()
    content = md.read_text()
    assert "Pagina" in content


def test_convertir_y_validar_passing(passing_qmd: Path):
    r = subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), str(passing_qmd), "--json"],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0
    report = json.loads(r.stdout)
    assert report["passed"] is True


def test_convertir_y_validar_failing(failing_qmd: Path):
    r = subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), str(failing_qmd), "--json"],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0
    report = json.loads(r.stdout)
    assert report["passed"] is False
