# OutboundOS — RecruiterGTM (own-sales engine)

RecruiterGTM's OWN end-to-end outbound engine. Maps our niche's total addressable market, verifies it, and every week surfaces ~200 fresh intent-matched leads → enriches → personalises → loads to HeyReach (LinkedIn) + Instantly (email) as **drafts** → Reyhan spot-checks + approves → campaigns auto-activate. Reyhan's weekly job ≈ 10 minutes.

Client campaigns stay in `outbound-os-setup` / `gtm-engine`. This skill is only for selling RecruiterGTM (main offer + talent division).

**Engine stack (reused, do not rebuild):** `outbound-os-claude` (pipeline) · `list-quality-scorecard` (QA gate) · `email-deliverability` (send preflight) · `personalization-subagent-pattern` (final mile) · `copy-engine` + `humanizer` (all copy) · `email-writer` (approval msgs). Domain-verify rules D1–D4: `references/sops/tam-building-sop.md`.

**Approved build plan:** `~/.claude/plans/cosmic-booping-bear.md`.
**Comms channel:** Slack **#recruitergtm-outboundsales** (`C0BJE6BR5KP`) — every batch approval, spot-check, and question goes here. German-market comms: **#recruitergtm-german-division** (`C0BMUJDEHQE`).

---

## The 3 sub-engines (angles on one pipeline)

| # | Sub-engine | Offer / angle | Market | ICP size | Owner |
|---|-----------|---------------|--------|----------|-------|
| 1 | **EN — main offer** | RecruiterGTM: community / systems group / DFY setups | US · UK · CA · AU | Solo–20 | Daniyal (copy) |
| 2 | **DE — main offer** | Same offer, German copy (Patrick-as-peer) | DACH | Solo–10 | Shmookh + Patrick |
| 3 | **Talent division** | "RecruiterGTM Academy" — offshore GTME / recruiter placement | EN (broader) | Broader | Noroze |

Build order: **EN first → DE → Talent.** One sub-engine reaches "live" before the next starts.

