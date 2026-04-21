# YouTube Content Skill

Generate titles, descriptions, thumbnail concepts, tags, pinned comments, and LinkedIn clip ideas from a video outline or transcript. Built for Reyhan's RecruiterGTM YouTube channel.

---

## How to Invoke

Paste a video outline, transcript, or rough notes → `/youtube-content`

The skill will output:
1. **5 title options** with different angles
2. **Full description** (primary keyword above fold, hook, timestamps if needed, CTAs, links)
3. **3 thumbnail concepts** with AI generation prompts (Ideogram / Nano Banana / Midjourney)
4. **7-10 tags**
5. **Pinned comment** to drive engagement
6. **End screen / card strategy**
7. **Content pillar tag** (Content GPS matrix)
8. **3-5 LinkedIn clip ideas** from the same video

---

## Channel Context

- **Channel:** RecruiterGTM (Reyhan Khan)
- **Niche:** GTM systems, AI for recruiters, Claude Code use cases, recruitment agency ops
- **Audience:** Recruitment agency owners, founders, GTM engineers
- **Skool community:** https://skool.com/recruitergtm
- **Website:** recruitergtm.com
- **Claude Code DFY page:** recruitergtm.com/claude-code-dfy

---

## The 4 Content Pillars (Content GPS Matrix)

Every video is tagged into one pillar:

| Pillar | Focus | Example angles |
|--------|-------|----------------|
| **OutboundOS** | Client-side outbound, lead gen, market mapping | TAM builds, Clay workflows, Instantly setups, funding signals |
| **SourcingOS** | Candidate sourcing, evergreen pipelines, intent signals | Boolean builds, MPC correlation, waterfall enrichment, ATS integration |
| **ContentOS** | LinkedIn / YouTube / newsletter systems | Voice training, content flywheels, batching, distribution |
| **OperatorOS / Claude Code** | Backend ops, SOPs, Claude Code setups | Ops manager builds, skill design, MCP integration, agency automation |

Every video should test **one pillar × one format**:

| Format | What it is |
|--------|------------|
| Case study | Real client before / after with numbers |
| Framework | Named system / process / matrix |
| Tutorial | Step-by-step setup or walkthrough |
| Behind-the-scenes | How Reyhan runs his own desk |
| Contrarian take | Counter-intuitive opinion with evidence |

---

## YouTube Algorithm (April 2026 State)

Three primary signals:

1. **Click-Through Rate (CTR)** — target 5%+. Below 2% = thumbnail / title problem.
2. **Average View Duration (AVD)** — target 50%+ of video length retained.
3. **Session Time** — the new north star. YouTube rewards videos that keep viewers on the platform *after* yours ends. Always link to your next video.

**Satisfaction signals** matter too — repeat views, not-interested clicks, likes, comments, subscribes. The algorithm surveys viewers post-watch.

**Implication for this skill:** every description includes a "Watch next" link to a related RecruiterGTM video. Pinned comment drives engagement. Mid-video CTA pushes to Skool or newsletter (not just a subscribe ask).

---

## Title Formulas That Work (April 2026)

**Length:** 50-60 characters. Primary keyword in first 40 characters. Natural language beats keyword stuffing.

**Formulas:**

1. **How to [Specific Outcome] (2026 Guide)**
   Example: "How to Install GTM Systems for Recruiters (2026 Guide)"

2. **[Number] [Specific thing] [Big promise]**
   Example: "5 Claude Code Skills Every Recruiter Needs in 2026"

3. **The [Tool/Framework] that [Result]**
   Example: "The Claude Code Setup That Replaced My VA"

4. **Why [Popular belief] is Wrong (Do This Instead)**
   Example: "Why Mass Outreach is Dead for Recruiters (Do This Instead)"

5. **[Name] [Result] in [Timeframe] with [Method]**
   Example: "How Patrick Hit 2M LinkedIn Impressions in 90 Days"

**Always generate 5 title variants across different formulas** so Reyhan can pick the one that fits the video best.

---

## Description Structure

**Above the fold (first 125 characters):** This is what shows in search results and suggested videos before "Show more". Must include primary keyword + hook.

