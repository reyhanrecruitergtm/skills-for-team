# SOP — Community-Only Onboarding (Skool $1,497)

**Audience:** Daniyal (owner). Salar (BD campaign). Reyhan (roadmap call).
**Trigger:** New Skool member payment confirmed (Stripe).
**Outcome:** Member is fully ramped by Day 30 with Claude Ops Manager + 1st Intent BD campaign live + Website/SEO live (if scoped). Day 31+ they enter community-only support mode.
**Notion field:** `Community Stage` on Client Tracker row.

---

## Day 0 — Payment Received (Owner: Daniyal)

**Notion Stage:** `Onboarding (D0–3)`

Actions:
- [ ] Create row in Notion Client Tracker (`26f5231b-4546-4f7a-b7b1-8f51d854d956`)
  - Client / Agency Name
  - Offer / Tier = `Skool`
  - Deal Closed Date = today
  - Status = `Onboarding`
  - Community Stage = `Onboarding (D0–3)`
- [ ] Approve Skool join request
- [ ] Send Skool welcome DM with Calendly link for the 60-min Systems Roadmap call with Reyhan
  - Calendly link: per `reference_calendly_link.md`
- [ ] Add member email to community Beehiiv list

**Deliverables generated:**
- Skool welcome DM
- Roadmap intake form link (if not auto-sent on payment)

---

## Day 1–3 — Roadmap Call (Owner: Reyhan, Daniyal preps)

**Notion Stage:** `Roadmap call scheduled` → `Discovery + roadmap delivered`

Pre-call (Daniyal, 24h before):
- [ ] Pull member's LinkedIn + agency website
- [ ] Pre-fill discovery doc with: niche, team size, current stack, current MRR (if known)
- [ ] Drop pre-fill doc into Reyhan's call prep folder

Call (Reyhan, 60 min):
- [ ] Run the Systems Roadmap call (script in `roadmap-generator` skill)
- [ ] Confirm: niche, ICP, 3 biggest blockers, what they want by Day 30
- [ ] Update Notion: `Community — Day 3 Roadmap Call` date field

