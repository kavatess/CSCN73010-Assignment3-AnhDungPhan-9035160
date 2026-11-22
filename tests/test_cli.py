from unitconv.cli import main


def test_cli_success(capsys):
    assert main(["10", "km", "mi"]) == 0
    assert "mi" in capsys.readouterr().out


def test_cli_error_returns_nonzero(capsys):
    assert main(["1", "m", "kg"]) == 1
    assert "error" in capsys.readouterr().err
