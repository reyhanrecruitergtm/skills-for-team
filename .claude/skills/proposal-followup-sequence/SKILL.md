# Skill: Proposal Follow-Up Sequence

A daily (Mon–Sat) agent that runs a fixed 3-step follow-up sequence on every Attio **"Proposal Sent"** lead who hasn't replied. It creates threaded Gmail **drafts** (never auto-sends) and DMs Reyhan the list to approve via Cris.

Distinct from `pipeline-nudge` (which is a weekly, single, generic nudge across all high-intent stages). This skill is a precise time-triggered sequence with locked copy, for Proposal Sent only.

---

## Locked Rules

### A. Send mode (HARD)
- A1. **Drafts only, never auto-send.** Per `feedback_never_send_emails.md`. The agent creates Gmail drafts in-thread and posts the list to Cris for Reyhan to send. Reyhan approves with `SEND` / `SEND 1 3` etc.
- A2. Every follow-up is a **reply inside the existing proposal thread** (subject `Re: {original proposal subject}`). Never a new thread — FU1 literally says "the proposal and video I sent above".

### B. The 3 locked emails (use verbatim, only swap {FirstName} / {CompanyName})

**Follow-up 1 — fires 2 days after the proposal email was sent**
```
Hey {FirstName}, hope all is well with you.

Did you see the proposal and video I sent above?

Lmk if you have any questions.

Best,
Reyhan
```

**Follow-up 2 — fires 2 days after FU1 was sent (~day 4)**
```
Hey {FirstName}, Is everything ok?

I never heard back from you.
```

**Follow-up 3 (final) — fires 10 days after FU2 was sent (~day 14)**
```
Hey {FirstName}, I understand you're busy.

Should I stop following up? I'm not sure if my emails are landing in spam lol

Lmk if you're not interested in improving systems for {CompanyName} atm.
```

- B1. Copy is locked exactly as Reyhan wrote it (FU1 has "Best, Reyhan"; FU2/FU3 have no sign-off — keep as-is).
- B2. Zero em dashes. No subject-line changes. No extra lines.

### C. Timing (relative to the previous email's actual send date)
Each step triggers off when the *previous* message actually went out (read from the Gmail thread), so approval delays don't break the cadence:

| Step | Trigger |
|---|---|
| FU1 | ≥ 2 days since the **proposal email** was sent, and no FU1 sent yet |
| FU2 | ≥ 2 days since **FU1** was sent, and no FU2 sent yet |
| FU3 | ≥ 10 days since **FU2** was sent, and no FU3 sent yet |

After FU3 is sent with no reply → sequence complete. Flag in the Cris DM for a manual stage decision (e.g. → `Interested BUT Unresponsive` or `90 Day Back Burner`). **Do not auto-move stages.**

### D. Stop conditions (check every run, before drafting)
- D1. **Prospect replied** anywhere in the thread after the proposal → STOP the sequence. Flag in the Cris DM: "✅ {Name} replied — move them out of Proposal Sent." Do not draft.
- D2. **Reyhan already engaged in the last 2 days** (sent/received email or a meeting on calendar) → SKIP for today, don't draft over fresh contact.
- D3. **A previous follow-up draft is still unsent** in the thread → do NOT create the next draft or a duplicate. Remind Reyhan: "⏳ FU{n} for {Name} still pending your send."
- D4. **Lead already past FU3** → skip, flag as sequence-complete.
- D5. **Hard cap — 4 emails total (HARD STOP).** Count every email Reyhan has sent in the thread with no reply, **including the original proposal**. The moment that count reaches **4** (proposal + 3 follow-ups, or proposal + fewer follow-ups plus any manual sends Reyhan made), STOP the sequence permanently for that lead — never draft another follow-up. Flag in the Cris DM as sequence-complete. This means a manually-sent email mid-sequence reduces the number of auto follow-ups, never increases the total past 4.
- D6. **Backlog age gate (HARD).** Only auto-start the sequence for proposals sent within the **last 16 days** (covers the full Day 2 → Day 14 window + buffer). If a lead's proposal is older than 16 days **and no follow-up has been sent yet**, it's pre-existing backlog — do NOT auto-fire follow-ups. Flag it in the Cris DM under a `BACKLOG (your call)` section for Reyhan to re-engage or clean up manually. Leads already mid-sequence continue normally regardless of age. (Anchor on the Gmail proposal date; fall back to the stage `active_from` if no thread is found.)

