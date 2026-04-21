# RecruiterGTM Claude Code Template

The internal starter kit for the RecruiterGTM team to run Claude Code with our full skill and agent library from day one.

This template ships with:
- **19 skills** covering proposal generation, sourcing, content, email writing, outbound setup, humanizer, and more
- **2 live agents** (research, notion-tasks) running on Claude Haiku
- **Full CLAUDE.md** with business context, tool stack, and rules
- **Context files** (me, work, team, priorities, goals) as templates
- **Communication-style rules**, reference docs, SOPs, templates

It does NOT ship with:
- Personal memory (each person builds their own)
- Client projects, proposals, agreements
- API keys or MCP credentials

---

## Setup (first time)

### 1. Clone this repo

```bash
gh repo clone reyhanrecruitergtm/recruitergtm-claude-template ~/recruitergtm-claude
cd ~/recruitergtm-claude
```

### 2. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Sign in to Claude Code with your Anthropic / Claude.ai account when prompted.

### 3. Copy environment template

```bash
cp .env.example .env
```

Open `.env` and fill in your own API keys. This file is gitignored — your keys stay on your machine.

### 4. Connect your MCP servers

You'll need access to these MCP servers (contact Reyhan for invite links or credentials):

- Attio
- Fireflies
- Gmail / Google Workspace
- Slack
- Notion
- Clay
- Apollo
- Canva

Add each one via the Claude Code settings UI or `claude mcp add <name>`. Do NOT commit `.mcp.json` — it's gitignored.

### 5. Customise `CLAUDE.md` and `context/`

The `CLAUDE.md` file ships with Reyhan's working context as an example. Before your first session:

- Keep the parts about the business, tools, and skills as they are
- Update `context/me.md` to describe your own role and preferences (or leave it for Reyhan-specific setups)

### 6. Start Claude Code

```bash
claude
```

You'll inherit every skill, agent, and rule from this repo. Your memory, proposals, and research stay local and private.

---

## Daily workflow

### Using skills

All skills are auto-available. Examples:

- `/proposal-generator` — paste a Fireflies transcript and build a full HTML proposal
- `/outbound-os-setup` — paste an intake doc and build a Clay TAM
- `/sourcing-os` — full SourcingOS execution engine
- `/candidate-sourcing` — turn a job brief into a Boolean + target list + messaging
- `/email-writer` — paste a thread + purpose, get an email in Reyhan's voice
- `/content-os` — LinkedIn / Skool posts in Reyhan's voice
- `/humanizer` — remove AI signs from any text
- `/graphic-generation` — generate LinkedIn post graphics
- `/research` — Perplexity deep research (requires PERPLEXITY_API_KEY)

Run `claude` and type `/` to see the full list.

### Using agents

Agents run on Claude Haiku in the background for faster / cheaper work:

- **research** — quick web research, auto-invoked on "research this" / "who is X" / "compare A vs B"
- **notion-tasks** — pull / create / update Notion tasks, generate morning brief

### Memory

Your personal memory lives in `~/.claude/projects/<this-repo-hash>/memory/` — not in this repo. Each team member builds their own memory over time. Reyhan's memory is not shared.

### Adding new skills or agents

Build new skills in `.claude/skills/<skill-name>/SKILL.md`. When you push to main, everyone else can pull and get the new skill on their next session.

---

## Keeping in sync

When Reyhan ships new skills, agents, or rules:

```bash
cd ~/recruitergtm-claude
git pull
```

Everything auto-refreshes. Next Claude Code session picks up the changes.

If you build something worth sharing:

```bash
git add .claude/skills/<new-skill>
git commit -m "Add <skill-name> skill"
git push
```

---

## What's in this repo

```
.claude/
  skills/          — 19 skills (proposal-generator, sourcing-os, email-writer, etc.)
  agents/          — 2 agents (research, notion-tasks)
  rules/           — shared behavioural rules (prioritization, communication-style)
  scripts/         — helper scripts used by skills
  settings.json    — shared Claude Code config

context/
  me.md            — role / preferences (customise per user)
  work.md          — business model, revenue, pricing
  team.md          — team roster and contacts
  current-priorities.md  — what we're focused on this quarter
  goals.md         — quarterly goals

templates/
  session-summary.md — template for end-of-session summaries

references/
  sops/            — standard operating procedures
  examples/        — master proposal templates, example outputs
  business-model.md — full business model reference
  playbook.md      — operating playbook

CLAUDE.md          — project instructions (read by Claude Code on every session)
.env.example       — copy to .env and fill in
.gitignore         — excludes memory, projects, env, credentials
```

---

## Questions

Message Reyhan on Slack.
