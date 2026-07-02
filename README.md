# MyST + Sphinx autodoc example

This repository is a complete, minimal example showing how to use
[MyST](https://myst-parser.readthedocs.io/) with
[Sphinx autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
to pull Python docstrings from `mymodule.py` into Markdown documentation pages.

## Files included

- `mymodule.py` - example module with documented functions and a class
- `docs/conf.py` - Sphinx configuration for MyST and autodoc
- `docs/index.md` - landing page with autodoc directives
- `docs/api.md` - API reference page with multiple autodoc examples
- `requirements.txt` - dependencies needed to build the docs

## Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Build the documentation

```bash
sphinx-build -b html docs docs/_build/html
```

After the build finishes, open `docs/_build/html/index.html` in a browser.

## What this example demonstrates

- `autofunction` for individual functions
- `autoclass` for classes and methods
- `automodule` for module-level API pages
- autodoc options such as `:members:`, `:undoc-members:`, and `:special-members:`

## Project layout

```text
.
├── docs
│   ├── api.md
│   ├── conf.py
│   └── index.md
├── mymodule.py
└── requirements.txt
```
