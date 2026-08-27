# Skill: OutboundOS-Claude

Claude-native version of OutboundOS. Replaces Clay with local data files + Claude Max reasoning + a 2-source enrichment waterfall. Same 4-phase output as the Clay-based skill, but the entire pipeline runs inside Claude Code with no SaaS workflow tool in between.

Inspired by the YALC architecture (Othmane Khadri's open-source GTM OS) — adapted to RecruiterGTM's playbook menu, ICP language, and proposal benchmarks.

**Runs on the canonical [Nowoslawski architecture](../../../memory/wiki/references/reference_nowoslawski_architecture.md) — split work by cost + risk:**
- Cheap, invisible work (TAM, enrichment, qualification) runs in Claude Code with **parallel Task sub-agents (no external API key)** and persists to **Pulse**.
- The **prospect-facing personalisation line** is generated through the approval-looped [personalization-subagent-pattern](../personalization-subagent-pattern/SKILL.md), run through `copy-engine`.
- **Nothing exports until it clears the [list-quality-scorecard](../list-quality-scorecard/SKILL.md) QA gate.** Never let a vibe-coded pipeline touch what the prospect sees.

---

## When to Use

- Client is on the Claude-Code-DFY tier (technical enough to run a CLI / bash scripts)
- Client wants a lean stack (Claude + 2 enrichment sources, no Clay subscription)
- Reyhan says "set up OutboundOS-Claude for [client]"
- Any time `/outbound-os-claude` is invoked

**When NOT to use:** standard OutboundOS retainers where Salar/Shmookh operate the day-to-day. Use [outbound-os-setup](../outbound-os-setup/SKILL.md) instead — that workflow is built around Clay tables our team is already fluent in, and protects the Clay affiliate revenue line.

---

## Architecture

```
┌────────────────────────────────────────────────────┐
│  Claude Max (parent session)                       │
│  ↳ Plans, qualifies, personalises, validates       │
├────────────────────────────────────────────────────┤
│  Local data plane: ./data/clients/<slug>/          │
│  ↳ tam.csv · contacts.jsonl · qualified.jsonl      │
│  ↳ copy/ · campaigns/ · intelligence/              │
├────────────────────────────────────────────────────┤
│  Enrichment waterfall (3 sources per client)       │
│  ↳ Default: Prospeo (PRO, 15k credits/mo, $0) →    │
│    Apollo → Apify (LinkedIn scrape)                │
│  ↳ Configurable per client in clients/<slug>.yaml  │
├────────────────────────────────────────────────────┤
│  Send layer: Instantly (email) + HeyReach (LI)     │
│  ↳ CSV handoff, no direct API send from this skill │
└────────────────────────────────────────────────────┘
```

**Key swap vs Clay version:**

| Clay version | Claude version |
|---|---|
| Clay TAM table | `data/clients/<slug>/tam.csv` |
| Claygent AI columns | Claude qualifier prompt run over JSONL |
| Clay waterfall (50+ providers) | 2 sources, configured per client |
| Clay → Lemlist push | CSV export → Instantly/HeyReach upload |
| Clay run history | `intelligence/` folder per client (what worked, what didn't) |

---

## How to Invoke

1. Open or create the client config: `.claude/skills/outbound-os-claude/clients/<slug>.yaml`
2. Paste the intake doc into the conversation
3. Say `/outbound-os-claude` or "let's set up OutboundOS-Claude for [client]"

---

## The 4 Phases

### Phase 1 — TAM Build

**Goal:** Generate a target company list using the client's 2 enrichment sources (no Clay).

**Steps:**
1. Parse intake doc → ICP filters: industries, headcount, geo, inclusion/exclusion keywords, decision-maker titles
2. Pick the right source for company discovery:
   - **Apollo** — standard for SaaS / B2B services / agency targets
   - **Crustdata** — deeper for funded startups, hiring signals, intent
   - **Apify** — LinkedIn-derived lists (Sales Nav exports, post engagers, group members)
   - **PeopleDataLabs** — when client wants enrichment depth over discovery
3. Output the **API call config** (not a Clay filter spec — the actual JSON body for the chosen API)
4. Estimate TAM size from API count endpoint before spending credits
5. Write results to `data/clients/<slug>/tam.csv`

**TAM rotation rule still applies:** TAM ÷ 3 = companies/month during pilot. Tag each row with its monthly band.

---

### Phase 2 — Client Review & Approval

**Goal:** Sign-off on the TAM before spending enrichment credits.

Same as Clay version — produce plain-English summary, flag ambiguities, draft Slack/email message via [email-writer](../email-writer/SKILL.md), wait for approval.

**Checkpoint:** No Phase 3 enrichment until client approves. Credits are real money.

---

### Phase 3 — Playbook Selection

Identical to Clay version. Use the standard menu:

| Playbook | Signal |
|---|---|
| LinkedIn Jobs | Company is actively hiring |
| Leadership Change | New DM joined in last 90 days |
| Low Internal HR Ratio | <1% of staff in HR roles |
| 90-Day Job Change | Contact changed roles recently |
| Talent Replacement Backfills | Same role re-posted after short tenure |

Output the recommended playbooks with rationale per playbook.

---

### Phase 4 — Playbook Execution

**Goal:** For each playbook, run the 2-source enrichment waterfall + Claude qualifier + Claude personaliser, then export a clean CSV ready for Instantly/HeyReach.

**Pipeline per playbook:**

1. **Filter TAM** to companies that match the playbook signal (e.g. hiring filter via Apollo job postings endpoint)
2. **Find decision-makers** at each company using Source 1 (default Apollo people search by title)
3. **Enrich emails / LinkedIn** using Source 2 (default Apify LinkedIn URL scraper for verification + Prospeo fallback if email missing)
4. **Claude qualifier** — run a structured prompt over each contact JSONL row. Output: `qualified: yes/no`, `qualifier_reason`, `icp_score 1-10`
5. **Personalise via [personalization-subagent-pattern](../personalization-subagent-pattern/SKILL.md)** — never hand-write 500 lines then find the prompt was wrong. Sample on 1 → approve → batch of 10 → approve → 2 clean rounds locks the prompt → fan out **parallel Claude Code Task sub-agents (no external API key)** to generate `personalisation_line_1` + `personalisation_line_2` per qualified contact, grounded in the playbook signal (hiring → "saw you opened the [role] req"; leadership change → "saw [name] joined as [title] in [month]"). Every line obeys `copy-engine` (banned phrases + rubric).
6. **Export CSV** — columns ready for the send tool. No empty-comma column shifts. (Gated by Phase 4B.)

**Per-row JSONL schema** (write to `data/clients/<slug>/contacts.jsonl`):

```jsonc
{
  "company": "...",
  "domain": "...",
  "linkedin_company": "https://linkedin.com/company/...",
  "playbook_signal": "hiring | leadership_change | ...",
  "signal_evidence": "Open req: Senior RecOps, posted 2026-04-22",
  "contact": { "name": "...", "title": "...", "linkedin": "https://linkedin.com/in/...", "email": "..." },
  "enrichment_source_1": "apollo",
  "enrichment_source_2": "apify",
  "qualified": true,
  "qualifier_reason": "...",
  "icp_score": 8,
  "personalisation_line_1": "...",
  "personalisation_line_2": "..."
}
```

---

### Phase 4B — Data Verification (MANDATORY before export)

Identical rule to Clay version: **no CSV leaves this skill without a verification pass.**

1. HTTP-verify every LinkedIn URL (200 valid, 999 LinkedIn rate-limit flag, anything else fix or drop)
2. MX-check every email domain
3. Check CSV column alignment — empty fields with commas shift columns
4. Output verification summary: total rows, valid URLs, invalid URLs, missing emails
5. **Run the [list-quality-scorecard](../list-quality-scorecard/SKILL.md) QA gate** — `python3 ../list-quality-scorecard/score_list.py --list export.csv --titles "…" --industries "…" --headcount-min … --headcount-max …`. **Grade < B → do NOT export.** Fix the flagged issues (dedupe, 100% verification, bad titles, First/Last split, ICP drift) and re-run. This is the prospect-boundary checkpoint.

See [feedback_verify_linkedin_urls.md](../../../memory/feedback_verify_linkedin_urls.md).

---

## Per-Client Config

Each client gets their own config file at `clients/<slug>.yaml`:

- Which 2 enrichment sources they're licensed for
- API key env var names
- ICP from intake doc
- Playbook selection
- Send tool (Instantly / HeyReach / both)

Template: [client-config-template.yaml](client-config-template.yaml)

Active clients:
- **Ozgur** → [clients/ozgur.yaml](clients/ozgur.yaml) — first test client, Claude Max + Apify + Apollo

---

## Hard Rules (carried over from OutboundOS)

- TAM rotation: TAM ÷ 3 = companies/month, label "(1/3 TAM)" on every batch
- Verify all LinkedIn URLs before any export ([feedback_verify_linkedin_urls.md](../../../memory/feedback_verify_linkedin_urls.md))
- Use [email-writer](../email-writer/SKILL.md) for any client-facing email at every checkpoint
- All affiliate-able tools in client deliverables use our affiliate links ([reference_affiliate_links.md](../../../memory/reference_affiliate_links.md)) — Apollo and Apify both qualify
- Never invent candidate / company numbers ([feedback_no_inflated_numbers.md](../../../memory/feedback_no_inflated_numbers.md))
- Never promise team-wide training ([feedback_never_promise_team_training.md](../../../memory/feedback_never_promise_team_training.md)) — scope is the single founder/CEO

---

## Intelligence Loop (YALC-inspired)

After each campaign batch, append a JSONL row to `data/clients/<slug>/intelligence/learnings.jsonl`:

```jsonc
{
  "date": "2026-05-09",
  "playbook": "hiring",
  "batch_size": 200,
  "qualified_rate": 0.62,
  "reply_rate": 0.071,
  "positive_reply_rate": 0.024,
  "winning_subject_line": "...",
  "losing_subject_line": "...",
  "hypothesis_validated": true,
  "notes": "..."
}
```

This becomes the per-client memory the next batch reads before generating new copy. Mirrors YALC's intelligence store concept without the SQLite/Drizzle overhead — plain JSONL is enough at our scale.

**Persistence (Nowoslawski v2 route):** for accounts **we manage**, also persist TAM + contacts + these learnings to **Pulse** (our Supabase) so the campaign lives in the internal OS alongside the client's other data. Standalone Claude-Code-DFY clients running their own stack keep it local as plain JSONL. Same schema either way.

---

## Reference

- [YALC repo](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system) — architecture inspiration
- [outbound-os-setup](../outbound-os-setup/SKILL.md) — Clay-based sibling skill
- [deepline/](../../../deepline/) — internal enrichment helpers (existing)
