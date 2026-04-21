# Command: validate-copy

10-point quality check on any outreach copy before it goes live. Run this on every sequence produced by write-sequence or submitted by a client for review.

---

## When to Use

- Before launching any new Lemlist or HeyReach sequence
- When a client submits copy they wrote themselves
- After refreshing an underperforming sequence
- Any time Reyhan or Shmookh wants a second opinion on copy

---

## How to Run

Paste the copy into the conversation and say `/gtm-engine validate-copy`. Score each criterion, flag failures, and output the revised copy if needed.

---

## The 10-Point Checklist

Score each point: ✅ Pass / ⚠️ Warning / ❌ Fail

### 1. Opener — No Filler
❌ Fail if opener contains any of:
- "I hope this finds you well"
- "I wanted to reach out"
- "My name is X and I work at Y"
- "I came across your profile"
- Any greeting longer than 1 line before getting to the point

✅ Pass: Opens with observation, problem, or direct value statement.

---

### 2. Personalisation — Specific, Not Merged
❌ Fail if personalisation is:
- Generic merge field only (e.g. "Hi {{firstName}}, I love what {{companyName}} is doing")
- Flattery without substance ("I've been following your work")
- Vague ("I noticed your company is growing")

✅ Pass: References a specific signal (role posted, headcount growth, leadership change, recent news).

---

### 3. Offer Clarity — Can They Say Yes or No Immediately?
❌ Fail if the ask is:
- Vague ("Would love to connect and explore synergies")
- Too demanding on first touch ("Book a 45-minute strategy call")
- Missing entirely

✅ Pass: One clear, low-friction ask. "Worth a 15-min call?" or "Want me to send the [lead magnet]?"

---

### 4. No Links
❌ Fail if any touch contains:
- Calendly link
- Website URL
- Any tracked link or redirect

✅ Pass: Zero links. Calendar booking happens after reply, not in the sequence.

---

### 5. Length — Right Size for the Channel
❌ Fail if:
- LinkedIn message > 5 lines on touch 1-2
- Email > 8 lines on touch 1
- Follow-up longer than the opener

✅ Pass: LinkedIn touch 1-2 ≤ 4 lines. Email opener ≤ 6 lines. Follow-ups shorter than openers.

---

### 6. Tone — Human, Not Corporate
❌ Fail if copy contains:
- "leverage", "synergy", "partnership opportunity", "circle back", "touch base"
- Passive voice ("It would be great if we could")
- Three-part lists ("fast, efficient, and reliable")
- Em dashes used more than once

✅ Pass: Reads like a message from a thoughtful person, not a sales deck.

---

### 7. Proof — At Least One Credibility Signal
❌ Fail if there is no credibility signal anywhere in the sequence.

✅ Pass: At least one touch includes a result, client name, case study reference, or relevant number. Example: "We helped a 35-person agency book 12 meetings in their first month."

---

### 8. British English (for RecruiterGTM and UK clients)
❌ Fail if copy uses American spelling:
- "optimize" → should be "optimise"
- "color" → "colour"
- "recognize" → "recognise"
- "realize" → "realise"

✅ Pass: Consistent British spelling throughout.

---

### 9. Follow-up Cadence — Not Too Aggressive
❌ Fail if:
- Follow-up sent same day or next day as opener
- More than 4 touches in a LinkedIn sequence
- More than 5 touches in an email sequence
- No break-up message at the end

✅ Pass: Touch 1 → Touch 2 (day 3-4) → Touch 3 (day 7-8) → Break-up (day 12-14).

---

### 10. ICP Match — Would This Land for the Target?
❌ Fail if:
- Copy references problems the ICP doesn't have
- Proof points are from an irrelevant niche
- Tone doesn't match the audience (e.g. casual copy for enterprise HR Directors)

✅ Pass: Every line is written for the specific persona in the ICP, not a generic prospect.

---

## Output Format

```
VALIDATE-COPY REPORT
====================

Score: X/10

✅ Opener
✅ Personalisation
❌ Offer Clarity — [specific issue]
✅ No Links
⚠️ Length — [Touch 3 is too long at 9 lines]
✅ Tone
✅ Proof
✅ British English
✅ Cadence
⚠️ ICP Match — [proof point references SaaS clients, ICP is recruitment agencies]

ISSUES TO FIX:
1. [Issue + suggested fix]
2. [Issue + suggested fix]

REVISED COPY (if score < 8):
[Full revised sequence]
```

---

## Auto-Pass Threshold

- Score 9-10: Ready to launch
- Score 7-8: Fix flagged issues, re-check before launch
- Score ≤ 6: Rewrite required — use write-sequence command
