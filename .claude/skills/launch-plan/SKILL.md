# Launch Plan Skill

Turns a **signed retainer client's** onboarding intake + ~1 week of account research into a **Launch & Scale Strategy** for their GTM engine, mapped to the DeliveryOS 90-day timeline.

Built for the retainer launch process: onboarding call → 1 week research → come back with the strategy → tools setup + ramping → run the 90-day pilot.

**Engine coverage:** OutboundOS is fully built out (default). SourcingOS and ContentOS are stubbed — use the OutboundOS flow as the spine and swap the signal/deliverable layer (see `## Other Engines`).

---

## What This Skill Does

Produces **two outputs** from one intake:

1. **Internal Strategy Doc** (`launch-plan-internal.md`) — the full working strategy for Reyhan + the GTME. Includes signal data, reasoning, copy angles, tool setup checklist, costs, and the DeliveryOS milestone/target mapping. Not shown to the client as-is.
2. **Client-Facing Launch Deck** (`launch-plan-<client>.html`) — the polished launch & scale strategy the client sees on the post-research call. Signals + rationale, copy angles, tool ramp, 90-day timeline. No internal costs, margins, or capacity data.

The internal doc is generated first and is the source of truth; the deck is derived from it.

---

## Locked Rules

### A. Tooling (canonical OutboundOS/SourcingOS stack)
- A0. **DELIVER IN THE CLIENT'S TOOLS — they pay for credits.** The GTM engine is built inside the **client's own Clay, Instantly, and HeyReach** accounts; they pay for their own enrichment credits, sending, and LinkedIn outreach. **Our tools/credits are last resort only.** The ONE exception: the **launch/research phase** — it's fine to use our tools (Prospeo, Exa, Claude research) to build the initial company research, because it helps Reyhan organize and plan. But the moment companies are uploaded into the **client's Clay TAM table**, all enrichment, scoring, signals, and outreach run on the **client's tools/credits**. Never default to spending RecruiterGTM credits for ongoing fulfilment.
- A1. The engine runs on **Instantly** (email), **HeyReach** (LinkedIn), **Clay** (data/TAM/signals), **HyperTide** (deliverability infra), and **Claude Code** (AI ops layer). Never substitute or invent tools.
- A2. When a tool is named in any client-facing artifact, use the affiliate URL + code from `memory/reference_affiliate_links.md`: Instantly (`31AV2`), HeyReach (`SDJKLGDNJKLEW`), Clay (link). HyperTide = **our own infra, passed through at $75/mo, no affiliate**. Claude Code Max = no affiliate.
- A3. Never invent or estimate tool prices. Pull from `memory/reference_recruitergtm_partner_pricing.md` or ask Reyhan (`feedback_never_assume_tool_prices`).

### B. Signals & data
- B1. **Every proposed signal MUST be backed by a real, live-pulled count** from the client's TAM via **Clay + Prospeo** — never Apollo (dropped from the stack). Never invent counts or use round-number placeholders (`feedback_preflight_check`, `feedback_context_for_numbers`, `feedback_data_source_clay_prospeo_not_apollo`).
- B2. Propose **3–4 signals** for an OutboundOS launch — not all 10. Lead with Tier 1/Tier 2 signals that have real volume in this client's market.
- B3. Each signal gets: the data backing it, why it fires for this niche, and the copy angle that matches it.

### C. Format & positioning
- C1. Client deck hero uses co-branding: **"RecruiterGTM × [Company]"** (`feedback_hero_recruitergtm_x_company`).
- C2. No talent-placement positioning anywhere — engine framing only (`feedback_no_talent_placement_online`).
- C3. Never use "ship/ships/shipped/shipping" — use deliver / build / launch / push live (`feedback_no_ship_language`).
- C4. Never reference "The Ops Agent Lda." — entity is RecruiterGTM LLC (`feedback_no_ops_agent_lda`).
- C5. Any CSV/lead list output splits **First Name / Last Name** — never a single Name column (`feedback_csv_names_split`).
- C6. Cross-check every stat against context files before output (`feedback_preflight_check`).

### D. Files
- D1. Save everything to `~/Desktop/Clients/<client>/launch-plan/` (`feedback_client_deliverables_desktop_folder`).
- D2. Don't create stray .md files — the two named outputs are the deliverables (`feedback_no_unnecessary_md_files`).
- D3. Never auto-open files; never send emails — drafts only (`feedback_never_auto_open_files`, `feedback_never_send_emails`).

---

## Inputs (collected on the onboarding call)

Paste whatever exists; the skill flags gaps rather than inventing.

