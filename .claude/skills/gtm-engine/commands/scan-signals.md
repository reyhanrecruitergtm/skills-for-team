# Command: scan-signals

Surface live buying signals from a prospect list or Clay table. Identifies which prospects have the highest intent right now so outreach is timed perfectly.

---

## When to Use

- Before launching a new sequence — find the hottest prospects to prioritise
- Weekly signal refresh for active campaigns
- When a client asks "who should we reach out to first?"
- When Shmookh needs to prioritise outreach for a retainer client

---

## Inputs Required

1. **Prospect list** — Clay table name, CSV, or list of company names
2. **Signal types to scan** — which of the 4 tiers to check (see below)
3. **ICP** — confirm the target persona and company profile

---

## Signal Tier Framework

Signals are ranked by buying intent — Tier 1 is hottest, Tier 4 is coldest.

### Tier 1 — Active Hiring Signals (Hottest)
Company is actively trying to solve the problem you solve.

| Signal | What it means | How to find it |
|--------|--------------|----------------|
| Posting 2+ open roles in target function | Growing fast, recruitment pain is live | Clay → LinkedIn Jobs enrichment |
| Re-posting same role after 60+ days | Can't fill it — frustrated, open to help | LinkedIn Jobs history |
| Posting a Head of [function] role | Scaling the team = systems needed | Job title keyword in Clay |
| Sudden hiring spike (30%+ headcount growth) | Hypergrowth = operational strain | LinkedIn headcount trend column |

### Tier 2 — Leadership Change Signals (Very Hot)
New decision makers have mandate and budget. Old loyalties don't apply yet.

| Signal | What it means | How to find it |
|--------|--------------|----------------|
| New C-suite or Head of [function] in last 90 days | New DM, new budget cycle | Clay → LinkedIn job change enrichment |
| Founder stepped back from operations | Professionalising the business | LinkedIn activity + job changes |
| New HR/People leader at a company with no HR system | First priority will be fixing infrastructure | LinkedIn People filter |

### Tier 3 — Company Growth Signals (Warm)
Company is in a growth phase — pain will follow if it hasn't already.

| Signal | What it means | How to find it |
|--------|--------------|----------------|
| Raised a funding round in last 6 months | Capital to spend, pressure to grow | Crunchbase enrichment in Clay |
| Announced expansion into new market | New headcount needed | News/press releases via Clay |
| Multiple senior hires across departments | Scaling across the org | LinkedIn headcount growth |

### Tier 4 — Weak Signals (Cold — use for volume plays only)
Useful for broad outreach but not priority targeting.

| Signal | What it means | How to find it |
|--------|--------------|----------------|
| In ICP industry and headcount range | Fits the profile | Standard Clay TAM filters |
| Active LinkedIn presence | Reachable via LinkedIn | Profile activity enrichment |
| No ATS or CRM visible | Gap in their stack | Tech stack enrichment |

---

## Scoring Output

For each prospect, assign a signal score:

| Score | Signal tier present | Action |
|-------|--------------------|----|
| 🔴 Priority | Tier 1 + Tier 2 firing simultaneously | Personalised first touch — write bespoke opening line |
| 🟠 High | Tier 1 OR Tier 2 | Priority in sequence — add to top of list |
| 🟡 Medium | Tier 3 only | Add to standard sequence |
| ⚪ Low | Tier 4 only | Volume play — batch outreach |

---

## Output Format

```
SIGNAL SCAN REPORT
==================
List: [name]
Scanned: [date]
Total prospects: [X]

PRIORITY (🔴) — [X] prospects
- [Company] | [Contact] | Signals: [Tier 1: hiring 3 engineers] + [Tier 2: new CTO hired Oct 2025]
- [Company] | [Contact] | Signals: [Tier 1: re-posting Head of EB for 90 days]

HIGH (🟠) — [X] prospects
- [Company] | [Contact] | Signal: [Tier 1: 4 open roles in data team]

MEDIUM (🟡) — [X] prospects
[list]

LOW (⚪) — [X] prospects
[count only — not worth listing individually]

RECOMMENDED ACTION:
- Launch personalised sequence for Priority list first
- Add High list to standard sequence week 1
- Add Medium list to sequence week 2
- Hold Low list for volume campaign
```

---

## Clay Column Setup (for running this inside a Clay table)

Add these enrichment columns to capture signal data:

| Column | Clay enrichment | Output |
|--------|----------------|--------|
| Open roles count | LinkedIn Jobs lookup | Number |
| Open roles in target function | LinkedIn Jobs + keyword filter | Y/N |
| Days since role first posted | LinkedIn Jobs history | Number |
| New leader in last 90 days | LinkedIn job change | Y/N + name + title |
| Headcount growth 12mo | LinkedIn headcount trend | % |
| Funding in last 6 months | Crunchbase enrichment | Y/N + amount |
| Signal score | Formula column | 1-4 |
| Priority tier | IF formula on signal score | 🔴/🟠/🟡/⚪ |