### E. State = the Gmail thread (no manual data entry)
- The **Attio "Proposal Sent" stage** defines WHO is in the sequence.
- The **Gmail thread** is the clock + memory:
  - Day 0 = the proposal email Reyhan sent (earliest sent message matching the proposal).
  - Which follow-ups already went out = detect by the locked opening lines ("Did you see the proposal and video I sent above?", "Is everything ok?", "Should I stop following up?").
  - Whether they replied = any inbound message from the prospect after the proposal.
- Use only **sent** messages to advance steps; a **draft** present-but-unsent triggers rule D3, not advancement.

### F. Merge fields
- `{FirstName}` → person `name.first_name` in Attio.
- `{CompanyName}` → the company linked to the person/deal in Attio (plain trading name).

### G. Cris DM destination
Daily output goes to the **Cris ↔ Reyhan DM channel `D0AL0N9AL9L`** using `SLACK_BOT_TOKEN` from `.env`. See `reference_cris_slack_bot.md`.

---

## Step-by-Step Execution (per daily run)

### Step 1 — Pull Proposal Sent leads
`filter-list-entries` on the Sales Pipeline 2026 list:
- `listId`: `59c6844e-264d-490b-b78d-245a1cd7b5f4`
- `attributeSlug`: `stage`, `condition`: `equals`, `value`: `Proposal Sent`
- `limit`: 50

Capture `entry_id`, `parent_record_id`, `deal_type`, company.

### Step 2 — Person + interaction dates
`get_record_details` on `people` for each `parent_record_id`:
`["name", "email_addresses", "last_email_interaction", "last_calendar_interaction"]`
Skip + log if no email on record.

### Step 3 — Find + read the Gmail thread
Gmail search `from:{email} OR to:{email}` (last 120 days). Take the proposal thread. Read it to extract:
- proposal sent date (day 0)
- FU1 / FU2 / FU3 sent? (match locked opening lines) + their send dates
- any inbound reply from the prospect after the proposal
- any unsent follow-up draft already in the thread

### Step 4 — Apply stop conditions (Rule D)
Reply → STOP+flag. Recent engagement (≤2d) → SKIP. Pending unsent draft → remind, don't advance. Past FU3 → flag complete.

### Step 5 — Decide the due step (Rule C)
Compute days since the last *sent* message and pick FU1 / FU2 / FU3 / none.

### Step 6 — Create the threaded Gmail draft
`gmail_create_draft` with:
- `to`: prospect email
- `subject`: `Re: {original proposal subject}`
- `body`: the locked FU copy with `{FirstName}` / `{CompanyName}` filled
- `threadId`: the proposal thread ID
Per Rule A1 — draft only, never send.

### Step 7 — Notify Reyhan in Slack (the deliverable)
This Slack DM is the notification that drafts are ready — it's the cue for Reyhan to go send the emails (and paste the LinkedIn DMs). `chat.postMessage` to `D0AL0N9AL9L`:
```
✉️ *Proposal Follow-Ups — {date}*
👉 {N} email drafts are ready in Gmail — go send them.

{N} drafts ready · {R} replied (move them) · {P} pending from before · {D} done

——— GO SEND THESE ———
*1. {Name}* · {Company} · FU{n} (day {x})
   📧 Gmail draft is in the thread — open + send.
   💬 LinkedIn (send manually) → {linkedin_url}
      "{LinkedIn FU{n} copy, vars filled}"
*2. {Name}* ...

——— THEY REPLIED (move out of Proposal Sent) ———
✅ {Name} · {Company}

——— STILL PENDING FROM A PREVIOUS DAY ———
⏳ {Name} · FU{n} draft created {date}, not sent yet

——— SEQUENCE COMPLETE (4 emails, no reply) ———
☠️ {Name} · decide: Unresponsive / Back Burner

Once sent, just reply: DONE  (or SKIP {name})
```
If a lead has no `linkedin` URL, omit the 💬 line for them.

