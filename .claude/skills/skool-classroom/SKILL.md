---
name: skool-classroom
description: Generate or edit Skool classroom HTML for the four RecruiterGTM courses (OperatorOS, OutboundOS, RecruiterOS, ContentOS). Locks the canonical module list per course. Invoke before adding, removing, or restructuring any classroom module.
---

# Skool Classroom Skill

> ⚠️ **SUPERSEDED (2026-07-07) — canonical structure now lives in `community-os`.** The four-course canon (OperatorOS/OutboundOS/RecruiterOS/ContentOS) is dissolved into ONE course, "The RecruiterGTM System" (5 stages × 25 modules, Engine Framework). For ANY structure question or community task, invoke `/community-os`. The HTML build rules below (two-location sync, light theme, TOC discipline) remain valid and are duplicated in community-os Locked Rules §E.

The single source of truth for what each RecruiterGTM Skool course contains. Stops module drift (the "did we have 6 or 10?" problem) by locking the canonical structure of every course.

---

## Locked Rules

### A. Two-location sync (mandatory after every edit)
- A1. Skool course files exist in TWO locations and BOTH must stay in sync.
  - **Source of truth (where to edit):** `projects/skool-courses/<course-name>/<file>.html`
  - **Where Reyhan opens the file:** `~/Desktop/Skool Courses/<file>.html`
- A2. After EVERY edit to any file under `projects/skool-courses/`, immediately `cp` it to the matching path under `~/Desktop/Skool Courses/`. Same for any associated assets (e.g. the `visuals/` directory).
- A3. Pattern mirrors proposals (edit in `projects/`, sync to `~/Desktop/proposals/`). Same rule applies to anything Reyhan opens from his Desktop.
- A4. Reyhan flagged May 3 2026 — hours of edits went unseen because the Desktop copy wasn't synced. Wasted time and broke trust. Never again.

---

## When to invoke

- Adding, removing, or restructuring any classroom module
- Building a new course HTML from scratch
- Editing slide/section content inside an existing course
- Answering "how many modules does X have"
- Before any `Edit` or `Write` against a file in `projects/skool-courses/`

## Hard rules — do NOT break these

