"""Input parsing and validation for calculator expressions."""

from decimal import Decimal, InvalidOperation

from calculator.core import Expression, Operator
from calculator.exceptions import (
    InvalidInputError,
    InvalidOperatorError,
    ParseError,
)

# Mapping from operator symbols to Operator enum
OPERATOR_MAP: dict[str, Operator] = {
    "+": Operator.ADD,
    "-": Operator.SUBTRACT,
    "*": Operator.MULTIPLY,
    "/": Operator.DIVIDE,
}


def parse(input_string: str) -> Expression:
    """Parse user input into a validated Expression.

    Args:
        input_string: Raw string from user, expected format "<number> <operator> <number>"

    Returns:
        Expression with validated operands and operator

    Raises:
        ParseError: If input is empty or has wrong number of tokens
        InvalidInputError: If operands are not valid numbers
        InvalidOperatorError: If operator is not +, -, *, or /
    """
    tokens = input_string.strip().split()

    if len(tokens) != 3:
        raise ParseError()

    left_str, operator_symbol, right_str = tokens

    operator = OPERATOR_MAP.get(operator_symbol)
    if operator is None:
        raise InvalidOperatorError(operator_symbol)

    try:
        left_operand = Decimal(left_str)
    except InvalidOperation as exc:  # pragma: no cover - Decimal raises for invalid input
        raise InvalidInputError(left_str) from exc

    try:
        right_operand = Decimal(right_str)
    except InvalidOperation as exc:  # pragma: no cover - Decimal raises for invalid input
        raise InvalidInputError(right_str) from exc

    return Expression(
        left_operand=left_operand,
        operator=operator,
        right_operand=right_operand,
    )
