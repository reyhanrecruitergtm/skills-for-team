# RecruiterGTM SEO / AI-Search Playbook

*Team reference — Noroze (writing + off-page) & Daniyal (technical + schema + build). Last updated 2026-08-17.*

---

## 0. What we're actually doing

We write content that gets **cited by AI engines** — ChatGPT, Perplexity, Google AI Overviews, Claude — while also ranking on classic Google. It's **one discipline, not two.** When a formatting choice trades off between "looks like a normal Google result" and "easy for an AI to extract and cite," **AI extraction wins.**

- We do **not** call this "AEO" and we do not sell a renamed SEO audit. AI-engine citation is just what modern SEO is now.
- The headline success metric is **AI citations**, not ranking position.

**Where we stand (Aug 2026):** RecruiterGTM is cited ~2 times across all AI engines. A tiny competitor doing this properly (hikmahaiagency, ~11 pages, low authority) sits at ~100. **Structure and off-page presence beat volume and beat domain authority.** That gap is the opportunity, and this Playbook is how we close it.

**The 80/20 you must remember:** on-page writing (schema, FAQ, headings) is table-stakes and mostly DIY. **84–93% of AI-citation weight comes from OFF our website** — third-party mentions, entity presence, reviews. So great writing is necessary but not sufficient; the off-page engine (Section 4) is where the real lift is.

---

## 1. On-page writing rules (Noroze — every post)

These make a post extractable by AI engines. Non-negotiable.

1. **Answer first.** The opening paragraph is a direct 40–60 word answer to the target question. No "In this article we'll explore…" — AI skips it and humans bounce.
2. **Every H2 answers before it expands.** Lead each section with a 40–60 word direct answer, then go deeper.
3. **H2s phrased as real questions** where natural ("How do recruiters automate sourcing?") — matches how people prompt AI.
4. **One citable stat per 150–200 words**, each with a named source + link.
5. **Original data is the magnet.** Every post carries at least one first-hand number, client result, or tested verdict a competitor would have to cite us for. AI cites source material, not summaries.
6. **FAQ section (3–5 Qs)** on every post — this is the single biggest lever for AI citation.
7. **Tables over paragraphs** for any comparison. AI parses tables cleanly.
8. **Semantic chunking** — bullets, numbered lists, short paragraphs.
9. **The lift test.** Every section, pulled out on its own, must still carry the entity + the context + the claim. One subject per paragraph. (AI retrieves at passage level, not page level.)
10. **Single-URL completeness.** One post answers what it is / who it's for / how to choose / what it costs. Top-cited pages do all four.
11. **Comparison posts give explicit verdicts** ("Best for solo agencies", "Best budget option") with stated criteria — the exact format LLMs lift into answers.
12. **Freshness counts.** Content updated within 30 days earns ~3.2× more AI citations. Visible "last updated" date required. Every post re-enters the queue at its 30-day mark.

**Word count:** at least the median of the top 5 results for the query (within 10%). Pillar guides 2,000+ words; spokes follow the SERP median. Never under 600 words.

---

## 2. Voice rules (Noroze)

- **Practitioner, not consultant.** Write like the operator who's done the work.
- Real numbers, real client names (with permission), real timelines.
- **British / neutral English.** Not American marketing speak.
- **No AI vocabulary:** leverage, delve, crucial, pivotal, landscape, navigate, robust, seamless, ecosystem.
- **Max 1 em dash per post.**
- **Industry-specific every sentence.** If a sentence could apply to "any business," rewrite it for recruitment agencies.
- Audience skew: ~80% solo or small (2-senior + VA) boutique recruitment agencies, not big staffing firms. Write to a founder/tiny team.

**Never:** promise revenue or results; claim we've delivered SEO/AI-search results for a client (no such case study exists); invent a stat; recommend a tool without its affiliate link. Any number not on the verified stats list gets flagged to Reyhan before it's published — never guessed.

---

## 3. Structure + technical rules (Daniyal owns the technical; Noroze respects the structure)

**Structure (per post):**
- Exactly one H1, containing the primary keyword.
- Internal links: 1 pillar page + 2 spoke posts minimum.
- CTA at the end of every post (book a call / join community / lead magnet).

**Technical / schema (Daniyal):**
- **JSON-LD on every blog post:** `BlogPosting` + `FAQPage`. Service/Course schema on service pages.
- **Organization schema** (site-wide) with `sameAs` to every owned profile. *Current gap to fix:* add the RecruiterGTM company LinkedIn, `alternateName`, `foundingDate`, `founder.url`, and `knowsAbout` (recruitment automation, candidate sourcing, GTM systems). See the entity work in Section 4.
- **Crawlability (Gate 0 — if this fails, nothing else matters):** robots.txt must allow GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended. Load-bearing content must be **server-rendered** — nothing important hidden in images, PDFs, or client-only JS. AI can't cite what it can't read.
- **Metadata:** title ≤60 chars, description ≤155, canonical URL, OpenGraph image.
- **Visible `dateModified`** (freshness signal, rule 12).
- **On publish:** update sitemap → IndexNow ping → request indexing in GSC for priority pages.

