# SEO Engine Skill

Plan, write, publish, and optimise SEO content for RecruiterGTM and retainer clients (currently April Ben-Sabat / IC&A). Multi-tenant.

**Core mission:** get our content cited by AI engines (ChatGPT, Perplexity, Claude, Google AI Overviews / AI Mode) — that is the PRIMARY target — while also ranking in classic Google. One discipline, not two. We don't use the term "AEO"; AI-engine citation is just what modern SEO is. When a formatting or structure decision trades off between classic SERP convention and AI-extraction friendliness, AI extraction wins.

**This skill is a living system.** It gets constantly improved via the Continuous Improvement Loop (bottom of this file) — new research, GSC/citation data, and algorithm/AI-search changes feed back into the Locked Rules. Never treat the current rules as final.

---

## How to Invoke

- `/seo-engine brief [client] [keyword]` → generate a content brief from SERP research
- `/seo-engine write [brief-file]` → write the post from a completed brief
- `/seo-engine gsc-wins [client]` → list "almost-ranking" queries (positions 8-20) to upgrade
- `/seo-engine refresh [client] [slug]` → quarterly refresh of an existing post
- `/seo-engine publish [client] [slug]` → run pre-publish checklist + deploy + IndexNow ping
- `/seo-engine register [client]` → show current state of the content register
- `/seo-engine improve` → run the Continuous Improvement Loop: research sweep + performance review → proposed rule changes
- `/seo-engine metrics [client]` → monthly hybrid metrics run: automated Perplexity citation checks + screenshot-assisted ChatGPT/AI Overviews checks + GSC/GA4 → scorecard

**Always read `clients/[client-id].md` FIRST** before any work. Voice, pillars, CMS, deploy method, ICP all live in the client config.

**The per-post checklist is `post-sop.md`** — 7 phases, brief → write → review → technical → publish → packet distribution → track/refresh. Every post follows it top to bottom; it is the operational expansion of the Locked Rules below.

**The glossary is `glossary.md`** — plain-English definitions of every SEO term used in this Playbook (DR, KD, TP, CTR, CPC, backlinks, indexing, schema, AI citation, etc.), each with a RecruiterGTM-specific use case, plus the RecruiterGTM Backlink Guide (how we build links at DR 0.1). Read it first if the terminology is new; keep it current as new terms enter the workflow.

**The competitor + backlink research is `competitor-and-backlink-research.md`** — live-Ahrefs analysis of RecruiterGTM's competitors (business vs search fronts), the winnable keyword landscape, and the backlink-potential map across Reyhan's real relationships (Clay/Instantly/HeyReach DR 71-79, Benjamin Mena/Mark Whitby DR 27-30) + the LinkedIn factor. Read before any competitor-positioning, keyword-priority, or link-building decision. Refresh quarterly.

**The RecruiterGTM Keywords Bank is `keywords-bank.md`** — the master target list for the informational engine (recruitergtm.com), every term a live-Ahrefs winnable (KD ≤ ~10) ICP-relevant keyword, organised by the 4 pillars, tiered by priority, mapped to existing-vs-new pages, with a recommended first-10-post build order. The Monday plan draws from here. Commercial "best ATS/CRM/tool" terms are reserved for the (not-yet-built) Pulse Recruit bank.

**The SEO model to copy is `seo-model-and-inspiration.md`** — who already wins recruitment-niche organic search (Recruiterflow DR 76 / 28k visits, Happlicant, Pin, Leonar, Manatal, etc.) and the replicable product-led template (best-for / alternatives / vs / pricing / free-tool pages that rank with ~no backlinks). Defines the three-engine model and the multi-site architecture: informational authority on recruitergtm.com + the tool-SEO template on Pulse Recruit, interlinked. Read before building any commercial/comparison page or the Keywords Bank.

---

## Locked Rules

### A. Process

A1. Never write a post without a completed brief in `templates/briefs/[client]-[slug].md` first. No brief = no post.
A2. Never publish without running the pre-publish checklist (Section: Workflow → Step 3).
A3. Every post is logged in `content-register.md` the moment a brief is started — not after publish.
A4. Posts older than 90 days get reviewed for stat refresh + position check.
A5. Read the client config (`clients/[client-id].md`) before every task. Each client has different voice, CMS, deploy.
A6. Refresh beats net-new: before greenlighting a new post, check whether an existing page covers the topic and upgrade it instead (updating old content averages +106% organic traffic; ~90% of marketers find it more effective than new posts — NP 2026). Every refresh must add original perspective, never a re-hash.

### B. Keyword & SERP

