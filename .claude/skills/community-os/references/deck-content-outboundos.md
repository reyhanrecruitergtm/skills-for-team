# OutboundOS Deck — Content Map

Source: `projects/skool-courses/outbound-os/OutboundOS.pdf` (188 pages, full read 2026-07-16). This is the slide deck behind the OutboundOS course videos — the Tella recordings (Dec 30 2025 – Jan 5 2026) follow it module by module. Use this to answer "what does OutboundOS lesson X actually teach".

## Overview (p1–6)
- OutboundOS = proven multichannel outbound system for recruitment founders → steady pipeline of high-quality value-based conversations.
- Course map: M1–3 foundations/infrastructure/list building · M4–5 Dream100 + copywriting · M6 intent signals · M7–9 Clay · M10 3 ready-to-deploy playbooks + 8 use cases · M11 omnichannel launch · M12 CEO Power Hour.
- Requirements: ~$750/mo tech cost, offer-angle creativity, willingness to implement. Expected results: 5–7 qualified conversations/mo within 30 days; time: 1 hr/day CEO Power Hour + 15–20 hrs/wk maintenance (CEO or GTM Engineer).

## Module 1 — OutboundOS Foundations (p7–19)
- What OutboundOS is/is not: multichannel engine (email + LinkedIn + SMS + phone) that automates targeting, enrichment, sequencing, follow-up; NOT spray-and-pray, NOT set-and-forget, NOT a fix for bad positioning.
- Two roles: GTM Engine (automated: list building, intent signals, enrichment, sequencing) vs CEO (human: warm conversations, Dream100, deal progression). "Automation creates conversations. You convert them."
- **The 50:30:20 rule:** 50% leads (market definition, timing, intent signals) · 30% copy (positioning, opening lines, human language) · 20% tech. Most recruiters get it backwards (60% tech).
- Wrong vs right example: 2,000 unfiltered HR-director emails = 0.3% reply; 400 Series-A-SaaS-hiring-engineers emails = 8% (25x).
- Time: 4–6 hr one-time setup, 1 hr/day Power Hour, 8–10 hrs/wk total. Cost table: Sales Nav $99, Apollo $79, Clay $149–349, Instantly $79, HeyReach $59, OpenAI $20 → $500–750/mo.

