# Skill: Browser Use

Gives Claude control of a real headless browser. Navigate URLs, click elements, fill forms, extract content from JavaScript-rendered pages, and take screenshots — all as part of a natural language workflow.

---

## How to Invoke

Say `/browser-use` followed by the task. Or describe what you need and Claude will recognise it requires live browser access.

**Examples:**
- `/browser-use check if this URL loads correctly and screenshot it: https://...`
- `/browser-use fill out the contact form at [URL] with these details: ...`
- `/browser-use scrape all the pricing tiers from [URL]`
- `/browser-use log into [dashboard] and tell me the current campaign stats`

---

## Installation

**Runtime:** Python 3.11 + browser-use + Playwright Chromium

```bash
# Already installed on this machine:
python3.11 -m browser_use.skill_cli doctor
```

All commands run via:
```bash
python3.11 -m browser_use.skill_cli [command] [args]
```

---

## Command Reference

### Navigate
```bash
python3.11 -m browser_use.skill_cli open https://example.com
```

### Get page state (URL, title, all interactive elements with index numbers)
```bash
python3.11 -m browser_use.skill_cli state
```

### Take screenshot (returns base64 — pipe to file for viewing)
```bash
python3.11 -m browser_use.skill_cli screenshot --output /tmp/screenshot.png
```

### Click element by index (get indexes from `state`)
```bash
python3.11 -m browser_use.skill_cli click 21
```

### Type text (into currently focused element)
```bash
python3.11 -m browser_use.skill_cli type "hello world"
```

### Type into a specific element
```bash
python3.11 -m browser_use.skill_cli input 5 "text to type"
```

### Press keyboard keys
```bash
python3.11 -m browser_use.skill_cli keys Enter
python3.11 -m browser_use.skill_cli keys "Control+a"
```

### Scroll
```bash
python3.11 -m browser_use.skill_cli scroll down 500
```

### Run JavaScript
```bash
python3.11 -m browser_use.skill_cli eval "document.title"
```

### Go back
```bash
python3.11 -m browser_use.skill_cli back
```

---

## How Claude Uses This Skill

Claude acts as the intelligence. browser-use is the execution engine.

**Workflow for any browser task:**

1. `open [URL]` — navigate to the target
2. `state` — read the page, identify interactive elements and their index numbers
3. `screenshot` — visually confirm what's on screen
4. `click [index]` / `type [text]` / `input [index] [text]` — interact with elements
5. `state` again — confirm the result
6. `screenshot` — capture final state
7. Report findings to user

**Rule:** Always run `state` before clicking anything. Index numbers are assigned dynamically — never guess them.

---

## Use Cases

### Research & Scraping
- Extract pricing from competitor pages
- Pull job listings from boards that block bots
- Read content from pages that require JavaScript to render
- Scrape LinkedIn company data (carefully — respect rate limits)

### QA & Verification
- Check that a deployed landing page renders correctly
- Verify form submissions work end-to-end
- Screenshot a URL and flag visual issues
- Test that a redirect chain resolves correctly

### Form Filling & Automation
- Fill out contact forms
- Submit data to web interfaces that don't have APIs
- Log into dashboards and extract stats

### Live Web Research
- Navigate to a page and read its current content (bypasses training data cutoff)
- Follow links and synthesise information across pages
- Check if a URL is live and what it says

---

## Limitations

- **Login sessions don't persist** between separate invocations (each session starts fresh)
- **CAPTCHAs** will block automation — flag these to the user
- **2FA-protected dashboards** require manual step or pre-stored session cookies
- **Heavy JavaScript apps** may need a `wait` command before `state` reads correctly
- **Screenshots save to /tmp by default** — specify `--output` if you need to keep them

---

## Session Management

Sessions persist within a single conversation turn. To reuse a named session:
```bash
python3.11 -m browser_use.skill_cli --session my-session open https://example.com
python3.11 -m browser_use.skill_cli --session my-session state
```

---

## Output Format

When completing a browser task, report:

```
BROWSER TASK COMPLETE
=====================
URL visited: [URL]
Task: [What was requested]

RESULT:
[What was found / done]

ISSUES FOUND (if any):
[Any errors, broken elements, or anomalies]

SCREENSHOT: [path if saved, or "available on request"]
```