**Full structure:**

```
[Hook line — 1 sentence using primary keyword in first 70 chars]

[2-3 sentence expansion of what the viewer will learn and why it matters]

────────────────────
🎯 JOIN THE COMMUNITY
────────────────────
Build your own GTM system with recruitment agency owners inside the RecruiterGTM community:
👉 https://skool.com/recruitergtm

────────────────────
📚 FREE RESOURCES
────────────────────
• Claude Code for Recruiters: https://recruitergtm.com/claude-code-dfy
• OutboundOS playbook: https://recruitergtm.com/outbound-os
• Newsletter (weekly): https://recruitergtm.com/newsletter

────────────────────
⏱ TIMESTAMPS
────────────────────
0:00 — [Hook / what you'll learn]
[timestamps per major section]

────────────────────
🔗 TOOLS MENTIONED
────────────────────
[tool 1 with affiliate link if applicable]
[tool 2]

────────────────────
📺 WATCH NEXT
────────────────────
[related RecruiterGTM video URL]

────────────────────
📬 CONNECT
────────────────────
LinkedIn: https://linkedin.com/in/reyhankhann
Skool: https://skool.com/recruitergtm
Website: https://recruitergtm.com

#RecruitmentSystems #ClaudeCode #GTM
```

**Rules:**
- First 70 characters must contain the primary keyword. This is what ranks.
- Put Skool community link in the FIRST section (above the fold when expanded). Don't bury it.
- Timestamps only if video is 8+ minutes. Adds perceived value and boosts retention.
- "Watch next" link drives session time. Always include.
- Hashtags at the end only. 3 max. More than 3 gets suppressed.
- 300-500 words total in the description. Long enough for credibility without bloat.

---

## Thumbnail Strategy

**Specs:**
- 1280x720px (16:9)
- Under 2MB
- Must be readable at mobile size (5-inch screen ~ 10% of desktop view)

**MrBeast Formula (still valid in 2026):**
- One face
- One object / visual element
- One idea (1-2 words of text max)

**Reyhan-specific rules:**
- Brand colour: Violet Ray `#8A00FF` as the dominant accent
- Background: pure black or dark gradient (matches recruitergtm.com and landing pages)
- Face: Reyhan, closed-mouth / focused expression beats shocked-face by 15-20% CTR
- Text: 1-2 words MAX, bold sans-serif, thick stroke, white or violet
- High contrast between face and background — never a flat grey mid-tone
- Object: a specific symbol of the video (Claude logo, dashboard screenshot, octopus, etc.)

**Examples of good thumbnail text for our niche:**
- "AI OPS MANAGER"
- "CLAUDE CODE"
- "NO MORE MASS DMs"
- "$5K → FREE"
- "GTM ENGINE"
- "I QUIT OUTBOUND"

**Zoom-out test:** Preview the thumbnail at 10% size. If you can't read the text and recognise the subject, redesign.

---

## Thumbnail AI Tool Workflow

**Recommended stack (April 2026):**

| Tool | Best for | When to use |
|------|----------|-------------|
| **Ideogram 3.0** | Text rendering on image | Final step — the 1-2 word overlay. Renders text cleanly unlike Midjourney. |
| **Midjourney v7** | Artistic concept direction | First step — exploring 3-5 visual concepts for the video theme |
| **Nano Banana (Gemini 2.5 Flash Image)** | Fast realistic iteration | Best for photo-realistic faces + backgrounds. Fast enough for bulk generation. |
| **Canva Magic Studio** | Batch assembly + A/B variants | Final assembly — drop the generated image in, add Reyhan's face cutout + text |

**Founder workflow (Reyhan + Daniyal):**

1. **Reyhan:** Write the video title and pick the 1-2 word thumbnail text
2. **Daniyal / designer:** Generate 3 concepts in Midjourney (or Nano Banana for realistic)
   - Prompt template: *"YouTube thumbnail, [subject/object], dark background with violet glow #8A00FF, high contrast, cinematic lighting, 16:9 --ar 16:9 --v 7"*
