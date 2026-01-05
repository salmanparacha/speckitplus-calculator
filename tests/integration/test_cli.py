"""Integration tests for the calculator CLI."""

from collections.abc import Iterator
from typing import Any

import pytest

from calculator import cli


def _input_generator(responses: list[str]) -> Iterator[str]:
    yield from responses
    while True:
        yield "exit"


@pytest.mark.usefixtures("monkeypatch")
def test_basic_session(monkeypatch: pytest.MonkeyPatch, capsys: Any) -> None:
    inputs = _input_generator(["5 + 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(inputs))

    cli.main()

    captured = capsys.readouterr().out
    assert "CLI Calculator" in captured
    assert "8" in captured
    assert "Goodbye!" in captured
