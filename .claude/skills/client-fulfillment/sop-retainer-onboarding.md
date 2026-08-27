# SOP — Retainer Client Onboarding (Managed Pilot $2,500/mo+)

**Audience:** Assigned GTME (owns the account end-to-end). Daniyal (Claude builds + DeliveryOS + ops). Reyhan (launch call + Day 90 renewal). Community/Assist hire (supports lists, enrichment, QA).
**Trigger:** Retainer agreement signed + first payment processed.
**Outcome:** Client launched within 5 days, hitting cumulative outbound milestones across the 90-day pilot, with a Day 75 analysis report + Day 90 pilot report + 6-month extension offer.
**System of record:** DeliveryOS (client record + stage + targets). Notion Client Tracker mirrors until DeliveryOS migration completes.

> **Tags used in this SOP:** `[T]` = templated / build-once-reuse-everywhere · `[C]` = custom thinking per client · `[A]` = automated. Target ratio across the whole pilot: **~70% [T]/[A], ~30% [C].** If standing up a new client takes more than ~1.5 days of unique [C] work, a template is missing — flag it.

> **Data flow (locked):** **Clay** (TAM, lists, signals — internal system of record) → **DeliveryOS** (client-facing dashboard + dial/engage lists + tracking) → **Instantly / HeyReach** (sending). Claude OutboundOS skill (Prospeo + exa) layers on top of Clay to boost lead counts per signal.

> **Capacity rule (locked):** ideal **4 clients/GTME, max 5.** Never let one GTME have more than **2 clients in build-month (Phase 1) at the same time** — stagger onboarding starts. A Phase-1 client carries ~3x the load of a Phase-3 client. See `capacity-model.md`.

---

## Phase 0 — Onboarding (Week 0, Day 0–5)

**Stage:** `Launch Call & Prep`

### Day 0 — Deal Closes (Owner: assigned GTME + Daniyal)
Triggers: agreement signed, first payment received, deal moved to "Closed Won" in Attio.

- [ ] Create DeliveryOS client record (+ mirror Notion row) within 24h **[A]** (target: Stripe/Attio → DeliveryOS auto-create)
  - Client / Agency · Engine (OutboundOS / SourcingOS / ContentOS) · Deal Closed Date · Amount · Niche · Assigned GTME · Stage = `Launch Call & Prep`
- [ ] Create Slack channel `#client-{slug}` (invite client + Reyhan + GTME + Daniyal) **[T]**
- [ ] Create Drive folder `Clients/{name}/` → `Discovery/ Implementation/ Deliverables/ Reporting/ Contracts/` (drop signed agreement) **[A]**
- [ ] Send welcome email via `email-writer` skill: Slack invite + Drive link + Calendly for launch call within 3 business days **[T]**

### Day 0–2 — Pre-Launch Prep (Owner: GTME)
- [ ] Read signed agreement + closing-call transcript **[C]**
- [ ] Pre-fill Discovery doc: niche, ICP, current stack, current MRR, pain points, agreed deliverables **[C]**
- [ ] Draft 90-day implementation timeline (template at bottom) **[T]**
- [ ] Pre-write Slack pinned post (timeline + contacts + weekly call slot) **[T]**

### Day 3–5 — Launch Call (Owner: Reyhan + GTME; Daniyal silent)
- [ ] Reyhan re-states pilot goal, deliverables, how success is measured
- [ ] GTME walks the 90-day timeline
- [ ] **Collect all logins + access:** CRM, ATS, mailboxes/auth, LinkedIn, brand assets, website access (for lead magnet page) **[T]** access checklist
- [ ] Confirm weekly recurring call day/time (GTME runs; Reyhan joins Day 30/60/90)
- [ ] Action items captured as a Slack checklist

**Post-call (same day):** pin timeline in Slack · Stage → `Build in Progress` · schedule recurring weekly call.

> **🚦 GATE — no build work starts until logins + access are confirmed.** A client missing access on Day 5 is the #1 cause of a blown Phase 1. Flag in #ops if not resolved within 48h of the launch call.

---

