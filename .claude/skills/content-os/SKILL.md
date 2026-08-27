# ContentOS — Multi-Channel Content Skill

## What This Skill Does
Produces content in Reyhan Khan's exact voice for RecruiterGTM across three channels — **LinkedIn, Blog, Newsletter** — each with its own dedicated structure and rules. LinkedIn rules live in this file in full; blog and newsletter each have a dedicated channel section below that defines their structure and names the owning process skill.

## How to Invoke
Paste a topic, angle, or raw notes → say which channel(s). If no channel is named, ask.
For LinkedIn, always ask: what content type is this? (see Content Types below)

---

## Channels (locked 2026-07-17)

ContentOS is multi-channel. Each channel has its own dedicated structure — never apply one channel's formatting to another.

| Channel | Structure lives in | Process owner |
|---------|-------------------|---------------|
| **LinkedIn** | THIS file — everything below the Channels section | content-os |
| **Blog** (recruitergtm.com/blog) | "Channel: Blog" section below | `seo-engine` owns process: brief → write → pre-publish checklist → publish → IndexNow. No brief = no post. |
| **Newsletter** (Beehiiv) | "Channel: Newsletter" section below (summary) | `newsletter-writer` owns the locked 7-part shape. Never freehand a newsletter. |

### Cross-channel rules (apply to ALL three)
- X1. Every piece runs the **copy-engine loop + humanizer** before Reyhan sees it. Never show a first draft (CORE rule).
- X2. **Preflight every stat** against sources/context files. No invented numbers; vendor-blog stats are never presented as solid.
- X3. **Repurposing flow:** one source asset (YouTube video, Market Pulse edition, case study) → LinkedIn post + blog post + newsletter section, each REBUILT in its channel's structure. Never paste one channel's copy into another.
- X4. **The Recruitment Market Pulse** (`market-pulse` skill) feeds all three channels monthly: edition page → blog-depth content, LinkedIn launch post, newsletter section.
- X5. The Section A–M rejection rules below (banned words/phrases, banned sentence patterns, hollow-line check, em dash limits, mission phrasing) are **Reyhan's taste rules and apply to every channel** — including website page copy. Channel *structure* differs; the bans do not.

### Channel: Blog — dedicated structure (locked 2026-07-17)
`seo-engine` owns the process (brief-first, SERP-format match, word-count targets, schema, register). This section defines the editorial structure inside that process:
1. SEO title under 60 characters + meta description 150–160 characters.
2. First paragraph answers the target query directly in 40–60 words (the AEO extraction layer).
3. Key-takeaways box after the intro: 3–5 bullets.
4. H2 sections, one idea per section. Flowing short paragraphs, max 5 lines each — NO one-sentence-per-line formatting (that is LinkedIn's structure, not the blog's).
5. Every major section carries a real number with a named source; real tools by name; client examples where permitted.
6. Minimum 2 internal links (one service page + one related post or Pulse edition) plus external links to every cited source.
7. FAQ section when the query warrants it (FAQPage schema per seo-engine).
8. One CTA block at the end: book a call (`/start-pilot`) or newsletter (`/newsletter`). Never pricing.
9. Voice: practitioner, British/neutral English on the blog. All Section A–M bans apply.

### Channel: Newsletter — dedicated structure (summary)
Owned by `newsletter-writer/SKILL.md`. The locked 7-part shape: subject (hyphen-space pattern, <60 chars) → 3-line opener (stat + contrast + analogy) → setup paragraph → numbered-list spine (3–5 items, each with a contextualised number) → "why this matters now" → giveaway/offer with reply-keyword CTA → PS + casual sign-off. 400–500 words, zero or one em dash, no emojis in the body, no markdown headers. ContentOS routes newsletter jobs there and applies X1–X5 on top.

---

---

## STEP 0 — LOAD CONTEXT (MANDATORY, NEVER SKIP)

**You cannot write a post without first loading Reyhan's context.** If you skip this, you will produce hollow generic lines like "what fulfilment looks like to me" — Reyhan flagged this on May 9 2026 and will reject the post.

Before drafting anything, read these files and let them inform every line:

1. `context/me.md` — who Reyhan is, brand identity, base, top priority
2. `context/work.md` — RecruiterGTM business model, revenue streams, pricing tiers, current MRR & target
3. `context/team.md` — current team (4 people), who owns what
4. `context/current-priorities.md` — what's actually on his plate right now
5. `context/goals.md` — quarterly goals, definition of a good quarter
6. `memory/user_journey.md` — full origin story (S&P Global → Upwork → Head of Ops at 7-8 figure agencies → Clay → RecruiterGTM Jan 2026)
7. `memory/MEMORY.md` — index of project memories, pull any that match the topic
8. **`.claude/skills/content-os/gold-standard-posts.md` — MANDATORY** (added 2026-07-29). The curated "write like THESE" corpus: full finalized posts Reyhan has approved, with a note on what each demonstrates. These are the few-shot exemplars — imitate their rhythm, specificity, and imperfection. Rules tell you what to avoid; this file shows you what to hit.
9. **`content/linkedin-posts.md` — MANDATORY** (locked 2026-06-08). Every finalized post is appended to this file. Read it every time before drafting to: match voice + cadence, avoid duplicating recent hooks/angles/CTAs, pull through callbacks ("a week ago I posted that…"), and balance keyword usage so you do not run the same CTA keyword (META, PLAYBOOK, etc.) three weeks running. The Pulse content calendar (`team_content_posts` in Supabase) is authoritative for scheduling, status, and tracking (locked 2026-07-13 — Notion tracker retired), but this local file is the source of truth for context-window loading inside Claude Code.
10. **`.claude/skills/content-os/algorithm-playbook.md`** (added 2026-07-08) — distilled Q4 2025 State of the Algorithm report (329k posts analysed). Optimize every post against it: length, format, hooks, timing, links, engagement strategy. On any conflict, the locked voice rules in this SKILL.md win.

**Then write the post.** Every line must trace back to a real specific from the context — a person, a number, a date, a project, a piece of his story. If a line is abstract ("what fulfilment looks like to me", "this is what the work is all about", "doing what I love"), delete it. Replace with the concrete fact behind the feeling.

**Hollow-line check before submitting:** read each line and ask "could this appear in any other founder's post?" If yes, rewrite with a Reyhan-specific anchor (his journey, his clients, his current week, his actual mission).

---

## STEP 0.5 — THE 5-STEP WRITING PROCESS (HARD RULE — ported 2026-07-29)

Ported from the client ContentOS skills (`contentos-daleo` STEP 0.5 is the canonical reference, locked 2026-06-13) because Reyhan's own posts were drifting AI-flavoured for the same root cause: **a topic alone gives the model no fresh input, so it remixes the past corpus and the output reads like AI.** The POV is the spine, fresh substrate is the evidence, a one-line hook is the front door.

