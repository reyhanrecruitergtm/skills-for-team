# SEO Playbook — Glossary & Backlink Guide

Plain-English definitions plus how each one applies to RecruiterGTM specifically. Read this before your first SEO task if the terms are new. Everything here is written for our situation: a young domain (DR 0.1 as of 2026-08-12) whose primary target is AI-engine citation, classic Google alongside it.

> Numbers in brackets like [KD 5] use the metric being defined. Ahrefs is our data source, so where a metric is tool-specific (DR, UR, KD, Traffic Potential) the Ahrefs definition is the one that applies.

---

## 1. Authority & Backlinks

**Backlink** — A link from another website's page to one of yours. Google and AI engines treat each one as a vote of trust: the more relevant, high-quality sites point to you, the more they believe you.
*Use case:* We have almost none, which is why our Domain Rating is 0.1. Building these is now a first-class workstream, not an afterthought (see the Backlink Guide below).

**Referring domain** — The count of unique websites linking to you, regardless of how many links each one sends. Ten links from one blog = one referring domain.
*Use case:* This matters more than raw backlink count. In our competitor scan, alexbirkett.com ranks page 1 with only 7 referring domains — proof that a handful of *quality* domains beats hundreds of junk links.

**Domain Rating (DR)** — Ahrefs' 0-100 score of a whole domain's backlink strength, logarithmic (getting 20→30 is far easier than 70→80).
*Use case:* Ours is 0.1. The pages we're trying to outrank sit at DR 40-95. Our first authority goal is DR ~20, which unlocks the "beatable" competitors (asymbl DR 40, hiretruffle DR 47).

**URL Rating (UR)** — The same idea as DR but for a single page instead of the whole domain. Driven by links pointing at that specific URL plus internal links.
*Use case:* A strong pillar page with lots of internal links from spokes builds UR even before the domain catches up. This is why internal linking matters.

**Domain Authority (DA)** — Moz's competitor metric to DR, also 0-100. Same concept, different company's maths.
*Use case:* You'll see DA quoted by guest-post sellers and PR sites. Treat it as roughly interchangeable with DR for judging a site's strength; we standardise on DR because we run on Ahrefs.

**Anchor text** — The visible, clickable words of a link ("recruitment automation software" vs "click here").
*Use case:* When we earn or place a link, natural, varied anchor text is safer than repeating an exact keyword every time — Google flags over-optimised anchors as manipulation.

**Dofollow / nofollow** — A dofollow link passes authority ("link juice") to you. A nofollow link (tagged `rel="nofollow"`) tells Google not to pass authority. Most social, forum, and UGC links are nofollow.
*Use case:* Nofollow links (LinkedIn, Reddit) still drive traffic and AI citations even though they don't lift DR directly. We chase both — dofollow for DR, nofollow for reach and citation.

**Link building / Digital PR** — The active practice of earning backlinks. Digital PR is the highest-quality version: creating something newsworthy (original data, a report) that journalists and bloggers cite.
*Use case:* Our angle is original data nobody else has (650 agencies audited, 50+ OutboundOS deployments). That's link bait — see the Backlink Guide.

---

## 2. Keywords & Difficulty

**Keyword** — A word or phrase people type (or say to an AI) to search. "Recruitment automation software" is a keyword.

**Seed keyword** — A broad starting term you feed into a research tool to generate hundreds of related ideas.
*Use case:* We seeded "candidate sourcing", "recruitment automation", "AI recruiting" etc. into Ahrefs Keywords Explorer to build the keyword universe.

**Long-tail keyword** — A longer, more specific, lower-volume phrase ("passive candidate sourcing techniques" vs "sourcing"). Less traffic each, but easier to rank and higher intent.
*Use case:* At DR 0.1 long-tail is where we win first. 94.7% of all keywords get ≤10 searches/month, so long-tail is most of the map anyway.

**Search volume** — Estimated monthly searches for a keyword in a given country.
*Use case:* We filter for volume, but never on volume alone — a low-volume term with buyer intent beats a high-volume term that just brings tyre-kickers.

