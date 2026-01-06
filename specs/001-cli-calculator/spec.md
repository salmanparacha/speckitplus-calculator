# Feature Specification: CLI Calculator

**Feature Branch**: `001-cli-calculator`
**Created**: 2026-01-04
**Status**: Draft
**Input**: Build a basic CLI-based calculator that handles addition, subtraction, multiplication, and division with proper error handling.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Perform Basic Arithmetic (Priority: P1)

As a user, I want to enter two numbers and an operation to get the calculated result displayed in the terminal.

**Why this priority**: Core functionality - without basic arithmetic, the calculator has no value.

**Independent Test**: Can be fully tested by entering `5 + 3` and verifying output is `8`.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** user enters `10 + 5`, **Then** the system displays `15`
2. **Given** the calculator is running, **When** user enters `20 - 8`, **Then** the system displays `12`
3. **Given** the calculator is running, **When** user enters `6 * 7`, **Then** the system displays `42`
4. **Given** the calculator is running, **When** user enters `15 / 3`, **Then** the system displays `5`

---

### User Story 2 - Handle Decimal Numbers (Priority: P2)

As a user, I want to perform calculations with decimal numbers and receive accurate decimal results.

**Why this priority**: Essential for real-world calculations beyond simple integers.

**Independent Test**: Can be tested by entering `3.5 + 2.7` and verifying output is `6.2`.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** user enters `3.14 * 2`, **Then** the system displays `6.28`
2. **Given** the calculator is running, **When** user enters `10 / 4`, **Then** the system displays `2.5`
3. **Given** the calculator is running, **When** user enters `0.1 + 0.2`, **Then** the system displays `0.3` (handling floating-point precision)

---

### User Story 3 - Handle Negative Numbers (Priority: P2)

As a user, I want to perform calculations with negative numbers correctly.

**Why this priority**: Negative numbers are common in real calculations and must work correctly.

**Independent Test**: Can be tested by entering `-5 + 3` and verifying output is `-2`.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** user enters `-5 + 10`, **Then** the system displays `5`
2. **Given** the calculator is running, **When** user enters `-3 * -4`, **Then** the system displays `12`
3. **Given** the calculator is running, **When** user enters `5 - -3`, **Then** the system displays `8`

---

### User Story 4 - Handle Division by Zero (Priority: P3)

As a user, I want to receive a clear error message when attempting to divide by zero.

**Why this priority**: Prevents crashes and provides user-friendly error handling.

**Independent Test**: Can be tested by entering `10 / 0` and verifying an error message appears.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** user enters `10 / 0`, **Then** the system displays an error message "Cannot divide by zero"
2. **Given** division by zero occurred, **When** user enters a valid calculation, **Then** the calculator continues to work normally

---

### User Story 5 - Handle Invalid Input (Priority: P3)

As a user, I want to receive a clear error message when I enter invalid input so I know what went wrong.

**Why this priority**: Prevents crashes and guides users to correct their input.

**Independent Test**: Can be tested by entering `abc + 5` and verifying an error message appears.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** user enters `abc + 5`, **Then** the system displays "Invalid input: please enter valid numbers"
2. **Given** the calculator is running, **When** user enters `5 % 3` (unsupported operator), **Then** the system displays "Invalid operator: use +, -, *, or /"
3. **Given** invalid input was entered, **When** user enters a valid calculation, **Then** the calculator continues to work normally

---

### Edge Cases

- What happens when user enters only one number without an operator?
- How does system handle very large numbers (overflow)?
- How does system handle empty input?
- How does system handle extra whitespace between numbers and operators?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST accept two numbers and one arithmetic operator as input
- **FR-002**: System MUST support addition (+), subtraction (-), multiplication (*), and division (/) operators
- **FR-003**: System MUST display the calculation result after each valid operation
- **FR-004**: System MUST handle decimal numbers (floating-point) in calculations
- **FR-005**: System MUST handle negative numbers correctly in all operations
- **FR-006**: System MUST display a clear error message when division by zero is attempted
- **FR-007**: System MUST display a clear error message when non-numeric input is provided
- **FR-008**: System MUST display a clear error message when an unsupported operator is used
- **FR-009**: System MUST continue operating after an error (not crash)

### Key Entities

- **Number**: A numeric value (integer or decimal, positive or negative) provided by the user
- **Operator**: One of four arithmetic symbols (+, -, *, /) that defines the operation
- **Result**: The computed output displayed to the user
- **Error Message**: User-friendly text explaining what went wrong

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can complete a basic calculation in under 5 seconds
- **SC-002**: All four basic operations produce mathematically correct results
- **SC-003**: 100% of division-by-zero attempts display an error message instead of crashing
- **SC-004**: 100% of invalid inputs display a helpful error message instead of crashing
- **SC-005**: Decimal calculations maintain precision to at least 2 decimal places
- **SC-006**: Negative number operations produce mathematically correct results

## Assumptions

- Single operation per input (no chaining like `5 + 3 * 2`)
- Input format: `<number> <operator> <number>` (space-separated)
- Calculator runs in a loop until user explicitly exits
- Standard floating-point precision is acceptable (no arbitrary precision required)
