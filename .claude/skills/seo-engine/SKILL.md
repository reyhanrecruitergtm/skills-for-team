# SEO Engine Skill

Build, publish, and optimise SEO content for recruitergtm.com. Every page and blog post is built for both Google ranking and AI engine citation (AEO).

---

## How to Invoke

- "Write a blog post about [topic]" → `/seo-engine`
- "Add a new page to the website about [topic]" → `/seo-engine`
- "Optimise [page] for SEO" → `/seo-engine`

---

## What This Skill Does

1. **Creates SEO-optimised blog posts and pages** as Next.js App Router components
2. **Deploys them to Vercel** via CLI
3. **Updates sitemap automatically** (sitemap.ts in app/)
4. **Adds structured data** (JSON-LD) per page
5. **Follows AEO best practices** so content gets cited by ChatGPT, Perplexity, and Google AI Overviews

---

## Website Location

**Project:** `/Users/reyhankhan/Library/CloudStorage/GoogleDrive-reyhan@recruitergtm.com/My Drive/EA Demo/projects/website-nextjs/`
**Domain:** recruitergtm.com
**Hosting:** Vercel (free tier)
**Framework:** Next.js 16 App Router + Tailwind CSS + shadcn/ui
**Deploy command:** `cd [project dir] && vercel deploy --prod`

---

## Target Keywords (Primary Clusters)

### Cluster 1: Recruitment Automation
- recruitment automation tools
- how to automate recruitment
- recruitment business automation
- recruitment agency management system

### Cluster 2: AI in Recruitment
- AI for recruiters
- AI recruitment software
- AI sourcing tools for recruiters
- Claude Code for recruiting

### Cluster 3: Outbound & Sourcing
- outbound recruitment strategy
- candidate sourcing automation
- sourcing automation tools
- LinkedIn automation for recruitment

### Cluster 4: Agency Growth
- how to scale a recruitment agency
- recruitment agency growth strategies
- recruitment lead generation tools
- remote recruitment team

### Cluster 5: Tool Comparisons
- Clay alternatives for recruiting
- best recruitment CRM for agencies
- OutboundOS vs Lemlist
- recruitment tech stack 2026

---

## Content Architecture (Hub & Spoke)

### Pillar Pages (Hub)
These are long-form (2,000-3,000 word) authority pages living at top-level routes:

1. `/automation` — "The Complete Guide to Recruitment Automation in 2026"
2. `/ai-recruiting` — "AI for Recruiters: Everything You Need to Know"
3. `/scaling` — "How to Scale a Recruitment Agency Past $100k/Month"

### Blog Posts (Spokes)
Shorter posts (800-1,500 words) that link back to pillar pages:

Route: `/blog/[slug]`

Each blog post targets a specific long-tail keyword and links to the relevant pillar page. This builds topical authority.

---

## Blog Post Creation Process

### Step 1 — Keyword & Intent
Identify the target keyword, search intent (informational, commercial, transactional), and which pillar page it links to.

### Step 2 — Create the Page File
Create `app/blog/[slug]/page.tsx` with:

```typescript
import type { Metadata } from "next";
import BlogPost from "./content";

export const metadata: Metadata = {
  title: "[Title] | RecruiterGTM",
  description: "[155 chars max, include primary keyword]",
  openGraph: {
    title: "[Title]",
    description: "[Description]",
    url: "https://recruitergtm.com/blog/[slug]",
    type: "article",
  },
};

export default function Page() {
  return <BlogPost />;
}
```

### Step 3 — Write the Content Component
Create `app/blog/[slug]/content.tsx` as a client component with:

```typescript
"use client";

export default function BlogPost() {
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    headline: "[Title]",
    description: "[Description]",
    author: {
      "@type": "Person",
      name: "Reyhan Khan",
      url: "https://www.linkedin.com/in/reyhankhan"
    },
    publisher: {
      "@type": "Organization",
      name: "RecruiterGTM"
    },
    datePublished: "[YYYY-MM-DD]",
    dateModified: "[YYYY-MM-DD]",
    url: "https://recruitergtm.com/blog/[slug]"
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd).replace(/</g, "\\u003c"),
        }}
      />
      {/* Blog content here */}
    </>
  );
}
```

### Step 4 — Content Structure (Non-Negotiable)

