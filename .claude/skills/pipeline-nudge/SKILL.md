# Skill: Pipeline Nudge

Weekly automated review of every high-intent deal in Attio Sales Pipeline 2026, generate personalized follow-up email drafts in Reyhan's voice, increment touch counters, and DM Reyhan as Cris with the prioritized list every Saturday 11am UK.

---

## Locked Rules

### A. Voice & template choice
Reyhan's follow-up voice is **casual British neutral**, short, conversational. Always uses "Lmk" not "Let me know", uses "mate" naturally, no em dashes, no "just following up", no "I hope this email finds you well". Reads like a text message from a friend, not a sales email.

### B. Three approved follow-up templates (use these exactly, swap only the variables)

#### Template 1 — Default Casual Check-In (use for ⭐3 and most cases)

> Subject: Re: {original subject}
>
> Hey {first_name}, it's been a while mate. I hope all is well with you.
>
> Did you get a chance to see the proposal and video I sent?
>
> Lmk if you don't want to set these systems anymore and I will stop following up.

**When to use:** Default. Works for almost every Proposal Sent or Negotiation lead. Soft, casual, gives them an easy exit.

#### Template 2 — Direct Decision Push (use for ⭐4-⭐5 stuck in Negotiation)

> Subject: Re: {original subject}
>
> Hey {first_name}, hope you're doing well mate.
>
> I want to make sure we close this out one way or another. Is the {system_name} build still on the table for you?
>
> If timing is off or it's not the right fit anymore, just lmk and I'll stop the follow-ups.

**When to use:** High-intent leads (⭐4-5) that have been sitting in Negotiation 4+ weeks. Forces a yes/no/not now answer so you can free up the slot.

#### Template 3 — Soft Urgency / Slot Available (use for high-value deals 4+ weeks stale)

> Subject: Re: {original subject}
>
> Hey {first_name}, hope all is well with you mate.
>
> Quick one, I have one slot opening up for {month} and wanted to check if you're still planning to move on the {system_name} we mapped out.
>
> If not, no worries, I'll reroute it and stop chasing.

**When to use:** Big-ticket deals ($5k+) that have gone cold. Creates real urgency (slot availability) without being pushy.

### C. Variables to fill in
- `{first_name}` — from Attio person record
- `{system_name}` — pull from `deal_type` in Attio (e.g. "OutboundOS retainer", "SourcingOS build", "Community + Claude setup"). Use plain language, not internal product names.
- `{month}` — the next 1-2 months from today

### D. Subject line rule
Always reply in the existing Gmail thread when possible. Subject = `Re: {original proposal subject}`. Never create a new thread for a follow-up.

### E. Sign-off
Single line: `Reyhan`. No "Best", no "Cheers", no "Regards" — these aren't his voice.

### F. What never goes in a follow-up
- No "just following up" / "circling back" / "touching base"
- No "I hope this email finds you well"
- No em dashes (zero, hard limit)
- No bullet lists or numbered steps in the message body
- No CTAs like "let me know your thoughts!" — Lmk is the only acceptable form
- No talent placement references (per `feedback_no_talent_placement_online.md`)
- No mention of pricing or scope changes — those go in a separate email

### G. 5-day silence rule (HARD)
**Never nudge a lead if Reyhan has engaged with them in the last 5 days.** Engagement = email sent/received OR meeting on calendar.

Check via Attio fields on the person record:
- `last_email_interaction.interacted_at` — most recent email
- `last_calendar_interaction.interacted_at` — most recent meeting
- `last_interaction.interacted_at` — rolled-up max

If `max(last_email, last_calendar) >= today - 5 days` → **SKIP this lead**, log as `⏭️ Skipped — recent contact: {date}`.

### H. Template selection logic (deterministic)

| Lead state | Template |
|---|---|
| ⭐5 OR Ready to Sign | Template 2 (Direct Decision Push) |
| ⭐4 + Negotiation 4+ weeks | Template 2 (Direct Decision Push) |
| ⭐4 + Proposal Sent | Template 1 (Default) |
| ⭐3 + deal value ≥ $5k + stage 4+ weeks | Template 3 (Soft Urgency) |
| Everything else | Template 1 (Default) |

### I. Auto-kill recommendation (flag, don't auto-execute)
If a lead has:
- ⭐2 confidence AND
- 60+ days in stage AND
- No calendar interaction ever

→ Flag in the Slack DM as `☠️ Recommend → 90 Day Back Burner` but do NOT move the stage automatically. Reyhan decides manually.

