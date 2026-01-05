"""Core calculation types and operations using Decimal precision."""

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal, getcontext
from enum import Enum

from calculator.exceptions import DivisionByZeroError

# Configure Decimal context for consistent precision
getcontext().prec = 28
getcontext().rounding = ROUND_HALF_UP


class Operator(Enum):
    """Supported arithmetic operators."""

    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


@dataclass(frozen=True)
class Expression:
    """Represents a parsed arithmetic expression."""

    left_operand: Decimal
    operator: Operator
    right_operand: Decimal


@dataclass(frozen=True)
class CalculationResult:
    """Result of a calculation with the original expression."""

    value: Decimal
    expression: Expression


def calculate(expression: Expression) -> CalculationResult:
    """Perform the arithmetic operation defined by the expression.

    Args:
        expression: Validated Expression from parser

    Returns:
        CalculationResult with computed value and original expression

    Raises:
        DivisionByZeroError: If dividing by zero
    """
    left = expression.left_operand
    right = expression.right_operand
    operator = expression.operator

    if operator is Operator.ADD:
        result_value = left + right
    elif operator is Operator.SUBTRACT:
        result_value = left - right
    elif operator is Operator.MULTIPLY:
        result_value = left * right
    elif operator is Operator.DIVIDE:
        if right == 0:
            raise DivisionByZeroError()
        result_value = left / right
    else:  # pragma: no cover - all operators enumerated above
        raise ValueError(f"Unsupported operator: {operator}")

    return CalculationResult(value=result_value, expression=expression)
