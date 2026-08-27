# Newsletter Writer Skill

## What This Skill Does
Writes the RecruiterGTM beehiiv newsletter in Reyhan's exact voice and structure. Based on real sends (April 9 "Claude Cowork for Recruiters", March 10 "OutboundOS - The Lead Gen Engine for Recruiters").

## How to Invoke
Paste the topic + any source material (LinkedIn post, landing page, offer, demo video) + desired CTA → `/newsletter-writer`

## When to Use This Skill
- Any beehiiv newsletter send from `recruitergtm@mail.beehiiv.com`
- Weekly Wednesday newsletter slot
- Offer-driven broadcasts (DFY drops, community openings, product releases)
- Never freehand a newsletter. Always run through this skill.

---

## The Reyhan Newsletter Format

### Shape
Every newsletter follows the same 7-part shape. Keep the same order every time.

1. **Subject line** — short, benefit-led or curiosity-led. Hyphen with spaces separates the topic from the hook. Examples:
   - "Claude Cowork for Recruiters - Where to Start?"
   - "OutboundOS - The Lead Gen Engine for Recruiters"

2. **Opener stat + contrast line + analogy** — three lines, one per line. Stat grounds the claim. Contrast sets up the problem. Analogy makes it stick.
   - "43% of recruitment agencies are using AI in 2026."
   - "Most of them are using it to rewrite job descriptions and summarise CVs."
   - "That is like buying a Formula 1 car and using it to drive to Tesco."

3. **Setup paragraph** — 2-4 sentences. What we did, where, how many people saw it, why this email exists. Keep it matter-of-fact, not salesy.

4. **Numbered list (3-5 items)** — this is the spine. Each item:
   - `1. Title - short benefit line` (bold the whole line)
   - One short paragraph underneath (3-5 sentences max)
   - One concrete proof point with a number (candidates sourced, posts written, time saved)
   - Optional sub-bullets for sub-items using the `Thing: description` pattern

5. **"Why this matters now"** — one short paragraph. Usually another market stat (X% of talent leaders / agencies / founders) and a consequence line. Half fear of missing out, half data. Never doomer, never hype.

6. **The offer / giveaway** — one paragraph. Make it feel generous, not pitchy. Use "So what am I giving away here?" / "Here is what I am doing" / "So here is what you get" as the hinge line. CTA is either:
   - **Reply keyword CTA**: "Reply to this email with 'KEYWORD' and I will send you the link." (preferred — builds list warmth, lets Reyhan respond personally)
   - **Link CTA**: single bold link at the end

7. **PS + sign-off** — PS adds authority proof (e.g. "We are building this for 47 recruitment agencies inside RecruiterGTM"). Sign-off is casual and short: "Keep crushing!" / "Hope we get a sunny week" / "Speak soon". Then `Reyhan` on its own line.

---

## Voice Rules (Hard)

### Tone
- Smart practitioner talking to peers, not a consultant pitching down.
- British / neutral English. Use "summarise" not "summarize", "optimise" not "optimize", "agencies" and "founders" not "businesses."
- Dry humour early. The F1 / Tesco line, the "Terms and Conditions pop-up" line, the "Ferrari in your garage" line. Every newsletter should have one.

### Sentence rhythm
- First 3 lines of the body: one sentence per line. Punchy.
- Inside numbered list items: flowing short paragraphs, not bullet spam.
- Break walls of text with white space. Never a paragraph longer than 5 lines.

### Numbers
- Always contextualise a number. "600 lawyers in 8 minutes for a legal recruiter, around 75 profiles a minute." Never a naked "600 candidates."
- Reference real tools by name — Apollo, Clay, Apify, n8n, Exa, Lemlist, Skool, Claude Code. It signals you actually use them.

### What to avoid
- Em dashes. Zero or max one per newsletter. Use "." or " - " (hyphen with spaces) instead.
- Headings like `### Section`. This format uses bold-line numbers and one-line section cues, not markdown headers.
- Corporate speak: "leverage," "synergies," "unlock potential," "ecosystem" (unless quoting someone).
- AI slop: "what actually matters," "[X] is real" as a standalone, "the future of [industry]."
- Generic CTAs like "Let me know your thoughts." Always an action verb + keyword or link.
- Promising "booked calls." Always say "value-based conversations" or "conversations with decision makers."
- Emojis in the body. The content template doesn't use them. (Numbered emojis like 1️⃣ are fine in LinkedIn posts but NOT in the newsletter.)