1. **Never add a module** to any course without explicit ask from Reyhan. If a draft "feels short" or you think a topic is missing, raise it as a question — do not add it silently.
2. **Never remove a module** without explicit ask. If a section feels redundant, propose a merge in chat first.
3. **Never renumber modules** silently. If renumbering happens, update the TOC and every `<!-- MODULE N —` comment AND every `Module N Recap` header in the same change.
4. **TOC must match body.** After every edit, grep `<!-- MODULE \d+` and TOC card count — they must agree.
5. **Bonus library content (Operator's Library, Tyson Franco shout-out) is a separate bonus card, not a module.** Don't number it.
6. **Sync rule:** every edit to `projects/skool-courses/<course>/<file>.html` must be copied to `~/Desktop/Skool Courses/<file>.html` immediately.
7. **Light theme.** All four courses use the light theme: `--bg: #FAFAF7; --ink: #0A0A0A; --card: #FFFFFF; --violet: #8A00FF`. Never write white text on tinted backgrounds. Inline cards use solid white backgrounds with coloured borders + dark text.

## Canonical module lists

The course-specific files in this skill folder hold the locked module list per course:

- [OPERATOROS.md](OPERATOROS.md) — 7 modules + bonus (locked May 5 2026)
- [OUTBOUNDOS.md](OUTBOUNDOS.md) — pending Reyhan confirmation
- [RECRUITEROS.md](RECRUITEROS.md) — pending Reyhan confirmation
- [CONTENTOS.md](CONTENTOS.md) — pending Reyhan confirmation

**Read the relevant course file FIRST** before any classroom edit. If the canonical list is marked "pending confirmation", surface that to Reyhan before editing.

## File locations

| Asset | Path |
|---|---|
| Source HTML | `projects/skool-courses/<course>/<course>.html` |
| Live mirror | `~/Desktop/Skool Courses/<course>.html` |
| Visuals | `projects/skool-courses/<course>/visuals/` |
| Backups | none — rely on git for recovery |

## Locked Design System (use OperatorOS as the canonical source)

Every classroom HTML — and every standalone deck — MUST match OperatorOS's exact visual system. No ad-libbing fonts, no extra type families, no different card radii. Copy the system below verbatim.

### Fonts — Montserrat ONLY

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
```

- **NEVER add Syne, Inter, JetBrains Mono, or any other font family.** Montserrat only, weights 300-900.
- Body uses `font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;`
- All headings (h1, h2, h3) also use Montserrat. Style differentiation comes from weight + size, not family.

### CSS variables (exact)

```css
:root {
  --violet: #8A00FF;
  --ink: #0A0A0A;
  --ink-soft: #2A2A2A;
  --mute: #6E6E73;          /* not --muted */
  --bg: #FAFAF7;
  --card: #FFFFFF;
  --divider: #E5E5E0;       /* not #E5E5DF */
}
```

### Container + section pattern

```css
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 48px; }
section { padding: 90px 0; border-top: 1px solid var(--divider); }
```

- Width is **1080px**, padding **48px**. Not 900, not 32.
- Sections separated by `border-top: 1px solid var(--divider)` — NOT by card wrappers. White space + hairline divider is the structure.

### Typography scale (uses clamp for responsive)

```css
.hero h1 { font-size: clamp(52px, 8vw, 96px); font-weight: 800; line-height: 1.02; letter-spacing: -2px; }
h2       { font-size: clamp(34px, 4.5vw, 52px); font-weight: 700; letter-spacing: -1px; line-height: 1.1; }
.module-divider h1 { font-size: clamp(48px, 7vw, 88px); font-weight: 800; letter-spacing: -1.5px; }
.big-idea p { font-size: clamp(28px, 3.5vw, 42px); font-weight: 600; }
.quote blockquote { font-size: clamp(24px, 3vw, 34px); font-weight: 600; }
.hero .sub { font-size: 22px; color: var(--mute); max-width: 720px; }
.point p { font-size: 19px; color: var(--ink-soft); }
.recap li { font-size: 18px; color: var(--ink-soft); }
.col li { font-size: 16px; color: var(--ink-soft); }
```

### The violet `<em>` trick

Every h1 and h2 can have `<em>...</em>` tags to highlight key words in violet. The `em` tag is styled, not italicised:

```css
h1 em, h2 em, .big-idea p em, .module-divider h1 em { color: var(--violet); font-style: normal; }
```

Use it sparingly — one or two `<em>` tags per heading max. It's an accent, not a stripe.

### Eyebrow (section label) — always above h2

```css
.eyebrow {
  font-size: 12px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--violet);
  font-weight: 700;
  margin-bottom: 20px;
}
```

### Canonical components — use these, don't invent new ones

| Component | Use | Pattern |
|---|---|---|
| `.points` + `.point` | Numbered list of 5-8 items (most common) | Violet 2-digit number + ink-soft 19px body |
| `.compare` grid + `.col.bad` / `.col.good` | Old way vs new way | 2-column white cards, 8px radius, 36px padding |
| `.big-idea` | The headline statement of a module | Black background, white text, violet `<em>` accents, 80px padding |
| `.quote` | Real quote with attribution | White card, left-border violet 3px, 8px radius |
| `.recap` | Module recap, numbered list | White card, 48px padding, auto-counter with violet 2-digit numbers |
| `.module-divider` | Hero between modules | Full-bleed, gradient bg, violet pill tag, massive h1 |
| `.usecase-card` | Live demo walkthrough | White card, head + grid (What you'll see / Inputs→Outputs) + Why this matters |
| Your Task callout | Mandatory before recap | White card, violet 1.5px border, 14px radius, violet pill title |

### Border radius rules

- Cards: **8px** (`.col`, `.quote`)
- Larger boxed sections: **12px** (`.big-idea`, `.recap`)
- Task callouts: **14px**
- NEVER 16px, 18px, or "rounded-2xl" style modern radii. The aesthetic is sharp, slightly softened.

### Spacing rules

- Section vertical padding: **90px**
- Hero: **140px 0 120px**
- Module-divider: **180px 0 120px**
- Card internal padding: **36px** (compare cols) / **48px** (recap, quote) / **80px 60px** (big-idea)
- Grid gap between cards: **24px**

### Banned anti-patterns

- Multiple font families (Syne, Inter, JetBrains, etc.)
- Card wrappers for every section (use `border-top` dividers instead)
- Border radius > 14px
- Letter-spacing 0 on display headings (must be negative)
- Light-grey body text under 16px (use `--ink-soft` or `--mute` at proper sizes)
- Solid violet section backgrounds (violet is for accents only — text, borders, eyebrows, `<em>`)
- "Hero" patterns that aren't `padding: 140px 0 120px` with eyebrow + h1 + sub

### Before any classroom or deck HTML edit

1. Open OperatorOS HTML in the editor as a reference. Copy patterns from it.
2. Use the same `<style>` block tokens. Do not invent new ones.
3. Use existing component classes (`.points`, `.compare`, `.recap`, `.big-idea`, `.quote`). Build new ones only if no existing class fits.
4. If you find yourself adding a `<link>` to a new font, stop. Use Montserrat with a different weight.

---

## Standard course HTML structure

Every course HTML follows the same skeleton:

```
1. <head> — light-theme CSS variables, Montserrat + Syne fonts
2. <section class="hero"> — course title + tagline
3. <section> "What you will learn" — 5–7 bullets
4. <section> Table of Contents — N module cards + bonus card
5. Module 1
   - hero: "Module 01" eyebrow + h1 + sub
   - "We will cover" bullets
   - body sections
   - "Your Task This Week" callout (mandatory on every module)
   - Module Recap section