### J. Touches Sent counter
After generating a Gmail draft for a lead, increment the `touches_sent` field on that lead's list entry by 1. Use `manage-list-entry` mode 3 with `{"touches_sent": current_value + 1}`. Skip increment if no draft was created (e.g. skipped via 5-day rule).

### K. Cris DM destination (NOT #ai-brain)
Saturday cron output goes to **Cris ↔ Reyhan DM channel `D0AL0N9AL9L`** using the `SLACK_BOT_TOKEN` from `.env`. See `reference_cris_slack_bot.md` for full Cris config.

The old `#ai-brain` (`C0AMLGAMLH3`) is retired for pipeline-nudge. All future DMs go through Cris.

---

## How to Invoke

```
/pipeline-nudge
```

No arguments needed. Run manually any time, or it fires automatically every Saturday 11am UK via the scheduled cron.

---

## Stages Included (Pipeline Coverage)

Pull leads from ALL of these stages, not just Proposal Sent:

1. `Proposal Sent`
2. `Interested + Negotiation`
3. `Interested BUT Need Time`
4. `Interested BUT Unresponsive`
5. `Ready to Sign - Send Contract`
6. `On Hold/Need Time`

Use the `advanced-filter-list-entries` mode with `matchAny: true` (OR logic across stages) OR pull each stage separately and combine.

---

## Step-by-Step Execution

### Step 1 — Pull all high-intent leads from Attio

For each of the 6 stages above, call `filter-list-entries`:
- `listId`: `59c6844e-264d-490b-b78d-245a1cd7b5f4`
- `attributeSlug`: `stage`
- `condition`: `equals`
- `value`: (one of the 6 stage names above)
- `limit`: 50

Combine all results. Capture per entry:
- `entry_id`, `parent_record_id`
- `stage.title`, `stage.active_from` (days in current stage)
- `deal_type.title` (the system being sold)
- `deal_value.currency_value` (USD amount)
- `confidence_score.value` (1-5 stars)
- `touches_sent.value` (current counter, default 0 if empty)

### Step 2 — Get person details + interaction dates

For each `parent_record_id`, call `get_record_details` on `people` with fields:
`["name", "email_addresses", "linkedin", "last_email_interaction", "last_calendar_interaction", "last_interaction"]`

### Step 3 — Apply 5-day silence rule

For each lead, compute:
```
last_contact = max(
  last_email_interaction.interacted_at,
  last_calendar_interaction.interacted_at
)
```

If `last_contact >= today - 5 days` → mark `SKIP`, do not draft. Log the skip reason in the Slack DM.

### Step 4 — Pull call notes for non-skipped leads

For each remaining lead, call `list_notes` on `people` (limit 5).
For the most recent note, call `get_record_details` on `notes` to get `content_markdown`.
Use note content for personalisation context (niche, role types, what they care about).

### Step 5 — Select template per lead (per rule H)

Apply the template selection logic table from Rule H. Output: each lead has a chosen template number (1, 2, or 3).

### Step 6 — Draft personalised follow-up

Fill in the chosen template variables:
- `{first_name}` from `name.first_name`
- `{system_name}` from `deal_type.title` (translate internal names: "RecruiterGTM Standard Community Package" → "Community + Claude setup", "OutboundOS Retainer" → "OutboundOS engine", "SourcingOS Retainer" → "SourcingOS build", "GTM Academy - GTM Ops Integrator" → "Ops Integrator placement", etc.)
- `{month}` = name of next month after today, or month after next if today is past mid-month

### Step 7 — Find Gmail thread for each lead

For each lead, call Gmail search: `from:{their_email} OR to:{their_email}` filtered to last 90 days.
- Capture the most recent `threadId` matching the proposal subject.
- If no thread found, fall back to a new email (subject: their `deal_type` proposal).

### Step 8 — Create Gmail drafts (NOT sent)

For each lead, call `gmail_create_draft` with:
- `to`: their email address
- `subject`: `Re: {original_proposal_subject}` (or new if no thread)
- `body`: the filled template + signature
- `threadId`: the Gmail thread ID (if found)

Per `feedback_never_send_emails.md` — ONLY create drafts, never send. Reyhan reviews + sends manually.

### Step 9 — Increment touches_sent counter (per rule J)

For each lead that got a draft created, call `manage-list-entry` mode 3:
```json
{
  "listId": "59c6844e-264d-490b-b78d-245a1cd7b5f4",
  "entryId": "<lead's entry_id>",
  "attributes": {"touches_sent": <current_touches_sent + 1>}
}
```

