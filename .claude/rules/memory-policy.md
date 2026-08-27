# Memory Policy

The default auto-memory behavior produces fragmentation: every new piece of feedback becomes its own `feedback_*.md` in `/memory/`. Over time this scatters skill-specific rules across dozens of files and makes the workspace unscalable.

**This policy overrides the default auto-memory behavior for this workspace.**

> **Memory now lives in the wiki: `memory/wiki/`** (Karpathy-style knowledge base — see `memory/wiki/wiki-CLAUDE.md`). The old flat `/memory/*.md` files are a frozen pre-migration backup — do NOT write new files there. New memory goes into the right `memory/wiki/<domain>/` folder, gets an entry in `memory/wiki/index.md`, and a line in `memory/wiki/log.md`. Domains: `clients/ offers/ team/ projects/ references/ rules/ personal/ research/`.

---

## Where feedback goes

### Skill-specific feedback → into the skill's SKILL.md

If a rule only applies when a specific skill is invoked, it belongs **inside that skill's `SKILL.md`**, NOT in `/memory/`.

Examples:
- "Every proposal must include 10 sample candidates" → `proposal-generator/SKILL.md`
- "Never use 'Here is the kicker.' fragments in LinkedIn posts" → `content-os/SKILL.md`
- "Always create Gmail draft when proposal finalized" → `proposal-generator/SKILL.md`
- "Verify LinkedIn URLs before CSV export" → `sourcing-os/SKILL.md`

Each `SKILL.md` has (or gets) a **`## Locked Rules`** section near the top of the file (right after "What This Skill Does"), grouped into lettered sections (A, B, C…) the way `content-os/SKILL.md` already does. New rules are added as one-liners to the relevant section.

### Cross-cutting feedback → `memory/wiki/rules/` + one line in `CORE.md`

A rule is cross-cutting only if it applies regardless of which skill is running. Examples:
- `feedback_never_auto_open_files.md` — applies to every `open` command
- `feedback_never_send_emails.md` — applies to every email tool call across skills
- `feedback_no_talent_placement_online.md` — positioning rule that constrains every artifact
- `feedback_attio_dedup.md` — Attio behavior that applies to every Attio call
- `feedback_preflight_check.md` — universal stat-verification rule

Put the detailed file in `memory/wiki/rules/` and add a one-line summary (with a `[[wikilink]]` to it) under the right heading in `memory/wiki/CORE.md` — CORE is the only rules file loaded every session.

If unsure, ask: "does this rule fire only when one specific skill is invoked?" If yes → skill file. If no → wiki rules + CORE.

### Projects, references, user notes → the matching `memory/wiki/` folder

This policy only changes where **feedback** goes. Project, reference, and personal memories are one note each in `memory/wiki/projects/`, `references/`, or `personal/` respectively — not skill-bound, but they live in the wiki (indexed + linked), not the frozen `/memory/` backup.

---

## Adding a new rule (going forward)

1. Decide: skill-specific or cross-cutting?
2. **Skill-specific:** open the skill's `SKILL.md`, find the right section under `## Locked Rules`, add a one-liner. Do NOT create a new file anywhere in memory.
3. **Cross-cutting:** create `memory/wiki/rules/feedback_<name>.md` with the standard frontmatter, add a one-line summary + `[[wikilink]]` to it under the right heading in `memory/wiki/CORE.md`, and add it to `memory/wiki/index.md`.
4. If no matching section exists in the skill file, add the section and the rule together.
5. Non-rule memory (project/reference/personal): create the note in the matching `memory/wiki/<domain>/` folder, wire `[[links]]`, and index it. Append a line to `memory/wiki/log.md`.

---

## Why this policy exists

- Skill files are loaded when the skill is invoked. Rules that constrain that skill should travel with it.
- `/memory/` is loaded every conversation. Filling it with skill-specific rules wastes context.
- 50+ fragment files in `/memory/` made the workspace unscalable. Consolidation into skill files was completed on 2026-05-11.
- See `content-os/SKILL.md` for the canonical pattern (sections A through K).