### What to keep
- Specifics over abstractions. Named clients (when permitted), named tools, named stats.
- The PS — always present, always authority proof or community count.
- Casual sign-off. Never "Best regards."

---

## Length Target
- **400–500 words total body** (excluding subject and sign-off).
- If it's over 550, cut a use case or trim the setup paragraph.

---

## Cadence and Send Window
- **Target day:** Wednesday, 1 PM EST (same as April 9 Newsletter 3).
- **Cadence:** Weekly.
- **List source:** beehiiv, sent from `recruitergtm@mail.beehiiv.com`.

---

## Output Template

```
Subject: [Topic] - [Hook]

[Stat line.]
[Contrast line.]
[Analogy line.]

[Setup paragraph — 2-4 sentences about the context.]

[Transition line — e.g. "Here is what we covered" / "4 use cases stuck" / "Here are the three pillars."]

1. [Title] - [benefit line]
[Explanation paragraph with one concrete number or proof point.]

2. [Title] - [benefit line]
[Explanation paragraph with one concrete number or proof point.]

3. [Title] - [benefit line]
[Explanation paragraph with one concrete number or proof point.]

4. [Title] - [benefit line]
[Explanation paragraph with one concrete number or proof point.]

Why this matters now
[One paragraph with a market stat and a consequence.]

So here is what I am giving away
[Offer paragraph. Generous framing. Concrete value.]

Reply to this email with "[KEYWORD]" and I will [what happens next].

Ps: [Authority proof or community count.]

[Casual sign-off],
Reyhan
```

---

## Pre-Send Checklist
Before handing the draft off:
- [ ] Subject is under 60 characters and uses the hyphen-space pattern
- [ ] Opener is 3 lines (stat + contrast + analogy)
- [ ] Numbered list has 3-5 items, each with a specific number
- [ ] Every number has context (client, niche, per-minute rate, total count)
- [ ] Zero or one em dash total
- [ ] No markdown headers in the body (## / ###)
- [ ] No emojis in the body
- [ ] CTA is reply-keyword or single bold link — never both
- [ ] PS is present
- [ ] Sign-off is casual
- [ ] Word count 400-500
- [ ] Mentions a real tool by name at least once
- [ ] Mentions RecruiterGTM member count or a named client as proof

---

## Reference Archive

**Locked rule (2026-07-21): every sent newsletter gets archived in full, same day.** Beehiiv has no connector, so the archive only exists if we write it. When Reyhan confirms a send went out (or a draft is finalized for sending), save the FULL body + metadata (sent date, subject, topic, CTA, sign-off, notable mechanics) as `memory/wiki/references/reference_newsletter_<slug>.md`, add it to the list below, index it in `memory/wiki/index.md`, and log it in `memory/wiki/log.md`. If a newsletter was written in a session but never archived, that is a bug — the archive is the ground truth this skill drafts from.

Past newsletters stored in `memory/wiki/references/`:
- `reference_newsletter_march_10_2026.md` — "OutboundOS - The Lead Gen Engine for Recruiters"
- `reference_newsletter_april_9_2026.md` — "Claude Cowork for Recruiters - Where to Start?"
- `reference_newsletter_claude_ops_dfy.md` — "Claude Code Ops Manager. Done for you. Free." (the $1,497 offer-stack send: ✔️ inclusion list, $5k anchor, deadline mechanics)
- `reference_newsletter_mastermind_2026.md` — "My 2026 Manifestation" (Lisbon Mastermind: category-contrast opener, DFY deliverables, scarcity PS)
- `reference_newsletter_reoffer_july_2026.md` — "20th July - ReOffer" (last-chance $1,497 send: list-only structure, two-layer inclusion stack, DIY/DWY/DFY separation as the honest deadline reason, April-send callback PS)

**Finalized newsletters live in the "Newsletter Emails" Google Doc** (Drive id `1XledtJe73dzKoiDzD0tsxYyb5UhxxKJL1vhFi5QsEuk`), newest section at the bottom. ALWAYS read its latest section before drafting or repurposing any newsletter — then archive per the locked rule above.

Always read at least one of these before drafting, to anchor the voice.

### Rule correction from the real sends (2026-07-19)
The "no emojis in the body" rule is WRONG against the archive: the Claude Ops DFY send uses 1️⃣2️⃣ numbered emojis and a ✔️ inclusion list. Corrected rule: **no decorative emojis, but 1️⃣2️⃣3️⃣ for numbered feature lists and ✔️ for inclusion stacks are house style in offer-driven sends.** The real sends are ground truth over this file when they conflict.
