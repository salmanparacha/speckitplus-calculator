# Calculator API Contract

**Feature**: 001-cli-calculator
**Date**: 2026-01-04
**Type**: Python Module API (not HTTP)

## Overview

This is a CLI application, not a web service. The "API" defines the public Python interfaces that compose the calculator.

## Module: `calculator.parser`

### `parse(input_string: str) -> Expression`

Parses user input into a validated Expression.

**Input**:
- `input_string`: Raw string from user, expected format `<number> <operator> <number>`

**Output**:
- `Expression` dataclass with `left_operand`, `operator`, `right_operand`

**Errors**:
| Exception | Condition |
|-----------|-----------|
| `InvalidInputError` | Non-numeric operand |
| `InvalidOperatorError` | Operator not in +, -, *, / |
| `ParseError` | Wrong number of tokens, empty input |

**Examples**:
```python
parse("5 + 3")      # Expression(Decimal('5'), Operator.ADD, Decimal('3'))
parse("-2.5 * 4")   # Expression(Decimal('-2.5'), Operator.MULTIPLY, Decimal('4'))
parse("abc + 5")    # raises InvalidInputError
parse("5 % 3")      # raises InvalidOperatorError
parse("5")          # raises ParseError
```

---

## Module: `calculator.core`

### `calculate(expression: Expression) -> CalculationResult`

Performs the arithmetic operation defined by the expression.

**Input**:
- `expression`: Validated Expression from parser

**Output**:
- `CalculationResult` with `value` (Decimal) and original `expression`

**Errors**:
| Exception | Condition |
|-----------|-----------|
| `DivisionByZeroError` | Division where right_operand is 0 |

**Examples**:
```python
expr = Expression(Decimal('10'), Operator.ADD, Decimal('5'))
calculate(expr)  # CalculationResult(value=Decimal('15'), expression=expr)

expr = Expression(Decimal('10'), Operator.DIVIDE, Decimal('0'))
calculate(expr)  # raises DivisionByZeroError
```

---

## Module: `calculator.cli`

### `main() -> None`

Entry point for the CLI calculator. Runs a REPL loop.

**Behavior**:
1. Print welcome message
2. Loop:
   - Prompt for input (`> `)
   - If input is `exit` or `quit`, break loop
   - Parse input → calculate → display result
   - On error, display error message and continue
3. Print goodbye message

**Exit Codes**:
| Code | Meaning |
|------|---------|
| 0 | Normal exit (user typed exit/quit) |

---

## Error Message Format

All errors produce user-friendly messages suitable for CLI display.

| Error Type | Message Format |
|------------|----------------|
| `DivisionByZeroError` | `Error: Cannot divide by zero` |
| `InvalidInputError` | `Error: Invalid input: please enter valid numbers` |
| `InvalidOperatorError` | `Error: Invalid operator: use +, -, *, or /` |
| `ParseError` | `Error: Invalid format: use <number> <operator> <number>` |

---

## CLI Session Example

```
$ calc
CLI Calculator (type 'exit' to quit)

> 5 + 3
8

> 10 / 4
2.5

> -3 * -4
12

> 10 / 0
Error: Cannot divide by zero

> abc + 5
Error: Invalid input: please enter valid numbers

> 5 % 3
Error: Invalid operator: use +, -, *, or /

> exit
Goodbye!
```