Every blog post MUST follow this structure for both SEO and AEO:

1. **H1** — Contains primary keyword. One per page.
2. **Answer paragraph** — First 40-60 words directly answer the query. This is what AI engines extract.
3. **H2 sections** — Each targets a secondary keyword or question
4. **FAQ section** — 3-5 questions with FAQPage schema markup
5. **Internal links** — Link to pillar page + 2-3 related blog posts
6. **CTA** — Book a call or join community. Every post ends with a CTA.
7. **Stats** — At least 1 statistic per 150-200 words with source attribution

### Step 5 — Update Sitemap
Add the new URL to `app/sitemap.ts`:
```typescript
{ url: `${baseUrl}/blog/[slug]`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.7 },
```

### Step 6 — Deploy
```bash
cd [project dir] && vercel deploy --prod
```

---

## AEO Rules (Answer Engine Optimisation)

These rules ensure content gets cited by ChatGPT, Perplexity, and Google AI Overviews:

1. **Answer-first H2s** — Start every section with a 40-60 word direct answer before expanding
2. **One stat per 150-200 words** — AI engines prefer citable data with sources
3. **Semantic chunking** — Use bullet points, tables, and numbered lists. AI parses these better than prose.
4. **FAQPage schema** — Add to every blog post. AI engines extract Q&A pairs directly.
5. **Update quarterly** — Refresh high-value posts with new data every 3 months
6. **Tables over paragraphs** — Comparison content works better in table format for AI extraction
7. **No fluff intros** — Start with the answer. "In this article we will explore..." gets skipped by AI.

---

## Content Voice

Use the same voice rules as the email-writer and linkedin-content skills:
- Write like Reyhan: practitioner, not consultant
- Short sentences. One idea per sentence.
- Real numbers, real client names, real timelines
- British/neutral English
- No AI vocabulary (leverage, delve, crucial, pivotal, landscape)
- Max 1 em dash per post
- Anti-fluff: if a sentence could apply to any industry, rewrite it for recruitment specifically

---

## FAQ Schema Template

Add to every blog post that has a FAQ section:

```typescript
const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: [
    {
      "@type": "Question",
      name: "[Question]",
      acceptedAnswer: {
        "@type": "Answer",
        text: "[Answer - keep under 200 words]"
      }
    },
    // ... more questions
  ]
};
```

---

## Organization Schema (Add to Layout)

Add this to `app/layout.tsx` once:

```typescript
const orgSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: "RecruiterGTM",
  url: "https://recruitergtm.com",
  logo: "https://recruitergtm.com/favicon.png",
  description: "AI-powered GTM systems for recruitment agencies. OutboundOS, SourcingOS, ContentOS.",
  founder: {
    "@type": "Person",
    name: "Reyhan Khan"
  },
  sameAs: [
    "https://www.linkedin.com/in/reyhankhan",
    "https://www.youtube.com/@recruitergtm",
    "https://www.skool.com/recruitergtm"
  ]
};
```

---

## Completed SEO Work (as of 2026-04-16)

### Infrastructure — DONE
- Blog directory created at `/app/blog/`
- Blog index page at `/blog`
- OG image created (1200x630, Main Logo on black bg) at `/public/og-image.png`
- OG images updated from lovable.dev to recruitergtm.com/og-image.png in layout.tsx
- Organization JSON-LD in layout.tsx

### All Pages Optimised — DONE (18 pages)
Every page now has:
- Canonical URL (`alternates.canonical`)
- Page-specific OpenGraph tags
- Relevant JSON-LD structured data (WebSite, Service, Course, BlogPosting, FAQPage)

Pages with **Service JSON-LD**: `/outboundos`, `/sourcingos`, `/contentos`, `/gtmacademy`
Pages with **FAQPage JSON-LD + visible FAQ sections**: `/outboundos`, `/sourcingos`, `/contentos`, blog post
Pages with **Course JSON-LD**: `/outbound-os` (mini-course)
Pages with **WebSite JSON-LD**: `/` (homepage)
Pages with **BlogPosting JSON-LD**: blog post, all 4 pillar guides

### Pillar Pages (Hub & Spoke) — DONE
Built around the 4-pillar framework. These are educational guides, NOT service pages. They do NOT appear in the site header nav.

