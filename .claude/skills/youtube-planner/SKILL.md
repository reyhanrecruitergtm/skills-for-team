# YouTube Content Planning Skill

Plan and maintain the RecruiterGTM YouTube channel: the 90-day topic slate, the two-series model, audience + funnel optimization, and the production tracker. This is the **planning** layer. Per-video production (titles, descriptions, thumbnails, tags, clip ideas) is handled by the separate **`youtube-content`** skill — invoke that when it's time to script a specific video.

**Invoke:** `/youtube-planner` — or when Reyhan says "plan YouTube topics", "update the YouTube tracker", "add a video idea", "rebuild the slate", "map topics to offers".

---

## Locked Rules

**A. Structure & source of truth**
- A1. The **tracker is the deliverable** — `RecruiterGTM YouTube 90-Day Tracker.xlsx`. Build it as a real `.xlsx` (openpyxl) and upload to Drive; **never** a native Google Sheet (per `feedback_drive_trackers_as_docx`).
- A2. Build script lives at `.claude/skills/youtube-planner/build_tracker.py`. Edit that script and re-run to regenerate — don't hand-edit the xlsx.
- A3. Raw idea backlog = the Google Doc **"YouTube Content - Scripts & Outlines"** (`1YxH6Q995XsIdQI0xanvJatMspoocgRnJGPgB3DUL-SA`). Pull new ideas from there.
- A4. Everything (tracker, scripts, edited videos, b-roll) lives in the **company Drive YouTube folder** `1ir2UjePVdfjsKmdfu9p1RYz4Ywrr3qII`. Upload there. Local working copy: `projects/youtube-channel-launch/`.
- A5. On update: regenerate → upload new to the Drive folder → delete the superseded upload (no duplicates). Keep the local copy in sync.

**B. Two series (every video is exactly one)**
- B1. **AI & Tech for Recruiters** — the converter series. Tool feedback, tutorials, Claude/AI use cases, system walkthroughs. Edit: screen-share heavy, fast, burned-in captions, chapter markers. Colour = violet `#8A00FF` tint.
- B2. **Founder Lessons** — the nurture series. Story, mindset, lifestyle, contrarian takes. Edit: cinematic, location/lifestyle b-roll, slower, music-led, minimal text. Colour = cream tint.
- B3. Target mix ≈ **9 Tech : 4 Founder** across 13 weeks; land a Founder Lesson roughly every 3rd week to keep the personal thread alive.

**C. Audience + funnel optimization (the core job)**
- C1. Audience = **recruitment agency owners/founders** (primary) + **GTM engineers** (secondary). Every title is written for them, leads with the outcome, and carries a **primary SEO keyword** in the first ~40 chars.
- C2. **Every topic maps to a Pillar/offer + a funnel destination.** No orphan videos. The channel is top-of-funnel for RecruiterGTM offers, not generic content.
- C3. Funnel logic: **Tech videos → hard CTA** (Skool / claude-code-dfy / outbound-os / book a call). **Founder videos → soft CTA** (newsletter + subscribe).
- C4. Keep **promotional videos ≤30%** of the mix.
- C5. Coverage check every rebuild: all **3 DFY engines** (BD / Sourcing / Content), all **5 Pillars**, **Talent placement**, and the **3 Skool value-props** (Claude Ops Manager, 1st Intent-Based BD Campaign, Website/SEO) each have ≥1 asset in slate or reserve.

**D. Cadence & tracker tabs**
- D1. Cadence: **1 long-form/week + 5 shorts/week**. Shorts = clips sliced from each long-form + the standalone hooks in the Shorts Bank.
- D2. Tracker tabs (locked): **90-Day Slate · Strategy · Series Guide · Reserve Topics · Shorts Bank**.
- D3. Slate columns: Wk · Target Publish · Series · Title · RGTM Pillar/Offer · Format · Primary Keyword (SEO) · Offer/Funnel · Edit Style · Status (dropdown) · Thumbnail Text · Editor · Editor Notes.
- D4. Default editor = **Shayan** (part-time video editor, reports to Reyhan). Graphics on request = **Shehroz**. Keep the Series Guide tab current so Shayan has one source of truth.

