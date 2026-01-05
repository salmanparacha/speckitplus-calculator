"""CLI entry point and REPL loop for the calculator."""

from calculator.core import calculate
from calculator.exceptions import CalculatorError
from calculator.parser import parse


def main() -> None:
    """Run the calculator REPL loop.

    Displays welcome message, prompts for input, calculates results,
    handles errors gracefully, and exits on 'exit' or 'quit'.
    """
    print("CLI Calculator (type 'exit' to quit)")
    print()

    while True:
        try:
            user_input = input("> ").strip()
        except EOFError:
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            break

        try:
            expression = parse(user_input)
            result = calculate(expression)
            print(result.value)
        except CalculatorError as error:
            print(f"Error: {error}")

    print("Goodbye!")


if __name__ == "__main__":
    main()
