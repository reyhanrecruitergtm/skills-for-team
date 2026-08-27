# OutboundOS-RGTM — Pipeline & AI Agent Roster

Two stages: a **one-time heavy build** per market (verify + full pre-enrich into a master pool), then a **light weekly skim** of the top 200–300 by intent. Agents are spawned inline (Task/Agent) during a run — no persistent API keys, runs on the Claude plan (`personalization-subagent-pattern`). Fan out in parallel; merge by `lead_id`.

**Target contact (locked, Reyhan 2026-08-13):** FOUNDER / OWNER / CEO / MANAGING DIRECTOR only — the highest-level exec, **one per company**. Smaller agencies → the founder is the buyer. Do NOT pull Directors / Heads / mid-level. If no founder/owner/CEO/MD is identifiable, **skip the company** — never substitute a lower title.

---

## STAGE 1 — One-time heavy build (per market)

### Agent: `tam-harvester`
- **In:** Clay table ids + Drive file ids in `../../projects/rgtm-outbound-funnel/sources.md`.
- **Does:** pull each source (Clay MCP / Drive export) → normalise → dedupe by **root domain** → `data/<sub-engine>/tam-raw.csv`.

### Agent: `company-gate` (fan out ~16 companies/agent, parallel)
The "good fit" check — the OutboundOS verification gate (domain + LinkedIn URL + live current-role). **No people until this passes.**
- Per company: (1) resolve website + LinkedIn; (2) **domain-verify (D1)** — matched record's website root-domain == target, else reject; (3) ICP fit — active recruitment agency, live site + LinkedIn, niche captured; (4) size band via Apify `harvestapi/linkedin-company` `employeeCountRange` (≤20 EN / ≤10 DE), **verified not asserted (D3/D4)**.
- **Out:** `data/<sub-engine>/tam-verified.csv` (`Verified Yes/No`). Report the **set-level domain-vs-website mismatch rate (D2)** to #recruitergtm-outboundsales.

### Agent: `founder-finder` (fan out ~16 companies/agent, parallel)
- One record/company: the **founder / owner / top exec**. Apollo people-search via **MCP** (`apollo_mixed_people_api_search`, batch ~13 domains/call) — free, no lead credits; Clay fallback.
- **Filter (tuned batch-1, 2026-08-13): do NOT over-constrain seniority.** Small-agency owners title themselves "Managing Partner / Managing Member / Principal / Director / Head of" — a strict `owner/founder/c_suite` seniority filter cut hit-rate to ~27%. Use broad titles (Founder, Co-Founder, Owner, CEO, Managing Director, Managing Partner, Managing Member, Founding/Managing Principal, President, Partner, Director, Head of), `include_similar_titles: true`, **no** hard seniority filter; then pick the single most owner-like title per company (Founder/Owner/CEO/Managing Partner > Director > Head of). Skip only if truly none.
- **Infra note:** the OAuth'd Apollo account (via MCP) has the data; the `.env APOLLO_API_KEY` returned 0 (different/empty account). For scripted/headless scale, get the API key for the OAuth account or run founder-find through MCP subagents.

### Agent: `people-enricher` — BULK, one-time (waterfall to protect Apollo credits)
- Reveal email for every founder in `tam-verified.csv` via **Prospeo (free ~15k/mo) → Apollo waterfall** (first-hit-wins; never pay two sources for one email). Spread across Prospeo's monthly free tier where possible before spending Apollo.
- **Out:** `data/<sub-engine>/pool.csv` — the master enriched pool (First Name, Last Name, Title, Company, Domain, LinkedIn URL, Email, base ICP score). This is the ready pool the weekly run skims.
- **Note:** emails are NOT verified-fresh at this stage — freshness is enforced at send-time (Stage 2, step 4). Don't over-verify the whole pool now; it decays.

---

## STAGE 2 — Weekly skim (`run`) — process only the top 200–300

### 1. Agent: `intent-scanner`
Refresh intent across `pool.csv`. Signals ranked hottest-first: `Open role` (agency hiring recruiter/BD/resourcer — Apify `curious_coder/linkedin-jobs-scraper`, **one URL/company**, `f_C=<id>`; never batch ids → HTTP 414) › `New founder` (launched 6–12 mo) › `Growth/funding` › `Warm` (1st-degree + content engagers). Score each pool row; **rank; take the top 200–300.**

