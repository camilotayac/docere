"""Tests for artifex/scripts/validate_output.py."""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "artifex" / "scripts" / "validate_output.py"


def _run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
    )


class TestValidateOutput:
    def test_passing_qmd(self, passing_qmd: Path):
        result = _run([str(passing_qmd)])
        assert result.returncode == 0
        assert "APROBADO" in result.stdout

    def test_failing_qmd(self, failing_qmd: Path):
        result = _run([str(failing_qmd)])
        assert result.returncode == 1
        assert "REQUIERE CORRECCIONES" in result.stdout

    def test_json_output(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        assert result.returncode == 0
        report = json.loads(result.stdout)
        assert "passed" in report
        assert "total_checks" in report
        assert "checks" in report
        assert report["passed"] is True

    def test_json_output_failing(self, failing_qmd: Path):
        result = _run([str(failing_qmd), "--json"])
        assert result.returncode == 0
        report = json.loads(result.stdout)
        assert report["passed"] is False
        assert report["failed_checks"] > 0

    def test_verbose_output(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--verbose"])
        assert result.returncode == 0
        assert "box_balance" in result.stdout

    def test_sections_output(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--sections"])
        assert result.returncode == 0
        sections = json.loads(result.stdout)
        assert "present" in sections
        assert "missing" in sections
        assert "teoria-box" in sections["present"]

    def test_sections_failing(self, failing_qmd: Path):
        result = _run([str(failing_qmd), "--sections"])
        assert result.returncode == 0
        sections = json.loads(result.stdout)
        assert "teoria-box" in sections["present"]
        assert "ejemplo-box" in sections["missing"]

    def test_error_input_not_found(self):
        result = _run(["/no/existe.qmd"])
        assert result.returncode == 1
        assert "Error" in result.stderr or "Error" in result.stdout


class TestValidateIndividualChecks:
    def test_box_balance_passing(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        report = json.loads(result.stdout)
        box_check = next(c for c in report["checks"] if c["name"] == "box_balance")
        assert box_check["passed"] is True

    def test_all_boxes_present(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        report = json.loads(result.stdout)
        check = next(c for c in report["checks"] if c["name"] == "all_boxes_present")
        assert check["passed"] is True

    def test_teacher_notes_detected(self, failing_qmd: Path):
        result = _run([str(failing_qmd), "--json"])
        report = json.loads(result.stdout)
        check = next(c for c in report["checks"] if c["name"] == "no_teacher_notes")
        assert check["passed"] is False

    def test_caracterizados_count(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        report = json.loads(result.stdout)
        check = next(c for c in report["checks"] if c["name"] == "caracterizados_count")
        assert check["passed"] is True

    def test_ejemplos_niveles(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        report = json.loads(result.stdout)
        check = next(c for c in report["checks"] if c["name"] == "ejemplos_niveles")
        assert check["passed"] is True

    def test_evaluacion_reactivos(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        report = json.loads(result.stdout)
        check = next(c for c in report["checks"] if c["name"] == "evaluacion_reactivos")
        assert check["passed"] is True

    def test_socializacion_box_exists(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        report = json.loads(result.stdout)
        check = next(c for c in report["checks"] if c["name"] == "socializacion_box_exists")
        assert check["passed"] is True

    def test_socioemocional_competencia(self, passing_qmd: Path):
        result = _run([str(passing_qmd), "--json"])
        report = json.loads(result.stdout)
        check = next(c for c in report["checks"] if c["name"] == "socioemocional_competencia")
        assert check["passed"] is True

    def test_failures_by_agent(self, failing_qmd: Path):
        result = _run([str(failing_qmd), "--json"])
        report = json.loads(result.stdout)
        assert "failures_by_agent" in report
        assert len(report["failures_by_agent"]) > 0