| Pillar | URL | Target Keyword | JSON-LD | FAQ |
|--------|-----|---------------|---------|-----|
| OutboundOS | `/outbound-guide` | outbound recruitment strategy | BlogPosting + FAQPage | 5 Qs |
| SourcingOS | `/sourcing-guide` | candidate sourcing automation | BlogPosting + FAQPage | 5 Qs |
| ContentOS | `/content-guide` | LinkedIn for recruiters | BlogPosting + FAQPage | 5 Qs |
| OperatorOS | `/operations-guide` | recruitment agency management system | BlogPosting + FAQPage | 5 Qs |

Each pillar page has CTA buttons (Book a Call + See [Service]) at the bottom. These CTAs are allowed. The header nav only shows: OutboundOS, SourcingOS, ContentOS, GTM Academy.

### Blog Posts — 1 LIVE, 9 REMAINING

**Published:**
| # | Title | URL | Pillar |
|---|-------|-----|--------|
| 1 | How Patrick Hit 2M LinkedIn Impressions in 90 Days | `/blog/how-patrick-hit-2m-linkedin-impressions-90-days` | ContentOS |

Old URL `/case-study/patrick-schildmann` redirects to the blog post.

**Still to write (priority order):**
| # | Title | Target Keyword | Type | Pillar Page |
|---|-------|---------------|------|-------------|
| 2 | 5 Recruitment Automation Mistakes Costing You $500k/Year | recruitment automation | Problem-solution | /outbound-guide |
| 3 | The Sourcing Automation Playbook: 30-50 Candidate Conversations/Month | sourcing automation | Playbook | /sourcing-guide |
| 4 | How to Scale a Recruitment Agency to $100k MRR Without Hiring 5 More People | scale recruitment agency | Guide | /operations-guide |
| 5 | Clay vs Lemlist vs HeyReach: Which Outbound Stack for Your Agency | recruitment outbound tools | Comparison | /outbound-guide |
| 6 | Why Volume Sourcing Is Dead: The Qualified Enrichment Framework | AI sourcing recruiters | Contrarian | /sourcing-guide |
| 7 | Building a Remote Recruitment Team: 48-Hour GTM Engineer Placement | remote recruitment team | Case study | /operations-guide |
| 8 | Recruitment CRM for Agencies: 7 Setup Mistakes That Waste 10 Hours/Week | recruitment CRM agencies | Listicle | /operations-guide |
| 9 | The Recruitment Content Flywheel: Generate Inbound Clients Via LinkedIn | recruitment lead generation | Framework | /content-guide |
| 10 | AI Twins for Recruiters: Why Your LinkedIn Bot Isn't Working | AI for recruiters | Contrarian | /outbound-guide |

### Search Engine & AI Indexing — DONE
- **Google Search Console**: Verified (domain property). Sitemap submitted. 4 priority URLs manually requested for indexing (homepage, /outboundos, /outbound-guide, /blog/patrick post).
- **IndexNow (Bing/ChatGPT/Copilot)**: API key deployed at `/public/23383546a937c61170b825616560e5e8.txt`. 15 pages submitted, 202 accepted. Use IndexNow to ping Bing whenever new pages are published.
- **Bing Webmaster Tools**: Pending setup (import from Google Search Console at bing.com/webmasters).
- **robots.txt**: Allows all crawlers (`*`). GPTBot, ClaudeBot, PerplexityBot, Google-Extended all permitted.
- **AI crawlers**: No bots blocked. FAQ schemas and answer-first paragraphs optimised for AI citation.

### IndexNow — How to Ping After Publishing
After deploying any new page, run this to get it indexed in Bing/ChatGPT within minutes:
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

---

## What NOT to Do

- Never publish thin content (under 600 words)
- Never keyword stuff. Use primary keyword 3-5 times naturally.
- Never skip the FAQ section. It's the AEO engine.
- Never deploy without metadata and JSON-LD
- Never write generic content. Every sentence should be specific to recruitment agencies.
- Never copy competitor content. Use original data from RecruiterGTM clients.
- Never add pillar guide pages to the header nav. Header only shows: OutboundOS, SourcingOS, ContentOS, GTM Academy.
- Never deploy without running IndexNow ping for new pages.
