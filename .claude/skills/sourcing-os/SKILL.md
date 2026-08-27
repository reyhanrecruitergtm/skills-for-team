# Skill: SourcingOS

Fully managed candidate sourcing engine powered by Claude Code. Scrape target firms, enrich profiles with LinkedIn + email data, match news/deals to candidates, generate personalised outreach, and push everything into a campaign-ready Google Sheet.

This is the internal execution engine behind RecruiterGTM's SourcingOS managed service. It delivers 30–50 quality candidate conversations per month across 4 evergreen role pipelines.

---

## Locked Rules

### A. URL verification (mandatory before any export)
- A1. Every LinkedIn URL HTTP-verified before including in any CSV, campaign, or proposal table. 200 = valid, 999 = LinkedIn rate-limit (usually still valid, flag for manual check), anything else = broken.
- A2. After generating any CSV with LinkedIn URLs, run the verification script. Fix or remove invalid URLs before handing the file to Reyhan.
- A3. Also check for CSV column alignment — empty fields with commas can shift columns and put podcast names in URL fields (real bug, real CSV that went to Lemlist).
- A4. Applies to: Lemlist campaign CSVs, proposal candidate/company tables, any export with LinkedIn links.

### B. Candidate links (cross-cuts with proposal-generator J4)
- B1. Candidate tables use personal LinkedIn (`linkedin.com/in/`) URLs. Company tables use company LinkedIn (`linkedin.com/company/`) URLs. NEVER mix.
- B2. If candidates legitimately lack personal profiles (blue-collar workers), label the column "Employer" and note explicitly that these are employer pages.

---

## How to Invoke

Say `/sourcing-os` followed by a target firm, niche, or sourcing brief.

Examples:
- `/sourcing-os run waterfall on this JD: [paste JD or URL] — target 200 candidates`
- `/sourcing-os scrape https://www.weil.com/people — SF and NY offices, all lawyers`
- `/sourcing-os enrich lawyers from weil_lawyers.json — find LinkedIn + personal emails`
- `/sourcing-os generate emails for Weil lawyers based on their deals and news`

---

## Waterfall v2 — Pin-First Sourcing (PRIMARY MODE)

The default path when given a JD or job role. End-to-end: JD in → Google Sheet of 200–500 qualified candidates out, scored against criteria with personalised hooks. This replaces the per-firm scraping path for any sourcing brief that starts as a role (not a firm directory).

### The waterfall (per candidate) — LOCKED 2026-05-24

| Layer | Tool | What it adds |
|-------|------|-------------|
| 1 | **Pin.com** (MCP) | Name, title, company, location, LinkedIn URL, Pin match score |
| 2 | **Prospeo** (own API key, PRO plan — 15k credits/mo at zero cost) | Primary email enrichment from LinkedIn URL → verified email. Burn freely. Memory: `reference_prospeo_api.md`. CLI: `.claude/skills/prospeo/prospeo.py` |
| 3 | **Apollo** (MCP) | Second pass for whatever Prospeo missed — work email, personal email, phone, current employment metadata |
| 4 | **Apify Google Search** | Third pass — cross-validate LinkedIn URL if Pin's missing/stale, or scrape profile bio for additional context |
| 5 | **SalesQL** *(planned)* | Fourth fallback for personal email + direct dial when all three above miss |
| 6 | **Web research** (Apify + Exa) | Recent posts, awards, news, deals — fuel for the hook |
| 7 | **Claude qualifier** | Score against each must-have criterion (✓/✗), overall fit /10, 1-line personalised hook |

### The volume engine (per role, to hit 200–500)

Pin returns 10 per `get_candidates`. Claude is the human-in-the-loop replacement:

1. `create_job` from JD (or `scrape_job_description` if URL)
2. `get_candidates` → 10 candidates
3. Claude auto-triages each vs criteria → strong fit / weak fit / reject
4. **`reject_candidate`** for weak fits with reasons — teaches Pin's recalibrator
5. **DO NOT call `accept_candidate`** — it triggers Pin's auto-email which we don't want. Save strong fits to the sheet only. We use our own Lemlist outreach.
6. `recalibrate_search` every 2–3 batches with the rejection signals
7. Loop until target hit (20 calls = 200 candidates, 50 calls = 500)

