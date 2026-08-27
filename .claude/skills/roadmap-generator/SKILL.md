# Skill: 90-Day Roadmap Generator

Generate a personalized 90-Day Roadmap for every new RecruiterGTM community member after their 1-hour audit session with Reyhan.

## How to Invoke
`/roadmap-generator` followed by:
- Fireflies transcript or call notes from the audit session, OR
- Manually pasted discovery answers

---

## Locked Rules

### ⛔ STEP 0 — HARD GATE: invoke `content-os` BEFORE writing a single line (re-flagged 2026-08-22)

**You may NOT draft, assemble, or edit any roadmap copy — cover, section intros, pillar headings + body, CTA callouts, milestone/next-step cells, tech-stack "why" cells, or the Skool DM — without first invoking the `content-os` skill in this session.** Drafting off the template (or "the rules are already in context") does NOT satisfy this. This is the roadmap-specific application of the CORE rule "never write copy without INVOKING the relevant writing skill" and of Rule S below.

**Order of operations (non-negotiable):**
1. Extract discovery data.
2. **Invoke `content-os`** → load its Section A–M taste rules + copy-engine loop + humanizer. Write ALL copy through them.
3. Build the HTML.
4. QC (≥2 subagents) INCLUDING a ContentOS-taste pass: banned-word grep, em-dash sweep, negation-parallel + "saying-what-it-isn't" filler, and the "every `<h2>` states a concrete picturable point" check.

**Why re-flagged 2026-08-22 (Ricky Paloy roadmap):** the deck was drafted straight off the template + generic QC subagents, `content-os` was never invoked, and it shipped with a vague filler heading ("The one thing the next 90 days is for"), 85 em-dashes (drama-dash AI tell), negation-parallels ("the move isn't to abandon that — it's to add…"), and "saying-what-it-isn't" lines ("not generic", "the system, not the willpower"). Reyhan: *"fix this whole deck and make sure it's saved in skill memory to always use this skill for writing."* If `content-os` was not invoked this session, STOP and invoke it before touching copy.

**Heading test (every `<h2>`):** could this heading sit on any other client's deck? If yes, it's filler — rewrite it to state the concrete point in Reyhan's plain, practitioner voice. Banned template carry-overs: "The one thing the next 90 days is for", "The system, not the willpower", any "X, not Y" / "not just X" heading. Em dashes: default to periods/colons in flowing prose; keep only for label separators, natural-speech quotes, and hook headlines.

---

### A. 5-pillar order (FIXED — updated 2026-08-06, mirrors the Engine Framework DIY course stages, see community-os Rule B3)
Every roadmap (discovery doc + polished HTML + community proposal 12-mo framing) uses this exact order — the same order members meet the stages in the DIY course (S1 RecruiterOS → S2 OperatorOS → S3 OutboundOS → S4 TrackingOS → S5 ContentOS):

1. **Pillar 1 — Productization**
2. **Pillar 2 — AI Layer**
3. **Pillar 3 — Multichannel Outbound**
4. **Pillar 4 — ATS + Newsletter**
5. **Pillar 5 — Content + Authority**

- A1. NEVER reorder by primary focus. Primary focus dictates depth/emphasis inside each pillar, never pillar position.
- A2. Pillar overview slide (5-card grid) lists 01 → 05 in this order.
- A3. Day 30/60/90 milestones table columns: Productization · AI · Outbound · ATS+News · Content.
- A4. The 2026-05-09 order (AI first, Productization last) is REPEALED — Reyhan flagged 2026-08-06 that roadmap pillars must match the DIY course stage order so Skool learning and the build move together. First roadmap on the new order: Jennifer Wolf.
- A5. Previously delivered roadmaps on an older order are done — do not retro-fit unless the client asks.

### B. RecruiterGTM-owned commitments (3 + 1) — locked 2026-05-29
Every roadmap shows the 3 things RecruiterGTM ships + the 1 thing the client books:

