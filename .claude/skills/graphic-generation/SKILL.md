# Graphic Generation Skill

Generate LinkedIn post graphics for RecruiterGTM.

---

## CHOOSE THE RIGHT ENGINE FIRST (read before anything)

There are TWO graphic engines. Picking the wrong one produces garbage.

| If the graphic is… | Use | Why |
|---|---|---|
| **An illustration / mascot / character / scene / anything that should look "designed" or "drawn"** (e.g. "Claude wearing a headset", a logo personified, a concept illustration) | **Nano Banana — `mcp__gemini-image__generate_image`** (Gemini 2.5 Flash Image) | Hand-coded SVG of a character ALWAYS looks stiff and amateur. Image models are built for this. |
| **A data / diagram / system graphic** — the variation-10 solar-system hub, power bars, tool→skill maps, stat cards, list grids | **HTML + inline SVG** (the rest of this skill) | Precise layout, exact text, charts. SVG is right here. |

**Hard rule (flagged 2026-06-22):** never hand-code SVG for an illustrated/mascot concept. Reyhan rejected hand-built SVG mascots — correctly. Default illustration work to Nano Banana.

**Nano Banana usage:** `mcp__gemini-image__generate_image`, `aspect_ratio: "4:5"`, save to `~/Desktop/linkedin-graphics/*.png`. Write rich art direction (subject, style, lighting, palette, composition, negative space). Text renders unreliably — leave space and overlay copy after, or regenerate.

**Known blocker:** the `gemini-image` key needs **billing enabled** — free tier = 0 image requests/day, returns HTTP 429 `limit: 0`. If you hit that, STOP and flag it; do NOT fall back to hand-coded SVG for an illustration.

---

## How It Works (HTML/SVG engine — for data/diagram graphics only)

Graphics are built as self-contained HTML files with inline SVG. This gives full control over gradients, glow effects, bezier curves, segmented bars, and precise typography. Output opens directly in the browser for review and can be screenshotted or exported for LinkedIn.

**Output format:** HTML file saved to `~/Desktop/linkedin-graphics/`
**Canvas size:** 1080 x 1350px (4:5 ratio for LinkedIn feed posts)
**Open with:** `open [filename].html` to preview in browser

---

## Brand Guidelines

**Primary colour:** Violet Ray — `#8A00FF` (RGB: 138, 0, 255)
**Secondary:** Black — `#000000`
**Aesthetic:** Dark, minimal, modern — never corporate, never stock photo
**Typography:** Helvetica Neue / Helvetica / Arial (system sans-serif), bold numbers, white text on dark backgrounds
**Brand mark:** "RecruiterGTM" wordmark at bottom of every graphic in violet gradient

### Colour Flexibility Rules

Violet is the brand anchor — it does NOT need to dominate every graphic. Use it as an accent, not wallpaper.

**Approved background palettes:**
- Pure black `#08080e` or `#0a0a0a` — extreme minimalism
- Dark navy `#0d1117` — futuristic/tech
- Charcoal `#1a1a1a` — warm dark
- Off-white / cream — for list/grid posts (Matt Gray Founder OS style)

**Accent colour options (one per graphic max):**
- Violet `#8A00FF` — brand default
- Electric lime `#BFFF00` — high contrast, stop-scroll energy (use sparingly)
- Amber/gold `#FFB700` — warmth, for personal/journey posts
- Cyan `#00C8FF` — tech/data feel
- White only — for extreme minimalism

**The rule:** restraint is premium. One accent colour. Maximum two colours total (background + accent). The less colour, the more confident the graphic looks.

**Reference styles:**
- Matt Gray minimalism: pure black bg + one accent dot/shape + single line of text
- ColdIQ illustrated infographic: rich concept visual + brand colour + clear hierarchy
- Matt Gray grid: light bg + bold headline + icon grid

---

## LinkedIn Post Graphic Specs

| Use case | Dimensions | Aspect ratio |
|----------|-----------|-------------|
| Feed post (standard) | 1080 x 1350 | 4:5 |
| Landscape / article header | 1920 x 1080 | 16:9 |
| Square | 1080 x 1080 | 1:1 |

Default to 1080 x 1350 (4:5) unless told otherwise.

---

## Approved Design: Solar System Hub (Variation 10)

This is the winning design style. Use it as the base for all system/tool/workflow graphics.

### Structure

