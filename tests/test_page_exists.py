from pathlib import Path

PAGE = Path(__file__).resolve().parents[1] / "site" / "index.html"


def test_the_page_exists_and_is_html():
    text = PAGE.read_text(encoding="utf-8")
    assert text.lstrip().lower().startswith("<!doctype html>")
