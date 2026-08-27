# Skill: Research

Deep research using Perplexity's sonar-deep-research model. Context-aware -- automatically injects Reyhan's business, priorities, and active projects into every query.

---

## When to Use This Skill

Use this skill (not a basic web search) when:
- Reyhan asks to "research", "look into", "dig into", or "find out about" something
- Pre-call prospect or company research is needed
- Competitive tool or platform analysis is requested
- Market trend or industry analysis
- Content research for LinkedIn posts or YouTube videos
- Any research that benefits from citing real, sourced information

Do NOT use this for: simple factual lookups, quick definitions, or things answerable from existing context files.

---

## How to Invoke

```bash
python .claude/skills/research/research.py "topic here" --purpose [purpose]
```

### Purpose flags:
| Flag | Use when |
|------|----------|
| `general` | Default. Comprehensive deep-dive. |
| `market` | Market size, trends, players, opportunities |
| `competitor` | Analysing a tool, platform, or competitor |
| `sales` | Prospect/company research before a sales call |
| `content` | Research to fuel LinkedIn or YouTube content |

### Examples:
```bash
python .claude/skills/research/research.py "Pin.com vs Clay for candidate sourcing" --purpose competitor
python .claude/skills/research/research.py "recruitment agency market UK 2026" --purpose market
python .claude/skills/research/research.py "Amplis agency founder Tyler Mounce" --purpose sales
python .claude/skills/research/research.py "AI adoption in recruitment statistics 2025" --purpose content
```

---

## What the Script Does

1. Reads `.env` for the Perplexity API key
2. Loads all context files (`context/me.md`, `context/work.md`, `context/current-priorities.md`, `context/goals.md`) and active project names
3. Injects that context into the system prompt so Perplexity understands who Reyhan is and what matters to him
4. Calls `sonar-deep-research` (multi-step deep research with citations)
5. Saves the full report to `research/YYYY-MM-DD-[topic-slug].md`
6. Prints a preview to the terminal

---

## After Running

1. Read the saved file from `research/`
2. Synthesize and present key findings to Reyhan in his preferred format (bullets, short paragraphs)
3. Add a **"Relevance to RecruiterGTM"** section based on what you know about his current priorities
4. If the research is strong enough to inform a decision, offer to log it in `decisions/log.md`
5. If it's relevant to a specific project, offer to add a summary to that project's `README.md`

---

## Output Location

All research reports saved to: `research/YYYY-MM-DD-[topic-slug].md`

These accumulate over time and become a searchable knowledge base.

---

## API Key

Stored in `.env` at the project root. Already git-ignored. Never commit this file.