| Input | Used for |
|-------|----------|
| **Current state** | Where their BD is today — manual, spray-and-pray, no system |
| **Desired state** | The outcome target the 90 days drives toward |
| **Previous clients data** | Reverse-engineer the ICP — who they actually win with |
| **Top candidates placed** | Confirms the talent supply side (informs which roles are realistic to win) |
| **Top roles filled** | The functions to target open-job signals against |
| **Current tech stack** | What's already in place vs what we set up + ramp |
| **Niche / vertical** | Drives signal selection + copy angle |
| **Geos** | TAM boundaries for the live pull |

---

## Workflow

### Step 1 — Parse intake
Read the onboarding notes / Fireflies transcript. Build the **ICP hypothesis** by reverse-engineering from *previous clients* + *top roles filled* (company size, vertical, seniority of roles, geo). State it explicitly and flag any missing input.

### Step 2 — Account research (the "1 week")
- Run the `research` agent on the niche + named target accounts for market context.
- Reverse-engineer the TAM boundary from the ICP hypothesis.
- This is where the live data pull happens (Step 3).

### Step 3 — Signal selection (LIVE DATA — non-negotiable)
For the client's TAM, pull real counts to back candidate signals. See `signal-library.md` for the full 10-signal catalogue, DeliveryOS enum mapping, and the exact tool to pull each.

**Data source — Clay + Prospeo ONLY. Never Apollo** (dropped from the stack — see `memory/feedback_data_source_clay_prospeo_not_apollo.md`).

**TAM-build pipeline (canonical orchestration):**
1. **Clay first** — build the TAM in Clay using its Find Companies sources + the ICP filters; Clay is the orchestration layer and signal source-of-truth (job postings, funding, headcount, job-change enrichments are all native here) and feeds DeliveryOS.
2. **Prospeo enrich** — layer Prospeo (15k free credits/mo) for email + mobile + filtered prospecting. NOTE: Prospeo Search Person/Company is not yet wired into `prospeo.py` (only per-person `/enrich-person` is) — flag if a filtered market search is needed before it's built.
3. **Claude web-wide discovery** — use Claude (web search / Apify) to surface companies the standard databases miss — newly-out-of-stealth, niche, emerging — and feed them back into the Clay TAM. This is what closes the "DB underrepresents our market" gap.

The same Clay tables built here become the live engine and the DeliveryOS `signals` rows — never a throwaway count.

**Clay source-filter limits (important):** Clay's Find Companies source CANNOT filter on funding stage or business model (SaaS/B2B/etc.). Do not try to make the source filter precise — you'll lose real TAM. Instead:
1. **Pull broad-but-anchored** on what Clay reliably supports: HQ location, headcount band, Industry (real LinkedIn values), and **include + exclude Keywords**. For a niche TAM (e.g. defense), require a **domain-anchor include keyword** (defense / national security / DoD / dual-use) AND a vertical include keyword so generic companies don't flood in — then add **exclude keywords** for the consumer/commercial contexts that share vertical language (autonomy→self-driving, sensors→consumer IoT, drones→agriculture). Keep excludes conservative — each one risks cutting a dual-use fit; the AI gate is the safety net.
2. **Move the un-filterable criteria to enrichment columns** post-pull (funding stage, founded year) — enrich, then filter.
3. **Enforce precision at the qualification gate, not the source:** the AI data-points (`tam-ai-datapoints.md` — Defense Alignment, Score, Tier) remove non-fits. Rule: domain-alignment = Low → drop; Tier 4 → drop/watch. This is where "no non-fits" is actually enforced.

Output: **3–4 chosen signals**, each with: live count in their TAM ("X companies in your market are posting Y right now"), the DeliveryOS `signals.type` enum, the tier, and why it fires for this niche.

### Step 4 — Copy angles per signal
One distinct angle per signal. Each angle = the trigger event + the value prop tied to it. Follow OutboundOS copy rules: human, 1–2 personalisation variables max, **no links in cold email**, 3-touch minimum per channel. Reference `.claude/skills/gtm-engine/commands/write-sequence.md` for full sequence build if drafting the actual copy.

### Step 5 — Tool setup & ramp plan
For each tool, state: current status (from intake stack), what we set up, and the **ramp schedule**. Email infra (Instantly + HyperTide) warms over weeks 1–3 — never launch cold at full volume. LinkedIn (HeyReach) ramps connection cadence. Clay tables built per chosen signal. Claude Code = the AI ops layer config. Connection requests go out **blank, no note** (`feedback_linkedin_connection_no_message`).

### Step 6 — Map to DeliveryOS 90-day timeline
Map the plan onto the DeliveryOS milestone keys, phases, and targets (see `## DeliveryOS 90-Day Mapping`). Every launch plan produces the same backbone so it drops straight into DeliveryOS.

### Step 7 — Generate internal strategy doc
Write `launch-plan-internal.md` (template below).

### Step 8 — Generate client deck
Derive `launch-plan-<client>.html` from the internal doc, stripping internal-only data. Use the proposal styling from `references/examples/proposal-template.html` as the visual base.

---

