# API reference

This page collects a few different autodoc patterns that work inside MyST
Markdown files.

## Entire module

```{automodule} mymodule
:members:
:undoc-members:
```

## One function at a time

```{autofunction} mymodule.repeat_text
```

## Class with method details

```{autoclass} mymodule.Greeter
:members:
:undoc-members:
:special-members: __init__
```