B1. Brief MUST include: target query, search volume, KD, intent, top 3 SERP competitors, dominant format, content gap, word-count target.
B2. Match the dominant SERP format. If page 1 is listicles, write a listicle. If page 1 is comparison tables, lead with a table.
B3. Word count ≥ median of top 5 SERP results (within 10%). Going significantly shorter loses; going 3x longer wastes effort.
B4. Never target KD > 40 on a domain under DR 25. Pick winnable battles. Use long-tail until DA catches up.
B5. Search intent first. A "best X" query is commercial, not informational — the post structure is different.
B6. Never judge a keyword on volume alone (94.7% of keywords get ≤10 searches/month — NP 2026). Weigh intent + our topical authority + whether an AI Overview already owns the SERP.
B7. Every brief lists 2-3 conversational/question phrasings of the target query ("How do I…", full-sentence prompts). AI search runs on natural language, not compressed keyword strings.

### C. AI Search Citation (part of SEO — never call it "AEO")

C1. First paragraph = 40-60 word direct answer to the query. This is what AI engines extract.
C2. Every H2 leads with a 40-60 word answer before expanding.
C3. One citable stat per 150-200 words with source link/attribution.
C4. FAQ section (3-5 Qs) + FAQPage schema on every post.
C5. Tables over paragraphs for comparisons. AI parses tables cleanly.
C6. No fluff intros. Never write "In this article we will explore..." — AI skips it, humans bounce.
C7. Semantic chunking: bullets, numbered lists, short paragraphs. AI engines extract these.
C8. Frame H2s as conversational questions where natural ("How do recruiters automate sourcing?") — matches how people prompt AI engines (NP 2026).
C9. Original data is the citation magnet: every post carries at least one first-hand number, client result, or tested verdict competitors would have to cite us for. AI engines cite source material, not summaries.
C10. Comparison posts give explicit verdicts ("Best for solo agencies", "Best budget option") with stated evaluation criteria — the format LLMs lift into answers.
C11. Brand entity consistency: describe the client with the same one-liner and terminology everywhere (site, LinkedIn, guest posts, directories). LLMs learn entities from cross-platform consistency.
C12. Self-contained passages: every section must survive the "lift test" — pulled out alone, it still carries the entity, the context, and the claim. Single subject per paragraph; split multi-topic paragraphs. (MK 2026 — retrieval happens at passage level, not page level.)
C13. Single-URL completeness: a post answers "what is it / who's it for / how to choose / what it costs" in ONE URL — top-cited URLs do all four. (KI 2026)
C14. Freshness is a citation factor, not a nicety: content updated within 30 days earns ~3.2x more AI citations; visible dateModified required. (KI 2026)
C15. Review & recommendation-signal engineering: actively shape third-party review/testimonial language (G2, Capterra, Skool, Trustpilot, LinkedIn recommendations) so it reads as a SPECIFIC recommendation ("best for solo recruitment agencies") not generic praise — LLMs weight recommendation-phrased reviews as citation/ranking signals, not just on-page tweaks. Give reviewers a light prompt: use case + who it's for + outcome. Off-page recommendation language is a citation lever the page itself can't provide. (Reddit AEO-agency thread 2026-08-14 — Marina/Edge Studio; comment 3 earned-media signals)
C16. Citation-source targeting (makes C9/AS operational): each metrics cycle, pull the SPECIFIC third-party domains/pages AI actually cites for our category's key prompts (Ahrefs Brand Radar cited-domains/pages + manual prompt checks) into a Citation Source Target list, then deliberately earn presence there (guest post, listing, directory, mention, review). Distribution stops being generic "post to LinkedIn" and becomes "get into the exact sources the models pull from for our category." (Reddit thread 2026-08-14 — Marina point 2; AS 84-93% external)
C17. Entity / knowledge-graph building (beyond C11 consistency): Organization schema carries `sameAs` to every owned profile, and we pursue structured-knowledge presence (Wikidata, Crunchbase, relevant industry directories) so engines resolve the brand as a KNOWN entity, not just a string. Entity resolution is what lets an LLM attribute a claim to us. (Reddit thread 2026-08-14 — comment 2 entity & semantic SEO)

### D. Structure

D1. H1 contains primary keyword. Exactly one H1 per page.
D2. Internal links: 1 pillar page + 2 spoke posts minimum.
D3. CTA at end of every post — book a call, join community, or lead magnet.
D4. JSON-LD: BlogPosting + FAQPage on every blog post. Service / Course schema for service pages.
D5. Metadata: title (≤60 chars), description (≤155 chars), canonical URL, OpenGraph tags.

### E. Voice

