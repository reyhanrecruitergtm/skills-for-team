# Skill: SourcingOS

Fully managed candidate sourcing engine powered by Claude Code. Scrape target firms, enrich profiles with LinkedIn + email data, match news/deals to candidates, generate personalised outreach, and push everything into a campaign-ready Google Sheet.

This is the internal execution engine behind RecruiterGTM's SourcingOS managed service. It delivers 30–50 quality candidate conversations per month across 4 evergreen role pipelines.

---

## How to Invoke

Say `/sourcing-os` followed by a target firm, niche, or sourcing brief.

Examples:
- `/sourcing-os scrape https://www.weil.com/people — SF and NY offices, all lawyers`
- `/sourcing-os enrich lawyers from weil_lawyers.json — find LinkedIn + personal emails`
- `/sourcing-os generate emails for Weil lawyers based on their deals and news`
- `/sourcing-os full pipeline — [firm URL] — [offices/filters] — [output sheet URL]`

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

### Data Sources (Current)
| Source | What It Gets | API/Method |
|--------|-------------|------------|
| **Target firm website** | Name, title, office, bio, practice areas, education, deals, news | Sitemap + requests/BS4 scraping |
| **Apify Google Search** | LinkedIn profile URLs | `apify/google-search-scraper` — `site:linkedin.com/in` queries |
| **Apollo** | Verified work email, personal email, phone | `apollo_people_match` MCP tool — name + company + LinkedIn URL |
| **Apify LinkedIn Scraper** | Full LinkedIn profile data, contact info | `apify/linkedin-profile-scraper` (or similar actor) |
| **Pin.com** | Candidate database, ATS-connected profiles | [PENDING — MCP integration] |
| **Weil/firm news pages** | Deal announcements, awards, thought leadership | Direct scraping of news/insights sections |

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

## Pin.com Integration [PENDING]

**Status:** Messaged Pin team for MCP server URL. They confirmed MCP exists but only showed ATS connection options in the UI.

**What Pin.com adds:**
- Candidate database search by criteria
- ATS-connected candidate profiles
- Potentially pre-enriched contact data

**Next steps:**
1. Get MCP server URL or npm package from Pin team
2. Get API key / auth format
3. Add to `.claude/settings.local.json` as MCP server
4. Build Pin.com search + enrichment into Phase 2

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
