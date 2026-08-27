# GTME Training Playbook

**Audience:** RecruiterGTM internal team (Shmookh, Komal, Daniyal) + Reyhan
**Goal:** Make every GTM Engineer on the team fluent in advanced signal-based list building AND signal-driven cold copy — the two skills that separate a real GTME from someone who "uses Clay."
**Weighting:** 60% list building / signals · 40% cold email copy
**Anchors:** Jordan Crawford (Blueprint GTM) for list building · Will Allred (Lavender) for copy

---

## What This Skill Does

This is the canonical training curriculum for turning the RecruiterGTM team into signal-based GTM Engineers. It is BOTH:
1. A **reference playbook** — the frameworks, drills, and standards live here.
2. A **runnable program** — a 4-week internal cohort (one module set per week) where each lesson ends in a drill on a *real client list or campaign*.

Source material (full, unabridged) lives alongside this file:
- `source-jordan-crawford.md` — Jordan's full methodology (FIND, PQS, PVP, data sources, Claude Code stack, worked examples)
- `source-will-allred.md` — Will's full copy playbook (psychology, 16 frameworks, BAR, anti-patterns, scoring)
- `teardown-creative-ideas-campaign.md` — Eric Nowoslawski's "Creative Ideas Campaign" — the canonical signal→copy worked example + a ready OutboundOS template
- `recruitment-space-thought-leaders.md` — our-niche educators (Deep Singh, Benjamin Mena, Whitby, DSP, Tegze, Raath…) with their signature themes, a Q&A topic bank, and white-space we can own. Includes the 10-person tracked watchlist. For mining community content/Q&As.
- `qa-topic-shortlist.md` — 10 highest-engagement topics mined from the watchlist, written as Q&A-ready topics with 2-line outlines. Pick from these for upcoming Q&As.
- `resources.md` — every free + paid link, ranked, with a learning path and a budget
- `delivery-guide.md` — the best way to build and run this as a playbook/course

> Teaching rule (from Will): teach **frameworks, not templates**. Every module explains *why* each element exists so the team can adapt, not copy.

---

## Locked Rules

**A. Structure**
- A1. The 60/40 weighting is fixed: list building leads, copy serves the list. "The list is the message" (Jordan) — copy can only be as good as the signal behind it.
- A2. Every module = Principle → recruitment worked example → drill on real client data. No passive reading-only modules.
- A3. Recruitment examples always. The anchors teach generic B2B; our job is to translate every framework to recruitment (finding clients for recruiters + sourcing candidates).