E1. Practitioner voice, not consultant. Write like the brand owner has done the work.
E2. Real numbers, real client names (with permission), real timelines.
E3. British / neutral English.
E4. No AI vocabulary: leverage, delve, crucial, pivotal, landscape, navigate, robust, seamless, ecosystem.
E5. Max 1 em dash per post (per `feedback_em_dashes.md`).
E6. Industry-specific. Every sentence must be specific to the client's niche — if it could apply to "any business," rewrite it.
E7. Match client voice file in `clients/[client-id].md`. RecruiterGTM ≠ April voice.

### F. Publishing

F1. Update sitemap on publish (or client CMS equivalent).
F2. Run IndexNow ping immediately after deploy.
F3. Manually request indexing in GSC for high-priority pages.
F4. Update `content-register.md` with publish date + initial GSC position (re-check at 14, 30, 60, 90 days).
F5. Measure AI visibility, not just rank: at the 30/60/90-day checks, also spot-check whether the brand/post gets cited in ChatGPT + Perplexity for the target query, and watch branded search volume trend in GSC. Citation in AI answers now matters more than position #1 (NP 2026: AI Overviews hit 30-47% of US desktop searches and cut top-position CTR ~58%).

### G. Anti-patterns

G1. Never publish under 600 words.
G2. Never keyword-stuff. Primary keyword 3-5 times max, naturally placed.
G3. Never skip the FAQ section — it's the single biggest lever for AI-engine citations.
G4. Never copy competitor content. Original data, original framing.
G5. Pillar guides never appear in the site header nav (RecruiterGTM rule).
G6. Never recommend a tool without using the affiliate URL (per `feedback_always_use_affiliate_links.md`).

---

## Multi-Tenant Architecture

This skill runs for multiple clients. Each has a config file at `clients/[client-id].md` containing:

- Domain + CMS + deploy method
- Voice notes (with sample posts)
- Niche / ICP / buyer persona
- Pillar pages (hub & spoke topics)
- GSC + GA access status
- Target keywords (validated, not assumed)
- Brand guidelines (logo, colours, CTA links)

**Current clients:**

| Client | Config | Cadence | Stack |
|--------|--------|---------|-------|
| recruitergtm | [clients/recruitergtm.md](clients/recruitergtm.md) | As needed | Next.js 16 + Vercel CLI |
| april-ben-sabat | [clients/april-ben-sabat.md](clients/april-ben-sabat.md) | 5 posts/month | TBD (intake pending) |

---

## Workflow

### Step 1 — Brief (every post starts here)

Use the template at `templates/content-brief.md`. Save the completed brief to `templates/briefs/[client]-[slug].md` BEFORE writing. The brief is non-negotiable — it's where ranking is decided.

Brief must include:
- Target query + 3-5 secondary keywords
- Search volume + KD (from Ahrefs/SEMrush/keyword tool)
- Intent (informational / commercial / transactional)
- Top 3 SERP competitors (URL + word count + format + angle)
- Content gap we're filling (what nobody on page 1 covers)
- Word-count target (SERP median ±10%)
- Format (listicle / guide / comparison / case study / contrarian)
- Pillar page link + 2 spoke internal links
- Primary CTA
- 3-5 stats with sources

### Step 2 — Write

Follow Locked Rules (Voice, Structure, AI Search Citation). Match brief format. Hit word-count target.

### Step 3 — Pre-publish Checklist

Before deploy, verify every box:

