from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures() -> Path:
    return FIXTURES


@pytest.fixture
def test_pdf() -> Path:
    return FIXTURES / "test_input.pdf"


@pytest.fixture
def test_md() -> Path:
    return FIXTURES / "test_input.md"


@pytest.fixture
def passing_qmd() -> Path:
    return FIXTURES / "passing.qmd"


@pytest.fixture
def failing_qmd() -> Path:
    return FIXTURES / "failing.qmd"


@pytest.fixture
def tmp_output(tmp_path: Path) -> Path:
    return tmp_path / "output.pdf"
