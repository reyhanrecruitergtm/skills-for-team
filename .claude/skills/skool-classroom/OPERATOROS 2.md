---
name: OperatorOS canonical module list
description: Locked module list and key sections for the OperatorOS Skool classroom. Source of truth — do not add, remove, or renumber without explicit ask from Reyhan.
---

# OperatorOS — Locked Module List (May 5 2026)

**File:** `projects/skool-courses/operator-os/operator-os.html`
**Mirror:** `~/Desktop/Skool Courses/operator-os.html`
**Total modules:** 8 + 1 bonus

## The 8 modules

| # | Title | Key sections |
|---|---|---|
| 1 | Who is a Lean Operator | The problem, definition, 3 shifts, day in the life, traits, leverage scorecard |
| 2 | Project Management & Operating Rhythms | Lean Project System, Mon/Fri calls, priority stack (High/Med/Low), 3 Notion workspaces, Notion+Slack+Claude stack, daily/weekly/monthly rhythm cards, week-in-the-life calendar grid, EOD reports + Slack mock + auto-reminder |
| 3 | Resource Management & KPIs | Money (~$1k/mo stack), Time (Buyback Principle + Pain Line), Team (future-proof structure), Hire/Outsource/AI/Kill, Drucker quote, Ops Integrator + Junior Recruiter KPI tables, Mon/Fri agendas, Notion vs Trello, 4 self-accountability rituals |
| 4 | SOPs & Documentation | Why docs are leverage, 7-section SOP template, 5 must-have SOPs (Sourcing / Interview / Client Onboarding / Submittal / Weekly Reporting), Loom-to-SOP in 10 mins |
| 5 | Hiring & Onboarding the Lean Team | The 2 lean roles (Jr Recruiter + GTM Engineer), trait maps, AI-proof assessments per role, salary benchmarks (PK + SA), where to source, JD templates, 5-question interview rubric, 30-day onboarding (Mon/Fri calls + daily first 2 weeks), 2-week fire-fast window, Wise/Deel payment mechanics, the $3k "hire through us" option |
| 6 | Claude Ops Manager — what it is + setup (CORE) | Chat vs Cowork vs Code (sandbox vs your-machine framing), 5 context files, 6 skills (Daily Brief / Dashboard Report / Follow-Up Writer / Candidate Sourcing Pack / Business Coaching / Market Researcher), MCP connectors, install playbook |
| 7 | 5 Live Demos (Tella-ready, step-by-step) | (1) Sourcing a live role end-to-end · (2) **Categorize LinkedIn 1st connections into warm outreach list** · (3) Spin up a new website page · (4) Build a client proposal in one prompt · (5) Claude as your business coach. Each demo gives exact on-screen steps + prompts for live recording. |
| 8 | Firefighting & Exception Handling | Who handles which fire (CEO / Ops Integrator / Junior Recruiter), 4-level escalation ladder, 15-minute rule, post-mortem template, every fire becomes an SOP |

## Bonus

- **The Operator's Library** — 24 books across 6 categories curated by Tyson Franco. EPUB attached in Skool. Includes Tyson Franco shout-out section.

## Modules that DO NOT exist (and must not be re-added)

- ~~Client Onboarding & Service Delivery~~ — removed May 5 2026. This was internal RecruiterGTM process, not student-facing. Course teaches recruiters to run their business; not how WE deliver to clients.
- ~~Operating Rhythms~~ as a standalone — folded into Module 2.
- ~~KPIs & Reporting~~ as a standalone — folded into Module 3.
- ~~Delegation & Buyback~~ as Module 5 — repealed May 6 2026. Buyback Principle + Pain Line + AI/offshore delegation split was overlapping with Module 3. Module 5 replaced with Hiring & Onboarding the Lean Team. Module 3 keeps Buyback/Pain Line content as recorded.

## Linked assets

- **GTM Engineer Assessment (existing):** Google Doc `118bi3IyLR7nazSpPiFOb_zY7VvZKQPYutCYGf9ulXjU` — "The RecruiterOS Challenge". Open AI assessment, 3 scenarios + 3-min Loom + evaluation rubric.
- **Jr Recruiter Assessment:** Google Doc created May 6 2026 (see `manage_drive search` for "Jr Recruiter Assessment"). Open AI assessment, 4 scenarios + 3-min Loom + evaluation rubric.

## Verification commands

```bash
cd "/Users/reyhankhan/Library/CloudStorage/GoogleDrive-reyhan@recruitergtm.com/My Drive/EA Demo/projects/skool-courses/operator-os"
grep -cE '<!-- MODULE [0-9]+ —' operator-os.html         # expect 8
grep -cE 'Module [0-9]+ Recap' operator-os.html          # expect 8
grep -c 'Your Task This Week' operator-os.html           # expect 8
grep -c "Tyson Franco" operator-os.html                  # expect ≥ 1
```

## Last verified
2026-05-05 — post merge of M2+M7 → new M2, M3+M8 → new M3, M9 deleted, M10 → M7.
