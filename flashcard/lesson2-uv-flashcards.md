# UV: Modern Python Package Management - Flashcards

## Core Terminology

Q: What is UV?
A: A modern, unified Python package manager written in Rust that replaces pip, venv, and other tools with a single fast tool.

Q: What is a package manager?
A: A tool that installs libraries, manages versions, isolates environments, and tracks reproducibility for a project.

Q: What is a dependency?
A: A piece of code someone else wrote that you want to use in your project (e.g., requests, pandas).

Q: What is PyPI?
A: Python Package Index - the online repository where Python packages are downloaded from.

Q: What is a virtual environment?
A: An isolated space that keeps a project's libraries separate from other projects on the same machine.

Q: What is a lock file?
A: A file that records exact dependency versions to ensure teammates get identical library versions.

Q: What company created UV?
A: Astral (also created Ruff, a fast Python linter).

Q: What programming language is UV written in?
A: Rust - a systems programming language designed for speed.

## Key Concepts

Q: What are the four functions of a package manager?
A: 1) Install libraries, 2) Manage versions, 3) Isolate environments, 4) Track reproducibility.

Q: How much faster is UV compared to pip?
A: 10-100x faster (e.g., installing requests: pip 8-12s vs UV 0.5-2s).

Q: Why does Python have so many package managers?
A: Different teams solved the same problem independently over 15+ years, creating fragmentation.

Q: What does `uv init` do?
A: Creates a new Python project with proper structure and configuration.

Q: What does `uv add` do?
A: Adds a dependency to your project and updates the lock file.

Q: What does `uv sync` do?
A: Synchronizes the environment to match the lock file (ensures exact same packages).

Q: What does `uv run` do?
A: Runs code in the project context without manual environment activation.

## Tool Comparisons

Q: What is the main limitation of pip?
A: It's slow and doesn't manage virtual environments.

Q: What is the main limitation of venv?
A: It creates environments but doesn't manage dependencies.

Q: When was UV created?
A: 2024.

Q: When was pip created?
A: 2008.

Q: What is conda primarily designed for?
A: Data science - it manages both packages and Python versions but is heavy.

Q: What is poetry's main characteristic?
A: Modern Python packaging, but complex and opinionated.

## Relationships & Comparisons

Q: What is the difference between pip and UV?
A: pip only installs packages (slowly); UV handles packages, environments, locking, and Python versions (10-100x faster).

Q: What is the difference between venv and UV?
A: venv only creates isolated environments; UV handles environments plus packages, locking, and more.

Q: What analogy describes the speed difference between pip and UV?
A: pip is like a hand shovel; UV is like a power shovel.

Q: When should you NOT switch to UV?
A: When working on a legacy project already using poetry or pipenv mid-development.

Q: When is UV the recommended choice?
A: For new Python projects, personal learning, and team collaboration in 2025.

---
Source: lessons/lesson2-uv.md
Card count: 24
