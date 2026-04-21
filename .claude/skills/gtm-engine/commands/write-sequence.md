# Command: write-sequence

Write a complete outbound sequence for HeyReach (LinkedIn) or Lemlist (email), adapted to RecruiterGTM's niche, tone, and anti-AI-slop standards.

---

## When to Use

- Building a new sequence for a client's OutboundOS engine
- Writing copy for a new playbook (hiring signal, leadership change, etc.)
- Refreshing a sequence that has gone stale or dropped in reply rate

---

## Inputs Required

Ask Reyhan for these before writing anything:

1. **Channel** — LinkedIn (HeyReach), Email (Lemlist), or both
2. **ICP** — Who are we targeting? Title, company type, size, location
3. **Offer** — What are we offering in the sequence? (audit, call, demo, lead magnet)
4. **Pain trigger** — What signal made this prospect enter the sequence? (hiring spike, new leader, etc.)
5. **Tone** — Client's tone of voice (or default to RecruiterGTM TOV if writing for Reyhan)
6. **Personalisation variable** — What 1-2 Clay-enriched variables are available? (e.g. job title, company name, recent hire)
7. **Lead magnet** — Is there a give-first asset to offer? (mini audit, benchmark, insight)

---

## Copy Framework

Every sequence follows this structure per touch:

**Observation → Problem → Proof → Ask**

- **Observation:** One specific, relevant thing about their situation (pulled from the intent signal or Clay variable)
- **Problem:** Name the pain they're likely feeling — don't pitch yet
- **Proof:** One line of credibility (result, client, relevant win)
- **Ask:** Soft, frictionless — not "book a 30 min call", but "worth a quick chat?"

---

## Sequence Structure

### LinkedIn Sequence (HeyReach) — 4 touches

**Touch 1 — Connection Request**
- 0 words (blank note) OR 1 line personalised note
- Rule: If using a note, reference the intent signal only. No pitch.
- Example: "Noticed [Company] is scaling the [function] team — would love to connect."

**Touch 2 — Opening Message (sent after connection accepted)**
- 3-4 lines max
- Lead with the observation (personalised variable)
- Name the problem
- Soft ask or give-first (offer the lead magnet)
- No links

**Touch 3 — Follow-up (day 4-5)**
- 2-3 lines
- Reframe the value, different angle
- Reference proof point
- Repeat soft ask

**Touch 4 — Break-up (day 8-10)**
- 1-2 lines
- Light humour or honest close
- Leave door open — no burning bridges

---

### Email Sequence (Lemlist) — 3 touches + 1 follow-up

**Email 1 — Opener**
- Subject: 3-5 words, no clickbait, no question marks
- Body: 4-6 lines
- Icebreaker (personalised variable from Clay)
- Who you are in one sentence
- Problem + proof
- Soft CTA — easy to reply to
- No links, no calendly, no tracking URLs

**Email 2 — Follow-up (day 3)**
- Subject: Re: [original subject]
- Body: 2-3 lines
- Restate the offer differently
- One proof point
- Repeat the ask

**Email 3 — Value add (day 7)**
- Subject: New line, not a reply thread
- Lead with something genuinely useful (stat, insight, relevant news)
- Tie it to the offer
- Soft ask

**Email 4 — Break-up (day 12)**
- Subject: "Still worth it?"
- 2 lines max
- Honest close, no guilt, leave door open

---

## Tone Rules (RecruiterGTM Default)

- British English — "recognise", "colour", "whilst"
- No corporate opener ("I hope this finds you well" → delete)
- No filler ("I wanted to reach out" → just reach out)
- No em dashes in copy
- Personalisation feels researched, not merged — "I saw your team just hired a Head of EB" not "Hi {{firstName}}"
- One sentence per line in LinkedIn messages
- Max 2 personalisation variables per sequence ({{companyName}} + one signal-based variable)

---

## Output Format

Output the full sequence ready to paste into HeyReach or Lemlist:

```
CHANNEL: [LinkedIn / Email / Both]
ICP: [Who this is for]
TRIGGER: [What signal puts someone in this sequence]

--- TOUCH 1 ---
[Content]

--- TOUCH 2 ---
[Content]

--- TOUCH 3 ---
[Content]

--- TOUCH 4 ---
[Content]
```

Then run validate-copy on the output before marking it ready to launch.

---

## Swipe File (Proven Patterns)

**Openers that work for recruitment niche:**
- "Saw [Company] just posted 3 [role] roles this month — that's a busy hiring season."
- "Noticed [Name] joined as [Title] recently — new leaders usually inherit some interesting hiring challenges."
- "Your [Company] team grew from [X] to [Y] people this year — that kind of pace usually tests the recruitment setup."

**CTAs that work:**
- "Worth a 15-min call this week?"
- "Happy to send over [lead magnet] — just say the word."
- "Open to sharing what we've seen work for similar setups?"

**What kills reply rates:**
- Asking for 30+ minutes on first touch
- Mentioning price in the sequence
- Attaching anything (triggers spam)
- Using "synergy", "partnership", "reach out" in opener
