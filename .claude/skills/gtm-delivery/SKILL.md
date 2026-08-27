# GTM Delivery Skill

Reyhan's weekly delivery-management system for retainer clients. Keeps every GTME focused on the right accounts, gives them concrete ideas/experiments per account each week, and makes sure every client is on track for a **complete recruitment-systems transformation** — not just campaign results — against the DeliveryOS 90-day timeline.

This is the skill Reyhan runs to do what he already does manually every week (see the Shmookh example in `examples/shmookh-weekly-review.md`): look across each GTME's book, spot what's behind, give direction, and confirm ownership.

---

## What This Skill Does

Produces, per GTME, a **Weekly Delivery Review** with:
1. A per-account status read against the DeliveryOS timeline + the Transformation Standard.
2. Gap analysis — where each account is behind, where comms/sentiment are slipping.
3. 2–3 concrete ideas/experiments to test that week (from `experiments-bank.md`).
4. A clear, dated **Focus of the Week** per account.
5. A **GTME coaching message** drafted in Reyhan's voice, ready to paste into Slack.
6. An updated **Transformation Scorecard** per client.

The review is the source of truth; the coaching message and scorecard are derived from it.

---

## Locked Rules

### A. The Transformation Standard (every retainer client, every engine)
Every retainer client — OutboundOS, SourcingOS, or ContentOS — must be driven toward ALL of these, not just their core engine. This is what makes it feel like a transformation instead of "we ran some campaigns":
1. **Claude Ops Manager** set up for their operations + daily productivity.
2. **Claude connected to ALL their tools** (ATS, CRM, email, LinkedIn, sheets) so the client can *operate from inside Claude* — this is the transformation feeling, non-negotiable.
3. **GTM engine live and delivering results** (the core — outreach/sourcing/content).
4. **≥4 signals launched** (signal-triggered campaigns — never fewer than 4).
5. **1 lead magnet** (salary guide, market map, report, etc.).
6. **A newsletter** (in most cases — nurture the database/audience).
7. **Weekly reporting call** + 12-month community access (already in every agreement).

Track all 7 on the scorecard for every client. A client missing #1/#2/#4/#5/#6 is behind on transformation even if the engine is "working."

