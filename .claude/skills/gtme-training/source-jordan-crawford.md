# Jordan Crawford's Signal-Based GTM Methodology (Source Reference)

**Creator:** Jordan Crawford, Founder of Blueprint GTM & Cannonball GTM
**Use:** Anchor reference for Part 1 (list building / signals) of the GTME Training Playbook.
**Primary channels:** Cannonball GTM Substack · On the Edge by Blueprint (edge.blueprintgtm.com) · Blueprint courses (learn.blueprintgtm.com) · YouTube (Blueprint GTM)

---

## 1. Core Frameworks by Name

### FIND Framework (Focus, Investigate, Narrate, Deploy)

Four-phase process for signal-to-campaign conversion, usable with AI tools (Claude, ChatGPT, Deep Research).

**Phase 1: FOCUS**
- Identify existential metrics causing acute business pain RIGHT NOW (not future pain).
- Define ICP by pain intensity + readiness, not firmographics.
- Example: Texada (equipment rental SaaS) — utilization of 60% vs 70%+ = ~$1M profit gap.

**Phase 2: INVESTIGATE**
- Mine 2-5 unique data sources to create merged insights prospects lack.
- Combine public records + proprietary data + behavioral signals.
- Output: ranked list of prospects in pain NOW.

**Phase 3: NARRATE**
- Build a PVP (Permissionless Value Prop) from the data.
- Describe the prospect's situation back to them — no product mention.
- Structure: specific data point → financial impact → one-sentence CTA.

**Phase 4: DEPLOY**
- Warming (4-6 weeks paid social) → marketing sequence → PVP-driven SDR outreach.
- Ship fast, iterate. Benchmarks: 2% baseline reply, 4-5% with signal validation, 15%+ meeting book.

### Pain-Qualified Segment (PQS)

A group experiencing a specific high-tension pain RIGHT NOW meeting three conditions:
1. **Novelty** — pain is new (no workarounds yet)
2. **Criticality** — existential to operations
3. **Identifiability** — data sources can locate them

"The list is the message. You don't need clever positioning — just clearly articulate that you understand and solve their specific pain."

Legal SaaS examples: DISCO (first-time litigation w/ heavy discovery — PACER), Smokeball (3-6x caseload jumps — court filings), Fastcase/VLEX (international expansion — subsidiary + Spanish-language postings), Evisort (late-stage SaaS contract debt pre-IPO — funding + headcount). Winning segments cluster at transition points: expansion, rapid growth, litigation, model shifts.

### Permissionless Value Proposition (PVP)

"A message so specific and valuable the prospect would pay to receive it, even if they never buy your product." Deliver insight FIRST; the meeting comes later.

Real example (equipment rental):
> "Your crane hasn't moved in 47 days. Maxwell Construction, located five miles away, has just pulled a permit for a wind turbine installation, which is likely a six-day job worth $145,000."

Structure: curiosity subject → specific data → quantified $ benefit → solution only at the end (if at all) → 5th-6th grade reading level → NO product name in first message.

How to build: identify acute pain → mine for evidence they have it → combine 2-3 unique insights → describe situation + opportunity, ask for nothing → include a data point that proves you understand their world.

---

## 2. Data Sourcing Methodology: Non-Obvious Sources

**Public records / government data**
- **PACER** (court records): litigation as pain signal; first-time litigation + high discovery = spike. Use: e-discovery.
- **USASpending.gov** (DoD contracts): compliance obligations w/ deadlines. Found 68 DoD contractors = $188B contracts lacking CMMC Level 2 in 60 minutes.
- **Building permits (Shovels.ai)**: equipment needs, scope, timeline; permits filed WITHOUT supporting permits = gap.
- **DOT transit permits (FOIA)**: equipment ownership + idle patterns (crane idle 47+ days).
- **SEC filings / Crunchbase**: funding, hiring, expansion, pivots → high-growth before they've built process.

