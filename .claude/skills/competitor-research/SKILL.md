# Competitor Research Skill

Track and analyse competitors in the recruitment agency owner / GTM systems coaching space. Refresh the briefs quarterly and pull a battle card whenever a competitor surfaces on a sales call or in an email.

---

## How to Invoke

- `/competitor-research [competitor name]` — refresh or build the brief for one competitor
- `/competitor-research battle-card [competitor name]` — pull the 1-pager for use on a call or in a reply email
- `/competitor-research compare [competitor name]` — side-by-side comparison vs RecruiterGTM, drop-in for client emails
- `/competitor-research review` — quarterly refresh across all tracked competitors

---

## Tracked Competitors (LIVING LIST)

| Competitor | Founder | Brief location |
|---|---|---|
| The Digital Headhunter (DSP) | David Stephen Patterson | `memory/reference_competitor_dsp.md` |
| Mark Whitby | Mark Whitby | `memory/reference_competitor_mark_whitby.md` |
| The Agency Blueprint | James Blackwell | `memory/reference_competitor_agency_blueprint.md` |

**Add a new competitor when:**
- A client/prospect names them on a sales call as an alternative
- They surface in 3+ Skool community conversations
- They run paid ads in our LinkedIn audience
- They publish a methodology/framework that overlaps with ours

---

## Competitor Brief Template (the deep dive — saved in memory)

Every competitor brief follows this structure. Saved as `memory/reference_competitor_[slug].md` with `type: reference`.

```markdown
---
name: Competitor — [Name]
description: [3-line summary: who they are, what they sell, who they serve]
type: reference
last_refreshed: YYYY-MM-DD
---

## At a glance
[3-line summary]

## Founder
- Name, age range, location
- Recruitment / GTM background, prior firms
- Public profile reach (LinkedIn followers, podcast audience, X)
- Active or stale on social

## Core offer & methodology
- Named programs / tiers
- Methodology name and pillars (what they actually claim)
- What gets delivered vs what's just marketing language

## Pricing (with sources)
- Public pricing if shown
- Tier costs found in podcast mentions / LinkedIn / Reddit / third-party reviews
- Whether pricing is hidden behind a sales call (a tell)

## Tech stack
- AI tools (Claude, GPTs, custom builds)
- Outbound stack (Lemlist, Instantly, HeyReach, Apollo, Clay)
- ATS / CRM
- Workflow automation
- How modern is their stack vs the 2026 standard

## Community / coaching structure
- Skool, Slack, Circle, Mighty Networks, paid Discord, none
- Frequency of live calls, 1:1, group
- Whether community is one-way (podcast/newsletter) or two-way

## Track record
- Claimed numbers (clients, students, revenue)
- Verified numbers (Trustpilot, named case studies, video testimonials)
- Gap between claimed and verified

## Target ICP
- Solo / small / scaling agency
- Country focus
- Niche focus (exec search, contingent, retained, healthcare, tech, etc.)

## Recent activity (last 90 days)
- New programs, podcasts, content drops
- Whether they're shipping or coasting

## Overlap with RecruiterGTM
- Where their offer overlaps ours
- Where it diverges
- Surface-level overlap vs core overlap

## Where they're genuinely strong
- Be honest. Don't dismiss real strengths.

## Where they're weak / gaps
- Specific gaps RecruiterGTM fills

## Red flags or things to verify
- Marketing claims that don't match the methodology
- Vague guarantees
- Anonymous testimonials only
- Stale brand signals

## Sources
- Direct URLs (homepage, programs page, pricing page if visible, founder LinkedIn)
- Podcasts / interviews
- Third-party reviews
```

---

## Battle Card (the 1-pager — used on sales calls and email replies)

Pulled on demand. Format:

```
COMPETITOR: [Name]
THE PITCH IN ONE LINE: [their core promise]

WHEN A PROSPECT MENTIONS THEM:
1. [Where they're genuinely strong — acknowledge honestly]
2. [Where the surface overlap with us hides a different bet]
3. [The single sharpest differentiator we have]

3 QUESTIONS TO ASK THE PROSPECT:
- [Question that exposes a gap their offer doesn't fill]
- [Question that surfaces a need we uniquely serve]
- [Question that lets the prospect pick honestly]

REFRAME (NOT FEATURE-MATCH):
"[Competitor] is built for [their actual core bet]. We're built for [our actual core bet]. If your priority is [X], they're a real choice. If your priority is [Y], we're the better fit."

DO NOT:
- Trash the competitor — losing trust isn't worth winning the deal
- Feature-match item by item — pulls into their frame
- Claim parity on things we don't ship

LAST REFRESHED: YYYY-MM-DD
```

---

## Side-by-side Comparison (for emails like Patrick's)

Used when a prospect explicitly asks for a comparison. Output format:

```
HONEST READ on [Competitor] vs RecruiterGTM:

Where [Competitor] is genuinely strong:
- [Real strengths — track record, experience, brand reach]
- [Their guarantee or differentiator if real]

Where RecruiterGTM is different (not better, different):
- [Tech generation or methodology gap]
- [Capacity layer or service we offer they don't]
- [Pricing transparency or accessibility]

Frame for the decision:
- If you want X, go with [Competitor].
- If you want Y, RecruiterGTM is the better fit.

[Optional: one specific gap in their offer that matters for this prospect's stage]
```

---

## Research Process (per competitor)

When refreshing or building a brief:

1. **Homepage** — what they SELL at the top of funnel
2. **/process or /how-it-works** — what they actually DELIVER
3. **/pricing or any pricing pages** — public pricing if visible
4. **Lead magnet / methodology PDF** — what their actual framework promises (often less than the sales pages)
5. **Founder LinkedIn** — recent posts, audience size, current positioning
6. **Podcast / YouTube** — audience size, sponsor money, content tone
7. **Trustpilot, Google Reviews, Reddit r/recruiting, LinkedIn comments** — third-party signal
8. **LinkedIn ads library** — are they actively running ads, what angles
9. **Their community (if accessible)** — Skool/Slack member count, post frequency

**Always cross-check:** does the homepage sales page match the methodology PDF? When they don't match, the homepage is marketing, the PDF is reality.

---

## Refresh Cadence

- **Quarterly** review of every tracked competitor (1st of Jan, Apr, Jul, Oct)
- **Ad hoc** when a competitor surfaces in 3+ sales conversations or runs new ads
- **On addition** — full brief built first time

Mark `last_refreshed` field on every brief. Anything older than 6 months gets a flag in the next review.

---

## Output Examples

When the skill runs, it outputs in 3 modes depending on the request:

1. **Brief mode (default)** — full deep-dive saved to memory
2. **Battle card mode** — 1-pager for in-call use
3. **Compare mode** — drop-in side-by-side for client emails

Default to "Brief mode" if not specified.

---

## Notes for me (Claude / Cristiano)

- Be honest about competitor strengths. Not flattering them, just accurate.
- Don't inflate competitor weaknesses to make Reyhan feel better.
- Cross-check sales-page claims against the methodology PDF / process page. Marketing language often outruns actual delivery.
- When marketing claims don't match the methodology, FLAG IT — that's a real insight for sales conversations.
- The goal is durable competitive intelligence, not a hit piece.
- Update the tracked competitors table at the top of this file whenever a new competitor is added.