## Phase 1 — Foundation & First Launch (Day 1–30)

**Stage:** `Build in Progress` → `Launched`. **Owner: GTME** (Claude DFY: Daniyal)

**Targets:** ≥2,000 email leads + 500 LinkedIn leads launched. Strongest-signal leads → LinkedIn first.

- [ ] **TAM analysis** → TAM Companies + TAM People tables in **Clay**. ICP-matched 1st-connections also go into TAM. **[C]** TAM/ICP definition · **[T]** Clay table blueprint
- [ ] **Lead magnet** via Claude lead-magnet skill — authentic value on "evolution of recruitment in {niche}": what recruitment system to run, usable by the ICP. Publish live on client's site with a capture form. Send link as the lead magnet. **[T]** generator · **[C]** niche angle
- [ ] **1st-connection nurture** — conversational copy angle on the niche's evolution + how they're coping. **[C]**
- [ ] **2 campaign copies:** (1) no-signal + simple AI line, (2) signal-matched + AI line. **[T]** copy frameworks · **[C]** the lines
- [ ] **Build 2 signals** beyond 1st-connection nurture. Split data → signal tables + 1 non-signal table. **[T]** signal recipes · **[A]** Clay enrichment
- [ ] **Boost lead counts** per signal with Claude OutboundOS skill (Prospeo + exa) on top of Clay. **[A]**
- [ ] **Deploy Claude Code DFY setup** (Daniyal). **[T]**
- [ ] Launch: LinkedIn (strongest signal first, ≥500) + Email (≥2,000). Replies route to Slack + DeliveryOS. **[A]** reply routing

**✅ Definition of Done — Phase 1:** lead magnet live + capturing · 2 signals running · ≥2,000 email + 500 LinkedIn launched · Claude DFY deployed · baseline metrics visible in DeliveryOS.

**Day 30 — Baseline Locked (Owner: GTME + Reyhan):** deliver Month 1 report (volume, open/reply/positive-reply, conversations, bottlenecks, Month 2 plan). Reyhan joins the weekly call. Log baseline in `Reporting/` + DeliveryOS.

---

## Phase 2 — Scale & Multichannel (Day 31–60)

**Stage:** `Launched`. **Owner: GTME**

**Targets:** +1,500 email + 500 super-targeted LinkedIn (cumulative ≥3,500 email + 1,000 LinkedIn).

- [ ] **+2 more signals** (Claude or Clay). **[T]/[A]**
- [ ] **2nd-connection ICP-match campaign** on LinkedIn. **[C]**
- [ ] **Newsletter** set up to the warm audience + 3-step welcome sequence. **[T]** sequence template
- [ ] **AI auto-reply** deployed *only if* the client can't convert messages → meetings themselves. **[T]**
- [ ] Run cumulative toward **4 distinct intent-based playbooks** (email + LinkedIn each), first A/B split test live.

**✅ Definition of Done — Phase 2:** 4 intent-based multichannel campaigns live · newsletter sending + welcome sequence live · auto-reply live where needed · ≥3,500 email / 1,000 LinkedIn cumulative.

**Day 60 — Conversation Checkpoint (Owner: GTME + Reyhan):** confirm cumulative **10+ positive responses**. If below → escalate to Reyhan, build recovery plan, don't wait. Reyhan joins the weekly call.

---

## Phase 3 — Optimise & Prove (Day 61–90)

**Stage:** `Scaled`. **Owner: GTME + Reyhan (renewal)**

- [ ] **+1 unusual signal** — alumni, marketing spend, or zipcode. **[T]** recipe
- [ ] **Refresh all no-reply lists** from Months 1–2 → re-run through the best-performing angle. **[A]** list refresh
- [ ] **Day 75 — detailed analysis report** (75 days post-launch). **[T]** report template
- [ ] **🎯 Guarantee gate:** if **< 5 positive replies** by Day 75 → offer the client either (a) free meta-ad setup (client- or candidate-targeting) **or** (b) 3 weeks of content done-for-them. Client's choice.
- [ ] **Day 90 — pilot report + 6-month extension offer** (Reyhan).