**Data home:** `projects/rgtm-outbound-funnel/` — `plan`/registry (`lists.md`, `angles.md`, `results.md`), `sources.md` (all harvest links), and `data/<sub-engine>/` (see that folder's README).

---

## Locked Rules

### A. Ownership & approvals
- A1. **Nothing sends without Reyhan's approval.** Every batch loads as a DRAFT; Reyhan approves the batch + angle in #recruitergtm-outboundsales; only then does the routine activate the campaign (CORE: never auto-send).
- A2. Booked calls + replies land in **Attio** (source of truth; dedup before creating).
- A3. Owners: Daniyal = EN copy + sourcing/automation infra; Shmookh + Patrick = DE; Noroze = Talent. Reyhan approves everything.

### B. TAM & lists
- B1. **No people until a company passes the gate** — domain-verify (D1), ICP fit, size band via `employeeCountRange` (D3/D4), set-level mismatch audit reported (D2). Verify by DOMAIN, never name.
- B2. **Harvest, don't rebuild** — pull existing Clay/Drive TAM (see `sources.md`), dedupe by root domain, then gate. No top-up sourcing unless Reyhan asks.
- B3. Every weekly batch passes `list-quality-scorecard` at **Grade ≥ B** before load. Below bar = fix or kill.
- B4. **Full pre-enrich (heavy work up front, Reyhan 2026-08-13).** After the company gate, bulk-enrich people for the ENTIRE verified TAM into a master pool, so weekly runs just skim the top 200–300 by intent. Two safeguards are mandatory: (a) **enrich via waterfall Prospeo (free ~15k/mo) → Apollo** to minimise paid credits; (b) **re-verify at send-time** — the Apify live current-company check + email re-verify runs each week on only the batch being sent, catching job-changers before contact (defeats data decay).
- B5. Never re-work a person — dedup every batch against `data/<sub-engine>/ledger.csv` (LinkedIn URL).
- B6. **Founder / top-exec only (Reyhan 2026-08-13).** One contact per company: FOUNDER / OWNER / CEO / MD. Smaller agencies → the founder is the buyer. No Directors / Heads / mid-level; if no top exec found, skip the company (never substitute down).
- B9. **TAM dashboard uses the April "Target Account List" format (Reyhan 2026-08-19).** The RGTM-TAM-Dashboard.xlsx layout is locked to April's dashboard design — canonical builder: `data/en/build_dashboard.py`. Structure: **Overview** (brand header · 4-stat hero row · "Your ICP" block · Tiers table with score bands · Data Quality & Accuracy report showing the full funnel · "how it was verified" narrative · column guide) → **Spot-Check Guide** (5-step ICP check + green good-examples / red cut-by-the-gate) → **Tier A — Start Here** → **All Founders** (ranked A→B). Palette: navy `1f2d3d` · teal `1f6feb` · green `0f7a4d` · gold `9a5b00` · grey `5a6473`; row tints green `E7F5EE` (A) / blue `EEF3FB` (B) / red `FBECEC`. Every stat computed live from the pool, never asserted (C3). Clone this format for DE + Talent dashboards.
- B8. **All Drive-facing outbound files live in the OutboundOS Drive folder (Reyhan 2026-08-19).** Every TAM dashboard, weekly-leads sheet, and any other Drive deliverable for this engine goes in `OutboundOS` (`1-90qsbZ1tyd4qV6EMyut22PaqHbcvhAB`) — build/output there or move there straight after generating; never leave them loose in the synced `data/en/` mirror or a Drive root. Pipeline CSVs/scripts stay in the git project; this rule is for the Drive-shared xlsx deliverables. Clean up any duplicate copies.
- B7. **Never cold-outreach Reyhan's 1st-degree connections — both channels (Reyhan 2026-08-15).** They're warm; cold outreach burns the relationship + sender reputation. Enforcement is layered: (a) **LinkedIn** — every HeyReach sequence starts `CHECK_IS_CONNECTION`; the already-connected branch goes straight to `END` (runtime-proof, covers future connections too). (b) **Email** — Instantly has no connection check, so every batch is deduped by LinkedIn profile URL against the maintained connection list before load; matches are dropped. (c) **TAM scrub** — the whole verified pool is pre-scrubbed against 1st connections so a connection never resurfaces. Connection list: `projects/rgtm-outbound-funnel/connections/1st-degree-urls.txt` (pulled from HeyReach `get_my_network_for_sender` for account 13334, ~11.7k; refresh monthly). TAM exclusions: `data/en/tam-connection-exclusions.txt`. First scrub 2026-08-15 removed 5 from Week-1 + 23 from the launch-ready pool (1,195→1,172).

### C. Copy
- C1. Master angle per sub-engine in `angles.md`; A/B variants derive from it; promote/kill on **reply data only**.
- C2. Every line runs `copy-engine` + `humanizer` before load. Banned phrases apply; preferred CTA "Lmk if that's of interest"; msg 1 = interest check, call ask later.
- C3. **Stats must be verified** — no unconfirmed number ships (see the PENDING list in `angles.md`: "70+ agencies", "€38,500", "2M impressions", placement prices). Client results = attributed testimonials only, never promises (CORE).
- C4. Talent (sub-engine 3) is **never pitched without ≥2 real sample candidates + video intros** ready (CORE).
- C5. **Fixed subject lines per Play — no `{{subj}}` merge field (Reyhan 2026-08-17).** Play 1 `your back office` · Play 2 `your best candidates` · Play 3 `Exclusive Invite`. A niche merge field in the subject risks a blank/broken subject on generic-fallback leads; keep subjects hard-coded (2–3 words, lowercase, internal tone). New Plays each get one fixed line. Custom-field VALUES must be trimmed (no leading/trailing spaces) so body merge fields never render a double space.
- C6. **Follow-ups are non-apologetic (Reyhan 2026-08-17).** Lead with the core problem the Play solves, then offer the proof (2-min recording / walkthrough) as a soft yes/no. Never apology openers ("no worries if not", "all good if not", "no stress") or self-shrinking closes ("no strings", "no call needed", "my door is open"). → [[feedback_non_apologetic_followups]]
- C7. **Email spacing (Reyhan 2026-08-17).** Blank line after the greeting, a blank line between every paragraph, and a two-line sign-off (`Best,` then `Reyhan`) — never one block. Instantly HTML: `<div><br /></div>` between paragraphs + `<div>Best,</div><div>Reyhan</div>`. → [[feedback_email_spacing_format]]

### D. Channels & volume
- D1. HeyReach = LinkedIn steps; Instantly = email steps. Multichannel per approved sequence.
- D2. **20–30 sends/day/channel** inside warmup caps. `email-deliverability` preflight before any Instantly ramp. Never cold-send from `recruitergtm.com` — cold domains only (already warmed).
- D3. **Instantly custom variables MUST be nested under `custom_variables`** in the lead object (`{email, first_name, custom_variables:{forrec,leaders,subj,…}}`) — top-level custom fields are silently dropped and render blank. HeyReach uses native `customUserFields` + a `fallbackMessage` (degrades to generic, never blank). Always spot-check the Instantly preview after a load. (Bug caught + fixed 2026-08-15.)

### E. The learning loop
- E1. On each batch: log sends / replies / positive / calls per angle in `results.md` + `data/<sub-engine>/learnings.jsonl`.
- E2. Winning messages → copy-engine swipe file with their reply rate. Numbers decide, not opinion.

---

## The pipeline
Full step detail + AI sub-agent roster: **`pipeline.md`**. Two stages:

**Stage 1 — one-time heavy build (per market):** harvest Clay/Drive → company gate → find the founder/top-exec per company → **bulk pre-enrich the whole verified TAM** (Prospeo→Apollo waterfall) into `data/<sub-engine>/pool.csv`.

**Stage 2 — weekly skim (`run`):** refresh intent across the pool → rank → **take top 200–300** → dedup (`ledger.csv`) → **drop any 1st-degree connection (B7)** by profile-URL match against `connections/1st-degree-urls.txt` → **send-time re-verify only that batch** (Apify current-company + email re-verify) → qualify → personalise (copy-engine + humanizer) → scorecard ≥ B → load as **drafts** into the 6 standing campaigns (HeyReach + Instantly) → Slack spot-check → approve → activate → log (`results.md`, `learnings.jsonl`, Attio).

---

## Commands — `/rgtm-outbound [command]`
- **`status`** — active sub-engine, TAM/verify state, last batch, Apollo credit balance.
- **`harvest [en|de|talent]`** — pull the Clay/Drive TAM (`sources.md`) → `tam-raw.csv`, dedupe by domain.
- **`verify-tam [en|de|talent]`** — run the company gate → `tam-verified.csv` + mismatch-rate report.
- **`run [en|de|talent]`** — execute the weekly pipeline → drafts loaded + Slack spot-check. (This is what the cron calls.)
- **`copy [en|de|talent]`** — (re)generate the sequence from the master angle via copy-engine.
- **`approve [batch]`** — after Reyhan's OK: activate the drafted campaigns.
- **`review`** — weekly numbers: update `results.md` + swipe file; promote/kill angles.

---

## Automation / cron — LIVE (wired 2026-08-18)
**Routine:** `RGTM Outbound · Weekly Batch Prep` (`trig_01PxGbPXqMW5VZn26V6eTt7E`) — cloud routine, **Mon 08:00 UTC (09:00 UK / BST)**, model sonnet-5, repo `ea`, Slack connector attached.

**Why it's prepare-only:** a cloud routine can only reach MCPs in Reyhan's **claude.ai connector registry** (Slack, Apollo, Attio, Pulse, …). **HeyReach + Instantly are LOCAL MCPs** (project `.mcp.json`) — not in that registry — so the cron CANNOT load or send. It PREPARES + NOTIFIES; the push happens from a local session via MCP. (The distinction is "connected to a local session" ≠ "registered as a claude.ai connector".)

### The weekly handoff loop
1. **Cron (cloud)** runs `data/en/weekly_prep.py` → next 200 net-new (pool − `ledger.csv` − 1st-degree connections), 3-Play split (`i%3`), niche custom fields, scorecard → writes loader files to `data/en/weekly/week-<date>/` (`he_play1-3.json`, `in_play1-3.json`, `weekly-leads.csv`) → **git commit + push** (so the batch persists on the remote) → **Slack post** to #recruitergtm-outboundsales (counts, scorecard grade, 5 samples, path, "push via MCP" reminder). **Sends nothing.**
2. **Reyhan** forwards the Slack ping / says "push this week's batch".
3. **Local session (Claude)** — `git pull` FIRST (the cron's folder is on the remote, not this working copy) → read `weekly/week-<date>/` → load the 6 standing campaigns via HeyReach + Instantly MCP as **drafts** (never new campaigns) → Slack spot-check → Reyhan approves → activate.
4. **Ledger** — append the batch's LinkedIn URLs to `ledger.csv` **only AFTER load**, never at prep time. If a week is skipped nothing breaks and no one is double-messaged: the batch waits, and the next cron re-selects the same net-new set until it's loaded (`weekly_prep.py` does NOT touch the ledger).

### To make it fully auto (removes the manual push)
Add HeyReach + Instantly as **claude.ai custom connectors** (their HTTP MCP URLs, keys embedded in URL/header — key-based auth runs fine headless). Once they're in the registry, attach them to the routine and the cron loads the drafts itself; the Slack message becomes "loaded, ready to approve." Apify send-time re-verify stays out of the cron (no cloud key) — rely on the pool's build-time OutboundOS verification, or Daniyal exposes it via API/n8n.

- **Headless risk:** key-based MCPs (HeyReach/Instantly URL keys) run fine headless; interactive-OAuth connectors flake. Clay OAuth is fragile — prefer Apollo for any cloud people-discovery.
- Clone the routine per market as DE + Talent go live.

---

## Current status (2026-08-15)
**EN TAM built + verified.** Scored TAM = **35,305** companies. Deep-enriched + OutboundOS-verification-gated so far: **2,595 founders** (2,088 role-verified, **1,195 launch-ready** = verified + email). Two Drive files live in folder `1-90qsbZ1tyd4qV6EMyut22PaqHbcvhAB`: `RGTM-TAM-Dashboard.xlsx` + `RGTM-Weekly-Leads-Week1.xlsx` (200 leads, 3 plays, sharp person-first niches). Copy: 3 plays (Claude Code · candidate-correlation engine · one-stop-shop SaaS), 2 LinkedIn + 3 email each, through copy-engine + humanizer + linter.

**⏳ QUEUED — full-TAM deep enrich (Reyhan 2026-08-15):** run the deep enrich + OutboundOS verification gate on the **remaining ~30k** of the 35,305 TAM. Deferred until **Apify usage renews (cycle resets the 16th monthly; next reset 2026-08-16).** Actual rate so far ≈ $0.03/company attempted → full remainder ≈ **~$900 Apify**, i.e. ~5 monthly $175 cycles unless the limit is raised. Chip through the next tranche each cycle until the whole TAM is verified. Enrich scripts are resumable + budget-guarded (`.attempted` sidecars).

**▶️ NOW:** launch the first weekly batches from the 1,195 launch-ready — Reyhan's LinkedIn (HeyReach) + email (Instantly) only, ~25/day, as DRAFTS → Reyhan approves → activate.

### Standing campaigns (built 2026-08-15 — every weekly batch pushes into THESE, never new ones)
Sender: LinkedIn = Reyhan's account `13334` (25 connects/day, auto-throttled across all 3). Email = 10 warmed `joinrecruitergtm.com` inboxes (~20/day). Sequences: LinkedIn = blank connect → msg1 → msg2 (4d); Email = 3 touches (0/3/4d). Per-lead niche via custom fields (`forrec`/`leaders`/`small`/`few`/`subj`); generics fall back to "for recruiters".

| Play | HeyReach campaign | HeyReach list | Instantly campaign |
|------|------------------|---------------|--------------------|
| 1 · Claude Code | `552883` | `864842` | `d9f61372-42f5-496c-bf22-114fd76b0f29` |
| 2 · Correlation Engine | `552884` | `864844` | `80269f22-32f7-480e-adfe-00f051cbc7e3` |
| 3 · One-Stop-Shop | `552885` | `864843` | `263659c8-119c-429b-b7f5-a2f05e5db44a` |

Week-1 loaded: 200 leads (67/67/66) on BOTH channels, then scrubbed against Reyhan's 1st-degree connections (B7) → **5 removed = 195 live**. **WENT LIVE 2026-08-17 20:44 UK with copy v2** (fixed subjects C5 · non-apologetic follow-ups C6 · fixed email spacing C7 · Play 3 "built on the RecruiterGTM framework → tailored experience" + unicorn/co-creator framing) — all 6 campaigns IN_PROGRESS/active on a **UK schedule (08:00–16:00 Mon–Fri**; HeyReach Europe/London, Instantly Europe/Isle_of_Man). Batch-1's 195 written to `data/en/ledger.csv` so the weekly run pulls net-new.

### Weekly routine — NOT yet scheduled (wire AFTER first live batch)
The `run` logic is defined but **no cron exists yet.** Once Reyhan confirms the first batch is live and clean, wire a Claude cloud routine (Mon ~08:00 UK) that: re-scans intent across the verified pool → takes next ~200 not in `ledger.csv` → send-time re-verify + niche → personalise → `add_leads_to_list_v2` (HeyReach) + `add_leads_to_campaign_or_list_bulk` (Instantly) into the 6 standing campaigns as drafts → Slack spot-check in #recruitergtm-outboundsales. Dedup ledger must be written per batch (not yet populated).

DE + Talent sub-engines queued after EN is validated live.
