# Research: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-04
**Status**: Complete

## Research Tasks

### 1. Decimal Module Best Practices for Calculator Operations

**Decision**: Use `decimal.Decimal` with explicit context configuration

**Rationale**:
- Constitution mandates `decimal.Decimal` over floats (Principle III)
- Avoids floating-point precision issues (e.g., `0.1 + 0.2 = 0.30000000000000004`)
- Provides explicit control over rounding and precision
- Built into Python standard library (no external dependencies)

**Implementation Details**:
```python
from decimal import Decimal, InvalidOperation, DivisionByZero
from decimal import getcontext

# Configure context once at module level
getcontext().prec = 28  # Standard precision
getcontext().rounding = ROUND_HALF_UP
```

**Alternatives Considered**:
- `float`: Rejected - Constitution prohibits floats in public APIs
- `fractions.Fraction`: Rejected - Overkill for basic calculator, less intuitive output
- Third-party libs (mpmath): Rejected - Constitution requires standard library preference

---

### 2. CLI Input Parsing Strategy

**Decision**: Simple string splitting with regex validation

**Rationale**:
- Spec defines format: `<number> <operator> <number>` (space-separated)
- Single operation per input (no expression trees needed)
- Regex provides clean validation of numeric patterns including negatives/decimals

**Implementation Details**:
```python
import re

# Pattern matches: optional negative, digits, optional decimal
NUMBER_PATTERN = r'-?\d+\.?\d*'
OPERATORS = {'+', '-', '*', '/'}
```

**Alternatives Considered**:
- `argparse`: Rejected - Overkill for simple expression input
- `shlex`: Rejected - Designed for shell-like parsing, unnecessary complexity
- Full parser (pyparsing): Rejected - No expression chaining needed per spec

---

### 3. Error Handling Architecture

**Decision**: Domain-specific exception hierarchy with user-friendly messages

**Rationale**:
- Constitution requires typed exceptions (Principle V)
- Spec requires clear, actionable error messages
- Exceptions map 1:1 to error scenarios in spec

**Implementation Details**:
```python
class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when dividing by zero."""
    def __init__(self) -> None:
        super().__init__("Cannot divide by zero")

class InvalidInputError(CalculatorError):
    """Raised for non-numeric input."""
    def __init__(self, value: str) -> None:
        super().__init__(f"Invalid input: please enter valid numbers (got '{value}')")

class InvalidOperatorError(CalculatorError):
    """Raised for unsupported operators."""
    def __init__(self, operator: str) -> None:
        super().__init__(f"Invalid operator: use +, -, *, or / (got '{operator}')")
```

**Alternatives Considered**:
- Return tuples (value, error): Rejected - Less Pythonic, harder to compose
- Use built-in exceptions only: Rejected - Constitution requires domain-specific types

---

### 4. Project Structure for Single CLI Application

**Decision**: Minimal `src/` layout with separate test directory

**Rationale**:
- Constitution mandates minimal surface design (Principle VI)
- Single project type per spec (CLI calculator)
- Standard Python project layout for `uv` compatibility

**Implementation Details**:
```
src/
├── calculator/
│   ├── __init__.py
│   ├── core.py          # Decimal operations
│   ├── parser.py        # Input parsing/validation
│   ├── exceptions.py    # Domain exceptions
│   └── cli.py           # Entry point and REPL loop
tests/
├── unit/
│   ├── test_core.py
│   ├── test_parser.py
│   └── test_exceptions.py
└── integration/
    └── test_cli.py
pyproject.toml            # uv configuration
```

**Alternatives Considered**:
- Flat structure (all in one file): Rejected - Harder to test, less modular
- Deep nesting: Rejected - Over-engineering for simple calculator

---

### 5. Testing Strategy

**Decision**: pytest with parametrized tests covering all spec scenarios

**Rationale**:
- Constitution mandates pytest (Principle IV)
- Parametrized tests efficiently cover all operator/input combinations
- Integration tests verify CLI behavior end-to-end

**Test Categories**:
| Category | Coverage |
|----------|----------|
| Unit: core.py | All 4 operators, decimals, negatives |
| Unit: parser.py | Valid input, invalid numbers, invalid operators |
| Unit: exceptions.py | Message formatting |
| Integration: cli.py | REPL loop, error recovery, exit handling |

**Alternatives Considered**:
- unittest: Rejected - pytest is more concise and constitution-specified
- hypothesis (property-based): Considered for future - not needed for basic calculator

---

### 6. UV Configuration and Scripts

**Decision**: Single `pyproject.toml` with uv scripts for all tasks

**Rationale**:
- Constitution mandates uv as single source of truth (Principle II)
- Scripts ensure consistent local and CI environments

**Implementation Details**:
```toml
[project]
name = "ai300-calculator"
version = "0.1.0"
requires-python = ">=3.12"

[project.scripts]
calc = "calculator.cli:main"

[tool.uv.scripts]
test = "pytest tests/ -v"
lint = "ruff check src/ tests/"
format = "ruff format src/ tests/"
typecheck = "mypy src/"
all = "uv run lint && uv run typecheck && uv run test"
```

**Alternatives Considered**:
- Makefile: Rejected - Constitution specifies uv scripts
- poetry: Rejected - Constitution specifies uv

---

## Summary of Resolved Clarifications

| Item | Resolution | Source |
|------|------------|--------|
| Arithmetic precision | `decimal.Decimal` with 28-digit precision | Constitution III |
| Dependency management | `uv` only | Constitution II |
| Float handling | Prohibited in public APIs | Constitution III |
| Testing framework | `pytest` + `mypy` + `ruff` | Constitution IV |
| Error handling | Domain-specific typed exceptions | Constitution V |
| Project structure | Single CLI project with src/ layout | Constitution VI |

All NEEDS CLARIFICATION items from technical context have been resolved.
