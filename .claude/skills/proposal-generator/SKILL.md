# Proposal Generator Skill

Generate a complete, client-specific RecruiterGTM proposal — slide content + Tella video script — from a Fireflies transcript and/or LinkedIn profile.

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

**CRITICAL — Candidate/Company Profile Tables Must Have Clickable LinkedIn Links:**
- Every candidate or company profile shown in the proposal MUST include a "Profile" column with a clickable "View →" link to their LinkedIn profile
- Use Clay MCP to source profiles — it returns real LinkedIn URLs (e.g. `https://www.linkedin.com/in/name/`)
- Link format: `<a href="https://www.linkedin.com/in/name/" target="_blank" style="color:#8A00FF;text-decoration:none;">View →</a>`
- NEVER use placeholder names or generic profiles without LinkedIn links
- Dataset source line must credit all data sources used: "Dataset compiled from Apollo, Clay & Apify"

**CRITICAL — Sample Dataset Consistency Rules (apply to every proposal):**
Every proposal pitching a managed service MUST include these sample datasets in the relevant service section:

1. **OutboundOS section** must include:
   - TAM pills (total companies, contacted/month at 1/3 TAM, approx DM conversations)
   - Company table: real companies from Apollo with 2+ open jobs. Columns: Company | HQ | Employees | Open Roles | Signal. With clickable LinkedIn "View →" links.
   - Open Jobs table: live job postings from those companies. Columns: Company | Role | Location | Posted | Signal.

2. **SourcingOS section** must include:
   - Candidate TAM pills (total reachable candidates from Apollo, contacted/month at 1/3 TAM, 30-50 candidate conversations benchmark)
   - Candidate table: real candidates from Clay with full names, titles, companies, and clickable LinkedIn "View →" links.

3. **ContentOS section** must include:
   - The 2 ContentOS proof screenshots — ALWAYS. These are the REAL image files at `references/testimonials/ContentOS sample 1.png` and `references/testimonials/ContentOS sample2.png`. Read them, base64-encode them, and embed as `<img src="data:image/png;base64,...">` side by side in a grid. NEVER use fake stat cards or made-up numbers as a substitute. The screenshots are the proof.
   - 4 tailored content theme/angle cards for the client's audience
   - Content angles only. NO newsletter in ContentOS — newsletter always goes in OutboundOS.

**Newsletter Placement Rule:** Newsletter setup + subscriber capture is ALWAYS an OutboundOS deliverable, NOT a ContentOS deliverable. ContentOS = LinkedIn posts + social listening + Claude setup + content themes.

These datasets and proof screenshots prove the market is real. Without them the proposal is just claims.

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

## Voice Rules (Apply to ALL Custom Sections)

Copy in this proposal must sound like Reyhan wrote it — not a consultant, not an agency. Non-negotiable.

**Sentence style:**
- Short, direct sentences. One idea per sentence.
- No long compound sentences chained together.
- If a sentence has more than one clause, split it.

**Banned words and phrases** (never use these):
- tooling, noise, landscape, leverage, transformative, visibility, precision, invaluable
- "breaks through", "amplifies", "streamlines", "optimises", "unlocks potential"
- Any figurative language or idioms (e.g. "weight in the market", "move the needle", "stalls")
- Corporate transitions: "This ensures that...", "As a result...", "In order to..."

**Em dashes:**
- Maximum 1 per entire output. Zero is better.

**Tone:**
- Write like a practitioner naming what they see. Not a consultant diagnosing a case study.
- Problems should feel like things the client already knows but hasn't said out loud.
- Solutions should feel like a clear plan from someone who has done this before.
- Confident, not salesy. Specific, not vague.

**Plain English test:**
- Read each sentence out loud. If it sounds like a brochure, rewrite it.
- If a word has a simpler alternative, use the simpler one.

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

## SECTION 6 — Investment Options

Always 2 options. New pricing structure below.

**Option 1: 3-Month Managed Pilot**
- Full [OutboundOS / SourcingOS / ContentOS] setup — done for you
- Dedicated account operator running the engine daily
- Weekly performance report delivered automatically
- Interested leads/candidates notified instantly via Slack
- Monthly strategy review with Reyhan
- Option to extend to 6 months after the pilot
- Price: [set based on service scope — see pricing reference below]

**Option 2: RecruiterGTM Community**
- Self-implement with full training and templates
- 12 months access to OutboundOS, RecruiterOS, Content Flywheel modules
- Weekly group Q&A calls with Reyhan
- 1:1 Systems Roadmap call (60 min)
- 50% discount on future offshore hires
- Price: $1,497 (Standard) / $4,497 (Premium — includes 1 DFY system or placement)

**Pricing reference for Option 1:**
- OutboundOS managed pilot (3 months): $2,500/month
- SourcingOS managed pilot (3 months): $2,500/month
- ContentOS managed pilot (3 months): $2,500/month
- Combined (OutboundOS + ContentOS or SourcingOS + ContentOS): $4,000/month
- Full engine (all 3): $5,500/month

Minimum is $2,500/month. Never go below this regardless of scope.

Always note: "Option to extend to 6 months after the pilot."

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

## MANDATORY: URL VERIFICATION BEFORE DELIVERY

**This step is NON-NEGOTIABLE. Every proposal must pass this before being copied to Desktop or shown to Reyhan.**

1. Extract every LinkedIn URL from the HTML file
2. HTTP-verify each one (200 = valid, 999 = LinkedIn rate limit, flag for manual check, anything else = BROKEN)
3. Any broken URL must be fixed or the row must be replaced with a company/candidate that has a verified URL
4. Re-run verification after fixes until broken count = 0
5. Output a verification summary: total URLs, valid, broken

**If a single broken URL ships in a proposal, the entire proposal is considered defective.**

This applies to:
- Company TAM tables (OutboundOS)
- Candidate sample tables (SourcingOS)
- Employer Brand / HR Director tables (Giles-type proposals)
- Any other table with LinkedIn links

Also verify:
- Employee counts are realistic (BAE Systems is not 201-500)
- Company locations match the client's actual market (not UK for a US-based recruiter)
- No placeholder or fabricated company names
- CSV column alignment if exporting to Lemlist