---

## 4. The off-page engine (the real lift — Noroze drives, Reyhan opens doors)

This is where 84–93% of citation weight lives. Three workstreams. (Full task list + targets is in the shared **SEO/AEO Tracker** spreadsheet.)

**A. Entity / knowledge-graph — make AI able to identify us (C17).**
Fix how AI resolves "RecruiterGTM" as a known entity: dedup the LinkedIn profile, create Crunchbase, list on G2 as "Pulse by RecruiterGTM", correct the stale RocketReach description, standardise our one-liner everywhere, add the company page + fields to the site's Organization schema. An engine can only attribute a claim to an entity it can resolve.

**B. Citation-source targeting — earn presence where AI already pulls from (C16).**
Each metrics cycle we pull the exact third-party domains AI cites for our category (currently Reddit, LinkedIn, then small sites like herohunt, metaview, hiretruffle, selectsoftwarereviews). We deliberately earn presence there — guest posts, mentions, listings — easiest-first. Distribution stops being "post to LinkedIn" and becomes "get into the sources the models pull from."

**C. Recommendation-signal reviews (C15).**
Coach happy clients/members to leave reviews (G2, LinkedIn recommendations) phrased as a *specific recommendation* ("best for solo recruitment agencies"), not generic praise. LLMs weight recommendation-phrased reviews as citation signals. Real customers only, never scripted.

**The highest-leverage single habit:** post every published post's strongest claim to LinkedIn, verbatim, from Reyhan's profile. LinkedIn is the most-cited source in our category that we fully control.

---

## 5. How we QC a post (the Wave Review)

Every draft clears **Gate 0 + 5 lenses** before it reaches Reyhan:
- **Gate 0 — Retrieval:** can AI crawl + read it (Section 3 crawlability). Fail here = stop.
- **Lens 1 — Extraction:** the first-50-words test, question H2s, FAQ + schema.
- **Lens 2 — Passage engineering:** the lift test; single-subject paragraphs; does it cover the query's variants.
- **Lens 3 — Citation-magnet format:** listicle/comparison where the SERP allows; explicit verdict labels; freshness date logged. (No self-promotional listicle gaming.)
- **Lens 4 — Trust & evidence:** named sources; author byline + credibility line; entity consistency; one first-hand number; recommendation-phrased proof exists (or the distribution note says where to earn it).
- **Lens 5 — Commercial path:** which buying stage does it serve; who-it's-for / trade-offs / alternatives / cost / proof; CTA + links.

Two automated QC gates also run on every article: an editorial score (must be ≥90/100) and an SEO checklist (must be 100%). Both must pass before Reyhan sees it.

---

## 6. Operating rhythm

**Weekly** (channel: `#recruitergtm-seo`):

| Day | Who | What |
|-----|-----|------|
| Mon — Plan | Claude | Pick 1–2 posts (service-answerable buying prompts first), write a brief each |
| Tue–Wed — Write | Noroze | Draft from the brief only (no brief = no post); one original stat each |
| Thu — Review | Claude → Noroze | Wave Review + QC gates; Noroze applies fixes same day |
| Fri — Publish + distribute | Claude → Noroze/Reyhan | Claude builds/deploys (schema, links, IndexNow); Noroze produces the distribution kit; Reyhan posts LinkedIn |

**Weekly off-page (Noroze, ongoing):** 2 earn-mention pitches · Reddit monitoring + genuine answers · the LinkedIn claim post · one entity fix.

**Monthly (1st):** two automated runs — one refreshes these rules from tracked SEO experts, one produces the AI-visibility scorecard (citations per engine + who's cited for our prompts + entity gaps). Reyhan does a 20-min manual check of ChatGPT + Google AI answers.

---

## 7. Who owns what

- **Reyhan:** approves posts + flagged stats; posts to LinkedIn; earned media through his relationships (partner blogs, podcasts); films YouTube.
- **Noroze:** writing; the entire off-page engine (entity build, outreach, reviews, Reddit); weekly distribution kit.
- **Daniyal:** the technical layer — schema, crawlability, site build/deploy, IndexNow, Organization-schema enrichment, GSC/analytics plumbing.
- **Claude:** Monday briefs; Thursday reviews; Friday build/publish; monthly measurement; keeping this Playbook current.

---

*This Playbook is a living document — it's refreshed monthly from performance data and new AI-search research. If something here is contradicted by our own citation data, the data wins.*