### Step 8 — On Reyhan's reply (manual mode)
`SEND ALL` / `SEND 1 3` → the drafts are already in Gmail; Reyhan sends from there (or, if approved, the skill may send only the explicitly-approved ones). `SKIP {name}` → leave as-is. For the daily cron, just deliver the DM and exit.

---

## LinkedIn Channel (manual)

Reyhan sends LinkedIn messages himself for now. The agent does **not** push to any tool — it just **writes the matching LinkedIn DM and drops it into the Slack notification**, ready to copy-paste. The lead is already a 1st-degree connection (proposal sent), so it's a direct message.

- L1. Include a LinkedIn line only when the lead has a `linkedin` URL on the Attio person record. Put the URL in the Slack DM so Reyhan clicks straight through. No URL → skip the LinkedIn line.
- L2. The LinkedIn message mirrors the email step that's due (FU1 / FU2 / FU3). Locked copy below — only swap `{FirstName}` / `{CompanyName}`. No subject line, no sign-off (it's a DM).

**LinkedIn copy (locked):**
- **FU1:** `Hey {FirstName}, hope all is well. Did you get a chance to see the proposal and video I sent over? Lmk if you have any questions.`
- **FU2:** `Hey {FirstName}, is everything ok? Haven't heard back from you on the proposal.`
- **FU3:** `Hey {FirstName}, I know you're busy. Should I stop following up? Not sure if my emails are landing in spam lol. Lmk if you're not interested in improving systems for {CompanyName} atm.`

---

## Schedule
**LIVE** as a cloud routine: `trig_01SM8RUnvCEJuFsD9WbEcSVi` — cron `3 8 * * 1-6` UTC (~9am UK Mon–Sat). Manage at https://claude.ai/code/routines/trig_01SM8RUnvCEJuFsD9WbEcSVi
Cloud constraint: Attio has no claude.ai connector, so the routine reads Attio via its **REST API** (Bearer token embedded in the routine prompt — rotating/revoking the token in Attio breaks the routine, update it then). Gmail + Slack run via claude.ai connectors. Notification is a Slack **DM to Reyhan** (not the Cris bot token, which isn't available in the cloud env).

Daily, Monday–Saturday (skip Sunday), 9:00 AM UK.
Cron: `0 9 * * 1-6`, tz `Europe/London`.
```
/schedule create "proposal-followup-sequence" --cron "0 9 * * 1-6" --tz "Europe/London" --command "/proposal-followup-sequence"
```

---

## Key References
| What | Value |
|------|-------|
| Pipeline list ID | `59c6844e-264d-490b-b78d-245a1cd7b5f4` |
| Stage filter | `Proposal Sent` (status id `686958d9-41ca-43f3-bebb-f8d87e80c1b7`) |
| Cris DM channel | `D0AL0N9AL9L` |
| Slack token env | `SLACK_BOT_TOKEN` |
| Cris bot details | `reference_cris_slack_bot.md` |
| Never-send rule | `feedback_never_send_emails.md` |
| Sibling skill | `pipeline-nudge` (weekly generic nudge) |

---

## Edge Cases
- **No Gmail thread found:** can't anchor the sequence — flag "no proposal thread found for {Name}", don't draft.
- **No email on record:** skip + log.
- **Prospect replied but stage still Proposal Sent:** flag for manual move (don't auto-move).
- **Multiple proposal threads:** use the most recent one matching the proposal subject / deal_type.
- **Reyhan sent a manual reply mid-sequence:** counts as engagement (D2) and resets the clock off that send date.
</content>
