# Tasks: CLI Calculator

**Input**: Design documents from `/specs/001-cli-calculator/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Included per Constitution Principle IV (Test-First Safety Net)

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, etc.)
- All paths relative to repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and uv configuration

- [x] T001 Create project directory structure: `src/calculator/`, `tests/unit/`, `tests/integration/`
- [x] T002 Create `pyproject.toml` with uv configuration, pytest, mypy, ruff dependencies
- [x] T003 [P] Create `src/calculator/__init__.py` with package exports
- [x] T004 [P] Configure ruff and mypy in `pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core types and exceptions that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create `src/calculator/exceptions.py` with CalculatorError base class and all domain exceptions (DivisionByZeroError, InvalidInputError, InvalidOperatorError, ParseError)
- [x] T006 [P] Create Operator enum in `src/calculator/core.py` with ADD, SUBTRACT, MULTIPLY, DIVIDE values
- [x] T007 [P] Create Expression dataclass in `src/calculator/core.py` with left_operand, operator, right_operand fields (Decimal types)
- [x] T008 [P] Create CalculationResult dataclass in `src/calculator/core.py` with value and expression fields
- [x] T009 Configure Decimal context (precision, rounding) in `src/calculator/core.py`

**Checkpoint**: Foundation ready - all types and exceptions available for user stories

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: User can enter two numbers and an operator to get the calculated result

**Independent Test**: Enter `5 + 3` and verify output is `8`

### Tests for User Story 1

> **Write tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Unit test for addition in `tests/unit/test_core.py::test_add`
- [x] T011 [P] [US1] Unit test for subtraction in `tests/unit/test_core.py::test_subtract`
- [x] T012 [P] [US1] Unit test for multiplication in `tests/unit/test_core.py::test_multiply`
- [x] T013 [P] [US1] Unit test for division in `tests/unit/test_core.py::test_divide`
- [x] T014 [P] [US1] Unit test for parse function with valid input in `tests/unit/test_parser.py::test_parse_valid`

### Implementation for User Story 1

- [x] T015 [US1] Implement `calculate()` function in `src/calculator/core.py` supporting all 4 operators
- [x] T016 [US1] Implement `parse()` function in `src/calculator/parser.py` for basic `<num> <op> <num>` format
- [x] T017 [US1] Implement `main()` REPL loop in `src/calculator/cli.py` with welcome/goodbye messages
- [x] T018 [US1] Add `calc` entry point to `pyproject.toml` pointing to `calculator.cli:main`
- [x] T019 [US1] Integration test for basic REPL session in `tests/integration/test_cli.py::test_basic_session`

**Checkpoint**: User Story 1 complete - basic integer arithmetic works via `uv run calc`

---

## Phase 4: User Story 2 - Decimal Numbers (Priority: P2)

**Goal**: User can perform calculations with decimal numbers (e.g., 3.14 * 2)

**Independent Test**: Enter `3.5 + 2.7` and verify output is `6.2`

### Tests for User Story 2

- [ ] T020 [P] [US2] Unit test for decimal addition in `tests/unit/test_core.py::test_add_decimals`
- [ ] T021 [P] [US2] Unit test for decimal division in `tests/unit/test_core.py::test_divide_decimals`
- [ ] T022 [P] [US2] Unit test for parsing decimals in `tests/unit/test_parser.py::test_parse_decimals`
- [ ] T023 [P] [US2] Unit test for 0.1 + 0.2 precision in `tests/unit/test_core.py::test_decimal_precision`

### Implementation for User Story 2

- [ ] T024 [US2] Update `parse()` in `src/calculator/parser.py` to handle decimal number patterns
- [ ] T025 [US2] Ensure `calculate()` in `src/calculator/core.py` uses Decimal for all operations (no floats)
- [ ] T026 [US2] Format output in `src/calculator/cli.py` to display clean decimal results (strip trailing zeros)

**Checkpoint**: User Story 2 complete - decimal arithmetic works correctly

---

## Phase 5: User Story 3 - Negative Numbers (Priority: P2)

**Goal**: User can perform calculations with negative numbers (e.g., -5 + 10)

**Independent Test**: Enter `-5 + 3` and verify output is `-2`

### Tests for User Story 3

- [ ] T027 [P] [US3] Unit test for negative + positive in `tests/unit/test_core.py::test_negative_positive`
- [ ] T028 [P] [US3] Unit test for negative * negative in `tests/unit/test_core.py::test_negative_multiply`
- [ ] T029 [P] [US3] Unit test for parsing negative numbers in `tests/unit/test_parser.py::test_parse_negative`
- [ ] T030 [P] [US3] Unit test for double negative (5 - -3) in `tests/unit/test_parser.py::test_parse_double_negative`

### Implementation for User Story 3

- [ ] T031 [US3] Update regex in `src/calculator/parser.py` to correctly handle negative number patterns (including `-5`, `--3` edge cases)
- [ ] T032 [US3] Integration test for negative number session in `tests/integration/test_cli.py::test_negative_numbers`

**Checkpoint**: User Story 3 complete - negative number arithmetic works correctly

---

## Phase 6: User Story 4 - Division by Zero (Priority: P3)

**Goal**: User receives clear error message when dividing by zero, calculator continues working

**Independent Test**: Enter `10 / 0` and verify error message "Cannot divide by zero"

### Tests for User Story 4

- [ ] T033 [P] [US4] Unit test for DivisionByZeroError in `tests/unit/test_core.py::test_divide_by_zero`
- [ ] T034 [P] [US4] Unit test for error message format in `tests/unit/test_exceptions.py::test_division_by_zero_message`

### Implementation for User Story 4

