# 1st-Degree Connections Qualification (low-hanging-fruit play)

Turn a client's raw LinkedIn 1st-degree connections export into two ranked, ready-to-use lists — **Clients (nurture)** and **Senior Candidates (bench)** — fast, free, and credit-free. This is the warmest, fastest signal of any launch; run it Week 1.

**Validated on Adrian/ALAC (2026-06):** 11,396 connections → 1,443 client targets + 108 Director+ candidates, all in Claude/Haiku, zero enrichment credits.

## Input
LinkedIn `Connections.csv` (Settings → Data privacy → Get a copy of your data → Connections).
- **Skip the 3-line preamble** (Notes:/disclaimer/blank) — the real header starts at `First Name,Last Name,...`.
- Real columns: `First Name, Last Name, URL, Email Address, Company, Position, Connected On`. **Job title = Position** (don't trust "column N" from old prompts — map from the actual header). Emails are mostly blank (LinkedIn privacy) — fine, ranking needs only Company + Position.

## The pipeline (two-stage funnel — order matters for cost)
**Stage 1 — Company ICP fit (dedup FIRST):**
1. Normalise + **dedup to unique companies** (people cluster — 11k people ≈ 7k unique companies; classify the companies, not every row).
2. **Match unique companies against the client's TAM** → instant ICP-Yes, free.
3. **AI-classify the rest** (Haiku, chunked ~750/agent, inline — no sub-spawning): ICP = Yes/No/Maybe. EXCLUDE mega-primes, government/military branches, big tech, universities, staffing/recruiting agencies, generic non-niche. New ICP-Yes companies not in the TAM = **TAM-growth bonus** (add them).
4. Keep only people at ICP-Yes companies (Adrian: 11,396 → 3,037).

**Stage 2 — Person classification (ICP-Yes people only):**
Classify Position (Haiku, chunked, inline) into:
- **Hiring Manager** — owns/influences technical hiring (VP/Director/Head/Chief/Lead of Eng/Programs/Tech/Ops, CTO/COO/CEO/Founder, Eng Manager).
- **Recruiter** — IN-HOUSE TA/people leader who can BUY agency services. **Agency/staffing recruiters → Exclude** (competitors).
- **Candidate** — placeable technical IC. Keep **Director+ only** (Director/Head/VP/Chief/C-level/Founder/Principal/Staff/Lead).
- **Exclude** — everything else.
Add Seniority = Director+ / Below.

## Output (two lists)
- **CLIENTS (nurture):** Hiring Managers + in-house Recruiters → feed the 1st-degree HeyReach nurture (Signal 1).
- **SENIOR CANDIDATES:** Candidate + Director+ → bench/sourcing.
Apply **suppression** (relationship + excluded accounts), dedup by profile URL, first/last already split.

## Cost rule
Whole thing runs **free in Claude/Haiku** — never burn enrichment credits to qualify. Contact enrichment (emails/mobiles) happens later, ONLY on the final shortlist, and writes to TAM_People so it's never repaid (see `signal-library.md` cache).

## Tuning knobs to confirm per client
- "Senior candidate" threshold (default Director+).
- Recruiter handling (in-house buyer vs agency exclude).
- ICP reference = the client's own TAM.
