# Client Fulfillment Skill

## What This Skill Does

Owns the end-to-end onboarding and ramp-up workflow for every paying client RecruiterGTM closes. Two paths:

1. **Community-Only** — Skool members at $1,497 one-time. 30-day onboarding sprint, then 11 months of community support.
2. **Retainer** — Managed pilot clients at $2,500/mo+. 90-day pilot, full delivery, weekly comms.

Every closed deal MUST go through one of these two SOPs. No exceptions.

## How to Invoke

- "Onboard {client name}" → identify path (community vs retainer) → walk through Day 0 checklist
- "What's next for {client}?" → look up their retainer + open tasks in Pulse (`lookup_client` / `list_tasks`) → output the next action(s). (Notion Client Tracker retired 2026-07-19 — Pulse/DeliveryOS is the system of record; stage mapping below is the historical Notion reference.)
- "Check ramp status" → audit all active clients against their Day-N targets, flag anyone late
- "Build kickoff package for {client}" → generate Slack channel naming, Drive folder structure, kickoff doc template, agenda

## Source of Truth

- **Notion Client Tracker** (`26f5231b-4546-4f7a-b7b1-8f51d854d956`) — every client lives here with their `Community Stage` or `Retainer Stage` + milestone date fields
- **Attio Sales Pipeline 2026** — deal closure triggers entry into the tracker
- **SOPs** — `sop-community-onboarding.md` and `sop-retainer-onboarding.md` in this folder are the canonical day-by-day playbooks. Send these to Daniyal verbatim when he asks for the onboarding spec.

## Two Paths At A Glance

### Community-Only (Skool $1,497)
```
Day 0   → Joins community (Stripe payment hits)
Day 1–3 → Roadmap call with Reyhan booked + delivered
Day 3–6 → 90-Day Roadmap deliverable sent (48–72h after call)
Day 7   → Claude Ops Manager call with Daniyal booked
Day 10  → BD campaign kickoff call with Salar booked
Day 21  → Claude Ops Manager LIVE + 1st Intent BD Campaign LIVE
Day 30  → Website + SEO LIVE (if scoped)
Day 31+ → Ongoing support: weekly Q&A, 1:1 messaging, Daniyal-only 1:1 calls if needed
```

### Retainer ($2,500/mo+)
```
Day 0   → Deal closes (contract signed + payment received)
Day 0–2 → Slack channel + Drive folder + Discovery/Implementation doc created
Day 3–5 → Launch call delivered, 90-day timeline pinned in Slack, weekly recurring call scheduled
Day 15  → 1st LinkedIn campaign LIVE
Day 21  → 1st Email campaign LIVE
Day 28  → 2nd Email campaign LIVE
Day 45  → 4 intent-based multichannel campaigns running
Day 60  → 10 outbound responses generated
Day 90  → Pilot report delivered + 6-month extension offer
```

See the two SOPs for the full day-by-day, owners, deliverables, and Notion stage transitions.

## Notion Stage Mapping

The Client Tracker already has these stage fields ready to use:

**Community Stage** (status field):
- Onboarding (D0–3)
- Roadmap call scheduled
- Discovery + roadmap delivered
- Claude Ops Manager building
- BD campaign building
- Website + SEO building
- Ongoing support (M2–12)
- Completed / Alumni

**Retainer Stage** (status field):
- Launch Call & Prep
- Build in Progress
- Launch Approval
- Launched
- Scaled
- Completed
- Churned

**Milestone dates already in schema**:
- Community: Day 3 Roadmap Call · Day 17 Claude Live · Day 22 Campaign Live · Day 45 Website Live · Last Q&A · Last 1:1 Message
- Retainer: Day 30 Baseline Locked · Day 90 Renewal

⚠️ Diff vs Reyhan's stated targets (2026-05-13): Notion currently has Day 17 Claude + Day 22 Campaign + Day 45 Website. Reyhan's locked targets are **Day 21 Claude + Day 21 BD Campaign + Day 30 Website**. Daniyal must update the date-field labels and any At-Risk formula thresholds to match the locked dates.

## Locked Rules

### A. Path classification
- **Community-only path** = client paid the $1,497 one-time Skool fee and nothing else.
- **Retainer path** = client signed any managed pilot agreement ($2,500/mo or more), regardless of whether community is bundled.
- A client who buys community + later upgrades to retainer = move them to the retainer SOP from the day the retainer starts. Community stays in parallel.

