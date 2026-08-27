# How to Build & Run the GTME Training Playbook

The question isn't "what content goes in the course" — that's already in `SKILL.md` + the two source files. The question is **how to deliver it so the team actually internalizes it**. Here's the recommended path.

---

## The core principle: learn by building, on real client work

Do NOT run this as a passive course (watch videos → read docs → quiz). GTME is a *skill*, not knowledge. The team gets good by building real lists and writing real copy under feedback. So:

> **Turn fulfillment into curriculum.** Every drill runs on a live client's list or campaign. The team learns the method while producing billable work. Nothing is thrown away.

This also solves the "high-agency gap" from `context/team.md` — the team builds domain ownership by owning real outputs, not toy exercises.

---

## Recommended format: 4-week internal cohort

| Week | Modules | Live session | Drill (on real client work) |
|------|---------|--------------|------------------------------|
| 1 | 1-2 (PQS + data sourcing) | 60-min working session, Reyhan leads | Each person writes 3 PQS defs + finds 2 non-obvious sources for a live client |
| 2 | 3-4 (Claude Code pipeline + qualification) | Live build, screen-shared | Build one real 50-row enriched list, every row carrying a signal; rank by readiness |
| 3 | 5-6 (psychology + core copy frameworks) | Copy clinic w/ Lavender | Rewrite a real client email to <50 words / 5th grade; write one segment 3 ways |
| 4 | 7-8 (anti-patterns + signal→copy bridge) | Peer teardown | **Capstone:** ship one real signal-sourced + signal-written campaign per person |

Cadence: ~2 modules/week, one 60-90 min live session, async reading between. Owner: confirm whether Reyhan or a GTM Engineer leads delivery (see open question in `context/team.md`).

---

## The delivery stack (what to build it in)

**Phase 1 — Internal (now):**
- **This skill = the source of truth.** Living markdown. Cheap, versioned, always current.
- **Loom/recorded walkthroughs** of each live session → reusable for new hires (and raw material for Phase 2).
- **Lavender free tier** = copy scoring harness.
- **Claude Code** = the build environment for the list-building drills.

**Phase 2 — Productize (once validated internally):**
- Repackage the validated playbook into a **Skool classroom module** using the `skool-classroom` skill (RecruiterGTM community has OperatorOS/OutboundOS/ContentOS already — this slots into OperatorOS or a new "GTM Engineering" track).
- The team's capstone campaigns become the recruitment-specific case studies (the thing no competitor has — Jordan/Will teach generic B2B).
- Optional: a paid cohort/course for the wider market, since "Recruitment GTM Engineer" is uncontested white space.

---

## Why this beats the alternatives

- **vs. a Notion doc dump:** docs don't build skill; drills on real work do.
- **vs. buying Blueprint Membership and pointing the team at it:** Jordan's material is generic B2B and advanced; without a recruitment-translation layer + guided drills, the team won't transfer it. Buy it in Phase 2 as depth, not as the curriculum.
- **vs. building a polished course first:** you'd be guessing what works. Run it internally, capture what lands, *then* productize. Cheaper and the case studies write themselves.

---

## First three moves

1. Reyhan does the learning path in `resources.md` (≈half a day of reading).
2. Schedule Week 1 session; pick the live client whose data the cohort will build on.
3. Run Module 1-2, record it, capture outputs back into this skill as the first recruitment worked examples.