### The qualifier (per candidate)

Claude reads:
- The JD's must-haves (auto-extracted) + nice-to-haves
- The candidate's bio, title, company, tenure, LinkedIn activity (when Apify pulled it)

Outputs:
- One column per criterion: ✓ / ✗ / ?
- Overall fit score 1–10
- 1-line hook in Reyhan's voice (Tom & Jon proposal style — references something specific)
- Disqualification reason (if score < 4)

### Output sheet columns

| Name | Title | Company | Location | LinkedIn | Pin Score | Crit 1 | Crit 2 | Crit 3 | Crit 4 | Crit 5 | Fit /10 | Work Email | Personal Email | Phone | Hook line 1 | Hook line 2 | Included? | Drop reason | Source |

Filterable, sortable, ready for Instantly / HeyReach / Lemlist import.

### HARD RULE — Inclusion Gate (replaces per-email approval)

To be added to ANY outreach campaign, a candidate row MUST have BOTH:

1. **At least one contact channel** — work email OR personal email OR LinkedIn URL (any one)
2. **At least one custom hook line** — a 1- or 2-line opener tailored to them (Tom & Jon proposal style — references something specific they did, said, built, or signed)

If a row is missing EITHER, mark `Included?` = NO with the drop reason and skip. Never fabricate.

**Empty fields are fine.** If we can't find a phone number, leave it blank. If we can't find a specific deal, leave it blank. We never invent data to fill a gap. The inclusion rule guarantees that every row that DOES make it into a campaign has the minimum needed for a real touchpoint with a real personalisation hook.

This rule replaces per-email approval. We don't ask the client to approve every send. The bar is the inclusion gate — pass it and the email goes; fail it and the row is dropped.

### Approval flow (per role)

- **First list per role: manual review.** We send the sheet to the client (Slack channel), they review the hooks + criteria scoring, give the green light, we launch.
- **After 1-2 lists are approved and trust is built: automated.** Subsequent lists for the same role go straight to Instantly / HeyReach with no client approval — the inclusion rule does the gating.
- **Always:** flag rows where the personalisation source was thin (e.g. only a generic firm bio, no recent deal/post). Client reviews these before send even after we automate.

### HARD RULES — Credit Discipline (READ BEFORE ANY RUN)

Pin and Apollo both burn credits per call. Always:

1. **Confirm target count + budget with Reyhan BEFORE any production run.** Default cap: 200 candidates per test job unless explicitly raised.
2. **Test runs default to 50 candidates, NOT 200–500.** Production volume only after a test pass is approved.
3. **Pin recalibrate cap: 5 cycles per job.** More than that means the JD is too narrow — go back to Reyhan, don't keep burning credits.
4. **Apollo enrichment runs ONCE per candidate, after Claude qualifier has scored fit ≥ 6.** Never enrich rejects.
5. **Dedupe by LinkedIn URL before any enrichment call** — Pin and existing internal data may overlap.
6. **Keep a credit ledger.** Log Pin batches, Apollo lookups, Apify compute per run in `projects/sourcing-os/credit_ledger.csv` so we can track ROI per role.
7. **Never `accept_candidate`** — Pin's auto-outreach must stay off. Reject the weak fits, save the strong fits to the sheet only.

### Build artefacts (planned location)

- `projects/sourcing-os/run_waterfall.py` — the loop runner (Pin → Prospeo → Apollo → Apify → Claude → Sheet)
- `projects/sourcing-os/credit_ledger.csv` — credit consumption log
- `projects/sourcing-os/jobs/{job_id}/` — per-job artefacts (JD, criteria, candidates, sheet URL)

### When NOT to use Pin-first

- Brief is "scrape this firm directory" (e.g. Weil law firm) → use the firm-scraping path below
- Specialist executive search where Pin coverage is thin → Apify + Apollo first, Pin as secondary check
- Highly niche / new emerging roles where Pin's index hasn't caught up

---

## Exa Find-Similar (added 2026-06-05)