Post-call (Daniyal, within 24h):
- [ ] Update Notion: Community Stage = `Discovery + roadmap delivered`
- [ ] Schedule Day 7 Claude Ops Manager kickoff call with Daniyal (book directly in member's calendar)
- [ ] Schedule Day 10 BD campaign kickoff call with Salar

---

## Day 3–6 — Roadmap Deliverable Sent (Owner: Daniyal, drafts via skill)

**Notion Stage:** `Discovery + roadmap delivered` (locked)

Actions:
- [ ] Generate 90-Day Roadmap via `roadmap-generator` skill (call transcript + LinkedIn + intake doc)
- [ ] Reyhan approves
- [ ] Send roadmap PDF + Loom walkthrough via Skool DM (target: 48–72h after the roadmap call)
- [ ] Drop a copy into member's Skool community profile

**Deliverable:** Polished 90-Day Roadmap (4 pillars + DFY sprint + milestones)

---

## Day 7–10 — Claude Ops Manager Kickoff Call (Owner: Daniyal)

**Notion Stage:** `Claude Ops Manager building`

Pre-call:
- [ ] Send member the prep doc: list of accounts to bring (their CRM, ATS, Gmail, Slack, etc.) and credentials checklist

Call (Daniyal, 60 min):
- [ ] Scope the Claude Ops Manager: which skills to install, which MCPs to wire (CRM, ATS, Gmail, Calendar, Notion, etc.)
- [ ] Walk member through Claude Code install on their machine
- [ ] Confirm: which 3–5 skills get prioritized (per the 90-Day Roadmap)

Post-call:
- [ ] Daniyal builds the Claude Ops Manager (target: 7–10 days of work)

---

## Day 10–14 — BD Campaign Kickoff Call (Owner: Salar)

**Notion Stage:** `BD campaign building`

Pre-call (Salar, prep):
- [ ] Review member's roadmap + niche
- [ ] Pre-draft 1 intent-based playbook for their primary ICP
- [ ] Pull ~50-prospect sample list from Apollo/Apify

Call (Salar, 60 min):
- [ ] Validate ICP + intent triggers
- [ ] Walk through the 1st intent-based BD campaign structure
- [ ] Confirm: outbound mailbox setup (HyperTide if they need new mailboxes, otherwise theirs), LinkedIn account, sequence cadence
- [ ] Get sign-off on copy direction

Post-call (Salar builds, target: 7–10 days):
- [ ] Mailboxes warmed
- [ ] Sequences loaded into Instantly + HeyReach
- [ ] First 200–300 prospects enriched + validated
- [ ] Sample reply handling SOP shared with member

---

## Day 21 — LAUNCH MILESTONES (Owners: Daniyal + Salar)

**Notion Stage:** transitions from building → live for both Claude + BD

Two simultaneous launches:

### A. Claude Ops Manager LIVE (Daniyal)
- [ ] All scoped skills installed + tested on member's machine
- [ ] MCPs wired + authenticated
- [ ] 60-min handover call: how to invoke each skill, where to find logs, how to ask Claude for help
- [ ] Update Notion: `Community — Day 17 Claude Live` date field = today (rename field to "Claude Live" — exact date varies)

### B. 1st Intent BD Campaign LIVE (Salar)
- [ ] Sequences sending to first batch
- [ ] Member added to dedicated reply-tracking Slack thread (or Skool thread)
- [ ] Update Notion: `Community — Day 22 Campaign Live` date field = today (rename field to "Campaign Live")
- [ ] Community Stage updates to `Website + SEO building` (if scoped) OR `Ongoing support (M2–12)` (if no website work)

**Comms to member (Daniyal):** Skool DM summary: "Claude Ops Manager is live, BD campaign is sending. Here's what to watch this week. First check-in in 7 days."

---

## Day 22–30 — Website + SEO Build (Optional, Owner: Daniyal)

**Notion Stage:** `Website + SEO building`

Only runs if member scoped a website/SEO refresh in the roadmap.

Actions:
- [ ] Build site on Lovable or refresh existing (use `website` skill)
- [ ] SEO basics: meta tags, schema, internal links, key landing pages
- [ ] Launch by Day 30
- [ ] Update Notion: `Community — Day 45 Website Live` date field = today (rename field to "Website Live" — target is Day 30 per Reyhan's locked spec)

---

## Day 30 — Sprint Complete (Owner: Daniyal)

**Notion Stage:** `Ongoing support (M2–12)`

Actions:
- [ ] Send 30-day review DM via Skool: what's live, what's running, what to focus on next 60 days
- [ ] Hand off the remaining 60 days of the 90-Day Roadmap action items to the member (they execute, we support via Q&A + DMs)
- [ ] Update Notion:
  - Community Stage = `Ongoing support (M2–12)`
  - Status = `Active`
  - Check-ins = add `30 Day Check in`
- [ ] Add member to weekly Q&A reminder list (Wed 4:40 PM UK with Salar + Fri Strategy with Reyhan)

---

## Day 31–365 — Ongoing Community Support (Owner: Daniyal as interim CM)

**Notion Stage:** `Ongoing support (M2–12)` (locked until end of year-1 access)

Standing rituals:
- [ ] Weekly Q&A attendance tracking (update `Community — Last Q&A Attended` date)
- [ ] Skool inbox check daily (update `Community — Last 1:1 Message` date when member messages)
- [ ] 60 Day Check in DM (Daniyal sends, logs in `Check-ins` field)
- [ ] **NO scheduled 1:1 calls with Reyhan** at this stage — only Daniyal jumps on 1:1 if the member specifically requests one
- [ ] Watch `At Risk (Auto)` formula — if member flagged at risk, Daniyal personal outreach within 48h

Optional upsells (log in `Renewal / Upsell Signals`):
- `Managed Pilot interest` — escalate to Reyhan for a discovery call
- `Claude Code DFY add-on` — Daniyal can run a paid scope expansion
- `Talent placement interest` — route to Shmookh

---

## Day 365 — Renewal or Alumni

**Notion Stage:** `Completed / Alumni`

Actions:
- [ ] 30 days before access expires: Reyhan or Daniyal sends a renewal DM
- [ ] If renew → start fresh Year 2 onboarding (skip Day 0–21, go to Day 31+ steady-state with updated roadmap)
- [ ] If alumni → move Status to `Completed`, Community Stage to `Completed / Alumni`, keep them in Beehiiv list

---

## Daniyal's Implementation Checklist (Notion + Automations)

Things Daniyal needs to build to operationalize this SOP:

1. **Field date label updates** (15 min):
   - Rename `Community — Day 17 Claude Live` → `Community — Day 21 Claude Live`
   - Rename `Community — Day 22 Campaign Live` → `Community — Day 21 Campaign Live`
   - Rename `Community — Day 45 Website Live` → `Community — Day 30 Website Live`
   - Update `At Risk (Auto)` formula thresholds: Claude late at Day 21+7, Campaign late at Day 21+7, Website late at Day 30+7

2. **n8n automation: Stripe → Notion row create** (1 day):
   - Trigger: Stripe payment_intent.succeeded for the Skool product
   - Action: create row in Client Tracker with Offer/Tier = Skool, Deal Closed Date = today, Status = Onboarding, Community Stage = Onboarding (D0–3)

3. **n8n automation: Notion → Slack reminders** (1 day):
   - Daily at 9 AM UK, scan Client Tracker for any row where today >= Deal Closed Date + N (the milestone target days)
   - Post to `#ops` Slack: "{Client} hits Day {N} today — {owner} needs to {action}"

4. **Update existing onboarding SOP doc** that Daniyal already maintains — fold this version into it.

---

## Diff vs Notion Today (2026-05-13)

| Field | Notion now | Locked target | Action |
|---|---|---|---|
| Claude live | Day 17 | Day 21 | Daniyal: rename field + update At Risk formula |
| BD campaign live | Day 22 | Day 21 | Daniyal: rename field + update At Risk formula |
| Website live | Day 45 | Day 30 | Daniyal: rename field + update At Risk formula |

The Community Stage status options are already correct.