**✅ Definition of Done — Phase 3:** 5th signal live · no-reply lists refreshed + re-run · Day 75 report delivered · guarantee resolved (not triggered, or fulfillment scheduled) · Day 90 renewal call held.

> **Define "positive reply" precisely** (interested / asked a question / booked) and track the live count in DeliveryOS so the guarantee never surprises you. **Budget the guarantee's cost** — free meta ads or 3 weeks content = real GTME hours. Track the trigger rate; a high rate means the upstream signals/copy need fixing, not a bolt-on.

### Day 90 — Outcome paths
- **Renew:** restart timeline at fresh Day 0 for the 6-month extension. Same GTME continues.
- **Not renew:** Stage = `Completed`. Move to alumni. Final invoice + handover doc.
- **Churn:** Stage = `Churned`. Reyhan personal call. Log learnings in `decisions/log.md`.

---

## The Always-On Signal Engine

Run a **30-day signal refresh** across each client's TAM (cron). This alone generates more than enough leads for 90 days.

**Signal library (build each once as a Clay/Claude recipe, reuse on every client):** `[T]`
Open Jobs (3 job boards) · 1st connection · 2nd connection · 90-Day Job Change · Backfill (reverse 90-day JC) · Career Page · Recent LinkedIn Post · Alumni · Marketing Spend · No Internal HR.

Phase 1 = 1st-conn nurture + 2 signals. Phase 2 = +2 signals. Phase 3 = +1 unusual signal. By Day 90 every client has 6 live signal sources feeding a self-refreshing pipeline.

---

## Weekly Cadence (locked, Day 5 onward)

- **Weekly client call** (GTME, 30 min). Reyhan joins Day 30 / 60 / 90.
- **Weekly Slack update** (GTME, before the call) into `#client-{slug}`: this week's numbers (volume, opens, replies, positive replies) · what we built · what's blocked / needs client input · next week's plan.
- **Monday QA ritual (team):** every active client scored against its current-phase Definition of Done in DeliveryOS. Anything red → flagged in #ops. *This is the mechanism that guarantees identical quality across all clients.*

---

## Daniyal's Implementation Checklist (DeliveryOS + Automations)

1. **Stripe/Attio → DeliveryOS auto-create** — new retainer creates client record + Drive folder + Slack channel.
2. **30-day signal-refresh cron** — re-runs each client's signal recipes against their TAM, pushes new leads to DeliveryOS dial/engage lists.
3. **No-reply refresh job** — pulls Month 1–2 no-replies, re-queues into best-performing angle.
4. **Day-N reminder bot** (daily 9 AM UK): Day 30 baseline · Day 60 < 10 responses → ping Reyhan + GTME · Day 75 < 5 positive replies → trigger guarantee flag · Day 75 renewal prep · Day 90 escalate.
5. **DeliveryOS stage + target tracking** — see `deliveryos-schema.md` for the field spec.

---

## 90-Day Timeline Template (Slack pin)

```
🚀 90-DAY PILOT TIMELINE — {Client Name}

Phase 0 (Day 0–5): Onboarding
  • Logins + access collected, Slack + Drive live
  • Launch call + 90-day timeline pinned

Phase 1 (Day 1–30): Foundation & first launch
  • TAM + 2 signals built in Clay
  • Lead magnet live on your site
  • 2,000 email + 500 LinkedIn launched
  • Claude Code DFY deployed
  • Day 30 — baseline locked

Phase 2 (Day 31–60): Scale & multichannel
  • +2 signals · 2nd-connection LinkedIn campaign
  • Newsletter + 3-step welcome live
  • +1,500 email / +500 LinkedIn
  • Day 60 — 10+ positive responses

Phase 3 (Day 61–90): Optimise & prove
  • +1 unusual signal (alumni / ad spend / zipcode)
  • No-reply lists refreshed + re-run
  • Day 75 — detailed analysis report
  • Day 90 — pilot report + 6-month extension

Weekly call: {day/time} · Daily comms: this channel · Reporting: DeliveryOS + Drive/Reporting/
```
