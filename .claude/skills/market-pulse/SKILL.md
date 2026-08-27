# Market Pulse Skill

Owns **The Recruitment Market Pulse** end to end: always-current research on the recruitment agency market → monthly published edition → repurposed content → offer optimization. This skill is the single home for "what is happening in our market and what do we do about it."

## What This Skill Does

1. **Maintains the research base** — `research/market-pulse/<YYYY-MM>/` holds each month's sweep. Each month builds on prior months (what changed), never repeats them.
2. **Produces the monthly edition** — drafted in the locked 8-section structure, published as its own page on recruitergtm.com.
3. **Repurposes** — LinkedIn post(s), newsletter section, Skool post per edition.
4. **Optimizes the offer** — every edition ends with an internal pass: what do this month's findings say about RecruiterGTM's own offers, pricing model, and positioning? Material findings go to `decisions/log.md` and get raised with Reyhan.

## Locked Rules

### A. Structure & ratio
- A1. Every edition uses the locked 8-section structure, in this order, never renamed or reordered: **1 TL;DR (5 pointers) · 2 Sentiment Check · 3 Who's Winning With What · 4 The Numbers That Matter · 5 Where the Market Is Heading · 6 The Playbook (3–5 moves) · 7 Sources · 8 How RecruiterGTM Helps**. One structure every time (Reyhan, 2026-07-17).
- A2. Content ratio is locked: **95% actionable research for agency owners, 5% RecruiterGTM**. Section 8 CTA = book a call (`/start-pilot`) + newsletter (`/newsletter`). Never any pricing.
- A3. Page layout follows the 5-layer consultancy format (hero stat → KPI cards → TL;DR → numbered sections with "What this means" boxes → playbook → linked sources). Recipe: `research/2026-07-17-industry-report-format-analysis.md`.
- A4. Audience is owners of small-to-medium recruitment agencies who skim on phones. Practitioner voice, British/neutral English, no hashtags, no consultant-speak.
- A5. **Edition naming = the month it PUBLISHES/SENDS, never the research month (Reyhan, 2026-08-03).** Research gathered in July, published 1 August → "August 2026 edition" everywhere: page title, URL slug, badge, graphic, posts, newsletter, internal stat source lines. Edition 01 = August 2026 (`/market-pulse/august-2026`; the old `july-2026` slug 301-redirects). The monthly routine runs on the 1st, so each run's output is named for the month it fires in.

### B. Sources & stats
- B1. Two tiers. **Quotable:** Bullhorn GRID, REC, APSCo, SIA, ASA, and named primary reports/filings. **Caution:** vendor blogs and uncorroborated marketing stats — verify against a primary source or exclude. Never present caution-tier as solid.
- B2. Every stat carries a named source + date in the copy, and a link in Sources. Never invent or pad numbers (preflight rule).
- B3. The edition page states the methodology line (compiled from primary reports; vendor stats excluded unless corroborated).
- B4. **Internal RecruiterGTM data point is mandatory (Reyhan, 2026-08-03):** every edition includes at least one data point or trend from our OWN internal research — a Skool community poll (always state the n, e.g. "polled across our 82-member community"), client account campaign benchmarks, or audit/placement data — placed inside the research sections (not the Section 8 CTA) so readers associate the research with RecruiterGTM. Internal stats obey B2 like any other stat: actually measured, never estimated or invented. If no fresh internal number exists at draft time, run the community poll during the research window (post poll → wait ~48h → use the real result). A hypothetical Reyhan floats in conversation (e.g. "50% find Claude Code easier than Clay") is a POLL QUESTION to run, not a stat to print.

### C. Website
- C1. Editions get their own URL: `/market-pulse/<month>-<year>` (month per rule A5 = publish month). Index at `/market-pulse`. New edition = new view in `src/views/`, new app route, sitemap entry, index page `editions` array entry, **`pulseEditions` array entry in `app/resources/page.tsx`**, and page-log update in `memory/wiki/references/reference_website_lovable.md` — all in the same pass.
- C4. Pages use the site's dark brand theme ONLY (`bg-background`, `glass-card`, `text-violet-ray`, `font-heading`). Never white or beige page backgrounds (Reyhan, 2026-07-17).
- C2. Every page includes the main site `Header` (website skill rule A4). `npm run build` must pass before handing over.
- C3. Never commit/push to main without Reyhan's explicit go — push = live deploy.

