# Q&A Topic Scout Skill

Research the recruitment systems + GTM space and pitch **at least 5 teachable Q&A topics** mapped to the 5 RecruiterGTM pillars. Runs every Wednesday morning ahead of the 4:30 PM UK community Strategy call, so Reyhan picks a topic and hands it to `/qa-deck-generator`.

## How to Invoke
- **Scheduled:** Wednesdays 8:00 AM Europe/London via the `schedule` skill (cron: `0 8 * * 3`, tz `Europe/London`)
- **Manual:** `/qa-topic-scout` any time (e.g. to re-run with a steer: `/qa-topic-scout focus on sourcing`)

---

## Locked Rules

### A. Output contract
- A1. **Minimum 5 topics per run.** Every topic maps to exactly one of the 5 pillars; across the 5+ topics, cover at least 3 different pillars.
- A2. Each topic must teach a **strategy** (a repeatable play members can implement), not news commentary. Test: "could a community member action this in their agency next week?"
- A3. Topics must be NEW to the community — check `~/Desktop/Community-Decks/weekly-qa/` folder names and `content/linkedin-posts.md` before pitching. Never re-pitch a topic covered in the last 8 weeks.
- A4. Save the full topics doc to `~/Desktop/Community-Decks/weekly-qa/topics/YYYY-MM-DD-topics.md` (weekly Q&A artifacts rule) AND send the summary as a Slack DM.

### B. The 5 pillars (topic categories — from `reference_recruitergtm_5_pillars.md`)
1. **AI Layer** — Claude Ops Manager, skill libraries, MCP integrations, AI-native workflows
2. **Multichannel Outbound** — email + LinkedIn + voice, intent playbooks, copy, reply handling
3. **LinkedIn Content + Authority** — content frameworks, ContentGPS, drafting, repurposing
4. **ATS + Newsletter** — ATS hygiene, segmentation, Beehiiv nurture, re-engagement
5. **Productization** — offer structure, pricing, retained/fractional/subscription models

### C. Research sweep (do ALL lanes, keep it fast)
Use the `research` agent (Haiku, WebSearch) or direct WebSearch — one query lane per pillar plus a trends lane. Restrict to the last 30 days where possible.

1. **AI Layer lane:** new Claude/Anthropic releases, MCP ecosystem news, AI agent workflows for recruiting ("Claude recruiting workflow", "AI agents recruitment agency")
2. **Outbound lane:** cold email + LinkedIn outreach changes (deliverability updates, LinkedIn limits, Clay/Instantly/HeyReach feature releases, intent-signal tactics)
3. **Content lane:** LinkedIn algorithm changes + creator tactics (cross-check `content-os/algorithm-playbook.md` — flag anything that contradicts it)
4. **ATS/Newsletter lane:** ATS vendor news (Recruiterflow, Loxo, Bullhorn, Ashby, Recruit CRM), newsletter/nurture tactics for recruiters
5. **Productization lane:** recruitment agency business models, retained/fractional pricing trends, productized service case studies
6. **Trends lane:** what top GTM voices are teaching this week (Clay blog/webinars, GTM engineering newsletters, 30MPC, recruitment industry reports) — steal angles, adapt to recruitment

### D. Topic card format (each of the 5+)
```
## N. [Q&A-ready title — specific, provocative, no clickbait]
- Pillar: [one of the 5]
- Why now: [the trigger — source + date, one line]
- The strategy to teach: [2-3 bullets, the actual play members implement]
- Member fit: [who this serves — solo founder / small team / scaling agency]
- Poll idea: [one audience poll for the deck, per qa-deck-generator B6 style]
- Repurpose: [blog post title for Noroze + LinkedIn hook line]
```

### E. Ranking + recommendation
- E1. Rank the topics 1-N. Score on: member demand signals (recent Skool questions if known, common pain points) → teachability (clear play) → freshness (why-now strength) → repurposing value.
- E2. End with a one-line recommendation: "My pick: #N because …" — Reyhan decides, the skill recommends.

### F. Delivery
- F1. Slack DM to Reyhan — channel_id `U0AD7M61FLY` (self-DM, same as morning-brief). Use `mcp__slack__slack_post_message` (or `mcp__claude_ai_Slack__slack_send_message`).
- F2. DM format: "🎯 Wednesday Q&A — 5 topic pitches" header, then per topic: number, title, pillar, one-line why-now. Full cards live in the saved file — link the path. End with the recommendation + "Reply with a number and I'll brief /qa-deck-generator."
- F3. Never auto-generate the deck. Topic selection is Reyhan's call; deck generation is a separate explicit step.

### G. Context to load before researching (mandatory)
1. `memory/reference_recruitergtm_5_pillars.md` — pillar definitions
2. `~/Desktop/Community-Decks/weekly-qa/` — folder names = topics already covered
3. `content/linkedin-posts.md` — recent post angles (avoid duplication, spot pre-validated winners worth deepening)
4. `.claude/skills/content-os/algorithm-playbook.md` — current algorithm playbook (content-lane topics must align)
5. `context/current-priorities.md` — what Reyhan is pushing this quarter (topics should ladder into it)
6. `.claude/skills/community-os/SKILL.md` — member journey/checkpoints, so topics fit where members actually are

---

## Process (per run)

1. Load context (Section G).
2. Run the 6 research lanes (Section C) — parallel where possible, ~15 min budget total.
3. Draft 6-8 candidate topics, then cut to the strongest 5+ (Section A rules).
4. Write topic cards (Section D), rank them (Section E).
5. Save `~/Desktop/Community-Decks/weekly-qa/topics/YYYY-MM-DD-topics.md`.
6. Send the Slack DM (Section F).

## What NOT to do
- No news-roundup topics ("What happened in AI this week") — strategies only.
- No topics requiring tools the community doesn't use (check `reference_tool_stack.md` — Instantly + HeyReach + Clay + Claude Code are the defaults).
- No talent-placement topics — back-end only, never public/community-facing (`feedback_no_talent_placement_online.md`).
- Don't invent stats — every "why now" needs a real source.
