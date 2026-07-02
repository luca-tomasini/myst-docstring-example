"""Sphinx configuration for the MyST autodoc example."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

project = "MyST docstring example"
author = "luca-tomasini"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
]

source_suffix = {
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = [
    "_build",
    "best_practices.md",
    "git_commands.md",
    "governance.md",
]

autoclass_content = "both"
html_theme = "alabaster"
