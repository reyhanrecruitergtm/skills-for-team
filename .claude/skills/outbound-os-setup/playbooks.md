# OutboundOS Playbooks Reference

Detailed setup instructions for each Clay playbook. Each playbook runs on top of the approved TAM table.

---

## Playbook 1 — LinkedIn Jobs

**Intent signal:** Company is actively hiring — warm indicator they have budget and headcount need.
**Best for:** Almost every client. Strongest warm signal available.
**Credits per row:** ~3–4 data credits (job enrichment + company + person + email via waterfall)

### What it does
Finds companies in the TAM that have open job postings on LinkedIn. Filters by job title keywords relevant to the client's niche to surface the hottest targets.

### Clay Setup Steps

1. **Start from TAM table** — duplicate or use a connected table with approved companies
2. **Add column: LinkedIn Jobs Search**
   - Provider: LinkedIn Jobs (Clay native)
   - Input: company LinkedIn URL (from TAM enrichment)
   - Filter by job title keywords matching client's niche (e.g. "Recruiter", "Head of Talent", "HR Manager")
   - Output: list of matching open jobs per company
3. **Add column: Job Count**
   - Formula: count of returned jobs
   - Filter rows where Job Count > 0
4. **Add column: Job Title (first match)**
   - Extract top job title from jobs list
5. **Add column: ICP Score**
   - AI column (use own OpenAI key)
   - Prompt: *"Given this company [description] and open role [job title], score 0–100 how likely they are to need external recruitment support. Return only the number."*
6. **Filter:** Keep rows where ICP Score > 60
7. **Add column: Decision Maker Search**
   - Provider: Clay People Search
   - Input: company LinkedIn URL + titles from intake (e.g. CEO, Head of People)
8. **Add column: Email (waterfall)**
   - Step 1: Prospeo (own API key)
   - Step 2: Hunter.io
   - Step 3: Clay native
9. **Add column: Personalisation Variable**
   - AI column: *"In one sentence, write a personalised observation about why [company name] might need recruitment support based on their job posting for [job title]."*

### Output Columns for Lemlist
`First Name`, `Last Name`, `Email`, `Company Name`, `Job Title (open role)`, `Personalisation Variable`

---

## Playbook 2 — Leadership Change

**Intent signal:** New decision-maker joined in the last 90 days — high propensity to change suppliers and review processes.
**Best for:** Clients targeting HR/People/C-suite buyers. Works well for retained and RPO pitches.
**Credits per row:** ~3 data credits (job change enrichment + person + email)

### What it does
Identifies contacts at TAM companies who recently started a new role (within 90 days). New leaders are 5x more likely to make vendor changes in their first 90 days.

### Clay Setup Steps

1. **Start from TAM table**
2. **Add column: Recent Job Changes**
   - Provider: Clay People Search
   - Input: company LinkedIn URL + target titles from intake
   - Filter: "started in last 90 days"
3. **Add column: Person LinkedIn URL**
   - Extract from job change results
4. **Add column: Person Enrichment**
   - Provider: LinkedIn Person enrichment
   - Input: person LinkedIn URL
   - Output: Full name, current title, location, tenure
5. **Add column: Days in Role**
   - Formula: calculate days since start date
   - Filter: keep rows where Days in Role ≤ 90
6. **Add column: Email (waterfall)**
   - Step 1: Prospeo (own API key)
   - Step 2: Hunter.io
7. **Add column: Personalisation Variable**
   - AI column: *"[First name] just started as [title] at [company]. In one sentence, write a relevant, non-generic reason why a new [title] might want to review their recruitment process."*

### Output Columns for Lemlist
`First Name`, `Last Name`, `Email`, `Company Name`, `Title`, `Days in Role`, `Personalisation Variable`

---

## Playbook 3 — Low Internal HR Ratio

**Intent signal:** Company has fewer than 1% of staff in HR roles — indicator they outsource or under-invest in internal recruitment.
**Best for:** Staffing, RPO, and fractional HR clients. Strong cold signal for companies without in-house hiring capability.
**Credits per row:** ~3 data credits (company enrichment + headcount data + person + email)

### What it does
Uses headcount data to calculate the ratio of HR staff to total staff. Companies where this is < 1% are likely reliant on external recruitment support or open to it.

### Clay Setup Steps

1. **Start from TAM table**
2. **Add column: Total Headcount**
   - Provider: Clearbit or Clay LinkedIn enrichment
   - Output: total employee count
3. **Add column: HR Department Headcount**
   - Provider: Clay People Search
   - Filter by department: Human Resources
   - Output: count of HR staff
4. **Add column: HR Ratio**
   - Formula: `HR Headcount / Total Headcount * 100`
   - Filter: keep rows where HR Ratio < 1
