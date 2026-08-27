# Q&A Deck Generator Skill

Generate the weekly RecruiterGTM Community Q&A presentation deck — dark theme (locked 2026-07-08), 1280×720 screen-share ratio, anchored to OperatorOS classroom material, with interactive audience polls baked in.

## How to Invoke
`/qa-deck-generator` followed by:
- Topic + date, OR
- Recent context (yesterday's Skool post, a specific OperatorOS module the talk extends)

---

## Locked Rules

### A. Cadence + format
- A0. **DEFAULT FORMAT = the flowing "proposal-style" layout, NOT fixed 1280×720 slides (Reyhan 2026-08-19).** Fixed-height slides kept squeezing/cutting text at the bottom, so the standing preference is now the proposal structure: a centered column (`max-width ~900px`, `margin:0 auto`), `.sec` blocks that are `min-height:100vh` + flex-centered (present like slides when scrolled full-screen) but **auto-grow with content so nothing is ever clipped**, generous padding (~110px top/bottom), centered headings/eyebrows/leads, DM Sans body + Space Grotesk display, dark violet gradient bg. Reyhan presents the **HTML** full-screen by scrolling (same as he opens proposals). **Canonical template: `~/Desktop/Community-Decks/weekly-qa/2026-08-19-new-era-outbound/deck.html`** — copy its CSS. Section count is flexible in this format (the 8–10 cap in A2 was for fixed slides). Only build fixed 1280×720 slides (Section C) if Reyhan explicitly asks for that old format. When exporting a PDF from the flowing format, add a `@media print` block that re-asserts multi-column grids (`.grid.g2/g3`, `.loop` with `!important`) — Chrome's print viewport otherwise fires the mobile breakpoint and collapses + clips them.
- A1. RecruiterGTM Weekly Q&A runs every Wednesday, 4:30–6:00 PM UK. The deck is for screen-share during the live call.
- A2. **8–10 slides per deck.** Mini format. Cover + 6–8 content + Resources close. (Applies to the legacy fixed-slide format; the flowing default in A0 has no slide cap.)
- A3. **1280×720 slide size** (16:9, fills Zoom/Google Meet share at full screen). (Legacy fixed-slide format only — see A0.)
- A4. **Always export both HTML + PDF.** HTML for editing, PDF for screen-share.
- A5. **Output folder:** `~/Desktop/Community-Decks/weekly-qa/YYYY-MM-DD-topic-slug/` with `deck.html` + `deck.pdf` inside.
- A6. **Every deck's copy is written to ContentOS rules and style, every time. Non-negotiable (Reyhan 2026-08-12).** Before rendering, run ALL slide copy — titles, body, cards, callouts, poll options — through `content-os/SKILL.md`: obey the Section A–M rejection rules (banned words incl. ship / guessing / leverage / robust / seamless / "real"-as-filler / "moat" & idioms; banned fragment patterns like "That is it." / "X is real."; hollow-line check; ≤1 prose em dash), practitioner voice, plain 60/40 US–UK English, real numbers + real names. Then run the humanizer + the Section M final-pass checklist. Deck copy is copy; the CORE "always invoke the writing skill" rule applies. Never ship a raw first draft. After the pass, self-audit with a grep for banned words + em dashes before declaring the deck ready.
- A7. **Footer clearance is mandatory — this keeps recurring, so treat it as a hard gate.** The brand mark + slide number sit at `bottom:22px` (baseline ≈ y698). Every slide MUST reserve `padding-bottom:96px` on `.slide` so the content box ends at y624, and **no content may cross y624**. Mechanical check before shipping: render EVERY slide to PNG (`pdftoppm -png -r 96`) and confirm the lowest content element (banner, callout, foot-note, table, last card) has a **clear visible gap above the brand mark** — its bottom edge must sit at ~y630 or higher, never touching the `RecruiterGTM` text. If ANY slide crosses it, the slide is overfull: FIX by cutting content, not by shrinking padding — shorten copy, drop a table row, fold trailing foot-notes up into the intro/sub line, or reduce a dense block's font (e.g. a `.small` prompt variant). Re-render and re-check. A trailing free-flow `.foot-note` right under a tall table/callout is the usual culprit — either give it clear room or remove it. Never tell Reyhan a deck is ready until this PNG check passes on all slides. (Failed 2026-08-12 logo-over-text; again 2026-08-19 slide-6 foot-note over brand.)
- A8. **The bottom "lesson / CTA" banner gets real height** — never a thin cramped strip. Give it `min-height` (~96px+), 19–20px text, generous padding, and pin it to the bottom of the content area (`margin-top:auto`). It carries the single most important line of the slide. Include a short tag chip (e.g. "Lesson", "Do this", "Your homework").

### B. Interactive polls (mandatory — 2–3 per deck)
- B1. Every Q&A deck MUST include **2–3 interactive poll slides** distributed across the deck (not all at the end).
- B2. **Always one poll early** (slide 2 or 3) to get the audience warm and engaged.
- B3. **Always one poll late** (before Resources) to drive a conversation that bleeds into open Q&A.
- B4. Poll format: a single direct question + 3–5 short response options + "Respond in the chat with the number" CTA.
- B5. Poll slides have a distinct visual style — yellow/amber accent stripe + eyebrow "Audience Poll" — so attendees see it's their turn to engage.
- B6. Poll questions are conversational, not yes/no. "How many team members do you have? Solo · 2 · 3 · 4 · 5+" beats "Do you have a team? Yes/No."

### C. Visual design system (locked — DARK theme per Reyhan 2026-07-08; light theme retired)
Tokens (use exactly):
- `--violet: #B44DFF` (accent/text on dark — readable violet)
- `--violet-deep: #8A00FF` (fills: numbered circles, solid accents)
- `--violet-bg: #221238` (violet-tinted card/strip background)
- `--ink: #FFFFFF` (headings)
- `--ink-soft: #C9C9CE` (body text)
- `--mute: #8E8E96`
- `--bg: #101014` (slide background)
- `--card: #1A1A20`
- `--divider: #2A2A32`
- `--poll-amber: #F59E0B`
- `--poll-amber-bg: #1C1508` (dark amber-tinted poll slide background)
- Table headers: `#26262E` background, white text (never a `var(--ink)` fill on dark — ink is now white)
- Page background around slides: `#050506`; dot-grid: `rgba(180,77,255,0.07)`
- Reference dark deck: `~/Desktop/Community-Decks/weekly-qa/2026-07-08-database-reactivation/deck.html` (first dark deck — copy its CSS, not the old light lean-operator deck's)
- Logo note: dark backgrounds pair with the violet "Transparent Icon.png" per `reference_recruitergtm_logo_path.md`
- Font: Montserrat (300, 400, 500, 600, 700, 800, 900)

Slide chrome:
- Brand mark `RecruiterGTM` bottom-left in violet uppercase
- Slide number `01 / 09` bottom-right in mute
- Subtle dot-grid background pattern (radial-gradient at 38px spacing)
- `eyebrow` label at top of every content slide (violet, uppercase, 3px letter-spacing)

### D. Standard slide structure (8–10 slides)
1. **Cover** — title + eyebrow (e.g. "OperatorOS · Q&A") + date + host
2. **Setup / Hook** — frames why this topic matters. Often a Before/After or yesterday's Skool post reference.
3. **Poll #1 (audience warm-up)** — light, builds engagement (e.g. "How many team members do you have?")
4. **Core Framework #1** — quadrant, table, or X/Y graph (see Section E for visuals)
5. **Core Framework #2** — supporting framework or list
6. **Poll #2 (mid-deck)** — sharper question tied to the topic
7. **Core Framework #3** — playbook, timeline, or table
8. **Poll #3 (optional, late)** — bleeds into open Q&A
9. **Resources** — OperatorOS modules + template links + DM CTA
10. **Final slide** — open Q&A invitation, single line ("Bring your questions.")

Adjust depending on topic — but always keep **at least 2 polls** distributed across the deck.

### E. Visual patterns (reusable)
**Quadrant (2×2 cards):** for splitting a concept into 4 zones — e.g. functions, decision matrices.
**X/Y axis graph:** for plotting items against two dimensions. MUST have visible axis lines, labelled endpoints, plotted points with dots + name labels. Not just 4 boxes — a real graph.
**Hire-order / system table:** numbered rows, role/name/range columns. Used for the "people" or "systems" slides.
**Two-column compare:** Before/After or You-Keep/You-Hand-Off splits. Card on left (neutral), card on right (violet-accented = where you want them to land).
**Timeline (4-column):** M1-3 / M4-6 / M7-9 / M10-12 cards. Final cell uses violet-accent for the payoff.

### F. Anchor to OperatorOS content (do not invent frameworks if one already exists)
Before drafting any deck, check `~/Desktop/Skool Courses/operator-os.html` for relevant existing language. Reuse:
- "From Operator to Lean Operator"
- "Stay the operator. Stop being the implementer."
- "Two calls a week. That's the cadence." (Mon + Fri)
- "Daily EOD reports tie it together. No standups."
- "Three workspaces. One operating system." (Team Tasks · CEO Tasks · Content Tracking in Pulse)
- "Three tools. That's it." (Pulse + Slack + Claude Code)
- "Freedom is the KPI."
- "5 MITs" (Most Important Tasks)
- "High / Medium / Low and the art of saying no"

Always close the Resources slide with the relevant OperatorOS Module(s).

### G. Poll slide HTML template
Use this exact structure for poll slides — distinctive amber styling so attendees know to respond:

```html
<div class="slide poll-slide">
  <div class="poll-stripe"></div>
  <div class="eyebrow poll-eyebrow">Audience Poll</div>
  <h1 class="poll-question">[QUESTION HERE]</h1>
  <div class="poll-options">
    <div class="poll-option"><span class="poll-num">1</span><span class="poll-label">Solo</span></div>
    <div class="poll-option"><span class="poll-num">2</span><span class="poll-label">2 people</span></div>
    <div class="poll-option"><span class="poll-num">3</span><span class="poll-label">3 people</span></div>
    <div class="poll-option"><span class="poll-num">4</span><span class="poll-label">4 people</span></div>
    <div class="poll-option"><span class="poll-num">5</span><span class="poll-label">5+</span></div>
  </div>
  <div class="poll-cta">Respond in the chat with the number that matches you.</div>
  <span class="brand">RecruiterGTM</span>
  <span class="slide-num">XX / YY</span>
</div>
```

Poll-specific CSS (add to deck styles):

```css
.poll-slide { background: var(--poll-amber-bg); }
.poll-stripe { position: absolute; top: 0; left: 0; right: 0; height: 6px; background: var(--poll-amber); }
.poll-eyebrow { color: var(--poll-amber); letter-spacing: 3px; }
.poll-question { font-size: 56px; font-weight: 800; line-height: 1.1; letter-spacing: -1.5px; color: var(--ink); margin: 30px 0 40px; max-width: 1000px; }
.poll-options { display: grid; gap: 14px; max-width: 700px; margin-bottom: 36px; }
.poll-option { display: flex; align-items: center; gap: 18px; background: #fff; border: 1.5px solid var(--divider); border-radius: 12px; padding: 16px 22px; }
.poll-num { display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 50%; background: var(--poll-amber); color: #fff; font-weight: 800; font-size: 16px; }
.poll-label { font-size: 18px; font-weight: 700; color: var(--ink); }
.poll-cta { font-size: 15px; color: var(--ink-soft); font-style: italic; }
```

### H. How to apply

1. **Confirm topic + date + tie-in.** Ask Reyhan if it ties to yesterday's Skool post, a specific OperatorOS module, or a new angle.
2. **Read the relevant OperatorOS section.** Pull existing frameworks rather than inventing.
3. **Propose the 8–10 slide structure** with poll placements highlighted. Wait for approval before building.
4. **Build the HTML** using the locked design tokens (Section C) and visual patterns (Section E).
5. **Render to PDF** via Chrome headless:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf="<output>/deck.pdf" \
     "file://<output>/deck.html"
   ```
6. **Save both files** to `~/Desktop/Community-Decks/weekly-qa/YYYY-MM-DD-topic-slug/`.
7. **Tell Reyhan the deck is ready** with the path. Don't auto-open per `feedback_never_auto_open_files.md`.

### I. Poll question library (steal from this list when the topic fits)

**Audience size / stage:**
- "How many team members do you have? Solo · 2 · 3 · 4 · 5+"
- "How long have you been running your agency? <1yr · 1-3yrs · 3-5yrs · 5-10yrs · 10+yrs"
- "Where are you in the AI adoption curve? Haven't touched it · Experimenting · Daily use · Running automations · Full Claude Ops Manager"

**Pain / bottleneck:**
- "What's your biggest bottleneck right now? Lead gen · Sourcing · Fulfilment · Content · Ops"
- "When was the last time you took a full week off? Never · 6+ months ago · 3-6 months · 1-3 months · This year"
- "What do you spend most of your week doing? Selling · Recruiting · Managing the team · Doing the work yourself · Admin"

**Buy-in / readiness:**
- "What would you delegate first? Outbound · Sourcing · Content · Ops · Sales"
- "Which feels harder right now — hiring or automating? Hiring · Automating · Both equally · Neither"
- "If you had $4k/mo to hire one person, would you hire? Recruiter · GTM Engineer · Ops Manager · Content Manager · No one — automate instead"

**Confidence / commitment:**
- "By end of Q3, you will have: Hired 1 new person · Automated 1 workflow · Both · Neither · Already done both"

### J. Output checklist before shipping

- [ ] Cover slide has eyebrow, title, date, host name
- [ ] 2-3 poll slides distributed (not clustered at end)
- [ ] At least one visual framework (quadrant, X/Y graph, or compare)
- [ ] All slides have brand mark + slide number
- [ ] Resources slide names specific OperatorOS modules
- [ ] PDF renders cleanly at 1280×720 (open it, scroll through)
- [ ] No invented stats — every number traces back to context files, memory, or Reyhan's input
- [ ] Slide count between 8 and 10

---

## Reference deck (canonical example)

`~/Desktop/Community-Decks/2026-06-03-lean-operator-qa/deck.html`

The Lean Operator Q&A deck (3 June 2026) is the canonical reference. It demonstrates:
- The "Stay the operator, stop being the implementer" frame
- 2×2 quadrant (functions you keep strategy on vs. hand off implementation)
- Real X/Y axis graph with plotted points (NOT 4 boxes)
- Numbered systems list with ATS first
- Firefighting table with named owners
- 4-column timeline with violet-accented payoff cell
- OperatorOS Module 2 / 5 / 6 anchored on Resources slide

Future decks borrow CSS + visual patterns from this file.