- [ ] T035 [US4] Add division by zero check in `calculate()` in `src/calculator/core.py`, raise DivisionByZeroError
- [ ] T036 [US4] Handle DivisionByZeroError in REPL loop in `src/calculator/cli.py`, display "Error: Cannot divide by zero"
- [ ] T037 [US4] Integration test for error recovery in `tests/integration/test_cli.py::test_division_by_zero_recovery`

**Checkpoint**: User Story 4 complete - division by zero shows error, calculator continues

---

## Phase 7: User Story 5 - Invalid Input (Priority: P3)

**Goal**: User receives clear error messages for invalid input, calculator continues working

**Independent Test**: Enter `abc + 5` and verify error message appears

### Tests for User Story 5

- [ ] T038 [P] [US5] Unit test for InvalidInputError in `tests/unit/test_parser.py::test_parse_invalid_number`
- [ ] T039 [P] [US5] Unit test for InvalidOperatorError in `tests/unit/test_parser.py::test_parse_invalid_operator`
- [ ] T040 [P] [US5] Unit test for ParseError (wrong format) in `tests/unit/test_parser.py::test_parse_malformed`
- [ ] T041 [P] [US5] Unit test for all error messages in `tests/unit/test_exceptions.py::test_all_error_messages`

### Implementation for User Story 5

- [ ] T042 [US5] Add number validation in `parse()` in `src/calculator/parser.py`, raise InvalidInputError for non-numeric
- [ ] T043 [US5] Add operator validation in `parse()` in `src/calculator/parser.py`, raise InvalidOperatorError for unsupported operators
- [ ] T044 [US5] Add format validation in `parse()` in `src/calculator/parser.py`, raise ParseError for wrong token count
- [ ] T045 [US5] Handle all CalculatorError types in REPL loop in `src/calculator/cli.py` with "Error: {message}" format
- [ ] T046 [US5] Integration test for invalid input recovery in `tests/integration/test_cli.py::test_invalid_input_recovery`

**Checkpoint**: User Story 5 complete - all error cases handled gracefully

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final cleanup and validation

- [ ] T047 [P] Run `uv run typecheck` (mypy) and fix any type errors
- [ ] T048 [P] Run `uv run lint` (ruff) and fix any lint errors
- [ ] T049 [P] Run `uv run test` and ensure all tests pass
- [ ] T050 Validate quickstart.md instructions work end-to-end
- [ ] T051 Add docstrings to all public functions in `src/calculator/`

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup) ─────────────────┐
                                 ▼
Phase 2 (Foundational) ──────────┤ BLOCKS all user stories
                                 ▼
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
Phase 3 (US1)              Phase 4 (US2)              Phase 5 (US3)
     │                           │                           │
     └───────────────────────────┼───────────────────────────┘
                                 ▼
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
Phase 6 (US4)              Phase 7 (US5)              (parallel)
     │                           │                           │
     └───────────────────────────┼───────────────────────────┘
                                 ▼
                        Phase 8 (Polish)
```

### User Story Dependencies

| Story | Depends On | Can Parallelize With |
|-------|------------|---------------------|
| US1 (Basic Arithmetic) | Phase 2 only | - |
| US2 (Decimals) | Phase 2 only | US1, US3 |
| US3 (Negatives) | Phase 2 only | US1, US2 |
| US4 (Div by Zero) | Phase 2 only | US1, US2, US3, US5 |
| US5 (Invalid Input) | Phase 2 only | US1, US2, US3, US4 |

### Within Each User Story

1. Tests written FIRST (must FAIL)
2. Implementation to make tests pass
3. Integration test to verify end-to-end
4. Checkpoint validation

---

## Parallel Execution Examples

### Phase 2 (Foundational) - Parallel Tasks

```bash
# All [P] tasks can run together:
Task T006: "Create Operator enum in src/calculator/core.py"
Task T007: "Create Expression dataclass in src/calculator/core.py"
Task T008: "Create CalculationResult dataclass in src/calculator/core.py"
```

### Phase 3 (User Story 1) - Parallel Tests

```bash
# All test tasks can run together:
Task T010: "Unit test for addition"
Task T011: "Unit test for subtraction"
Task T012: "Unit test for multiplication"
Task T013: "Unit test for division"
Task T014: "Unit test for parse function"
```

### Cross-Story Parallelism (with team)

```bash
# Developer A: User Story 1 (MVP)
# Developer B: User Story 2 + 3 (after Phase 2)
# Developer C: User Story 4 + 5 (after Phase 2)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T009)
3. Complete Phase 3: User Story 1 (T010-T019)
4. **STOP and VALIDATE**: Run `uv run calc` with `5 + 3`
5. MVP ready for demo/feedback

### Incremental Delivery

| Increment | Stories | Capability Added |
|-----------|---------|------------------|
| MVP | US1 | Basic integer arithmetic |
| v0.2 | US1 + US2 | + Decimal support |
| v0.3 | US1 + US2 + US3 | + Negative numbers |
| v0.4 | All | + Full error handling |
| v1.0 | All + Polish | Production ready |

---

## Summary

| Metric | Value |
|--------|-------|
| **Total Tasks** | 51 |
| **Setup Tasks** | 4 |
| **Foundational Tasks** | 5 |
| **US1 Tasks** | 10 |
| **US2 Tasks** | 7 |
| **US3 Tasks** | 6 |
| **US4 Tasks** | 5 |
| **US5 Tasks** | 9 |
| **Polish Tasks** | 5 |
| **Parallel Opportunities** | 28 tasks marked [P] |
| **MVP Scope** | Phase 1-3 (19 tasks) |

---

## Notes

- All tests use pytest with parametrized fixtures where applicable
- All code must pass mypy (strict mode) and ruff
- Decimal.Decimal required for all numeric operations (no floats)
- Each checkpoint = working increment that can be demoed
- Commit after each task or logical group
