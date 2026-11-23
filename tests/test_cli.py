import pytest

from unitconv.cli import main


def test_cli_success(capsys):
    assert main(["10", "km", "mi"]) == 0
    assert "mi" in capsys.readouterr().out


def test_cli_error_returns_nonzero(capsys):
    assert main(["1", "m", "kg"]) == 1
    assert "error" in capsys.readouterr().err


def test_cli_rejects_below_absolute_zero(capsys):
    assert main(["-300", "C", "K"]) == 1
    assert "absolute zero" in capsys.readouterr().err


def test_module_entry_point_runs():
    import runpy

    with pytest.raises(SystemExit) as exc:
        import sys

        old = sys.argv
        sys.argv = ["unitconv", "1", "m", "cm"]
        try:
            runpy.run_module("unitconv", run_name="__main__")
        finally:
            sys.argv = old
    assert exc.value.code == 0