### Step 10 — Optional LinkedIn nudge via Lemlist (⭐4-5 only)

For leads with ⭐4 or ⭐5 confidence AND a valid `linkedin` URL on their person record:
- Build a Lemlist campaign named `Pipeline Nudge LinkedIn — Week of {date}`
- Each lead = one step in the campaign
- Use Template 1 or 2 (whichever applies) adapted for LinkedIn DM (drop the subject line, keep the body)
- Push the campaign via Lemlist API (key in `.env` as `LEMLIST_API_KEY`, see `reference_lemlist_api.md`)
- Set campaign to **draft state** — Reyhan activates in Lemlist UI after reviewing copy

Skip this step entirely for ⭐3 and below.

### Step 11 — Post to Cris DM (the deliverable)

POST to Slack chat.postMessage with `SLACK_BOT_TOKEN`:
- `channel`: `D0AL0N9AL9L`
- `text`: header + ranked list (Template-2 leads first, then Template-3, then Template-1)

Format (markdown, plain text — avoid Block Kit complexity):

```
🎯 *Pipeline Nudge — Week of {Saturday date}*

{N} drafts created · {S} skipped (recent contact) · {K} auto-kill candidates flagged

Combined deal value at stake: ${total}

——— TOP PRIORITY (Template 2 — Decision Push) ———

*1. {Name}* · {Company} · `{Stage}` · ${value} · ⭐{score} · {days_stale}d
   Email draft created in thread. {Touch #N}

*2. {Name}* ...

——— HIGH VALUE (Template 3 — Soft Urgency) ———

...

——— STANDARD (Template 1 — Casual Check-In) ———

...

——— SKIPPED (5-day silence rule) ———

• {Name} — last contact {date}, ({channel})

——— AUTO-KILL CANDIDATES (Reyhan decides) ———

☠️ {Name} · ${value} · ⭐2 · {days} days stale, no call ever

Reply: SEND ALL / SEND 1 3 5 / KILL {name}
LinkedIn campaign: {campaign name} in Lemlist (draft state)
```

### Step 12 — Wait for Reyhan's reply (manual mode only)

For the Saturday cron, just deliver the DM and exit.

For manual `/pipeline-nudge` invocations, wait for Reyhan to reply:
- `SEND ALL` → drafts stay as drafts (this is already done in step 8). Skill confirms.
- `KILL {names}` → move those entries to `90 Day Back Burner` stage via `manage-list-entry` mode 3 with `{"stage": "90 Day Back Burner"}`
- `SCORE` → review and update confidence_scores based on latest signals

---

## Schedule

Saturday 11:00 AM UK (`Europe/London`).

Cron expression: `0 11 * * 6`

Cron is scheduled via the `schedule` skill. To set or change:
```
/schedule create "pipeline-nudge weekly" --cron "0 11 * * 6" --tz "Europe/London" --command "/pipeline-nudge"
```

---

## Key References

| What | Value |
|------|-------|
| Pipeline list ID | `59c6844e-264d-490b-b78d-245a1cd7b5f4` |
| Stage attribute ID | `c87ba3bd-ba69-49d5-adc7-64461d29137b` |
| Stages included | 6 listed under "Stages Included" above |
| Cris DM channel | `D0AL0N9AL9L` |
| Slack bot token env var | `SLACK_BOT_TOKEN` |
| Lemlist API key env var | `LEMLIST_API_KEY` |
| Memory: Cris bot details | `reference_cris_slack_bot.md` |
| Memory: Lemlist API details | `reference_lemlist_api.md` |
| Memory: Attio pipeline stages | `reference_attio_pipeline_stages.md` |

---

## Edge Cases

- **No call notes:** Still apply template based on confidence score. The 3 templates work without personalisation.
- **No LinkedIn URL on a ⭐4-5 lead:** Skip the Lemlist step for that lead. Note in the DM as "LinkedIn channel skipped — no URL".
- **Gmail thread not found:** Create a new email with the deal_type as part of the subject (`Re: {deal_type} proposal`).
- **Lead is a Won deal that hasn't been moved:** Detect via `date_closed` field being set. Skip and flag to Reyhan as "pipeline hygiene needed — already closed".
- **Email field missing:** Skip the lead, log "no email on record" in the DM. Cannot draft. (See Luke Buckmaster.)
- **Confidence score is empty:** Treat as ⭐3 default.