## DeliveryOS 90-Day Mapping

Source of truth: `projects/deliveryos/deliveryos-schema.md`. Every OutboundOS launch maps to the same backbone.

### Milestones (`milestones.key`, dates = deal_closed_date + offset)
| Key | Day | What it means |
|-----|-----|---------------|
| `access_collected` | D0–7 | Onboarding intake + tool access gathered |
| `baseline_d30` | D30 | First launch live, baseline volume hit |
| `responses_d60` | D60 | Optimised, second launch, first positive replies |
| `report_d75` | D75 | Performance report + scale recommendation |
| `renewal_d90` | D90 | Validate, scale winners, renewal conversation |

### Phases (`clients.phase`) + Targets (`targets`)
| Phase | Window | Email leads | LinkedIn leads | Positive replies |
|-------|--------|-------------|----------------|------------------|
| **P1** | M1 | 2,000 | 500 | — |
| **P2** | M2 | +1,500 | +500 | — |
| **P3** | M3 | — | — | **5 (guarantee)** |

### 4-week sprint (the setup track shown on the timeline slide)
Discovery & Setup → Build → Launch → Full Operation.

### 3-month bands (shown below the sprint track)
- **Month 1:** Research, ICP definition, market mapping, technical setup (Instantly + HyperTide warm, HeyReach, Clay tables), copywriting, first launch.
- **Month 2:** Optimisation, split testing, second launch.
- **Month 3:** Validation, scaling winners, cutting non-performing angles, renewal.

Timeline slide header: **"From setup to scale inside 90 days."** Always render both the 4-week track and the 3-month bands (`project_outboundos_timeline`).

---

## Internal Strategy Doc — structure (`launch-plan-internal.md`)

```
# <Client> — OutboundOS Launch & Scale Strategy (INTERNAL)
Deal closed: <date> · GTME: <owner> · MRR: <$>

## 1. Current State → Desired State
## 2. ICP Hypothesis (reverse-engineered from past clients + top roles)
## 3. Proposed Signals (3–4) — each with LIVE count, tier, DeliveryOS enum, rationale
## 4. Copy Angles (one per signal)
## 5. Tool Setup & Ramp (Instantly, HyperTide, HeyReach, Clay, Claude Code) — status + schedule + cost
## 6. DeliveryOS 90-Day Map (milestones, phases, P1/P2/P3 targets)
## 7. Risks / gaps / open questions for Reyhan
```

## Client Deck — sections (`launch-plan-<client>.html`)

1. **Hero** — "RecruiterGTM × <Company>" + "Your OutboundOS Launch & Scale Strategy"
2. **Where you are → where we're taking you** (current → desired state)
3. **Who we're targeting** (ICP, no internal cost data)
4. **The signals we're running** — 3–4 cards, each: signal name + the live market data ("142 companies in your market posting senior roles right now") + why it matters
5. **How we'll reach them** — copy angle per signal (concept, not full copy)
6. **Your engine stack** — Instantly + HeyReach + Clay + HyperTide + Claude Code, with affiliate links + the ramp story (no cold-launch)
7. **The 90-day timeline** — 4-week sprint track + 3-month bands ("From setup to scale inside 90 days")
8. **CTA** — "Approve to launch" / Calendly

---

## Other Engines (stubs — build out on first use)

- **SourcingOS:** swap the signal layer for *candidate-side* signals (open roles to source against, candidates moving companies, alumni pools) and deliverables for the SourcingOS engine. Targets shift from leads → candidate conversations (30–50/mo per `context/work.md`). Use `.claude/skills/sourcing-os/` for execution.
- **ContentOS:** swap signals for content pillars + ContentGPS, deliverables for post cadence. Targets = impressions/reach (50k–100k impressions, 25k reach/mo). Use `.claude/skills/content-os/` and the per-client contentos skills.

When first running a non-OutboundOS launch, build out that engine's signal/deliverable section here following the OutboundOS pattern.

---

## Related
- `first-degree-qualification.md` — the Week-1 low-hanging-fruit play: turn a client's LinkedIn connections export into ranked Clients + Senior Candidates lists, free in Claude (two-stage: company ICP fit → person classification).
- `tam-ai-datapoints.md` — the per-company AI-enrichment + ICP scoring schema (Clay AI columns: Defense Alignment, Clearance Likelihood, Score, Tier, persona, wedge, hook…). Run AFTER firmographic enrichment, BEFORE signals.
- `signal-library.md` — full signal catalogue + live-data sourcing + per-signal enrichment/copy columns (read before Step 3)
- `projects/deliveryos/deliveryos-schema.md` — DeliveryOS source of truth
- `memory/project_service_outboundos.md` — 5 deliverables + positioning
- `.claude/skills/gtm-engine/` — sequence writing, signal scanning, reply handling for the running engine
- `references/examples/proposal-template.html` — deck visual base