### D. Workflow & cadence
- D1. Monthly cloud routine `market-pulse-research` (cron `0 7 1 * *` UTC ≈ 8 AM UK) drafts research + repurposes into `research/market-pulse/<YYYY-MM>/`, creates the Pulse content-tracker task + Google Calendar review event, and DMs Reyhan. Human gate before anything is public.
- D2. Repurposed copy runs through the house voice rules: LinkedIn per `content-os` (hook alone on first line, one sentence per line, no hashtags, —— sign-off), newsletter per `newsletter-writer`, everything through `copy-engine` before delivery.
- D3. Offer-optimization findings that change strategy, pricing, or positioning are logged in `decisions/log.md` and flagged to Reyhan — never silently applied.
- D4. **Internal-data cadence (added 2026-08-03, enforces B4):** the monthly `market-pulse-research` routine (1st of month) now includes research angle (d): find or request the edition's internal RecruiterGTM data point. If no fresh internal number exists, the routine drafts ONE community poll question for the edition theme, marks the draft `[INTERNAL DATA PENDING]`, puts a checklist line on the monthly Pulse review task, and flags the poll in Reyhan's Slack DM so he posts it in Skool — real result gets filled in before publish. Poll results, when they land, get saved to `research/market-pulse/<YYYY-MM>/` so the routine and edition builds can find them.
- D5. **Edition launch graphic is LOCKED (Reyhan, 2026-08-03):** every monthly edition's LinkedIn launch post uses the cover template at `.claude/skills/market-pulse/edition-graphic-template.html` (1080×1350): dark navy `#0d1117`, cyan `#00C8FF` accent, "The Recruitment Market **Pulse**" masthead, month badge, ECG heartbeat line, "Inside this edition" ✔ list, CTA button directly below the list (not pinned to the bottom), url + RecruiterGTM brand. Per edition swap ONLY: the month badge and the ✔ bullets. The internal B4 data point is always one of the bullets, stated WITHOUT a source on the graphic — the source line lives on the report landing page. Never include the line "Every number linked to its source" on the graphic. Structure changes need Reyhan's explicit sign-off.

## Commands

Invoke `/market-pulse [command]`:

- **`refresh`** — Run the research sweep now (don't wait for the routine). Fan out three research agents: (a) productized models + named firms, (b) practitioner sentiment (Savage, Mena, Azzouz, Caan, r/recruiting, LinkedIn), (c) market direction (Bullhorn GRID, REC, APSCo, SIA, ASA + AI adoption). Save to `research/market-pulse/<YYYY-MM>/`, summarize what changed vs last month.
- **`edition`** — Draft this month's edition from the latest research folder, in the locked structure (A1–A4, B1–B3).
- **`publish`** — After Reyhan approves the draft: build the edition view + route, update index/sitemap/page log, run the build, hand over for push approval (C1–C3).
- **`repurpose`** — Generate the LinkedIn post, newsletter section, and Skool post from the current edition (D2). Drafts only.
- **`offer-check`** — Map the latest findings against RecruiterGTM's current offers (`context/work.md`, 5 pillars, pilot/retainer structure): what should we double down on, reframe, or test? Output a short memo + `decisions/log.md` entries for anything material (D3).
- **`status`** — Show latest edition, next routine run, pending review tasks, and whether website/index are current.

## Key files & references
- Project note: `memory/wiki/projects/project_market_pulse.md` (baseline July 2026 findings live here)
- Research base: `research/market-pulse/` + the three 2026-07-17 baseline reports in `research/`
- Website: `projects/website-nextjs/` — `src/views/MarketPulseIndex.tsx`, `src/views/MarketPulse<Month><Year>.tsx`, `app/market-pulse/`
- Routine: claude.ai/code routine `market-pulse-research` (cloud; needs GitHub repo access to `reyhanrecruitergtm/ea`)
- Distribution: website → Skool → Beehiiv → LinkedIn, in that order, after Reyhan's review
