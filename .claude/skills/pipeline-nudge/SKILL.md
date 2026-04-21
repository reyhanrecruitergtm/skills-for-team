# Skill: Pipeline Nudge

Review all "Proposal Sent" leads in Attio, generate personalized follow-up emails, and post to Slack for approval.

---

## How to Invoke

```
/pipeline-nudge
```

No arguments needed. Run it manually any time, or it runs automatically on the weekly cron schedule.

---

## What This Skill Does

1. Pulls all leads currently in "Proposal Sent" stage from the Sales Pipeline 2026 list in Attio
2. Fetches each person's name, email, deal type, deal value, and call notes
3. Writes a short personalized follow-up email for each lead
4. Posts all drafts to Slack `#ai-brain` for Reyhan's approval
5. Waits — does NOT send anything until explicitly told to

---

## Step-by-Step Instructions

### Step 1 — Pull Proposal Sent leads from Attio

Use `filter-list-entries` with these exact parameters:
- `listId`: `59c6844e-264d-490b-b78d-245a1cd7b5f4` (Sales Pipeline 2026)
- `attributeSlug`: `stage`
- `condition`: `equals`
- `value`: `Proposal Sent`
- `limit`: 50

Collect all `parent_record_id` values and the `stage.active_from` date (this is when the proposal was sent).

### Step 2 — Get name, email, deal info for each lead

For each `parent_record_id`, call `get_record_details` on `people` with fields: `["name", "email_addresses"]`.

Also capture from the list entry:
- `deal_type` (title)
- `deal_value` (currency_value)
- `stage.active_from` (date proposal was sent)

### Step 3 — Get call notes for each lead

For each `parent_record_id`, call `list_notes` on `people`.

If notes exist, call `get_record_details` on `notes` for each note ID to get the full `content_markdown`.

If no notes, mark as "No call notes — write a generic follow-up."

### Step 4 — Write personalized follow-up emails

For each lead, write a short follow-up email using the rules below.

**Email rules:**
- 3–5 lines maximum. Never longer.
- Subject line: `Re: RecruiterGTM Proposal` (always the same — implies reply to existing thread)
- No "just following up" or "hope you're well" openers
- Reference one specific thing from their call notes (pain point, goal, or something they said)
- End with a single direct question or a soft urgency (e.g., one April slot left)
- Sign off: `Reyhan`
- Write in Reyhan's voice — short sentences, practitioner tone, no corporate language
- Do NOT mention tool names (Clay, Lemlist, etc.) in the email body

**Example tone:**
> Hey [Name],
>
> Quick check-in on the proposal from [X] weeks ago.
>
> [One sentence referencing their specific situation from notes.]
>
> Still the right time to move on this? Happy to answer any questions before you decide.
>
> Reyhan

### Step 5 — Post to Slack

Post a single message to **`#ai-brain`** (channel ID: `C0AMLGAMLH3`).

Format the message like this:

```
📋 *Pipeline Nudge — [DATE]*

[N] leads in Proposal Sent. Draft follow-ups below.

Reply with *SEND ALL* to send every email, or *SEND [Name]* for specific ones. Reply *SKIP [Name]* to hold off on someone.

---

*1. [Full Name]* | [email] | [Deal Type] | $[Value] | Sent [X] days ago

> [Subject line]
>
> [Full email draft]

---

*2. [Full Name]* | [email] | [Deal Type] | $[Value] | Sent [X] days ago

> [Subject line]
>
> [Full email draft]

---
```

Calculate "Sent X days ago" from `stage.active_from` to today.

### Step 6 — Wait for approval

After posting to Slack, stop. Do NOT send any emails.

If running manually, tell Reyhan: "Posted to #ai-brain. Reply SEND ALL or SEND [Name] to trigger sends."

If Reyhan replies `SEND ALL` or `SEND [Name]` in this conversation, proceed to send via `gmail_create_draft` (or send directly if Gmail MCP is available).

---

## Sending Emails (When Approved)

When Reyhan approves — either by replying in this conversation or in Slack:

1. For each approved lead, use `gmail_create_draft` with:
   - `to`: their email address
   - `subject`: `Re: RecruiterGTM Proposal`
   - `body`: the approved email draft
   - If a `threadId` is available from searching Gmail, pass it to reply in-thread

2. Confirm back to Reyhan: "Draft created for [Name] — [email]."

Note: If Gmail MCP is unavailable, output all final emails as clean copy for manual sending.

---

## Key Attio References

| What | Value |
|------|-------|
| Pipeline list | Sales Pipeline 2026 |
| List ID | `59c6844e-264d-490b-b78d-245a1cd7b5f4` |
| Stage to filter | `Proposal Sent` |
| Slack channel | `#ai-brain` (ID: `C0AMLGAMLH3`) |

---

## Edge Cases

- **No notes on a lead:** Write a shorter generic follow-up. Note in Slack that no call context was available.
- **Lead sent proposal 3+ weeks ago with no reply:** Add a soft urgency line ("I have one slot open in April if timing works").
- **More than 10 leads:** Flag to Reyhan — something may be wrong with pipeline hygiene. Still process all of them.
- **Duplicate leads (same person, two entries):** Flag it, process only the most recent one.
