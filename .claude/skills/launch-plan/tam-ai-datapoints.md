# TAM AI Enrichment Data Points (Clay AI columns)

The canonical per-company data-point schema for an OutboundOS launch TAM, lifted from Adrian/ALAC's "Full Account List" tab — **reuse this as the standard ICP scoring + qualification schema for every OutboundOS client** (adapt the vertical-specific wording per client).

**Build order (locked):** merge + dedup TAM → **firmographic enrichment** (standard credits) → **AI data points** (AI credits, this file) → score → Tier → client approves → THEN signals (`signal-library.md`). Never run the AI columns before the TAM is deduped — AI credits are the expensive ones; only spend them on unique, in-ICP rows.

**Two-pass AI gate (protect AI credits when the source pull is broad/recall-first):**
- **Pass 1 — cheap gate:** run only `Defense Alignment (High/Med/Low)` + confirm US/Canada HQ + headcount + stage. Drop `Low` / out-of-ICP rows here.
- **Pass 2 — full enrichment:** run the expensive AI columns (Score, Tier, P(Close), Confidence, Fit Reasons, Risks, persona, wedge, offer, Insight Hook) ONLY on Pass-1 survivors.
This is the per-company ICP check that replaces aggressive source-side exclude keywords (recall-first pull → precision at the gate).

> Reyhan's intent (2026-06): "after enriching the TAM, find all these data points on the TAM companies within Clay using AI credits." Source tab: `docs.google.com/spreadsheets/d/1N0MM1I0SPwEU1DFTjPs4tgqEPR-1ZhMe` (gid 852225276).

---

## Group 1 — Firmographic (standard enrichment, NOT AI credits)
Resolve these first, from the merge + Clay/Prospeo/Exa enrichment:

| Field | Notes |
|-------|-------|
| Company | name |
| Website / Domain | dedup key |
| Vertical | e.g. "Defense & Space", "Autonomy", "Deep Tech" |
| HQ | country (US gate) |
| Location | City, State |
| Stage | Seed / Series A / B / C |
| Employee Band | headcount or band |
| Funding Range | last round / total |
| LinkedIn | company URL |

## Group 2 — AI-generated (Clay AI columns — AI credits)
One AI column each. Value formats taken from the real sheet (e.g. Red 6 = Defense Alignment High, Score 97, Tier 1, P(Close) 86, persona VP Engineering, wedge "Cleared talent scarcity angle", offer "Embedded Growth ($8K/mo)").

| Data point | Value format | What the AI column assesses |
|------------|--------------|------------------------------|
| **Defense Alignment** | High / Med / Low | how defense/dual-use the company's mission is |
| **Clearance Likelihood** | High / Med / Low | likelihood roles need cleared talent (ALAC's edge) |
| **Hiring Likelihood 90d** | High / Med / Low | AI *estimate* of near-term hiring (the real live signal is layered later from `open_jobs`/`backfill` — this is the pre-signal estimate) |
| **Score** | 0–100 | composite ICP fit from geo + vertical + stage + size + defense alignment + clearance likelihood |
| **Tier** | 1 (85+) / 2 (70–84) / 3 (55–69) / 4 (<55) | matches Adrian's existing tier bands |
| **P(Close)** | 0–100 | estimated close probability |
| **Confidence** | High / Med / Low | model confidence in the assessment |
| **Top 3 Fit Reasons** | pipe-separated, 3 items | e.g. "US-based (core ICP) \| High defense alignment—cleared talent need \| Defense & Space—core ALAC vertical" |
| **Top 2 Risks** | pipe-separated, ≤2 items | e.g. "None significant—strong fit" |
| **Best Entry Persona** | title | e.g. "VP Engineering" |
| **Backup Persona** | title | e.g. "Head of Talent/People" |
| **Best Wedge Strategy** | short phrase | e.g. "Cleared talent scarcity angle" |
| **Best Offer Type** | offer + price | e.g. "Embedded Growth ($8K/mo)" |
| **Trigger / Why Now** | sentence | e.g. "Post-Series B/C growth mandate — likely scaling leadership team" |
| **Insight Hook** | sentence (cold-open line) | e.g. "Seeing defense & space companies hit a ceiling when they can't find cleared engineering leaders—curious how you're navigating that" |
| **Next Action** | Pursue Now / Nurture / Watch / Skip | routing decision off the Tier |

---

## TAM Build Method — multi-source union → triage → AI dual-use recovery (LOCKED)

The proven sequence for building a launch TAM (validated on Adrian/ALAC, 2026-06):

1. **Multi-source pull** — gather from all available sources for max recall:
   - Client's existing list · Clay export (keyword-anchored) · Claude web research (sub-sector fan-out) · Exa (`findSimilar` + stealth) · **Prospeo `search-company`** (30M DB; the richest — returns funding, live job_postings, NAICS/SIC, AI descriptions, founded, revenue). Prospeo has NO keyword filter, so anchor via Industry enum + headcount + location and accept noise.
2. **Dedup into one union** by normalized domain (prefer the richest source's row on overlap — usually Prospeo).
3. **FREE rule-based triage** (Python, zero credits) → STRONG / MAYBE / NOISE, scored from: industry, defense NAICS prefixes (3364, 334511, 33641x, 332994, 336992, 5417x), defense keyword hits in description+keywords, minus noise terms (news/media/staffing/agency).
4. **AI dual-use recovery (CRITICAL — do NOT skip):** rule-based keyword gating **over-drops dual-use** companies whose descriptions don't say "defense" (e.g. a fabless FPGA maker, an airship company, a rad-hard diamond-semi startup all serve defense but read generic). So run an **AI classification pass over MAYBE + the deep-tech/aero NOISE** (not the clearly-off NOISE like agriculture/media/staffing) to recover real dual-use fits. Run it on **Claude (subagents, free)** — reserve Clay AI credits for final enrichment. This pass doubles as Pass-1 Defense Alignment scoring.
5. **Score survivors** (this file's AI data points) → Tier → client approves → signals.

**Why it matters:** on ALAC, the free triage cut 18,365 → ~8k, but ~9,300 "noise" rows were in deep-tech/aero industries where dual-use fits hide — deleting them outright would have lost real TAM. Recover with AI, never with keyword rules alone.

## Notes
- **Scoring consistency:** re-score Adrian's existing 698 with the SAME AI columns so old + new companies are comparable (don't trust mixed-vintage scores). The schema above IS the ICP rubric referenced in `SKILL.md` Step 3.
- **Hiring Likelihood 90d vs signals:** the AI column is a static *estimate*; the live `open_jobs`/`backfill` signals (with `job_source` etc.) overwrite/augment it in the signals phase. Keep "fit score" and "intent score" separate.
- **Offer/price values** (e.g. "Embedded Growth ($8K/mo)") must come from the client's real offer ladder — never invent (`feedback_never_assume_tool_prices`).
- **Persona/hook outputs** feed the copy layer — design the Clay → copy mapping so `Insight Hook`, `Best Entry Persona`, and `Best Wedge Strategy` flow into sequence first-lines.