**E. Guardrails (verify before anything is finalized — preflight)**
- E1. **No revenue promises.** We install the 5-pillar system; sanctioned outcomes = profitability ↑, stress ↓, more conversations. Client numbers = testimonials only. (`feedback_no_revenue_promises`)
- E2. **Talent placement stays educational on YouTube.** Never pitch without ≥2 real sample candidates + video intros — those appear at the call/booking stage, not in the video. (`feedback_talent_needs_sample_candidates`)
- E3. **No hard prices in titles.** Don't invent or mis-state tool/offer prices; DFY pilot benchmark ≈ $2,500/mo (not $2k) — keep it off the thumbnail. (`feedback_never_assume_tool_prices`)
- E4. **Always use affiliate links** for any tool named in a description (Clay, Instantly, HeyReach, Apollo, Apify, Pin.com). (`feedback_always_use_affiliate_links`)
- E5. **Approved stats only:** 650+ agencies audited · 200+ GTME placements (98% still in role at 18mo) · 50+ OutboundOS deployments · 82 Skool members · 4 yrs recruitment systems / 8 yrs GTM. NOT valid: "250+ placed across 300+ companies". (`feedback_preflight_check`)
- E6. **Entity:** RecruiterGTM LLC on any on-screen legal/branding.

**F. Handoff**
- F1. When a specific video moves to Scripting/Filming, invoke **`youtube-content`** to generate the 5 titles, description, 3 thumbnail concepts, tags, pinned comment, end-screen plan, and LinkedIn clip ideas. This skill plans; that skill produces.
- F2. Scripting is done **after Reyhan's call with Shayan** (as of 2026-08-10) — don't pre-script the slate unasked.

---

## What "optimize a topic" means (the method)

For each raw idea from the Google Doc, produce:
1. **Optimized title** — audience-first, outcome-led, SEO keyword in first ~40 chars, using a `youtube-content` title formula.
2. **Series** — AI & Tech or Founder Lessons.
3. **Pillar / Offer** — which of the 5 Pillars and/or which DFY engine / offer it feeds.
4. **Primary keyword** — the search term a recruitment agency owner would type.
5. **Offer / Funnel** — the CTA and what RecruiterGTM asset it drives to, plus any proof point (approved stats) to reference.
6. **Thumbnail text** — 1-2 words.
7. **Format** — Case study / Framework / Tutorial / Behind-the-scenes / Contrarian.

---

## RecruiterGTM context to factor in (keep current)

- **Mission / flagship:** #1 Claude + AI systems implementer for recruitment agencies. Lead with Claude/AI implementation; talent placement is now public (Noroze) and can feature alongside.
- **5 Pillars:** 1) AI Layer (Claude Ops Manager) · 2) Multichannel Outbound · 3) Content + Authority · 4) ATS + Database (Stardex) · 5) Productization. (`reference_recruitergtm_5_pillars`)
- **Primary offer:** DFY 90-Day Pilots — one engine each: **BD / Sourcing / Content**. Benchmark ≈ $2,500/mo.
- **Skool community:** $1,497 one-time, 12 mo. 3 value props: Claude Ops Manager + 1st Intent-Based BD Campaign + Website/SEO.
- **Talent placement:** offshore GTM engineers / ops / recruiters; Noroze owns delivery.
- **Retainers** (~$2k/mo) + **Affiliates** (~10% of revenue).
- **Tool stack:** Claude Code, Clay, Instantly, HeyReach, Apollo, Apify, Attio, Pulse, Stardex, Lovable, Beehiiv.
- **Team for YouTube:** Shayan (editor, PT → Reyhan), Shehroz (graphics, on request → Reyhan). See `context/team.md`.

Always re-read `context/work.md`, `context/me.md`, and `memory/wiki/references/reference_recruitergtm_5_pillars.md` before a rebuild so the mapping reflects the current offers.

---

## Regenerating the tracker

1. Edit `.claude/skills/youtube-planner/build_tracker.py` (row data + reserve + shorts + strategy).
2. Run: `python3 .claude/skills/youtube-planner/build_tracker.py` → writes to `projects/youtube-channel-launch/`.
3. Upload the new `.xlsx` to Drive folder `1ir2UjePVdfjsKmdfu9p1RYz4Ywrr3qII` (mimeType `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` — keep it as xlsx, don't convert).
4. Delete the previous Drive upload by fileId. Verify one copy remains.
5. Never auto-open the file (`feedback_never_auto_open_files`).
