# Signal Library — OutboundOS Launch Plans

The full catalogue of intent signals available for an OutboundOS launch, mapped to the DeliveryOS `signals.type` enum, ranked by intent tier, with the **exact live-data source** for backing each one and the copy angle it implies.

**Rule (from SKILL.md B1):** never propose a signal without a real, live-pulled count from the client's TAM. The "Live data source" column tells you how to get that number.

**Data source: Clay + Prospeo only — NEVER Apollo** (dropped from the stack). Clay is the source of truth for TAM, signals, and market counts (native enrichments for job postings, funding, headcount, job changes); Prospeo (15k free credits/mo) is the email/mobile enrichment layer + filtered prospecting. See `memory/feedback_data_source_clay_prospeo_not_apollo.md`.

---

## The 10 signals (DeliveryOS enum → tier → sourcing → angle)

### Tier 1 — Active hiring (hottest: pain is live right now)

**`open_jobs`** — Company posting 2+ roles in the client's target function.
- *Means:* growing, recruitment pain is active, budget is allocated.
- *Live data source:* Clay LinkedIn Jobs / job-board enrichment across the TAM. Count = # companies in TAM with ≥2 open target-function roles.
- *Copy angle:* "Saw you're hiring [N] [role] — most agencies will pitch you on the role. I want to show you the system behind filling them faster."

