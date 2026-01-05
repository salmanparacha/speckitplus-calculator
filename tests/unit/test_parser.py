"""Unit tests for calculator.parser.parse."""

from decimal import Decimal

import pytest

from calculator.core import Expression, Operator
from calculator.parser import parse


@pytest.mark.parametrize(
    ("raw_input", "expected_operator", "expected_left", "expected_right"),
    [
        ("5 + 3", Operator.ADD, Decimal("5"), Decimal("3")),
        ("20 - 8", Operator.SUBTRACT, Decimal("20"), Decimal("8")),
        ("6 * 7", Operator.MULTIPLY, Decimal("6"), Decimal("7")),
        ("15 / 3", Operator.DIVIDE, Decimal("15"), Decimal("3")),
    ],
)
def test_parse_valid(
    raw_input: str,
    expected_operator: Operator,
    expected_left: Decimal,
    expected_right: Decimal,
) -> None:
    expression = parse(raw_input)

    assert expression.operator == expected_operator
    assert expression.left_operand == expected_left
    assert expression.right_operand == expected_right
    assert isinstance(expression, Expression)
