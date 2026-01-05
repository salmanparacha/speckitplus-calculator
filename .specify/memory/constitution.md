<!--
Sync Impact Report
Version change: (initial) → 1.0.0
Modified principles:
- None (initial version)
Principles added:
- I. Typed Python Source of Truth
- II. UV-Managed Reproducibility
- III. Deterministic Arithmetic Accuracy
- IV. Test-First Safety Net
- V. Input Validation & Error Transparency
- VI. Minimal Surface CLI Design
Added sections:
- Additional Constraints & Stack
- Development Workflow & Quality Gates
Removed sections:
- None
Templates:
- ✅ .specify/templates/plan-template.md
- ✅ .specify/templates/spec-template.md
- ✅ .specify/templates/tasks-template.md
Follow-up TODOs:
- None
-->
# AI300 Calculator Constitution

## Core Principles

### I. Typed Python Source of Truth
All runtime and support code MUST target CPython 3.12+ and include precise type hints. Functions return explicit types, `mypy` (or pyright) must pass, and no untyped `Any` leaks are allowed. Type contracts document every value flowing through calculator operations and guard against implicit casts.

### II. UV-Managed Reproducibility
`uv` is the single source of truth for dependency resolution, packaging, and scripts. No `pip install` or ad-hoc venvs. Lock files live in repo, and every command that mutates state is codified as a `uv` script to keep local and CI environments identical.

### III. Deterministic Arithmetic Accuracy
Use `decimal.Decimal` with explicit context configuration for every calculation. Rounding rules, precision, and exception handling are enforced in one module and referenced everywhere. Division-by-zero, overflow, or precision loss must raise structured domain errors instead of propagating floats.

### IV. Test-First Safety Net
Before implementing or modifying operators, author pytest cases (unit + boundary) that express the desired behavior: decimals, negatives, invalid tokens, and zero division scenarios. CI blocks merges unless the suite (including type checks and lint) is green.

### V. Input Validation & Error Transparency
CLI or library inputs are parsed through a validation layer that rejects malformed expressions, alphabetic noise, or unsupported operators with actionable messages. Errors bubble up as typed exceptions and user-facing strings, never silent failures.

### VI. Minimal Surface CLI Design
Expose the calculator through a single focused CLI/module namespace. Prefer small, composable functions over frameworks. New features must justify themselves through learning value; avoid speculative abstractions and keep IO strictly text-based for lesson reuse.

## Additional Constraints & Stack

- **Language & Toolchain**: Python 3.12+, `uv` for env + packaging, `ruff` for lint/format, `mypy` (or pyright) for typing.
- **Dependencies**: Standard library + explicitly approved math/CLI helpers. External libs require constitution-compliant rationale.
- **Data & Precision**: `decimal` module with centrally defined context; no floats in public APIs.
- **Error Handling**: Domain-specific exception classes with string messages suitable for CLI output and notes.
- **Documentation**: `/notes/` captures learning artifacts; CLI usage examples belong alongside lesson notes.

## Development Workflow & Quality Gates

1. Follow Spec → Plan → Tasks sequence (`/sp.specify`, `/sp.plan`, `/sp.tasks`) before coding. Deviations must be documented.
2. Each user story is independently testable; tasks name exact files per template guidance.
3. Tests: `pytest` + type checking + lint run in CI and locally before PR. Add regression tests for every bug.
4. Code Reviews: No self-merge. Reviewers verify principle adherence, especially Decimal usage and uv scripts.
5. Release Criteria: CLI help text updated, README challenges addressed, and quickstart instructions validated.

## Governance

- This constitution supersedes ad-hoc preferences. All PRs must reference the principles they touch and note compliance in descriptions.
- Amendments require consensus in review, recorded reasoning, and immediate template cross-checks. Version number increments per semantic rules (MAJOR for breaking governance, MINOR for new principles/sections, PATCH for clarifications).
- Compliance Reviews: At least once per feature cycle, confirm Decimal context, uv manifests, and typing gates remain intact. Non-compliance blocks release until remediated.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04
