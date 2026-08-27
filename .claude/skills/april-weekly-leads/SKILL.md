# April Weekly Intent Leads — Agent Runbook

## What this does
Runs April Ben-Sabat's (Inner Circle Agency) weekly intent-led lead refresh: re-scan intent → rank → find 2 verified decision-makers per company → live-verify each → dedup against everyone already contacted → append to the running **Weekly Intent Leads** sheet → upload to Drive. Target ~200 new verified leads per week.

Invoke: `/april-weekly-leads` (or scheduled weekly, Monday UK). Read `memory/wiki/clients/april-inner-circle.md` FIRST — it holds the confirmed ICP + all title/verification/dedup rules that govern this.

## Standing assets
- **TAM (canonical):** `~/Desktop/Clients/April Ben-Sabat/_build-data/TAM-sources/master_signals.csv` (2,785 confirmed, match+size+ICP verified).
- **Running sheet:** `~/Desktop/Clients/April Ben-Sabat/Reyhan Plan/April - Weekly Intent Leads.xlsx` (person-level, `Week` + `Date Pulled` cols; the sheet IS the dedup ledger).
- **Drive folder (upload final here):** https://drive.google.com/drive/folders/10SNcAjhysKfMo2Fhvyz4XpbDGt4yyHE3
- Keys in repo `.env`: `APIFY_API_KEY`. Clay via MCP `mcp__claude_ai_Clay__find-and-enrich-contacts-at-company`. (Apollo out of credits; Prospeo/Exa NOT for people.)

## The weekly pipeline (each step proven 2026-08-11)

1. **Re-scan intent (fresh open jobs).** Apify `curious_coder/linkedin-jobs-scraper`, ONE job-search URL per company `https://www.linkedin.com/jobs/search?f_C=<id>&geoId=92000000` (numeric LinkedIn id; passing all ids in `companyIds` = HTTP 414). Parse JD text for finance/ERP titles (open-role signal) + ERP system names. Merge into `master_signals.csv` (`FinanceRoleOpen`, `ERPDetected`, `OpenJobs`, `ERPSystems`). Intent refreshes weekly, so new open-role companies surface each run.

2. **Rank by the waterfall:** open finance/ERP role → ERP-detected → ICP-match rank (Tier+Score). No-intent only once intent is exhausted.

3. **Exclude anyone already worked.** Read the existing sheet's `LinkedIn URL` column (and the companies already pulled). Skip companies whose 2 contacts are already in the sheet; a company can be revisited only for a NEW person.

4. **Find people = Clay** (`find-and-enrich-contacts-at-company`), chunk ~16 companies/subagent, parallel. `job_title_keywords` = CFO/Chief Financial Officer/Chief Accounting Officer/VP Finance/Vice President Finance/Finance Director/Director of Finance/Head of Finance/Controller/Financial Controller/Corporate Controller + fallback Head of Talent/Head of Talent Acquisition/CHRO/Chief People Officer/VP People. `exclude` = Assistant/Intern/Junior/Analyst/Specialist/Clerk/Coordinator/Recruiter/Staff.
   - **Selection priority:** CFO > CAO > VP Finance > Finance Director/Dir of Finance/Head of Finance > **Financial Controller** (ACCEPT only "Controller"/"Financial Controller"/"Corporate Controller"; REJECT Plant/Regional/Project/Assistant/Cost/Divisional Controller). Head-of-Talent ONLY if NO finance leader. CEO only if <500. 2 per company.
   - First-pass verify: keep only if Clay `latest_experience_company` matches the target.

5. **LIVE-verify EVERY person = Apify `harvestapi/linkedin-profile-scraper`** (`profileScraperMode:"Profile details no email ($4 per 1k)"`, `queries`=[profile URLs]). Keep ONLY if the live current company matches the target. Set **Decision Maker Verified = Yes** (only Yes go to April; No held).

6. **Append** the verified rows to the running sheet with the new `Week` label + today's `Date Pulled`. Dedup on LinkedIn URL across the whole sheet before appending. Rebuild via the same column layout (see the Week-1 build for the format).
   - **Column layout (locked 2026-08-11):** Week · Date Pulled · Company · Website · Vertical · Angle · **Signal Category** · **Why Pulled** · Name · Title · LinkedIn URL · Decision Maker Verified · 1-liner (draft, April voice).
   - **Signal Category** = the reason the lead was pulled, one of: `Open Job` (hiring an open finance/ERP role) → `Growth` (hiring surge / headcount expansion signal) → `ERP Signal` (runs a target ERP our candidates already know) → `ICP Fit (fallback)` (strong ICP match, no active signal this week). This mirrors the waterfall order — always fill the highest tier that applies. **Why Pulled** = the plain-English specific (e.g. "Runs SAP (an ERP our finance candidates already know)"). No em dashes in either column.

7. **Upload** the updated `.xlsx` to the Drive folder (delete the old, upload new — or overwrite). Keep the folder to 2 files: the Target Account List (dashboard) + Weekly Intent Leads.

## Locked rules (from April, do not violate)
- Financial controllers OK; **NO Plant/Regional/Project/Assistant/Cost Controllers**; no TA specialists/coordinators/recruiters; no random VPs (Preconstruction/BizDev/R&D); no CEO >500; no <200-employee companies.
- **Every person live-verified current** before it reaches April (her #1 past complaint was stale/job-changed contacts).
- **Never contact the same person twice** — dedup on LinkedIn URL against the whole sheet.
- Construction = finance-only (no ERP/tech contacts). ERP routing: finance-side→CFO, ops-side→VP Ops.
- **1-liners** are drafts → finalize via `email-writer`/`content-os` in April's operator voice, no em dashes, no "Hook:" prefix, pain-point angle. LinkedIn connection+message only, 15–25/day.

## Scheduling
Run weekly (Mon 8am UK) via `/schedule` (cron). Needs the Clay + Apify MCP/keys available in the run context. If a scheduled/headless run can't reach Clay (OAuth), flag it and run interactively.