## Module 2 — Agency-Grade Infrastructure (p20–50) → "Infrastructure" set
- 7-stage infrastructure stack graphic: 1 account selection (Sales Nav/Apollo/Prospeo) · 2 data & signal capture (Clay/Sentrion) · 3 personalization & assets (Gamma/Tella/Gemini) · 4 copywriting (Claude/Twain) · 5 outreach & sequencing (HeyReach/Instantly/Aloware/Wati) · 6 integrations & AI agents (n8n/respond.io) · 7 deal tracking (Recruiterflow/Attio).
- **Must-have tools (1–9):** Zapmail (secondary domains + mailboxes, $39; buy 5 lookalike domains × 2 mailboxes, DNS auto: SPF/DKIM/DMARC, connect to Instantly warmup) · Instantly (sending/warmup/unified inbox, Hypergrowth $79) · HeyReach (LinkedIn sequences, Pro $59) · n8n (integrations + AI reply agents, $24) · Sales Navigator ($99) · Prospeo (base list builder, Growth $89) · Apollo (backup data source, Professional $99) · RecruiterFlow (ATS+CRM hub post-reply, Advanced $119/user) · Tella ($20) · OpenAI ($20).
- **Email deliverability fundamentals:** secondary domains only (protect main brand); warmup rules — start 5 emails/day, +5 every 3 days, never exceed 50/day/account, minimum 14 days before cold sends; sending limits 30–50/day per mailbox; inbox rotation on.
- **LinkedIn account health rules:** 20–30 connection requests/day (ramp to 35 after a month), 50–100 messages/day, 100–150 profile views/day, 8am–8pm schedule.
- **Advanced tools (10–18):** Clay (intent playbooks hub, Explorer $349) · Claude (ideation/long-form copy, Pro $20) · Twain (human-sounding copy variations, credits) · Sentrion (job-posting intent alerts, Growth $149) · Gamma (proposals/decks, $10) · Ocean.io (lookalike company lists, $199) · JustCall (dialer + SMS sequences) · Apify (scrape ATS job boards Clay can't reach) · Wati (WhatsApp outreach, $49).

## Module 3 — Data Sourcing & List Building (p51–65) → "List Building" set
- List quality = the 50%: 200 perfect-fit leads beat 5,000 random; timing > volume.
- **Define ICP first — 10 questions:** industry/vertical, company size, buyer titles, geography, tech-stack indicator, growth signals, disqualifiers, ideal client's LinkedIn look, active problems, why you.
- **Build TAM (core market map):** Sales Navigator (dataset) + Prospeo (instant email enrichment); ALL companies matching ICP; 3 decision-makers per company; Apollo as CSV backup; organise in a Google Sheet.
- **6 list strategies:** 1 TAM (company filters → saved accounts → people search → Prospeo → Sheet) · 2 90-day job change ("changed jobs in past 90 days" lead filter; 3–5x more likely to meet) · 3 posted on LinkedIn in past 30 days (active profiles) · 4 2nd-degree connections matching ICP (mention the mutual) · 5 1st-degree connections matching ICP (straight to DM — sitting on warm leads) · 6 live jobs (manual LinkedIn Jobs / VA 30–60 min/day / Clay automated).
- List & performance tracker template. Clay positioned as later upgrade ("don't need it when starting").
- Later addition to the set: **"Apify as your List Building Tool"** video (May 12) — Apify actors for job boards / directories as list source.

## Module 4 — The Dream100 Playbook (p66–76)
- 100 transformative accounts; criteria: £50k+ annual potential, logo value, proof of fit, decision-maker access, revenue match.
- Not cold outreach — account monitoring: Month 1 engage content, M2 connect, M3 share value, M4 warm outreach, M5+ nurture. Daily 10-min actions (alerts, 3–5 comments, 1 thoughtful DM, log triggers, update CRM). Good vs bad engagement examples. Track in Recruiterflow pipeline or Dream100 tracker sheet.

## Module 5 — Copywriting That Converts (p77–99) → "Copywriting & Intent Signals" set
- Goal: START A CONVERSATION, not sell. Different sequences per lead type (cold = awareness; live = urgency; Dream100 = personalised relationship).
- Metrics: reply rate main metric; >5% good; 1.5% positive-reply very good.
- **Rules:** 80–150 words · one idea per email · specific beats generic · ask don't tell.
- 3 templates: Timeline Hook (open roles + 60–90-day fill pain), Insight Hook (funding trigger + warm bench), Pattern Interrupt (roles open ~120 days + 3 pre-vetted candidates).
- **The 2-step process:** ask permission first ("worth seeing how we…?"), then deliver value (case study/Loom) → call.
- Subject lines: 3–6 words, lowercase, mirror the trigger, no spam words; 10 value-first + social-proof + follow-up subject line banks. Custom variables ({{job_title_hiring_for}}, {{local_restaurant}}, {{content_reference}}…). DOs/DON'Ts (no calendar links in email 1, no "Let's talk!!"). AI tools: Claude/GPT for variations, Twain, spintax, liquid syntax — always review. Run 3–5 campaigns at once.

## Module 6 — Intent Signals Explained (p100–112) → signals half of the set
- Intent signal = publicly observable change meaning a company may need you NOW. Intent-based outreach 5–15% reply vs 1–3% random — timing = 50% of success.
- **Warm triggers:** 1 live jobs · 2 talent replacement/backfills (someone left → ex-manager outreach) · 3 company growth (funding rounds, headcount growth) · 4 90-day job change · 5 post engagers (yours + competitors').
- **Cold triggers:** alumni campaigns, marketing spend (FB/Google ads library), tech-stack match.
- **Stacking signals:** 2+ signals = 10x response likelihood (e.g. Series A + 5 open roles + new VP Engineering).

## Module 7 — Clay Foundations (p113–122)
- Clay = Input → Processing → Output across 100+ sources. Plans: free trial → Explorer $349 (Starter lacks API/HTTP/scheduling). Folders → workbooks → tables; Actions button. 4-step personalization: draft ideal email first → break into {variables} → map each variable to an enrichment → combine. "Think like a builder."

## Module 8 — Clay Data Logic & Control (p123–135)
- Credit economy ($0.04/enrichment; API ≈ 1/3 cost). Email waterfalls: Prospeo → Icypeas → LeadMagic (pay only on success). Merge columns free vs formulas. Formula types (conditional/formatting/conditional outputs) + 20-formula exercise. Filtering + auto-updates (off for beginners). AI prompting: define input → action → constrain output; #ROLE/#INPUT/#INSTRUCTION/#CONSTRAINTS template.

## Module 9 — Building Clay Playbooks (p136–147)
- Every playbook = Inputs (companies/people/jobs from Clay, Sales Nav, Apify, CSV, CRM, webhooks) → Processing (find people, email waterfall, enrich company/job, AI copy with Claude/GPT/Twain — spot-check 10–20%) → Outputs (person + verified email + personalised line → Instantly/HeyReach/CRM/Slack).

## Module 10 — RecruiterGTM Clay Catalog (p148–167)
- Prereq: TAM table in Clay (companies + decision makers) — "fish in a pond, not the sea".
- 3 autopilot playbooks with flowcharts + copyable templates: **LinkedIn Jobs Monitor** (TAM → find jobs → qualify → extract variables → find DM → waterfall → AI email → Instantly+HeyReach), **Recent Job Change Monitor** (90-day movers; new-company vs promotion split), **Backfills Monitor** (leavers → old company → vacancy age → DM).
- Use cases 4–11: low recruiter:employee ratio · career-page scraping · MPC-to-open-roles matching · Dream100 hitlist monitoring · track movers/champions · MPC lookalike poaching (rival companies) · recent funding · high ad spend.

## Module 11 — Launching Omnichannel Sequences (p168–179)
- Reply rates: email only 1–2%, LinkedIn 4–6%, combined 5–8%, + voicenotes/video 10–15%.
- Instantly setup steps (warmed accounts 14+ days, campaign per playbook, 3–5 emails 3–4 days apart, 30–50/day, rotation) · HeyReach setup steps (accounts aged 2+ wks SSI 50+, connection → follow-up if accepted, 20–30 connections/50–80 messages, rotate, sync with email).
- Typical sequence: D1 LinkedIn connect → D3 email 1 (permission opener) → D4 LinkedIn msg → D7 email 2 → D14 voicenote/video → D21 breakup.
- Reply handling: positive → pause both tools, move to CRM, respond personally; negative → remove; question → respond in 15 min; never >24 hrs. n8n cross-removal automation. SMS/WhatsApp only after 2–3 non-responses (JustCall/Wati; 10–20/day).

## Module 12 — The CEO Power Hour (p180–188)
- 60 min/day, high-leverage BD only. Structure 20-20-20: content & Dream100 engagement → personalised outreach/warm replies → calls & voicenotes. Keep: warm replies, active opportunities, Dream100 engagement, calls. Avoid: list building, Clay maintenance, sequences, tool setup (GTM Engineer's job). Rules: calendar-block, no admin, no distractions, hard stop. Math: 5 focused hrs/wk beats 20 scattered; system does 90% of touches, you close the 10%.