- [ ] H1 contains primary keyword (exactly once)
- [ ] Answer paragraph 40-60 words at top
- [ ] Every H2 leads with 40-60 word answer
- [ ] FAQ section: 3-5 Qs + FAQPage schema
- [ ] Internal links: 1 pillar + 2 spokes minimum
- [ ] Word count ≥ SERP median (within 10%)
- [ ] Stats: 1 per 150-200 words + sources cited
- [ ] JSON-LD: BlogPosting + FAQPage validated (use https://validator.schema.org)
- [ ] Metadata: title ≤60ch, desc ≤155ch, canonical, OG image
- [ ] CTA present + affiliate URLs for any tool mentioned
- [ ] Voice check: no AI vocabulary, ≤1 em dash, practitioner tone

### Step 4 — Publish

Run the publish command from the client config. RecruiterGTM:
```bash
cd [project dir] && vercel deploy --prod
```
Other clients: see their config file.

### Step 5 — IndexNow Ping

After deploy (RecruiterGTM):
```bash
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "recruitergtm.com",
    "key": "23383546a937c61170b825616560e5e8",
    "keyLocation": "https://recruitergtm.com/23383546a937c61170b825616560e5e8.txt",
    "urlList": ["https://recruitergtm.com/blog/NEW-SLUG-HERE"]
  }'
```
For April + future clients: provision IndexNow key during onboarding, store in client config.

### Step 6 — Update Register

Append the post to `content-register.md` with: client, slug, target keyword, publish date, word count, pillar link. Re-check GSC position at 14, 30, 60, 90 days.

---

## GSC Wins Workflow

The single highest-ROI move on any site with existing content: find queries ranking position 8-20 and upgrade those pages.

Process:
1. Pull GSC Performance report (last 28 days, all queries).
2. Filter: position 8-20, impressions ≥ 100, CTR < 2%.
3. For each query, check the ranking URL on our site.
4. Open the page. Audit against current SERP top 3.
5. Identify the gap: word count, missing H2, weak intro, no FAQ, stale stats, format mismatch.
6. Upgrade the page (don't write a new one). Re-deploy. IndexNow ping.
7. Re-check position in 14 and 28 days.

Run this monthly on any client with 10+ ranking pages.

---

## Weekly Operating Rhythm (locked 2026-08-07)

The recurring week-by-week system for running SEO. Channel: Slack `#recruitergtm-seo`. Writer: Noroze. Review + publish: Claude. Approvals: Reyhan. All days UK time.

| Day | Who | What |
|-----|-----|------|
| **Monday — Plan** | Claude | Pick the week's posts (backlog + refresh queue + April cadence once live). Produce a BRIEF per post (SERP scan, keyword validation, packet definition: the one citable stat + LinkedIn angle + YouTube yes/no). Post briefs in the channel by EOD. |
| **Tue-Wed — Write** | Noroze | Write from the brief only (no brief = no post), following `post-sop.md` phases 1-2. Self-check against the phase checklists. Drop one Google Doc link per post in the channel by Wednesday EOD. |
| **Thursday — Review** | Claude → Noroze | Same-day review against the Wave Review Framework. Verdict + numbered fix list posted in-thread. Noroze applies fixes same day. Any number not on the verified stats list (in `context/me.md`) gets flagged to Reyhan in the thread — never published unverified. |
| **Friday — Publish + distribute** | Claude → Noroze/Reyhan | Claude builds approved posts on the site (schema, links, metadata), deploys, IndexNow pings, updates the register, and produces the distribution kit (LinkedIn article/post + YouTube description, corrected + ready to paste). Noroze schedules LinkedIn for Tuesday 8am UK; video goes into the YouTube pipeline. Reyhan: manual GSC index request (2 min). |
| **Monthly (1st)** | Automated + Reyhan | `seo-engine-improve` routine (rule updates from the expert panel) + `/seo-engine metrics` run (Perplexity citations automated; Reyhan's ChatGPT/AI Overviews screenshot pass). Output: scorecard + "upgrade next" list → becomes next Monday's refresh items. |

**Standing rules of the rhythm:**
- W1. Default volume: 1-2 new RecruiterGTM posts/week + refresh items; April at 5/month once her intake lands. Every published post re-enters the Monday plan at its 30-day touch date (C14).
- W2. A post's status is one of: Brief → Writing → In Review → Fixes → Published → Distributed. It is not "done" until Distributed (packet live off-domain, per Phase 6).
- W3. Noroze never invents a number. The verified stats list lives in `context/me.md` (Key Stats). Anything else → ask Reyhan in the thread first.
- W4. Reyhan's only recurring jobs: verify flagged numbers, GSC index requests, film videos, post to his LinkedIn. Everything else runs without him.
- W5. If Pulse gets a blog pipeline (Daniyal build), statuses mirror W2 and the monthly "upgrade next" list lands as Pulse tasks with due dates.
- W6. All drafts live in the shared Drive folder **"Website Content + SEO"** (https://drive.google.com/drive/folders/1Ur22oZudc8vw3syRhzJ3PP-12XVqy7VU · local: `My Drive/RecruiterGTM/Content/Website Content + SEO/`) — one folder per topic packet (`[client]/YYYY-MM <topic-slug>/`) containing separate docs named `Blog — <title>`, `LI Article — <title>`, `YT — <title>`. Briefs in `[client]/_briefs/`. See the README in that folder. Claude pulls drafts from here; Noroze puts everything here — no personal drives. When Daniyal's Pulse organic-content tracker is live (topic entry with Blog/LI/YT statuses per topic), tracking moves to Pulse and each Drive folder maps to one Pulse topic; Drive stays the document store.

---

## Metrics Workflow (`/seo-engine metrics [client]`)

Monthly per-client scorecard. Hybrid by design: engines with an API are automated; ChatGPT and Google AI Overviews are checked by Reyhan with a screenshot protocol (no clean API exists — Reyhan approved this split 2026-08-04). Run on the 1st of each month, same day as the improvement sweep.

### Step 1 — Build the query list
Pull every published post's target query from `content-register.md` + the pillar page keywords. Cap at ~15 queries per client per run (Perplexity cost + Reyhan's manual time). **Purchase-intent audit (required):** the list MUST include explicit BOFU buying prompts, not only informational queries — e.g. "best recruitment GTM system", "X vs Y for agencies", "is [category] worth it for a small recruitment agency". These are the prompts that sit in closed-won paths; their month-over-month movement IS the visibility-score we report. (Reddit thread 2026-08-14 — Marina point 3.)

### Step 2 — Automated: Perplexity citations
```bash
python3 .claude/skills/seo-engine/metrics/check_citations.py \
  --domain [client-domain] --queries-file [tmp queries file]
```
Records per query: cited yes/no + which URLs. Uses `PERPLEXITY_API_KEY` from `.env` (sonar model, ~cents per run).

### Step 2b — Automated: AI citation counts across ALL engines (Ahrefs Brand Radar) — added 2026-08-13
The fastest, no-screenshot way to measure AI-engine citations. Ahrefs' `mcp__ahrefs__site-explorer-ai-responses-count` returns citation counts + distinct cited pages **per engine (ChatGPT, Perplexity, Gemini, Copilot, Grok, Google AI Overviews)** for any domain — ours AND competitors'.

Run per client + top 2-3 competitors each metrics cycle:
`select: chatgpt,perplexity,gemini,copilot,grok,google_ai_overviews`, `mode: subdomains`, current date. Record the per-engine citation + page counts in the scorecard; this is the domain-level AI-citation scoreboard, automated. Use the manual screenshot pass (Step 3) ONLY for the query-level qualitative detail Ahrefs can't give (which competitor is cited *instead* for a specific target query, exact answer wording).

**Baseline (2026-08-12):** RecruiterGTM ≈ 0 citations (ChatGPT 0 / Perplexity 0 / Gemini 0 / AIO 0 / Copilot 2 across 1 page). Automindz (closest content competitor) ≈ 8 total, all near-zero. Reference target: hikmahaiagency.com — a tiny AEO-first agency (DR 3.5, 0 Google traffic) — sits at ~98 citations from ~11 well-structured pages. Lesson: **citation-optimized page structure beats volume.** Grow RecruiterGTM's number every cycle; this is now the headline success metric (per F5).

### Step 2c — Brand-description capture + answer-intent map (added 2026-08-14)
Citation yes/no is not enough — good agencies track HOW the brand is described and where the category conversation actually lives. Two artifacts, maintained each cycle:
1. **Brand-description log:** for the top prompts (esp. the purchase-intent ones), record not just cited y/n but the exact words each engine uses to describe us, and any mischaracterisation (wrong service, wrong ICP, stale claim). A wrong description is a content/entity fix (C11/C17), not a citation loss to shrug off.
2. **Answer-intent map:** a living table of the category's key prompts × each engine's current answer × who's cited instead. This is the map that tells us which prompts to target next and which Citation Source Targets (C16) to earn presence on. Store at `metrics/[client]/answer-intent-map.md`; update, don't rewrite.
(Reddit thread 2026-08-14 — Marina point 1.)

### Step 3 — Manual-assist: ChatGPT + Google AI Overviews
1. Print the numbered query list and tell Reyhan: "Run each of these in ChatGPT (web search on) and in Google. Screenshot each answer (screenshots land in `~/Desktop/Screenshots`), or copy-paste the answer text back here. Say done when finished."
2. WAIT for Reyhan. Never fabricate or infer a result for these engines.
3. When he says done, Read the newest screenshots from `~/Desktop/Screenshots` (or parse pasted text), and record per query: brand/domain cited yes/no, which competitor was cited instead.
4. Any query he skips is logged as `not checked` — never as a no.

### Step 4 — GSC + GA4
- If Google service-account credentials exist in `.env` (`GOOGLE_APPLICATION_CREDENTIALS`): pull positions/impressions/CTR + branded-search trend (GSC) and the AI-referral segment — sessions from chatgpt.com, perplexity.ai, claude.ai, gemini referrers (GA4).
- Until then: ask Reyhan for the headline GA numbers or mark the section `pending API setup`.

### Step 5 — Scorecard + register update
Write `metrics/[client]/YYYY-MM.md`: table of query × engine (Perplexity / ChatGPT / AI Overviews / classic rank) with month-over-month movement, the AI-referral + branded-search numbers, and a ranked "upgrade next" list (posts not cited anywhere = first candidates for the refresh workflow). Update `content-register.md` positions. Post the headline summary in chat (or Slack DM if run headless).

### Locked rules for this workflow
- M1. Never fabricate a citation result. Unchecked = `not checked`.
- M2. Screenshot protocol only for ChatGPT + AI Overviews; everything with an API stays automated.
- M3. A post uncited in ALL engines for 2 consecutive months auto-joins the refresh queue (Rule A6).
- M4. Track competitor domains that get cited for our queries — they reveal the format/content gap to close.

---

## Wave Review Framework (`/seo-engine review [drafts]`)

Panel-derived review for draft posts, built 2026-08-05 from the tracked experts' published methodologies (sources in Improvement Log). Review every post through Gate 0 + 5 lenses; each lens is attributed to the coach whose research defines it.

### Gate 0 — Retrieval (Lily Ray + Jose Velez) — site-level, once per wave
- robots.txt allows GPTBot, ChatGPT-User, PerplexityBot, Claude-Web
- Critical content server-rendered; nothing load-bearing hidden in images/PDFs/forms
- Fail here = nothing else matters; AI can't cite what it can't read.

### Lens 1 — Extraction (Velez + Patel): the first-50-words test
- Direct standalone answer in the first 40-60 words (the extraction window)
- Every H2 phrased as the question users ask; first sentence under it answers it
- FAQ section + FAQPage schema

### Lens 2 — Passage engineering (Mike King): the lift test
- Run C12 on every section: lifted alone, does it carry entity + context + claim?
- Single-subject paragraphs; clean heading hierarchy
- Query fan-out coverage: does the post handle the related, comparative, and reformulated variants of the target query (an AI engine runs all of them, not just the head term)

### Lens 3 — Citation-magnet format (Kevin Indig + Patel)
- Listicle/comparison format wherever the SERP allows — 59.5% of all AI-cited URLs are listicles (KI)
- Comparison tables carry explicit verdict labels ("Best for solo agencies") with stated criteria
- C13 single-URL completeness check
- Refresh date logged at review time; post enters the 30-day touch cycle (C14). Do NOT game listicles with self-promotion — Google actively targets self-promotional listicle patterns since Dec 2025 (LR).

### Lens 4 — Trust & evidence (Aleyda Solis + Lily Ray)
- Every stat has a NAMED source; our own data states its methodology
- Author byline + one-line credibility statement (E-E-A-T said plainly, not implied)
- Entity consistency with the rest of the site (C11); entity resolvable off-site via sameAs / knowledge-graph presence (C17)
- At least one first-hand number/result competitors would have to cite us for (C9)
- Recommendation-signal check (C15): is there recommendation-phrased third-party proof for this topic ("best for solo recruitment agencies"), not just decorative testimonials? If none exists, the wave's distribution note names where to earn it (C16)

### Lens 5 — Commercial path (Jose Velez): the closed-won test
- Which buying-journey stage does this post serve? BOFU pages that appear in closed-won paths get citation priority in Velez's system — every wave needs some, never all-TOFU
- Decision-support completeness (AS): who it's best for, trade-offs, alternatives, cost, proof
- CTA + 1 pillar + 2 spoke links

### Wave-level output (not per post)
- Verdict per post: **Publish** / **Fix-then-publish** (numbered list back to writer) / **Re-aim** (brief was wrong)
- Distribution note per post: 84-93% of AI citation weight comes from THIRD-PARTY sites (AS) — so the review lists where each post's core insight should also live (LinkedIn, guest posts, newsletter). On-page perfection alone does not win citations.
- House layer still wraps everything: facts preflight, voice rules (section E), affiliate links, anti-patterns (section G).

---

## Content Brief Template

Lives at [templates/content-brief.md](templates/content-brief.md). Copy and fill before writing.

---

## Schema Templates

### BlogPosting (every post)
```typescript
const jsonLd = {
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  headline: "[Title]",
  description: "[Description]",
  author: { "@type": "Person", name: "[Author]", url: "[Author URL]" },
  publisher: { "@type": "Organization", name: "[Brand]" },
  datePublished: "[YYYY-MM-DD]",
  dateModified: "[YYYY-MM-DD]",
  url: "[Full URL]"
};
```

### FAQPage (every post with FAQ)
```typescript
const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: [
    {
      "@type": "Question",
      name: "[Question]",
      acceptedAnswer: { "@type": "Answer", text: "[Answer ≤200 words]" }
    }
  ]
};
```

### Organization (site-wide, in layout)
Already deployed to recruitergtm.com. Provision per-client on onboarding.

---

## RecruiterGTM — Pillar Pages (Hub & Spoke)

Built around the 4-pillar framework. Educational guides, NOT service pages. Do NOT appear in header nav.

| Pillar | URL | Target Keyword | Schema |
|--------|-----|---------------|--------|
| OutboundOS | `/outbound-guide` | outbound recruitment strategy | BlogPosting + FAQPage |
| SourcingOS | `/sourcing-guide` | candidate sourcing automation | BlogPosting + FAQPage |
| ContentOS | `/content-guide` | LinkedIn for recruiters | BlogPosting + FAQPage |
| OperatorOS | `/operations-guide` | recruitment agency management system | BlogPosting + FAQPage |

Each pillar has CTA buttons at bottom (Book a Call + See [Service]). Pillar guides target 2,000+ words — cornerstone content at that depth performs ~1.86x better (NP 2026); spokes follow the normal SERP-median rule (B3).

---

## RecruiterGTM — Infrastructure (as of 2026-04-16)

- Blog index at `/blog`, posts at `/blog/[slug]`
- OG image at `/public/og-image.png` (1200x630)
- Organization JSON-LD in `app/layout.tsx`
- All 18 pages have: canonical URL, page-specific OG, JSON-LD
- GSC: Verified domain property. Sitemap submitted.
- IndexNow key deployed: `/public/23383546a937c61170b825616560e5e8.txt`
- Bing Webmaster Tools: pending import from GSC
- robots.txt: all crawlers allowed (GPTBot, ClaudeBot, PerplexityBot, Google-Extended)

---

## RecruiterGTM — Blog Backlog (1 LIVE, 9 REMAINING)

**Published:**
| # | Title | URL | Pillar |
|---|-------|-----|--------|
| 1 | How Patrick Hit 2M LinkedIn Impressions in 90 Days | `/blog/how-patrick-hit-2m-linkedin-impressions-90-days` | ContentOS |

**Backlog (priority order):**
| # | Title | Target Keyword | Type | Pillar |
|---|-------|---------------|------|--------|
| 2 | 5 Recruitment Automation Mistakes Costing You $500k/Year | recruitment automation | Problem-solution | /outbound-guide |
| 3 | The Sourcing Automation Playbook: 30-50 Candidate Conversations/Month | sourcing automation | Playbook | /sourcing-guide |
| 4 | How to Scale a Recruitment Agency to $100k MRR Without Hiring 5 More People | scale recruitment agency | Guide | /operations-guide |
| 5 | Clay vs Lemlist vs HeyReach: Which Outbound Stack for Your Agency | recruitment outbound tools | Comparison | /outbound-guide |
| 6 | Why Volume Sourcing Is Dead: The Qualified Enrichment Framework | AI sourcing recruiters | Contrarian | /sourcing-guide |
| 7 | Building a Remote Recruitment Team: 48-Hour GTM Engineer Placement | remote recruitment team | Case study | /operations-guide |
| 8 | Recruitment CRM for Agencies: 7 Setup Mistakes That Waste 10 Hours/Week | recruitment CRM agencies | Listicle | /operations-guide |
| 9 | The Recruitment Content Flywheel: Generate Inbound Clients Via LinkedIn | recruitment lead generation | Framework | /content-guide |
| 10 | AI Twins for Recruiters: Why Your LinkedIn Bot Isn't Working | AI for recruiters | Contrarian | /outbound-guide |

Each of these needs a brief before writing. Old keyword clusters in earlier versions of this skill are NOT validated SERP data — re-research each before brief.

---

## Continuous Improvement Loop

This skill must get better every month. Run `/seo-engine improve` monthly (or whenever Reyhan shares new SEO/AI-search material). The loop:

### 1. Research sweep (external)
Check each tracked source for what's NEW since the last Improvement Log entry:

**Tracked experts (the monthly watch list):**
| Who | Where | Angle |
|-----|-------|-------|
| Neil Patel / NP Digital | neilpatel.com/blog + LinkedIn | Broad data studies, AI-search traffic numbers |
| Jose Velez — Reach AI | linkedin.com/in/zevelez + reach.ai | GEO for B2B SaaS — #1 AI-citation case studies, BOFU-for-AI strategy. Reyhan's friend; posts sporadically but practitioner-grade |
| Kevin Indig — Growth Memo | growth-memo.com | Most rigorous AI retrieval/citation research (1.2M-result sample sizes), weekly |
| Mike King — iPullRank | ipullrank.com | Passage-level optimisation / relevance engineering — how AI reads passages, not pages |
| Aleyda Solis — SEOFOMO | seofomo.com + aleydasolis.com/en | Weekly curated pulse of the whole space + SaaS/ecommerce AI-search frameworks |

**Alternates** (swap in if a tracked source goes quiet): Lily Ray (algorythmic.co — brand signals in LLMs), Bernard Huang (clearscope.io/blog — tool-maker view of AI content readability).

**Also always check:** Google Search Central (algorithm updates, AI Overviews/AI Mode changes, schema support), and anything Reyhan pastes in (podcast notes, courses, threads).

### 2. Performance review (internal)
- Pull the content register: which posts got AI citations / rankings, which didn't
- Diff winners vs losers against the Locked Rules — which rules are earning their place, which are unproven
- GSC: branded search trend + position-8-20 movement since last loop

### 3. Update the skill
- Propose rule changes to Reyhan as a short diff: ADD / CHANGE / RETIRE per rule, each with the evidence
- On approval, edit the Locked Rules in one pass and append an Improvement Log entry (date, what changed, why, source)
- Rules contradicted by our own performance data get retired even if a guru still preaches them — our data outranks external advice

**Cadence:** monthly minimum — automated via the `seo-engine-improve` cloud routine (1st of each month, ~8 AM UK; results DM'd to Reyhan on Slack). Trigger a manual run immediately on: a Google core update, a major AI-search product change (new AI Mode features, ChatGPT search changes), or a post unexpectedly winning/losing citations.

---

## Improvement Log

### 2026-08-14 — Reddit AEO-agency thread → off-page + measurement layer
Reyhan shared a Reddit thread where practitioners (incl. Marina, an AEO strategist at Edge Studio) debated whether paying an agency for AEO is worth it. The consensus: on-page fundamentals (FAQ schema, question headings, entity/snippet work) are DIY-able and are what most "AEO" retainers wrongly resell as a checklist — which our skill already reflects (term "AEO" retired, C1-C14 cover the on-page layer). The genuine agency-grade work they named was all off-page + measurement, which our Playbook under-specified. ADDED: C15 (review/recommendation-signal engineering — reviews phrased as recommendations are citation signals), C16 (citation-source targeting — identify the exact third-party domains AI cites for our category and earn presence there, making the AS/C9 "external weight" rule operational), C17 (entity/knowledge-graph building — sameAs + Wikidata/Crunchbase so engines resolve us as a known entity). Metrics workflow: added Step 2c (brand-description log + living answer-intent map — track HOW we're described, not just cited y/n) and a required purchase-intent audit in Step 1 (BOFU buying prompts tracked month-over-month = the visibility score). Wave Lens 4 gained a recommendation-signal + off-site-entity check. Guardrail held: still no "AEO" branding, still one discipline. Commercial spin-off logged separately to the offers wiki: lead with a productised one-time "AI Visibility Audit" entry offer ahead of the retainer (Marina: an audit beats a $5k/mo retainer before you know your baseline). Source: WhatsApp/Reddit thread pasted by Reyhan 2026-08-14.

### 2026-08-05 — Panel methodology deep-dive → Wave Review Framework
Extracted the concrete evaluation criteria from all 6 tracked experts' 2025-2026 published work and built the Wave Review Framework (Gate 0 + 5 lenses) from them. ADDED rules C12 (self-contained passages, MK), C13 (single-URL completeness, KI), C14 (30-day freshness = 3.2x citations, KI). Key sources: Indig's State of AI Search Optimization 2026 (growth-memo.com — 59.5% of cited URLs are listicles, 30-day recency data), King's chunking + query fan-out guides (ipullrank.com), Solis's AI Search Optimization Checklist + third-party citation research (aleydasolis.com — 84-93% of citation weight is external), Patel's LLM seeding guide (neilpatel.com/blog/llm-seeding/), Velez's LinkedIn system posts, Ray's Substack reflection (crawlability blockers, listicle-manipulation warning).

### 2026-08-04 — Neil Patel 2026 sweep (first entry)

Added rules A6, B6-B7, C8-C11, F5 + pillar 2,000-word target. Reframed skill core: AI-engine citation primary, classic Google alongside; "AEO" term retired. Rules tagged "NP 2026" come from Neil Patel / NP Digital's 2026 content. Key sources if a rule needs re-verifying:

- https://neilpatel.com/blog/seo-dead/ — AI Overviews on 30-47% of US desktop searches, top-position CTR down ~58%; citation > ranking
- https://neilpatel.com/blog/llm-optimization-llmo/ — LLM-friendly formatting, schema as "cheat sheet", citation-magnet content types
- https://neilpatel.com/blog/keyword-research/ — volume unreliability, conversational/prompt research
- https://neilpatel.com/blog/updating-old-content-to-boost-ranking/ — refresh +106% organic traffic
- https://neilpatel.com/blog/aeo-vs-geo-vs-llmo/ — his stance: AEO/GEO/LLMO are one unified discipline (matches our no-"AEO" rule)

His client case (RefiJet, 2026): traditional SEO + AI-citation optimisation together drove +522% top-3 rankings YoY and +2,012% LLM traffic — evidence the combined approach in this skill is the right shape.
