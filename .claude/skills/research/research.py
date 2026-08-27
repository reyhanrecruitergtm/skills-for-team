#!/usr/bin/env python3
"""
RecruiterGTM Research Skill
Calls Perplexity API with full business context injected.
Usage: python research.py "topic" --purpose "general|market|competitor|sales|content"
"""

import sys
import os
import json
import argparse
import urllib.request
import urllib.error
import re
from datetime import date
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parents[3]  # EA Demo root
CONTEXT_DIR = BASE_DIR / "context"
PROJECTS_DIR = BASE_DIR / "projects"
RESEARCH_DIR = BASE_DIR / "research"
ENV_FILE = BASE_DIR / ".env"

# ── Load .env ─────────────────────────────────────────────────────────────────

def load_env():
    if not ENV_FILE.exists():
        print("ERROR: .env file not found. Create one at the project root with PERPLEXITY_API_KEY=...")
        sys.exit(1)
    env = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env

# ── Read context files ────────────────────────────────────────────────────────

def read_file_safe(path):
    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception:
        return ""

def build_business_context():
    parts = []

    me = read_file_safe(CONTEXT_DIR / "me.md")
    if me:
        parts.append("=== WHO I AM ===\n" + me)

    work = read_file_safe(CONTEXT_DIR / "work.md")
    if work:
        parts.append("=== MY BUSINESS ===\n" + work)

    priorities = read_file_safe(CONTEXT_DIR / "current-priorities.md")
    if priorities:
        parts.append("=== CURRENT PRIORITIES ===\n" + priorities)

    goals = read_file_safe(CONTEXT_DIR / "goals.md")
    if goals:
        parts.append("=== GOALS ===\n" + goals)

    # Active projects
    if PROJECTS_DIR.exists():
        project_names = [
            p.name for p in PROJECTS_DIR.iterdir()
            if p.is_dir() and not p.name.startswith(".")
        ]
        if project_names:
            parts.append("=== ACTIVE PROJECTS ===\n" + "\n".join(f"- {p}" for p in project_names))

    return "\n\n".join(parts)

# ── Slugify topic ─────────────────────────────────────────────────────────────

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60]

# ── Call Perplexity ───────────────────────────────────────────────────────────

PURPOSE_INSTRUCTIONS = {
    "general":    "Provide a comprehensive deep-dive with actionable insights.",
    "market":     "Focus on market size, trends, key players, and opportunities for a recruitment GTM business.",
    "competitor": "Analyse this as a competitor or tool. Cover: what it does, who uses it, pricing, strengths, weaknesses, and how it compares to Clay, n8n, Lemlist, and HeyReach.",
    "sales":      "Research this prospect or company from a sales perspective: what they do, company size, likely pain points, recent news, and how RecruiterGTM's offer would resonate.",
    "content":    "Research this topic to inform high-quality LinkedIn and YouTube content. Surface data, stats, contrarian angles, and expert perspectives.",
}

def call_perplexity(api_key, topic, purpose, business_context):
    purpose_instruction = PURPOSE_INSTRUCTIONS.get(purpose, PURPOSE_INSTRUCTIONS["general"])

    system_prompt = f"""You are a senior research analyst working exclusively for Reyhan Khan and his business RecruiterGTM.

You have deep knowledge of his business, team, and priorities. Every research report you produce must be:
- Specific to Reyhan's context (recruitment agencies, GTM systems, offshore talent)
- Actionable -- include clear implications and recommended next steps
- Structured with clear sections
- Citing real sources

{business_context}

Research purpose for this request: {purpose_instruction}

Always end your response with:
1. A "Key Takeaways" section (3-5 bullets)
2. A "Recommended Actions for Reyhan" section (specific to his business and current priorities)"""

    payload = json.dumps({
        "model": "sonar-deep-research",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Research this topic in depth: {topic}"}
        ],
        "temperature": 0.2,
        "return_citations": True,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.perplexity.ai/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"ERROR: Perplexity API returned {e.code}: {body}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Could not reach Perplexity API: {e.reason}")
        sys.exit(1)

# ── Save output ───────────────────────────────────────────────────────────────

def save_research(topic, purpose, content, citations):
    RESEARCH_DIR.mkdir(exist_ok=True)
    today = date.today().isoformat()
    slug = slugify(topic)
    filename = f"{today}-{slug}.md"
    filepath = RESEARCH_DIR / filename

    citation_block = ""
    if citations:
        citation_block = "\n\n## Sources\n" + "\n".join(f"- {c}" for c in citations)

    output = f"""# Research: {topic}

**Date:** {today}
**Purpose:** {purpose}

---

{content}{citation_block}
"""

    filepath.write_text(output, encoding="utf-8")
    return filepath

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="RecruiterGTM Research Skill")
    parser.add_argument("topic", help="What to research")
    parser.add_argument(
        "--purpose",
        choices=["general", "market", "competitor", "sales", "content"],
        default="general",
        help="Type of research (shapes the output)"
    )
    args = parser.parse_args()

    env = load_env()
    api_key = env.get("PERPLEXITY_API_KEY", "")
    if not api_key or api_key == "your_key_here":
        print("ERROR: Add your Perplexity API key to .env: PERPLEXITY_API_KEY=pplx-...")
        sys.exit(1)

    print(f"Building business context from context files...")
    business_context = build_business_context()

    print(f"Calling Perplexity (sonar-deep-research) on: \"{args.topic}\"")
    print("This may take 30-60 seconds for deep research...")

    result = call_perplexity(api_key, args.topic, args.purpose, business_context)

    content = result["choices"][0]["message"]["content"]
    citations = result.get("citations", [])

    filepath = save_research(args.topic, args.purpose, content, citations)

    print(f"\nDone. Saved to: {filepath.relative_to(BASE_DIR)}")
    print("\n" + "="*60)
    print(content[:1500] + ("..." if len(content) > 1500 else ""))
    print("="*60)
    print(f"\nFull report: {filepath}")

if __name__ == "__main__":
    main()
