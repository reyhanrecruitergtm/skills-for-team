# Command: ab-test

Structure and track A/B tests for outreach copy. Prevents random guessing — every test is structured, isolated, and produces a clear winner.

---

## When to Use

- Before refreshing a sequence that's underperforming
- When reply rates drop below benchmark for 2+ consecutive weeks
- When you have a hypothesis about a new angle but don't want to risk the whole campaign
- Monthly copy refinement cycle

---

## The Golden Rule of A/B Testing

**Test one variable at a time.** If you change the subject line AND the opener in the same test, you'll never know which one moved the needle.

---

## What to Test (Priority Order)

| Priority | Variable | Why |\n|----------|----------|-----|\n| 1 | Subject line | Highest leverage — affects open rate before anything else |\n| 2 | Opener angle | Second sentence they read — drives reply rate |\n| 3 | CTA | Changes what action you're asking for |\n| 4 | Touch timing | Day 3 vs Day 5 for follow-up |\n| 5 | Sequence length | 3-touch vs 4-touch |\n| 6 | Channel order | LinkedIn first vs email first |

---

## Test Design Rules

### 1. Sample Size
- Minimum 100 contacts per variant before calling a winner
- For LinkedIn: 50 connections per variant minimum (smaller pool)
- Never call a winner before 7 days of data

### 2. Isolation
- Both variants must run simultaneously (not sequentially — sender reputation and timing differ)
- Same ICP segment for both variants
- Same sending domain/inbox

### 3. What Counts as a Winner
- Subject line test: winner = higher open rate (minimum 5% difference to be meaningful)
- Opener test: winner = higher reply rate (minimum 3% difference)
- CTA test: winner = higher interested rate
- Always report the percentage lift, not just the raw number

---

## Test Templates

### Test Type 1: Subject Line

**Hypothesis:** [What you expect and why]

| | Variant A (Control) | Variant B (Challenger) |
|-|---------------------|----------------------|
| Subject | [Current line] | [New line] |
| Contacts sent | X | X |
| Opens | X | X |
| Open rate | X% | X% |
| Replies | X | X |
| Reply rate | X% | X% |

**Winner:** [A / B / No clear winner]
**Action:** [Roll out winner / Run more data / Test next variable]

---

### Test Type 2: Opener Angle

**Hypothesis:** [What you expect and why]

| | Variant A (Control) | Variant B (Challenger) |
|-|---------------------|----------------------|
| Angle | [Current angle — e.g. hiring spike] | [New angle — e.g. leadership change] |
| Opening line | [First sentence] | [First sentence] |
| Contacts sent | X | X |
| Replies | X | X |
| Reply rate | X% | X% |
| Interested | X | X |
| Interested rate | X% | X% |

**Winner:** [A / B / No clear winner]
**Action:** [Roll out / More data / Test next variable]

---

### Test Type 3: CTA

**Hypothesis:** [What you expect and why]

| | Variant A (Control) | Variant B (Challenger) |
|-|---------------------|----------------------|
| CTA | [e.g. "Worth a 20-minute call?"] | [e.g. "Happy to share a quick overview — would that be useful?"] |
| Contacts sent | X | X |
| Interested replies | X | X |
| Interested rate | X% | X% |
| Meetings booked | X | X |
| Booking rate | X% | X% |

**Winner:** [A / B / No clear winner]
**Action:** [Roll out / More data / Test next variable]

---

## Subject Line Bank (Proven for Recruitment Niche)

**Style 1 — Specific observation:**
- [Company]'s recruitment setup
- [Company]'s hiring for [role]
- Quick question about [Company]'s EB strategy

**Style 2 — First name + context:**
- [Name], your [function] team
- [Name] — saw [Company] is hiring
- [Name], one thought on [topic]

**Style 3 — Curiosity gap:**
- Something for [Company]
- [Company] + [RecruiterGTM/client name]
- Intro — [Name]

**Avoid:**
- "Following up" in subject lines (spam trigger)
- Questions in subject lines (lower open rates in recruitment)
- Anything with "free", "guaranteed", "urgent"

---

## Opener Angle Bank (Proven for Recruitment Niche)

**Hiring signal angle:**
"Noticed [Company] has been hiring [X role] for a while — that's usually a sign the search is tougher than expected."

**Leadership change angle:**
"Saw [Name] just joined [Company] as [Title] — congrats to the team. New [title] hires usually have a short window to get quick wins on the board."

**Growth signal angle:**
"[Company]'s headcount has grown [X]% in the last 12 months — that kind of growth puts real pressure on the people function."

**Problem empathy angle:**
"Most [company size] recruitment agencies at [growth stage] find that [specific problem]. Is that something on your radar?"

---

## Output Format

```
A/B TEST BRIEF
==============
Campaign: [Name]
Test type: [Subject line / Opener / CTA / Timing]
Hypothesis: [One sentence — what you expect and why]
Variable tested: [Exact text of both variants]

VARIANT A (Control):
[Copy block]

VARIANT B (Challenger):
[Copy block]

Minimum sample: [X contacts per variant]
Decision date: [Date — minimum 7 days out]
Success metric: [Open rate / Reply rate / Interested rate]
Winner threshold: [X% difference required to call it]

TRACKING TABLE:
[Insert relevant table from above]
```

---

## After the Test

Once you have a winner:
1. Roll it out to the full list
2. Log the result in the campaign notes (date, what won, by how much)
3. Run `auto-refine` to update the copy bank with the winning angle
4. Queue the next test — always have one running
