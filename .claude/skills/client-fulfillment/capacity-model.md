# Capacity & Stagger Model

How many clients a GTME can actually hold, and how to schedule onboarding so nobody catches fire.

---

## The load-weighting principle

Headcount ÷ clients is the wrong math. A client in **build month** is ~3x the work of a client in **steady state**. Capacity is about how many clients are in *which phase at the same time*, not the raw count.

**Phase load weights:**
| Phase | What's happening | Weight |
|---|---|---|
| Phase 1 (Day 1–30) | TAM, lead magnet, signals, first launches | **3** |
| Phase 2 (Day 31–60) | Scale, +signals, newsletter, auto-reply | **2** |
| Phase 3 (Day 61–90) | Optimise, refresh, reports, renewal | **1** |
| Renewed / steady | Maintenance only | **1** |

**A GTME's capacity ceiling = 10 load points.**
- 4 steady clients = 4 points → comfortable (the "ideal 4").
- 5 steady clients = 5 points → fine (the "max 5", once they're past build).
- But **2 Phase-1 clients alone = 6 points.** Add three steady = 9. That's a full GTME. A *third* Phase-1 client (9 points just from builds) is the danger zone.

**Hard rule: no GTME holds more than 2 Phase-1 clients at once.** Stagger new starts so builds don't stack.

---

## Current state (12 clients) — mapped

| GTME | Clients | Notes |
|---|---|---|
| Shmookh | 5 | At max — keep here, don't add |
| Daniyal | 4 | + Claude builds + DeliveryOS + (community until new hire lands) |
| Reyhan | 3 | **Stopgap** — Salar offboarding patch, exit by ~Day 60 |
| New community/assist hire | 0 accounts | Takes community off Daniyal + assists on lists/enrichment/QA |

**Reality check:** real account-carrying capacity = Shmookh 5 + Daniyal 4 = **9 steady**. Reyhan's 3 is not a system. At 12 clients you are at theoretical max with **zero buffer and zero growth capacity.**

---

## The growth problem

Q2 goal = **+5 retainers/month → $60k.** You cannot land 5 new clients/month onto a team whose only spare hands are a community assistant — every new client is a Phase-1 (weight 3) load spike, and there's nowhere to put it.

**Required capacity to grow:** each block of 5 new clients ≈ 1.25 GTMEs once they pass build. Account capacity — not community — is the bottleneck.

### Recommended hiring shape
- **Hire 2 juniors, not 1** (the "2 hungry for the same money" instinct is correct):
  - **Hire A — Community + Assist:** takes community off Daniyal week one; assists GTMEs on list-building, enrichment, QA. Learns the engine by doing.
  - **Hire B — GTME-in-training:** shadows 30 days, carries 1–2 accounts by Day 60. This is the capacity that lets you take May/June retainers.
- If budget allows only one now: hire **A**, and **lock a date for B within 45 days.** Don't let it drift.

### Target end-state (team of 4–5, growth-ready)
| GTME | Steady ceiling | Role |
|---|---|---|
| Shmookh | 5 | Senior GTME |
| Daniyal | 4 | GTME + Claude builds + DeliveryOS (protect — don't overload) |
| Hire B (GTME-in-training → GTME) | 2 → 4 | Ramps to full load by ~Day 90 |
| Reyhan | 0 | **Exit accounts by Day 60** — back to Coach/Architect |
| Hire A (Community + Assist) | 0 accounts | Community + cross-account support |

That's a 12-client floor with room to grow to ~13–15 as Hire B ramps — and Reyhan out of operator mode, which is the Q2 definition of a good quarter.

---

## Stagger calendar rules

1. **Max 2 Phase-1 clients per GTME at any time.** Before assigning a new client, check the capacity board in DeliveryOS — if the GTME already has 2 in Phase 1, route elsewhere or delay the start.
2. **Space new starts ~2 weeks apart per GTME** so a build finishes (drops to weight 2) before the next begins.
3. **When closing 5/month, spread starts across the team and across the month** — don't let four Day-0s land in the same week.
4. **Reyhan's 3 stopgap accounts** transition to Hire B as they pass Phase 1 (lower handover cost when they're in steady state).

---

## DeliveryOS hook

The `capacity board` view (see `deliveryos-schema.md`) computes live load per GTME using the phase weights above and flags:
- any GTME over 10 points,
- any GTME with >2 Phase-1 clients,
- the best home for the next incoming client.

Review it in the Monday team sync before assigning any new deal.
