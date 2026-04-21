# Skill: Candidate Sourcing Pack

Turn a job brief into a complete sourcing pack in one shot. Boolean strings, target companies, outreach messages, and screening questions — ready to use immediately.

---

## How to Invoke

Paste a job brief and say `/candidate-sourcing`.

Minimum required input:
- Job title
- Location
- Company type (startup, agency, corporate, etc.)
- 2–3 key requirements or must-haves

Optional but useful:
- Salary range
- Seniority level
- Industries to target or avoid
- Whether this is a retained or contingent search

---

## What This Skill Outputs

A complete sourcing pack with 6 sections — ready to use immediately, no editing required.

---

## Step-by-Step Instructions

### Step 1 — Parse the brief

Read the job brief carefully. Extract:
- Role title and seniority
- Location and remote/hybrid status
- Must-have skills or experience
- Nice-to-haves
- Company context (size, stage, industry)
- Any exclusions (companies to avoid poaching from, etc.)

If the brief is too vague to produce useful output, ask for the 2–3 most important requirements before proceeding.

---

### Step 2 — Output Section 1: Boolean Strings

Write 3 Boolean strings:

**String 1 — LinkedIn Recruiter**
Use `AND`, `OR`, `NOT` operators. Include title variations, key skills, and location. Format it ready to paste directly into LinkedIn Recruiter search.

**String 2 — Google X-Ray (LinkedIn profiles)**
Format: `site:linkedin.com/in "[title]" "[skill]" "[location]"`
Include 2–3 variations.

**String 3 — Niche/alternative source**
Depending on the role, write a search string for the most relevant alternative source:
- Tech roles → GitHub, Stack Overflow
- Creative roles → Dribbble, Behance
- Finance/ops → specialist job boards or alumni networks
- Recruiters → RecruiterOS communities, Bullhorn users

---

### Step 3 — Output Section 2: Target Companies

List 8–10 companies to proactively source from.

For each company include:
- Company name
- Why they're a good source (relevant team size, same role type, recent redundancies, etc.)

Think about: direct competitors, adjacent industries, companies that just downsized, companies the ideal candidate has likely passed through.

---

### Step 4 — Output Section 3: Sourcing Filters

Recommend the exact filters to apply on LinkedIn Recruiter:

- Job titles (primary + alternatives)
- Industries
- Company headcount range
- Years of experience
- Keywords to include in profile
- Keywords to exclude

---

### Step 5 — Output Section 4: Outreach Messages

Write 3 outreach variants. Each under 300 characters for LinkedIn connection requests.

**Variant A — Cold outreach**
No mutual connection. Lead with the role or the opportunity, not "I came across your profile."

**Variant B — Warm/referred**
There's a mutual connection or they've engaged with content. More personal opener.

**Variant C — Re-engage (lapsed candidate)**
They're already in the database. Acknowledge the gap, update them on a new opportunity.

Rules for all three:
- No "hope you're well" or "I came across your profile"
- One sentence max per idea
- End with a question or hook — not a statement
- Sound like a human texting a peer, not a recruiter sending a template

---

### Step 6 — Output Section 5: Screening Questions

Write 6 screening questions for the first call.

For each question:
- The question itself
- What a strong answer sounds like (2 sentences)
- What a red flag answer sounds like (1 sentence)

Mix of:
- 2 experience/background questions
- 2 competency/situational questions
- 1 motivation/culture fit question
- 1 curveball that reveals how they think

---

### Step 7 — Output Section 6: Sourcing Strategy Note

2–3 sentences summarising the sourcing approach for this role.

Include:
- Where the best candidates are likely hiding
- The hardest part of this search and how to get around it
- One non-obvious tactic specific to this role or market

---

## Output Format

```
--- CANDIDATE SOURCING PACK ---
Role: [Title] | [Location] | [Company Type]
Generated: [Date]

--- 1. BOOLEAN STRINGS ---
[content]

--- 2. TARGET COMPANIES ---
[content]

--- 3. SOURCING FILTERS ---
[content]

--- 4. OUTREACH MESSAGES ---
[content]

--- 5. SCREENING QUESTIONS ---
[content]

--- 6. SOURCING STRATEGY NOTE ---
[content]
```

---

## Edge Cases

- **Very niche role** (e.g. LanguageTech CTO): Flag that Boolean strings will return small pools. Recommend widening geography or targeting conference speakers and open source contributors.
- **Location is a constraint**: Note if the talent pool in that city is thin and suggest remote-first alternatives to suggest to the client.
- **Confidential search**: Adjust outreach messages to omit company name. Lead with role function and opportunity type instead.
- **Replacement hire**: Do not reference the outgoing person. Focus purely on the role requirements.