New layer in the waterfall when you have ONE ideal candidate and want lookalikes based on what they've actually done (papers, talks, GitHub, blog posts, conference pages), not just LinkedIn headline. Especially useful for:

- Niche or emerging roles where Pin / Apollo coverage is thin.
- Senior placements where the best candidates don't optimise LinkedIn.
- "Find me 30 more engineers like the one I just placed" — fastest fill mechanism for the 4 evergreen role pipelines.

### How to invoke

```bash
python3 projects/exa-tools/find_similar_candidates.py \
  --seed-url <ideal candidate LinkedIn or personal site URL> \
  --role "<role label>" \
  --count 30 \
  --slug <client-or-role-slug>
```

Output drops to `~/Desktop/sourcing-runs/<slug>__YYYY-MM-DD.csv` (+ matching `.json`). Every LinkedIn URL HTTP-verified before write per Rule A1.

### Where it sits in the waterfall

Use as **Layer 0** (before Pin) when a brief comes in as "fill more of these" rather than "fill this JD". Feed the Exa output's LinkedIn URLs into the existing Pin / Apollo / Apify enrichment passes — Exa supplies discovery, the existing waterfall supplies verified contact data.

### When NOT to use Exa Find-Similar

- Brief is a clean JD with no seed candidate yet → stay on Pin-first.
- Brief is a firm directory scrape → still use Apify.
- Volume push of 500+ — Exa is per-query priced; Pin scales cheaper for bulk.

### Setup

One-time: paste Exa API key into `.env` as `EXA_API_KEY=...`. See `projects/exa-tools/README.md` for details.

---

## Exa TAM Builder (added 2026-06-05)

Same `projects/exa-tools/` folder also includes `tam_builder.py` for **proposal TAM tables** — solves the recurring problem of generating verified 10-20-row decision-maker tables for `proposal-generator` (cross-cuts with that skill, not SourcingOS-specific). Use when:

- A proposal needs a TAM table for a niche where prior research stalled.
- A SourcingOS client brief asks for the **decision-maker side** of their market (e.g. for John Randolph: Managing Partners at sub-150 CPA firms).

```bash
python3 projects/exa-tools/tam_builder.py \
  --niche "<niche brief>" \
  --target "<target titles>" \
  --count 15 \
  --slug <client-slug>
```

### Open questions to resolve before first run

These need Reyhan's answer before the build:

1. **Test JD** — which role do we test against?
2. **Target count for first test** — 50 (default) or higher?
3. **Apollo credit budget** — confirm cap before bulk enrichment.
4. **Output Drive folder** — which Drive folder gets the sheet?
5. **SalesQL key** — when ready, paste API key so we can wire Layer 4.

---

## What This Skill Delivers

The 5 SourcingOS deliverables, automated:

### 1. Candidate ICP Market Map
- Scrape target firm directories (law firms, consultancies, agencies, corporates)
- Extract: name, title, office, phone, work email, bio, practice areas, education, awards
- Build candidate ICP per role: seniority, skills, tenure, location
- Market map: target companies, exclusion filters, competitor-placed candidates

### 2. Profile Enrichment Pipeline
- **LinkedIn URLs** — Apify Google Search Scraper (`site:linkedin.com/in "Name" "Company"`)
- **Work emails** — scraped directly from firm websites
- **Personal emails** — Apollo People Match (name + company + LinkedIn URL), Apify LinkedIn scraper for contact info
- **Phone numbers** — Apollo enrichment where available
- **Pin.com integration** — [PENDING: awaiting MCP server URL from Pin team] — candidate database search, ATS-connected profiles

### 3. News & Deal Intelligence
- Scrape firm news/insights pages (press releases, deal announcements, thought leadership)
- Match articles to individual lawyers/candidates based on name mentions
- Extract deal details: transaction type, value, parties involved
- This becomes the personalisation layer for outreach

### 4. Personalised Outreach Generation
- LLM generates custom email per candidate based on:
  - Their specific deals/transactions
  - Recent news mentions
  - Practice area + seniority
  - Signal that triggered them (tenure, promotion, company change)
- Output: email subject + body, LinkedIn connection request, follow-up sequence
- Follows SourcingOS copywriting rules: passive candidate tone, signal-triggered, 3-touch minimum

