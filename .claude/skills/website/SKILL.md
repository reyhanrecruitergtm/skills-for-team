# Skill: Website

Manage RecruiterGTM website pages. Edit the Next.js repo directly, track all pages and their purpose, and plan SEO strategy.

## How to Invoke
`/website` followed by what you need — new page, page update, SEO plan, etc.

## Website
- **Domain:** recruitergtm.com
- **Built with:** Next.js (App Router) + Tailwind, in `projects/website-nextjs/`. Hosted on Vercel; pushes to `main` auto-deploy.
- **Lovable is RETIRED (2026-07-15, per Reyhan: "I never use Lovable anymore").** Never write Lovable prompts; make changes directly in the repo. Routes live in `app/<slug>/page.tsx`, shared views in `src/views/`, redirects in `next.config.mjs`, sitemap in `app/sitemap.ts`.
- Changing a page's URL = `git mv` the route dir + permanent redirect from the old slug + sitemap update + grep for internal links.

## Design Inspiration
Layout/component patterns worth borrowing (systems, not branding) live in `design-inspiration.md` — read it before any new page or redesign for recruitergtm.com or Pulse Recruit. First entry: hikmahaiagency.com (interactive funnel-viz hero, contextual colour system, proof density). Add a numbered entry whenever Reyhan flags a design he likes.

## Locked Rules
- A1. Every new Lovable page gets its prompt saved into `memory/reference_website_lovable.md` immediately. Don't defer to "later" — that's how the page log goes stale and Reyhan can't tell what's deployed.
- A2. Every page URL, purpose, form fields, and downstream connections (Attio, Pulse, etc.) tracked in `memory/reference_website_lovable.md`.
- A3. Save BEFORE the page is shipped, not after — easier to capture intent at the time of build than reconstruct later.
- A4. (2026-07-13) Every resource/guide/lead-magnet page includes the main site Header (`src/components/Header.tsx` in `projects/website-nextjs/`) at the top so visitors can navigate to the rest of the site. No standalone mini-navs on resource pages — flagged by Reyhan on the newsletter-launch-guide build.
- A5. (2026-07-13) Never put tool pricing on a public page without verifying it via web search the same day, and add a "pricing checked [month year]" line under any pricing table.
- A6. (2026-08-02) Every giveaway/lead-magnet page and blog post, once Reyhan approves it, gets a card added to `/resources` (`app/resources/page.tsx`) in the same pass — plus the sitemap entry. A page is not "done" until it's listed in the Resource Library. Flagged when `/contentos-breakdown` (then `/linkedin-content-sprint`) went live without a Resources card.

## Rules
1. Every new page gets a Lovable prompt saved here
2. Every page URL, purpose, and form fields tracked in `memory/reference_website_lovable.md`
3. Prompts should reference existing pages for consistency ("match the style of /start-pilot")
4. Never include design system details (colors, fonts) in prompts — Lovable has these
5. Always include: page purpose, sections, CTAs, any embeds, form fields if applicable

## Pages Built

### /start-pilot
- Form for leads wanting to start a managed pilot
- CTA: "Start Pilot Now"
- Webhook: Slack #client-onboarding + Attio update

### /claude-for-recruiters
- Free guide with 4 live Claude demos for recruiters
- CTA: Join Skool + Subscribe Newsletter

### /case-study/patrick-schildmann (NEW — prompt below)
- Case study landing page with Tella video embed
- Patrick Schildmann, Patrick Michaeli GmbH, Germany
- Finance & accounting recruitment

## Lovable Prompts

### /case-study/patrick-schildmann

See `projects/lovable-prompts/case-study-patrick.md` for the full prompt.

---

## SEO Strategy (Planned)
- Service pages: /outboundos, /sourcingos, /contentos
- Case study pages: /case-study/[name] (one per client)
- Resource pages: /claude-for-recruiters, future guides
- Blog/content: TBD
