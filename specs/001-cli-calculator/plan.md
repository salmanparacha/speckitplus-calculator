# Implementation Plan: CLI Calculator

**Branch**: `001-cli-calculator` | **Date**: 2026-01-04 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-cli-calculator/spec.md`

## Summary

Build a command-line calculator that performs basic arithmetic (addition, subtraction, multiplication, division) with robust error handling for decimal numbers, negative numbers, division by zero, and invalid input. Uses Python's `decimal.Decimal` for precision and domain-specific exceptions for clear error messages.

## Technical Context

**Language/Version**: Python 3.12+
**Primary Dependencies**: Standard library only (`decimal`, `dataclasses`, `enum`, `re`)
**Storage**: N/A (in-memory calculation only)
**Testing**: pytest + mypy + ruff
**Target Platform**: Linux/macOS/Windows CLI
**Project Type**: Single CLI application
**Performance Goals**: Instant response (<100ms per calculation)
**Constraints**: No floating-point in public APIs (use Decimal)
**Scale/Scope**: Single-user CLI tool, educational project

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Typed Python Source of Truth | ✅ PASS | Python 3.12+ with full type hints |
| II. UV-Managed Reproducibility | ✅ PASS | uv for all dependency/script management |
| III. Deterministic Arithmetic Accuracy | ✅ PASS | decimal.Decimal for all calculations |
| IV. Test-First Safety Net | ✅ PASS | pytest with parametrized tests planned |
| V. Input Validation & Error Transparency | ✅ PASS | Domain exceptions with clear messages |
| VI. Minimal Surface CLI Design | ✅ PASS | Single CLI entry point, composable functions |

**Gate Result**: PASS - All principles satisfied

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-calculator/
├── plan.md              # This file
├── research.md          # Phase 0 output (complete)
├── data-model.md        # Phase 1 output (complete)
├── quickstart.md        # Phase 1 output (complete)
├── contracts/           # Phase 1 output (complete)
│   └── calculator-api.md
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
└── calculator/
    ├── __init__.py       # Package initialization
    ├── core.py           # Decimal arithmetic operations
    ├── parser.py         # Input parsing and validation
    ├── exceptions.py     # Domain-specific exceptions
    └── cli.py            # CLI entry point and REPL loop

tests/
├── unit/
│   ├── test_core.py      # Unit tests for arithmetic
│   ├── test_parser.py    # Unit tests for parsing
│   └── test_exceptions.py # Unit tests for error messages
└── integration/
    └── test_cli.py       # End-to-end CLI tests

pyproject.toml            # uv configuration and scripts
```

**Structure Decision**: Single project layout selected per Constitution Principle VI (minimal surface design). The calculator is a focused CLI tool with no need for separate frontend/backend or multi-platform structure.

## Complexity Tracking

> No violations - all constitution principles satisfied without exceptions.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |

## Phase 0 Artifacts

- [x] **research.md** - Technical decisions resolved
  - Decimal module configuration
  - Input parsing strategy
  - Error handling architecture
  - Project structure
  - Testing approach
  - UV configuration

## Phase 1 Artifacts

- [x] **data-model.md** - Entity definitions
  - Expression (left_operand, operator, right_operand)
  - Operator enum (ADD, SUBTRACT, MULTIPLY, DIVIDE)
  - CalculationResult (value, expression)
  - Exception hierarchy

- [x] **contracts/calculator-api.md** - Module interfaces
  - `parser.parse()` - Input to Expression
  - `core.calculate()` - Expression to Result
  - `cli.main()` - REPL entry point
  - Error message formats

- [x] **quickstart.md** - Developer setup guide
  - Prerequisites
  - Installation steps
  - Usage examples
  - Development commands

## Next Steps

Run `/sp.tasks` to generate the implementation task list with test cases.

## Architecture Decisions

No significant architectural decisions requiring ADR documentation. The implementation follows standard Python CLI patterns with constitution-mandated tooling (uv, pytest, mypy, ruff, decimal).