### 5. Campaign-Ready Output
- Google Sheet with all enriched data in target Drive folder
- Columns: Name, Title, Office, Work Email, Personal Email, Phone, LinkedIn, Bio, Practice Areas, Deals, News, Personalised Email Draft
- Ready to import into Lemlist for multi-channel campaign
- CSV export for any other outreach tool

---

## Architecture

### Data Sources (Current — Pin.com is PRIMARY)

Priority order for any new sourcing brief:

1. **Pin.com (PRIMARY)** — job-role candidate search via MCP. Use first when the brief is a job role.
2. **Apify** — firm directory scraping + Google `site:linkedin.com/in` search for missing LinkedIn URLs.
3. **Apollo** — verified work email, personal email, phone.
4. **Web research** — news, deals, awards, signals (for the personalisation layer).

| Source | What It Gets | API/Method |
|--------|-------------|------------|
| **Pin.com** | Ranked candidates against a job role, with accept/reject feedback loop | MCP server `https://mcp.pin.com/mcp` — see Pin.com Integration section below |
| **Target firm website** | Name, title, office, bio, practice areas, education, deals, news | Sitemap + requests/BS4 scraping |
| **Apify Google Search** | LinkedIn profile URLs | `apify/google-search-scraper` — `site:linkedin.com/in` queries |
| **Apollo** | Verified work email, personal email, phone | `apollo_people_match` MCP tool — name + company + LinkedIn URL |
| **Apify LinkedIn Scraper** | Full LinkedIn profile data, contact info | `apify/linkedin-profile-scraper` (or similar actor) |
| **Firm news pages** | Deal announcements, awards, thought leadership | Direct scraping of news/insights sections |

### Data Sources (Planned)
| Source | What It Gets | Status |
|--------|-------------|--------|
| **Lusha** | Personal email + direct phone | Need API key |
| **Hunter.io** | Email verification + finder | Need API key |
| **Dropcontact** | GDPR-compliant email enrichment | Need API key |
| **Crustdata** | Company signals (layoffs, funding, leadership changes) | Evaluate |
| **LinkedIn Sales Nav** | Advanced people search + saved leads | Via Apify or browser-use |

### Tools Stack
- **Apify** — web scraping actors (API key in `.env` as `APIFY_API_KEY`)
- **Apollo** — people enrichment (connected via MCP `mcp__claude_ai_Apollo_io`)
- **Google Workspace** — Sheets output (connected via MCP `mcp__google-workspace`)
- **Python** — scraping scripts in `projects/legal-sourcing/`
- **Claude** — LLM for email personalisation, deal matching, candidate scoring

---

## Step-by-Step Execution

### Phase 1: Scrape Target Firm
1. Identify the firm's people directory URL
2. Check for sitemap (`/sitemap.xml`, `/robots.txt`) — use Googlebot UA if needed
3. Extract all profile URLs from sitemap or paginated listing
4. Scrape each profile page with 5 parallel threads, 0.3s delay
5. Parse: name, title, office, phone, email, bio, practice areas, education, awards, deals, news
6. Filter by target office/location
7. Save as JSON: `{firm}_lawyers_raw.json` and `{firm}_lawyers_{filter}.json`

**Key parsing patterns (law firms):**
- Title + Office: `<header class="bio-bar-header"><span class="h3">Title<span>Office</span></span></header>`
- Bio: content after `<h2>Biography</h2>`
- Practice areas: `<section>` with `<h2 class="h4">Practice Areas</h2>` → `<ul class="link-list-small">`
- Education: same pattern with "Education" heading
- Awards: `<ul class="link-list">` with `<span class="link-list-head">` items
- DataLayer fallback for title: `window.dataLayer.push({'Role': 'Partner'})`

### Phase 2: LinkedIn Enrichment
1. For each candidate without a LinkedIn URL:
   - Build query: `"{First} {Last}" "{Company}" site:linkedin.com/in`
   - Run via Apify Google Search Scraper in batches of 50
   - Extract first `linkedin.com/in/` result from organic results
