# Skill: Candidate List

Generates a clean HTML delivery doc presenting a batch of pre-screened candidate profiles to an already-closed client. Use AFTER the placement deal is signed — this is a delivery doc, not a pitch.

## How to Invoke
`/candidate-list` — paste candidates (name + LinkedIn + video + expected comp + CV) for the client.

Per-client scripts live in `projects/generate_[client-slug]_candidates_batch[N].py` and import from this skill's `generate.py`. The generator owns all HTML structure, copy, and styling — the per-client script only supplies a `CFG` dict.

## When to Use This vs. proposal-generator

| Scenario | Skill |
|---|---|
| Client hasn't signed — sales pitch with stats, testimonials, tech stack, pricing | `proposal-generator` |
| Client has signed — delivering candidate shortlist for review | **this skill** |

If you're tempted to add a stats grid, testimonials, "What You Get" section, tech stack, or pricing card → STOP. Wrong skill. This is delivery, not sales.

---

## Locked Rules

### ⚠️ P. Pushing candidates INTO Pulse Talent — use `candidates` + `candidacies`, NEVER `placement_candidates`
When adding a batch to a Pulse Talent job (a `placements` row), the UI reads candidates **through `candidacies`**. `placement_candidates` is a **LEGACY table the UI ignores** — write there and the job shows empty. (This was missed twice on Rachel Biggs, 2026-07-16 — do not repeat.)

Correct procedure, per candidate:
1. **Find or create the candidate** in `candidates` — dedupe by email, then name first (many already exist from `recruiter_applications` intake, often with better emails than the delivery doc). Fields: `name, email, phone, country, linkedin_url, current_title, current_company, video_intro_url, resume_url, notes, salary_expectation`.
2. **Create the `candidacies` row** linking `candidate_id` → `placement_id`, with `stage` (`sourced` / `applied` / `screen` / `final_interview` / `placed` / `rejected`), `sort`, and `source`. **This is the row that makes the candidate appear on the job.**
3. When the client hires someone, set that candidacy's `stage = 'placed'`.

Backfill blank `video_intro_url` / `resume_url` / `linkedin_url` / `salary_expectation` on the existing `candidates` row (COALESCE — never overwrite good data). Full Pulse Talent schema in `pulse-agency/SKILL.md`.

### A. Page structure (locked)
- A1. Page MUST contain exactly four blocks: Header → Hero → Candidates → Footer. Nothing else.
- A2. NEVER include: stats grid, track record copy, testimonials, training curriculum, deliverables/guarantee list, tech stack pills, pricing card, CTA section.
- A3. If a client asks for one of those, push back: that lives in the original proposal. This doc is delivery.

### B. Heading (locked template)
- B1. Hero H1 follows exactly: `[Role Title] Candidates for [Company] — Batch [N]`. No other phrasing.
- B2. Eyebrow above H1 always reads: `RecruiterGTM × [Company]`.

### C. Hero sub (locked structure — talent descriptor is role-aware)
The hero sub template is hardcoded in `generate.py` as `LOCKED_HERO_SUB_TEMPLATE`. Reads:

> *We are continuously engaging and pre-screening qualified **[talent descriptor]** from our active Academy bench and extended network. Below is the latest batch we have lined up for your review. Watch each video and reply with the candidates you would like to interview — let us know if you would like to see additional profiles.*

- C1. The sentence structure is locked — never rewrite it per client.
- C2. **The talent descriptor MUST match the role being placed** (Reyhan, 2026-07-10). Before building any list, check the JD / job type on the Pulse Talent job (`placements.role_title` + `jd`) and set `CFG["talent_descriptor"]` to match: recruiter placements → `"recruitment talent"`, GTM Engineer / ops roles → `"GTM talent"` (the default). Never describe recruiter candidates as GTM talent or vice versa.
- C3. If a client needs framing beyond the descriptor swap, raise it before editing.

### D. Per-candidate fields (required)
Every candidate dict in `CFG["candidates"]` MUST have:
- `initial` — single letter for the avatar circle
- `name` — full display name
- `rank` — `"Option 0N · [Role]"` (e.g. `"Option 01 · GTM Engineer"`)
- `headline` — one-line positioning (broader GTM/ops framing, NOT just recruitment — see rule H)
- `summary` — 4-6 sentence bio with concrete numbers from CV
- `fit` — "Best fit if Kadima clients need someone who..." style
- `video` — embeddable iframe URL. Loom: `https://www.loom.com/embed/{id}`. Tella: `https://www.tella.tv/video/{slug}/embed`. Google Drive: `https://drive.google.com/file/d/{id}/preview`.
- `linkedin` — full LinkedIn profile URL
- `comp` — expected monthly comp (string with `/mo` suffix e.g. `"$3,000/mo"`)

