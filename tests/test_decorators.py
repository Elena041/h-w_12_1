import pytest

from src.decorators import log


def test_log_with_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=log_file)
    def test_function(x, y):
        return x + y

    test_function(1, 2)

    with open(log_file, "r") as file:
        content = file.read()
        assert "test_function ok" in content


def test_log_without_file(capsys):
    @log()
    def test_function(x, y):
        return x + y

    test_function(1, 2)

    captured = capsys.readouterr()
    assert "test_function ok\n" == captured.out


def test_log_error_with_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=log_file)
    def error_function(x, y):
        raise ValueError("Error!")

    with pytest.raises(ValueError):
        error_function(1, 2)

    with open(log_file, "r") as file:
        content = file.read()
        assert "error" in content