**`backfill`** — Same role re-posted after 60+ days (can't fill it).
- *Means:* frustrated, current approach is failing, open to a different one.
- *Live data source:* LinkedIn Jobs posting history via Clay; days-since-first-posted column.
- *Copy angle:* "[Role] has been open since [month] — that's usually a sourcing problem, not a market problem."

**`career_page`** — Active careers page with multiple live roles.
- *Means:* hiring at volume, often without enough TA capacity.
- *Live data source:* Apify careers-page scrape / Clay career-page enrichment. Count = # TAM companies with live roles.
- *Copy angle:* volume-hiring efficiency angle.

### Tier 2 — Leadership / org change (very hot: new mandate + budget)

**`90d_job_change`** — New decision-maker (C-suite / Head of function) in last 90 days.
- *Means:* new mandate, fresh budget cycle, old vendor loyalties don't apply.
- *Live data source:* Clay LinkedIn/Sales Nav job-change enrichment (or Prospeo Search Person) filtered to changed-jobs in 90d at TAM companies.
- *Copy angle:* "Congrats on the [title] role — first 90 days is when most leaders rebuild their hiring engine."

**`no_internal_hr`** — Company in ICP range with no internal TA/HR leader.
- *Means:* no one owns hiring internally — they outsource by default.
- *Live data source:* Clay — TAM companies with zero TA/Recruiter/People titles (HR-headcount enrichment); or Prospeo Search Company.
- *Copy angle:* "You're at [headcount] with no internal recruiter — that's exactly when hiring quietly stalls."

### Tier 3 — Growth (warm: pain is coming)

**`marketing_spend`** — Funding / revenue / expansion / ad-spend growth.
- *Means:* capital to spend, pressure to grow headcount.
- *Live data source:* Clay Crunchbase / funding enrichment (funding, headcount growth) across the TAM.
- *Copy angle:* "Post-raise, the bottleneck is always hiring speed, not budget."

**`alumni`** — Alumni pools of target/competitor companies.
- *Means:* warm, credible network effect; good for trust-led outreach.
- *Live data source:* LinkedIn alumni filter via Clay / HeyReach.
- *Copy angle:* shared-background warm opener.

### Tier 4 — Warm-network & weak (volume / LinkedIn-led)

**`1st_conn`** — Client's existing 1st-degree LinkedIn connections.
- *Live data source:* HeyReach / client's LinkedIn export. Highest reply rate — run first.
- *Copy angle:* re-engagement, no cold framing.

**`2nd_conn`** — 2nd-degree network (shared connections).
- *Live data source:* HeyReach 2nd-degree targeting.
- *Copy angle:* mutual-connection warm intro.

**`recent_post`** — Prospect active on LinkedIn recently.
- *Means:* reachable + receptive on LinkedIn.
- *Live data source:* LinkedIn activity enrichment.
- *Copy angle:* comment-then-DM, reference their post.

---

## Selecting the 3–4 for a launch

1. Always include **at least one Tier 1** signal — it carries the launch.
2. Add **one Tier 2** if the TAM has the volume (check the live count).
3. Add **`1st_conn`** almost always — it's the fastest path to early positive replies (feeds the P3 guarantee).
4. Pick the 4th by where the live data is strongest in *this* niche.
5. Reject any signal whose live TAM count is too thin to feed P1 volume (2,000 email + 500 LI) — say so explicitly in the internal doc rather than padding.

---

## Mapping to DeliveryOS

Each chosen signal becomes a `signals` row (`type` = the enum above, `status` = `building` → `live`, `clay_table_ref` = the Clay table built for it). Leads sourced from each signal carry `signal_id` so per-signal performance is tracked in the `campaigns` / `targets` rollups.

---

## Signal Enrichment & Copy Columns (build phase — do AFTER TAM is scored & approved)

**Principle:** every signal gets its own **logic + enrichment columns** in Clay, and the enrichment output feeds **copy variables**. The signal isn't just "is this true Y/N" — it captures the *specific detail* that makes the first line land. Build one enrichment block per signal; map each output column to a copy merge field.

**Canonical example — `open_jobs`:**
- Pull open roles from **multiple job boards**, not one: LinkedIn Jobs, Indeed, Google Jobs, the company careers page, and ATS feeds (Greenhouse / Lever / Ashby / Workday).
- Dedupe roles across boards (same role posted in 3 places = one row).
- Capture per role: `open_role` (title), **`job_source`** (which board it was found on), `date_posted`, `job_url`.
- **Copy variable:** `"we saw you posted {{open_role}} on {{job_source}}"` → e.g. "we saw you posted a Senior GNC Engineer role on Greenhouse." The `job_source` is what makes it feel hand-found, not scraped.

### Open Jobs — multi-platform pipeline (3 linked tables, NOT one)
Jobs, accounts, and contacts are three different grains (one company → many jobs → many contacts), so the open-jobs signal spans **three linked Clay tables**:

1. **Jobs feed table** — **Apify** actors scrape open roles across MULTIPLE platforms (LinkedIn Jobs, Indeed, Google Jobs, + ATS boards: Greenhouse / Lever / Ashby / Workday). One row per posting. Capture: company, company domain, role title, **platform/source**, date posted, JD link. Filter to the client's target roles.
2. **Match to TAM** — Clay lookup joins the Jobs table to the **Accounts (TAM) table** on normalized domain. Keep jobs at in-TAM companies. **Bonus signal:** a defense company hiring a target role that is NOT in the TAM = a TAM-growth candidate → route to review, don't discard.
3. **Decision-maker / Contacts table** — for matched companies, find the DM for that role (hiring manager / VP Eng / Head of Talent / founder at Series A) via **Prospeo** → one row per contact → sequence in Instantly + HeyReach.

Copy keyed to the trigger + source: `"saw you posted {role} on {job_source}"`. Refresh the Jobs feed on a schedule (jobs are perishable).

**Persistent cache (NON-NEGOTIABLE — protects credits):** maintain two growing tables that are the source of truth and the enrichment cache:
- **TAM_Companies** (keyed by normalised domain) — every company we ever touch. New job → look up its domain here FIRST; if present, reuse the enrichment, never re-enrich. If absent (and it passes defense-qualification), enrich once and ADD it (this is how the TAM grows from jobs).
- **TAM_People** (keyed by LinkedIn URL / verified email) — every decision-maker ever enriched. Before any Prospeo/Clay person lookup, check here; if present, reuse — never pay to enrich the same person twice.

**Deduplication (3 levels — all required):**
1. **Company:** canonical key = normalised domain (strip www/subdomain/protocol; resolve careers.x.com → x.com; handle parent vs subsidiary). Match on domain, never fuzzy company name.
2. **Same job across platforms:** collapse to ONE job record keyed by `domain + normalised_role_title`; keep an array of `job_source`s.
3. **Same job, same platform, different location:** collapse by `domain + normalised_role_title`; aggregate locations into one record (don't create N leads for N cities). Normalise titles ("Sr GNC Eng" = "Senior Guidance Navigation & Control Engineer") before comparing. Track `first_seen` + a job hash so reposts don't re-trigger or re-enrich.

**Pattern for every other signal** (build each later):
| Signal | Enrichment columns to build | Copy variable(s) |
|--------|------------------------------|------------------|
| `open_jobs` | open_role, **job_source**, date_posted, job_url | "you posted {{open_role}} on {{job_source}}" |
| `backfill` / `90d_job_change` | departed_name, departed_role, departure_date, company | "noticed {{departed_name}} recently left {{company}}" |
| `marketing_spend` (funding/stealth) | round, amount, date, investors, stealth_exit_date | "saw {{company}} just raised {{round}}" / "just came out of stealth" |
| `1st_conn` / `recent_post` | connection_degree, last_post_topic, engagement_type | "saw you {{engagement_type}} my post on {{last_post_topic}}" |

**Build order:** TAM (Clay table) → score against ICP → Adrian approves → THEN build these per-signal enrichment blocks. Never wire signals before the TAM is locked. Each block's source column (e.g. `job_source`) must survive through to the copy layer — design the Clay → copy mapping at build time, not after.