2. Expected hit rate: 85–90%
3. Save enriched data: `{firm}_lawyers_enriched.json`

### Phase 3: Email Enrichment
1. **Work emails** — usually captured during firm scrape (pattern: first.last@firm.com)
2. **Apollo enrichment** — for personal emails:
   - Use `apollo_people_match` with: first_name, last_name, organization_name, linkedin_url
   - Set `reveal_personal_emails: true`
   - **WARNING: consumes Apollo credits per lookup — confirm with Reyhan before bulk runs**
3. **Apify LinkedIn Scraper** — for candidates with LinkedIn but no email:
   - Scrape LinkedIn profile contact info section
   - Some profiles expose personal email there

### Phase 4: News & Deal Intelligence
1. Scrape firm's news/insights sections:
   - Newsroom, press releases, deal announcements
   - Blog posts, thought leadership articles
   - Awards and recognition pages
2. For each article, extract:
   - Title, date, URL
   - Named lawyers/people mentioned
   - Deal details: parties, transaction type, value
3. Match articles to scraped lawyers by name
4. Store as `news_matched` field on each candidate

### Phase 5: Personalised Outreach
1. For each candidate with deals/news data:
   - Generate custom email using Claude
   - Input: candidate bio + deals + news + practice area + signal
   - Output: email subject, body, LinkedIn connection request
   - Tone: professional, specific to their work, not templated
2. Follow the copy rules from SourcingOS service definition:
   - Signal-triggered (not spray-and-pray)
   - Passive candidate tone
   - 3-touch minimum follow-up sequence
3. Save drafts to the Google Sheet

### Phase 5B: Data Verification (MANDATORY before export)
1. Run HTTP verification on every LinkedIn URL in the dataset
   - 200 = valid
   - 999 = LinkedIn rate limit (URL format likely valid, flag for manual check)
   - 404 or other error = invalid, must be fixed or removed
2. Check CSV column alignment — empty fields with commas can shift columns and put wrong data in URL fields
3. Remove or flag any row with an invalid LinkedIn URL
4. For email addresses, verify domain exists (MX record check) at minimum
5. Output a verification summary: total rows, valid URLs, invalid URLs, missing emails
6. **Rule:** No CSV or Google Sheet leaves this skill without a verification pass. Reyhan has had campaigns fail because of invalid URLs that were never checked.

### Phase 6: Campaign Output
1. Create Google Sheet in target Drive folder
2. Upload all enriched + personalised data
3. Format: one row per candidate, all fields populated
4. Ready for Lemlist import or manual outreach

---

## Firm-Specific Scrapers

### Law Firms (Proven)
- **Weil Gotshal & Manges** — sitemap at `/sitemap/people`, server-rendered profiles, Sitecore CMS
  - Scripts: `projects/legal-sourcing/scrape_weil.py`, `enrich_linkedin.py`
  - Output: 1,291 total lawyers, 606 in SF+NY

### Adapting to New Firms
Most large law firm websites follow similar patterns:
1. Check `/robots.txt` for sitemap URLs
2. Look for `/people`, `/attorneys`, `/professionals` directories
3. Profile pages usually have: name (h1), title+office in header area, bio section, practice area links
4. Adapt the CSS selectors in `scrape_profile()` for each firm's HTML structure

---

## Pin.com Integration [LIVE — PRIMARY SOURCE]

Pin.com is the **primary candidate source** for SourcingOS. Pin is job-role-driven, not person-search-driven — you create a job, Pin returns ranked candidates, you accept/reject, Pin recalibrates. Use this lane first; fall back to Apify + Apollo only when Pin runs dry or for fields Pin doesn't expose (personal email, news/deals, signals).

### Connection

- **MCP URL:** `https://mcp.pin.com/mcp`
- **Transport:** Custom connector (SSE-based)
- **Auth:** OAuth — authenticate Pin account against Claude

### Setup (Antigravity / Claude Desktop)

1. Customize → "+" icon → "Add custom connector"
2. Name: `pin`
3. URL: `https://mcp.pin.com/mcp`
4. Authenticate Pin with Claude
5. Set tool permissions to "always allow" (Pin recommends this)

### Available MCP Tools

