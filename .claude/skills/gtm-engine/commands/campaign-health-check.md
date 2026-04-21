# Command: campaign-health-check

Weekly audit of a live campaign's deliverability, engagement, and pipeline health. Catches problems before they become disasters.

---

## When to Use

- Weekly check for Shmookh's retainer clients
- When open rates or reply rates suddenly drop
- Before adding new contacts to a live sequence
- When a client asks "how is the campaign doing?"

---

## Inputs Required

1. **Campaign name / client**
2. **Stats from Lemlist or HeyReach** — paste the dashboard numbers
3. **Domain/inbox details** — which domains and mailboxes are sending
4. **How long the campaign has been running**

---

## Health Check Areas

### Area 1: Deliverability

**Email:**

| Check | Healthy | Warning | Critical |
|-------|---------|---------|---------|
| Bounce rate | < 2% | 2–4% | > 4% — pause immediately |
| Spam complaint rate | < 0.1% | 0.1–0.3% | > 0.3% — pause immediately |
| Open rate | > 40% | 25–40% | < 25% — deliverability issue |
| Inbox placement | > 90% | 80–90% | < 80% — check DNS |

**LinkedIn:**

| Check | Healthy | Warning | Critical |
|-------|---------|---------|---------|
| Connection acceptance rate | > 35% | 25–35% | < 25% — profile or message issue |
| Account restriction warnings | None | 1 warning | Any restriction — reduce volume immediately |
| Daily send volume | ≤ 25 connections/day | 25–35 | > 35 — throttle back |

**Deliverability fixes:**
- Bounce rate too high → clean the list, run email verification (Findymail/NeverBounce)
- Spam complaints → check copy for trigger words, reduce sending frequency
- Low open rate → check if emails are landing in promotions/spam tab, test subject line
- LinkedIn restrictions → reduce daily volume, warm up account more slowly

---

### Area 2: Engagement

| Metric | Healthy | Needs attention |
|--------|---------|----------------|
| LinkedIn reply rate | > 15% | < 15% |
| Email reply rate | > 3% | < 3% |
| Positive reply rate | > 5% of total contacted | < 5% |
| Link clicks (if used) | N/A — no links in cold email | — |

**Engagement fixes:**
- Low reply rate → run validate-copy, refresh Touch 1 opener
- High open, low reply → offer isn't landing or CTA too demanding
- Replies but mostly negative → ICP mismatch or wrong pain angle

---

### Area 3: Pipeline Health

| Check | Healthy | Needs attention |
|-------|---------|----------------|
| Interested replies this week | Consistent with prior weeks | Drop of > 30% week-on-week |
| Meetings booked | On track vs goal | Below target for 2+ consecutive weeks |
| Meetings showing up | > 70% show rate | < 70% → follow-up process issue |
| Leads in Attio updated | All within 48 hours | Any leads sitting > 72 hours without update |

---

### Area 4: Infrastructure

**Monthly checks (flag if overdue):**
- [ ] SPF, DKIM, DMARC records intact — use MXToolbox
- [ ] Sending domain reputation — use Google Postmaster Tools
- [ ] Mailbox warm-up still running (for domains < 3 months old)
- [ ] Sending volume within safe limits (max 40 emails/mailbox/day)
- [ ] HeyReach account within LinkedIn sending limits

---

## Output Format

```
CAMPAIGN HEALTH CHECK
=====================
Client: [Name]
Campaign: [Name]
Period: [Week of X]
Running for: [X weeks]

DELIVERABILITY: 🟢 Healthy / 🟡 Warning / 🔴 Critical
- Bounce rate: X% [status]
- Open rate: X% [status]
- LinkedIn connection rate: X% [status]

ENGAGEMENT: 🟢 / 🟡 / 🔴
- LinkedIn reply rate: X% [status]
- Email reply rate: X% [status]
- Positive reply rate: X% [status]

PIPELINE: 🟢 / 🟡 / 🔴
- Meetings booked this week: X (target: X)
- Interested replies: X
- Leads updated in Attio: [Y/N]

INFRASTRUCTURE: 🟢 / 🟡 / 🔴
- DNS records: [intact / needs check]
- Warm-up status: [active / complete / not running]

ISSUES FOUND:
1. [Issue + recommended fix]
2. [Issue + recommended fix]

ACTIONS THIS WEEK:
- [ ] [Action 1]
- [ ] [Action 2]
```