**Keyword Difficulty (KD)** — Ahrefs' 0-100 estimate of how hard it is to rank in the top 10 for a keyword, based mostly on the backlink strength of the pages already ranking.
*Use case:* Our rule: never target KD > 40 on a domain under DR 25 (that's us). We're hunting KD 0-10. Caveat we learned live: KD can say "easy" while the actual SERP is full of DR 70+ pages — always sanity-check KD against a real SERP scan.

**Traffic Potential (TP)** — Ahrefs metric: the total traffic the current #1 page for your keyword gets from *all* the keywords it ranks for. Shows the real prize of ranking, not just the one term's volume.
*Use case:* "ai recruiting companies" has only 250 volume but TP 6,000 — ranking that one page could pull traffic from thousands of related terms. TP is often a better priority signal than volume.

**Parent Topic** — Ahrefs concept: the broader keyword you can rank for while covering a narrower one on the same page. Stops you writing five thin posts when one would rank for all five.
*Use case:* If "what is candidate sourcing" and "candidate sourcing definition" share a parent topic, we write ONE post, not two.

**Search intent** — The *why* behind a search. Four main types:
- **Informational** — learning ("what is recruitment automation").
- **Commercial** — comparing before buying ("best recruitment automation software").
- **Transactional** — ready to act ("book recruitment automation demo").
- **Navigational** — looking for a specific brand/site ("hireEZ login").
*Use case:* Intent decides format. A commercial term needs a comparison listicle with verdicts; an informational term needs a clear definition + guide. Matching intent is non-negotiable (rule B5).

**CPC (Cost Per Click)** — The average price advertisers pay per click on a keyword in paid search, in USD (Ahrefs returns cents — divide by 100).
*Use case:* We don't run ads, but CPC is a free read on commercial value. A high CPC ("candidate sourcing platform" CPC $14) means buyers with budget search it — worth targeting organically even at lower volume.

---

## 3. Performance & Ranking Metrics

**SERP (Search Engine Results Page)** — The page Google shows for a query.

**Position / Ranking** — Where your page sits in the organic results (1 = top). "Position 8-20" is the upgrade sweet spot once you have pages ranking.
*Use case:* We have exactly one ranking page today ("gtm recruiter", position 1), so the position-8-20 "quick wins" play doesn't apply yet — it will once posts start landing.

**Impressions** — How many times your page appeared in search results, whether or not anyone clicked.
*Use case:* Rising impressions before clicks = Google is testing you. It's the first sign a new post is being noticed. Watched in Google Search Console (GSC).

**CTR (Click-Through Rate)** — Clicks ÷ impressions, as a %. Position 1 gets ~30-40%; it drops fast down the page.
*Use case:* A page with high impressions but low CTR usually has a weak title/meta description — fixable without touching rankings. AI Overviews are cutting CTR industry-wide (~58% drop on top positions), which is exactly why citation now matters more than pure ranking.

**Organic traffic** — Visitors arriving from unpaid search results.
*Use case:* Our baseline is ~75/month. Every metrics run tracks this trend; it's the scoreboard number.

**SERP features** — Everything on a results page that isn't a plain blue link: featured snippets, People Also Ask, AI Overviews, image/video packs, local packs, sitelinks.
*Use case:* If a query's SERP is dominated by an AI Overview or a snippet, ranking #1 organic may still lose clicks — we check SERP features before committing to a keyword.

**Featured snippet** — The boxed direct answer Google lifts to the top of some results ("position zero").
*Use case:* Won by answering the query in a clean 40-60 word paragraph or a tight list — the same formatting that wins AI citations. Our C1/C2 rules target this directly.

---

## 4. Indexing & Technical

**Crawling** — Search/AI bots (Googlebot, GPTBot, PerplexityBot, ClaudeBot) reading your pages by following links.
*Use case:* If bots can't crawl it, it can't rank or be cited. Our robots.txt deliberately allows all the AI crawlers.

**Indexing** — Google storing a crawled page in its database so it's eligible to rank. Crawled ≠ indexed ≠ ranking — they're three separate steps.
*Use case:* After publishing we manually request indexing in GSC for priority pages and fire an IndexNow ping so Bing/others pick it up in minutes instead of weeks.

**IndexNow** — A protocol that instantly tells participating engines (Bing, Yandex, others) you've published or updated a URL, instead of waiting to be crawled.
*Use case:* We ping it on every publish. Our key lives at `/public/23383546a937c61170b825616560e5e8.txt`.

**Sitemap** — An XML file listing all your pages so engines can find them. Lives at `/sitemap.xml`.
*Use case:* Updated on every publish (`app/sitemap.ts` in the Next.js repo). Submitted to GSC.

**robots.txt** — A file telling crawlers what they may and may not access.
*Use case:* Ours allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended. A single wrong line here can make you invisible to AI engines — it's Gate 0 of the review.

**Canonical URL** — The tag that tells Google which version of a page is the "real" one when duplicates exist (e.g. with/without tracking params).
*Use case:* Prevents duplicate-content dilution. Every one of our pages sets one.

**noindex** — A tag telling engines to keep a page OUT of the index.
*Use case:* Used on funnel/logistics pages we don't want ranking (e.g. `/call-booked`, `/mastermind-agenda-2026`). Never put it on a blog post by accident.

**Schema / Structured data (JSON-LD)** — Code that labels your content for machines ("this is an FAQ", "this is an article by this author, published this date"). Doesn't change how the page looks to humans.
*Use case:* We put BlogPosting + FAQPage on every post. It's a cheat sheet that helps AI engines extract and cite us, and can trigger rich results. Validate at validator.schema.org.

**Core Web Vitals** — Google's page-experience metrics: loading speed (LCP), interactivity (INP), visual stability (CLS).
*Use case:* Our Next.js + Vercel stack handles most of this by default. Worth a check, not a obsession, at our stage.

---

## 5. AI Search (our primary target)

**AI Overview (AIO)** — Google's AI-generated answer box at the very top of many results, pulling from multiple sources. Now on 30-47% of US desktop searches.
*Use case:* Being *cited inside* the AI Overview is the new #1. It's why our whole content structure optimises for extraction (40-60 word answers, FAQs, tables).

**AI citation** — When ChatGPT, Perplexity, Claude, or an AI Overview names or links your page in its answer.
*Use case:* This is our primary success metric, tracked monthly with the metrics workflow. 84-93% of AI citation weight comes from third-party sites, which is why distribution (LinkedIn, guest posts, Reddit) sits alongside on-page work.

**GEO / AEO / LLMO** — Competing industry acronyms (Generative Engine / Answer Engine / LLM Optimisation) all describing "optimising to be cited by AI engines."
*Use case:* We deliberately DON'T use "AEO" and treat this as one discipline with classic SEO, not a separate thing. Know the terms because clients and gurus use them.

**Retrieval / passage-level ranking** — AI engines pull and cite *passages* (sections), not whole pages. A section is retrieved on its own merits.
*Use case:* Our "lift test" (rule C12): every section must carry its entity + context + claim if pulled out alone. Write self-contained chunks.

**Query fan-out** — An AI engine answers one prompt by silently running many related sub-queries and combining results.
*Use case:* A post should cover the comparative, reformulated, and question variants of a term, not just the head keyword, so it surfaces across the fan-out.

**llms.txt** — An emerging convention (a file at your root) proposing which content AI models should use. Not yet a ranking factor; worth tracking.

---

## 6. Content & Structure

**Topical authority** — Google/AI trusting you on a subject because you've covered it thoroughly and interlinked it, rather than posting one-off articles.
*Use case:* Why we build in clusters (hub + spokes) instead of scattered posts. Owning "candidate sourcing" end-to-end beats one lonely post.

**Pillar / Hub-and-spoke** — A pillar (hub) is a broad cornerstone guide; spokes are focused posts on sub-topics, all interlinking back to the pillar.
*Use case:* Our four pillars are /outbound-guide, /sourcing-guide, /content-guide, /operations-guide. Every blog post links to its pillar + 2 sibling spokes (rule D2).

**Internal linking** — Links between your own pages.
*Use case:* Spreads authority (UR), helps crawling, and builds topical authority. Free and under our full control — we never skip it.

**E-E-A-T (Experience, Expertise, Authoritativeness, Trust)** — Google's framework for judging content credibility, especially the author.
*Use case:* We state it plainly, not imply it: real author byline (Reyhan), a one-line credibility statement, named sources, first-hand data. This is a genuine edge for us — we've actually done the work.

**Content refresh** — Updating an existing post (new stats, new sections, current year) rather than writing a new one.
*Use case:* Updating old content averages +106% organic traffic and content updated within 30 days earns ~3.2x more AI citations. We refresh on a 90-day review cycle, and refresh beats net-new when a page already covers the topic (rule A6).

**Meta title / Meta description** — The clickable headline (≤60 chars) and summary (≤155 chars) shown in search results.
*Use case:* The title carries the primary keyword; the description sells the click. Weak ones tank CTR even at good positions.

**H1 / H2** — Page headings. Exactly one H1 (the title, containing the primary keyword); H2s structure the body.
*Use case:* We phrase H2s as the questions people actually ask ("How do recruiters automate sourcing?") so each one can be extracted as an answer.

**Word count target** — The length to aim for, set by the median of the current top 5 ranking pages (±10%), not a fixed number.
*Use case:* Going much shorter loses; going 3x longer wastes effort. Pillars are the exception — we target 2,000+ words there.

---

## 7. How We Build Backlinks (RecruiterGTM playbook)

We're at DR 0.1, so this is the single biggest lever on whether any of our content ranks. We build links from our real assets, in rough priority order:

1. **Original-data digital PR (highest value).** Turn our proprietary numbers into a citable asset — e.g. a "State of Recruitment Agency Outbound 2026" report from the 650 audits + 50+ deployments. Original stats are what journalists, bloggers, and AI engines cite. One good data study can earn dozens of referring domains.

2. **Podcast guesting.** Every appearance = a dofollow link from the show's site + episode notes, plus referral traffic. The Benjamin Mena / Elite Recruiter episode is already one of our strongest lead magnets — we systematise this: pitch 2-3 recruitment/GTM podcasts a month, always get the link to a relevant page (not just the homepage).

3. **Guest posts on recruitment + SaaS blogs.** Write a genuinely useful post for a relevant DR 30-60 site with a contextual link back to a pillar. Target recruitment-industry publications, ATS/tool blogs, and adjacent GTM sites. Quality and relevance over volume.

4. **HARO-style source requests** (Help a B2B Writer, Featured, Qwoted, Terkel). Reyhan answers journalist queries on recruitment/AI/GTM; earns a cited link when quoted. Low effort, compounding.

5. **The LinkedIn → link flywheel.** Reyhan's LinkedIn content already drives attention. Point posts at first-comment links to blog posts and lead magnets; others who reference the ideas link back. Nofollow but strong for traffic + AI citation.

6. **Reddit / community citation.** r/RecruitmentAgencies ranks on page 1 for our automation terms. Being genuinely helpful there (not spammy) earns traffic and gets our pages surfaced in threads AI engines cite. Nofollow, but real.

7. **Client case-study cross-links.** When a client (Patrick, etc.) features our work, or we're named on their site, that's a relevant contextual link. Ask for it as part of delivery.

8. **Tool directories & partner pages.** Affiliate/partner relationships (Clay, Instantly, HeyReach, Apify, etc.) sometimes list case studies or partners — a legitimate, relevant link source.

9. **Skool community + newsletter** as owned distribution that seeds the above — members and subscribers share and reference content, which surfaces it to potential linkers.

**What we do NOT do:** buy link packages, PBNs, mass directory spam, or exact-match-anchor schemes. At DR 0.1 a clean, slow, relevant profile is worth more than a fast dirty one, and Google penalises the dirty version.

**Reality check:** links compound slowly. Expect 3-6 months to move DR meaningfully and start ranking the Automation + AI cluster. Anyone promising faster at DR 0.1 is selling something.

---

## Quick reference — what "good" looks like for us right now

| Metric | Our status (2026-08-12) | Near-term target |
|--------|--------------------------|------------------|
| Domain Rating (DR) | 0.1 | ~20 (unlocks DR 40-50 competitors) |
| Referring domains | ~none | 20-30 quality domains |
| Ranking keywords | 1 | 20+ |
| Organic traffic/mo | ~75 | grow via the cluster plan |
| Target KD ceiling | — | ≤ 10 (never > 40 under DR 25) |
| Primary success metric | — | AI citations (ChatGPT/Perplexity/AIO) |
