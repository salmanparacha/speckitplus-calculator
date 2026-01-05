# Data Model: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-04

## Entities

### Expression

Represents a parsed calculation expression from user input.

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| left_operand | `Decimal` | First number in expression | Must be valid decimal |
| operator | `Operator` | Arithmetic operation | Must be +, -, *, / |
| right_operand | `Decimal` | Second number in expression | Must be valid decimal |

**State Transitions**: None (immutable value object)

### Operator (Enum)

Represents supported arithmetic operations.

| Value | Symbol | Description |
|-------|--------|-------------|
| ADD | `+` | Addition |
| SUBTRACT | `-` | Subtraction |
| MULTIPLY | `*` | Multiplication |
| DIVIDE | `/` | Division |

### CalculationResult

Represents the outcome of a calculation.

| Field | Type | Description |
|-------|------|-------------|
| value | `Decimal` | Computed result |
| expression | `Expression` | Original expression |

### Error Types

Domain-specific exceptions per Constitution Principle V.

| Exception | Trigger | Message Template |
|-----------|---------|------------------|
| `CalculatorError` | Base class | N/A |
| `DivisionByZeroError` | `right_operand == 0` with DIVIDE | "Cannot divide by zero" |
| `InvalidInputError` | Non-numeric token | "Invalid input: please enter valid numbers" |
| `InvalidOperatorError` | Unsupported operator | "Invalid operator: use +, -, *, or /" |
| `ParseError` | Malformed expression | "Invalid format: use <number> <operator> <number>" |

## Type Definitions

```python
from decimal import Decimal
from enum import Enum
from dataclasses import dataclass

class Operator(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

@dataclass(frozen=True)
class Expression:
    left_operand: Decimal
    operator: Operator
    right_operand: Decimal

@dataclass(frozen=True)
class CalculationResult:
    value: Decimal
    expression: Expression
```

## Relationships

```
User Input (str)
     │
     ▼
┌─────────────┐
│   Parser    │──▶ InvalidInputError / InvalidOperatorError / ParseError
└─────────────┘
     │
     ▼
┌─────────────┐
│ Expression  │
└─────────────┘
     │
     ▼
┌─────────────┐
│    Core     │──▶ DivisionByZeroError
│ (calculate) │
└─────────────┘
     │
     ▼
┌─────────────────────┐
│ CalculationResult   │
└─────────────────────┘
     │
     ▼
   Display (str)
```

## Validation Rules

| Entity | Field | Rule | Error |
|--------|-------|------|-------|
| Expression | left_operand | Must parse as Decimal | InvalidInputError |
| Expression | right_operand | Must parse as Decimal | InvalidInputError |
| Expression | operator | Must be in Operator enum | InvalidOperatorError |
| Calculation | right_operand | Cannot be 0 for DIVIDE | DivisionByZeroError |

## Notes

- All numeric values use `decimal.Decimal` per Constitution Principle III
- Entities are immutable (frozen dataclasses) for safety
- No persistence layer - pure in-memory calculation
