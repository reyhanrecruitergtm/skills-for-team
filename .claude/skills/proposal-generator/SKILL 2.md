# Proposal Generator Skill

Generate a complete, client-specific RecruiterGTM proposal — slide content + Tella video script — from a Fireflies transcript and/or LinkedIn profile.

---

## Locked Rules

Canonical source of every rule that constrains this skill. Run every proposal through this checklist before opening for Reyhan. Detailed expansions live in the prose sections below — this index is the contract.

### A. Skill invocation (mandatory)
- A1. Every proposal — community, pilot, talent placement, Claude DFY, custom — runs through `/proposal-generator`. No cloning old HTML in Python, no raw agents.
- A2. Always output the Call Brief block (Step 0) before drafting any proposal content.

### B. Call analysis (before drafting)
- B1. Pull the Fireflies summary first. Confirm WHICH service(s) the client actually needs (OutboundOS, SourcingOS, ContentOS, or combo). Never default to single-service without confirming from the transcript.
- B2. List every explicit point Reyhan gave you. Every one must survive revisions — never silently drop or merge.

### C. Pricing rules
- C1. Always show TWO pricing options side by side, one tagged "Recommended". Sole exception: Reyhan explicitly says "ONLY community pricing".
- C2. Default pair = Community ($1,497) + 90-Day Managed Pilot ($2,500/mo for the engine that fits the call).
- C3. The $4,497 Premium tier is dead. Never add it.
- C4. Dollar amounts appear ONLY inside the `<div class="pricing-card">`. Off-limits: hero title, hero sub, closing CTA, section titles, header, email subject/body.
- C5. Each pricing card lists EVERY deliverable in that tier. Counts must match the deliverables section above.

### D. Community-only deliverables (locked structure)
- D1. Every community proposal anchors to 3 pillars in order: (1) Custom Claude Ops Manager, (2) 1st Intent-Based BD Campaign, (3) Benchmarking + Systems Audit + 12mo Support. No 4th pillar.
- D2. Community $1,497 INCLUDES (always list, never as discount): Claude Code Ops Manager DFY setup, 1st Intent-BD Campaign launched, 60-min 1:1 Systems Roadmap call with Reyhan, Website + SEO done for them, 12mo access, Weekly Q&As Wed AND Fri, full module library, 1:1 message support from Reyhan, discounted offshore hire ($3k for members).
- D3. Every community proposal also needs 3+ client-specific value points on top of the standard list. Generic pitches don't convert.
- D4. Pre-sourced candidates / market data tables are NOT community deliverables. They go in the SourcingOS demonstration section as upsell proof.
- D5. Community BD scope = ONE-TIME launch (list + copy + go-live). Optimisation, weekly reporting calls, A/B testing rhythm, "we run BD for you" framing are pilot-only — never bundle into community language.

### E. Community-only formatting
- E1. Header = co-branded "RecruiterGTM × [Client Company]" with both logos + × separator. Page title same format. **APPLIES TO ALL PROPOSAL TYPES** (community, managed pilot, placement, custom) per Reyhan 2026-05-16 — not community-only. Hero eyebrow also reads "RecruiterGTM × [Client Company]". Hero H1 can stay outcome-focused but the × branding must be visible in eyebrow + header. See `feedback_hero_recruitergtm_x_company.md`.
- E2. Hero title is outcome/peer-success oriented. NEVER "A custom Claude Ops Manager for [Client]".
- E3. Final CTA = ONE button only: `Join Community →` linking to `https://www.skool.com/recruitergtm`. No mailto, no "Start Now", no secondary buttons.
- E4. NO 90-day timeline or 4-week ramp-up section. Those are pilot-only.
- E5. TAM section shows ONE pill only: total count (e.g. "~110 Sales Managers · Rochester Metro"). NEVER include Contacted/Month or Convos/Month pills on community-only — those are managed-pilot benchmarks.
- E6. Stats grid uses the community 4-card set: 50 OutboundOS Engines · 200+ Use Cases · 25 Claude Ops Managers · 68 Recruitment Businesses Supported. Managed-pilot stats ($550k Q1 2026, 8yrs, 50+ Agencies) FORBIDDEN on community proposals.
- E7. Testimonials = 3 sections in this order: (1) LinkedIn Recommendations + Patrick, (2) Julia Arpag offshore, (3) Instantly + HeyReach proof stack. Pull Abby's markup verbatim. Mike Buontempo BANNED.

### F. Multi-service proposals
- F1. Single service = plain name only ("OutboundOS for {Client}"). Multiple services = numbered ("Service 1 — OutboundOS", "Service 2 — SourcingOS"). Never number a single service.
- F2. Each service's data section follows directly after that service's deliverables. Never group all data at the end.

### G. Managed pilot section (when shown alongside community)
- G1. Pilot section needs full retainer-level detail — NOT a thin 4-week timeline. Six required blocks: deliverables, 4-week sprint, 3-month roadmap, tech stack, conversation benchmarks, pricing line.
- G2. Pilot model is consulting + DFY setup on the CLIENT'S tools. We do NOT run sequences from our Lemlist / our Clay. Pilot = benchmarking, education, setup, weekly direction. Client's stack runs the engine.
- G3. Pilot deliverables (always 7, use 🪓 axe bullets): ICP Market Map, 3 Custom Intent Playbooks, Value-First Copywriting, Email + LinkedIn Outreach Setup, Dedicated Slack, Dedicated GTM Engineer (5+ yrs), Weekly Reporting Call.
- G4. **4-week timeline must use the Jayce Grayye detailed format**, NOT 1-2 sentence summaries. Each week block: `<p class="timeline-period">Week N · [Phase Name]</p>` + `<div class="timeline-title">[concrete deliverable headline]</div>` + `<ul class="week-list">` containing **4 specific concrete actions** for that week (call kickoff, ICP locked, MCP built, sequences live, first reporting call, etc.). Generic "Engine running, replies coming in" lines are banned — reference real artefacts (sequences, playbooks, candidates, dashboards) per week. Reference build: `projects/jayce-grayye-proposal.html` lines 1637–1720.

### H. Voice & copy
- H1. Never use team-member names (Salar, Daniyal, Shmookh) anywhere in the proposal. Always "RecruiterGTM" or "we".
- H2. Tool names (Lemlist, Instantly, HeyReach, Clay, Apify, Apollo, Prospeo, n8n, Pin.com, HyperTide, Stardex, Spott) live ONLY in the Tech Stack section with logos. Everywhere else describe the OUTCOME. Client's own tools (their CRM/ATS) are allowed — those are facts about the buyer, not pitch.
- H3. Banned words: tooling, noise, landscape, leverage, transformative, visibility, precision, invaluable, "breaks through", "amplifies", "streamlines", "optimises", "unlocks potential", figurative idioms ("move the needle", "stalls", "weight in the market"). Corporate transitions: "This ensures that…", "As a result…", "In order to…".
- H4. Max 1 em dash in prose across the entire proposal. Zero is better.
- H5. Never promise "booked calls". Frame as "value-based conversations with key decision-makers".
- H6. Never invent conversation / meeting / placement numbers. Use approved benchmarks: OutboundOS 5-10 DM convos/mo, SourcingOS 30-50 candidate convos/mo, ContentOS 50k-100k impressions + 25k reach/mo. Or omit.
- H7. Never promise team-wide training or "onboard your X recruiters". Proposals are scoped to the single CEO/founder unless Reyhan explicitly scopes wider.
- H8. When referencing community members in case studies, frame as transformation arcs ("they joined paying for X, we swapped them to Y"). NEVER ongoing failure ("members are still spending on X").
- H9. When referencing the data layer, use "data enrichment waterfall (Apify + Apollo + Prospeo)" — never "Apollo" alone.
- **H10. CHANNEL ORDERING — LOCKED (Reyhan flagged 2026-05-19 on Kofi proposal where I wrote "LinkedIn-First Candidate Outreach"):** Default channel order in every proposal is **Email + LinkedIn**. Email goes first, every time. SMS / WhatsApp / voice are OPTIONAL add-ons — frame as "with option to add SMS" or "SMS optional", never as defaults. Banned: "LinkedIn-First", "LinkedIn + Email", "LinkedIn cadence (Email Optional)". Only swap to a LinkedIn-led framing if Reyhan explicitly instructs for that specific client. Tools: Email = Instantly, LinkedIn = HeyReach.
- H10. **Trademark mandatory on the four OS names** every time they appear in a proposal: **OutboundOS™, SourcingOS™, ContentOS™, OperatorOS™**. Hero, pillars, deliverables, service headers, pricing cards, tech stack labels, comparison block, CTA. Not first-mention-only. Not optional. Lifts proprietary perception and matches competitor convention (Blueprint trademarks every framework name — we already have the better systems, take the symbol).