**Search management**
| Tool | What it does |
|------|-------------|
| `create_job` | Initiates candidate search using job title + description (+ optional company name/website) |
| `scrape_job_description` | Extracts title, location, description from a job board URL |
| `modify_search` | Adjusts search criteria using natural language |
| `recalibrate_search` | Applies accept/reject feedback to generate an improved next batch |
| `list_jobs` | Returns active searches, filterable by job title |

**Candidate review & actions**
| Tool | What it does |
|------|-------------|
| `get_candidates` | Returns up to 10 ranked unreviewed candidates per search |
| `accept_candidate` | Moves candidate into Pin's outreach sequence with auto-email |
| `reject_candidate` | Declines candidate + sources replacement; accepts structured or free-text rejection reasons |

### Two Use Cases

**Use Case A — Pull candidates against a job role (PRIMARY)**
This is Pin's native mode. Use it whenever the brief is "find candidates for [role]".

**Use Case B — Look up a specific person**
Pin has no direct person-lookup endpoint. Workaround: `create_job` with a description tightly scoped to that person's profile (current title + company + niche skills), then scan `get_candidates` results for the name. If they don't appear, fall back to Apify Google search (`site:linkedin.com/in "Name" "Company"`).

---

## Pin.com Scenario Walkthrough — Senior Property Manager (San Francisco)

Concrete example. Client is a property management recruitment agency. The brief: "Senior Property Manager, San Francisco, 5+ years residential, AppFolio or Yardi, 200+ unit portfolios."

**Step 1 — Create the job**
```
mcp__pin__create_job(
  title: "Senior Property Manager",
  description: "5+ years managing residential property portfolios in SF Bay Area. Familiar with AppFolio or Yardi. Track record of 200+ unit portfolios. Strong tenant relationship skills.",
  company: "(client's company name, optional)"
)
→ Returns: job_id
```

**Step 2 — First batch of candidates**
```
mcp__pin__get_candidates(job_id: <id>)
→ Returns: 10 ranked candidates with name, current title, current company, location, LinkedIn URL, Pin's match score
```

**Step 3 — Review with Reyhan / client**
- Render the 10 in a table
- Reyhan accepts 4, rejects 6 with reasons ("too junior", "wrong asset class", "out of region")

**Step 4 — Apply feedback + pull next batch**
```
mcp__pin__recalibrate_search(job_id: <id>, ...feedback...)
mcp__pin__get_candidates(job_id: <id>)
→ Next 10 candidates, now closer to the target
```

Repeat steps 3–4 until the shortlist hits the target size (typically 30–50 across the role).

**Step 5 — Accept candidates → Pin auto-outreach**
```
mcp__pin__accept_candidate(candidate_id)
→ Pin moves them into its sequence with the configured auto-email
```

**Step 6 — Cross-enrich beyond Pin (RecruiterGTM layer)**
Pin's auto-email is generic. For tier-1 candidates, override with our own personalised outreach:
- Apollo for personal email + phone (Pin returns work email; we want both)
- Apify Google search for LinkedIn cross-validation
- News/deal/awards matching from firm pages, LinkedIn activity, public mentions
- Claude drafts the email + LinkedIn message in the founder's voice