**Job posting analysis** (Blueprint's origin — Crawford scraped job boards systematically)
- CTO hire outside tech = outsourcing dev (offshore/contractor signal)
- Role rewrites (DevOps → Platform Reliability) = maturity shift + budget reallocation
- Freezes + cuts + cancellations = upcoming layoffs
- Rapid role expansion = tech adoption acceleration
- How: scrape Lever/LinkedIn/Indeed/Greenhouse; track role counts, titles, salary bands, geos month-over-month.

**Company / leadership signals**
- LinkedIn activity (post frequency, speaking, podcasts, publishing) = innovation appetite
- Conference exhibitor/attendee lists (e.g. IBC) = high intent
- Press: funding, board/CEO changes, expansion, partnerships

**Regulatory / compliance triggers (highest urgency)**
- Hard-deadline mandates: CMMC Level 2, SOC 2, GDPR/CCPA, HIPAA. Required under penalty, affects a population, solutions exist, time pressure.

---

## 3. Claude Code / AI Tooling Architecture

**Philosophy:** "Do all your work in Claude Code — building campaigns, analyzing churn, scoring customer health, parsing call transcripts, shipping enrichment pipelines."

**Three use cases:**
1. **List building & segmentation** — query data sources → score matches → export CSV by pain intensity.
2. **Enrichment pipelines** — raw list → enriched with signals (jobs, records, news) + PVP suggestions, via MCP to Shovels/Firecrawl/Exa/Apollo.
3. **Personalization at scale** — 1,800+ unique PVPs in 1 hour (~$0.07/prospect).

**Three master tools (master these, don't sprawl):**
- **Exa.ai** — person/company discovery from full-text web search (decision-makers, contact info, public statements).
- **Firecrawl.dev** — scrape + extract to structured JSON (job postings, permit DBs, regulatory docs).
- **Apify** — content evaluation + full-page scraping (behavioral qualification: speaking history, podcasts, publishing).

**MCP architecture:** Claude reads/writes across all connected systems in real time — no manual export/import. Example ~$400/mo stack: Clearcue + HeyReach + Supabase + Shovels + Clay, all via MCP.

**Workflow:** install Claude Code → cd to working folder → feed a CLAUDE.md context file (company, ICP-by-pain, unique datasets) → ask in plain English. Context persists across sessions, building institutional knowledge. Good starting point: export 180 days of Gong transcripts → match to CRM → ask "what predictive win/loss hypotheses are identifiable from public data alone?"

---

## 4. Signal → Segment → Copy Linkage

**Step 1 — Signal detection:** observable, data-detectable change. Must be new, critical, identifiable.
Examples: DoD contractor w/o CMMC + deadline · construction permit w/o transport permit · hired VP Sales but no sales infra · founder posting 3x more · "Series B to expand into Spanish market."

**Step 2 — Segment qualification:** find everyone with the signal → verify intensity (existential vs nice-to-have) → score readiness (budget, DM, urgency) → cluster.

**Step 3 — Copy crafting:** describe situation back to them, no product name until the final sentence, use the signal's specific numbers + financial impact + opportunity window.

| Signal | Segment | PVP Copy |
|--------|---------|----------|
| Crane idle 47+ days + nearby permit | Rental cos <60% utilization | "Your crane hasn't moved in 47 days. Maxwell, 5 miles away, pulled a $145K permit needing 4 excavators. You own 2." |
| No transport permit filed | Active projects needing equipment | "You have a $250K project starting in 6 days. Permits filed for 2 excavators. You need 4. Here's 3 rental options." |
| High downtime pattern | Fleet-heavy, low-utilization | "Your utilization averaged 58% last quarter. Moving to 70% = $1.2M profit. Here's how similar operators did it." |

---

## 5. Worked Examples

**Case 1 — DoD CMMC (60-min build):** USASpending.gov → 100 contractors → 68 validated → $188B contracts. Hour 1 list, Hour 2 validate emails, Hour 3 deploy. 2% baseline / 4-5% validated reply, 15%+ meetings. "You don't have to be right if you can ship fast."

**Case 2 — Texada (multi-channel):** ICP = rental cos <60% utilization, $5M-$50M rev. Sources: DOT permits + Shovels + licensing DBs. Warming (paid social 4-6 wks) → marketing sequence → PVP SDR. 4-5% reply, 15%+ meetings.

**Case 3 — Construction (live demo):** Shovels + IBC exhibitor list + internal pricing → 1,800+ unique PVPs in 1 hour at $0.07 each. Sample: "3A Composites pulled a $144M Miami permit. You spec composites. Here's how similar suppliers structured bids."

**Case 4 — Legal SaaS PQS:** DISCO, Smokeball, Fastcase/VLEX, Evisort (see §1).

---

## 6. Where Best Material Lives

**Cannonball GTM Substack** (cannonballgtm.substack.com) — must-reads:
- A Quick and Dirty Guide to the Cannonball GTM Methodology (Texada) — best full walkthrough
- The One-Hour List: $188B DoD Contractor Segment in 60 Minutes
- How Jordan Built The Cannonball GTM Prospect List in 30 Minutes
- Brand Blitz: The Art of Finding Pain-Based Segments (4 legal SaaS examples)
- The Cannonball GTM Glossary

**On the Edge by Blueprint** (edge.blueprintgtm.com) — Claude Code + signal dispatches.

**Blueprint courses** (learn.blueprintgtm.com):
- Free: "Who To Target & What to Say" crash course (email sequence)
- Paid: Blueprint Membership (~$2,499/yr) — 443 corpus entries, 10 installable Claude Code tools, 3 courses (AutoClaygent, Agent 7, Who To Target & What to Say)

**YouTube (Blueprint GTM):** Course Overview · "PQS or PVP Message" · "What is a PVP" · "The #1 GTM Engineer In The World."

**Podcasts:** E60 The Claude Code Era (Revenue Leadership) · GTM 133 (GTMnow) · The Transaction Ep 55 · Martech Podcast Crash Course · The RevOps Review · SaaS Group "A+ Campaign in 1 Hour."

---

## 7. Frameworks Glossary

| Framework | Definition |
|-----------|-----------|
| FIND | Focus → Investigate → Narrate → Deploy |
| PQS | Pain-Qualified Segment — group in high-tension pain NOW |
| PVP | Permissionless Value Prop — message valuable enough to pay for |
| The List Is The Message | targeting accuracy = message effectiveness |
| Existential Data Point | critical metric creating genuine urgency |

---

## 8. RecruiterGTM Translation

- Signal-based lists for recruiter client-acquisition (job postings + hiring patterns + funding/expansion) and candidate sourcing (people at signal-flagged firms).
- Pain-to-copy for ContentOS + OutboundOS (describe the recruiter's pain, not our service).
- Claude Code signal mining: CLAUDE.md + job boards + leadership moves + Apollo/Apify enrichment via MCP.