**RecruiterGTM owns:**
- B1. **Day 3** — 90-Day Roadmap delivered (this document IS the Tech Benchmarking + Systems Roadmap — never list both as separate artifacts).
- B2. **Day 17** — Custom Claude Ops Manager delivered (built by Daniyal in the 7 days following the Day 10 combined onboarding call).
- B3. **Day 22** — Intent-based BD Campaign launched (built by Komal in the 12 days following the Day 10 combined onboarding call. List, copy, sequence pushed live on the client's tools).

**Client owns:**
- B4. **Day 10** — Fill the pre-call form + book + attend the **single 30-min combined onboarding call** with Komal (Head of Fulfilment) + Daniyal (Ops Manager). One call, both leads on it — Komal collects ICP / target signals / copy direction; Daniyal collects stack / content themes / Claude Ops Manager context. Both initiate their builds after this single call.

Frame verbally: **"3 things on us, 1 thing on you."** No separate Day 15 BD kick-off call. No separate Daniyal call. No separate "Day 21 Tech Benchmarking" deliverable.

**Why locked (2026-05-29):** Reyhan flagged that the old two-call structure (Day 10 Daniyal + Day 15 Salar) was wasting a 30-min slot per client on both sides. The combined onboarding call covers everything both leads need to start building. Subsequent feedback / iteration calls happen organically during the build phase — they do NOT get listed in the roadmap.

**HARD RULE — never mention additional kick-off, scoping, or feedback calls beyond the single Day 10 onboarding call.** The roadmap shows exactly one client-booked call. Feedback calls happen during deployment but stay out of the deliverable.

### C. "Prepared for" format (shared with proposal-generator)
- C1. The `meta-value` next to "Prepared for" shows ONLY the founder name(s). NOT the company name. NOT both.
- C2. Single founder: `Prepared for: Matt Gorgolinski`. Two partners on the call: `Prepared for: Tom Wood & Jon Humphries` (use `&`, not "and", not comma).
- C3. The company name goes in a separate "Company" meta-value field below "Prepared for".
- C4. Same format applies to header sticky bar — no company name there either.

### E. Discovery doc prices override everything (locked 2026-05-14)

**Hard rule:** the discovery doc is the canonical source of truth for tool prices on a per-client basis. Never invent or estimate a price for a line that the client filled into their discovery doc.

**Decision tree before quoting ANY tool price in a roadmap:**

1. **Is the price written in the client's discovery doc?** &rarr; Use that exact figure. Even if it differs from public retail or partner pricing, the client's stated cost is canonical for THEIR roadmap.
2. **Is the tool in `memory/feedback_never_assume_tool_prices.md` with a confirmed price?** &rarr; Use that figure. (Pin.com $160, Claude Max $100, HeyReach $59 partner, Instantly $73 partner, HyperTide $75 partner, Apollo Pro $99, Prospeo Growth $89, Apify $39, Lusha Professional $69.90, FullEnrich Pro $55, n8n Cloud $24.)
3. **Is the tool's public retail pricing easily verifiable and stable?** &rarr; WebFetch the official pricing page, cite the source in the doc, use the exact figure.
4. **Otherwise &rarr; STOP. Leave the price field blank or marked "pending" and ASK Reyhan.** Do NOT estimate. Do NOT extrapolate per-seat math to team size. Do NOT assume the standard tier.

**Why:** Reyhan flagged 2026-05-14 that I invented RecruitCRM at $300/mo (for team of 5) and Zapier at $50/mo for Frederic's roadmap. Neither figure was in the discovery doc. The discovery doc had RecruitCRM and Zapier listed as tools but no prices. I treated absence as license to estimate &mdash; wrong move. The client may pay something completely different.

**How to apply when assembling a tech stack audit:**
- Parse the discovery doc Systems Audit table. For every row, extract the tool name AND the price (if listed).
- For each tool, classify into: (a) priced in doc &rarr; use that; (b) priced in memory &rarr; use that; (c) public stable price &rarr; WebFetch + cite; (d) unknown &rarr; ASK before shipping.
- Cost summary should show partial totals when prices are pending, NOT a fake aggregate. Example: "~$839/mo + RecruitCRM + Zapier" with a note "RecruitCRM + Zapier amounts pending from Frederic."
- Never round up to a "clean" number to avoid asking. The roadmap is a delivery artifact &mdash; wrong prices erode trust faster than a partial number does.

### D. Each pillar slide MUST have a "What RecruiterGTM Does Here" CTA (locked 2026-05-14)

Every pillar slide ends with a violet-bordered callout that makes the value RecruiterGTM provides crystal clear. Without these, the client reads the roadmap as "things we should do" instead of "things RecruiterGTM is going to help us do." The CTAs convert it from a plan into a partnership.

**Placement:** Bottom of each pillar slide, after the existing cards. Use this HTML pattern:

```html
<div style="margin-top:20px;background:rgba(138,0,255,0.06);border:1.5px solid var(--violet);border-radius:14px;padding:18px 24px;z-index:1;position:relative;">
  <div class="label" style="margin-bottom:6px;">What RecruiterGTM Does Here</div>
  <p style="font-size:14.5px;color:var(--ink-soft);line-height:1.55;margin:0;">[CTA text per pillar]</p>
</div>
```

**Standard CTA pattern per pillar** (customize the specifics per client):

- **D1. AI Layer:** *"Daniyal builds your custom Claude Ops Manager in the next 10-14 days. You start buying back ~[X] hours/week immediately on [client's manual work]."* The X hours is concrete — pulled from the discovery doc (manual MPC time, sourcing time, list-building time, invoicing time, etc.).

- **D2. Multichannel Outbound:** *"Komal launches your 1st intent-based BD campaign ([Playbook #1 name]) live on your tools by Day 22. You then copy the concept across [Playbook #2 + #3]."* Name the specific playbook from this client's plan.

- **D3. Content:** *"We give you 10 starter topics based on your positioning + content themes. Claude Ops Manager takes each topic from idea → full post in your voice."* Always 10 topics. Always tied to the client's specific positioning.

- **D4. ATS + Newsletter:** *"By Day 30: [X] clients + [Y] candidates tagged + cleaned in [client's ATS]. Data cleanup is the main goal — clean inputs = the engines actually work."* Pull X and Y from the discovery doc targets.

- **D5. Productization:** *"We build the side-by-side comparison deck for the new offer variations ([Offer A] vs [Offer B] vs [Offer C]). Claude drafts the variations. You send to [target audience]. We iterate together."* Name the specific offers from this client's Pillar 5.

**Why:** Reyhan flagged 2026-05-14 that the original pillar slides described WHAT happens in each pillar but didn't make explicit WHO does it and WHAT VALUE the client gets from RecruiterGTM. Without the CTAs, clients read it as a generic plan. With them, it reads as a specific partnership with named people delivering named outcomes.

**How to apply:**
- Every new roadmap MUST have a CTA card on every pillar slide.
- Customize each CTA with the client's specific numbers, tools, and offers — not generic copy.
- The hours/candidates/client counts come from the discovery doc, not assumptions.

### F. Action-step label discipline — never overclaim what RecruiterGTM does (locked 2026-05-20)

The "What RecruiterGTM Does Here" callout is ONLY for pillars where RecruiterGTM genuinely ships the work (Pillar 1 — Daniyal builds Claude, Pillar 3 — Komal launches the BD campaign). For pillars where the client owns the work, the callout label MUST change.

**Three approved callout labels (pillar numbers per the 2026-08-06 locked order):**

1. **"What RecruiterGTM Does Here"** — only when we deliver. Pillar 2 AI Layer (Daniyal builds Claude) and Pillar 3 Outbound (Komal launches BD).
2. **"Your Action Step"** — when the client owns the work end-to-end. Pillar 1 (Offer productization) and Pillar 4 (ATS cleanup). Lead with `**[Client first name]:**` and state the concrete task + due date.
3. **"We provide / Your action"** — split label when we provide an asset and they execute. Pillar 5 (Content): we provide the 10 topics + Claude content skill; they record voice notes + approve + post.

**Why locked:** Reyhan flagged 2026-05-20 that "By Day 30: 1,000 clients + 100 candidates tagged + cleaned in Loxo" sits under "What RecruiterGTM Does Here" — but RecruiterGTM doesn't do the cleanup, the client does. Misleading callouts erode trust on the first read. Match the label to who actually does the work.

**How to apply:** Audit every pillar's callout before shipping. If the action belongs to the client, relabel to "Your Action Step" and lead with the client's first name + the concrete task.

### G. Content pillar (Pillar 5 in the locked order) — list the 10 starter topics inline as a dedicated slide (locked 2026-05-20)

Whenever a pillar 4 (Content) CTA references "we give you 10 starter topics," those 10 topics MUST appear inline as the NEXT slide. Never reference an asset we don't deliver in the roadmap itself.

**How to apply:**
- The Content pillar slide ends with the "We provide / Your action" callout that references the next slide.
- Insert a dedicated slide titled "Pillar 5 — 10 Starter Topics" (or "Pillar 05 — Content Engine") immediately after.
- The slide uses the `card-grid card-grid-2` layout with 10 numbered cards.
- Each card has: topic number (01-10), the topic headline, and a 1-line angle/strategic purpose (e.g. "BD pain-point post that warms prospects for Playbook 3").
- Topics must be tied to the client's specific niche, geography, ICP, and offer mix — pulled from the discovery doc, not generic.
- Mix the 10 across BD pain-point, success stories, market-data authority, niche-defining, candidate-MPC, and offer-conversation-priming themes. Default split: 7 BD-driven + 2 candidate-MPC + 1 offer-warm-up.

### H. Pillar 4 ATS — mandatory two-part exercise (locked 2026-05-20)

Every roadmap's ATS pillar (Pillar 4 in the locked order — "ATS + Newsletter") MUST include these two client-owned exercises as concrete tasks in the pillar slide. Without them, the BD engine and the nurture campaigns have nothing clean to run on.

**Exercise 1 — Candidate-side ATS cleanup (for nurture sequence):**
- Action: categorize candidates for the client's TOP 2 ROLES (pulled from discovery doc — "Which 3 roles make you the highest fees?" question).
- Ensure: updated contact info (email + phone + LinkedIn URL) on every record.
- Ensure: correct tags (role-fit tag, source tag, last-contact-date tag).
- Ensure: correct custom fields filled (status, willingness to relocate, salary expectation, etc.).
- Outcome: enables launching a candidate nurture sequence on the cleaned subset.
- Due: Day 30.

**Exercise 2 — Client-side BD cleanup (for client nurture campaign):**
- Action: track at least **50 previous BD conversations** in the ATS / CRM client pipeline.
- Ensure: contact info + last-conversation-date + status (cold, warm, dead, win, etc.).
- Outcome: enables launching a client-side BD nurture campaign on the cleaned 50.
- Due: Day 30.

**How to apply:**
- Place both exercises in the Pillar 4 slide as numbered cards or list items, clearly labeled as "Exercise 1" and "Exercise 2".
- The "Your Action Step" callout at the bottom of the slide references both exercises.
- Both exercises map to the client's actual ATS (Loxo, Recruiterflow, Bullhorn, Stardex, etc.) — name the tool explicitly.
- The "top 2 roles" come from the discovery doc Section 4 Pillar 5 (Offer Productization) → highest-fee roles answer. If the answer lists 3 roles, pick the top 2 by fee value.

**Why locked:** Reyhan flagged 2026-05-20 that the ATS pillar was too abstract ("1,000 clients tagged"). These two concrete exercises convert it from a target into a specific, measurable week-1 task that unlocks two downstream engines (candidate nurture + client BD nurture).

### I. Next Steps table — must include the 2 RecruiterGTM-delivers rows (locked 2026-05-20)

Every roadmap's Next Steps table MUST contain two explicit rows for the RecruiterGTM-owned delivery commitments — visually marked with a violet `[RecruiterGTM delivers]` tag so the client can see what's on us vs. on them at a glance.

The two rows (tailored to the client's stack and playbook):

1. **Day 17:** `[RecruiterGTM delivers] Daniyal ships custom Claude Ops Manager — [client's specific 4 skills]` · Owner: RecruiterGTM
2. **Day 22:** `[RecruiterGTM delivers] Komal pushes 1st BD campaign live on [client's specific tools] ([client's specific playbook name])` · Owner: RecruiterGTM

**Why locked:** Reyhan flagged 2026-05-20 that Christine's Next Steps table assigned every row to the client and showed nothing on RecruiterGTM's side — making it look like she was doing all the work alone. Without these two rows, the roadmap reads as a punch-list of client homework instead of a partnership with named deliverables.

**How to apply:**
- Tailor the skill names + tool list + playbook name to the actual client, never boilerplate.
- Use the violet `[RecruiterGTM delivers]` tag pattern: `<strong style="color:var(--violet);">[RecruiterGTM delivers]</strong>`.
- These two rows are in addition to (not replacing) the implicit Day 3 Roadmap delivered row at the top of the table.

### J. Upsell Opportunities — write to Attio list at delivery time (locked 2026-05-21)

Every roadmap MUST identify 1-3 future upsell opportunities for the client and write them to the **Attio "Upsell Opportunties" list** (list ID `37f86ca4-062a-4be3-b54d-7fe1aad6d8db`, parent object `people`).

**What counts as an upsell opportunity (examples):**
- Offshore Hire (placement fee)
- Retained / Engaged pilot
- ContentOS lite or full
- SourcingOS managed retainer
- GTM Engine Management retainer (~$2-2.5K/mo)
- Additional BD campaign launches beyond the first
- ATS migration support
- n8n / workflow automation builds
- New secondary offer launches (e.g. Charles's Monarch, Rick's Recruitment Systems Partner)
- Paid community rejoin (for unpaid Skool members)

**Schema:**
- The list's `opportunity` field is a SELECT dropdown — use one of the existing options (ask Reyhan for the current option list if unsure; never invent options via free-text or the API will 400-error).
- All other detail (timing, estimated value, signal, source roadmap file) goes in a Note attached to the Person record, titled `Upsell — [Short headline]`.

**How to apply:**
1. At roadmap delivery time, identify 1-3 upsell opportunities from Pillar 5 (Offer), the Next Steps table (Day 60+ items), and any "M2+" deferred work.
2. For each opportunity:
   - Find the client's Person record in Attio (`search_records` with their email).
   - Add them to the Upsell Opportunties list via `manage-list-entry` (Mode 1) — set `opportunity` to the matching select option.
   - Create a Note on the Person record (`create_note`) with the full upsell detail: trigger, earliest date, estimated value, who advises, source roadmap file.

**Why locked:** Reyhan flagged 2026-05-21 that future upsells were getting buried inside roadmap Next Steps tables with no team-wide visibility. The Upsell Opportunties list + per-record Notes solve this — the team can query the list every Friday GTM call and the per-record notes carry the context.

### K. Next Steps table — rows ALWAYS sorted ascending by Day N (locked 2026-05-21)

**Hard rule:** every row in the Next Steps table must be in ascending Day order. No exceptions. Rows with `Day 3` appear before `Day 5`, which appear before `Day 7`, etc. Rows with `Ongoing` or no day at all go at the bottom.

**Why locked:** Reyhan flagged 2026-05-21 that James Hine's roadmap shipped with rows out of order — `Day 3 → 5 → 5 → 10 → 15 → 14 → 14 → 30 → 30 → 21 → 30 → 17 → 22`. The Day 17 + Day 22 RecruiterGTM-delivers rows were appended at the end of the config, and earlier rows (Day 14, Day 21) sat below later rows (Day 30). It reads as chaotic and breaks trust on the first eyeball.

**How to apply:**
- The render-helper for the Next Steps table MUST sort rows by extracted "Day N" before rendering. Reference implementation in `generate_batch2.py`:
  ```python
  def _sort_next_steps_rows(rows):
      import re
      def day_key(row):
          m = re.search(r"Day\s+(\d+)", row)
          return int(m.group(1)) if m else 10_000
      return sorted(rows, key=day_key)
  ```
- For any hardcoded HTML table (Cindy-style audit-only roadmaps, Patrick-style retainer audits, Ali-style next-steps docs), run `sort_next_steps.py` against the generator file before regenerating.
- Never trust the order of rows as written in the config — always sort at render time. Config order is for readability of the source; render order is what the client sees.

### L. Auto Slack notification on roadmap finalize (locked 2026-05-24)

**Hard rule:** every roadmap finalized (HTML written + copied to client's Drive folder + ready for delivery) MUST fire a Slack notification to `#90-day-roadmap-notifications` tagging Komal + Daniyal with the kick-off brief.

> **⛔ NEVER tag Salar (`U0AQMRN90JH`).** Salar left the team (2026-06-16). The BD-build owner is now **Komal** (`U0BAKGNHG5S`). Reyhan has flagged the Salar-tag mistake more than once — Komal + Daniyal are the ONLY two tags on this brief. Do not reintroduce Salar under any circumstance.

**Channel + user IDs (locked):**
- Channel: `90-day-roadmap-notifications` · ID `C0B5AH11K8X`
- Komal (BD build): `U0BAKGNHG5S`
- Daniyal (Claude / Ops): `U0ACA08EWRK`

**Locked message template (7 lines — do NOT add, do NOT expand):**

```
🛣️ *[CLIENT NAME IN CAPS]* — Roadmap finalized

<@U0BAKGNHG5S> <@U0ACA08EWRK>

• *Niche / Geo:* [Niche] | [Geography]
• *BD Angles:* [Playbook 1] · [Playbook 2] · [Playbook 3]
• *Claude Skills:* [Skill 1] · [Skill 2] · [Skill 3] · [Skill 4]
• 📁 *Drive Folder:* <https://drive.google.com/drive/folders/[FOLDER_ID]|[Client Folder Name]>
```

**Required cfg fields (add to every client config):**
- `cfg["niche"]` → `[Niche]`
- `cfg["geography"]` → `[Geography]`
- `cfg["outbound_pillar"]["playbooks"]` → BD Angles (titles joined by ` · `)
- `cfg["claude_skills"]` → new top-level string field, formatted like `"Skill 1 · Skill 2 · Skill 3 · Skill 4"`
- Drive folder ID looked up at send-time via `mcp__google-workspace__manage_drive search` on the client folder name

**Why locked:** Reyhan flagged 2026-05-22 that Komal + Daniyal waste 10-15 min before every kick-off call hunting through Drive + the discovery doc + the roadmap to figure out the BD angles and Claude skills they're scoping. The brief lands in Slack at roadmap-finalize time → they search the channel for the client's name on call day → instant context.

**Why CAPS:** the client name in caps makes the message searchable in Slack ("BRIAN BENNETT" pops in channel search; "Brian Bennett" buries in the noise of normal-case messages).

**Why short:** Reyhan rejected the long version (12+ lines). The locked template is 7 lines. Do not pad with "Top 2 fee roles," "Primary outreach tool," "Roadmap sent date," or any other extras. Komal + Daniyal click into the Drive folder for the full doc.

**How to apply (CONFIRM-THEN-SEND, never silent auto-fire):**

1. Build the roadmap (HTML written + copied to Drive folder + Skool DM drafted).
2. **Render the Slack brief in chat** so Reyhan can read it before it goes anywhere. Use the locked template above with the client's actual values filled in. Show it as a code block, not a tool call.
3. **Ask Reyhan explicitly:** *"Push this to #90-day-roadmap-notifications now?"*
4. Wait for confirmation. Only after Reyhan replies yes / push it / send / similar affirmation, fire `chat.postMessage`.
5. If Reyhan says no or asks for edits, revise the brief in chat and re-ask. Do NOT send a revised version without re-confirming.
6. For batched deliveries (multiple roadmaps in one approval), space sends 60s apart so the channel doesn't get spammed all at once.

**HARD rule — never auto-fire.** The Slack post is a public-team-visible action; treat it as risky per the executing-actions-with-care defaults. Reyhan approves each one.

**Reference implementation:**
- `projects/roadmap-build-2026-05-20/send_slack_notifications.py` — one-off Python script that loops a hard-coded client list. Use when Reyhan has approved multiple at once.
- `projects/roadmap-build-2026-05-20/generate_batch2.py` `notify_slack_brief()` — helper that posts a single brief; called from the conversation only after explicit confirmation.
- `SLACK_BOT_TOKEN` lives in `.env`.

**Locked formatting:**
- Opener emoji 🛣️ (motorway).
- Separator ` · ` (middle-dot with spaces).
- Client name in CAPS so the message is searchable in Slack channel search before kick-off calls.

**Future state — full auto-fire (deferred):** Reyhan confirmed 2026-05-24 that full automation is acceptable later, once the confirm-then-send loop has been running cleanly for N roadmaps and the template is locked in muscle memory. Switch path when graduating: flip `notify_slack=False` default to `True` in `write_outputs()` and remove the in-chat confirmation step. Until Reyhan explicitly opts into auto, ALWAYS confirm in chat first.

### M. Niche Strength Slide — mandatory on every roadmap (locked 2026-06-02)

**Hard rule:** every polished roadmap MUST include a "Niche Strength" slide inserted between the Primary Objective slide and the 5 Pillars Overview slide. It quantifies the client's niche × geography on a composite 0-10 score across 4 dimensions, with the underlying data shown.

**Why locked:** clients need to know how strong their market is before committing to a 90-day systems build. A strong niche × geo deserves aggressive pillar depth. A weak one deserves niche-of-niche pivots inside the roadmap. Without this slide, the rest of the roadmap is built on an unstated assumption.

#### Composite Formula

`Niche Strength Score = (Market Demand + Fee Potential + Competition + Niche Defensibility) / 4`

Each dimension is scored 0–10. Composite is the average, rounded to 1 decimal.

#### 4 Dimensions

| Dimension | What it measures | 10/10 threshold | Data sources |
|---|---|---|---|
| **Market Demand** | Sector growth direction + active hiring volume + funding signals | Government growth direction = growing AND 1,000+ active jobs in the geo | Geo-mapped labor stats (table below) + LinkedIn job postings count + Apollo company growth signals |
| **Fee Potential** | Avg base salary of the placed role × 25% retained fee | >$200k avg base salary | Glassdoor / Payscale / Levels.fyi / niche salary surveys |
| **Competition (inverse)** | Recruiters already serving this niche × geo | <10 named competitors | LinkedIn company search `"[niche] recruit*"` in [city] · cross-checked with Apollo industry/geo filter |
| **Niche Defensibility (TAM)** | Total target companies in niche × geo matching ICP | 500+ target companies | Apollo `mixed_companies_search` with industry + geo + size filters |

#### Geo-mapped Labor Stats Source

| Client geo | Source | URL pattern |
|---|---|---|
| US | BLS Occupational Outlook | bls.gov/ooh |
| UK | ONS + GOV.UK Labour Market Status | ons.gov.uk · gov.uk |
| EU | Eurostat + CEDEFOP Skills Panorama | ec.europa.eu/eurostat · cedefop.europa.eu |
| Canada | Statistics Canada / Job Bank | statcan.gc.ca · jobbank.gc.ca |
| Australia | Jobs and Skills Australia | jobsandskills.gov.au |
| Other / multi-country | LinkedIn Economic Graph + ILO | economicgraph.linkedin.com · ilostat.ilo.org |

For multi-country clients, use the country with the most placement volume. Pull from discovery doc Section 1 ("Geography").

#### Mandatory Slide Footer

> *Niche Strength reflects current market data at the date of analysis. It is a snapshot, not a forecast.*

#### How to Apply

1. Extract client niche + primary geo from discovery doc Section 1.
2. Run each of the 4 dimension queries using the data-source table above.
3. Score each dimension 0–10 per the rubric. Cite the source URL alongside the score.
4. Compute composite = (D1 + D2 + D3 + D4) / 4.
5. Build the slide HTML showing the composite score prominently, the 4-row breakdown table with actual numbers + source URLs, and the snapshot footer.
6. Insert as Slide 4 (between Primary Objective and 5 Pillars Overview). Increment all downstream slide numbers.

#### Data Honesty Rules

- **Never invent numbers.** If a data source returns no data, mark the dimension N/A and average over 3 dimensions instead of 4.
- **Cite source URLs in every row** so the client can verify.
- For Competition: name 3–5 observed competitors in a sub-line, not just a count.
- For Fee Potential: spell out the math (`avg CFO base $280k × 25% retained = $70k potential fee per placement`).
- For Market Demand: report the government growth direction as text (e.g. "growing, +13% projected over 10 years per BLS"), not a fake 3-year number.

### N. Never use "ship / ships / shipped / shipping" — locked 2026-06-07

**Hard rule:** ban the verb "ship" and all its inflections from every roadmap (HTML, PDF, Skool DM, Slack brief). Use **deliver** (for finished artifacts), **build** (for in-progress construction), **launch** or **push live** (for go-live moments).

**Why locked:** Reyhan flagged 2026-06-07 that AI writing leans on "we'll ship this", "Daniyal ships X" — it reads as Silicon-Valley-LLM diction and undermines the human-first brand. Humans don't say it.

**How to apply:**
- Pre-publish grep: `grep -niE "\bship[a-z]*" <file>` on every generated roadmap before saving. Replace every hit. False positives (relationship, leadership, partnership) won't match `\bship`.
- Default replacements: "Daniyal ships X" → "Daniyal delivers X" or "Daniyal builds X"; "BD campaign shipped" → "BD campaign launched" or "BD campaign live"; "what RecruiterGTM ships" → "what RecruiterGTM delivers".
- Cross-reference: `feedback_no_ship_language.md` in memory (cross-cutting — same rule applies to content-os, proposal-generator, email-writer).

### O. Niche Strength below 7 → add a "Stronger Alternatives" page — locked 2026-06-17

**Hard rule:** whenever the Niche Strength composite score (Rule M) is **below 7.0**, insert a dedicated **"Stronger Alternatives"** page immediately AFTER the Niche Strength slide, recommending **exactly 2 alternate niches that score 7+ within the SAME geography**. At 7.0 or above, do not add the page — the niche is strong enough to commit to as-is.

**Why locked:** Reyhan flagged 2026-06-17 that a sub-7 niche read leaves the client with a problem and no path. The alternates page turns "your niche is fee-constrained" into "here are two higher-leverage lanes in your market if you want to trade up or add a second lane." It's constructive, not a downgrade of their current plan.

**How to apply:**
- Score the 2 alternates on the **same 4-dimension method** as Rule M (Market Demand · Fee Potential · Competition inverse · Defensibility/TAM), composite = average. Each must clear 7.0 or it doesn't belong on the page.
- **Same geography** as the client (pull from discovery Section 1). Do not jump countries.
- **Prefer adjacency first:** the strongest alternate is usually a niche-of-niche or cross-border pivot off the client's EXISTING candidate pool / expertise (e.g. Cristian Tuica = Romanian medical → "Cross-Border Medical: Romanian doctors & nurses placed into Western Europe" where salaries/fees are 2-3× — fixes the exact dimension dragging the score). The second alternate can be the geography's strongest unrelated sector (e.g. Romania → IT/Software).
- Cite real sources per alternate (same honesty rules as Rule M — never invent numbers; cite URLs).
- Add a **"How to read this"** callout making clear the client does NOT have to move — the 90-day build that follows is still scoped to their current niche, and the same engine (Claude + playbooks + content) ports across if they want to pivot. They raise it on the kickoff call.
- **Renumber all downstream section labels + footer page numbers** after insertion (the page becomes the new slide 03; everything below shifts +1). Update the Skool DM's "Slide N" onboarding-timeline reference accordingly.
- Layout: 2-column `card-grid grid-2`, each card = niche name + large composite score + the 4 dimension scores + a "Why it's stronger" line. Reference build: `~/Desktop/90 Day Roadmaps/cristian-tuica-90day-roadmap.html` (section 03).

### P. Cover title is ALWAYS the consistent heading — never a bespoke creative title (locked 2026-06-23)

**Hard rule:** the cover (slide 1) H1 is always **`90-Day RecruiterGTM Roadmap for [Client Full Name]`**. Never a per-client creative/marketing title.

- P1. Banned pattern — bespoke headlines like "Your Phoenix BD Engine, Mapped in 90 Days", "Your Design Recruitment Engine, Mapped in 90 Days", "Keep what works. Add a second lane." as the COVER title. Those read as one-off and break consistency across the client set.
- P2. Keep the violet `.accent` styling on the brand word for visual consistency, e.g. `90-Day <span class="accent">RecruiterGTM</span><br>Roadmap for<br>Rashin Keller`. Line breaks are fine; the words are fixed.
- P3. The cover pill above the H1 stays `90-DAY ROADMAP · [COMPANY]` and the `<title>` stays `90-Day Roadmap — [Client Name] | RecruiterGTM`. Only the H1 wording is being standardized here.
- P4. Applies to every roadmap going forward and to the carl-wheatley-v2 / cristian-tuica dark template (their covers used bespoke titles — do NOT copy that part of the template).

**Why locked:** Reyhan flagged 2026-06-23 that Rashin's cover read "Your Phoenix BD Engine" — he wants every roadmap cover to carry the same predictable heading naming the client, not a creative one-off per client.

### Q. The Day 10 call is the "Implementation Call" — never "onboarding call" (locked 2026-07-02)

**Hard rule:** the single Day 10 client-booked call is called the **Implementation Call** everywhere — roadmap HTML (key dates, 21-day timeline, buttons), Skool DM, and Slack brief. Never "onboarding call" or "kick-off call."

- Same call, same purpose: Komal + Daniyal on one 30-min call collecting ICP / signals / copy + stack / content / Claude context. Only the label changes.
- The Calendly URL slug (`recruitergtm-onboarding-call`) can stay as-is — only the visible label reads "Implementation Call."
- Applies retroactively to the wording in Rule B and the "21-Day Onboarding Timeline" section below: read every "onboarding call" there as "Implementation Call."

**Why locked:** Reyhan flagged 2026-07-02 — "onboarding call" reads passive/admin; "Implementation Call" signals the build starts.

### R. Email infrastructure + Instantly code (locked 2026-08-06)

- **Always recommend [Zapmail](https://zapmail.ai/?via=obl) for sending domains + mailboxes** whenever the tech stack adds or keeps a cold-email sender (Instantly etc.) — dedicated infrastructure so cold email never runs on the client's main domain. Verified price 2026-08-06: Starter $39/mo for 10 Google mailboxes (from $2.50/mailbox at higher tiers) — re-verify on zapmail.ai if quoting other tiers.
- **The Instantly discount code `31AV2` is RETIRED (Reyhan, 2026-08-06).** Link the Instantly affiliate URL (https://instantly.ai/?via=obl) with NO code. Master list updated in `memory/wiki/references/reference_affiliate_links.md`.

### S. All roadmap copy runs through the ContentOS writing skill (locked 2026-08-17 · re-flagged + upgraded to STEP 0 HARD GATE 2026-08-22 — see top of Locked Rules)

**Hard rule:** every roadmap's copy — cover intro, section intros, pillar headings + body, CTA callouts, milestone/next-step cells, the Skool DM — is written through the **`content-os` writing skill** (its Sections A–M taste rules + the copy-engine loop + humanizer), not free-drafted off the template. Invoke `content-os` before writing/finalizing roadmap copy. This is the roadmap-specific application of the CORE rule "never write copy without invoking the relevant writing skill."

**Two things this specifically kills:**
- **Vague / tool-anthropomorphizing headings.** Reyhan flagged 2026-08-17 that Tracy Nini's Pillar 4 heading read "Loxo, working even harder" — it means nothing. State the plain point: what the pillar actually does ("Loxo as your single source of truth"). Every `<h2>` must say something concrete a client can picture, never a creative filler phrase.
- **ContentOS banned words leaking into the deck.** The Section A–M bans apply to roadmap copy too. The repeat offenders in roadmaps: **"lane"** (banned metaphor — use "niche / channel / side of the market / where competitors aren't"), **"desk"** (audience is solo/boutique — use "your recruiting / your business"), **"seat" for an open role** (Loxo "2 seats" = software licenses is fine), **"leverage", "pivot" (as a verb), "ship/ships/shipped" (Rule N), "seamless", "robust", "delve"**.

**Pre-publish grep (run on every generated roadmap before saving):**
```
grep -niE "\b(lane[s]?|leverage|pivot|seamless|robust|delve)\b" <file>   # metaphors/AI-slop
grep -niE "\bship[a-z]*" <file>                                            # Rule N
```
False positives to leave: "relationship/leadership/partnership" (won't match `\bship`), Loxo "seats" (software licenses), literal road/traffic uses. Replace every real hit before the roadmap ships— er, before the roadmap is delivered.

**Why locked:** Reyhan flagged 2026-08-17 on Tracy Nini's roadmap that "Loxo, working even harder" was meaningless and told me to run all roadmaps through the ContentOS writing skill. The first pass had used "lane" 15 times plus "leverage" and "pivot" — all on the ContentOS banned list — because the copy was drafted straight off the template instead of through `content-os`.

---

## What This Skill Produces

### Output 1: Discovery Doc (Google Doc)
A structured audit summary filled from the call. Uses the standard 4-section + NOTES template. This is the working document.

**Sections in the discovery template (template doc ID `1SyRUv7GBdf9qT5lhBySuCRFXSwX9EZ1ZGWtZ9eAYqbo` — v2, locked pillar order):**
1. CLIENT INFO (table)
2. DISCOVERY QUESTIONS (5 questions including 1-year goal)
3. SYSTEMS AUDIT (tool table)
4. THE 5 PILLARS (LOCKED ORDER — never reorder):
   - PILLAR 1: AI SYSTEM
   - PILLAR 2: ATS & NEWSLETTER
   - PILLAR 3: MULTICHANNEL OUTBOUND
   - PILLAR 4: CONTENT
   - PILLAR 5: OFFER PRODUCTIZATION
5. NOTES (free-form)

**Discovery doc is fill-on-call only.** The Milestones table, Primary Objective, and Next Steps that used to be in the discovery doc are now generated as part of Output 2 (the polished roadmap), NOT filled live.

### Output 2: Polished 90-Day Roadmap (Google Doc)
A client-facing deliverable with branded sections, personalized pillars, specific milestones, and clear next steps. This is what gets sent to the client.

---

## The Process

### Step 1: Extract Discovery Data

From the transcript or notes, extract:

**Client Info**
- Full name
- Agency name
- Niche / industry
- Geography (where they recruit)
- Team size
- Business model (contingent, retained, RPO, subscription, hybrid)

**Discovery Answers**
- Biggest bottleneck slowing the business
- Which part of weekly workflow takes most time
- Lead flow predictability (1-10 scale)
- What makes next 30 days a massive win
- Primary focus area

**Systems Audit**
For each category, capture current tool + recommended action:
- ATS / CRM
- LinkedIn Automation
- Email Outbound
- Data / Enrichment
- Newsletter
- Workflow Automation
- Sourcing
- Other tools

**Tech Stack Decision Framework**

The recommendation depends on what the client already has, their volume needs, and their niche. Never force a tool change if their current tool works. The goal is the right stack for their situation, not a one-size-fits-all.

**ATS / CRM — Keep what they have**
- Recruiterflow, Loxo, Bullhorn, Zoho Recruit, Vincere — all fine
- Only flag if they have NO ATS or are using spreadsheets
- If they're choosing between options: Recruiterflow for small teams, Bullhorn for scale

**Outreach Stack — Two approved configurations**

Config A: Lemlist Only (Default)
- Best for: Most clients. Multichannel (email + LinkedIn) in one tool.
- When to use: Client has no existing outreach tool, or is on Dripify/single-channel tools
- Migrate FROM: Dripify, standalone email tools
- Example: Julie Conti (was on Dripify + Instantly separately → consolidated to Lemlist)

Config B: HeyReach + Instantly (High Volume)
- Best for: Clients sending more than 300 emails per day who need separate LinkedIn automation
- When to use: Only when the client needs 300+ daily email volume. Below that, Lemlist handles everything.
- Example: Jay Veniard (kept HeyReach + Instantly, dropped Lemlist — volume needs exceeded Lemlist's capacity)

HARD RULE: Never recommend HeyReach + Lemlist together. They overlap on LinkedIn.

**Data / Enrichment — Assess per client**
- Clay: Best for complex enrichment workflows, multi-step data pipelines, clients who want to learn the tool
- Deepline / Claude Code: Best for clients who want AI-native data sourcing without learning Clay's UI
- Apollo: Contact data enrichment (emails, phones, company data). Works alongside Clay or standalone.
- Prospeo: Fallback email finder from LinkedIn URLs when Apollo doesn't have the data
- SalesQL: Quick LinkedIn email/phone extraction. Good for clients already using it.

No fixed default. Assess per client based on their niche, technical comfort, and whether they want to learn Clay or just get results.

**Sourcing Tools**
- LinkedIn Sales Navigator: Almost always keep. Primary sourcing tool for most recruiters.
- LinkedIn Recruiter: Keep if they have it. Expensive but powerful for candidate sourcing.
- Pin.com: Recommend for candidate sourcing. Good alternative/complement to Sales Nav.
- Apify: For job board scraping (Indeed, StepStone, Xing) and LinkedIn profile research. Mostly used in managed service, not self-serve.
- ContactOut / SignalHire: Keep if they have it for phone numbers. Don't add if they already have Apollo.

**Newsletter**
- Beehiiv: Always recommend if they have no newsletter. Best for recruitment newsletters.
- If they're already on Mailchimp/ConvertKit, migration to Beehiiv is optional — focus on actually launching the newsletter first.

**Workflow Automation**
- n8n: Preferred. Self-hosted, cheaper than Zapier at scale, supports AI agents.
- Zapier/Make: Keep if they're already using it and it works. Only suggest n8n migration if they're hitting cost limits or need AI agent capability.

**AI**
- Claude Code + Claude Pro ($20/mo): Always recommend for AI-native workflows.
- ChatGPT: If they're using it casually, fine. But position Claude Code as the upgrade for connected, tool-integrated AI.
- Claude Pro ($20/mo): Minimum recommendation for any client wanting to use AI seriously.

**Real Client Tool Decisions (for reference)**

| Client | Kept | Dropped | Added | Reasoning |
|--------|------|---------|-------|-----------|
| Jay Veniard | Clay, Instantly, HeyReach, Sales Nav, n8n | Lemlist, Bullhorn, Zapier | Beehiiv, Claude Code | Volume play — wanted separate LinkedIn + email tools |
| Julie Conti | Recruiterflow, Sales Nav, Zapier | Dripify, Instantly (separate) | Lemlist, Beehiiv, Claude Code | Consolidated to multichannel |
| Kylie Larwood | Loxo, Sales Nav, SalesQL, Dripify (till July) | — | Lemlist (after July), Pin.com, Claude Code | Waited for Dripify contract to end |
| Oliver Zauritz | Lemlist, Clay, Apollo, Sales Nav | — | Apify, Inboxology | German market, job board scraping needed |

### Step 2: Build the 5 Pillars

Every roadmap has 5 pillars in this LOCKED order — never reorder, regardless of primary focus:

1. **AI System** — Claude Code AI Ops Manager handling sourcing, BD, content, ops admin daily
2. **ATS & Newsletter** — clean ATS, captured leads, nurture sequence live
3. **Multichannel Outbound** — 2–3 intent-based playbooks generating conversations on autopilot
4. **Content** — LinkedIn (and YouTube/newsletter where relevant) authority engine
5. **Offer Productization** — packaging the offer with clear pricing, pain points, and side-by-side comparison

**HARD RULE — pillar order is fixed.** Primary focus informs depth and emphasis inside each pillar, but never the position. See `memory/feedback_pillar_order_locked.md`.

---

#### PILLAR 1: OFFER UNIQUENESS

**Goal:** 2 primary offers + 1 secondary offer with clear pricing

Capture:
- Current offer structure (contingent, retained, subscription, RPO, etc.)
- Problems with current model (predictability, exclusivity, pricing power)
- New offer to consider adding
- Secondary offer opportunity

**Standard 90-Day Outcome:**
Prepare a clear offer structure with pitch materials. If they're contingent-only, explore exclusive or subscription (RAAS) model. If they have a niche, productize it.

**Common patterns from real clients:**
- Julie Conti: Contingent + RAAS subscription → prepare SourcingOS pitch to convert client to RAAS
- Kylie Larwood: Mostly retained → push for exclusive-only + explore fractional/RPO
- Oliver Zauritz: Contingent property management → transition to "Talent Partner" positioning

---

#### PILLAR 2: MULTICHANNEL OUTBOUND

**Goal:** 2-3 playbooks running on autopilot generating conversations

Capture:
- ICP (industry, revenue range, employee count, geography)
- Excluded companies/segments
- Buying triggers (open jobs, leadership changes, no internal TA, contract wins, growth signals)

**Standard Playbooks** (pick 2-3 based on their niche):
1. **Live Jobs / Open Roles** — Companies with open jobs in their niche on LinkedIn/Indeed/StepStone
2. **Leadership Changes** — 90-day job changes at target companies (new VP, new CHRO)
3. **No Internal TA** — Companies without a dedicated recruiter/TA team
4. **Growth Signals** — Companies that raised funding, won contracts, expanding offices
5. **MPC Campaign** — Most Placable Candidate outreach to target companies

**Success Metric:** Vary based on team size and niche:
- Solo operator: 3-5 conversations/month
- Small team (2-4): 5-10 conversations/month
- Larger team (5+): 10-15 conversations/month

**Standard 90-Day Outcome:**
Generate 1 meeting from each playbook running. Full autopilot by Day 90.

**The Stack** (always mention):
- Clay: Signal-led sourcing and enrichment
- Lemlist: Multichannel outreach (email + LinkedIn)
- Apollo/SalesQL: Contact data
- Apify: Job board scraping

---

#### PILLAR 3: LINKEDIN CONTENT

**Goal:** 30 posts in 90 days, establish positioning, warmer outbound

Capture:
- Positioning statement (what they want to be known for)
- Content themes (placements, journey, niche insights, AI in recruiting)
- Who creates content (founder, assistant, AI-assisted)

**Standard 90-Day Outcome:**
Publish 30 LinkedIn posts, 5 videos, 10 image posts and 15 text posts.
Try the Recruiter Content Flywheel framework from RecruiterGTM.

**Always recommend:**
- Claude Code with LinkedIn Content Skill for drafting
- Content calendar aligned with outbound campaigns
- Repurpose: 1 long-form piece → 3-5 posts

---

#### PILLAR 4: ATS + NEWSLETTER

**Goal:** Clean ATS, newsletter capturing leads, nurture sequence live

Capture:
- Current ATS state (how many records, is it clean, are they using it properly)
- Newsletter status (none, LinkedIn-only, email newsletter)
- Newsletter promise (what value do subscribers get)

**Standard 90-Day Outcome:**
- ATS filtered list of at least 1,000 clients and 100 previous clients for nurture
- Launch 3 newsletter emails by Day 90
- Beehiiv setup with subscriber landing page

**Adjust the numbers based on their ATS size:**
- If they have 35,000 records (like Kylie): target 1,000 clients + 20 previous clients
- If they have 13,000 records (like Julie): target 1,000 clients + 100 previous clients
- If they have very few records: target 500 clients minimum

---

### Step 3: Build Milestones Table

Standard template — adjust specifics per client:

| Day | Pillar 1: Offer | Pillar 2: Outbound | Pillar 3: Content | Pillar 4: ATS |
|-----|-----------------|--------------------|--------------------|---------------|
| 30 | Offers finalized | 1st campaign live | 12 posts | ATS cleaned |
| 60 | Pitch deck ready | 2 playbooks running | 24 posts | Newsletter live |
| 90 | Tested 10+ prospects | Full autopilot | 30+ posts | 1st newsletter sent |

### Step 4: Define Primary Objective

One sentence summarizing what success looks like in 90 days. Extract this from:
- Their "massive win" answer
- Their biggest bottleneck
- Their lead flow predictability score

Examples:
- Oliver: "Transform from manual headhunting to a fully autonomous, signal-led outbound machine. Reclaim 20+ hours of founder time per week."
- Julie: "Fill 3 of 6 open roles and convert 1 client to RAAS subscription model."
- Kylie: "Generate 3 qualified conversations from cold outreach while running BD in the background without stopping fulfillment."

### Step 5: Next Steps

Standard next steps (always include):

| Action | Owner | Due |
|--------|-------|-----|
| Review roadmap and confirm alignment | Client | Day 3 |
| Access Skool course modules | Client | Day 3 |
| Book 30-min setup session with Daniyal on Skool | Client | Day 5 |
| Share tool logins (CRM, LinkedIn, email) | Client | Day 5 |
| Tech stack audit completed | RecruiterGTM | Day 7 |
| Signal-based outbound campaign launched | RecruiterGTM | Day 14 |
| LinkedIn content launch support | RecruiterGTM | Day 14 |
| MPC campaign n8n automation setup (with Daniyal) | RecruiterGTM | Day 21 |

**What RecruiterGTM delivers for community members:**
1. Tech stack audit
2. Assist with launching a signal-based outbound campaign
3. LinkedIn content launch support
4. MPC campaign n8n automation (with Daniyal)

Add client-specific next steps based on the audit.

### Step 6: Learning Path (Skool Course Recommendations)

Every roadmap includes a "Your Learning Path" slide recommending which Skool courses to watch and in what order. Tailor per client based on their pillars.

**4 Skool Classrooms available:**

1. **OutboundOS** (14 modules) — Foundations, Infrastructure, Market Mapping, ICP, Copywriting, Sequences, LinkedIn, Playbooks, Deliverability, Analytics, Dream100, Scaling, Advanced, Paths
2. **RecruiterOS** (5 modules) — Strategic Foundation (offer models, fractional, talent partner, DFY), AI Candidate Sourcing, Goldmine Database & Nurture, Authority & Scale, Transformation Delivery
3. **Recruiter Content Flywheel** (7 modules) — Authority Shift, Converting Posts to Deals, AI Content Stack, Full Growth System, Creator Studio, 90-Day Sprint Execution, Support Ecosystem
4. **Lean Ops Accelerator** (19 lessons) — AI Brain, Productivity Ops, Sales Ops, Marketing Ops, Team Ops, CEO Briefing, Client Onboarding, SOP Automation, Slack AI, Ops GPT, Dashboards, Offshore Team, Sourcing Offshore, QA, Client Comms, Research, Project Management, Fulfillment Engine. **Claude for Recruiters classroom is inside this section.**

**Mapping rules:**
- Pillar 1 (Offer) → RecruiterOS Module 1 (Strategic Foundation, L4-L9 for offer models)
- Pillar 2 (Outbound) → OutboundOS Module 1 (Foundations), Module 3 (Market Mapping), Module 5 (Copywriting)
- Pillar 3 (Content) → Recruiter Content Flywheel Module 1 (Authority Shift), Module 3 (AI Content Stack)
- Pillar 4 (ATS + Newsletter) → RecruiterOS Module 3 (Goldmine Database), Content Flywheel Module 6 (90-Day Sprint)
- AI/Claude → Always recommend: "Watch the tutorial at recruitergtm.com/claude-for-recruiters. It's inside the Lean Ops Accelerator classroom."

**Always recommend 4 cards in a 2x2 grid.** Pick the most relevant course first based on their primary bottleneck.

### Step 7: Get Started Slide (Always Last)

Every roadmap ends with a "Two Things to Lock In Now" slide:

**1. Add Weekly Q&A to your calendar** (locked 2026-05-29)
- **Title:** RecruiterGTM Weekly Q&A
- **When:** Every Wednesday, **4:30 - 6:00 PM UK time** (recurring weekly, no end date)
- **Google Meet:** https://meet.google.com/xjc-zmxy-yap
- **3 calendar buttons (MANDATORY):**
  - Primary CTA: **Add to Google Calendar** (solid violet button)
  - Secondary text links: **Add to Outlook** · **Download .ics**
- All three URLs are built by the `_qa_calendar_urls()` helper in `generate_batch2.py` and embed the meeting details + Google Meet location + weekly recurrence.
- The .ics ships as a `data:` URI so no file hosting is required — the HTML deliverable is fully self-contained.

**Why locked:** Reyhan flagged 2026-05-29 that adding a one-click "add to calendar" button on the final slide measurably increases Q&A attendance. The 3-button pattern covers Google (most clients), Outlook (corporate clients), and `.ics` (everyone else — Apple Calendar, Fastmail, etc.).

**2. Track Your Progress**
- Link: https://docs.google.com/spreadsheets/d/1aZBd7FFYYoCpy_6YHvwkUi25DeEgm4te/edit?gid=352351256#gid=352351256
- Instruction: "File → Make a copy → Track your goals for the next 90 days"

**3. Book a 30-min Setup Session with Daniyal**
- For anything RecruiterGTM (tool setup, Skool access, tech questions), members book a 30-min session with Daniyal by reaching out to him directly on Skool.
- Always include this as part of the Get Started slide or Next Steps table.

**Footer:** "Questions? Message Reyhan or Daniyal directly on Skool."

---

## Output Format

### Discovery Doc

Create a Google Doc using the standard template structure (7 sections):
1. Client Info (table)
2. Discovery Questions (filled answers)
3. Systems Audit (tool table with current/action/notes)
4. The 4 Pillars (each with current state, gaps, 90-day outcome)
5. 90-Day Milestones (table)
6. Primary Objective
7. Next Steps

Save as: `[Client Name] - 90-Day Roadmap Discovery`
Location: Client's Google Drive folder

### Polished Roadmap (HTML — 13 slides)

Build as a standalone HTML file using the proposal-generator design system (dark theme, violet #8A00FF accents, DM Sans font, 1280x720 slides).

**13-slide structure:**
1. **Cover** — client name, agency, niche, geography, prepared by Reyhan, date
2. **Client Overview** — business/model/discovery scores cards + current stack as pills
3. **Primary Objective** — one bold sentence + supporting paragraph
4. **5 Pillars Overview** — 5-card grid with pillar numbers and one-liner each
5. **Pillar 1: Offer Productization** — current state, 90-day target, milestones table
6. **Pillar 2: Multichannel Outbound** — ICP, buying triggers, success metric, 3 playbook cards
7. **Pillar 3: Content** — positioning, content themes, 90-day targets (30/15/10/5)
8. **Pillar 4: ATS & Newsletter** — ATS milestones + Beehiiv setup details
9. **Pillar 5: AI System** — what AI handles for them, Claude Code setup scope, daily workflows
10. **Tech Stack** — full table with Current/Action/Notes columns (Keep green / Transition yellow / Add violet)
11. **21-Day Onboarding Timeline** — MANDATORY (see "21-Day Onboarding Timeline" section below)
12. **90-Day Milestones + Next Steps** — Day 30/60/90 table + action items with owners and due dates
13. **Get Started** — Weekly Q&A calendar buttons + Performance Tracker link (see Step 7)

---

## HARD RULE — Primary Focus shapes DEPTH, never order

The discovery template's Section 2 captures 5 questions. **The "Primary focus" answer and the "What would make the next 30 days a massive win?" answer shape the depth, emphasis, and Primary Objective of the roadmap — never the pillar order.**

Pillar order is locked: AI System → ATS & Newsletter → Outbound → Content → Offer. See `memory/feedback_pillar_order_locked.md`.

What primary focus DOES change:
- The Primary Objective slide (one bold sentence pulled from the 30-day-win answer).
- The depth of writing inside the matching pillar.
- Tech stack recommendations.
- Day 30/60/90 milestones — column order stays AI / ATS / Outbound / Content / Offer, but the cells under the primary-focus pillar get the headline outcomes.
- 21-Day Onboarding emphasis: which kick-off is "the visible Day-X win".

What primary focus DOES NOT change:
- The order of the 5 pillar slides.
- The pillar overview grid (always 01 AI → 02 ATS → 03 Outbound → 04 Content → 05 Offer).
- The Day 30/60/90 milestone table column order.

**How to apply:**
- Read Section 2 first. Identify the primary focus.
- Build the Primary Objective slide directly from the 30-day-outcome answer.
- Keep pillar slides in the locked order. Adjust depth and wording inside the matching pillar.
- Make sure every milestone in the Day 30/60/90 table reinforces the primary focus.

## HARD RULE — Include every concrete deliverable mentioned on the call

If the call notes mention a specific deliverable (website build, ATS migration, newsletter setup, podcast launch, anything), it MUST appear in the roadmap. No exceptions.

The 21-day onboarding timeline is the natural home for these. Examples:
- "We'll build their website" → add to Day 10 milestone alongside Claude AI Ops Manager (Daniyal handles both)
- "ATS migration in week 2" → add to Day 14
- "Newsletter setup" → add to Day 21

Cross-check the discovery doc and the Fireflies transcript before building. If a deliverable was mentioned and isn't in the roadmap, the roadmap is incomplete.

## HARD RULE — Affiliate links on every tool recommendation

Every tool named in the audit table (KEEP / SWAP / DROP / ADD — all of them) MUST be hyperlinked to its RecruiterGTM affiliate URL when one exists, and the discount code appended visibly when one exists. See `memory/reference_affiliate_links.md` for the master list and `memory/feedback_always_use_affiliate_links.md` for the rule.

Never fake a link. Tools without an affiliate (Loxo, Bullhorn, Lusha, Exa, n8n, HyperTide, Claude, LinkedIn) are named normally.

After the roadmap ships, log every new client setup with an affiliate tool via the `affiliate-tracker` skill.

## HARD RULE — Systems Audit (mandatory, framework-driven)

Every polished roadmap MUST contain a tech stack audit slide that follows the official audit framework. NEVER write generic "Add X / Keep Y" recommendations off the top of memory.

**Master reference deck:** `~/Desktop/Skool Courses/tech-stack-2026.html` (and the newsletter version at `~/Desktop/newsletters/tech-stack-2026.md`). 9 categories, MCP-first principle, Starter $400-450/mo (solo) vs Advanced $1,150-1,250/mo (team) reference stacks.

**Tool rulings reference (LIVING):** `reference_tools_audit_decisions.md` in memory. Authoritative keep/swap/drop rulings per tool, by category. Updated every time Reyhan rules on a new tool.

### Audit slide must include 6 columns:

| Category | Currently Using | Action | Recommended Tool + Plan + Price | Why | Monthly Cost Impact |

Plus a **Cost Summary card** at the bottom: "Current spend ~$X/mo · Recommended ~$Y/mo · Net savings/investment $Z/mo"

### META-RULE — already-purchased tools

**If a client has already purchased a tool, do NOT advise them against it UNLESS the tool is on the ❌ list in `reference_tools_audit_decisions.md`.**

- Default to KEEP for any tool that isn't explicitly bad.
- Only SWAP when the existing tool is actively a problem (Bullhorn, Crelate, Vincere, Dripify, etc.).
- For ⚠️ tools (Loxo, Recruiterflow, PCRecruiter, SourceWhale-when-already-paid), flag the upgrade path but don't force migration. Frame as "explore for longer run."

### Decision logic per tool (apply in order):

1. Map every current tool to one of the 9 categories from `tech-stack-2026.html`.
2. Look it up in `reference_tools_audit_decisions.md`:
   - ✅ → KEEP
   - ❌ → DROP / SWAP to recommended replacement
   - ⚠️ → KEEP only if client is genuinely happy. Otherwise SWAP.
   - TBD → ASK Reyhan "yes / no / drop / keep / swap?", then update the memory file with the new ruling before continuing.
3. For each empty category, mark ADD. Pick from the Starter or Advanced tier based on client's team size.
4. Apply special weights:
   - Construction / trades / blue-collar / field-staff → recommend Pin.com over Sales Nav for sourcing
   - Solo founder → Starter stack ($400-450/mo total)
   - Team of 2-3 → Advanced stack ($1,150-1,250/mo total)
   - Client mentions dialing or calls → Lemlist over HeyReach
   - Client wants high-volume email → Instantly over Lemlist
5. Cite the tech-stack-2026 deck URL when recommending an upgrade.

### When you encounter an unknown tool

If a client uses a tool not listed in `reference_tools_audit_decisions.md`:
1. Pause the build.
2. Ask Reyhan "Is [tool] a yes / no / drop / keep / swap?"
3. Once he rules, append the ruling to `reference_tools_audit_decisions.md` so it's known next time.
4. Continue the build.

This is how the skill compounds knowledge — never guess, always learn.

---

## HARD RULE — 21-Day Onboarding Timeline (mandatory in every roadmap)

Every polished roadmap MUST include the 21-day onboarding slide that mirrors what we commit to in our proposals. Four milestones on a horizontal timeline:

**Day 3 — 90-Day Roadmap Delivered**
This document. Client reviews and confirms alignment.

**Day 10 — RecruiterGTM Onboarding Call (client books)** *(combined Komal + Daniyal session — locked 2026-05-25)*
Client must:
1. Fill the pre-call form: https://qecqr7a7us.zite.so/
2. Book the **combined onboarding call** with Komal (Head of Fulfilment) + Daniyal (Ops Manager): https://calendly.com/d/ct6h-hrd-cdk/recruitergtm-onboarding-call

One call, both leads on it. Komal collects ICP, target signals, and copy direction for the BD campaign. Daniyal collects stack, content themes, and Claude Ops Manager context. Both **initiate their builds after this single call** — the client does NOT need to build anything live. This saves Komal and Daniyal each a 30-min slot per client.

**Day 17 — Custom Claude Ops Manager delivered (RecruiterGTM ships)**
Daniyal ships the custom Claude Code AI Ops Manager 7 days after the Day 10 onboarding call. One of the 3 RecruiterGTM-owned deliverables. See `memory/feedback_recruitergtm_3_deliverables.md`.

**Day 22 — Intent-Based BD Campaign launched (RecruiterGTM ships)**
Komal pushes list, copy, and sequence live on the client's tools 12 days after the Day 10 onboarding call. Second of the 3 RecruiterGTM-owned deliverables.

**The Day 3 Roadmap IS the Tech Benchmarking + Systems Roadmap.** Do not list a separate Day 21 deliverable. The 90-Day Roadmap document delivered on Day 3 already contains the full keep / swap / drop / add audit + 90-day systems migration plan.

**Frame it as "3 things on us, 1 thing on you" in every roadmap and Skool DM:**
- On us: Day 3 Roadmap (= Tech Benchmarking) · Day 17 Claude Ops Manager · Day 22 BD Campaign launched
- On client: Day 10 combined onboarding call (Komal + Daniyal)

**4th timeline circle should be Day 22 — "Engine fully live"** showing both RecruiterGTM deliveries shipped (Claude Ops Manager + BD campaign).

**Slide implementation (HTML):**
- 4 violet circles in a horizontal row, each with the day number (Day 3, Day 10, Day 17, Day 22)
- Below each circle: milestone title + 1-2 line description
- For Day 10: include both the form link and the combined onboarding Calendly link as visible buttons. **Single Calendly button** — not two separate ones. Label it "Book onboarding call".
- Same styling as the existing community onboarding timeline in `tom-wood-jon-humphries-proposal.html`

Cross-reference: `reference_onboarding_links.md` (verify URLs are still live before every roadmap build).

**File locations (save to BOTH every time):**
1. `~/Desktop/90 Day Roadmaps/[client-slug]-90day-roadmap.html` (working copy on Desktop)
2. `~/Library/CloudStorage/GoogleDrive-reyhan@recruitergtm.com/My Drive/RecruiterGTM/CLIENTS/RecruiterGTM Clients/[Client Folder]/[client-slug]-90day-roadmap.html` (delivery copy in Drive)

The Drive folder names typically use the client's full name (e.g. `Trent Tate`, `Rashin Keller`, `Jon Humphries`). For multi-founder accounts (e.g. Tom Wood + Jon Humphries), there's usually only one folder under the lead contact's name — confirm via `ls` before copying.

**Export to PDF:** Chrome print → Save as PDF (no margins, background graphics on)

---

## Step 7: Draft the Skool Delivery Message

Every roadmap generation MUST end with a paste-ready Skool DM that Reyhan can send the client. The message accompanies the HTML (which Reyhan attaches manually or shares via Drive link).

**Template — adapt the 3 numbered lines per client:**

```
Hey [First Name],

Your 90-Day Roadmap is attached. Download the HTML file and open it in any browser — it's a styled deck, not a Google Doc.

Quick rundown:
1️⃣ [Top focus / decision — pulled from Pillar 1 or Primary Objective — ONE LINE]
2️⃣ [Tech stack / outbound highlight — biggest tangible change — ONE LINE]
3️⃣ [Niche-specific deliverable — playbooks, content angle, network unlock — ONE LINE]

Combined onboarding call with Komal and Daniyal on Slide [N].

Have a read and lmk if you have any questions on the next steps.

Reyhan
```

**Locked opener (2026-05-21):** every DM starts with exactly *"Your 90-Day Roadmap is attached. Download the HTML file and open it in any browser — it's a styled deck, not a Google Doc."* This prevents the "I can't see it" follow-up.

**"Updated" wording — locked 2026-05-23:** only use "Updated roadmap attached…" if Reyhan has actually sent the prior version to the client. If you're drafting the first DM (even after multiple internal revisions of the doc), use the standard opener. If unsure, ask Reyhan whether he's sent the prior version before drafting.

**Rules for the message:**
- Slide [N] = the 21-Day Onboarding slide number in the final HTML. Verify by counting before sending.
- NEVER paste the combined onboarding Calendly link into the message body — it lives in the roadmap on Slide [N].
- Max 1 em dash in the entire message.
- For multi-founder accounts (e.g. Tom + Jon), address the lead contact and reference the partner: *"Built it for you and Tom — every section is shaped around what you both said."*
- **HARD LIMIT — 12 lines or fewer, no exceptions. Don't restate the call. Don't pre-explain the bullets. The roadmap doc itself does the explaining.** (Locked 2026-05-21.)
- **HARD LIMIT — each numbered bullet (1️⃣ 2️⃣ 3️⃣) is ONE LINE only.** No multi-sentence bullets, no semicolon-stacking three thoughts into one bullet. If a bullet needs more than one line, it doesn't belong in the DM — it belongs in the roadmap. (Locked 2026-05-21.)
- **No pre-bullet context paragraph** beyond the 1-line "Your 90-Day Roadmap is attached" (or "Updated roadmap attached" for corrections). If you wrote 3+ sentences before "Quick rundown:", delete them.
- **Update / correction DMs** use the same shape: one short opener line (1 sentence flagging what changed) + same 3 one-line bullets + same closing. Never long-form-explain a correction.
- No hashtags, no salesy phrasing.
- **MANDATORY closing line (locked 2026-05-14):** the final line before "Reyhan" sign-off must always be: *"Have a read and lmk if you have any questions on the next steps."* No variations. No "flag anything that feels off" or similar. Locked verbatim.

**Final-pass check before submitting any DM:**
1. Count total lines (including blank lines + bullets + closing). Must be ≤ 12.
2. Each numbered bullet — is it one line? If wrap, rewrite shorter.
3. Did you add any context paragraph before "Quick rundown:" beyond the 1-line opener? Delete it.
4. Closing line verbatim? "Have a read and lmk if you have any questions on the next steps."

If any of these fail, rewrite before sending.

**Variant — opening line for multi-founder:**
> "Your 90-Day Roadmap is attached. Built it for you and [Partner] — every section is shaped around what you both said on the calls."

**Reference files (confirmed working roadmaps):**
- Kylie Larwood: `~/Desktop/proposals/kylie-larwood-90day-roadmap.html`
- Julie Conti: `~/Desktop/proposals/julie-conti-90day-roadmap.html`
- John Bult: `~/Desktop/proposals/john-bult-90day-roadmap.html`

---

## Rules

1. **Always extract from real call data.** Never invent business details. If something is unclear from the transcript, flag it as "[CONFIRM WITH CLIENT]".
2. **Tool recommendations are suggestions, not mandates.** If a client loves their current tool, keep it. Only recommend changes where there's a clear improvement.
3. **Success metrics must be realistic.** A solo operator won't generate 15 conversations/month. Match the metric to team size and niche.
4. **The 4 Pillars are always the same 4.** Content changes per client, but the structure is fixed: Offer Uniqueness, Multichannel Outbound, LinkedIn Content, ATS + Newsletter.
5. **Always include the DFY Sprint table** if client is on a managed service (Premium, VIP, or retainer). Omit if they're Standard tier (self-serve with community support).
6. **Milestones table is standard but adjustable.** The Day 30/60/90 structure stays. Specifics change per client.
7. **Save the final HTML to BOTH locations on every run.** Desktop working copy AND `RecruiterGTM/CLIENTS/RecruiterGTM Clients/[Client Folder]/`. Confirm the folder exists with `ls` before copying — never invent the path.
8. **Always draft the Skool delivery message at the end of the run.** Use the template in Step 7. Reference the correct 21-Day Onboarding slide number. Never paste the combined onboarding Calendly link into the message body.
9. **After generating, offer to create the Discovery Doc as a Google Doc** in the client's folder.

---

## Reference Files

- **Discovery Template (Google Doc) — v2 with locked pillar order (AI → ATS → Outbound → Content → Offer):** `1SyRUv7GBdf9qT5lhBySuCRFXSwX9EZ1ZGWtZ9eAYqbo`
- **Discovery Template (Google Doc) — v1 DEPRECATED (old order, do not use):** `1LTSMmkP8BC6gfEwCp0FdPl5xNbfTLz4zIw4lIZswojI`
- **Polished Roadmap example — Oliver Zauritz:** `1-QyAKtpFJa6Yw0ckMDlzXkUTWzKpzrVERR7ua-GfbXU`
- **Discovery example — Julie Conti:** `1FYBYvIWXFfSXHdPBvN8Ndn2KwSp18Vp9VcbfjC2ePfc`
- **Discovery example — Kylie Larwood:** `1iUW3MSA72pcrIApGOzup9A-MZWqkihPG7aItIkpKeEI`
- **Draft template (.docx):** `1jDT3ZuB_61vQP9KnS9NAI1bJQjN8pOk4`