### I. Blocker line
- I1. Default blocker line: `Your biggest blocker is not effort. It's the absence of an engine.` Use this exact wording unless Reyhan explicitly asks for a variant.
- I2. HTML styling: dim "Your biggest blocker is not", bright " effort.", dim " It's", grad " the absence of an engine."

### J. TAM & sample tables
- J1. Managed-pilot proposals: TAM shows 3 pills in order — Total Companies · Reachable Decision-Makers · With Open Jobs (or candidate variant). Single-pill TAM is BANNED on pilot proposals.
- J2. Community-only proposals: TAM shows ONE pill only (see E5).
- J3. Every proposal needs a sample companies table of 8-10 real companies: name, HQ, employees, open roles count, signal, clickable LinkedIn "View →" link. NEVER ship without it.
- J4. Every SourcingOS proposal also needs a 10-candidate sample table with title, company, signal, clickable PERSONAL LinkedIn (in/) links — NOT company (company/) links. If candidates legitimately lack personal profiles (blue-collar), label the column "Employer" and note explicitly.
- J5. Candidate TAM numbers must be (a) pulled live from Apollo with the exact filter shown, or (b) derived from defensible niche-specific math spelled out in the tam-note. Never round-number invention.
- J6. Never reuse the client's internal ATS DB count as a TAM pill. Their DB is their asset (covered by a refresh deliverable). Our TAM is what we source externally.
- J7. OutboundOS company tables prioritize companies with 2+ open roles (Apollo `organization_num_jobs_range` min: 2). Show open-roles count column. Single-job companies under-represent the opportunity.
- J8. **Legal recruiting SourcingOS proposals** must embed the Weil Gotshal scrape demo from `projects/nadeem-sheikh-proposal.html` as live proof: 606 lawyers scraped · 539 LinkedIn matched · 604 verified emails · under 8 min · stack = Pin.com + Apify + SalesQL + Claude Code. Plus 2-3 custom-per-candidate copy examples from that proposal. Reyhan walks legal clients through this on screen and it converts.
- J9. **OutboundOS company tables MUST show a named decision-maker per company, not just a company link.** Required columns: `Company` (with company LinkedIn link OK) · `Decision Maker` (Name + Title) · `Personal LinkedIn` (in/ URL, HTTP-verified) · `Signal` (specific intent — "Hiring 2+ PMs", "Landed $30M project", "5 open roles + no TA", etc.). A company link with no decision maker on it is useless — Reyhan flagged this 2026-05-16. Pull decision makers via Apollo `mixed_people_api_search` with `organization_ids: [orgId]` + senior titles (COO, Founder, Director of Operations, Hiring Partner, GC, etc.) per niche.
- J10. **LinkedIn URLs for proposal tables MUST come from Apollo `people_bulk_match` (enrichment by Apollo ID), NEVER from web search or research agents.** Reyhan flagged 2026-05-16 that web-research-sourced URLs are often plausible-looking but wrong — they pass HTTP verification but resolve to a different person with the same name. Apollo is the authoritative source (their data is scraped from LinkedIn). Workflow: (1) Apollo `mixed_people_api_search` with org filter to get candidate Apollo IDs, (2) `apollo_people_bulk_match` by ID to enrich and pull verified `linkedin_url`, (3) drop any NULL match from the table — never substitute with a web-search URL. Cost: 1 credit per match, 0 for misses. 10 candidates = max 10 credits. **Approval is implicit when Reyhan asks for verified URLs on a proposal.**
- **J11. SIGNAL COLUMN — LOCKED (Reyhan flagged 2026-05-18, after I shipped Towfeq / Ryan / Vaspian with US state names as "signals" and "Senior Legal" as candidate signal).** The Signal column is the INTENT signal — never a state name, never a generic seniority label.
  - **BD-side (OutboundOS company tables) — pull live from Apollo + Apify combo:**
    - `Hiring {N} roles` — from Apollo `organization.num_jobs` per company (always show the actual count, not "Hiring")
    - `Headcount +{X}% YoY` — from Apollo `organization.organization_headcount_growth.six_month_growth` or `twelve_month_growth`
    - `Recent funding` — from Apollo `organization.latest_funding_stage` + `latest_funding_round_date` (within last 12 months)
    - `New CEO / CTO / CHRO` — from Apollo job-change tracking on the org's leadership
    - `Lateral partner move` (legal) — from Apify-scraped law firm announcements + Apollo org changes
    - `M&A event` — Apify news scrape
    - `Just won {contract}` — Apify scrape of company press releases / news
  - **Candidate-side (SourcingOS candidate tables) — pull live from Apollo + Apify combo:**
    - `Open to work` — LinkedIn open-to-work flag via Apify LinkedIn scraper
    - `Tenure 2+ yrs (move-ready)` — Apollo `employment_history.current_role_duration_months >= 24`
    - `Recent promotion` — Apollo job-change tracking, title change within last 6 months at same company
    - `Just left previous role` — Apollo job-change tracking, role change within last 90 days
  - **BANNED as signals:** US state names, country names, generic seniority labels ("Senior Legal", "C-Suite", "VP+"), industry labels ("Tech", "Legal", "Manufacturing"). Those describe WHO the person is, not WHY they're a signal-driven target. If you don't have a real intent signal for that row, drop the row — never pad with a junk badge.
  - **Apollo fields to request:** when calling `people_bulk_match`, the response always includes `organization.num_jobs`, `organization.organization_headcount_growth`, `organization.latest_funding_*`. Use those directly. For candidate signals, run a second `people_bulk_match` with `reveal_personal_emails:false` and check `employment_history` + `last_updated_at`.
  - **TAM column order — LOCKED:**
    - OutboundOS (BD): `Company` · `Signal` · `Decision Maker` (Name · Title) · `LinkedIn` (in/ URL)
    - SourcingOS (candidate): `Name` · `Title` · `Company` · `Signal` · `LinkedIn` (in/ URL)
  - **TAM pills — LOCKED:** Always 3 pills per niche when shown. Format: `{Total DMs in niche}` · `{Hiring 2+ Open Roles}` · `{Niche-specific filter}` (e.g. mid-size only, or recently-funded). Multi-niche proposals (per Ryan Jaco) get 2 pills per niche side-by-side. Single number labelled "TAM" is BANNED on multi-engine pilots.

