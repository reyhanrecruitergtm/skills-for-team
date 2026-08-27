# GTM Engine Skill

RecruiterGTM's GTM management system. Covers the full outbound lifecycle — from signal scanning and list building to copy writing, reply handling, campaign analysis, and continuous refinement.

Built for recruitment agency owners and their offshore GTM Engineers.

---

## How to Invoke

Say `/gtm-engine` followed by the command name:

- `/gtm-engine write-sequence` — Write a Lemlist/HeyReach outreach sequence
- `/gtm-engine validate-copy` — Run quality check on outreach copy before launch
- `/gtm-engine scan-signals` — Surface live buying signals for a prospect list
- `/gtm-engine handle-replies` — Classify and draft responses to campaign replies
- `/gtm-engine auto-refine` — Update ICP and copy from campaign performance data
- `/gtm-engine campaign-health-check` — Audit deliverability, engagement, pipeline
- `/gtm-engine performance-review` — Full campaign debrief with forward recommendations
- `/gtm-engine ab-test` — Design and analyse A/B tests on subject lines or copy
- `/gtm-engine account-based` — Multi-threaded outreach for a single target account

---

## Context Files (Read Before Any Command)

These files are the source of truth. Always read the relevant ones before executing a command.

| File | What it contains |
|------|-----------------|
| `context/me.md` | Reyhan's background, brand, positioning |
| `context/work.md` | RecruiterGTM offers, pricing, ICP |
| `.claude/rules/communication-style.md` | Tone of voice, copy rules, sign-off block |
| `.claude/skills/outbound-os-setup/clay-reference.md` | TAM build standards, industry filters |
| `.claude/skills/gtm-engine/commands/` | Individual command files |

---

## RecruiterGTM Stack

Always reference these tools when building sequences or recommending infrastructure:

| Purpose | Tool |
|---------|------|
| Data enrichment & TAM | Clay |
| LinkedIn outreach | HeyReach |
| Email outreach | Lemlist |
| Automation | n8n |
| CRM | Attio |
| Project management | Pulse |

---

## Non-Negotiable Rules (Apply to All Commands)

1. **No AI slop.** Copy must sound human. Use 1-2 personalisation variables max — never full AI generation.
2. **No links in cold email.** Tracked links trigger spam filters. Never include URLs in sequences.
3. **Approval gate.** Nothing goes live without Reyhan or the client reviewing it first.
4. **Suppression first.** Always check against existing CRM contacts before adding to a sequence.
5. **ICP match required.** Every list must be scored against ICP criteria before outreach begins.
6. **British English.** All copy uses British spelling and phrasing — not American marketing speak.

---

## Command Routing

```
What do you need?
├─ Write outreach copy → write-sequence
├─ Check copy quality → validate-copy
├─ Find buying signals → scan-signals
├─ Deal with replies → handle-replies
├─ Learn from results → auto-refine
├─ Check campaign health → campaign-health-check
├─ Full debrief → performance-review
├─ Test variations → ab-test
└─ Target one account → account-based
```
