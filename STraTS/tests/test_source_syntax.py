from pathlib import Path


def test_all_source_modules_compile():
    """Catch syntax regressions without importing optional ML dependencies."""
    source_dir = Path(__file__).resolve().parents[1] / "src"
    for source_path in sorted(source_dir.glob("*.py")):
        compile(
            source_path.read_text(encoding="utf-8"),
            str(source_path),
            "exec",
        )