### B. Owners (locked)
- **Reyhan** — Roadmap call (community Day 1–3). Launch call (retainer Day 3–5). Day 90 retainer renewal call. Strategic escalations.
- **Daniyal** — Claude Ops Manager setup (community + retainer). Drive folder + Slack channel creation. Implementation docs. Ongoing 1:1 calls for community members post-Day 30. Notion stage updates.
- **Salar** — 1st Intent BD Campaign for community (Day 10–21). All outbound + sourcing fulfillment for retainers. Weekly retainer reporting call (post-launch).
- **Shmookh** — ContentOS client fulfillment (when scoped).
- **Community Manager (vacant)** — Day 30+ community check-ins. Currently covered by Daniyal as interim.

### C. Notion update cadence
- Every client gets a row in `Client Tracker` within 24h of deal close.
- Stage transitions happen the same day the milestone is hit. Daniyal owns this.
- `At Risk (Auto)` formula already flags lateness — review weekly in Monday team sync.

### D. Comms artifacts that MUST exist per client
**Community-only:**
- 90-Day Roadmap deliverable (generated via `roadmap-generator` skill, sent within 48–72h of roadmap call)
- Skool DM thread with Reyhan
- Optional: Slack channel only if client requests one (default = no channel for community-only)

**Retainer (mandatory, no exceptions):**
- Dedicated Slack channel named `#client-{slug}`
- Drive folder at `Clients/{Client Name}/` with subfolders: `Discovery`, `Implementation`, `Deliverables`, `Reporting`, `Contracts`
- Discovery + Implementation doc(s) — one per offering if multiple engines
- Pinned 90-day timeline in Slack (use the retainer SOP timeline as the template)
- Recurring weekly call on calendar (Reyhan + Salar + client)

### E. Day 90 retainer renewal — always offered
At Day 75, prep the renewal pitch. At Day 90, deliver the pilot report + offer 6-month extension at the same rate (default) or a discounted rate if scope or pricing needs to flex. Never let a retainer hit Day 90 without a renewal conversation.

### E1b. Launch call runs off the locked template (LOCKED 2026-07-09)
Every retainer launch call uses `launch-call-template.md` in this skill folder. Reyhan asks the questions live, Fireflies records, and post-call Claude pulls the transcript and files the answers into the template structure inside the client's Discovery doc. Includes the access-checklist gate and the pilot-goal framing. Never run a launch call freehand.

### E2. Under-delivery fallback — 30-day free extension (LOCKED 2026-07-09)
When a pilot or retainer account is under-delivering at renewal time (weak reply/meeting numbers, client questioning ROI, or client signalling wind-down), the DEFAULT fallback is: offer a 30-day extension free of cost so the new experiments run through enough data and deliver ROI. Always pair the offer with: (1) genuine thanks for their support, (2) explicit reassurance there is no auto-charge and no further payments are due (pilot payments already completed), (3) zero payment pressure. Offer this BEFORE accepting any wind-down. First used: Daniel Cheetham (Captains Club), 2026-07-09.

### F. Send the SOPs to Daniyal when asked
The two SOPs in this folder are written for Daniyal to implement in Notion + update his existing onboarding SOPs. When Reyhan asks "send these to Daniyal", paste both SOP files verbatim into Slack/Notion. Do not summarize or shorten.

## Files in this skill

- `SKILL.md` — this file. Invocation + locked rules.
- `sop-community-onboarding.md` — Skool member onboarding SOP. Day 0–30 sprint + Day 30+ steady-state.
- `sop-retainer-onboarding.md` — Retainer client onboarding SOP. Phase 0–3 (Day 0–90) pilot delivery with the signal engine, lead targets, [T]/[C]/[A] templatization tags, Definition of Done per phase, and the 5-positive-reply guarantee.
- `capacity-model.md` — phase-weighted load model (4 ideal / 5 max per GTME), current 12-client map, hiring shape, and stagger calendar rules.
- `new-hire-roles-training.md` — Community+Assist and GTME-in-training role definitions + 30-day copywriting/sales/GTM curriculum.
- DeliveryOS schema lives in `projects/deliveryos/deliveryos-schema.md` — the Supabase build spec that becomes the system of record (replaces Notion tracking).

> **Note (2026-06-13):** Salar is offboarding. The retainer SOP now uses a generic "assigned GTME" owner instead of Salar-specific ownership. Accounts re-home per `capacity-model.md`.

## Backlog / Next Builds

- [ ] Slack channel naming + Drive folder auto-creation script (Daniyal)
- [ ] Stripe webhook → Notion row create automation (Daniyal, n8n)
- [ ] Day-N reminder bot in #ops Slack channel — pings owner when a client hits a milestone target date (Daniyal, n8n)
- [ ] Community Manager hire — owns Day 30+ check-ins for community members
- [ ] Pilot report template — used at Day 90 for every retainer
