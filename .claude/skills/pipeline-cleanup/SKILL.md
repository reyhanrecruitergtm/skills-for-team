# Skill: Pipeline Cleanup

Monthly sales-pipeline hygiene. Reads the replies to our latest reactivation/reoffer push (LinkedIn + email), classifies every lead, **shows Reyhan a named summary for approval BEFORE any move**, then executes the Attio moves, logs reason-notes, and drafts a last-call follow-up to the ghosts for approval. Callable in Claude (`/pipeline-cleanup`), via Slack, or via email, and runs monthly on a cron.

---

## What This Skill Does

Turns a warm-but-stale pipeline into a clean one, once a month, without Reyhan babysitting it:

1. **Harvest replies** to the most recent reoffer/reactivation campaign across **both channels** — HeyReach (LinkedIn) + Gmail (email).
2. **Classify** every reoffered lead into a fixed set of buckets (below).
3. **Summarise with exact names + verbatim reasons FIRST** — never move anything before Reyhan signs off.
4. **Execute Attio moves** on approval (disqualify → `Lost`, timing → `90 Day Back Burner`, keep warm ones), and write a **reason-note** on every moved record (verbatim reply + revisit flag).
5. **Produce the "you owe them a reply" list** — warm leads waiting on Reyhan.
6. **Draft last-call follow-ups for the ghosts** (channel-split), post to Slack for approval. **Never auto-send.**

---

## Locked Rules

### A. Approval & safety
- **A1. Summary before any move — ALWAYS.** Produce the named, bucketed summary and get Reyhan's explicit go-ahead before touching Attio. This is the whole point of the skill. Never move first.
- **A2. Never send anything.** Emails = Gmail drafts only; LinkedIn = HeyReach/Slack drafts only. Ghost last-call messages go to Slack for approval, never straight out. (CORE: [[feedback_never_send_emails]])
- **A3. Disqualify ONLY on the two explicit triggers** (see C). Silence ≠ disqualify. Timing/"not now" ≠ disqualify. When a reply is ambiguous, put it in **INCONCLUSIVE** and show Reyhan the verbatim text — do not guess.
- **A4. Voicenotes / empty-body replies can't be read** — HeyReach does not transcribe them. Flag as INCONCLUSIVE with "voicenote — listen in LinkedIn", never infer sentiment.
- **A5. All drafted copy** runs through copy-engine + humanizer + rubrics before it reaches Reyhan (CORE: [[feedback_copy_engine_all_writing]]). Banned phrases apply ([[feedback_banned_copy_phrases]]).
- **A6. Attio dedup / source-of-truth** — Attio is the pipeline source of truth ([[feedback_attio_is_pnl_source_of_truth]]). Match leads to records by **email**, not name (name search returns wrong same-named records).

### B. Data sources
- **B1. Pipeline:** Attio list **Sales Pipeline 2026** — `list_id 59c6844e-264d-490b-b78d-245a1cd7b5f4`, `parent_object = people`, stage attribute slug `stage` (status type).
- **B2. LinkedIn replies:** HeyReach — find the reoffer campaign (`get_all_campaigns` keyword), then `get_conversations_v2` filtered to that campaign. A reply = a `CORRESPONDENT` message dated **≥ campaign start**. Older messages in the thread are history, ignore them.
- **B3. Email replies:** Gmail — the reoffer email subject changes per campaign (Aug 2026 = `"$3,000 off until Friday"`). Batch-search all recipient addresses: `newer_than:<N>d -in:sent (from:a OR from:b OR …)` in chunks of ~15. Read full thread bodies with `get_thread` (PLAIN_TEXT).
- **B4. Recipient list + channel map:** the campaign's project folder, e.g. `projects/community-reoffer-2026-08/` (`community-reoffer-leads.csv` has Bucket/Stage/Email/LinkedIn; `gmail-heyreach-final.csv` has the exact copy sent per lead).
- **B5. Big HeyReach payloads** exceed the token cap — always parse the saved tool-result file with Python/jq, extracting only `{name, sender, createdAt, body}` per message.

### C. Classification buckets (the rubric)
Assign every reoffered lead to exactly one. The two disqualify triggers are Reyhan's rule, verbatim: *"if somebody has said they don't have money… if somebody says they don't want to do it this way, they need to be disqualified."*

| Bucket | Trigger | Attio action |
|--------|---------|--------------|
| **DQ — No budget** | Explicitly can't afford / no budget ("budget won't allow", "wish I could afford") | → `No $$$` + note. Flag 🔁 revisit-warm if they invited future contact. |
| **DQ — Not a fit** | Doesn't want this model / declining the offer ("don't need a community", "sticking with current setup", "won't be of interest", "building my own") | → `DQ` + note. |
| **Follow-up — Warm** | Positive / conditional / wants a call / asked a question | **No stage change** — goes on the "Reyhan owes a reply" list. Book the call / answer the question. |
| **Back Burner — Timing** | Real interest, wrong time ("locked in until Jan", "circle back next year", "keep in touch") | → `90 Day Back Burner` + dated revisit note. |
| **Ghost** | Reoffer delivered, zero reply on either channel | **No stage change this cycle.** Queue the last-call follow-up. Disqualify only after the last-call cycle also gets silence. |
| **Inconclusive** | Voicenote, empty body, or genuinely ambiguous | Show Reyhan verbatim, let him rule. No move. |