### When this applies

EVERY us-built topic. The rule is skipped ONLY when the topic comes with its own fresh substrate:
- A Fireflies call from the last 7 days
- **A voice note Reyhan recorded this week — this is the PREFERRED substrate for batch generation.** For a batch of 3-5 posts, Reyhan records 2-3 minutes of raw takes per batch; the transcript is the substrate and his phrasing carries into the draft. Keep his sentences where they work — the draft should reuse his spoken wording, not paraphrase it.
- A real recent event (a client result, a placement, a build from this week, something that happened at RecruiterGTM)

In those cases the call / voice note / event IS the substrate. Skip web research and write straight from the source.

### The 5 steps

**1. Lock the POV.** Reyhan's specific take, in ONE sentence. Not the topic — the TAKE. If the POV can't be written in one sentence, the post isn't ready. The POV must align with Reyhan's locked positioning: the 5 RecruiterGTM pillars (`reference_recruitergtm_5_pillars`), the mission line (Section E), and the public positioning rules in `context/me.md`. Name which pillar or position it maps to.

**2. Pull 3 pieces of fresh multi-source substrate** (when no voice note / call / event supplied it):
- One recent data point (stat / study / report from the last 12 months)
- One named-voice take (a recent post / quote from a respected voice in recruiting, AI, or GTM)
- One current example or story

Research age rule (HARD): last 12 months, with the two exceptions from the canonical rule — older research confirmed by events (call out the gap) or proven wrong (use as a foil). Research is conversational fuel, not academic citation.

**3. Pick the anchor.** The substrate piece that best carries the POV. Default = named-voice take, so Reyhan riffs INTO an industry conversation instead of into the void.

**4. Write the hook — ONE LINE.** Line 1 stands alone, blank line after, 6-12 words. First 3 lines combined under 210 characters (the see-more cut). Give a 🟢 SHARP and 🟡 SOFT version. Line 2-3 = tease that earns the click.

**5. Write the body.** POV as spine, substrate as evidence, all voice rules (Sections A-M) apply. Close on a verdict or a reframing, not a summary.

### Research sources — recruitment podcasts (locked 2026-08-17)

For the "named-voice take" + "current example" substrate (step 2 above) AND for the weekly signal mine, pull hot/emerging recruitment topics from these three same-audience podcasts. All three publish full episodes on YouTube — grab the transcript from the YouTube link (transcript panel / auto-captions) and mine it for what recruitment agency owners are actually talking about right now.

1. **The Elite Recruiter Podcast** — Benjamin Mena. YouTube: `youtube.com/channel/UCFPyxMzqplJTxRCrLjuttew` · site `eliterecruiterpodcast.com`. Our strongest lead-magnet source already — 5 of the last 7 discovery calls came off Ben's show.
2. **The Resilient Recruiter** — Mark Whitby. YouTube: `youtube.com/myrecruitmentcoach`. Same audience: 7–8-figure agency owners + solo billers, weekly.
3. **The Recruitment Mentors Podcast** — Hishem Azzouz. YouTube: `youtube.com/@recruitmentmentorspodcast`. Agency owners + up-and-coming billers, twice weekly.

How to use them:
- Pull the last ~2–4 weeks of episodes; skim transcripts and extract recurring pain points, tool debates, hot takes, and the exact language owners use.
- Map each topic to one of the 5 RecruiterGTM pillars; feed the winners into the week's theme pick and the LinkedIn substrate.
- Riff INTO these conversations (name the host/guest where it earns the click) rather than posting into the void — this is the default "named-voice anchor".
- Podcast numbers are UNVERIFIED — never lift a guest's claim as our stat; run every number through X2 preflight before publishing.
- Swap or extend the list only with Reyhan's sign-off.

### Research sources — GTM / outbound inspiration (added 2026-08-19)

Cross-pollination source, distinct from the recruitment podcasts above. These are GTM/outbound systems builders (adjacent audience, not recruitment-specific) mined for angles, frameworks, tool debates, and content structure we can translate INTO the recruitment-agency-owner context. First **dual-channel** source — mine BOTH YouTube and LinkedIn.

1. **Eric Nowoslawski** — Founder, Growth Engine X (Clay/outbound). LinkedIn: `linkedin.com/in/outboundphd` (primary active handle) · YouTube: `youtube.com/@ericnowoslawski` · site `growthenginex.com`. Best for: cold-email/Clay/AI-outbound frameworks, campaign-angle breakdowns, and personalization-at-scale takes → translate to the solo/boutique recruiter.

How to use them:
- Pull the last ~2–4 weeks from BOTH channels — recent YouTube uploads (grab transcripts) AND recent LinkedIn posts. Extract frameworks, hot takes, and the exact language, then map to one of the 5 RecruiterGTM pillars (mostly AI Layer + Multichannel Outbound).
- This is INSPIRATION/adjacent, not same-audience — never present Eric's outbound-agency numbers or claims as ours; translate the *idea* to a recruitment-owner context, then run any stat through X2 preflight.
- Same guardrail: swap or extend this list only with Reyhan's sign-off.

### Auto-reject conditions

- POV can't be stated in one sentence → topic isn't ready
- Substrate is "past posts" or "the ContentGPS" → that's corpus, not fresh substrate
- Hook is multi-line or first 3 lines exceed 210 chars → rewrite
- No `Substrate sources` block on the draft (strip before publish)

### Required audit stamp on every draft

Every draft shown to Reyhan ends with one audit line (stripped before publish):

`Checks: humanizer pass ✓ · copy-engine loop ✓ · em dashes: N · POV: [one-liner] · Substrate: [voice note / call / 3-source]`

A draft without this stamp has not been through the loop (X1) and must not be shown. This is the enforcement mechanism for X1 — the stamp is written AFTER the humanizer + copy-engine passes actually ran, never pre-filled.

### Batch generation (the 30-day sprint workflow)

Generate in batches of 3-5 posts, never more per sitting — quality collapses past 5. Per batch: 1 voice note or fresh substrate set in → 3-5 drafts with audit stamps → Reyhan's edit pass in chat → approved posts to the Pulse content calendar + `content/linkedin-posts.md`. Six to eight batch sessions covers a 30-day month.

---

## Weekly Content Calendar

| Day | Pillar | Topics | Format |
|-----|--------|--------|--------|
| Monday | RecruiterGTM Value | What can recruitment businesses get from the community? Case studies, DFY results, offshore placements, GTM Engine retainer | Text or video caption |
| Tuesday | Recruitment Systems | Candidate sourcing, lead gen, ATS workflows, n8n automations, tool comparisons, proven system walkthroughs | Text, case study, or video caption |
| Wednesday | AI Opinion | AI models, Claude Code, AI controversies, "How good is AI" series, tool breakdowns, adoption stats | Text, opinion post, or article |
| Thursday | Journey / Meme / Story | Personal founder journey, remote work, work memes (pattern-breaker), story with lesson | Text or image/meme |
| Saturday | Jobs of the Week | Open GTM/Ops/Recruiter roles, tips for candidates | Text post |