6. Module 2 ... Module N (same pattern)
7. Bonus section(s) (optional)
8. Footer
```

## Mandatory section: Your Task This Week

Every module MUST end with a `Your Task This Week` callout immediately before the recap. Pattern:

```html
<section>
  <div style="margin-top:8px; padding:28px; background:#FFFFFF; border:1.5px solid #8A00FF; box-shadow: 0 1px 0 rgba(0,0,0,0.04); border-radius:14px;">
    <div style="display:inline-block; font-size:11px; font-weight:800; letter-spacing:0.12em; color:#fff; background:#8A00FF; text-transform:uppercase; padding:5px 10px; border-radius:6px; margin-bottom:14px;">&#9989; Your Task This Week</div>
    <h3 style="font-size:22px; color:#0A0A0A; margin-bottom:12px; line-height:1.3; font-weight:800;">[Action verb + concrete deliverable]</h3>
    <p style="font-size:14.5px; color:#2A2A2A; line-height:1.65; margin-bottom:14px;">[2-4 sentences: exactly what to do, in what order, on what tools]</p>
    <p style="font-size:13px; color:#6E6E73; line-height:1.6; margin:0;">Post [evidence] in the Skool community. Tag @Reyhan for [review type].</p>
  </div>
</section>
```

## Mandatory section: Module Recap

Every module ends with a recap directly after the task callout. Pattern:

```html
<section>
  <p class="eyebrow">Module N Recap</p>
  <h2>What we covered.</h2>
  <div class="recap">
    <ol>
      <li>[5-8 numbered bullets — one per substantive section in the module]</li>
    </ol>
  </div>
</section>
```

The recap line count must roughly match the section count of the module. If you merge two modules into one, the merged recap must combine bullets from both.

## Pre-edit checklist

Before touching any classroom HTML:

1. Read `SKILL.md` (this file)
2. Read the relevant `<COURSE>.md` for the canonical module list
3. Read the actual course HTML to see current state
4. If the user is asking to add/remove/renumber modules: confirm first
5. If the canonical list is "pending confirmation": ask Reyhan to confirm before editing

## Post-edit checklist

After every classroom HTML edit:

1. Grep `<!-- MODULE \d+ —` — count must match the canonical list
2. Grep `Module \d+ Recap` — count must match module count
3. Grep `Your Task This Week` — count must match module count
4. Visual TOC card count must match module count + bonus
5. Copy file to `~/Desktop/Skool Courses/<file>.html`
6. Confirm change to Reyhan with file path — do NOT auto-open

## Voice / tone

- Light theme, generous white space, no corporate fluff
- Practitioner voice — same as the LinkedIn content rules
- Real numbers, real names (Salar, Shmookh, Daniyal, Reyhan), real tools
- Banned phrases: "leverage", "transformative", "ensures", "amplifies"
- No emojis in body copy except the violet checkmark in Task callouts and the giveaway gift icon

## Common mistakes that have shipped — do not repeat

1. **Adding modules silently.** OperatorOS drifted from 6 to 10 modules without anyone asking — that's how this skill exists.
2. **TOC out of sync with body.** Catch with the grep checks above.
3. **Light theme + dark inline cards.** White text on `rgba(R,G,B,0.10)` backgrounds is invisible. Always use solid white cards with coloured borders.
4. **Forgetting the sync to `~/Desktop/Skool Courses/`.** Reyhan records from the Desktop copy, not the Drive copy. Both must match.
5. **Inventing client onboarding / internal-process modules.** This is a course for recruitment agency owners. Not a manual for our internal RecruiterGTM ops. If a topic is "how WE serve clients" rather than "how YOU run YOUR business", it does not belong.
