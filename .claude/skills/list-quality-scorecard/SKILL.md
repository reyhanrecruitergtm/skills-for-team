# List Quality Scorecard Skill

## What This Skill Does

Grades any lead or candidate CSV across **8 quality dimensions BEFORE it's sent or enriched further** — outputs a letter grade (A+ to F) + the top issues to fix + a pre-send checklist. Catches bad lists before they burn inboxes or waste enrichment credits. This is the **QA gate** in our Claude-Code-first outbound architecture (see [[reference_nowoslawski_architecture]]): nothing prospect-facing moves until the list clears this.

Adapted for RecruiterGTM from GrowthEngineX's open-source `list-quality-scorecard` (github.com/growthenginenowoslawski/coldoutboundskills). Python, stdlib only.

**Invoke:** after any list-build (`sourcing-os`, `build-tam`, Prospeo/Apollo/Apify pull) and email waterfall, **before** Clay personalization or an Instantly / HeyReach upload.

---

## Locked Rules

### A. Run it every time, before send
- Run on every prospect list AND every candidate list before it goes into a campaign or a client deliverable. No list ships un-graded.
- **Grade < C → do not send.** Fix the top 3 issues and re-run until ≥ B. A C-grade list reliably produces sub-1% reply rates and burns domain reputation.
- Skip only for lists <100 rows (sample too small) or a static list already graded once.

### B. The 8 dimensions + weights (locked)
Email verification (×2) · Duplicate emails (×1) · Duplicate domains (×1) · Title relevance (×1.5) · Bad-title detection (×1) · Catch-all/generic density (×1) · ICP fit (×2) · Name quality (×1). Grades: A+≥93 · A≥90 · B≥80 · C≥70 · D≥60 · F<60.

### C. Our-stack adaptations
- **Verifier** = Instantly built-in / MillionVerifier / ZeroBounce (any column named `verified`/`email_status`/`verification_status` is read). 100% verification before send is non-negotiable.
- **Name quality enforces [[feedback_csv_names_split]]** — the list must have separate **First Name + Last Name** columns; a single Name column fails this dimension outright.
- **Sender** = Instantly (email) + HeyReach (LinkedIn), never Smartlead.
- Applies to **candidate lists too** (sourcing), not just BD prospect lists.

### D. What next
- **≥ B** → hand the clean list to the Clay final-mile personalization + `copy-engine`, then upload to Instantly/HeyReach as DRAFT.
- **< C** → fix, re-run. If verification or 30%+ bad titles, fix those before spending more on enrichment.

---

## How to Run

```bash
python3 .claude/skills/list-quality-scorecard/score_list.py \
  --list <path/to/leads.csv> \
  [--out <scorecard.md>] \
  [--titles "Founder,CEO,Head of Talent"] \
  [--industries "Software,Staffing"] \
  [--headcount-min 30 --headcount-max 150]
```
- `--titles` / `--industries` / `--headcount-*` unlock the Title-relevance and ICP-fit dimensions (pull them from the client's ICP). Without them those two dimensions show `n/a` and drop out of the weighted average.
- Column detection is flexible (case-insensitive; handles `First Name`/`first_name`, `title`/`job_title`, `company_domain` or derives domain from email, etc.).

## Related
- [[reference_nowoslawski_architecture]] — where this sits in the pipeline (the QA gate)
- `copy-engine` — the quality loop for the personalization that follows a passing list
- `email-deliverability` — the 1% rule this protects
