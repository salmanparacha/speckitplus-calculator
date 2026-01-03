# UV: Modern Python Package Management - Quiz

## Instructions
Answer all questions. Review explanations after completing the quiz.

---

## Multiple Choice

**Q1.** A developer needs to set up a new Python project and wants their teammate to have the exact same environment. Which UV workflow accomplishes this?
- A) `uv init` → `uv add packages` → teammate runs `pip install -r requirements.txt`
- B) `uv init` → `uv add packages` → teammate runs `uv sync`
- C) `uv venv` → `uv pip install` → teammate runs `uv pip install`
- D) `pip install` → `pip freeze` → teammate runs `uv sync`

**Q2.** Why is UV significantly faster than pip?
- A) UV uses a more efficient algorithm written in Python
- B) UV downloads packages from a faster server
- C) UV is written in Rust, a systems programming language designed for speed
- D) UV caches all packages permanently on disk

**Q3.** You're joining a team with an existing project that uses poetry. What is the recommended approach?
- A) Immediately convert the project to UV for speed benefits
- B) Use pip instead since it's the standard
- C) Continue using poetry to avoid mid-project tool switching
- D) Delete the poetry.lock file and run `uv sync`

**Q4.** Which of the following is NOT a function of a package manager?
- A) Installing libraries from PyPI
- B) Managing specific library versions
- C) Writing your application code
- D) Isolating project environments

**Q5.** A data scientist needs specialized conda packages not available on PyPI. What should they consider?
- A) UV cannot be used; they must use conda exclusively
- B) Convert all conda packages to pip packages first
- C) Use conda for specialized packages, though UV is catching up
- D) Abandon the specialized packages for UV compatibility

**Q6.** In AI-assisted development, why does UV's speed particularly matter?
- A) AI models require fast package managers to function
- B) Fast tools keep developers in flow by providing quick feedback
- C) AI can only execute UV commands, not pip commands
- D) Speed reduces API costs when using AI assistants

---

## True/False

**Q7.** Python's package manager fragmentation happened because different teams independently solved the same problem over 15+ years. (True/False)

**Q8.** The command `uv run script.py` requires you to manually activate the virtual environment first. (True/False)

**Q9.** UV was created by Google as part of their Python infrastructure. (True/False)

**Q10.** When installing 50+ dependencies, UV can complete in under 10 seconds while pip might take over 2 minutes. (True/False)

**Q11.** You should always switch existing projects to UV regardless of what tool they currently use. (True/False)

---

## Short Answer

**Q12.** Explain why a beginner asking "Which Python package manager should I use?" gets five different answers, and how UV addresses this problem.

**Q13.** Compare the traditional pip/venv workflow to UV's workflow for starting a new project. What specific pain points does UV eliminate?

---

# Answer Key

## Q1
**Answer:** B
**Explanation:** UV's workflow is `uv init` to create the project, `uv add` to add packages (which updates the lock file), and teammates run `uv sync` to get the exact same environment from the lock file. Option A mixes pip with UV incorrectly.
**Reference:** notes/lesson2-uv.md - Practical Applications section

## Q2
**Answer:** C
**Explanation:** UV is written in Rust, a systems programming language designed for performance. The lesson uses the analogy of pip being a "hand shovel" while UV is a "power shovel."
**Reference:** notes/lesson2-uv.md - Key Concepts section

## Q3
**Answer:** C
**Explanation:** The lesson explicitly states: "Don't switch tools mid-project (creates git conflicts)." Legacy projects using poetry/pipenv should stick with their existing tool.
**Reference:** notes/lesson2-uv.md - Best Practices section

## Q4
**Answer:** C
**Explanation:** Package managers handle installation, version management, environment isolation, and reproducibility. Writing application code is the developer's job, not the package manager's.
**Reference:** notes/lesson2-uv.md - Key Concepts section

## Q5
**Answer:** C
**Explanation:** The lesson notes that for "Data science with conda packages," conda might be necessary since it has specialized packages, but "UV is catching up."
**Reference:** notes/lesson2-uv.md - When to Use Which Tool

## Q6
**Answer:** B
**Explanation:** The lesson states: "In AI-driven development, speed matters less for the commands themselves and more for getting feedback fast. Slow tools create friction in the feedback loop. Fast tools keep you in flow."
**Reference:** notes/lesson2-uv.md - Why Speed Matters

## Q7
**Answer:** True
**Explanation:** The lesson explains that "fragmentation isn't a mistake—it's the natural result of different teams solving problems independently." Over 15 years, pip (2008), venv (2011), pipenv (2017), poetry (2018), etc. were created.
**Reference:** notes/lesson2-uv.md - Understanding the Concepts

## Q8
**Answer:** False
**Explanation:** UV eliminates the need for manual activation. `uv run` executes code in the project context automatically. This is listed as a UV advantage: "Runs code in project context (no manual activation needed)."
**Reference:** notes/lesson2-uv.md - UV Commands Quick Reference

## Q9
**Answer:** False
**Explanation:** UV was created by Astral, the company that also created Ruff (a fast Python linter). Astral is an independent company focused on Python tooling.
**Reference:** notes/lesson2-uv.md - Key Concepts section

## Q10
**Answer:** True
**Explanation:** The lesson provides this exact comparison: "On larger projects (50+ dependencies), the difference is even more dramatic: pip might take 2+ minutes, while UV completes in under 10 seconds."
**Reference:** notes/lesson2-uv.md - Speed Comparison table

## Q11
**Answer:** False
**Explanation:** The lesson explicitly warns against this: "Legacy project using poetry/pipenv → Stick with existing tool" and "Don't switch tools mid-project (creates git conflicts)."
**Reference:** notes/lesson2-uv.md - Best Practices section

## Q12
**Answer:**
Beginners get different answers because Python accumulated multiple tools over 15 years (pip, venv, virtualenv, pipenv, poetry, conda), each created by different teams with different philosophies. None became the standard, so experienced developers recommend whichever tool they prefer.

UV addresses this by providing a unified solution—one tool that handles everything (packages, environments, locking, Python versions). Instead of choosing between fragmented tools, beginners can just use UV as the modern default.
**Reference:** notes/lesson2-uv.md - The Fragmentation Problem

## Q13
**Answer:**
**Traditional pip/venv workflow:**
1. Create virtual environment (confusing: venv? virtualenv? pipenv?)
2. Activate it (different commands for Windows/Mac/Linux)
3. Install packages (slow, 8-12+ seconds each)
4. Create requirements.txt manually
5. Teammate may get different versions

**UV workflow:**
1. `uv init my-project`
2. `uv add requests`
3. Done. Teammate runs `uv sync`

**Pain points eliminated:**
- No confusion about which tool to use
- No platform-specific activation commands
- 10-100x faster installation
- Automatic lock file generation
- Guaranteed identical environments for team
**Reference:** notes/lesson2-uv.md - Practical Applications

---
Source: lessons/lesson2-uv.md
Question count: 13
Difficulty: Intermediate
