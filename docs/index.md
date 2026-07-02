# MyST + autodoc example

This page shows how MyST Markdown can embed Sphinx autodoc directives that read
Python docstrings directly from `mymodule.py`.

```{toctree}
:maxdepth: 2

api
```

## Individual function

```{autofunction} mymodule.add_numbers
```

## Class example

```{autoclass} mymodule.Greeter
:members:
```