### B. Ownership & cadence
- B1. **One clear owner per account.** Name support roles explicitly (e.g. "Daniyal = implementation support"). Ambiguity is the #1 cause of dropped balls — the Justin W confusion happened because primary/support wasn't locked.
- B2. **Run weekly.** Each GTME gets a review + a focus-of-week every week.
- B3. **Confirm the roster against Attio every run** — owners and engines change. Never assume last week's book.
- B4. When a client is too high-maintenance for the assigned GTME, escalate the ownership decision to Reyhan (e.g. Justin W stays with Shmookh + Daniyal support, not Komal — Komal can't take a panicky client right now).

### C. DeliveryOS timeline adherence
- C1. Every account is mapped to its DeliveryOS milestone + phase (see `## DeliveryOS Timeline`). Flag any account behind its expected milestone for its day-count.
- C2. The 90-day clock starts at deal-closed date (from Attio). Always compute current day = today − deal_closed_date.

### D. Voice (coaching messages)
- D1. Reyhan's internal voice: direct, "bro," bullets, lead with the problem, name the specific number/fact ("0 campaigns on LinkedIn and only 1 on email"), end by asking the GTME how they're approaching it. No corporate softening. See `examples/shmookh-weekly-review.md`.
- D2. Be specific and evidence-based — quote the actual gap (campaign counts, win counts, engagement %, client complaints), never vague "do better."
- D3. Always close the loop: the GTME replies with their focus-of-week; Reyhan adjusts ownership/strategy. The skill supports both directions.

### E. Data sources
- Attio (active retainers, deal-closed dates, deal value, owner) · Slack (client channels for campaign activity + sentiment; team DMs) · Fireflies (client call notes) · Pulse (tasks/accountability) · DeliveryOS (milestones/targets, when queryable — Daniyal owns). Cross-check stats before writing (`feedback_preflight_check`). Never auto-send Slack messages — draft for Reyhan's approval.

---

## Current Roster — from Pulse / DeliveryOS

_Source of truth: the DeliveryOS Supabase `retainers` table (Pulse) + `retainer_members` joined to `profiles`. **Lead GTME = the member whose profile role is `team`** (Shmookh / Komal); `admin` = Reyhan (strategy) + Daniyal (operations@, automation). Pulled 2026-06-22. Re-query each run — Pulse is authoritative for roster + onboarding + engine; cross-check the gaps below._

| Client | Company | Engine(s) | Lead GTME | Onboarded |
|---|---|---|---|---|
| Duncan Seward | IRG Law | OutboundOS | Shmookh | 10 Dec 2025 (ongoing) |
| Georgiana Larg | Transilvania HR | OutboundOS | Shmookh | 15 Jan 2026 (ongoing) |
| Daniel Cheetham | Captains Club | OutboundOS | Komal | 22 Apr 2026 (+7) |
| Phil Feigenbaum | Huffman Associates | OutboundOS | ⚠️ none (Reyhan + Daniyal only) | 27 Apr 2026 |
| Justin D'Aleo | Sourcera | OutboundOS + ContentOS | Shmookh | 28 Apr 2026 |
| Paul Lingle | TriPax Resources | SourcingOS | ⚠️ none (Reyhan + Daniyal only) | 28 Apr 2026 |
| Patrick How | HowRecruit | OutboundOS + ContentOS | Shmookh | 4 May 2026 (+7) |
| Justin Williams | Ethix Staffing | OutboundOS + SourcingOS | Shmookh (primary) + Daniyal support | 22 May 2026 |
| April Ben-sabat | Inner Circle Agency | OutboundOS | Komal | 4 Jun 2026 |
| Mohammad Adris | Responsum | SourcingOS | Komal | 8 Jun 2026 |
| Adrian Munoz | AlacHR Solutions | OutboundOS (VIP) | Komal | 15 Jun 2026 (+10) |
| Christina Martins | Martins Investment Group | OutboundOS | Shmookh | date TBC in Pulse |
| Özgür Özen | Vincuro | OutboundOS (Claude-DFY) | Daniyal | date TBC in Pulse |

**By GTME:** Shmookh → Duncan, Georgiana, Justin D'Aleo, Patrick How, Christina, Justin W (primary). Komal → Responsum, Captains Club, Adrian, April. Daniyal → Vincuro + automation/implementation across all.

**Pulse data gaps (fix with Daniyal):**
- Justin D'Aleo (Sourcera) has **no `retainer_members` row** — add Shmookh.
- Phil Feigenbaum + Paul Lingle have **no `team` GTME** (only Reyhan/Daniyal admins) — assign a lead.
- Justin Williams still lists Komal as a member — per the ownership call she's off it: Shmookh primary + Daniyal support.
- Christina Martins + Özgür Özen have **no `onboarding_date`** → can't compute timeline.

> Salar left 2026-06-16 — don't assign to him. See `project_team_roles_june`.

---

## DeliveryOS Timeline (the yardstick)

Source of truth: `projects/deliveryos/deliveryos-schema.md`. Map every account to this.

| Milestone (`key`) | Day | Means |
|---|---|---|
| `access_collected` | D0–7 | Onboarding intake + tool access gathered |
| `baseline_d30` | D30 | First launch live, baseline volume hit |
| `responses_d60` | D60 | Optimised, second launch, first positive replies |
| `report_d75` | D75 | Performance report + scale recommendation |
| `renewal_d90` | D90 | Validate, scale winners, renewal conversation |

**Phases / targets:** P1 (M1): 2,000 email + 500 LinkedIn leads · P2 (M2): +1,500 email + 500 LinkedIn · P3 (M3): 5 positive replies (guarantee). SourcingOS swaps leads → **30–50 candidate conversations/mo**; ContentOS → **50k–100k impressions / 25k reach/mo**.

**4-week sprint:** Discovery & Setup → Build → Launch → Full Operation.

---

## Workflow

### Step 1 — Lock the roster
Pull active retainers from Attio (Sales Pipeline 2026, won + active). Confirm owner + engine(s) per account. Flag any account with no clear owner.

### Step 2 — Place each account on the timeline
Compute current day (today − deal-closed). Note expected milestone/phase. This is the yardstick for "behind or on track."

### Step 3 — Read current state per account
For each account pull what's actually happening:
- **Outreach:** campaigns live + volume (Instantly/HeyReach/Lemlist), replies, wins. Quote real counts.
- **Signals:** how many of the ≥4 are live? (X/4)
- **Content (if ContentOS):** posts shipped, engagement % trend, approval-process friction.
- **Transformation Standard:** Claude ops set up? Claude connected to their tools? Lead magnet? Newsletter?
- **Client sentiment + comms:** Slack channel activity, any WhatsApp/escalation complaints, response speed.

### Step 4 — Gap analysis
Compare state vs (a) DeliveryOS milestone for the day-count, and (b) the 7-point Transformation Standard. Name every gap with its evidence.

### Step 5 — Ideas + focus of week
For each account, pull 2–3 experiments to test from `experiments-bank.md` (matched to engine + what's missing). Then write a clear, dated **Focus of the Week**.

### Step 6 — Draft the GTME coaching message
One message per GTME, Reyhan's voice (Rule D), account-by-account, ending with "let me know how you're approaching them." Draft only — Reyhan sends.

### Step 7 — Update the Transformation Scorecard
Per client, update the 7-point scorecard. Surface clients behind on transformation even if the engine is "fine."

---

## Per-Account Review Template

```
### <Client> — <Engine(s)> · Day <N> (<Phase>, expected: <milestone>)
- Outreach: <campaigns live + volume + replies/wins — real numbers>
- Signals: <X/4 live> — <which ones>
- Content: <posts shipped, engagement trend, approval friction>  [ContentOS only]
- Transformation: Claude ops <✓/✗> · tools connected <✓/✗> · lead magnet <✓/✗> · newsletter <✓/✗>
- Client sentiment / comms: <Slack + escalations + responsiveness>
- GAPS vs timeline + standard: <specific, evidence-backed>
- Ideas to test this week: <2–3 from experiments-bank>
- ▶ Focus of the week: <clear, dated, owner + support>
```

## Transformation Scorecard (per client)

```
| Deliverable | Status |
|---|---|
| 1. Claude Ops Manager (ops + productivity) | ✓ / ✗ / in progress |
| 2. Claude connected to their tools | ✓ / ✗ / in progress |
| 3. GTM engine live + results | <summary> |
| 4. ≥4 signals launched | X/4 |
| 5. Lead magnet | ✓ / ✗ |
| 6. Newsletter | ✓ / ✗ / n/a |
| 7. Weekly report cadence | ✓ / ✗ |
```

---

## How To Invoke
- `/gtm-delivery` — full weekly review across all GTMEs.
- `/gtm-delivery Shmookh` (or any GTME) — review just that person's book.
- `/gtm-delivery <client>` — deep-dive one account.

Output: the Weekly Delivery Review + the draft coaching message(s) + updated scorecard(s). Save reviews to `~/Desktop/Clients/_delivery-reviews/<YYYY-MM-DD>-<gtme>.md` only if Reyhan wants a record; otherwise keep in chat (`feedback_no_unnecessary_md_files`).

---

## Related
- `experiments-bank.md` — the library of weekly experiments/ideas by engine (read in Step 5).
- `examples/shmookh-weekly-review.md` — the real review thread that defines the voice + depth.
- `.claude/skills/launch-plan/` — how a new account's 90-day plan is built (feeds the timeline).
- `.claude/skills/gtm-engine/` — campaign execution commands (sequence writing, signal scanning, reply handling) the GTMEs run.
- `projects/deliveryos/deliveryos-schema.md` — DeliveryOS milestones/targets source of truth.
- `context/team.md`, `project_team_roles_june` — current roster/ownership.
