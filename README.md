# SpecKit Plus Calculator

This project is a high-precision CLI calculator developed using the **SpecKit Plus** workflow. It features Decimal-based arithmetic to ensure accuracy for financial and scientific education use cases.

## Overview
A terminal-based calculator implementation with support for:
- Basic operations: `+`, `-`, `*`, `/`
- High precision using Python's `decimal` module
- Negative number support
- Elegant error handling for division by zero and invalid inputs

## Project Structure
- `src/calculator/` - Core source code (Parsing, Logic, CLI)
- `tests/` - Comprehensive unit and integration test suite
- `specs/` - Feature specifications, implementation plans, and research (SpecKit Plus)
- `.specify/` - SpecKit Plus workflow configuration, templates, and scripts

## Setup and Installation
This project uses **uv** for fast, reproducible dependency management.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/salmanparacha/speckitplus-calculator.git
   cd speckitplus-calculator
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

## Usage
Start the calculator REPL:
```bash
uv run calc
```

Example session:
```
CLI Calculator (type 'exit' to quit)
> 10.5 + 4.5
15.0
> 10 / 0
Error: Cannot divide by zero
> exit
```

## Running Tests
Run the full test suite with coverage:
```bash
uv run pytest
```

## SpecKit Plus Workflow
This repository follows a structured Specification-Driven Development (SDD) process:
- All features start in the `specs/` directory with a specification, plan, and research record.
- Architecture decisions are tracked via ADRs in `specs/checklists/`.
- Automated scripts in `.specify/` assist in generating new artifacts and maintaining consistency.

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)
