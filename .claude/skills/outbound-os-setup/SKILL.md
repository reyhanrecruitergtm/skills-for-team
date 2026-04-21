# Skill: OutboundOS Setup

Guide Reyhan through a full DFY OutboundOS GTM Engine setup for a client — from intake document to live Clay playbooks. Context-aware: reads the client's intake doc to generate Clay-ready configs, client approval messages, and per-playbook setup checklists.

---

## When to Use

- Reyhan says "help me set up OutboundOS for [client]"
- Reyhan says "help me build the TAM for [client]"
- A new DFY OutboundOS client has been onboarded
- Any time `/outbound-os-setup` is invoked

---

## How to Invoke

1. Paste the client's intake document into the conversation (Google Doc content, PDF text, or filled template)
2. Say `/outbound-os-setup` or "let's set up OutboundOS for this client"

The skill runs phase by phase. Complete each phase before moving to the next.

---

## The 4 Phases

---

### Phase 1 — TAM Build (Total Addressable Market)

**Goal:** Map every company in Clay that matches the client's ICP.

**Steps:**
1. Parse the intake doc and extract:
   - Target industries (map to Clay industry filter options — see `clay-reference.md`)
   - Company headcount ranges
   - Locations (country/region)
   - ICP inclusion keywords (company description must contain these signals)
   - ICP exclusion keywords (filter these out)
   - Decision-maker titles (for Phase 4 contact enrichment)

2. Output a **Clay Company Search Config** — the exact filters to enter in Clay:
   ```
   Industries: [list]
   Headcount: [ranges]
   Location: [countries/cities]
   Description includes: [keywords]
   Description excludes: [keywords]
   ```

3. Estimate TAM size based on filters. Flag if estimated < 3,000 companies.

4. If TAM is thin (< 3k), suggest alternate sources:
   - Apollo.io company search (same ICP filters)
   - LinkedIn Sales Navigator company search
   - Manual LinkedIn search + CSV export

5. Output: **TAM Config Checklist** (step-by-step Clay setup instructions)

---

### Phase 2 — Client Review & Approval

**Goal:** Get client sign-off on the company list before running enrichment.

**Steps:**
1. Summarise the TAM in plain English:
   - Total estimated companies
   - Industries covered
   - Locations covered
   - Any sectors that are borderline / need client confirmation

2. Flag any ambiguities:
   - Industries that could include unwanted company types
   - Keywords that may be too broad or too narrow
   - Countries/regions that need confirmation

3. Draft a short client-facing message (email or Slack) for Reyhan to send:
   - Summary of what was mapped
   - 1-2 specific questions for clarification
   - Request to approve before moving to playbooks

4. **Checkpoint:** Do not proceed to Phase 3 until client approves.

---

### Phase 3 — Playbook Selection

**Goal:** Choose which intent signal playbooks to run on the approved TAM.

**Steps:**
1. Review the client's niche, target roles, and goals from the intake doc
2. Match against the standard playbook menu (see `playbooks.md`)
3. Output recommended playbooks with rationale for each

**Standard Playbook Menu:**

| Playbook | Signal | When to recommend |
|----------|--------|-------------------|
| LinkedIn Jobs | Company is actively hiring | Almost always — strongest warm signal |
| Leadership Change | New DM joined in last 90 days | Client targets HR/People/C-suite buyers |
| Low Internal HR Ratio | <1% of staff in HR roles | Staffing or RPO-focused clients |
| 90-Day Job Change | Contact changed roles recently | Dream100 reactivation or warm list |
| Talent Replacement Backfills | Same role re-posted after short tenure | Specialist recruiters targeting churn |

**Output:** Recommended playbook list with one-line rationale per playbook.

---

### Phase 4 — Playbook Configuration

**Goal:** For each selected playbook, output the full Clay setup.

**For each playbook, output:**
- Table structure (which columns to create)
- Enrichment waterfall (data providers in order of priority)
- Filter logic (what to include/exclude at row level)
- AI column prompts (ICP scoring, personalisation variables)
- Estimated credit cost per row
- Per-playbook setup checklist

Detailed step-by-step instructions for each playbook are in `playbooks.md`.

---

### Phase 4B — Data Verification (MANDATORY before export)

**Goal:** Verify all LinkedIn URLs and email addresses before any CSV export or Lemlist upload.

**Steps:**
1. Run HTTP verification on every LinkedIn URL in the dataset
   - 200 = valid
   - 999 = LinkedIn rate limit (URL format likely valid, flag for manual check)
   - 404 or other error = invalid, must be fixed or removed
2. Check CSV column alignment — empty fields with commas can shift columns and put wrong data in URL fields
3. Remove or flag any row with an invalid LinkedIn URL
4. For email addresses, verify domain exists (MX record check) at minimum
5. Output a verification summary: total rows, valid URLs, invalid URLs, missing emails

**Rule:** No CSV leaves this skill without a verification pass. Reyhan has had campaigns fail because of invalid URLs that were never checked.

---

## Phases 5+ (Coming Soon)

- **Phase 5 — Copywriting:** Generate outreach sequences per playbook using client's ICP and value props
- **Phase 6 — Launch:** Lemlist campaign setup, sending limits, warm-up config, reply handling

---

## Reference Files

- `intake-template.md` — Standard intake form for new clients
- `clay-reference.md` — Clay filter options, headcount ranges, keyword logic
- `playbooks.md` — Full step-by-step setup for each playbook

---

## Weekly Research

This skill is kept current by an automated weekly research job (runs every Monday, 8AM UK time).
Findings saved to `research/` — review weekly reports to find better methods, new data sources, or updated Clay features to incorporate into this skill.
