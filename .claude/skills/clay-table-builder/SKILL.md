# Skill: Clay Table Builder (Zero-Credit)

Build fully-populated Clay tables by prompting in Claude Code — **without spending Clay credits on enrichment**. Clay is the orchestration surface and the client-facing deliverable (sourcing + final table). All enrichment runs on Reyhan's own API accounts: **Exa** (research/verification), **Apollo** (firmographics, funding dates, job postings, email fallback), **Prospeo** (primary email finder). Claude Code is the pipeline engine: gates, ratios, judgment, outreach copy.

Invoke when Reyhan says: "build a Clay table for X", "prompt-to-table", "zero-credit Clay build", or describes an ICP + gates + enrichment columns and wants the result *inside* Clay.

Proven end-to-end 2026-07-15 (the "TA Ratio Signal — SF SaaS" build: 10 companies, 3 gates, decision-makers + verified emails; the all-Clay version of the same pipeline cost 125 credits — this skill's routing takes that to 0).

---

## Locked Rules

### A. Credit policy (the point of this skill)
- A1. **Zero Clay credits by default.** Never start Clay-managed routine runs (`clay routines runs start function:t_*`), never add enrichment/AI/Claygent columns inside a Clay table, never trigger in-app waterfalls. All of these meter credits.
- A2. Free Clay surface only: `clay search filters-mode` (companies + people), `clay tables list/get/query` (reads), `clay credits`, and table creation via browser CSV import.
- A3. Run `clay credits` at the start AND end of every build. Report the delta in the final message. Target: **0.0**. Any nonzero delta must be explained.
- A4. If a step genuinely needs a Clay-only enrichment, STOP and ask Reyhan first — never spend silently (flag blockers, never work around).

### B. Data routing (which tool for what)
- B1. **Sourcing** (companies by ICP), **title-count searches** (e.g. count TA/recruiting staff at a domain), and **decision-maker discovery** (Founder/CEO/Head of X by domain) → `clay search filters-mode` — free, no credits.
- B2. **Firmographics, exact headcount, funding date/stage/amount, open job postings** → Apollo API via `apollo.py` in this skill folder (~1 Apollo credit per org enrich / job-postings call).
- B3. **News, funding verification, research for outreach angles** → Exa via `exa.py` (cents per call) and/or free WebSearch.
- B4. **Emails** → Prospeo FIRST (`../prospeo/prospeo.py`, `enrich_person` with `only_verified_email` when list quality matters), Apollo `people_match` as fallback. Never reveal personal emails or phone numbers unless Reyhan asks.
- B5. Funding recency that gates a keep/kill decision must be cross-checked against a second source (Apollo date + Exa/news) — Clay's own funding data has no date, and single-source dates are frequently stale.

### C. Pipeline order (gate-ordered spend)
- C1. Scope with Reyhan before any paid call: ICP, row target, gate definitions, sort order. Confirm the row count — enrichment cost scales linearly with rows carried past each gate.
- C2. Order: source (free) → Gate 1 from free search data (industry/HQ/size + judgment on descriptions) → Apollo enrich **survivors only** (bulk, 10 domains/call) → Gate 2 (growth) → ratio/count searches (free) → Gate 3 → decision-makers (free) → emails **last, qualifiers only** → outreach angles (Claude + Exa facts).
- C3. Compute gates locally (jq/python), never as paid enrichment columns.
- C4. Watch for aggregator false positives: a job platform's "open jobs" count may be its listings, not its own hiring (real case: Jobright showed 6,717). Use Apollo's own-postings endpoint and sanity-check outliers.

### D. CSV & table conventions
- D1. Person names split into **First Name + Last Name** columns (CORE rule — never a single Name column).
- D2. Keep disqualified rows in the table with the gate-fail reason as an audit trail, unless Reyhan says drop them. Enrichment columns stay empty for disqualified rows.
- D3. Apply the requested sort in the CSV row order BEFORE import — Clay preserves import order and the UI sort is view-level only.
- D4. Name the CSV file exactly what the table should be called — Clay names the imported table after the file. Rename the workbook to match.
- D5. Every gate column states PASS/FAIL **plus the reason** ("PASS — raised <18mo + 11 open roles"), never a bare boolean.

### E. Browser import runbook (table creation is UI-only)
The Clay CLI/API cannot create tables — CSV import through the app is the only programmatic-ish path. Proven sequence (claude-in-chrome):
- E1. `tabs_context_mcp` → new tab → `app.clay.com`. Screenshots may render BLANK while the DOM is fine — drive with `read_page` / `find` refs, not pixels. Screenshots start working after the first interactions.
- E2. Home → **New** → **Workbook**. Rename via the title textbox (cmd+a, type, Return). Then **Add** → **Import from CSV** (use `find` — the picker buttons are unlabeled in the a11y tree).
- E3. `file_upload` may reject host paths ("no longer accepts host filesystem paths"). Workaround: `javascript_tool` — create a `File` from the CSV string, attach via `DataTransfer` to `input[type=file]`, dispatch `input` + `change`. The tool result may return `[BLOCKED: …]` — that's the response sanitizer, not a failure; verify attachment via `read_page` (the input shows `C:\fakepath\<filename>`).
- E4. Before "Complete import": delimiter = Comma, "First row contains column names" = checked (verify via JS: `document.querySelectorAll('input[type=checkbox]')[0].checked`).
- E5. Verify success: URL now contains `/tables/t_…`, page text shows `n/n rows`. Screenshot for Reyhan and report the full table URL.
- E6. `clay tables get` may return `auth_forbidden` (observability API is Enterprise-only) — that is NOT a failure; the browser check is the verification.

### F. Reporting (final message every run)
- F1. Table URL + screenshot.
- F2. Funnel table: sourced → Gate 1 → Gate 2 → Gate 3 → enriched, with kill reasons.
- F3. Spend: Clay credit delta (must be 0), Apollo credits used, Prospeo credits used, Exa calls. Never invent per-credit prices.

---

## Helpers in this folder

| File | What it does |
|---|---|
| `apollo.py` | Apollo API client (reads `APOLLO_API_KEY` from parent `.env`). Commands: `org <domain>`, `bulk <d1,d2,…>`, `jobs <domain>`, `count <domain> "<title1,title2>"`, `match <first> <last> --domain <d>` |
| `exa.py` | Exa API client (reads `EXA_API_KEY`). Commands: `search "<query>" [-n 5] [--category news]`, `answer "<question>"` |
| `../prospeo/prospeo.py` | Existing Prospeo client (`PROSPEO_API_KEY`) — primary email finder |

All three walk up parent directories to find `.env` (project root), mirroring the stardex pattern. Run with `python3`.

---

## Clay free-surface cheat sheet

```bash
# Discover filters
clay search filters-mode fields --source-type companies   # or people

# Source companies (returns searchId; page with `run`)
clay search filters-mode create --source-type companies --filters '{
  "location_cities_include": ["San Francisco", "Palo Alto"],
  "location_states_include": ["California"],
  "location_headquarters_only": true,
  "minimum_member_count": 30, "maximum_member_count": 150,
  "industries": ["Software Development", "Technology, Information and Internet"],
  "types": ["Privately Held"],
  "funding_amounts": ["5m_10m", "10m_25m", "25m_50m", "50m_100m"]
}'
clay search filters-mode run <searchId> --limit 50

# Count people by title at a domain (free ratio numerator)
clay search filters-mode create --source-type people --filters \
  '{"company_identifier":["acme.com"],"job_title_keywords":["talent acquisition","recruiter","sourcer","people operations","human resources"]}'
# → run it, count .data, BUT filter client-side on latest_experience_title
#   (keyword match can hit past roles — real case: a co-founder matched on an old title)

# Decision-makers (free)
# job_title_keywords: ["founder","chief executive officer","CEO","head of talent","head of people"]
# People records: .name, .latest_experience_title, .url (LinkedIn), .structured_location

# Credit check (start + end)
clay credits
```

---

## Notes & known sharp edges

- People search returns board members/investors as "at company" — title-filter client-side on `latest_experience_title`.
- Clay search headcount is a LinkedIn range; Apollo `estimated_num_employees` is the exact denominator for ratios.
- Headcount *growth* (6–12mo delta) has no zero-cost source; growth gates should be OR-logic (recent raise OR active hiring) unless Reyhan approves a paid growth provider.
- Apollo renamed some search params in 2025 (`q_organization_domains` → `q_organization_domains_list`); if a people search returns 0 unexpectedly, check the current docs before concluding.
- Import CSVs are static — if Reyhan wants the table to keep updating inside Clay, that's Clay-metered territory: flag it and get approval first.