**Step 7 — Output**
- Google Sheet row per candidate: name, current title, company, location, LinkedIn, work email, personal email, phone, signal, deal/news matched, personalised email draft, personalised LinkedIn message
- For tier-1: bespoke outreach goes out via Lemlist (overriding Pin's auto-email)
- For tier-2/3: leave Pin's auto-email running

### When to use Pin first vs firm-scraping first

| Situation | Source order |
|-----------|-------------|
| Brief is a job role (any niche) | Pin → Apollo → web research |
| Brief is "scrape this firm" (e.g. Weil law firm directory) | Apify firm scrape → Apollo → Pin (only for cross-reference) |
| Blue-collar / construction / trades / field-staff | Pin → Apify → Apollo (Pin Indexes blue-collar talent well — see tools audit decisions) |
| Highly specialist / executive search where Pin coverage is thin | Apify + Apollo first, Pin as secondary check |

### Credit / cost discipline

- `get_candidates` and `recalibrate_search` consume Pin lookup credits per batch
- Always confirm with Reyhan before running more than 3 recalibration loops on a single job
- Apollo enrichment is also credit-billed — only run after Pin's accept_candidate decision, never on raw `get_candidates` output

---

## Intent Signals (Sourcing Intelligence Layer)

These signals determine WHEN to reach out, not just WHO. Every candidate should have at least one signal before a message is sent.

| Signal | Source | How to Detect |
|--------|--------|--------------|
| **Tenure 2-3 years** | LinkedIn profile | Check current role start date |
| **Recent promotion** | LinkedIn activity | Title change in last 6 months |
| **Company contraction** | Crustdata / news | Layoffs, restructures, leadership exits |
| **Deal completion** | Firm news page | Major transaction just closed — lawyer may be ready for next move |
| **Award/recognition** | Profile awards section | Recently named to rankings — peak visibility moment |
| **Content activity** | LinkedIn posts | Publishing thought leadership — open to conversations |
| **Job posting signal** | Apollo org data | Their firm is hiring similar roles — market is active |

---

## Quality Benchmarks

Per SourcingOS service definition:
- **30–50 quality candidate conversations per month** (across 4 evergreen roles)
- This means the system needs to surface 200+ qualified candidates per month to hit this at a 15-25% response rate
- Personalised, signal-triggered outreach is the multiplier

---

## Files

| File | Purpose |
|------|---------|
| `projects/legal-sourcing/scrape_weil.py` | Weil lawyer scraper (sitemap → profile scraping) |
| `projects/legal-sourcing/enrich_linkedin.py` | LinkedIn URL enrichment via Apify |
| `projects/legal-sourcing/weil_lawyers_raw.json` | All 1,291 Weil lawyers |
| `projects/legal-sourcing/weil_lawyers_sf_ny.json` | 606 SF+NY filtered lawyers |
| `projects/legal-sourcing/weil_lawyers_enriched.json` | With LinkedIn URLs (539/606 found) |
| `projects/legal-sourcing/weil_final_clean.csv` | Clean CSV uploaded to Google Drive |

---

## Edge Cases

- **JS-rendered directories** — use Apify Web Scraper (Puppeteer) instead of requests/BS4
- **Rate limiting** — respect 0.3s delay between requests, use Googlebot UA for sitemaps only
- **Name parsing** — handle suffixes (III, Jr., Jr), middle initials, hyphenated names
- **Multi-office lawyers** — some lawyers list multiple offices (e.g. "Washington, D.C., New York") — match if ANY target office appears
- **404 profiles** — some sitemap URLs are stale — skip gracefully
- **Apollo credit management** — always confirm before bulk enrichment runs, never run silently

---

## Recommendations for Future Enhancement

1. **Candidate Scoring Model** — score each candidate 1-10 based on: seniority match, practice area relevance, signal strength, reachability (email + LinkedIn). Prioritise outreach to highest-scored.

2. **ATS Integration** — auto-push interested replies into client's ATS (Bullhorn, JobAdder, Vincere) with source attribution. Status logic: Contacted → Replied → Screening → Submitted.

3. **Browser-Use for LinkedIn** — use the browser-use skill to navigate LinkedIn Sales Navigator, save leads to lists, and extract contact info from profiles that require login.

4. **Crustdata Company Signals** — monitor target companies for layoffs, funding rounds, leadership changes. Auto-trigger sourcing when a signal fires.

5. **Competitor Firm Scraping** — build scrapers for top 20 law firms (Skadden, Sullivan & Cromwell, Kirkland, Latham, etc.) and aggregate into a single talent pool. Same scripts, different CSS selectors.

6. **Automated Weekly Runs** — schedule the pipeline to run weekly via n8n or cron. New lawyers added to the firm → auto-scraped → auto-enriched → auto-added to sheet.

7. **WhatsApp/SMS Add-on** — for high-priority candidates, auto-generate WhatsApp message from the personalised email draft. Paid add-on per SourcingOS pricing.

8. **Candidate De-duplication** — cross-reference across multiple firm scrapes to avoid contacting the same person twice (lateral moves between firms).