---

## Category Playbooks

### MONDAY — RecruiterGTM Value

**Purpose:** Show what recruitment businesses actually get from joining RecruiterGTM. This is not a sales pitch — it's proof. Every Monday post should make a recruitment founder think "that's exactly what I need."

**Always mention RecruiterGTM by name.** This is the only day to do it naturally without sounding promotional.

**Topic pool:**
- GTM Engine Management retainer results (case studies, numbers, what changed)
- Offshore placement wins (role, background, cost, outcome within X days)
- DFY OutboundOS setups (client before/after, what was built, what it runs)
- Member wins inside the Skool community
- What the Standard / Premium / VIP tiers include (framed as value, not pricing)
- The 48-hour placement SLA — what it means in practice
- Why we cap GTM Engine at 2-3 clients/month

**Angle to always hit:** The gap between what recruitment agencies are doing now vs what's possible with the right system and operator. RecruiterGTM is how you cross that gap.

**What to avoid:** Don't open with "Join RecruiterGTM." Let the result do the selling. The community name comes in naturally mid-post or as context, not as the hook.

**Proven hook styles for Monday:**
- "We just wrapped [X] with [type of client]. Here's what happened."
- "30 days ago I placed [role description] for a client. Here's the result."
- "What kills the margins for a recruitment business?"
- "Most recruitment agencies are sitting on [untapped asset]."

---

### TUESDAY — Recruitment Systems

**Purpose:** Teach recruitment founders something practical they can use or steal. Position Reyhan as the practitioner who actually builds and runs these systems — not a coach talking theory.

**Topic pool:**
- Tool walkthroughs: Clay, Pin.com, HeyReach, Lemlist, Apify, Prospeo, SalesQL, Juicebox
- Tool comparisons: Clay vs Pin for sourcing, HeyReach vs Lemlist, Apollo vs Clay
- OutboundOS case studies: how a specific client's outbound engine was built (stack, steps, results)
- Candidate sourcing systems: boolean search → email finding → scoring → outreach
- ATS workflow improvements
- n8n automations for recruitment ops
- LinkedIn content systems for recruiters (Recruiter Content Flywheel)
- Niche-specific builds (German market, property management, LanguageTech, DeepTech)

**Tone:** Genuinely impressed or genuinely critical. Practitioner sharing findings — never salesy. If a tool is better for one use case and worse for another, say exactly that.

**What to avoid:** Don't focus only on Clay. Reyhan uses and teaches a full stack. Vary the tools.

**Proven hook styles for Tuesday:**
- "Most recruiters source candidates like this: [old stack]. Here's what changed."
- "Clay just [did something]. Here's what it means for recruitment agencies."
- "I put [Tool A] and [Tool B] head-to-head on a live search. Here's what happened."
- "We are currently implementing [system] for a [niche] client. Here's the stack."

---

### WEDNESDAY — AI Opinion

**Purpose:** Position Reyhan as the most AI-literate voice in the recruitment space. Not talking about AI in a hype way — cutting through the noise with honest, specific takes.

**Topic pool:**
- AI adoption stats (how behind recruitment actually is vs other industries)
- What "real AI adoption" looks like for a recruiter vs "using ChatGPT for posts"
- Claude Code use cases for recruitment ops
- New AI model releases and what they mean practically
- AI controversies and honest takes (when AI fails, when it wins)
- "How good is AI" series: test a specific use case, report the result
- LinkedIn's 360 Brew algorithm and what it means for recruiters
- AI tools stack for recruitment: what Reyhan actually runs

**Tone:** Dan Martell-style — contrarian opener, practitioner voice, specific. Not hype-driven. Comfortable saying "this doesn't work yet" as well as "this is genuinely impressive."

**Proven hook styles for Wednesday:**
- "'Everyone is using AI now.' That is not even close to true."
- "[AI tool] just [did something]. Here's the honest take."
- "84% of humanity has never used AI. Not once." (with source)
- "Using ChatGPT to write LinkedIn posts does not count lol"

---

### THURSDAY — Journey / Meme / Story

**Purpose:** Pattern-break the feed and build personal connection. Two modes: (1) real story with a lesson, (2) meme that makes recruiters share it.

**Story/journey topics:**
- Founder origin: $5/hr VA → RecruiterGTM
- Leaving the job (TAB) and going all in
- Early mistakes: wrong clients, wrong hires, wrong positioning
- Mindset lessons: overconfident vs underconfident hardworker, MIT framework, build mode vs implement mode
- Salar's story and the Clay Cup
- The 1-10 Hormozi close — tested in my own business
- Going from "how do I close this lead" to "how do I help this person"

**Meme topics (recruiter/GTM specific — never generic):**
- The Epstein email format: fictional leaked email about why recruiters aren't joining RecruiterGTM
- Reaction memes: recruiter doing all BD + sourcing + content + ops alone
- "Old recruiting vs GTM system" contrast
- LinkedIn persona vs real life gap (Kate Erwin style)

**Tone for stories:** Vulnerable, specific, self-aware. Real names, real dates, real feelings. Hormozi echo is fine: "I get happier the harder it gets."
**Tone for memes:** Wry, recruiter-specific, 3 lines max caption. The image does the work.

---

### SATURDAY — Jobs of the Week

**Purpose:** Show the talent side of RecruiterGTM. Build audience among candidates (GTM Engineers, Ops Managers, Junior Recruiters) who may also become clients or referrers.

**Structure:** Light human opener → list of 3-5 roles with bullet points each → DM CTA with role name → PS about AI-supported search process → sign-off.

**Always include PS:** "Our search process is fully AI-supported. For you, that means faster feedback, a clear process, and no radio silence."

**Roles typically posted:**
- AI Video Content Creator (Pakistan or South Africa)
- GTM Engineer (Pakistan or South Africa)
- Ops Manager (Remote Global)
- Junior Recruiter / 180 Recruiter (South Africa, US hours)
- RecruiterOS Operator

**Tone:** Warm, not corporate HR. Feels like a founder posting roles for their team, not a staffing agency blasting JDs.

---

## Post Structure (Standard)

1. **Hook** — bold stat, claim, question, or 2-4 word opener. Alone on its own line. Never an intro sentence.
2. **Setup** — 1-2 lines max. One sentence per line. Establishes tension or context.
3. **Body** — follows one of the patterns below. Real specifics: names, numbers, timelines.
4. **CTA** — always. Comment keyword (ALL CAPS), DM, or book a call. Point to first comment.
5. **Sign-off** — always ends with:

