from pathlib import Path

import pytest

from mymodule import Greeter, add_numbers, repeat_text


def test_add_numbers_returns_sum():
    assert add_numbers(2.5, 1.5) == 4.0


def test_repeat_text_repeats_with_separator():
    assert repeat_text("MyST", times=3, separator=" / ") == "MyST / MyST / MyST"


def test_repeat_text_rejects_non_positive_counts():
    with pytest.raises(ValueError, match="at least 1"):
        repeat_text("MyST", times=0)


def test_greeter_normalizes_names():
    greeter = Greeter("Welcome")

    assert greeter.greet("  ada lovelace ") == "Welcome, Ada Lovelace!"
    assert greeter.excited_greet("grace hopper") == "WELCOME, GRACE HOPPER!"


def test_docs_include_autodoc_directives():
    index_page = Path("docs/index.md").read_text(encoding="utf-8")
    api_page = Path("docs/api.md").read_text(encoding="utf-8")

    assert "```{autofunction} mymodule.add_numbers" in index_page
    assert "```{automodule} mymodule" in api_page
    assert ":undoc-members:" in api_page
