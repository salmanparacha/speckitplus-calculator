
CLAUDE must never ask for feedback. 

# Study Notes Project
## Purpose
Create and organize study materials with professional structure and quality.

## Key Directives

- Primary Goal: Maintain high-quality, well-structured documentation for learning
- Content Standard: Use clear, concise language appropriate for professional reference
- Format: Markdown format with consistent structure

## Directory Structure

```
/lessons/        - Source lesson materials for creating notes
/notes/          - All study notes and documentation
/flashcard/      - Flashcard files for memorization
/quiz/           - Quiz and assessment materials
```

## Content Guidelines

### Lessons Directory
- Contains source materials used as input for creating notes
- Organize by subject or course
- Reference these materials when creating notes

### Notes Directory
- All subject/topic notes go in `/notes/`
- Use consistent filename format (e.g., `01-topic-name.md`)
- Include sections: Overview, Key Concepts, Examples, References
- Maintain clear hierarchy with proper headings

### Flashcard Directory
- Flashcard files go in `/flashcard/`
- Format: Question on one line, Answer on next line
- Organize by subject/topic using subdirectories
- Use clear, factual statements for effective memorization

### Quiz Directory
- Quiz files go in `/quiz/`
- Include question, correct answer, and explanation
- Format multiple choice, true/false, or short answer clearly
- Provide reference to relevant note sections

## Non-Negotiable Rules

- No personal opinions in technical documentation
- Always cite sources for factual information
- Maintain professional tone throughout
- Review for clarity and completeness before finalizing

## Communication Style

- Direct and concise responses
- No feedback requests after answering questions
- Provide actionable information only

## Skills Reference

### browsing-with-playwright

Browser automation skill using Playwright MCP server.

**First-time setup (if browser not installed):**
```bash
npx playwright install chromium
```

**Quick start:**
```bash
# Headless (default in WSL/SSH/CI)
bash .claude/skills/browsing-with-playwright/scripts/start-server.sh

# With visible browser window
bash .claude/skills/browsing-with-playwright/scripts/start-server.sh --headed
```

**Troubleshooting:**

| Issue | Solution |
|-------|----------|
| "Browser not installed" error | Run `npx playwright install chromium` |
| Port 8808 already in use | Run `stop-server.sh` first, or `lsof -ti:8808 \| xargs kill -9` |
| Server starts but navigation fails | Ensure `--headless --no-sandbox` flags (auto-detected in WSL/SSH) |
| Chromium not found | Script auto-finds in `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome` |

**Environment notes:**
- WSL/SSH/CI: Automatically uses `--headless` mode
- Linux non-root: Automatically adds `--no-sandbox`
- The start script auto-detects and configures these flags