5. **Add column: Decision Maker Search**
   - Provider: Clay People Search
   - Titles: CEO, COO, MD, Founder (not HR — they likely don't have one)
6. **Add column: Email (waterfall)**
   - Step 1: Prospeo (own API key)
   - Step 2: Hunter.io
7. **Add column: Personalisation Variable**
   - AI column: *"[Company name] has [total headcount] employees and only [HR headcount] in HR. In one sentence, write an observation about how this might affect their ability to hire fast."*

### Output Columns for Lemlist
`First Name`, `Last Name`, `Email`, `Company Name`, `Total Headcount`, `HR Ratio`, `Personalisation Variable`

---

## Playbook 4 — 90-Day Job Change

**Intent signal:** A contact from the client's existing network or warm list has moved to a new company.
**Best for:** Dream100 reactivation, warming up existing relationships, re-engaging past prospects.
**Credits per row:** ~2–3 data credits (person enrichment + email)

### What it does
Monitors a list of named contacts (existing network, past clients, warm leads) for recent job changes. When someone moves, they're a fresh contact at a new company — prime timing for outreach.

### Clay Setup Steps

1. **Start from a contact list** (not the TAM — import from client's CRM or network)
2. **Add column: Current Company (enriched)**
   - Provider: LinkedIn Person enrichment
   - Input: person LinkedIn URL
   - Output: current company, title, start date
3. **Add column: Job Change Detected**
   - Formula: compare current company to previous company (if available)
   - Or filter: start date within last 90 days
4. **Add column: New Company LinkedIn URL**
   - Extract from enrichment output
5. **Add column: New Company in TAM**
   - Formula: check if new company exists in TAM table (VLOOKUP or Clay match)
   - Prioritise contacts who moved to a TAM company
6. **Add column: Email at New Company (waterfall)**
   - Step 1: Prospeo (own API key)
   - Step 2: Hunter.io
7. **Add column: Personalisation Variable**
   - AI column: *"[First name] recently moved from [old company] to [new company] as [title]. In one sentence, write a relevant re-engagement opener referencing their new role."*

### Output Columns for Lemlist
`First Name`, `Last Name`, `Email`, `New Company`, `New Title`, `Days Since Change`, `Personalisation Variable`

---

## Playbook 5 — Talent Replacement Backfills

**Intent signal:** A company has re-posted the same role within a short period — signals employee churn, hiring difficulty, or failed placement.
**Best for:** Specialist recruiters. Signals companies struggling to hire in specific functions.
**Credits per row:** ~4 data credits (job history enrichment + company + person + email)

### What it does
Identifies companies that have posted the same or similar job title multiple times within 60–90 days. This pattern indicates they failed to fill the role or had a quick departure — strong signal for specialist recruitment outreach.

### Clay Setup Steps

1. **Start from TAM table**
2. **Add column: LinkedIn Jobs History**
   - Provider: LinkedIn Jobs (Clay native)
   - Pull jobs posted in the last 90 days
   - Filter by role keywords matching client's placement niche
3. **Add column: Repeat Job Detected**
   - Formula: check if the same or similar job title appears 2+ times
   - Flag companies where this is true
4. **Add column: Original Post Date**
   - Extract date of first posting
5. **Add column: Re-post Date**
   - Extract date of second posting
6. **Add column: Days Between Posts**
   - Formula: Re-post Date minus Original Post Date
   - Filter: keep rows where Days Between Posts < 90
7. **Add column: Decision Maker Search**
   - Provider: Clay People Search
   - Titles from intake (hiring manager, Head of Talent, CEO)
8. **Add column: Email (waterfall)**
   - Step 1: Prospeo (own API key)
   - Step 2: Hunter.io
9. **Add column: Personalisation Variable**
   - AI column: *"[Company name] has re-posted [job title] within [days] days. In one sentence, write an observation about what this might signal about their hiring challenge."*

### Output Columns for Lemlist
`First Name`, `Last Name`, `Email`, `Company Name`, `Role`, `Days Between Posts`, `Personalisation Variable`

---

## Connecting Playbooks to Lemlist

After each playbook is built and filtered in Clay:

1. Export filtered rows as CSV (only rows with valid email + all output columns filled)
2. In Lemlist: create a new campaign → import CSV as leads
3. Map CSV columns to Lemlist variables: `{{firstName}}`, `{{companyName}}`, `{{personalisationVariable}}` etc.
4. Use the personalisation variable in the opening line of sequence step 1
5. Set daily sending limits: max 50 emails/day per inbox (warm-up phase), up to 100/day once warmed

---

## Playbook Selection Quick Guide

| Client type | Recommended playbooks |
|---|---|
| Generalist recruiter | LinkedIn Jobs + Leadership Change |
| Staffing / RPO | LinkedIn Jobs + Low HR Ratio + Talent Backfills |
| Exec search | Leadership Change + 90-Day Job Change |
| Specialist (tech, finance, etc.) | LinkedIn Jobs + Talent Backfills |
| Warm list reactivation | 90-Day Job Change |
