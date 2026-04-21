# Skill: 90-Day Roadmap Generator

Generate a personalized 90-Day Roadmap for every new RecruiterGTM community member after their 1-hour audit session with Reyhan.

## How to Invoke
`/roadmap-generator` followed by:
- Fireflies transcript or call notes from the audit session, OR
- Manually pasted discovery answers

## What This Skill Produces

### Output 1: Discovery Doc (Google Doc)
A structured audit summary filled from the call. Uses the standard 7-section template. This is the working document.

### Output 2: Polished 90-Day Roadmap (Google Doc)
A client-facing deliverable with branded sections, personalized pillars, specific milestones, and clear next steps. This is what gets sent to the client.

---

## The Process

### Step 1: Extract Discovery Data

From the transcript or notes, extract:

**Client Info**
- Full name
- Agency name
- Niche / industry
- Geography (where they recruit)
- Team size
- Business model (contingent, retained, RPO, subscription, hybrid)

**Discovery Answers**
- Biggest bottleneck slowing the business
- Which part of weekly workflow takes most time
- Lead flow predictability (1-10 scale)
- What makes next 30 days a massive win
- Primary focus area

**Systems Audit**
For each category, capture current tool + recommended action:
- ATS / CRM
- LinkedIn Automation
- Email Outbound
- Data / Enrichment
- Newsletter
- Workflow Automation
- Sourcing
- Other tools

**Tech Stack Decision Framework**

The recommendation depends on what the client already has, their volume needs, and their niche. Never force a tool change if their current tool works. The goal is the right stack for their situation, not a one-size-fits-all.

**ATS / CRM — Keep what they have**
- Recruiterflow, Loxo, Bullhorn, Zoho Recruit, Vincere — all fine
- Only flag if they have NO ATS or are using spreadsheets
- If they're choosing between options: Recruiterflow for small teams, Bullhorn for scale

**Outreach Stack — Two approved configurations**

Config A: Lemlist Only (Default)
- Best for: Most clients. Multichannel (email + LinkedIn) in one tool.
- When to use: Client has no existing outreach tool, or is on Dripify/single-channel tools
- Migrate FROM: Dripify, standalone email tools
- Example: Julie Conti (was on Dripify + Instantly separately → consolidated to Lemlist)