- **C1.** A lead can be DQ on the community offer but **active on another track** (e.g. talent placement) — do NOT `Lost` them; note the pivot and keep them under the live track.
- **C2. Excluded/active deals** (leads already mid-close, meeting booked) are out of scope — never touch them.

### D. Execution
- **D1. Move via** `mcp__claude_ai_Attio__update-list-entry-by-record-id` (list, parent_object `people`, parent_record_id, `entry_values:{"stage": "..."}`). Resolve record_id by **email** with `search-records`.
- **D2. Valid stage titles** (exact — full 16-stage pipeline in order): `Prospect`, `Warm (Plan Meeting)`, `Lead (Meeting Done)`, `Proposal (In Progress)`, `Proposal Sent`, `On Hold/Need Time`, `Interested BUT Unresponsive`, `Interested BUT Need Time`, `Interested + Negotiation`, `Ready to Sign - Send Contract`, `WON`, `90 Day Back Burner`, `Went Cold`, `Lost`, `DQ`, `No $$$`. **Disqualify → `No $$$` (no budget) or `DQ` (not a fit)** — these two match Reyhan's two disqualify triggers exactly. `Lost` = generic/declined-after-proposal; `Went Cold` = faded, no explicit no.
- **D3. Reason-note on every moved record** (`create-note`): bucket + verbatim reply snippet + revisit flag. Title format `Reoffer <Mon Year> — <bucket>`.
- **D4. Ghost last-call:** draft **per channel** (email leads → Gmail-draft-style; LinkedIn-only leads → HeyReach-style), short breakup/last-call tone. Show Reyhan the **template + 2 sample drafts first**, get approval, then batch all. Post the batch to Slack for a final spot-check.

### E. Output & comms
- **E1. Deliver the summary in chat** (internal, bullets, exact names) — this is an approval artifact, not a client deliverable, so no HTML needed unless Reyhan asks for a board.
- **E2. Slack channel** for drafts/approval: confirm with Reyhan on first run (default candidates: `#recruitergtm-outboundsales` or `#ai-brain`). Store the chosen channel in this file once set.
- **E3. Log the run** — append a one-line entry to `projects/pipeline-cleanup/log.md` (date, #reoffered, #DQ, #back-burner, #warm, #ghost).

---

## How To Run

**Invoke:** `/pipeline-cleanup` in Claude · a Slack message to the assistant ("run pipeline cleanup") · or the monthly cron. Optional arg: the campaign project folder (defaults to the newest `projects/*reoffer*`).

**Steps:**
1. Locate the latest reoffer campaign (project folder + HeyReach campaign + email subject).
2. Harvest LinkedIn replies (B2, B5) and email replies (B3) for every recipient.
3. Classify all leads (C). Reconcile both channels per lead (email + LinkedIn) so nobody is double-counted or missed — a HeyReach "no reply" may have replied by email and vice-versa.
4. **Post the named summary** grouped by bucket, with verbatim reasons for every DQ, the warm "owes a reply" list, and the full ghost list. **Stop for approval.**
5. On approval: execute moves (D1–D3).
6. Compile the warm owed-list; draft ghost last-calls (D4); post to Slack (E2).
7. Log the run (E3).

---

## Monthly Cron (wire only after Reyhan approves the plan)

- **Schedule:** 1st of each month, ~08:00 Europe/London (`0 8 1 * *`). *(Master time = UK.)*
- **Behaviour:** cloud routine runs steps 1–4 (harvest + classify + summary), posts the summary to Slack, and **waits for Reyhan's approval reply before any move** — it must not auto-move (A1). Approval in Slack ("go" / edits) triggers steps 5–7.
- **Prereq:** a reoffer/reactivation campaign must have run in the trailing ~30 days; if none, the routine reports "no campaign to clean up" and exits.

---

## Reference — Aug 2026 baseline run

First run: 2026-08-13 on the **"$1,497 Window"** reoffer (HeyReach campaign `535346`, email subject `"$3,000 off until Friday"`, sent Aug 4). 63 leads reoffered (5 active excluded) → 23 replied, 40 silent. Result: 6 DQ→Lost, 4→Back Burner, 9 warm owed-replies, 40 ghosts queued for last-call, 4 inconclusive (2 voicenotes) held for Reyhan. Baseline data: `projects/community-reoffer-2026-08/`.
