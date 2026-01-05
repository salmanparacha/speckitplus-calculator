"""Unit tests for calculator.core.calculate."""

from decimal import Decimal

import pytest

from calculator.core import CalculationResult, Expression, Operator, calculate


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (Decimal("5"), Decimal("3"), Decimal("8")),
        (Decimal("0"), Decimal("0"), Decimal("0")),
        (Decimal("-2"), Decimal("5"), Decimal("3")),
    ],
)
def test_add(left: Decimal, right: Decimal, expected: Decimal) -> None:
    expression = Expression(left_operand=left, operator=Operator.ADD, right_operand=right)
    result = calculate(expression)

    assert isinstance(result, CalculationResult)
    assert result.value == expected
    assert result.expression == expression


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (Decimal("10"), Decimal("3"), Decimal("7")),
        (Decimal("5"), Decimal("5"), Decimal("0")),
        (Decimal("2"), Decimal("8"), Decimal("-6")),
    ],
)
def test_subtract(left: Decimal, right: Decimal, expected: Decimal) -> None:
    expression = Expression(
        left_operand=left,
        operator=Operator.SUBTRACT,
        right_operand=right,
    )
    result = calculate(expression)

    assert result.value == expected
    assert result.expression == expression


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (Decimal("6"), Decimal("7"), Decimal("42")),
        (Decimal("0"), Decimal("100"), Decimal("0")),
        (Decimal("-3"), Decimal("4"), Decimal("-12")),
    ],
)
def test_multiply(left: Decimal, right: Decimal, expected: Decimal) -> None:
    expression = Expression(
        left_operand=left,
        operator=Operator.MULTIPLY,
        right_operand=right,
    )
    result = calculate(expression)

    assert result.value == expected
    assert result.expression == expression


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (Decimal("15"), Decimal("3"), Decimal("5")),
        (Decimal("10"), Decimal("4"), Decimal("2.5")),
        (Decimal("-8"), Decimal("2"), Decimal("-4")),
    ],
)
def test_divide(left: Decimal, right: Decimal, expected: Decimal) -> None:
    expression = Expression(
        left_operand=left,
        operator=Operator.DIVIDE,
        right_operand=right,
    )
    result = calculate(expression)

    assert result.value == expected
    assert result.expression == expression