Config B: HeyReach + Instantly (High Volume)
- Best for: Clients sending more than 300 emails per day who need separate LinkedIn automation
- When to use: Only when the client needs 300+ daily email volume. Below that, Lemlist handles everything.
- Example: Jay Veniard (kept HeyReach + Instantly, dropped Lemlist — volume needs exceeded Lemlist's capacity)

HARD RULE: Never recommend HeyReach + Lemlist together. They overlap on LinkedIn.

**Data / Enrichment — Assess per client**
- Clay: Best for complex enrichment workflows, multi-step data pipelines, clients who want to learn the tool
- Deepline / Claude Code: Best for clients who want AI-native data sourcing without learning Clay's UI
- Apollo: Contact data enrichment (emails, phones, company data). Works alongside Clay or standalone.
- Prospeo: Fallback email finder from LinkedIn URLs when Apollo doesn't have the data
- SalesQL: Quick LinkedIn email/phone extraction. Good for clients already using it.

No fixed default. Assess per client based on their niche, technical comfort, and whether they want to learn Clay or just get results.

**Sourcing Tools**
- LinkedIn Sales Navigator: Almost always keep. Primary sourcing tool for most recruiters.
- LinkedIn Recruiter: Keep if they have it. Expensive but powerful for candidate sourcing.
- Pin.com: Recommend for candidate sourcing. Good alternative/complement to Sales Nav.
- Apify: For job board scraping (Indeed, StepStone, Xing) and LinkedIn profile research. Mostly used in managed service, not self-serve.
- ContactOut / SignalHire: Keep if they have it for phone numbers. Don't add if they already have Apollo.

**Newsletter**
- Beehiiv: Always recommend if they have no newsletter. Best for recruitment newsletters.
- If they're already on Mailchimp/ConvertKit, migration to Beehiiv is optional — focus on actually launching the newsletter first.

**Workflow Automation**
- n8n: Preferred. Self-hosted, cheaper than Zapier at scale, supports AI agents.
- Zapier/Make: Keep if they're already using it and it works. Only suggest n8n migration if they're hitting cost limits or need AI agent capability.

**AI**
- Claude Code + Claude Pro ($20/mo): Always recommend for AI-native workflows.
- ChatGPT: If they're using it casually, fine. But position Claude Code as the upgrade for connected, tool-integrated AI.
- Claude Pro ($20/mo): Minimum recommendation for any client wanting to use AI seriously.

**Real Client Tool Decisions (for reference)**

| Client | Kept | Dropped | Added | Reasoning |
|--------|------|---------|-------|-----------|
| Jay Veniard | Clay, Instantly, HeyReach, Sales Nav, n8n | Lemlist, Bullhorn, Zapier | Beehiiv, Claude Code | Volume play — wanted separate LinkedIn + email tools |
| Julie Conti | Recruiterflow, Sales Nav, Zapier | Dripify, Instantly (separate) | Lemlist, Beehiiv, Claude Code | Consolidated to multichannel |
| Kylie Larwood | Loxo, Sales Nav, SalesQL, Dripify (till July) | — | Lemlist (after July), Pin.com, Claude Code | Waited for Dripify contract to end |
| Oliver Zauritz | Lemlist, Clay, Apollo, Sales Nav | — | Apify, Inboxology | German market, job board scraping needed |

### Step 2: Build the 4 Pillars

Every roadmap has 4 pillars. The content is personalized based on the audit.

---

#### PILLAR 1: OFFER UNIQUENESS

**Goal:** 2 primary offers + 1 secondary offer with clear pricing

Capture:
- Current offer structure (contingent, retained, subscription, RPO, etc.)
- Problems with current model (predictability, exclusivity, pricing power)
- New offer to consider adding
- Secondary offer opportunity

**Standard 90-Day Outcome:**
Prepare a clear offer structure with pitch materials. If they're contingent-only, explore exclusive or subscription (RAAS) model. If they have a niche, productize it.

**Common patterns from real clients:**
- Julie Conti: Contingent + RAAS subscription → prepare SourcingOS pitch to convert client to RAAS
- Kylie Larwood: Mostly retained → push for exclusive-only + explore fractional/RPO
- Oliver Zauritz: Contingent property management → transition to "Talent Partner" positioning

---

#### PILLAR 2: MULTICHANNEL OUTBOUND

**Goal:** 2-3 playbooks running on autopilot generating conversations

Capture:
- ICP (industry, revenue range, employee count, geography)
- Excluded companies/segments
- Buying triggers (open jobs, leadership changes, no internal TA, contract wins, growth signals)

**Standard Playbooks** (pick 2-3 based on their niche):
1. **Live Jobs / Open Roles** — Companies with open jobs in their niche on LinkedIn/Indeed/StepStone
2. **Leadership Changes** — 90-day job changes at target companies (new VP, new CHRO)
3. **No Internal TA** — Companies without a dedicated recruiter/TA team
4. **Growth Signals** — Companies that raised funding, won contracts, expanding offices
5. **MPC Campaign** — Most Placable Candidate outreach to target companies

**Success Metric:** Vary based on team size and niche:
- Solo operator: 3-5 conversations/month
- Small team (2-4): 5-10 conversations/month
- Larger team (5+): 10-15 conversations/month

**Standard 90-Day Outcome:**
Generate 1 meeting from each playbook running. Full autopilot by Day 90.

**The Stack** (always mention):
- Clay: Signal-led sourcing and enrichment
- Lemlist: Multichannel outreach (email + LinkedIn)
- Apollo/SalesQL: Contact data
- Apify: Job board scraping

---

#### PILLAR 3: LINKEDIN CONTENT

**Goal:** 30 posts in 90 days, establish positioning, warmer outbound

Capture:
- Positioning statement (what they want to be known for)
- Content themes (placements, journey, niche insights, AI in recruiting)
- Who creates content (founder, assistant, AI-assisted)

**Standard 90-Day Outcome:**
Publish 30 LinkedIn posts, 5 videos, 10 image posts and 15 text posts.
Try the Recruiter Content Flywheel framework from RecruiterGTM.

**Always recommend:**
- Claude Code with LinkedIn Content Skill for drafting
- Content calendar aligned with outbound campaigns
- Repurpose: 1 long-form piece → 3-5 posts

---

#### PILLAR 4: ATS + NEWSLETTER

**Goal:** Clean ATS, newsletter capturing leads, nurture sequence live

Capture:
- Current ATS state (how many records, is it clean, are they using it properly)
- Newsletter status (none, LinkedIn-only, email newsletter)
- Newsletter promise (what value do subscribers get)

**Standard 90-Day Outcome:**
- ATS filtered list of at least 1,000 clients and 100 previous clients for nurture
- Launch 3 newsletter emails by Day 90
- Beehiiv setup with subscriber landing page

**Adjust the numbers based on their ATS size:**
- If they have 35,000 records (like Kylie): target 1,000 clients + 20 previous clients
- If they have 13,000 records (like Julie): target 1,000 clients + 100 previous clients
- If they have very few records: target 500 clients minimum

---

### Step 3: Build Milestones Table

Standard template — adjust specifics per client:

| Day | Pillar 1: Offer | Pillar 2: Outbound | Pillar 3: Content | Pillar 4: ATS |
|-----|-----------------|--------------------|--------------------|---------------|
| 30 | Offers finalized | 1st campaign live | 12 posts | ATS cleaned |
| 60 | Pitch deck ready | 2 playbooks running | 24 posts | Newsletter live |
| 90 | Tested 10+ prospects | Full autopilot | 30+ posts | 1st newsletter sent |

### Step 4: Define Primary Objective

One sentence summarizing what success looks like in 90 days. Extract this from:
- Their "massive win" answer
- Their biggest bottleneck
- Their lead flow predictability score

Examples:
- Oliver: "Transform from manual headhunting to a fully autonomous, signal-led outbound machine. Reclaim 20+ hours of founder time per week."
- Julie: "Fill 3 of 6 open roles and convert 1 client to RAAS subscription model."
- Kylie: "Generate 3 qualified conversations from cold outreach while running BD in the background without stopping fulfillment."

### Step 5: Next Steps

Standard next steps (always include):

| Action | Owner | Due |
|--------|-------|-----|
| Review roadmap and confirm alignment | Client | Day 3 |
| Access Skool course modules | Client | Day 3 |
| Book 30-min setup session with Daniyal on Skool | Client | Day 5 |
| Share tool logins (CRM, LinkedIn, email) | Client | Day 5 |
| Tech stack audit completed | RecruiterGTM | Day 7 |
| Signal-based outbound campaign launched | RecruiterGTM | Day 14 |
| LinkedIn content launch support | RecruiterGTM | Day 14 |
| MPC campaign n8n automation setup (with Daniyal) | RecruiterGTM | Day 21 |

**What RecruiterGTM delivers for community members:**
1. Tech stack audit
2. Assist with launching a signal-based outbound campaign
3. LinkedIn content launch support
4. MPC campaign n8n automation (with Daniyal)

Add client-specific next steps based on the audit.

### Step 6: Learning Path (Skool Course Recommendations)

Every roadmap includes a "Your Learning Path" slide recommending which Skool courses to watch and in what order. Tailor per client based on their pillars.

**4 Skool Classrooms available:**

1. **OutboundOS** (14 modules) — Foundations, Infrastructure, Market Mapping, ICP, Copywriting, Sequences, LinkedIn, Playbooks, Deliverability, Analytics, Dream100, Scaling, Advanced, Paths
2. **RecruiterOS** (5 modules) — Strategic Foundation (offer models, fractional, talent partner, DFY), AI Candidate Sourcing, Goldmine Database & Nurture, Authority & Scale, Transformation Delivery
3. **Recruiter Content Flywheel** (7 modules) — Authority Shift, Converting Posts to Deals, AI Content Stack, Full Growth System, Creator Studio, 90-Day Sprint Execution, Support Ecosystem
4. **Lean Ops Accelerator** (19 lessons) — AI Brain, Productivity Ops, Sales Ops, Marketing Ops, Team Ops, CEO Briefing, Client Onboarding, SOP Automation, Slack AI, Ops GPT, Dashboards, Offshore Team, Sourcing Offshore, QA, Client Comms, Research, Project Management, Fulfillment Engine. **Claude for Recruiters classroom is inside this section.**

**Mapping rules:**
- Pillar 1 (Offer) → RecruiterOS Module 1 (Strategic Foundation, L4-L9 for offer models)
- Pillar 2 (Outbound) → OutboundOS Module 1 (Foundations), Module 3 (Market Mapping), Module 5 (Copywriting)
- Pillar 3 (Content) → Recruiter Content Flywheel Module 1 (Authority Shift), Module 3 (AI Content Stack)
- Pillar 4 (ATS + Newsletter) → RecruiterOS Module 3 (Goldmine Database), Content Flywheel Module 6 (90-Day Sprint)
- AI/Claude → Always recommend: "Watch the tutorial at recruitergtm.com/claude-for-recruiters. It's inside the Lean Ops Accelerator classroom."

**Always recommend 4 cards in a 2x2 grid.** Pick the most relevant course first based on their primary bottleneck.

### Step 7: Get Started Slide (Always Last)

Every roadmap ends with a "Two Things to Do Right Now" slide:

**1. Join the Weekly Q&A**
- Every Wednesday, 4:30 - 5:30 PM Lisbon/UK time
- Google Meet: https://meet.google.com/xjc-zmxy-yap
- 3 calendar buttons: Google Calendar, Outlook, Download .ics
- All set to recurring weekly

**2. Track Your Progress**
- Link: https://docs.google.com/spreadsheets/d/1aZBd7FFYYoCpy_6YHvwkUi25DeEgm4te/edit?gid=352351256#gid=352351256
- Instruction: "File → Make a copy → Track your goals for the next 90 days"

**3. Book a 30-min Setup Session with Daniyal**
- For anything RecruiterGTM (tool setup, Skool access, tech questions), members book a 30-min session with Daniyal by reaching out to him directly on Skool.
- Always include this as part of the Get Started slide or Next Steps table.

**Footer:** "Questions? Message Reyhan or Daniyal directly on Skool."

---

## Output Format

### Discovery Doc

Create a Google Doc using the standard template structure (7 sections):
1. Client Info (table)
2. Discovery Questions (filled answers)
3. Systems Audit (tool table with current/action/notes)
4. The 4 Pillars (each with current state, gaps, 90-day outcome)
5. 90-Day Milestones (table)
6. Primary Objective
7. Next Steps

Save as: `[Client Name] - 90-Day Roadmap Discovery`
Location: Client's Google Drive folder

### Polished Roadmap (HTML — 12 slides)

Build as a standalone HTML file using the proposal-generator design system (dark theme, violet #8A00FF accents, DM Sans font, 1280x720 slides).

**12-slide structure:**
1. **Cover** — client name, agency, niche, geography, prepared by Reyhan, date
2. **Client Overview** — business/model/discovery scores cards + current stack as pills
3. **Primary Objective** — one bold sentence + supporting paragraph
4. **4 Pillars Overview** — 4-card grid with pillar numbers and one-liner each
5. **Pillar 1: Offer Uniqueness** — current state, 90-day target, milestones table
6. **Pillar 2: Multichannel Outbound** — ICP, buying triggers, success metric, 3 playbook cards
7. **Pillar 3: LinkedIn Content** — positioning, content themes, 90-day targets (30/15/10/5)
8. **Pillar 4: ATS + Newsletter** — ATS milestones + Beehiiv setup details
9. **Tech Stack** — full table with Current/Action/Notes columns (Keep green / Transition yellow / Add violet)
10. **Your Learning Path** — 4 Skool course recommendation cards (tailored per client, see Step 6)
11. **Milestones + Next Steps** — Day 30/60/90 table + action items with owners and due dates
12. **Get Started** — Weekly Q&A calendar buttons + Performance Tracker link (see Step 7)

**File naming:** `~/Desktop/proposals/[client-slug]-90day-roadmap.html`
**Export to PDF:** Chrome print → Save as PDF (no margins, background graphics on)

**Reference files (confirmed working roadmaps):**
- Kylie Larwood: `~/Desktop/proposals/kylie-larwood-90day-roadmap.html`
- Julie Conti: `~/Desktop/proposals/julie-conti-90day-roadmap.html`
- John Bult: `~/Desktop/proposals/john-bult-90day-roadmap.html`

---

## Rules

1. **Always extract from real call data.** Never invent business details. If something is unclear from the transcript, flag it as "[CONFIRM WITH CLIENT]".
2. **Tool recommendations are suggestions, not mandates.** If a client loves their current tool, keep it. Only recommend changes where there's a clear improvement.
3. **Success metrics must be realistic.** A solo operator won't generate 15 conversations/month. Match the metric to team size and niche.
4. **The 4 Pillars are always the same 4.** Content changes per client, but the structure is fixed: Offer Uniqueness, Multichannel Outbound, LinkedIn Content, ATS + Newsletter.
5. **Always include the DFY Sprint table** if client is on a managed service (Premium, VIP, or retainer). Omit if they're Standard tier (self-serve with community support).
6. **Milestones table is standard but adjustable.** The Day 30/60/90 structure stays. Specifics change per client.
7. **Save both outputs to the client's Google Drive folder.** If no folder exists, create one.
8. **After generating, offer to create the Discovery Doc as a Google Doc** in the client's folder.

---

## Reference Files

- **Discovery Template (Google Doc):** `1LTSMmkP8BC6gfEwCp0FdPl5xNbfTLz4zIw4lIZswojI`
- **Polished Roadmap example — Oliver Zauritz:** `1-QyAKtpFJa6Yw0ckMDlzXkUTWzKpzrVERR7ua-GfbXU`
- **Discovery example — Julie Conti:** `1FYBYvIWXFfSXHdPBvN8Ndn2KwSp18Vp9VcbfjC2ePfc`
- **Discovery example — Kylie Larwood:** `1iUW3MSA72pcrIApGOzup9A-MZWqkihPG7aItIkpKeEI`
- **Draft template (.docx):** `1jDT3ZuB_61vQP9KnS9NAI1bJQjN8pOk4`
