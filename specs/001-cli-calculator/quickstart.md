# Quickstart: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-04

## Prerequisites

- Python 3.12+
- uv (install: `curl -LsSf https://astral.sh/uv/install.sh | sh`)

## Setup

```bash
# Clone and navigate to project
cd ai300

# Install dependencies with uv
uv sync

# Verify installation
uv run calc --help
```

## Running the Calculator

```bash
# Start the calculator REPL
uv run calc
```

## Usage Examples

```
CLI Calculator (type 'exit' to quit)

> 5 + 3
8

> 10.5 - 2.3
8.2

> -4 * 6
-24

> 15 / 4
3.75

> exit
Goodbye!
```

## Supported Operations

| Operator | Operation | Example |
|----------|-----------|---------|
| `+` | Addition | `5 + 3` → `8` |
| `-` | Subtraction | `10 - 4` → `6` |
| `*` | Multiplication | `6 * 7` → `42` |
| `/` | Division | `15 / 3` → `5` |

## Input Format

```
<number> <operator> <number>
```

- Numbers can be integers or decimals: `5`, `3.14`, `-2.5`
- Negative numbers are supported: `-5 + 3`
- Spaces are required between tokens

## Error Handling

The calculator handles errors gracefully and continues running:

```
> 10 / 0
Error: Cannot divide by zero

> abc + 5
Error: Invalid input: please enter valid numbers

> 5 % 3
Error: Invalid operator: use +, -, *, or /

> 5 + 3
8
```

## Development Commands

```bash
# Run tests
uv run test

# Run linter
uv run lint

# Run type checker
uv run typecheck

# Run all checks
uv run all

# Format code
uv run format
```

## Project Structure

```
src/calculator/
├── __init__.py      # Package init
├── core.py          # Calculation logic (Decimal operations)
├── parser.py        # Input parsing and validation
├── exceptions.py    # Domain-specific exceptions
└── cli.py           # CLI entry point and REPL

tests/
├── unit/            # Unit tests for each module
└── integration/     # CLI integration tests
```