> I'm Reyhan Khan, I post about how we help recruitment businesses install GTM Systems & Claude Code allowing their offers to stand out. If you want to follow the journey more closely, the newsletter link is in the first comment.

---

## Body Patterns

**Myth-Busting (❌/✅ format)**
- State the myth → bust it with a specific stat or fact
- Use ❌ for myth, ✅ for truth
- Good for: offshore objections, tool misconceptions, industry myths

**Case Study / Client Story**
- Situation → what we built → result (with numbers)
- Use numbered emojis (1️⃣ 2️⃣ 3️⃣) for steps
- Include: tool names, country, role type, outcome metrics

**Tool Comparison**
- Head-to-head with real search or test
- Bullets for each tool's experience
- Give a verdict — don't sit on the fence
- End with the broader systems lesson

**Tool Update / Quick Drop**
- Short and punchy — 6-10 lines max
- Hook: "[Tool] just did something."
- What changed → why it matters → what you can steal
- "Steal the flow" or "Watch it" as CTA language
- No sign-off block required — optional one-liner only
- Good for: HeyReach, Clay, n8n updates, new integrations

**List Post (numbered tips/mistakes)**
- 1. Title: explanation
- Real consequence of getting it wrong
- Good for: candidate advice, hiring mistakes, founder lessons

**Story / Journey**
- Start with a specific moment or memory
- Include names, dates, places (e.g. "Salar and I were at S&P Global in 2018")
- Reveal the transformation — old state → new state
- Self-aware tone: "I'm only in month 2..."

**Opinion / Industry Take**
- Lead with a counterintuitive claim
- Back it with data or a real observation
- Contrast "old way" vs "new way"
- End with what you're building / doing differently

**Hormozi-style Sales/Mindset**
- Personal experience first
- Framework or question that changed things
- Specific result
- Invite people to apply it themselves

**Meme / Pattern-Breaker (Thursday — image post)**
- Purpose: stop the scroll, get shares from people who'd never engage with a systems post
- Format: image with embedded joke/meme → short caption that lands the point → optional 1-liner CTA
- Caption structure: set up the joke in 1-2 lines → reveal → tie back to the offer or truth
- Tone: self-aware, recruiter-specific, never try-hard
- Proven formats Reyhan uses:
  - Fake leaked email (Epstein-style grainy monitor): fictional sender → subject line → highlighted punchline → tie to RecruiterGTM
  - Reaction meme (3am possessed kid, etc.): relatable recruiter scenario → image does the work → caption is the punchline
- Always recruiter/GTM-specific — never generic workplace humour
- Keep caption short (3-5 lines max). Image carries the weight.
- No sign-off block needed on pure meme posts — optional short CTA only

**Vulnerability / Truth Bomb (Kate Erwin style)**
- One honest admission or counterintuitive truth — on its own line
- 4-6 short sentences unpacking it
- No framework required — just the real observation
- Ends with a question or open invitation, not a hard CTA
- Good for: Thursday journey posts, breaking up systems-heavy weeks
- Examples: "My early calls were terrible." / "I had no idea what I was doing for the first 3 months."

---

## Voice Rules

