# Blog Post SOP — Every Post, Every Client

The single checklist for taking one post from idea to tracked asset. Work top to bottom; do not skip phases. Rule tags (C12, B6, KI 2026 …) point to `SKILL.md` Locked Rules and their sources.

---

## Phase 1 — Brief (nothing gets written without this)

- [ ] 1.1 **Refresh-first check (A6):** search `content-register.md` + the live site for an existing post on this topic. If one exists → run the refresh workflow instead of writing new (+106% avg traffic from refreshing, NP 2026).
- [ ] 1.2 **Read the client config** `clients/[client-id].md` — voice, CMS, pillars, CTA (A5).
- [ ] 1.3 **Keyword validation (B1, B4, B6):** target query, volume, KD (≤40 for domains under DR 25), intent, whether an AI Overview already owns the SERP.
- [ ] 1.4 **Conversational variants (B7):** write 2-3 question/prompt phrasings of the target query.
- [ ] 1.5 **SERP scan (B2, B3):** top 3 competitors — URL, format, word count, angle. Note dominant format and word-count median.
- [ ] 1.6 **Content gap:** what does nobody on page 1 cover that we can, with first-hand data?
- [ ] 1.7 **Define the packet:** the ONE citable stat (first-hand number/client result) this topic owns, planned LinkedIn angle(s), YouTube video yes/no.
- [ ] 1.8 **Fill the brief** from `templates/content-brief.md` → save as `templates/briefs/[client]-[slug].md`.
- [ ] 1.9 **Register the post** in `content-register.md` NOW, status `brief ready` (A3).

## Phase 2 — Write

- [ ] 2.1 **Answer first:** standalone 40-60 word direct answer in the opening (C1) — must make sense lifted out alone.
- [ ] 2.2 **H2s as questions** users actually ask; first sentence under each H2 answers it in 40-60 words (C2, C8).
- [ ] 2.3 **Lift test every section (C12):** pulled out alone, each passage carries entity + context + claim. One subject per paragraph.
- [ ] 2.4 **Single-URL completeness (C13):** post answers what it is / who it's for / how to choose / what it costs in this one URL.
- [ ] 2.5 **Format matches the SERP (B2):** listicles/comparisons wherever page 1 allows (59.5% of AI-cited URLs are listicles, KI 2026). Comparison tables get verdict labels ("Best for X") + stated criteria (C10). No self-promotional listicle gaming (Google targets it since Dec 2025).
- [ ] 2.6 **Evidence:** 1 stat per 150-200 words, every stat with a NAMED source (C3); at least one first-hand number competitors would have to cite us for (C9); our own data states its methodology.
- [ ] 2.7 **FAQ section:** 3-5 real questions (G3).
- [ ] 2.8 **Word count** ≥ SERP median within 10% (B3), never under 600 (G1).
- [ ] 2.9 **Voice pass (E, section G):** practitioner tone, British English, no AI vocabulary, ≤1 em dash, every sentence niche-specific, primary keyword 3-5 times max.
- [ ] 2.10 **Links + CTA:** 1 pillar + 2 spoke internal links (D2), CTA at end (D3), affiliate URL for every tool named (G6).

## Phase 3 — Review (Wave Review Framework in `SKILL.md`)

- [ ] 3.1 **Gate 0** (once per wave): robots.txt allows GPTBot / ChatGPT-User / PerplexityBot / Claude-Web; critical content server-rendered; no load-bearing images/PDFs.
- [ ] 3.2 **Run the 5 lenses:** Extraction · Passage engineering · Citation-magnet format · Trust & evidence · Commercial path (every wave includes BOFU posts, never all-TOFU).
- [ ] 3.3 **Facts preflight:** every stat, tool, price, and claim about us checked against context files. No revenue promises. Correct entity.
- [ ] 3.4 **Verdict:** Publish / Fix-then-publish (numbered list to writer) / Re-aim (fix the brief, not the prose).

## Phase 4 — Technical pre-publish

- [ ] 4.1 H1 contains primary keyword exactly once (D1).
- [ ] 4.2 Metadata: title ≤60 chars, description ≤155, canonical URL, OG image (D5).
- [ ] 4.3 JSON-LD: BlogPosting + FAQPage (+ VideoObject if the post embeds a video) — validate at https://validator.schema.org (D4).
- [ ] 4.4 Visible publish date AND dateModified (C14).
- [ ] 4.5 Author byline + one-line credibility statement (E-E-A-T said plainly).

## Phase 5 — Publish

- [ ] 5.1 Deploy per client config (RecruiterGTM: `vercel deploy --prod`).
- [ ] 5.2 Sitemap updated (F1).
- [ ] 5.3 IndexNow ping with the new URL (F2 — command in `SKILL.md`).
- [ ] 5.4 Manual index request in GSC (F3).
- [ ] 5.5 Register: status `published`, publish date, word count.

## Phase 6 — Packet distribution (within 7 days of publish)

84-93% of AI citation weight comes from third-party sites (AS 2026) — the post is not done until it exists off-domain.

- [ ] 6.1 **LinkedIn post(s)** carrying the packet's citable stat, phrased identically to the blog (C11). Blog link in first comment. (Write via content-os skill.)
- [ ] 6.2 **YouTube** (if the topic has/gets a video): embed the video in the post + paste the transcript on the page; video description links to the blog URL in line 1; video title uses the same question phrasing.
- [ ] 6.3 **Newsletter mention** in the next Beehiiv issue (via newsletter-writer skill).
- [ ] 6.4 Register: fill the LinkedIn and YouTube URL columns.

## Phase 7 — Track & refresh (ongoing)

- [ ] 7.1 GSC position at 14 / 30 / 60 / 90 days → register (F4).
- [ ] 7.2 Monthly metrics run (`/seo-engine metrics`): Perplexity citation check (automated) + ChatGPT / AI Overviews screenshot check (Reyhan) — never fabricate a result (M1).
- [ ] 7.3 **30-day freshness touch (C14):** every post gets a scheduled update within 30 days of publish (3.2x citations, KI 2026), then joins the quarterly refresh cycle (A4).
- [ ] 7.4 Uncited in ALL engines for 2 consecutive months → refresh queue automatically (M3). Track which competitors ARE cited for our queries (M4) — that's the gap brief for the refresh.
