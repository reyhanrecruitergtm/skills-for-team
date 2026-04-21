# Finance & Investment Operations Skill

## What This Skill Does
Manages RecruiterGTM's financial operations: revenue tracking from Attio + WHOP, profit & loss, company registration strategy, investment management (business + personal), and cash flow planning. Reyhan-only access.

## When to Use
- Monthly P&L review
- Revenue check from closed deals
- Investment decisions (business reinvestment or personal)
- Tax planning or jurisdiction questions
- "How much did we make this month"
- "What are my margins"
- "Where should I register"
- Any question about money, profit, expenses, or investments

## How to Invoke
`/finance-ops` or mention money, revenue, P&L, margins, tax, investment, registration

---

## Current Company Structure

### The Ops Agent Lda. (Portugal)
- **Type:** Portuguese Limitada (Lda.) — single-member limited company
- **Location:** Almada, Portugal
- **Tax residency:** Portugal
- **Monthly obligations:**
  - Accountant: €300/month
  - Social security: [amount TBD — ask Reyhan]
- **NHR status:** [Check with Reyhan — may be expired]
- **Brands operating under this entity:** RecruiterGTM, GTM Academy

### Jurisdiction Research (In Progress)
- Estonia and Georgia: attempted, no agency response
- Researching: Dubai/UAE freezone, Hong Kong, Singapore, UK Ltd, US LLC (Wyoming/Delaware), Bulgaria, Hungary, Cyprus, Malta, Ireland
- Goal: lowest possible corporate tax for digital services revenue
- Research findings will be added to this skill once complete

---

## Revenue Streams & Tracking

### Revenue Sources
| Stream | Price | Type | Tracked In |
|--------|-------|------|-----------|
| RecruiterGTM Community (Standard) | $1,497 one-time | One-time | Attio (closed deal) |
| DFY Managed Pilots (OutboundOS/SourcingOS/ContentOS) | $2,500/month | MRR | Attio (closed deal) |
| DFY Both Systems | $4,000/month | MRR | Attio (closed deal) |
| GTM Academy Placements | $4,497 one-time | One-time | Attio (closed deal) |
| Claude Code DFY Setup | $3,000 one-time | One-time | Attio (closed deal) |
| GTM Engine Management Retainers | ~$2,000/month | MRR | Attio (closed deal) |
| Affiliates (Clay, Lemlist, Pin.com) | ~10% of revenue | Recurring | Manual / affiliate dashboards |
| WHOP (digital products) | Variable | One-time/recurring | WHOP dashboard |

### How to Pull Revenue Data
1. **Attio:** Use `mcp__attio-mcp__filter-list-entries` on Sales Pipeline 2026 to pull deals in "Closed Won" or "Paid" stages for a given month
2. **WHOP:** Manual input — Reyhan provides WHOP numbers monthly
3. **Affiliates:** Manual input from Clay/Lemlist/Pin.com dashboards

### Monthly Revenue Review Process
1. Pull all closed deals from Attio for the month
2. Add WHOP revenue (Reyhan provides)
3. Add affiliate revenue (Reyhan provides)
4. Calculate total gross revenue
5. Present to Reyhan for approval before logging to P&L

---

## Profit & Loss (P&L)

### Fixed Monthly Costs
| Expense | Amount | Notes |
|---------|--------|-------|
| Accountant | €300/month | Portuguese Lda. maintenance |
| Social Security | TBD | Ask Reyhan for exact amount |
| Claude Max | $100/month | AI for operations |
| Clay | $149/month | Data enrichment |
| Lemlist | $99/month | Outreach |
| n8n | $24/month | Automation |
| Apollo | $79/month | Contact data |
| Antigravity | TBD | Claude Code interface |
| Skool | TBD | Community platform fee |
| Google Workspace | TBD | Email + Drive |
| Apify | TBD | Web scraping |
| Beehiiv | TBD | Newsletter |

### Variable Costs
| Expense | Notes |
|---------|-------|
| Team payroll (Salar, Shmookh, Daniyal, Robyn, Hassan) | Monthly — amounts TBD |
| Ad spend (Facebook, Indeed) | Per client, variable |
| One-off tool purchases | As needed |

### P&L Template (Monthly)
```
MONTH: [Month Year]

REVENUE
  Community sales:        $___
  Managed pilot MRR:      $___
  Placements:             $___
  Claude Code DFY:        $___
  Retainers:              $___
  Affiliates:             $___
  WHOP:                   $___
  TOTAL REVENUE:          $___

FIXED COSTS
  Accountant:             €___
  Social Security:        €___
  Tool subscriptions:     $___
  TOTAL FIXED:            $___

VARIABLE COSTS
  Team payroll:           $___
  Ad spend:               $___
  Other:                  $___
  TOTAL VARIABLE:         $___

TOTAL COSTS:              $___
GROSS PROFIT:             $___
PROFIT MARGIN:            ___%

APPROVED BY REYHAN: [ ]
```

---

## Investment Management

### Business Reinvestment
Track decisions on where to reinvest profits:
- Team hires (new GTM Engineers, content person)
- Tool upgrades (higher tier subscriptions)
- Ad budget increases
- Event costs (Lisbon mastermind, conferences)
- Website/brand development

### Personal Investment
Track Reyhan's personal investment decisions:
- Stocks / ETFs
- Crypto
- Property (Portugal)
- Emergency fund

### Investment Log Format
```
DATE: [YYYY-MM-DD]
TYPE: [Business / Personal]
AMOUNT: [€/$ amount]
WHAT: [Description]
REASONING: [Why this investment]
EXPECTED RETURN: [Timeline + expected outcome]
STATUS: [Planned / Executed / Completed]
```

---

## Rules
- NEVER make financial decisions without Reyhan's explicit approval
- NEVER share financial data with anyone other than Reyhan
- Always present revenue data for manual approval before logging
- All amounts in USD unless specifically about Portuguese obligations (EUR)
- Ask before assuming any expense amount — use TBD if unknown
- Tax advice is research-level only — always recommend confirming with an accountant before acting
- Investment decisions are logged, not made by this skill

---

## Files
- This skill: `.claude/skills/finance-ops/SKILL.md`
- P&L logs: `finance/p&l/[YYYY-MM].md` (create as needed)
- Investment log: `finance/investments.md` (create when first investment logged)
- Jurisdiction research: `finance/jurisdiction-research.md` (create when research completes)