Optional per-candidate fields (rendered only when present, in the meta block):
- `cv` — CV / resume link (Drive `/view`, Google Doc, Canva view URL — opens in a new tab). Renders a "📄 View CV →" button below the comp card. Omit for candidates without a shareable CV.

Generator asserts every required field is present; build will fail loud if any are missing.

### E. Candidate card meta layout (locked design)
At the bottom of every candidate card, two stacked elements:
1. **Expected Monthly Comp stat card** — violet gradient background, uppercase label, big bold dollar amount, money emoji on the right
2. **LinkedIn CTA button** — LinkedIn blue (#0A66C2), inline LinkedIn SVG logo, "View LinkedIn Profile →" centered

Always stacked vertically (gap 12px), never inline. Designed by Reyhan as the "gamified" presentation. Do NOT collapse them back into a single inline row.

### F. Header co-branding
Always RecruiterGTM × [Company] in the site-header brand block. Per `feedback_hero_recruitergtm_x_company.md`.

### G. Output paths (locked)
- `~/Desktop/proposals/[client-slug]-candidates-batch[N].html`
- Mirror at `projects/[client-slug]-candidates-batch[N].html`
- Filenames lowercased, hyphenated.

### H. Candidate description framing (locked 2026-06-08)
- H1. Don't over-index on recruitment-agency work even if the candidate's most recent role was at a recruitment firm. Pull broader GTM / RevOps / SaaS / eCommerce / program management experience from the CV to round them out.
- H2. Headlines should lead with the transferable skill (GTM Engineer, Ops Integrator, RevOps Manager), not the niche of their last employer.
- H3. Keep summaries tight — 4-6 sentences. Front-load the strongest concrete numbers.
- H4. Don't put "recruitment infrastructure" in the headline. Use "outbound", "sales engine", "revenue operations", or the verticals they've worked across.

### I. Video URL format
- I1. Loom share URLs (`/share/`) must be converted to `/embed/` before going into the CFG.
- I2. Tella share URLs must have `/embed` appended (`/video/[slug]/embed`).
- I3. Never paste a raw share URL into the CFG — iframe won't render.
- I4. Google Drive `/view` links must be converted to `/preview` (`https://drive.google.com/file/d/[id]/preview`).

### J. Date discipline
- J1. `cfg["date_str"]` reflects the actual delivery date in `Month D, YYYY` format.
- J2. If a client gets multiple batches, increment `batch_num` and update `date_str`. Never reuse a stale date from a prior batch.

### K. Client-specific required fields
- K1. **Shana & Lincoln Marr (MIR)** — locked 2026-07-03. EVERY candidate card on any Marr list MUST answer both screening questions: (1) **Current Salary** (current salary and bonus structure) and (2) **Why Leaving** (why they are leaving their current position). Render both in the meta block alongside Expected Comp. Never send a Marr list without these two answers filled for every candidate. Reference: `projects/generate_marr_candidates_batch2.py` (`current_comp` + `why_leaving` fields).

---

## How to Build a New Per-Client Script

1. Copy `template_skeleton.py` (in this folder) to `projects/generate_[client-slug]_candidates_batch[N].py`
2. Fill in the `CFG` dict — client_name, company, role_title, batch_num, date_str, candidates
3. Run the script — generator writes both output files and prints char count + div balance check
4. Open the HTML on Desktop to review
5. Once approved, send link to client

The generator handles all HTML, CSS (lifted from Carolyn template), and sanity checks. Per-client script never touches HTML — only CFG.

---

## Reference Implementation
`projects/generate_yael_lederman_candidates_batch2.py` is the canonical reference. Built for Yael Lederman (Kadima Labs), 4 candidates: Balaj Sikander, Jibran Mustafa, Komal Dilshad, Sarmad Ali Khan.

## Dependencies
- Reads CSS from `~/Desktop/proposals/carolyn-cope-proposal.html` (Carolyn lineage).
- If that file is missing, generator fails loudly with the path.

## Skill Backlog
- Auto-fetch candidate data from Stardex by candidate ID instead of hand-pasting (saves duplicate data entry)
- Optional Slack auto-notification to the client channel when a new batch is delivered
- Print-friendly mode for clients who want a PDF version