**DO:**
- One sentence per line, almost always
- White space is structural — use it
- Real names, real numbers, real timelines
- ✔️ grey tick bullets for lesson/takeaway lists (Reyhan's preferred format)
- → arrows for lists (secondary use)
- • bullets for secondary lists
- ✅ ❌ for pros/cons or myth-busting
- 1️⃣ 2️⃣ 3️⃣ for step-by-step
- Language: 60% American, 40% British blend — simple, plain English
- Self-aware: acknowledge you're early-stage when relevant
- Reference real thinkers: Hormozi, Steven Bartlett, Covey
- "lol" or casual asides are fine when genuine
- Comment keyword CTAs in ALL CAPS (e.g., "Comment FLYWHEEL")

## DO NOT — Consolidated Rejection List (every rule Reyhan has ever flagged)

**This section replaces the scattered feedback memory files. Run every draft against this checklist before submitting.**

### A. Banned words and phrases (never use, anywhere)
- **"ship", "ships", "shipped", "shipping", "it ships", "today it ships", "ready to ship"** — Reyhan does not talk about content/products/launches as "shipping". Use: "live", "out", "up", "launched", "running", "in the market", "public".
- **"what actually matters"** and any variant ("here's what matters", "what truly matters") — vague AI slop.
- **"[X] is real"** as a standalone sentence — "The problem is real", "The shift is real", "The fear is real". Means nothing. Replace with the specific thing backed by a number, example, or observation.
- **"No fluff." / "No hype." / "No BS."** — saying what something *isn't*. Just say what it IS.
- **"Not theory. Not slides."** / any "Not X. Not Y." parallel negation — robotic AI tell, even when the rest is clean.
- **"Not a tool. Not a hire."** / any "Not a [noun]. Not a [noun]." cadence — same problem. Triple-beat negation is also banned.
- **"Not just [X]. [Y]."** — variant of the above, still robotic.
- **"valutainment"** — made-up word, never write.
- **"HR teams"** as the audience descriptor — use "recruitment agencies" or "talent acquisition teams" instead.
- **"leverage", "delve", "transformative", "guessing"** and any AI vocabulary — practitioner voice, not consultant voice. Extended 2026-07-19 (community banned-word canon): **"robust", "seamless", "pivot" (as business verb), "It's worth noting", "In today's rapidly evolving..."** — same ban, same reason.
- **Filler qualifiers like "real" before a noun** (e.g. "real access", "real results", "real impact") when the noun stands on its own. Cut the qualifier. "Access to practical use cases" beats "real access to practical use cases".
- **"seat" for an open position** (2026-07-17) — never "filled seat", "empty seat", "seat at risk". Use "role", "position", "hire", or "placement": "price on the value of a filled role". Applies to every channel and every artifact (posts, course decks, proposals, website).
- **"LinkedIn outreach" as a phrase in LinkedIn posts (Reyhan, 2026-08-03)** — write **"LI outreach"** instead whenever a post discusses outreach/automation ON LinkedIn. The platform flags posts pairing its own name with outreach/automation keywords (Reyhan had a post banned for "LinkedIn would ban me for saying this"). Same caution applies to other risky pairings ("LinkedIn automation" → "LI automation"). Naming LinkedIn normally in neutral contexts (e.g. "LinkedIn content") stays fine.
- **"lane"** (2026-08-12) — never use "lane" as a metaphor ("the search lane is empty", "own your lane", "the SEO lane", "stay in your lane"). Reyhan flagged it hard. Say the literal thing: "channel", "search", "where competitors aren't showing up".
- **"moat"** (2026-08-19) — never use "moat" as a business metaphor ("speed is the only moat", "your moat", "build a moat", "competitive moat"). Reyhan flagged it. Say the literal thing: "advantage", "edge", "what competitors can't copy".
- **"desk"** (2026-08-13) — never call the reader's operation a "desk" or frame them as a big firm / team / division. Our audience is ~80% solo recruiters or 2-senior + VA boutiques. Write to a solo founder / tiny team: "your recruiting", "your business", "your day", "on your own / a small team". → [[feedback_audience_solo_recruiters]]
- **Extended AI-tell words (added 2026-08-22 — from the public AI-slop canon: Wikipedia "Signs of AI Writing" + GitHub anti-slop repos + Hormozi/Welsh/Handley).** Never use, on any channel:
  - *Grandeur nouns:* tapestry, realm, landscape (as metaphor), ecosystem (as metaphor), symphony, beacon, cornerstone, bedrock, testament, odyssey, kaleidoscope.
  - *Copula-dodging verbs (use "is/are" instead):* serves as, represents (as filler), boasts, showcases, underscores, fosters, harnesses, highlights.
  - *"Smart"-sounding words:* unlock, paradigm / paradigm-shift, cutting-edge, revolutionize, crucial, pivotal, meticulous(ly), vibrant, unparalleled, game-changer, groundbreaking, synergy / synergize, unprecedented, elevate, streamline, empower, supercharge, frictionless, state-of-the-art.
  - *Filler openers:* "in today's fast-paced world", "in this digital age", "when it comes to", "at the end of the day", "needless to say", "the world of / the realm of X".
  - *Promotional filler:* nestled, bustling, teeming, myriad, plethora, treasure trove, brimming, breathtaking, captivate, mesmerize.
  - *Chatbot politeness:* certainly, absolutely, "I'd be happy to", moreover, furthermore, additionally, "let's dive into", "let's explore".
  - *Significance inflation:* "marks a shift", "watershed moment", "turning point", "pivotal moment", "cannot be overstated".
  - Deliberately KEPT (too common in legit recruitment/GTM copy — allowed unless clearly slop): optimize, scalable, integrated, data-driven, dynamic, transparent, proactive, versatile.
- **Hashtags. Ever. Anywhere.**

### B. Banned sentence patterns
- **2-3 word fragments after a full stop** — "More every week.", "Big things coming.", "Today it ships.", "More to come.", "Soon." Always write complete sentences with the article ("the", "a", "is") and the connector ("if you...", "because...", "so that...").
  - Bad: `Link in the first comment. Free value every week.`
  - Good: `The link is in the first comment, hit subscribe if you want more breakdowns like this.`
- **Short setup fragments** — "Here is the kicker.", "The catch.", "The thing is.", "Here is the thing." Replace with complete sentences ("Here is what I tell every agency owner who asks me this.") or open-ended questions ("So what is the catch?", "So why does nobody do this?").
- **"Here is the part most people miss"** and every variant ("Here's what most people miss", "what most people get wrong", "the part everyone overlooks") — super AI tell, banned outright (Reyhan, 2026-07-19). Just state the insight directly as its own sentence.
- **Robotic transitions** — "The result:", "Here is what actually changed:", "The outcome was:". Use casual: "Here is what that looks like:", "What happened:", "Results we get:".
- **Formal section headers mid-post** — "The brief:", "Jan to mid-March. Real numbers:". Just write the next sentence.
- **Dramatic sentence fragments used as headers** — same as above.
- **"Great question!" / "Hope this helps!" / "Excited to share..."** corporate openers.
- **Generic CTAs** — "Let me know what you think!", "Drop a comment below!", "Would love your thoughts!". Use a keyword or DM prompt.
- **Idioms and figurative language** — "weight in the market", "stalls", "had weight", "moving the needle". Plain language only.
- **Snarky contrarian-mocking hooks** — never open by mocking the audience ("Most recruiters are still using AI to rewrite JDs. That is not AI adoption.") Use one of the 3 approved hook patterns: personal/journey, stat/fact-first, or service announcement.
- **"landed"** as a verb for placements / wins ("we landed a client", "we landed the deal"). AI tell. Use the actual outcome ("we signed Tom for the OutboundOS pilot", "Patrick joined the community last week").
- **Truncated binary shorthand** — "sign or not", "win or lose", "pay or don't", "work or quit", "buy or pass", "in or out". These compress the natural full phrase ("whether they sign with us or not") into AI shorthand that no human actually writes or says. **Always write the full phrase: "whether [subject] [verbs] or not."** Established English idioms like "now or never", "all or nothing", "do or die", "make or break" are fine — they exist in natural speech and predate AI. The test: would you SAY this out loud at the end of a sentence in conversation? If "sign or not" sounds robotic when spoken, it doesn't belong in a post. Flagged 2026-06-04 after Reyhan caught "Every recruitment agency we pitch gets a mini dataset, sign or not." This is the AI-compression pattern.
- **Copula avoidance (2026-08-22)** — replacing "is/are" with "serves as / represents / functions as / acts as". Just use "is/are". "This serves as a lead magnet" → "This is a lead magnet."
- **Present-participle stacking (2026-08-22)** — "by leveraging X, you're gaining Y that empowers you to Z." Stacked -ing verbs that delay the point. Rewrite as short active sentences.
- **Passive-voice + feature-dump chains (2026-08-22)** — "candidates are sourced, screened and matched using A and B and C…". Use active voice and 1–3 real outcomes, never a feature list joined by "and".
- **Hollow forced triads (2026-08-22)** — three same-length clauses that pad without specifics ("faster, smarter, better" / "source, screen, scale"). NOTE: deliberate punchy triples in Reyhan's voice ("Post. Capture. Get found." / "Three numbers. Three skills.") are FINE — ban only the hollow, generic ones.

### C. Hollow-line check (auto-rejected)
A line is hollow if it could appear in any other founder's post. Examples Reyhan has rejected:
- "That kind of response is what fulfilment looks like to me."
- "This is what the work is all about."
- "Doing what I love every day."
- "Grateful for the journey."

Every line must trace back to a Reyhan-specific anchor — a person, number, date, project, piece of his story, or his actual mission framing. If a line is abstract, delete it and rewrite with the concrete fact behind the feeling.

### D. Em dash rules
- **Max 1 em dash per post in prose**. Default to zero. Every em dash is a candidate to be cut and rewritten as a new sentence.
- **Sign-off separator is mandatory and exempt** — every post ends with `——` (DOUBLE em dash, U+2014 twice, no spaces between) on its own line, then the standard "I'm Reyhan Khan…" sign-off block. Single `—` is wrong. The separator does not count against the max-1 limit.

### E. Mission framing — locked phrasing
- **The RecruiterGTM mission line is:** "I started RecruiterGTM to give every recruiter access to practical use cases of best in class AI systems."
- **Never** frame it as "teach recruiters how to operate at 3 to 5x pace". The 3-5x pace is a downstream outcome, not the mission. It can appear in benefit copy describing the *result*, never as the founding mission.

### F. Voice — what to do instead
- **Every post targets recruiters / recruitment agency owners.** Even when Reyhan shares a personal system, win, or tool, the takeaway must be framed for a recruitment agency — which always means BOTH sides of the desk: client BD (leads, proposals, terms) AND candidate workflows (sourcing, submissions, follow-ups). Never leave a post as a generic founder/SaaS/sales take. If the draft would resonate equally with a SaaS founder, re-anchor it to a recruiter's day. Flagged 2026-06-22 after a Claude-agent post drifted generic.
- **Pulse / FulfillmentOS posts: never lead with placements or ATS framing.** Pulse is an all-in-one fulfillment product (tasks, calls, pipeline, content, scheduling, Skool sync) — a hook or headline built on "filled X positions" / placements shrinks it to a recruiter-only ATS. Placements are body-level proof, one item among several, never the frame. Flagged twice by Reyhan 2026-07-23 during the FulfillmentOS series.
- One sentence per line, almost always
- White space is structural — use it
- Real names, real numbers, real timelines, real dates
- Self-aware, practitioner voice ("I am only in month 4 of running this...")
- Reference real thinkers when relevant: Hormozi, Steven Bartlett, Covey, Drucker, Bartlett
- "lol" or casual asides are fine when genuine
- Comment keyword CTAs in ALL CAPS (e.g., "Comment FLYWHEEL")
- Don't use "we" when "I" is more honest
- Reader should be able to read the post out loud and have it sound like Reyhan speaking, not Reyhan writing telegrams

### G. Bullet rules
- Within a single list, every bullet uses the same icon. Don't rotate inside one list.
- Max 2 different bullet styles per post (numbered emojis 1️⃣2️⃣3️⃣ count as one consistent set).
- For use cases / steps: use numbered emojis 1️⃣2️⃣3️⃣
- For deliverables / feature lists: pick ONE icon (⚡, •, →, ✔️) and stick to it for the whole list

### H. CTA keywords — never invent or swap
- Keep keywords verbatim across revisions. If Reyhan says "JOIN", keep "JOIN". Do not substitute "CLAUDE" because the topic is Claude.
- If no keyword was specified, ask before writing one in.
- Approved keywords: FLYWHEEL, PLAYBOOK, NEWSLETTER, OUTBOUND, CALL, ENGINE, WORKFLOW.
- **Never** use RECRUITERGTM as a keyword — too self-promotional.

### I. YouTube-first
- Every major piece of content starts as a YouTube video, then repurposes to newsletter + LinkedIn post that links back to the video.
- When Reyhan says "let's create content about X", default to YouTube video first.

### J. Skool community posts
- Different tone from LinkedIn — feel like messaging a group chat. Casual, conversational, complete sentences.
- No bullet-point sells, no dramatic line breaks for effect, no "Most people do X wrong" framing.

### K. Workflow rules
- **`body` pushed to Pulse is the FINAL post copy ONLY** (locked 2026-08-17) — never prepend QC/theme/gate markers, a `--- CONTENTOS … ---` line, or any "delete before posting" text into `body`. That field IS the content box Reyhan approves and schedules from; anything extra is fluff he has to delete every time. Internal metadata (theme, pillar, gate scores) goes in Pulse's dedicated notes/internal field (or the post title), never the body.
- **LinkedIn blank-line spacer (locked 2026-08-17):** every empty line between paragraphs in a LinkedIn (and Skool) post `body` must contain a single **`⠀` braille-blank (U+2800)** character. LinkedIn's composer strips truly-empty lines on paste, collapsing the post into a wall of text; the ⠀ preserves the spacing. Rule: put ⠀ on each paragraph-break blank line (including the blank lines either side of the `——` sign-off separator). Do NOT spacer between consecutive/bullet lines that are meant to stay tight (→ / 1️⃣ lists). Mechanically: replace each blank line (`\n\n`) with `\n⠀\n`. This applies to the delivered `body` for every LinkedIn/Skool post; blogs (HTML) and YouTube bullet shot-lists are exempt.
- This skill is MANDATORY for any post drafting — LinkedIn, Skool, community, newsletter caption, comment, anywhere copy gets written. Never freehand a post without loading content-os first.
- ALWAYS show the post in chat for Reyhan to approve BEFORE pushing to Pulse, Skool, or anywhere else. Never write to a tracker first then ask.
- Axe bullets 🪓 are LinkedIn / Skool only. NEVER use 🪓 in emails — emails use plain `•` or `-` (rule lives in email-writer/SKILL.md too).
- **Pulse content calendar is the content tracker (locked 2026-07-13).** Post ideas, drafts, scheduling, and status live in the Pulse (Supabase) table `team_content_posts` — columns: `title`, `body`, `channel` (linkedin/skool/youtube/podcast/newsletter/other), `status` (`idea` / `scheduled` / `posted` — enforced by DB check constraint; `idea` added 2026-07-21 when the 216-row idea backlog was reclassified out of `scheduled`), `scheduled_at`, `posted_at`, `author_id`. The idea backlog = rows with `status = 'idea'`; a post is `scheduled` only once it has a real `scheduled_at`. At the start of any content batch, read the week: `SELECT * FROM team_content_posts WHERE (status = 'scheduled' AND scheduled_at >= [week start]) OR status = 'idea' ORDER BY scheduled_at NULLS LAST`. After Reyhan approves a draft in chat, `UPDATE` the row's `body` with the final copy (escape `'` as `''`). Reyhan finalizes and schedules on LinkedIn himself. Reyhan's rows use author_id `01fadbf8-ce2f-43a1-a2d7-8908b3ac6c11`. For video posts, recording talking points may sit inside `body` below a `--- RECORDING BULLETS (delete before posting) ---` marker. The Notion LinkedIn Content Tracker is retired for tracking (2026-07-13).
- **Date-driven daily flow (locked 2026-08-01 — born from the August 31-day challenge; this is the DEFAULT workflow going forward):** Reyhan is posting all 31 days of August 2026 ([[project_august_2026_content_challenge]]). When Reyhan names a date ("today's post", "the Aug 1 post", "next up"), the topic comes from the Pulse content calendar — pull the row via Supabase: `SELECT * FROM team_content_posts WHERE scheduled_at::date = '[date]' AND channel = 'linkedin'`. The row's `title` + `body` are the topic and rough substrate; Reyhan's wording in the rough draft carries into the final where it works (STEP 0.5 substrate rule). Never invent a different topic when a row exists; if NO row exists for that date, flag the gap in the 31-day plan and ask — do not fill it silently. Finalize through the full pipeline (STEP 0 → STEP 0.5 → Sections A–M → copy-engine loop + humanizer + audit stamp), show in chat, and ONLY after Reyhan approves: 1️⃣ `UPDATE` the row's `body` with the final copy (keep `status` and `scheduled_at`; escape `'` as `''`), 2️⃣ append to `content/linkedin-posts.md` (rule below). If the post includes a graphic, generate it via `graphic-generation` AFTER copy approval and add it to Pulse with the post — `team_content_posts` has no media column yet, so save the graphic to the post's project folder and reference its file path/URL at the bottom of `body` under a `--- GRAPHIC (attach when posting) ---` marker.
- **After Reyhan finalizes any post**, append it to `content/linkedin-posts.md` at the TOP (newest first), using the existing entry format (date + category + CTA + fenced post body). Same step also updates the post's row in the Pulse content calendar (`status`/`posted_at` once posted). The local file is read by Step 0 of this skill on every future run, so this is non-negotiable. Locked 2026-06-08, tracker updated to Pulse 2026-07-13.

### L. Video post captions — keep them short (locked 2026-06-08)
- L0. When the LinkedIn post is built around a video (Loom, Tella, native upload), the caption stays short. Once the viewer hits play, LinkedIn collapses the caption — anything beyond the first few lines goes unread.
- L1. Target structure for video posts: hook (1 line) → 1-3 short body lines that set up what they're about to watch → single CTA → optional 1-line aside. Total under ~80 words of body copy.
- L2. The standard "I'm Reyhan Khan…" sign-off block is OPTIONAL on video posts. Drop it when the body is already tight. Keep it when the post genuinely doubles as a text post with the video as an accompanying clip.
- L3. Numbered lists (like "1. Tool name" rows) are fine inside a video caption AS LONG AS each row stays to a single line. Let the video carry the explanation, not the caption.
- L4. Hook still mandatory. Hollow-line check still applies. Banned patterns still banned. Short does NOT mean lazy.
- L5. **Lead-magnet / walkthrough video posts are FULL-LENGTH (flagged by Reyhan 2026-08-01 on the ContentOS skill update post).** When the video presents a system, skill drop, or downloadable (anything with a landing page or a comment-keyword lead magnet behind it), the short-caption rule does NOT apply. Write the standard full structure: hook → setup paragraphs → ✔️ bullet list of what the system/asset contains (pull the bullets from the landing page or source asset, never invent features) → CTA → `——` + full sign-off block. The sign-off is MANDATORY on these, not optional. L0–L3 short captions are for simple demo/clip posts only. When unsure which mode a video post is, ask.

### M. Final pass before submitting
Run every draft through this checklist:
1. Did I load context first? (Step 0)
2. Any banned words or phrases from section A?
3. Any banned sentence patterns from section B?
4. Hollow lines from section C — could any line appear in another founder's post?
5. Em dash count in prose ≤ 1, and `——` separator before sign-off?
6. If RecruiterGTM mission is mentioned, is it the locked phrasing?
7. Is there a real specific (name, number, date, project) in every paragraph?
8. Read it out loud — does it sound like Reyhan speaking?
9. Approval-before-push check — am I about to push to Pulse/Skool without showing? Stop.
10. STEP 0.5 check — one-sentence POV locked, fresh substrate (not corpus), one-line hook, and the audit stamp (`Checks: humanizer pass ✓ ...`) present on the draft?

If any of these fail, rewrite before submitting. Reyhan rejects on first hollow line.

---

## Content Pillars

| Pillar | Max % | Examples |
|--------|-------|---------|
| Knowledge/Value | 40% | Tool comparisons, GTM systems, sourcing stacks, frameworks |
| Personal/Journey | 25% | Founder story, behind-the-scenes, "against the odds" |
| Authority/Social Proof | 25% | Client case studies, placement results, real numbers |
| Promotional | 10% | Lead magnets, RecruiterGTM, newsletter sign-ups |

---

## Keyword CTAs (use these — don't invent new ones without asking)
- FLYWHEEL — Recruiter Content Flywheel Checklist
- PLAYBOOK — Recruiters AI Playbook
- NEWSLETTER — Recruiter's Guide to Launching a Newsletter
- OUTBOUND — OutboundOS setup walkthrough video
- CALL — 1-10 question flow for strategy calls
- ENGINE — GTM outbound workflow breakdown (14-touchpoint)
- WORKFLOW — Sequence / process walkthrough
- CONTENTOS — Reyhan's ContentOS LinkedIn writing skill (the idea → framework → research → scoring pipeline; approved 2026-07-29)

**NEVER use RECRUITERGTM as a keyword — too self-promotional.**

---

## Real Examples (Voice Reference)

**Hook examples from real posts:**
- "Clay just changed their pricing."
- "Offshore hiring isn't the problem. These 3 Myths are!"
- "Overconfident hardworker >> Underconfident hardworker"
- "Most recruiters are sitting on a gold mine and don't even know it."
- "What kills the margins for a recruitment business?"
- "'Everyone is using AI now.' That is not even close to true."

**Transitions that work:**
- "Here is what actually changed:"
- "The honest pros and cons for recruitment agencies:"
- "Here is what [situation] looks like in practice:"
- "I am only in month [X] of running my own business and..."
- "Stop [old behavior]. Start [new behavior]."

**Verdicts / Conclusions:**
- "The goal is always the same: [outcome]."
- "Most agencies have the tool BUT — almost none have the system. That's the gap."
- "You cannot 'hack' this with tricks. You align with it by being clear, useful, and consistent."

**Reyhan's origin story (use for Thursday/journey posts):**
- Started as a $5/hr VA
- 10 years running ops and systems across agencies, bizopps, B2B infoproducts
- Coached 700+ clients before going all in
- Left corporate to build RecruiterGTM — not because it sounded cool, but because he had to
- "I get happier the harder it gets because I know no one else will follow" (Hormozi echo — authentic to him)
- God, energy, mindset references are fine when genuine — not performative

**Reyhan's recurring frameworks (reference these naturally):**
- MIT (Most Important Task) — identify the night before, complete first 60-90 mins
- Implement mode vs Build mode — reactive work vs building the actual offer
- "Buy back your time" — offshore operators free up the founder
- Content flywheel — one long-form piece → multiple posts
- Free Value Fridays (early brand) — spirit still applies: lead with generosity

**Brand evolution — NEVER reference old names:**
- Remote Ops Academy → AI Ops Academy → RecruiterGTM (current, always use this)
- Old sign-offs had "COO at Remote Assistants" — dead brand, ignore

---

## Real Numbers & Social Proof (Use When Relevant)

- GTM Engine Management retainer: 2-3 clients/month max (intentional constraint — quality over scale)
- Lemlist case study (LanguageTech/DeepTech client, Jan–Mar 2026): 3,456 contacted / 882 accepted invitations (28.6%) / 318 replied (10.1%) / 100 interested — 65% responses on LinkedIn, 35% on email
- Pakistan: 3rd biggest English-speaking country, 108M English speakers
- South Africa: native English speakers — 25% of placed candidates
- 65% of placed candidates from Pakistan
- Offshore 360 recruiter placement result: 10 years experience (McKinsey, S&P background), $2.5k base + $1k/placement, took over 80% of screening calls within 30 days
- Q2 additions to GTM Engine package: Lovable website revamps + ATS audits (on top of outbound engine)
- Hormozi 1-10 close: "Why not a 0?" → "What makes it a 10?" — tested in own business, month 2

## Pricing (RecruiterGTM — for Monday value posts)

| Tier | Price | Headline |
|------|-------|---------|
| Standard | $1,497 one-time | OutboundOS lite + 1:1 roadmap call + community |
| Premium | $4,497 one-time | Everything + DFY OutboundOS or offshore placement |
| VIP | $8,497 one-time | Everything + GTM Engineer placement + 14-day sprint + 8 weeks 1:1 |
| GTM Academy | $4,497 one-time | Offshore talent placement, 48hr candidate list SLA |
| GTM Engine Management | ~$2k/month | Fully managed outbound retainer, max 2-3 clients |

## Writing a Case Study Post — Specific Rules

- Don't sound like a screenshot dump. Write the narrative, not the data readout.
- Numbers support the story — they don't replace it.
- Always include: what made it work beyond the system (human/behaviour factor)
- Mention the constraint if relevant (e.g. "we only take 2-3 clients/month on this")
- Don't mention all metrics — pick the 3-4 that tell the story
- Niche matters: mention it (LanguageTech, DeepTech, Property Management, etc.)

## Writing Tool Posts — Specific Rules

- Sound genuinely impressed or genuinely critical — never salesy
- Reyhan is a practitioner sharing what he found, not promoting a tool
- For comparisons: give a real verdict, don't sit on the fence
- OK to admit Clay's complexity while praising Pin's simplicity — honesty builds trust
- When impressed: lead with the specific thing that impressed you (e.g. "This email was auto-generated...")
- When critical: frame as "here's what I found, here's what the data says"

---

## Generation Instructions

When asked to write a post:

0. Run STEP 0 (context load) then STEP 0.5 (POV → substrate → anchor → hook → body). No draft starts from a bare topic.
1. Confirm the content type and day (if not given, ask or pick the best fit)
2. Pick the body pattern that fits the topic
3. Write the hook first — if it's weak, the post fails
4. Keep each sentence short. One per line.
5. Include at least one real specific (number, name, tool, country)
6. End with a CTA that matches an existing keyword or a DM prompt
7. Always append the sign-off block
8. Do NOT add hashtags
9. After drafting, run a quick self-check:
   - Would someone in Reyhan's niche save or share this?
   - Does it sound like a practitioner, not a consultant?
   - Is the hook strong enough to stop the scroll?

---

## Influencer Style References

### Matt Gray (PRIMARY — rated higher, steal format freely)
linkedin.com/in/mattgray1 | Founder, content systems builder

> **Deep reference (added 2026-07-30):** `.claude/skills/content-os/matt-gray-top-posts.md` — his Top 10 LinkedIn posts with his own per-post framework breakdowns (hook construction, long-form image logic, list rhythm, interview distillation), quoted verbatim from his Founder OS guide. Read it when drafting list posts, carousels, or interview-distillation posts.

**What makes him work:**
- 67% of viral posts open with "I" or "I've" — vulnerability first, then credibility, then result
- Hook formula: broken state ("I was -$15k") → discovery → outcome ("built multiple 7-figure businesses")
- Always quantified: follower counts, revenue numbers, timelines — never vague claims
- "Steal this..." permission language — positions frameworks as gifts, not pitches

**His signature structures to borrow:**
- Vulnerability → Framework → Actionable breakdown → CTA
- "1 long-form piece becomes 25+ pieces" (content waterfall logic — adapt for recruitment: "1 case study becomes 5 posts")
- 30-in-30 batching: pre-written hooks + topic buckets = velocity without burnout

**Voice notes:**
- Short declarative sentences. Alternating rhythm: long + punchy + long.
- Active verbs only: build, scale, steal, ship — never "consider" or "perhaps"
- "Here's the secret:" as a transition
- Zero corporate fluff — reads like a text message from a smart friend
- Always ends with a system, not just an insight

**How Reyhan applies this:**
- Lead with personal truth (e.g. "I spent 60 minutes on a proposal that was 70% template work")
- Then reveal the system fix
- Steal the batching format for content velocity (addresses current priority: 5x/week LinkedIn)

---

### Kate Erwin (MEME / PATTERN-BREAKER reference)
linkedin.com/in/kateerwin | B2B copywriter, personality-first content

**What she actually does (not traditional memes):**
- Vulnerability hooks that open real conversation: "My early career was dark", "Painfully obvious tip"
- Contrarian positioning: anti-sameness, self-deprecating commentary about the gap between LinkedIn persona and real life
- Industry-specific humour — meta observations about B2B absurdities, not generic workplace jokes
- One sentence per line, 5-7 lines max, white space does the work
- Builds on 35-44 comment posts in her niche, not chasing viral

**How Reyhan applies this:**
- Thursday meme/pattern-breaker posts: image carries the joke, caption ties it to recruitment truth
- Vulnerability posts on Thursday: one honest admission → unpack it → no hard CTA
- The Epstein email and possessed kid formats Reyhan already uses ARE the right move — keep doing them
- For caption writing style: borrow her short-line, no-jargon approach

---

### Dan Martell (SECONDARY — contrarian hooks, mentor positioning)
linkedin.com/in/dmartell | SaaS coach, author of "Buy Back Your Time"

**What makes him work:**
- Contrarian opener that challenges convention: "One AI used to cut it. That era's over."
- Mentor tone — positions himself as accessible, not distant: "Message me 'AISTACK'"
- Structured, scannable breakdowns with bold highlights
- Two-part CTA: save prompt + low-friction DM offer
- Radical transparency: real metrics, real processes, real wins and losses

**His signature structures to borrow:**
- Contrarian claim → why the old way is dead → new system → accessible CTA
- Posts his real tech stack regularly — distinctive in his space
- "One [old thing] used to work. In 2026, it doesn't." (hook template)

**Voice notes:**
- Quality over velocity — one strong post beats five average ones
- Mentor/coach positioning, not peer (Reyhan is somewhere between both)
- "Message me '[KEYWORD]'" removes friction vs. funnel-first
- Core thesis maps directly to RecruiterGTM: buy back your time = offshore GTM operators

**How Reyhan applies this:**
- Use his contrarian hook template for tool/industry takes
- "Buy back your time" framing for offshore placement posts — it's the same thesis
- Accessibility CTA style: "Message me 'GTMSYSTEM'" instead of always pointing to first comment
- Real stack posts: Clay + Lemlist + n8n + HeyReach as a signature content piece