**B. Standards the team is held to**
- B1. No list ships without a named signal behind every segment (novelty + criticality + identifiability — Jordan's PQS test).
- B2. No copy ships that fails Will's pre-send checklist (Part 9 of `source-will-allred.md`): observation tied to a problem, 5th-grade reading level, one idea, tentative tone, interest-based CTA.
- B3. Observation ≠ problem. "They're hiring" is an observation; "they're scaling sales with no ops layer" is a problem. Always make the jump.
- B4. No product/service name in the first line of any PVP-style message. Lead with their situation.

**C. Tooling**
- C1. The team's signal stack maps to Jordan's three master tools: **Exa** (discovery) · **Apify/Firecrawl** (scrape/extract) · **Apollo + Clay** (enrich), orchestrated in **Claude Code** via MCP.
- C2. Lavender free tier is the copy practice harness — write, score, learn the rules by feedback. Target 90+.

---

## The Curriculum (8 modules → 4 weeks)

### PART 1 — LIST BUILDING / SIGNALS (60%) · Jordan Crawford

**Module 1 — Pain-Qualified Segments (the mindset shift)**
- Concept: stop targeting by firmographics, start targeting by *pain happening right now*. The 3 tests: Novelty, Criticality, Identifiability.
- "The list is the message."
- Recruitment example: instead of "recruitment agencies, 5-50 staff," target "agencies that just lost a biller (LinkedIn departure signal) + still posting active roles" = acute pain, identifiable.
- **Drill:** each team member writes 3 PQS definitions for a current client's ICP — each must pass all 3 tests.

**Module 2 — Non-obvious data sourcing (where signals hide)**
- The source menu: job boards (Greenhouse/Lever/Indeed/LinkedIn), funding (Crunchbase/SEC), leadership moves (LinkedIn), news, regulatory/compliance deadlines, court/public records.
- For each source: what signal it reveals. (Full table in `source-jordan-crawford.md` §2.)
- Recruitment translation:
  - Job postings = a company needs hiring help (client signal) AND tells you who's hiring (candidate signal)
  - Funding round = scaling team = recruiter need
  - VP/Head-of hire = team build coming underneath them
  - Layoffs = available talent + restructuring pain
- **Drill:** pick one client; find 2 non-obvious sources that reveal their buyers' pain. Document the signal each reveals.

**Module 3 — The Claude Code + Exa pipeline (build at scale)**
- Jordan's "master 3 tools" → our stack: Exa (find) → Apify/Firecrawl (scrape) → Apollo/Clay (enrich) → Claude Code (orchestrate via MCP).
- The CLAUDE.md context file: company overview, ICP-by-pain, unique datasets.
- The three jobs Claude Code does: list building & segmentation · enrichment pipelines · message personalization at scale (1,800 messages/hr at ~$0.07 each).
- **Drill:** build one real enriched list end-to-end in Claude Code for a live client. Target: 50 rows, every row carrying a signal.

**Module 4 — Signal → segment → readiness (qualification)**
- Detect signal → find everyone with it → score intensity (nice-to-have vs existential) → cluster into a segment → rank by readiness (budget, decision-maker, urgency).
- Recruitment example walkthrough using Texada-style logic applied to a staffing buyer.
- **Drill:** take Module 3's list, score and rank it by readiness. Top 10 get flagged for outreach.

### PART 2 — COLD EMAIL COPY (40%) · Will Allred

**Module 5 — The psychology (why replies happen)**
- Two drivers: Reciprocity (real personalization = 1200% more replies) + Cognitive Load (3-second decision, 5th-grade reading = 67% more replies).
- Frameworks over templates.
- **Drill:** rewrite one of the team's current client emails to 5th-grade level and under 50 words. Score in Lavender.

**Module 6 — The core frameworks**
- Teach 3 workhorses first: **The Mouse Trap** (1-2 lines, observation + binary question), **Vanilla Ice Cream** (observation → problem → credibility → solution → CTA), **BAR** (Background-Action-Results to embed proof — never link a case study).
- Full 16 in `source-will-allred.md` §2.
- **Drill:** write the same outreach 3 ways (Mouse Trap, Vanilla Ice Cream, Customer Mirror) for one real segment.

**Module 7 — Anti-patterns + CTAs**
- Ban list: broken logic (observation not tied to problem), informative/lecturing tone, pitch-slapping, complex words, linking case studies, multiple ideas.
- Interest-based CTAs ("Is this a priority right now?") not directional ("Open to a call?").
- The P.S. lever (+35% when personalized).
- **Drill:** run a peer teardown — each person reviews another's email against the Part 9 checklist; kill anything that fails.

### THE BRIDGE

**Module 8 — Signal → Copy (where 60% meets 40%)**
- This is the whole point. Jordan's PVP = Will's "observation tied to a problem." Same instinct, two halves.
- Process: take a Module 4 ranked segment → pull the specific signal data per prospect → write a PVP using a Will framework → describe their situation, financial/operational stakes, then one soft ask.
- Recruitment example:
  > "You've had the Senior Recruiter role open 71 days and just posted two more. Most agencies your size hit a ceiling here because sourcing is still manual. Worth a look at how 3 similar firms cleared their backlog?"
- Canonical worked example: Eric Nowoslawski's **Creative Ideas Campaign** (`teardown-creative-ideas-campaign.md`) — "if I were in your shoes, here's how I'd help," 3 ideas each locked to a real offering + AI-personalized per company. Study this before the capstone; it's the whole bridge in one campaign.
- **Drill (capstone):** each team member ships one real campaign — signal-sourced list (Part 1) + signal-written copy (Part 2) — for a live client. This becomes a documented case study added back into this skill.

---

## How to Run It

See `delivery-guide.md` for the full recommendation. Short version:
1. Run as a **4-week cohort**, ~2 modules/week, live working session each week.
2. Every module ends in a drill on **real client work** — not toy data. Fulfillment becomes the curriculum.
3. Capture the team's best outputs back into this skill as recruitment-specific worked examples.
4. Once validated internally, repackage into a Skool classroom module (use the `skool-classroom` skill) or a paid course.

---

## Maintenance

- Add new recruitment worked examples under each module as the team produces them.
- When the anchors publish materially new frameworks, update the relevant `source-*.md` and note it here.
- Keep this skill as the single source of truth — do not fragment GTME training notes into `/memory/`.
