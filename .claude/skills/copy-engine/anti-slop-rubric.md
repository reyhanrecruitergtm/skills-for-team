# Anti-Slop Rubric — the final gate before any writing ships

The last quality gate in the writing pipeline. Runs AFTER the copy-engine loop + humanizer, on every blog post, LinkedIn post, email, newsletter, proposal, and script. If a draft trips any check, it loops back — it does not reach Reyhan's approval queue.

Built from expert frameworks: **Alex Hormozi** ("Mozi" — his AI-slop memo), **Wikipedia "Signs of AI Writing"**, Ann Handley, Paul Graham ("Write Like You Talk"), plus aicheckr / HubSpot anti-slop checklists. Continuously improved by the Content OS research cron. Supplements — never overrides — the existing [[feedback_em_dashes]], [[feedback_banned_copy_phrases]], and `communication-style.md` rules.

> **Note for Reyhan:** you mentioned "Alex or Mozy" — the research points to both being **Alex Hormozi** (nickname "Mozi"). If you meant a second, different source, tell me and I'll layer it in.

---

## The 5 layers (pass/fail — any fail = revise)

### Layer 1 — Syntax & rhythm
- [ ] **No forced negation.** Kill "not just X, but Y" / "it isn't X, it's Y." State the claim directly.
- [ ] **Sentence length varies.** Mix short and long (roughly 4–20 words). No stacked staccato 3-word "punches."
- [ ] **Em dashes:** obey the house rule — default zero, max one per email/post (stricter than the generic "1 per 1000 words"). → [[feedback_em_dashes]]
- [ ] **No essay transitions:** "Firstly," "Moreover," "Furthermore," "In conclusion," "Additionally."
- [ ] **No rule-of-three adjective stacks:** "powerful, robust, scalable." Replace with one specific.
- [ ] **No gimmick devices** (added 2026-08-13): no bucket brigades ("Here's the deal:", "Want to know the best part?", "Now:"), no "here's the kicker" fragments, no formula listicle openers. We adopt the *substance* of top-SEO writing (readability, answer-first, original data, scannability) but reject these tics — they read as marketing slop in Reyhan's practitioner voice.

### Layer 2 — Vocabulary & tone
- [ ] **No AI trigger words:** unlock, discover, delve, transform, revolutionise, leverage, seamless, robust, landscape, navigate, elevate, tapestry, realm, ecosystem, harness. (Extends the E4 list in `seo-engine`.)
- [ ] **No cliché metaphors:** "vibrant tapestry," "dynamic ecosystem," "ever-evolving landscape."
- [ ] **Plain verbs:** built, found, measured, tested, broke, tried, shipped — not "utilise/facilitate."
- [ ] **No hedging:** "might potentially," "depending on various factors," "could help some teams." Make definitive claims with scope instead.
- [ ] **No banned phrases** (house list). → [[feedback_banned_copy_phrases]]

### Layer 3 — Specificity & evidence (the credibility layer)
- [ ] **Every number has a named source + date, or it's cut.** No orphan stats ("73% of businesses…"). No hallucinated citations. → [[feedback_preflight_check]]
- [ ] **At least one real, specific proof point:** real name (with permission), real number, real timeframe. "Marc Holdaway came from the Benjamin Mena episode" beats "a client once told me."
- [ ] **Audience named precisely:** "recruitment agency owners doing $200k–$2M" — not "businesses" or "everyone."
- [ ] **Questions answered directly with data**, not restated as "pricing is important…".
- [ ] **No knowledge-cutoff / hedging disclaimers** in the body ("based on available information").

### Layer 4 — Structure & flow
- [ ] **Opens with an outcome or specific hook**, never a macro throat-clear ("In today's fast-paced world, AI is transforming…").
- [ ] **No formulaic "Challenges/Benefits" template** sections. Show real tension: "we tried Y, Z broke, here's what we do now."
- [ ] **Conclusion reinforces the claim with scope**, doesn't hedge it away ("results may vary").
- [ ] **Caveats live in one place**, not scattered as parentheticals in every sentence.
- [ ] **Heading ≠ first line restated.** The first sentence under a heading adds NEW information (also the AEO extraction win).

### Layer 5 — Voice & humanity (does it sound like Reyhan?)
- [ ] **Written TO the reader, not AT them.** No "Here is your guide," "I hope this helps!"
- [ ] **Real stakes or emotion** — a win, a loss, a bet made. Not a reference-manual monotone.
- [ ] **Specific CTA**, per house rules ("Lmk if that's of interest" / "Comment KEYWORD") — never "let me know what you think."
- [ ] **Practitioner, British/neutral English**, matches `communication-style.md` and the client voice file.
- [ ] **Plain-text clean** — no zero-width/unicode artifacts from paste.

---

## Extended AI-tell canon (added 2026-08-22)
Scan every draft for these on top of the layers above (source: Wikipedia "Signs of AI Writing" + GitHub anti-slop repos + Hormozi/Welsh/Handley):
- **Words:** tapestry, realm, landscape/ecosystem (as metaphor), symphony, beacon, cornerstone, testament, odyssey; serves as, boasts, showcases, underscores, fosters, harnesses; unlock, paradigm, cutting-edge, crucial, pivotal, meticulous, vibrant, unparalleled, game-changer, groundbreaking, synergy, unprecedented, elevate, streamline, empower, supercharge, frictionless; nestled, bustling, myriad, plethora, treasure trove, breathtaking, captivate; certainly, absolutely, moreover, furthermore, "let's dive into".
- **Openers:** "in today's fast-paced world", "in this digital age", "when it comes to", "at the end of the day", "the world of X".
- **Significance inflation:** "marks a shift", "watershed moment", "cannot be overstated".
- **Patterns:** copula avoidance (use is/are); present-participle stacking; passive + feature-dump chains; hollow forced triads (keep deliberate punchy triples).

## The 60-second test (Hormozi's shortcut)
Read it aloud. If it sounds like a person who has actually done the work talking to another person, it passes. If it sounds like a press release or a Wikipedia intro, it fails. Specificity and stakes beat polish.

## How it plugs into the Content OS engine
- It is **Quality Gate step 2** in `projects/content-os-engine/PLAN.md` (after copy-engine + humanizer, before the Pulse approval queue).
- Every writing skill (content-os, email-writer, newsletter-writer, proposal-generator, youtube, seo-engine blogs) runs a draft through this checklist before output.
- The Content OS research cron (every 15 days) adds newly-found expert rules here, so the rubric compounds.

## Sources
Alex Hormozi (AI-slop memo) · Wikipedia "Signs of AI Writing" · Ann Handley (13 writing rules) · Paul Graham "Write Like You Talk" · aicheckr 12-pattern list · HubSpot anti-slop checklist.
