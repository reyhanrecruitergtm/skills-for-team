# Command: handle-replies

Classify inbound replies from outreach campaigns and draft the right response. Keeps pipeline moving without Reyhan or Shmookh having to think about every reply from scratch.

---

## When to Use

- Shmookh receives replies for a retainer client and needs to action them
- Reyhan gets replies on his own LinkedIn or email outreach
- GTM Engineer needs to handle a reply batch for a client

---

## Inputs Required

Paste the reply and confirm:
1. **Channel** — LinkedIn DM or email
2. **Which sequence they're in** — what offer/playbook triggered the outreach
3. **Client context** — who is responding on behalf of (Reyhan / client name)

---

## Reply Classification System

Every reply falls into one of 6 categories. Classify first, then act.

---

### Category 1: 🟢 INTERESTED
**Signals:** "Yes, tell me more" / "I'd be open to a chat" / "Can you send more info?" / "When are you free?"

**Action:**
- Reply within 2 hours (same business day at minimum)
- Do NOT send a Calendly link immediately — confirm their interest first with one question
- Move to Attio as a live opportunity
- Tag in Notion as "Meeting to book"

**Draft response template:**
```
Great to hear from you, [Name].

Happy to share more — [one line on what you'll cover in the call].

Are you free [day] or [day] this week for 20 minutes?
```

---

### Category 2: 🟡 NOT NOW
**Signals:** "Not the right time" / "Come back in Q3" / "We're mid-project right now" / "Revisit in a few months"

**Action:**
- Acknowledge with no pressure
- Set a Notion reminder for the date they mentioned (or 60 days if vague)
- Keep in sequence for a future nurture campaign

**Draft response template:**
```
Totally understand — timing matters.

I'll drop you a note in [timeframe they mentioned]. In the meantime, feel free to reach out if anything changes.
```

---

### Category 3: 🔴 NOT INTERESTED
**Signals:** "Not for us" / "We're all sorted" / "Please remove me" / "We use [competitor]"

**Action:**
- Remove from all sequences immediately
- Add to suppression list in Lemlist/HeyReach
- If they mentioned a competitor — log it in the campaign learnings
- Never reply with pushback or objection handling on first "no"

**Draft response template:**
```
No problem at all — I appreciate you letting me know.

Best of luck with [what they're doing].
```

---

### Category 4: 🔵 REFERRAL / REDIRECT
**Signals:** "You should speak to [Name]" / "Not my department — try [team]" / "Our [Title] handles this"

**Action:**
- Thank the person who replied
- Immediately research the referred contact
- Add referred contact to sequence with a warm intro angle
- Update Clay table with the correct decision maker

**Draft response template (to original):**
```
Really appreciate you pointing me in the right direction — that's helpful.

I'll reach out to [Name] directly. Thanks again, [Name].
```

**Outreach to referred contact:**
```
[Name] suggested I reach out — they thought what we're doing might be relevant to you.

[One line on the offer]. Would it make sense to connect?
```

---

### Category 5: 🟠 OBJECTION
**Signals:** "We already have someone for this" / "Too expensive" / "We tried this before and it didn't work" / "Why would I use you over [X]?"

**Action:**
- Do NOT defend or pitch immediately
- Acknowledge the objection first
- Ask one clarifying question before responding with proof
- Log objection type in campaign learnings for future copy refinement

**Common objections + responses:**

| Objection | Response angle |
|-----------|---------------|
| "We already have a recruiter" | "Good — we work alongside existing recruiters, not instead of them. What's the current setup?" |
| "Too expensive" | "Fair question. What would make it worth it for you?" |
| "Tried outbound before, didn't work" | "What did that look like? Most outbound fails on ICP or copy, not the channel itself." |
| "Why you over an agency?" | "Good question — happy to walk you through what's different. 15 minutes?" |

---

### Category 6: ⚪ UNCLEAR / NO SIGNAL
**Signals:** One-word reply / emoji / out-of-office / auto-reply

**Action:**
- If OOO: Note return date in Notion, follow up when they're back
- If emoji/one-word: Treat as mild interest, send a short follow-up
- If auto-reply: No action needed

---

## Output Format

```
REPLY CLASSIFICATION
====================
From: [Name] | [Company]
Channel: [LinkedIn / Email]
Category: [🟢 INTERESTED / 🟡 NOT NOW / 🔴 NOT INTERESTED / 🔵 REFERRAL / 🟠 OBJECTION / ⚪ UNCLEAR]

RECOMMENDED ACTION:
[Specific next step]

DRAFT RESPONSE:
[Ready-to-send reply]

CRM ACTION:
[What to update in Attio / Notion]
```

---

## SLA Targets

| Category | Response time |
|----------|--------------|
| 🟢 Interested | Within 2 hours (same business day) |
| 🟡 Not now | Within 24 hours |
| 🔴 Not interested | Within 24 hours (suppression same day) |
| 🔵 Referral | Original reply within 24 hours, new outreach within 48 hours |
| 🟠 Objection | Within 4 hours |
| ⚪ Unclear | 48 hours or skip |