3. **Daniyal:** Take best Midjourney output, drop into Ideogram with the 1-2 word text overlay
4. **Daniyal:** Assemble in Canva — add Reyhan's face cutout (use [remove.bg](https://remove.bg) or Canva's built-in), place text, export at 1280x720
5. **A/B test:** Upload 3 variants via YouTube's thumbnail test feature (now built into YouTube Studio)

**Alternative: Nano Banana only** — since Reyhan is using it for LinkedIn graphics, same workflow extends to YouTube. Nano Banana can generate the full thumbnail concept in one prompt if you include text instructions. Faster for a single-tool workflow.

---

## Tags

YouTube tags have lower ranking weight in 2026 than they did pre-2023, but still help with related-video surfacing and disambiguation for niche content.

**Tag strategy:**
- 1-2 broad tags (e.g., "recruitment", "AI for business")
- 3-4 niche tags (e.g., "claude code for recruiters", "recruitment GTM systems")
- 2-3 specific tags (video topic, tools mentioned)
- 1 brand tag ("RecruiterGTM", "Reyhan Khan")

**Total: 7-10 tags.** More than that dilutes signal.

---

## Pinned Comment Strategy

The pinned comment is prime real estate. Use it to:

1. Ask a direct question related to the video (drives comments)
2. Link to the Skool community or a related free resource
3. Include a keyword variant for SEO

**Template:**

```
If this resonated, the full system lives inside the RecruiterGTM community → https://skool.com/recruitergtm

Question for you: [specific question tied to the video topic]

Drop your answer below 👇
```

---

## End Screens & Cards

**End screen (last 20 seconds of video):**
- 1 slot: Subscribe button
- 1 slot: Related RecruiterGTM video (drives session time — algorithm gold)
- 1 slot: Link to skool.com/recruitergtm or recruitergtm.com/claude-code-dfy

**Cards (during video):**
- Mention a tool or previous video → drop a card pointing to it
- Max 3 cards per video. More feels spammy.

---

## LinkedIn Clip Ideas (Bonus Output)

Every YouTube video can be sliced into 3-5 LinkedIn posts. The skill outputs clip ideas with:

1. **Time range** in the video (e.g., 3:20 - 4:15)
2. **Hook** for the LinkedIn version
3. **Pillar** (Recruitment Systems / AI Opinion / etc.)
4. **Day suggestion** (Tuesday for Recruitment Systems, Wednesday for AI Opinion)

This feeds into the content-os skill to hit 5x/week LinkedIn posting without extra work.

---

## Output Format

When invoked, return a single structured block with all sections. Always end by asking which title Reyhan wants to go with so he can confirm before finalising the description.

---

## Quick Checks Before Publishing

- [ ] Title 50-60 chars, primary keyword in first 40
- [ ] Description first 70 chars has the hook + primary keyword
- [ ] Skool community link in first section of description
- [ ] Timestamps if video is 8+ minutes
- [ ] "Watch next" link at the bottom (session time)
- [ ] 7-10 tags
- [ ] Thumbnail readable at 10% zoom
- [ ] Thumbnail has 1-2 words of text max
- [ ] Pinned comment drafted
- [ ] End screen set up with subscribe + related video + external link
- [ ] LinkedIn clip plan exported to content-os queue

---

## Reference — Top Strategists to Model

| Strategist | Why model them |
|------------|----------------|
| **Paddy Galloway** | Packaging rigor. 30% time on ideation + packaging. Tested formats over invention. |
| **Jay Clouse (Creator Science)** | Email-first funnel for niche creators. YouTube is discovery, community is monetisation. Maps perfectly to RecruiterGTM → Skool. |
| **Matt Gray** | Content GPS framework. Batching system. 1 long-form → 25+ pieces. |
| **Dan Koe** | Profound message over production polish. iPhone + CapCut is enough. |
| **Sean Cannell (Think Media)** | Every video earns views independently. Don't rely on sub base. |

**Primary model for Reyhan:** Hybrid of Jay Clouse (email-first, community-funneled) + Paddy Galloway (packaging rigor) + Matt Gray (batching / Content GPS).
