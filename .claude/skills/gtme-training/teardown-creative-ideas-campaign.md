# Teardown: The Creative Ideas Campaign (Eric Nowoslawski / Growth Engine X)

**Source:** Eric Nowoslawski (Growth Engine X — 4 yrs, 5-8M cold emails/mo) YouTube walkthrough.
**Use in this skill:** the canonical worked example for **Module 8 (Signal → Copy bridge)** and a ready campaign template for OutboundOS. Pairs with Will's frameworks (Part 2) and Jordan's signal thinking (Part 1).

---

## What it is

Growth Engine X's single best-performing campaign across YC-backed, bootstrapped, and Fortune 500 clients. First discovered running outreach for Instantly.ai 2.5 years ago; also Clay's best-performing campaign. Beats every "normal signal" campaign they test.

**The core move:** "Saw your company. If I were in your shoes, here's how we'd help you." → 3 AI-personalized ideas, **each tied to one specific thing you actually offer**, written to the prospect's exact company.

Results cited: Donut Media — the one-liner version 3x'd reply rates. PR agency (Pay-A-Results) — 80 positive responses/day using this framework.

---

## The structure

A short email with 3 bullet ideas. Each bullet = one specific offering/play, personalized via AI to the target company.

Worked example — Clay.com's own outreach (the 3 bullets are FIXED, the content is AI-personalized per company):
1. **New hires play** — AI picks which job titles they'd target if going after new-hire signals
2. **Clagent play** — how they'd use Clay's research agent to find data points no one else can get
3. **Integration play** — AI picks BuiltWith / PredictLeads / another integration that fits this specific business and references company news

Then it collapses to a one-liner if you want it shorter:
> "If I were looking at your business, I would help in this way: [AI generates the second half]."

---

## The 3 rules (this is why it works)

1. **Constrain each bullet to what you can ACTUALLY deliver.** Cautionary tale: rolled out to a software dev shop, AI invented features they couldn't build → great replies, but the client couldn't fulfill. Each bullet must be locked to a real offering/play, not open creativity.
2. **Give the AI heavy business context** — not one sentence. The more it knows about what you do, the better the ideas.
3. **Hand-write 3-4 excellent examples** after reviewing 10 real target companies. This teaches the AI your tone, length, and how you read a company description → infer who they sell to → generate ideas. **When output is bad, add MORE examples — don't tweak the prompt.**

---

## The Clay build (under 5 min)

- **Model:** GPT-5 nano (best cost/quality blend; 4o-mini is a cheaper alt).
- **System prompt in two parts:**
  1. Context + goal + **constrain creativity per bullet** (bullet 1 = new hires/job titles, bullet 2 = Clagent, bullet 3 = PredictLeads news).
  2. **Examples of "good"** — 2 contrasting company types so the AI generalizes (Eric used Red Bull = CPG, and Pilot.com = B2B service).
- **Keep the main prompt tiny** — just the company description. Identical system prompt across rows triggers **OpenAI cached-input discounts** = cheaper at scale.
- Hand-write examples fast with voice (he used Whisper Flow). The prompt wording can be rough; the **examples** are what must be excellent.

---

## Recruitment translation (how we use it in OutboundOS)

Same skeleton, recruitment offerings locked into the 3 bullets. For a recruitment agency reaching out to potential client companies:

1. **Roles-they're-hiring play** (job-posting signal) — AI identifies which open roles we'd source for, by reading their careers page / postings.
2. **Speed/quality play** — how we'd deliver a shortlist on their hardest-to-fill role faster than their current process.
3. **Market-intel play** (news/funding signal) — AI references their recent funding/expansion and ties it to the hiring wave it implies.

One-liner version for recruiters:
> "Saw you've had [role] open [N] days and just posted two more — if I were you, here's how I'd clear that backlog: [AI second half]."

**Rule-1 discipline matters more for us:** lock the bullets to engines we actually run (sourcing, outbound, content) so we never imply a service we don't deliver. This is the same discipline as our `feedback_no_ship_language` / scope rules.

---

## Where it sits vs the anchors

- **Jordan (Part 1):** Eric's "new hires / news" bullets ARE signals. The campaign is a packaged signal→copy play.
- **Will (Part 2):** the one-liner version is pure Will — observation tied to a likely problem, one idea, soft framing. The 3-bullet version is a "Vanilla Ice Cream" variant where the 3 ideas carry the credibility/solution.
- **Caution:** Eric's long 3-idea email runs *against* Will's "under 50 words" rule. Both work — test both. Long wins when the ideas are genuinely well-curated; the one-liner wins on volume and deliverability.
