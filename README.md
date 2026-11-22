# unitconv

A small Python library and command-line tool for converting lengths, masses and temperatures.

## Project summary (Part A)

| Item | Value |
|---|---|
| Purpose | Convert values between common length, mass and temperature units, both as a library and from the command line. |
| Programming language | Python (3.10+; developed and tested on 3.13.18) |
| Framework | None (standard library only: `argparse`) |
| Test framework | pytest 8.3.3 |
| Coverage tool | pytest-cov 5.0.0 (coverage.py) |
| Baseline version | 0.1.0 (`unitconv/__init__.py`) |
| Supported units | Length: mm, cm, m, km, in, ft, mi. Mass: mg, g, kg, oz, lb. Temperature: C, F, K. |

## Layout

```
unitconv/
  __init__.py      package version
  __main__.py      enables `python -m unitconv`
  cli.py           argparse command-line interface
  converter.py     conversion functions
tests/
  test_converter.py
  test_cli.py
requirements-dev.txt
```

## Local setup and tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q --cov=unitconv --cov-report=term
```

Example:

```bash
python -m unitconv 10 km mi
# 10 km = 6.21371 mi
```

## Baseline status

This is the untouched baseline before any quality improvements. Quality work (static analysis findings, refactoring, and re-analysis) will be made in later commits.
