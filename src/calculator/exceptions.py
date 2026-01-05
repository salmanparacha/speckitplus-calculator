"""Domain-specific exceptions for the calculator."""


class CalculatorError(Exception):
    """Base exception for all calculator errors."""

    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    def __init__(self) -> None:
        super().__init__("Cannot divide by zero")


class InvalidInputError(CalculatorError):
    """Raised when input contains non-numeric values."""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"Invalid input: please enter valid numbers (got '{value}')")


class InvalidOperatorError(CalculatorError):
    """Raised when an unsupported operator is used."""

    def __init__(self, operator: str) -> None:
        self.operator = operator
        super().__init__(f"Invalid operator: use +, -, *, or / (got '{operator}')")


class ParseError(CalculatorError):
    """Raised when input format is malformed."""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(
            message or "Invalid format: use <number> <operator> <number>"
        )