### K. ContentOS-specific
- K1. ContentOS-only proposals MUST include 1 LinkedIn connection-only campaign alongside content. Content without a connection campaign is half a system. (If bundled with OutboundOS, the outbound engine covers it.)
- K2. ContentOS section MUST embed the 2 real ContentOS proof screenshots (`references/testimonials/ContentOS sample 1.png` + `ContentOS sample2.png`) base64. NEVER substitute fake stat cards or made-up numbers.
- K3. Newsletter setup + subscriber capture is always an OutboundOS deliverable. NEVER a ContentOS deliverable.

### L. Formatting
- L1. Features / deliverables / value props ALWAYS in bullets. Never crammed into prose. Use 🪓 axe bullets in proposal pricing cards / deliverables.
- L2. OutboundOS icon = lightning bolt (Power Bolt): 3D crystal bolt, purple neon glow, sparks, black background.
- **L3. TECH STACK — NON-NEGOTIABLE. Every proposal MUST include the FULL canonical 14-pill tech stack with logos. Reyhan has flagged this 12+ times.** Canonical 14 in order: **Clay · Lemlist · Claude · HeyReach · n8n · Pin.com · Apify · Instantly · SalesQL · HyperTide · Apollo · Prospeo · Stardex · Spott.** Recruit CRM REMOVED 2026-05-16. **No default ATS pill** — only add a tool if Reyhan explicitly names it for that client. Reference build: `projects/inject_tech_stack.py` (extracts Alina's 12 base64 logos + adds 2 favicon pills for HeyReach + SalesQL). Validation: `grep -c "tech-pill" <file>` MUST = 14. Dialed-down or placement proposals — STILL 14 pills, no exceptions. See `feedback_tech_stack_canonical.md`.

### M. Build mechanics
- M1. Always copy master template (`references/examples/proposal-template.html`), then swap content. Never build from scratch.
- M2. NEVER use non-greedy regex `<div>.*?</div>` to replace nested HTML sections — it stops at the first inner `</div>` and leaves orphans. Use sentinel comments (`<!-- ── SECTION_START ── -->` / `<!-- ── SECTION_END ── -->`) + flat-string replace.
- M3. Required sentinels in master template: PROBLEMS, BLOCKER, COMPARISON, PILLARS, DELIVERABLES, TAM, CANDIDATES, TIMELINE_21DAY, TIMELINE_90DAY, TECH_STACK, INVESTMENT, GUARANTEE, CLOSING.
- **M3a. CANONICAL SECTION ORDER (LOCKED — Reyhan flagged 2026-05-16, updated 2026-05-18):** HEADER → HERO → WHO AM I → **REAL CAMPAIGN RESULTS** → **TESTIMONIALS** → PROBLEMS → BLOCKER → **COMPARISON** → SOLUTIONS / PILLARS → SERVICE 1 (DELIVERABLES + TAM + CANDIDATES) → SERVICE 2 (...) → SERVICE 3 (...) → TIMELINE → TECH STACK → INVESTMENT (with PAYBACK LINE inside every pricing card per S4) → **GUARANTEE** → CTA. Reference build = `~/Desktop/proposals/justin-williams-proposal.html`. **TESTIMONIALS are NEVER at the end** — they always sit near the top right after Campaign Proof, before Problems. Cutting/moving testimonials to the bottom is BANNED. For dialed-down proposals that skip WHO AM I or PROBLEMS, testimonials still sit early (right after Hero / Campaign Proof). **COMPARISON and GUARANTEE blocks are mandatory on every proposal** — see locked rules Q and R for content.
- M4. Every build script ends with the orphan grep + div-balance check. Any hit = build failed, fix before shipping.
- M5. Every proposal is copied to `~/Desktop/proposals/` AND synced to `projects/` after build.
- M6. Every LinkedIn URL in the proposal is HTTP-verified before delivery (200 = valid, 999 = LinkedIn rate-limit flag for manual check). Any broken URL = build defective.
- M7. NEVER run plain find/replace across an HTML file that contains base64 data URLs — common short strings ("Atlas", "Daniel", any 3-5 char word) frequently appear inside base64 PNG data. A replacement changes the base64 length and breaks the image decoder. Before doing any global text substitution: stash every `data:image/...;base64,...` block behind a placeholder (e.g. `__BLOB_N__`), run replacements on the rest, then restore the blobs untouched.

### N. Send email (every proposal)
- N1. On finalize, ALWAYS draft the proposal-send email in Gmail (`gmail_create_draft`). Never skip.
- N2. ALWAYS show the email copy (To, Subject, Body) in chat for Reyhan to approve BEFORE creating the Gmail draft.
- N3. Subject line format: `RecruiterGTM Proposal - {Company Name}`. No services, no angle, no pricing in the subject.
- N4. Use the locked template in `reference_proposal_send_email_template.md` verbatim. Never bold lines, never restructure, never add sections, never insert "[INSERT TELLA URL]" placeholders.
- N5. **Send-email Tella line is MANDATORY on every proposal-send email** (managed-pilot, retainer, custom community, placement — all of them). Line 4 of the locked template per `reference_proposal_send_email_template.md`: "Here is a short Tella walkthrough I recorded for you (MUST WATCH)." — Reyhan adds the Tella link manually before sending. Framing = "must-watch BEFORE opening the proposal" with CTA "when do you want to start" (never "open in your own time"). Reyhan flagged 2026-05-16 after I had incorrectly dropped the Tella line from retainer/placement emails — that was a misread of his earlier comment about in-proposal Tella sections, not the send-email line.
- N6. Short template only. Do NOT recap the proposal in the email. The proposal is the proposal; the email is the handoff note.

### O. Agreements & contracts
- O1. NEVER commit to specific conversation / meeting / placement / revenue numbers as "targets" or "outcomes" inside a signed agreement PDF. Benchmarks live in proposals, not contracts. The only outcome language allowed in a contract is the Limitation of Liability disclaimer. Justin Daleo's 5-convos/mo clause is a one-off exception, not standard.

### Q. Comparison block (mandatory section)
- Q1. Every proposal includes a COMPARISON block. Slot in the section order: **after BLOCKER, before PILLARS/SOLUTIONS**. Frame: "The Old Way (Manually Doing It All)" on the left vs "The Intent-Based Engine" on the right.
- Q2. Rows mirror the 3 client-specific problems named in the PROBLEMS section, 1:1. Each row pairs that exact problem (left, manual version) with its RecruiterGTM engine answer (right). This is the bridge that turns named pain into the named engine they're buying.
- Q3. Row template (use the OS™ name in the right column):
  - **Old way row 1 (lead gen pain)** → OutboundOS™ intent-based campaigns
  - **Old way row 2 (sourcing pain)** → SourcingOS™ enrichment waterfall (Apify + Apollo + Prospeo + Pin.com)
  - **Old way row 3 (operator/admin pain)** → OperatorOS™ + Claude AI Ops Manager
  - **Old way row 4 (content/authority pain — if pitched)** → ContentOS™ engine
- Q4. Visual: 2-column dark theme. Left column muted with strike-through styling on each line. Right column uses 🪓 axe bullets to signal upgrade.
- Q5. NEVER use generic rows ("Cold calls → Multichannel outbound"). Every row must echo the specific problem language from this client's PROBLEMS section so the prospect sees their own words on the left.

### R. Guarantee block (mandatory section)
- R1. Every proposal includes a GUARANTEE block. Slot in the section order: **after INVESTMENT, before CTA**.
- R2. Guarantee copy varies by proposal type:
  - **Managed pilot / retainer:** *"We work with you until your engine is generating your first 5 qualified conversations."*
  - **Community-only:** *"We work with you until your Claude AI Ops Manager is live and running for your agency."*
  - **Multi-service:** stack both — one guarantee line per service tier card.
- R3. NEVER tie the guarantee to revenue ("until you close $X", "first retainer won", "until you make placements"). Outcome is operational, never commercial. We can't guarantee market behaviour. This is also what keeps us clear of competitor guarantee-trap framing.
- R4. Format = single ~3-line section. Headline "Our Guarantee" + the locked sentence + nothing else. No fine print, no carve-outs, no "as long as you commit and show up" qualifiers.

### T. Who Am I — canonical 4-stat grid (retainer agreements only)
- **T1. Every RETAINER / managed-pilot proposal's `Built solely for Recruitment Agencies` Who Am I section** uses the SAME 4 stat cards under `What the Engine Delivers`, in this exact order. Scope: retainer agreements only (OutboundOS / SourcingOS / ContentOS / multi-engine retainers). Community-only proposals use the E6 grid instead.
  1. `~5–8` — Qualified DM conversations per month from a live outbound engine *(tilde required — signals approximation, not hard promise — Reyhan added 2026-05-19)*
  2. `18 days` — From discovery to a fully live system — ICP mapped, copy approved, launched
  3. `200+` — Recruitment GTM systems deployed across agencies in the UK, US, and beyond
  4. `50` — Agencies running OutboundOS for us right now
- T2. Banned in the Who Am I slot: "8 yrs", "~5–10", "5–8" (no tilde), "4 wks", "30–50". The 30–50 candidate-conversation benchmark is a SourcingOS body number per H6, not a Who Am I metric.
- T3. Community-only proposals (Daniel Edgar canonical) use the E6 grid instead: 50 Engines · 200+ Use Cases · 25 Claude Ops Managers · 68 Recruitment Businesses. Never mix.
- See `feedback_who_am_i_canonical_stats.md` for full HTML snippet.

### S. Payback line (mandatory under every pricing card)
- S1. Every pricing card carries a one-line payback sentence directly underneath the price. Format: *"One $15k placement pays this back [Nx over | in [N] days]."*
- S2. Default math, pegged to **$15k average placement fee** (the RecruiterGTM benchmark — never invent a different anchor):
  - **Community ($1,497):** *"One $15k placement pays this back 10x over."*
  - **Managed pilot ($2,500/mo, $7,500 over 3 months):** *"One $15k placement covers the full 3-month engagement 2x over."*
  - **Claude-Code-DFY ($3–5k setup):** *"One $15k placement pays this back 3–5x over."*
  - **Talent placement standalone:** *"One $15k placement pays this back in full on day one."*
- S3. If the client mentioned their own placement fee on the discovery call, swap $15k for their number and recompute. Otherwise the $15k anchor is canonical — never round-number invention.
- S4. Payback line is part of the INVESTMENT section, NOT a separate section. Sits inside each `<div class="pricing-card">` directly under the price, above the deliverable list.

### P. Pre-ship checklist (run before opening any proposal)
1. Client identity correct — header "Prepared for {name}", hero title, dates, no leftover names like "Arvi Carkanji".
2. Niche / industry framing correct — no SaaS leftovers on a mortgage proposal, etc.
3. Services match the Fireflies action items.
4. Data integrity — no invented TAM, no conflating client DB with our TAM.
5. Tech stack compliance — Instantly + HyperTide standard, never HeyReach + Lemlist together.
6. Blocker line is the canonical default unless Reyhan specified a variant.
7. Claude Ops Manager use cases from the actual call, scoped to single CEO/founder.
8. Every pricing card lists every deliverable (counts match deliverables section).
9. Proof sections use real base64-embedded screenshots.
10. Copy hygiene — zero em dashes, no banned words, no "booked calls".
11. File hygiene — saved to `~/Desktop/proposals/` AND synced to `projects/`.
12. Final grep sweep — `arvi|carkanji|HeyReach.*Lemlist|Salar|Daniyal|Shmookh|\$550k.*community|Mike Buontempo.*community|prior-client-keywords` → all must be zero.
13. URL verification — every LinkedIn link HTTP-verified (200 valid, 999 flag for manual).
14. Orphan grep — orphan-signature scan + div-balance check on each replaced section.
15. **TECH STACK PILL COUNT — `grep -c "tech-pill" <file>` MUST equal 14**. Reyhan has flagged this 12+ times. If count != 14, the proposal is BROKEN. Canonical 14 (Recruit CRM removed 2026-05-16): Clay · Lemlist · Claude · HeyReach · n8n · Pin.com · Apify · Instantly · SalesQL · HyperTide · Apollo · Prospeo · Stardex · Spott. Reference build script: `projects/inject_tech_stack.py`. See `feedback_tech_stack_canonical.md`. **Run this check BEFORE shipping any proposal. No exceptions. Only add a tool if Reyhan explicitly names it for that client.**
16. **Trademark sweep (H10)** — every instance of `OutboundOS`, `SourcingOS`, `ContentOS`, `OperatorOS` in the file carries `™`. Run `grep -cE 'OutboundOS™|SourcingOS™|ContentOS™|OperatorOS™' <file>` and compare against `grep -cE 'OutboundOS|SourcingOS|ContentOS|OperatorOS' <file>` — counts must match. Any bare OS name without ™ = broken.
17. **Comparison block (Q)** present in the section flow AFTER Blocker, BEFORE Solutions/Pillars. Rows mirror the 3 client-specific problems 1:1. Left column = "The Old Way (Manually Doing It All)" with strike-through styling. Right column = "The Intent-Based Engine" with 🪓 axe bullets and the right OS™ name per row.
18. **Guarantee block (R)** present AFTER Investment, BEFORE CTA. Wording matches proposal type: managed pilot/retainer = "first 5 qualified conversations" / community-only = "Claude AI Ops Manager live and running" / multi-service = stacked per tier card. No revenue-tied language.
19. **Payback line (S)** under every pricing card, pegged to $15k average placement fee (or client's own placement fee if shared on the call). No round-number invention.

A proposal that hasn't passed the full checklist is NOT done.

---

### U. GTM Engineer Placement proposals — LOCKED structure (Yael 2026-05-23)

Use this structure for every GTM Engineer / GTM Operator / Ops Integrator placement proposal sold to a **non-recruitment** business owner (AI-native startups, agencies needing an operator next to a founder, anyone buying offshore GTM talent on a flat fee). For recruitment-agency talent placements (SA Sourcer model), use Carolyn Cope's lineage instead.

**Section order (mandatory):**
1. Header — RecruiterGTM × {Client Company}
2. Hero — outcome-focused, name the role + the speed ("place a GTM Engineer next to your clients this week"), NEVER mention price
3. Track Record — 4-stat GTM Academy grid: 200+ placed · $35k/yr savings · 1.5yr retention · 48hr shortlist
4. Testimonials — **Michael Alexander + Julia Arpag Tella videos ONLY** (Mike Buontempo / Patrick / Tyler / Shana / LinkedIn-recs grid all BANNED on non-recruiter clients)
5. **Trained Before Placement** — the 5-skill curriculum block (see U1 below). Mandatory. Goes right after testimonials, before the deliverables.
6. What You Get — deliverables (violet) + guarantees (green)
7. Candidates — pulled live from Stardex job pipeline, each with Loom embed + LinkedIn (when present)
8. Tech Stack — full 14-pill canonical (per L3)
9. Investment — single flat-fee pricing card, split-payment breakdown inside the card (deposit + balance), Whop link on the card button
10. CTA — Whop deposit button + Confirm Picks email button

**U1. Training curriculum — 5 skills, 🪓 axe bullets, locked content:**
- **Clay Signal-Based Playbooks** — Building intent-driven enrichment tables (job-change signals, funding triggers, hiring signals, technographic shifts)
- **Custom Waterfall Builds & Enrichment** — Multi-source waterfalls across Apollo + Apify + SalesQL + Prospeo + HyperTide + Pin.com, ranked by source confidence
- **Copywriting Mastery** — Value-first cold copy for email + LinkedIn + voice; niche-specific hooks, signal-based opens, multi-step sequencing, reply handling
- **Claude Code Mastery** — Custom Claude Ops Manager setup with skills library + MCP integrations to the client's stack (Attio, HubSpot, GHL, Slack, Notion, Stardex)
- **n8n Workflows + CRM Integrations** — End-to-end workflow automation in n8n + Make; webhook ingestion, reply routing, lead scoring, Slack alerts, CRM writebacks

If Reyhan adds new training skills, append to this list. Order = Clay → Waterfall → Copy → Claude → n8n.

**U2. Candidate sourcing — always live from Stardex:** Pull from the GTM Engineer job pipeline (id `88758666-0876-495b-8c1c-5c3aca46b219`) at Sourced stage (or whichever stage Reyhan names). Use `stardex.py persons get <person_id>` to pull full profile including Loom URL from custom field `Video URL` and LinkedIn from `linkedin_public_id`. Never fabricate Loom URLs.

**U3. Pricing default:** $5,000 flat fee unless Reyhan specifies. Default split: $1,000 Whop deposit + $4,000 at contract signing. Reyhan provides the Whop link per client. Always show the split breakdown inside the pricing card, not just the headline.

**U4. Guarantees mandatory:** 60-day replacement + ongoing GTM training for the placed Engineer (lifetime in seat) + 3 ramp-up calls with Reyhan + direct Slack access. These are non-negotiable on every GTM Engineer placement.

**Reference build:** `projects/yael-lederman-proposal.html` + builder `projects/generate_yael_lederman_proposal.py` (Yael Lederman / Kadima Labs, 2026-05-23).

---

## How to Invoke

Paste a Fireflies transcript (and/or LinkedIn profile URL or copied text) and say `/proposal-generator`.

---

## Inputs

- **Fireflies transcript ID** — preferred. Use `mcp__fireflies__fireflies_get_summary` to pull the full transcript summary automatically. Extract everything from there.
- **Fireflies transcript (pasted)** — use if no ID is provided
- **LinkedIn profile** (optional but use when available) — cross-reference: company name, seniority, industry, how long they've been running the agency, any visible content activity
- **Call notes** — supplement if the transcript is thin

From these inputs, determine:
1. Which service to recommend: OutboundOS, SourcingOS, ContentOS, or a combination
2. The 3 client-specific problems to name
3. The relevant testimonials to surface (pick 2–3 from the fixed bank that match their niche/situation)

---

## STEP 0 — Call Brief (Always Output First)

Before generating any proposal content, extract and output a Call Brief in this exact format. This is the structured summary of the call — it makes every other section faster and more accurate to produce.

```
--- CALL BRIEF ---

Business Context:
[What does the agency do, who do they serve, how big are they, how long running]

Niche:
[Recruitment niche — industry, role types, seniority levels]

Location:
[Where they operate, where clients and candidates are based]

Tech Stack:
[Tools they currently use — ATS, sourcing, outreach, CRM, job boards, anything mentioned]

What's Good:
[What's working — strong pipeline, good close rate, solid team, existing system, etc.]

What's Not:
[Pain points, bottlenecks, what's costing them time or money]

What They Want:
[Their stated goal — more clients, better candidates, faster placements, less manual work, etc.]

How We Can Help:
[Which service fits — OutboundOS, SourcingOS, ContentOS, or combination — and why, based on the above]
```

Output this block first. Then proceed to the proposal sections below.

If anything is unclear from the transcript, leave the field blank and note "— not mentioned on call" so it's visible.

---

## Output Format — HTML Proposal (ALWAYS use this)

Every proposal is built as a standalone HTML file. Never use Canva, Google Slides, or any other tool.

**Why HTML:**
- Fully programmatic — can create, edit, duplicate with zero manual steps
- Design-heavy dark theme matching RecruiterGTM brand exactly
- Screenshare-ready for Tella videos (fullscreen Chrome, arrow key navigation)
- Export to PDF via Chrome print (no margins, background graphics on)
- One master template → swap client content per proposal

**File naming:** `/tmp/[client-slug]-proposal.html` (e.g. `arvi-proposal.html`, `justin-proposal.html`)

**Master template location:** `/Users/reyhankhan/Library/CloudStorage/GoogleDrive-reyhan@recruitergtm.com/My Drive/EA Demo/references/examples/proposal-template.html`

Always copy the master template, then fill in client content. Never build from scratch.

---

## Build Templates

### Sentinel-based section replacement (the orphan-bug fix per M2)

Master template marks every replaceable section with HTML comment sentinels:

```html
<!-- ── PROBLEMS_START ── -->
<div class="section">
  <p class="label">Where You Are Right Now</p>
  <h2 class="section-title">{{PROBLEMS_TITLE}}</h2>
  <div class="problems-grid">
    {{PROBLEMS_CARDS}}
  </div>
</div>
<!-- ── PROBLEMS_END ── -->
```

Build script replaces between sentinels (flat strings, not nested regex):

```python
def replace_section(html, marker, new_block):
    start = f"<!-- ── {marker}_START ── -->"
    end = f"<!-- ── {marker}_END ── -->"
    s_idx = html.index(start) + len(start)
    e_idx = html.index(end)
    return html[:s_idx] + "\n" + new_block + "\n" + html[e_idx:]
```

### Pre-ship grep sweeps

```bash
# Team names (banned everywhere per H1)
grep -E "Salar|Daniyal|Shmookh" proposal.html

# Managed-pilot stats on community-only (banned per E6)
grep -E "\$550k|8yrs|50\+ Agencies" community-proposal.html

# Mike Buontempo on community (banned per E7)
grep -E "Mike Buontempo" community-proposal.html

# Booked-calls language (banned per H5)
grep -Ei "booked calls" proposal.html

# Tool names outside tech stack (banned per H2)
grep -E "Lemlist|Instantly|HeyReach|HyperTide|Apollo|Apify|Clay|Pin\.com|Prospeo|n8n|Stardex|Spott" proposal.html | grep -v "tech-pill\|tech-name\|alt=\""

# Orphan signatures from old templates
ORPHAN_SIGNATURES=(
  "Feast-or-Famine Cycle"
  "Connection Limit Ceiling"
  "No Internal TA Team"
  "Dedicated BD Infrastructure"
  "No-TA Target Outreach"
)
for sig in "${ORPHAN_SIGNATURES[@]}"; do
  if grep -q "$sig" "$OUTPUT_FILE"; then
    echo "Orphan candidate: $sig — verify against client context"
  fi
done
```

Plus a structural balance check on every replaced section:

```python
opens  = len(re.findall(r'<div\b', section))
closes = len(re.findall(r'</div>', section))
assert opens == closes, f"div imbalance in {marker}: {opens} opens vs {closes} closes"
```

Any hit on the greps or imbalance = build failed; fix before opening for Reyhan.

### Tool-name substitution patterns (per H2)

- `Email + LinkedIn Multichannel Outreach Setup (Lemlist)` → `Email + LinkedIn Multichannel Outreach Setup`
- `Apify pulls daily new job postings` → `Daily monitoring pulls new job postings`
- `n8n workflows wired` → `Workflow automations wired`
- TAM label `Apollo + Apify · April 2026` → `Refreshed April 2026`

### Community stats grid (per E6)

```
50    OutboundOS Engines Deployed
200+  Use Cases Built
25    Claude Ops Managers Deployed
68    Recruitment Businesses Supported Annually
```

### Community testimonials markup source

Pull verbatim from `~/Desktop/proposals/abby-langstaff-proposal.html` lines ~1216-1254. CSS classes already exist in every cloned template: `testi-two-col`, `testi-img`, `testi-label`, `testi-video`, `testimonial-full`, `proof-stack`, `proof-caption`, `proof-img`.

- Section 1 (LinkedIn rec + Patrick): use Abby's first `<img class="testimonial-full">`, plus Patrick video `https://www.tella.tv/video/recruiter-gtm-testimonial-9szz/embed`
- Section 2 (Julia offshore): photo + video `https://www.tella.tv/video/julia-arpag-c9sk/embed`
- Section 3 (Multichannel proof): `proof-stack` with Instantly + HeyReach screenshots

### Managed pilot section — 6 required blocks (per G1)

1. Pilot deliverables — full 7 axe bullets from G3, plus per-call extras (Newsletter Nurture, DB Re-Engagement, Live Job Postings, ATS Setup) when discussed on call.
2. 4-week sprint — concrete actions per week (kickoff/ICP; tables/copy/playbook config; sequences live/Slack/first reporting call; full ops/optimisation begins/baseline).
3. 3-month roadmap — M1 Foundation, M2 Optimise + Split Test, M3 Validate + Scale.
4. Tech stack — actual tools with logos + client's CRM/ATS, same format as main tech stack.
5. Conversation benchmarks — only approved numbers from H6, framed as "Based on what our current clients are seeing".
6. Pricing line — "$2,500/month for 3 months. Auto-renews into 6-month managed service at the same rate. 14 days written notice to discontinue before pilot ends."

Section stands alone — a reader who skipped to it must understand the complete scope. Do NOT carry the 21-day onboarding into this section.

### Blocker line HTML (per I2)

```html
<span class="dim">Your biggest blocker is not</span>
<span class="bright"> effort.</span>
<span class="dim"> It&apos;s</span>
<span class="grad"> the absence of an engine.</span>
```

### Reference proposals for cloning

- Master template: `references/examples/proposal-template.html`
- Community-only canonical: `~/Desktop/proposals/daniel-edgar-proposal.html` (or `adeel-nadeem-proposal.html` / `brian-bennett-proposal.html`)
- Multi-service canonical: `~/Desktop/proposals/justin-daleo-proposal.html`
- Offshore talent canonical: `projects/jeffrey-lord-proposal.html`

---

**Slides structure (12 slides):**
1. Cover — client name, prepared by Reyhan, date
2. Who Am I — fixed stats ($550k Q1 2026, 200+ use cases, 8yrs, 50+ agencies)
3. Problems — 3 client-specific problems
4. Biggest Blocker — single centred statement
5. Solutions — 3 solutions mirroring problems
6. System Detail — OutboundOS/SourcingOS/ContentOS deliverables
7. Playbooks — 3 intent trigger playbooks
8. Timeline — 4-week ramp up
9. Tech Stack — Clay, Lemlist, Claude, HeyReach, n8n + client's CRM (with logos)
10. Option 1 — 3-Month Managed Pilot ($2,500/month)
11. Option 2 — RecruiterGTM Community (from $1,497)
12. Closing — CTA + start date

**TAM Slide (insert after Playbooks, before Timeline):**
- Build Clay TAM table for client's ICP (use `mcp__claude_ai_Clay__find-and-enrich-company`)
- Build Open Jobs table (contacts at those companies or open roles)
- Take screenshot via `/browser-use` skill
- Embed screenshot in HTML as a dedicated slide showing "We already mapped your market."
- Include Conversation Potential Calculator below screenshots

**Sample dataset templates per service section** (rules in J3/J4/J7 and K2/K3):

- **OutboundOS** — TAM pills + Company table (Company | HQ | Employees | Open Roles | Signal) with clickable LinkedIn "View →" + Open Jobs table (Company | Role | Location | Posted | Signal).
- **SourcingOS** — Candidate TAM pills + Candidate table with names, titles, companies, clickable PERSONAL LinkedIn "View →".
- **ContentOS** — 2 ContentOS proof screenshots base64-embedded from `references/testimonials/ContentOS sample 1.png` and `ContentOS sample2.png` + 4 tailored content theme/angle cards.

Profile link format:
```html
<a href="https://www.linkedin.com/in/name/" target="_blank" style="color:#8A00FF;text-decoration:none;">View →</a>
```

Dataset source line: `Dataset compiled from Apollo, Clay & Apify`.

---

## What This Skill Outputs

**Part 0 — Call Brief**
Structured summary of the call: Business Context, Niche, Location, Tech Stack, What's Good, What's Not, What They Want, How We Can Help. Always output first.

**Part 1 — HTML Proposal (12 slides)**
- Cover
- Who Am I (fixed)
- 3 Problems
- Biggest Blocker Line
- 3 Solutions
- System detail (which OS was selected)
- 3 Playbooks
- TAM + Open Jobs slide (Clay data + screenshots)
- 4-week Ramp Up Timeline
- Tech Stack (with logos)
- Option 1 — 3-Month Managed Pilot
- Option 2 — RecruiterGTM Community
- Closing

**Part 2 — Tella Video Script**
- Personalised intro (client name, their situation, what this deck covers)
- Which templated clip(s) to insert (OutboundOS / SourcingOS / ContentOS)
- Personalised outro (what happens next, CTA)

---

## Voice Tone (in addition to H1-H9 in Locked Rules)

- Practitioner naming what they see. Not a consultant diagnosing a case study.
- Problems = things the client already knows but hasn't said out loud.
- Solutions = a clear plan from someone who has done this before.
- Sentence style: short, direct, one idea per sentence. If a sentence has more than one clause, split it.
- Plain English test: read each sentence out loud. If it sounds like a brochure, rewrite it.

---

## SECTION 1 — Three Problems

Each problem gets:
- A named label (capitalised, punchy — e.g. "The Contingent Gambler Trap")
- 2–3 sentences of diagnosis using the client's exact language from the call
- Grounded in specifics from their business — markets they serve, how they currently operate, what's missing

**Canva formatting note (manual step):** On the Problems and Solutions slides, the label before the colon (e.g. "Feast-or-Famine Cycle:") must be **bold** and the description after the colon is regular weight. The Canva MCP cannot apply partial bold within a text element — Reyhan must manually select each label in Canva and press Cmd+B after the slide content is saved.

Tone: clinical, not judgemental. You're naming their reality, not shaming them.

**Do NOT mention tool names** (no Clay, HeyReach, Lemlist, etc.). Problems are about the business situation, not the tech.

Format:
```
[Problem Name]
[2–4 sentences of diagnosis]

[Problem Name]
[2–4 sentences of diagnosis]

[Problem Name]
[2–4 sentences of diagnosis]
```

---

## SECTION 2 — Biggest Blocker Line

One sentence. Goes between Problems and Solutions.

Formula: "Your biggest blocker is not [effort/tools/people]. It's [the real root cause]."

This line must be punchy, specific to their situation, and stop them in their tracks.

Default preferred line (use unless a more specific version fits perfectly): **"Your biggest blocker is not effort. It's the absence of an engine."**

Examples:
- "Your biggest blocker is not effort. It's the absence of an engine."
- "Your biggest blocker is not your offer. It's that nobody outside your network has ever seen it."

**Canva formatting note:** The blocker line on slide 9 must be:
- **Centred** on the slide (text alignment: center)
- **No bullet point** — it is a standalone statement, not a list item
- Applied via `format_text` with `text_align: "center"` after `replace_text`
- "Your biggest blocker is not your team. It's the system they're being asked to run."

---

## SECTION 3 — Three Solutions

Each solution directly mirrors a problem (same order).

Format:
- Named solution (capitalised)
- 2–3 sentences: what we build, what changes for them

Tone: outcome-focused. What changes for the client, not how the tech works.

**Do NOT mention tool names.** The tech stack slide covers that separately.

Format:
```
[Solution Name]
[2–3 sentences]

[Solution Name]
[2–3 sentences]

[Solution Name]
[2–3 sentences]
```

---

## SECTION 4 — System Detail (Which OS)

Based on the call, identify the primary service(s) being proposed. Pull the relevant deliverables from the reference below.

**OutboundOS — select when:** BD is broken, inconsistent, or non-existent. Client needs more clients.
**SourcingOS — select when:** Placement pipeline is thin, sourcing is manual or starts from scratch per role. Client needs better candidates.
**ContentOS — select when:** Client has no LinkedIn presence, posting inconsistently, or authority is not building.

For each selected OS, list the 4 key deliverables (checkbox format for Canva slide):
- Client ICP Market Map
- [X] Custom Intent Playbooks
- Email + LinkedIn Outreach Setup
- Reporting & Lead Notifications in Slack

If multiple OS services are proposed, create one detail block per service.

---

## SECTION 5 — Clay Playbook + Market Map Screenshots + ROI Calculator

This is a 2-slide block in the proposal. Slide 1 = screenshot of the Clay tables we built for them. Slide 2 = ROI calculator with actual numbers from those tables.

The goal: make the opportunity feel real and specific before they sign. This is not a mockup — it's live data from their actual market.

---

### Step 1 — Build the Clay Playbook

For every client, create a Clay playbook with 2 tabs:

**Tab 1 — Market Map (Companies)**
Use `mcp__claude_ai_Clay__find-and-enrich-company` to search for companies matching their ICP:
- Industry / niche (from call transcript)
- Headcount range (from call — typical: 10–200 for recruitment clients)
- Region / market
- Hiring signal: active job postings where possible

Target: 200–500 companies in the initial pull. This is their total addressable market.

**Tab 2 — Jobs or People (depends on service recommended)**

For OutboundOS (client-side):
- Use `mcp__claude_ai_Clay__find-and-enrich-contacts-at-company` on the companies from Tab 1
- Filter for: Founder, MD, Head of Talent, Operations Director — whoever hires at those companies
- These become the outreach targets

For SourcingOS (candidate-side):
- Use `mcp__claude_ai_Clay__find-and-enrich-list-of-contacts` to find candidates matching their ideal profile
- Filter for: job title(s) they recruit for, seniority level, region, tenure signals where available
- These become the sourcing targets

For ContentOS:
- Use Tab 2 to pull key ICP decision-makers active on LinkedIn
- This shows the audience size they can reach with consistent content

---

### Step 2 — Screenshot the Clay Tables

After the tables are populated, use the `/browser-use` skill to:
1. Navigate to the Clay workspace
2. Open Tab 1 (Market Map) — screenshot the table with column headers and first 10–15 rows visible
3. Open Tab 2 (Jobs/People) — screenshot the table with column headers and first 10–15 rows visible
4. Save both screenshots locally (e.g. `/tmp/clay_market_map.png`, `/tmp/clay_contacts.png`)

Screenshots should show enough rows to prove the data is real but not so many it looks like noise. Aim for a clean, readable table that a non-technical person can immediately understand.

---

### Step 3 — Upload Screenshots to Canva

Use the Canva MCP to upload both screenshots and insert them into the proposal:
1. `mcp__claude_ai_Canva__upload-asset-from-url` — upload from local file path or use the file asset
2. `mcp__claude_ai_Canva__perform-editing-operations` — insert into the correct slide in the proposal deck

The slide layout: two screenshots side by side (Tab 1 left, Tab 2 right), with a header above: "We already mapped your market."

---

### Step 4 — Conversation Potential Calculator (same slide or slide below)

Use the actual counts returned from Clay to show the potential. Do NOT promise meetings, placements, or revenue. The calculator shows conversations only. Frame as: "Based on what our current clients are seeing."

**For OutboundOS:**
```
[X] decision-makers identified in your market
→ [Y] contacted per month at our standard send volume
→ 5–10 quality decision-maker conversations per month
```

**For SourcingOS:**
```
[X] candidates identified for your evergreen roles
→ [Y] contacted per month across email + LinkedIn
→ 30–50 quality candidate conversations per month
```

**For ContentOS:**
```
[X] ICP decision-makers active on LinkedIn in your niche
→ 3 posts per week, social listening active
→ 50,000–100,000 impressions per month
→ 25,000 new people reached every month
```

For combined services: stack all three.

**Benchmarks (real numbers from active clients — never fabricate):**
- OutboundOS: 5–10 quality decision-maker conversations/month
- SourcingOS: 30–50 quality candidate conversations/month (across 4 evergreen roles)
- ContentOS: 50k–100k impressions/month · 25k new people reached/month

**Never promise:** meetings booked, placements made, revenue generated, or response rates. The output is conversations. The client closes them.

**Slide copy:**

Header: "What this looks like in practice"
Subheader: "Based on what our current clients are seeing."

| System | What runs | What you can expect |
|--------|-----------|---------------------|
| OutboundOS | Email + LinkedIn outreach to [X] decision-makers | 5–10 quality client conversations/month |
| SourcingOS | Outreach to [X] candidates across 4 roles | 30–50 quality candidate conversations/month |
| ContentOS | 3 posts/week + social listening | 50k–100k impressions · 25k new people reached/month |

Footer: "These are real numbers from active clients. Not projections."

---

**Important:** The Clay data makes the market feel real and large. The conversation benchmarks make the investment feel justified. Never overstate.

---

## SECTION 6 — Timeline (3-Month Roadmap)

Always show BOTH the 4-week setup sprint AND the 3-month monthly breakdown. The header should read "From setup to scale inside 90 days." not "4-Week Ramp Up".

**4-Week Sprint (setup phase):**

**Week 1 — Discovery & Setup**
ICP mapping session. Target market defined. Infrastructure connected.

**Week 2 — Build**
Engine built. Copy drafted. Client reviews and approves playbooks.

**Week 3 — Launch**
Sequences go live. Early data reviewed. Messaging refined based on first replies.

**Week 4 — Full Operation**
Engine running daily. Reporting live. Optimisation begins.

**Monthly Breakdown (always include below the 4-week track):**

**Month 1 — Research, Build & First Launch**
ICP defined. Market mapped. Technical infrastructure connected. Copy written and approved. First sequences launched by end of week 4.

**Month 2 — Optimisation & Split Testing**
Reply data reviewed. Subject lines, opening hooks, and call-to-action variants tested. Second launch with refined copy and proven signals.

**Month 3 — Validation & Scaling**
Non-performing angles cut. Winning playbooks scaled. Volume increased on what is converting. Engine ready to extend into a 6-month managed service.

If client mentioned a hard deadline, reference it explicitly in Month 3.
If client is on managed retainer (Reyhan's team runs it), adjust Week 3–4 and Month 2–3 language — they don't operate it themselves.

Keep each week/month to 2–3 sentences max.

---

## Investment Options — pricing reference

Rules in Locked Rules section C. Pricing table (managed pilot Option 1):

| Service mix | $/month |
|---|---|
| OutboundOS managed pilot (3 months) | $2,500 |
| SourcingOS managed pilot (3 months) | $2,500 |
| ContentOS managed pilot (3 months) | $2,500 |
| Combined (Outbound+Content or Sourcing+Content) | $4,000 |
| Full engine (all 3) | $5,500 |

Minimum is $2,500/month. Never go below regardless of scope. Always note "Option to extend to 6 months after the pilot."

Option 2 = RecruiterGTM Community $1,497 one-time. Premium $4,497 tier is dead (C3).

---

## SECTION 7 — Testimonials to Feature

Pick 2–3 from the bank below based on the client's niche and situation. Surface them on the social proof slide.

- **Michael Alexander (Outreach AI)** — GTM Engineer running ops for 18 clients. Best for: anyone asking about the operator/GTM Engineer model.
- **Shana Marr** — Full offshore team, bought back 50% of her time. Best for: agency owners overwhelmed with ops.
- **Julia Arpag** — SA Ops Manager leading a team of 3, back-to-back million dollar years. Best for: clients focused on growth and team-building.
- **Mike Buontempo** — Use when niche is relevant to recruitment/agency sector.
- **Spencer Knibbe** — Use for outbound BD focus.
- **Daniel Boyle** — Use for systems/automation focus.
- **Patrick Schildmann** — Use for European market clients.

Output: "Feature testimonials from: [Name 1], [Name 2], [Name 3] — reason for each."

---

## Part 2 — Tella Video Script

Output a short video walkthrough script. Structure:

**[INTRO — Personalised, ~30 seconds]**
Start with the client's name and one sentence that shows you listened on the call.
Reference the 1–2 biggest things they said they're struggling with.
Tell them what the video covers.

Example:
"Hey [Name], really enjoyed our call earlier this week. You mentioned [pain point from transcript]. This video walks you through exactly what we'd build for [Company Name] — the system, the timeline, and what it would look like in practice."

**[MAIN — Insert Templated Clip]**
Tell the client which pre-recorded clip to watch here.
"[Insert OutboundOS system walkthrough clip]" or "Insert SourcingOS overview" etc.

If multiple services: list the clip order.

**[OUTRO — Personalised, ~20 seconds]**
Reference Option 1 pricing and the pilot structure.
Tell them what to do next.

Example:
"Based on what you told me, Option 1 is a 3-month managed pilot at $[X]/month — we run everything. You review, approve, and stay focused on delivery. At the end of 3 months, you decide if you want to extend. Drop me a message or book a call from the link below and we'll get started."

---

## Output Format

Output all sections in order, clearly labelled. No preamble — just the copy, ready to use.

```
--- PROBLEMS ---
[content]

--- BIGGEST BLOCKER LINE ---
[one sentence]

--- SOLUTIONS ---
[content]

--- SYSTEM DETAIL ---
[content]

--- 4-WEEK TIMELINE ---
[content]

--- INVESTMENT OPTIONS ---
[content]

--- TESTIMONIALS TO FEATURE ---
[names + reason]

--- TELLA VIDEO SCRIPT ---
[intro / clip instruction / outro]
```

---

## Fixed Slide Reference (Do Not Rewrite These)

For context — these are the fixed slides in the Canva template:

1. Cover — client name + company logo
2. Who Am I — $550k Q1 2026, 200+ use cases, 8 years experience (fixed)
3. Social Proof — testimonial slides (select 2–3 from bank above)
4. **PROBLEMS** ← custom
5. Biggest Blocker Statement ← custom (one-liner slide)
6. **SOLUTIONS** ← custom
7. System title slide (OutboundOS / SourcingOS / ContentOS logo) — fixed branding
8. **SYSTEM DETAIL** ← custom (which deliverables apply)
9. Playbook detail slides — fixed template, Reyhan fills manually
10. **CLAY PLAYBOOK SCREENSHOTS** ← custom (Tab 1: market map, Tab 2: jobs/people — built live in Clay, screenshotted via browser-use, uploaded via Canva MCP)
11. **ROI CALCULATOR** ← custom (actual numbers from Clay, shows client + candidate conversations potential)
11. **4-WEEK TIMELINE** ← custom
12. Tech Stack — Clay, Lemlist/Instantly, HeyReach, n8n, OpenAI, ATS (fixed)
13. **INVESTMENT OPTIONS** ← custom
14. Closing slide — fixed

---

## Example Output (Charles Eboigde — Guidewell)

**Problems:**

The Contingent Gambler Trap
Relying on contingent roles without exclusivity creates zero predictability. Without a committed retainer model, the team may be spending recruiter time on roles that never close.

Fragmented Sales Infrastructure
There is no unified outbound engine to fuel aggressive BD. Without one, the team cannot hit consistent volume in the Dutch market.

Passive Market Reliance
Depending on LinkedIn Recruiter and job boards creates a post-and-pray mentality. Hitting the 25–200 employee sweet spot requires a proactive system that contacts prospects consistently.

**Biggest Blocker Line:**
Your biggest blocker is not effort. It's the absence of an engine.

**Solutions:**

The Retained-Only Outbound Engine
We build a multichannel outbound system designed specifically to pitch retained and exclusive searches. This shifts focus from volume hiring to high-margin commitments with full pipeline predictability.

Aggressive Volume Automation
We deploy an outbound engine that hits the Dutch market with relentless consistency. Volume at scale — but every touchpoint feels personalised.

Localised Dutch Market Playbooks
We tailor the outbound narrative to the Dutch market while maintaining the send volume that gets results.

---

## GTM ACADEMY — OFFSHORE TALENT PLACEMENT PROPOSALS

This is a completely different proposal type from OutboundOS/SourcingOS managed services. Use when placing offshore talent (GTM Engineers, Ops Coordinators, Ops Integrators, Junior Recruiters, Admin Assistants) into a client's team.

**Full format documented in memory:** `reference_offshore_talent_proposal.md`

**Key rules:**
- Hero = outcome-focused ("20+ hours back every week"), never mention payment
- Stats = GTM Academy metrics only (200+ placed, $35k/yr savings, 1.5yr retention) — NOT OutboundOS stats
- "Built solely for Small Business Owners" (non-recruiter clients) or "Recruitment Agencies" (recruiter clients)
- Testimonials = Tyler Mounce, Michael Alexander, Shana Marr (Tella videos) + Mike Buontempo + Julia Arpag. Remove Patrick.
- NO campaign proof screenshots (Instantly/HeyReach) — client doesn't need outbound proof
- Sample candidates = real profiles with Loom video embeds (Sarmad, Shmookh, Shafaq)
- Tech stack → "Tools our resources are trained on" with tool names per category (CRM: HubSpot/Attio/GHL, PM: Asana/ClickUp/Monday, AI: Claude/OpenAI, Outbound Systems, Notetaking, Dashboarding, Soft Skills)
- Pricing = single card, flat one-time fee ($4,500), 60-day guarantee, 6mo support, 3 ramp-up calls, AI training access
- Reference build: `projects/jeffrey-lord-proposal.html`

---

## URL & data verification

Rule in M6. Procedure:

1. Extract every LinkedIn URL from the HTML.
2. HTTP-verify each (200 = valid, 999 = LinkedIn rate-limit flag for manual check, anything else = broken).
3. Replace broken rows with verified-URL companies/candidates. Re-run until broken count = 0.
4. Also sanity-check: employee counts realistic (BAE Systems is not 201-500), locations match client's actual market, no placeholder names, CSV column alignment if exporting to Lemlist.
5. Output a verification summary: total URLs, valid, broken.

Applies to every table with LinkedIn links: OutboundOS company TAM, SourcingOS candidate tables, Employer Brand / HR Director tables, anything else.
