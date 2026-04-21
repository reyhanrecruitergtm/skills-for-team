# Command: auto-refine

Reads campaign performance data and automatically updates ICP targeting, copy angles, and signal priorities based on what's actually converting. Closes the loop between results and strategy.

---

## When to Use

- After 4+ weeks of a campaign running (enough data to learn from)
- When reply rates drop below benchmarks
- Monthly campaign review for retainer clients
- When a client asks "why isn't this working?"

---

## Inputs Required

Paste or describe:
1. **Campaign stats** — contacts reached, connection rate, reply rate, interested rate, meetings booked
2. **Who replied positively** — company size, industry, title, which touch they replied to
3. **Who didn't reply** — any patterns in the silence?
4. **Objections received** — what are people saying when they decline?
5. **Current ICP definition** — what we were targeting

---

## Benchmarks (RecruiterGTM Standard)

Compare actual performance against these targets to identify gaps:

| Metric | Benchmark | Below benchmark = problem |
|--------|-----------|--------------------------|
| LinkedIn connection rate | 35–50% | ICP too cold, profile weak, or message too salesy |
| LinkedIn reply rate (of connected) | 15–25% | Copy issue or wrong persona |
| Email open rate | 40–55% | Subject line, deliverability, or sender reputation |
| Email reply rate | 3–8% | Copy, offer clarity, or list quality |
| Interested rate (of replies) | 25–40% | Offer mismatch or wrong ICP |
| Meeting conversion (interested → booked) | 60–80% | Response speed or friction in booking |

---

## The 5 Refinement Areas

### 1. ICP Refinement

**Ask:** Who actually replied positively? What do they have in common?

Look for patterns in:
- Company size (are smaller companies converting better than larger?)
- Industry (any sector over-indexing on positive replies?)
- Title (which exact titles are converting?)
- Signal (did hiring signal prospects convert better than leadership change prospects?)

**Output:** Updated ICP scoring — promote what's converting, demote what isn't.

---

### 2. Copy Refinement

**Ask:** Which touch got the most replies? What angle is resonating?

- If Touch 1 gets most replies: opener and observation are working
- If Touch 3 gets most replies: opener is too weak, follow-up is saving it
- If break-up email gets most replies: you're waiting too long to add value

**Common copy fixes:**
| Problem | Fix |
|---------|-----|
| Low open rates | Test new subject line — shorter, more specific |
| Low reply rate | Test new opener angle — change the observation |
| High open, low reply | Offer isn't compelling or CTA is too demanding |
| Replies but no meetings | Response speed or follow-up friction |

---

### 3. Signal Refinement

**Ask:** Which signal tier produced the best prospects?

Check: Did Tier 1 signals (active hiring) convert better than Tier 2 (leadership change)?

**Update scan-signals.md priority order based on findings.**

---

### 4. Objection Mapping

**Ask:** What are the most common objections?

For each objection:
- Is it a copy problem? (We're not addressing it proactively)
- Is it an ICP problem? (We're targeting the wrong people)
- Is it an offer problem? (The value prop isn't landing)

**Update write-sequence swipe file with objection-busting angles.**

---

### 5. Channel Refinement

**Ask:** Is LinkedIn or email performing better for this ICP?

If LinkedIn >> email: Double down on LinkedIn volume, use email only for follow-up
If email >> LinkedIn: Check if LinkedIn profile needs strengthening
If both underperforming: ICP or offer problem — not a channel problem

---

## Output Format

```
AUTO-REFINE REPORT
==================
Campaign: [Name]
Period: [Date range]
Data points: [Contacts reached]

PERFORMANCE vs BENCHMARK:
✅ Connection rate: 42% (benchmark: 35-50%)
❌ Reply rate: 8% (benchmark: 15-25%) ← main problem
⚠️ Interested rate: 22% (benchmark: 25-40%)
✅ Meeting conversion: 71% (benchmark: 60-80%)

ROOT CAUSE ANALYSIS:
Reply rate is the bottleneck. High connection rate means the profile and connection note are working. Low reply rate means the opening message is not compelling enough.

ICP UPDATES:
- Promote: Companies 50-200 employees (converting 3x vs 200-500)
- Demote: Enterprise 500+ (low reply rate, long sales cycle)
- New priority title: "Head of Talent" converts better than "HR Manager"

COPY UPDATES:
- Change opener angle from [hiring spike] to [leadership change] — leadership change replies converting 40% better
- Touch 2 performing better than Touch 1 — front-load more value in Touch 1
- New subject line to test: "[Company]'s recruitment setup" vs current "[Name], quick question"

SIGNAL UPDATES:
- Tier 1 (active hiring) converting 2.3x better than Tier 2 (leadership change) for this ICP
- Recommend: Prioritise Tier 1 signals exclusively for next 30 days

RECOMMENDED ACTIONS:
1. Rewrite Touch 1 opener — new angle: [specific suggestion]
2. Tighten ICP to 50-200 employees only
3. Add "Head of Talent" to contact title priority list in Clay
4. Test new subject line for 2 weeks before full rollout
```

---

## Refinement Cadence

| Campaign age | Refine |
|-------------|--------|
| Week 1-3 | Too early — let data accumulate |
| Week 4 | First refinement — ICP and copy |
| Week 8 | Second refinement — signals and channel |
| Monthly (ongoing) | Regular auto-refine cycle |