```
┌──────────────────────────────────────┐
│           TITLE (gradient)           │
│           Subtitle                   │
│                                      │
│  CONNECTORS    ☀ CLAUDE    SKILLS    │
│  ┌─────────┐   (sun)   ┌──────────┐ │
│  │ Apollo   │──╮     ╭──│ 01 Skill │ │
│  │ Clay     │──┤  ●  ├──│ 02 Skill │ │
│  │ Apify    │──┤     ├──│ 03 Skill │ │
│  │ SalesQL  │──╯     ╰──│ 04 Skill │ │
│  └─────────┘           └──────────┘ │
│  ─────────── divider ───────────── │
│         POWER BARS (gaming)         │
│  Metric 1  ████████████░░  Label    │
│  Metric 2  █████████░░░░░  Label    │
│  Metric 3  ████████░░░░░░  Label    │
│  Metric 4  ██████████░░░░  Label    │
│                                      │
│         [ CTA PILL BUTTON ]          │
│         recruitergtm.com/xxx         │
│                                      │
│           RecruiterGTM               │
└──────────────────────────────────────┘
```

### Key Visual Elements

**Central Sun (Claude/Hub):**
- Radial gradient: `#B44DFF` → `#8A00FF` → `#5500AA`
- Multiple glow layers (radialGradient with opacity falloff)
- Inner ring (white, 0.15 opacity)
- Dark core with label text
- 3 pulse rings expanding outward (decreasing opacity)
- 2 orbital ellipses behind (0.05-0.08 opacity)

**Connector Pills (left side):**
- Rounded pill shape (rx="28"), 175x56
- Background: `linear-gradient(#1a1a24, #12121a)`
- Border: `#8A00FF` at 0.5 opacity
- Glowing dot indicator (circle with `feGaussianBlur` filter)
- Tool names: Apollo, Clay, Apify, SalesQL (or swap per post context)

**Skill Pills (right side):**
- Same pill shape as connectors
- Border: `#8A00FF` at 0.7 opacity (slightly brighter)
- Numbered: 01, 02, 03, 04 in `#B44DFF`
- Skill names adapt per post topic

**Bezier Curves:**
- Connect pills to central sun using cubic bezier `<path>` elements
- Left curves: gradient from 0.1 → 0.6 opacity (fades in toward centre)
- Right curves: gradient from 0.6 → 0.1 opacity (fades out from centre)
- Small endpoint dots (3px circles) at curve origins
- Stroke width: 1.8px

**Power Bars (gaming health bars):**
- 4 bars, each a different accent colour (violet, lime, amber, cyan)
- Track: dark `#0e0e18` with `#1e1e2e` border, 18px height, rounded
- Fill: linear gradient (dark → mid → bright for each colour)
- Glow filter on each fill (`feGaussianBlur` + `feFlood` composite)
- Segmented look: repeating pattern mask (11px solid + 3px gap)
- Shine highlight: thin white bar (0.1 opacity) across top of fill
- Left label: metric name (13px, white)
- Right label: result/stat (11px, accent colour)

**Dot Grid Background:**
- Radial gradient dots, 50x50 spacing, 0.8px radius, `#1a1a28`
- Opacity: 0.35-0.4

### HTML Template Structure

```html
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #000; }
.canvas {
  width: 1080px; height: 1350px;
  background: #08080e;
  position: relative; overflow: hidden;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
.canvas::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  background-image: radial-gradient(circle, #1a1a28 0.8px, transparent 0.8px);
  background-size: 50px 50px;
  opacity: 0.35; pointer-events: none;
}
</style>
</head>
<body>
<div class="canvas">
  <svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350"
       style="position:absolute;top:0;left:0;">
    <!-- All SVG content here -->
  </svg>
</div>
</body>
</html>
```

### Adapting Per Post

When generating a graphic for a specific post:

1. **Title**: Change the main heading and subtitle to match the post topic
2. **Connectors**: Swap tool names for whatever tools/inputs are relevant
3. **Skills**: Swap skill names for whatever outputs/capabilities are relevant
4. **Power bars**: Change metric names, result labels, and fill widths to match the post data
5. **CTA pill**: Update button text and URL below it
6. **Brand**: Always keep "RecruiterGTM" at the bottom

### Reference File

The confirmed winning graphic is saved at:
`~/Desktop/linkedin-graphics/variation-10-final.html`

Use this as the literal code reference when building new graphics in this style.

---

## Generation Instructions

When asked to create a LinkedIn graphic:

1. Identify the post topic and what visual elements it needs
2. Copy the variation-10 HTML structure as the base
3. Swap in the post-specific content (title, connectors, skills, power bars, CTA)
4. Adjust power bar colours and fill widths to match the data
5. Save to `~/Desktop/linkedin-graphics/[descriptive-name].html`
6. Run `open [filename].html` to preview in browser
7. User screenshots or exports from browser for LinkedIn upload