### 2. Dedup (deterministic)
Drop anyone already in `data/<sub-engine>/ledger.csv` (LinkedIn URL). Never re-work a person.

### 3. Agent: `send-time-verify` (fan out, parallel) — **runs only on the ~200–300 selected**
Apify `harvestapi/linkedin-profile-scraper` — keep only if **live current company == target** (catches founders who moved on). Re-verify email deliverability (MillionVerifier/ZeroBounce); drop catch-all/role-based. This is the decay safeguard — cheap because it's only the batch being sent, not the whole pool.

### 4. Agent: `qualifier`
Confirm each is a founder/top exec at an ICP-fit company → `qualified`, `icp_score`, `reason`.

### 5. Agents: `personaliser` ×N (personalization-subagent-pattern)
Round 0 sample → owner OK → batches of 10 → lock after 2 clean rounds → scale parallel. `situation_line` + `value_line` grounded in the **actual signal**, in the sub-engine's angle/voice. **Every line through `copy-engine` + `humanizer`.**

### 6. Scorecard gate (deterministic)
`python3 .claude/skills/list-quality-scorecard/score_list.py --list data/<sub-engine>/weekly/week-<n>.csv --titles "Founder,Owner,CEO,Managing Director" ...` → **Grade ≥ B** or fix top 3 + re-run. Names split First/Last.

### 7. Deliverability preflight
`email-deliverability` check; cold domains healthy; enforce **20–30 sends/day/inbox**.

### 8. Agent: `loader`
Push as **DRAFTS**: HeyReach (LinkedIn steps, `mcp__heyreach__*`, do NOT start) + Instantly (email steps, `mcp__instantly__*`, do NOT activate). Multichannel per approved sequence.

### 9. Agent: `spot-check-poster`
Post to #recruitergtm-outboundsales: batch size, per-signal counts, verify/mismatch rates, scorecard grade, 3–5 sample founders + their personalised lines, the angle running. Ping Reyhan (draft via `email-writer`, never auto-send).

### 10. On approval → activate (deterministic)
`/rgtm-outbound approve` → `mcp__heyreach__start_campaign` + `mcp__instantly__activate_campaign`. Approval is the only gate.

### 11. Agent: `logger`
Append per-angle numbers to `results.md` + `learnings.jsonl`; winners → copy-engine swipe file; calls/replies → Attio (dedup first). Move sent people into `ledger.csv`.

---

## Weekly cron handoff (LIVE 2026-08-18) — cloud prepares, local pushes
The Monday routine (`trig_01PxGbPXqMW5VZn26V6eTt7E`, Mon 08:00 UTC) runs the deterministic selection script **`data/en/weekly_prep.py`** in the cloud — it collapses Stage-2 steps 1–7 into a no-API pass (take next 200 net-new = pool − `ledger.csv` − 1st-degree; 3-Play split; niche fields; scorecard) and writes the loader files to `data/en/weekly/week-<date>/`, commits + pushes them, and Slack-pings #recruitergtm-outboundsales. It does **NOT** run steps 8/10 (loader/activate): HeyReach + Instantly are local MCPs, absent from the cloud connector registry, so the cron can't load or send.

**So the pipeline splits by environment:**
- **Cron (cloud):** steps 1–7 via `weekly_prep.py` → save + Slack ping. Skips the Apify send-time re-verify (step 3) — leans on build-time verification — since Apify has no cloud key.
- **Local session (has HeyReach/Instantly MCP):** on Reyhan's "push this week's batch" → `git pull` → step 8 (load 6 standing campaigns as drafts) → step 9 (spot-check) → step 10 (approve → activate) → step 11 (append to `ledger.csv` — ONLY now, never at prep time).

Full loop + the "add claude.ai connectors → fully auto" path: see `SKILL.md` → Automation / cron.

## Model guidance
- Cheap/mechanical (harvest, size-verify, dedup, bulk-enrich, load): Haiku/Sonnet subagents.
- Judgement (company-gate ICP fit, qualifier, personaliser, spot-check): Sonnet.
- Keep heavy fan-out on Haiku/Sonnet for cost; no Fable.
