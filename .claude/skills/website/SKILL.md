# Skill: Website (Lovable)

Manage RecruiterGTM website pages built on Lovable. Write prompts for new pages, track all pages and their purpose, and plan SEO strategy.

## How to Invoke
`/website` followed by what you need — new page prompt, page update, SEO plan, etc.

## Website
- **Domain:** recruitergtm.com
- **Built with:** Lovable (AI website builder)
- **Lovable already knows:** color scheme, fonts, brand guidelines, existing page structure. No need to repeat design system in prompts.

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
