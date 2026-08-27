# Copy Engine Skill

## What This Skill Does

Produces outbound copy (cold LinkedIn DMs, cold email, follow-ups) that is *already good* before Reyhan sees it. It runs a Ralph-style draft → critique → rewrite loop, grounded in a swipe file of our real winners and scored against a 15-point rubric. Reyhan only ever sees the winner + runner-up, never a first draft.

**Invoke this BEFORE writing any cold DM / email / follow-up** — for our own outreach and for every client campaign (OutboundOS sequences). It sits on top of `humanizer`, `email-writer`, and `gtm-engine validate-copy`.

---

## Locked Rules

### A. The loop (run every time, never skip)
1. **Ground first.** Load `swipe-file.md` (our winners), `annotated-examples.md` (bad→good with reasoning), this rubric, [[feedback_banned_copy_phrases]], and the client's voice + the prospect's real signal. Then run the **Section D pre-writing questions** before drafting. Never draft cold.
2. **Best-of-N.** Draft 5–8 variants from *different* angles (signal-led, candidate-led, problem-led, peer-reconnect). Never one-and-done.
3. **Judge panel (3 lenses, not 1 — single judges are biased to long/formatted copy).** Score each variant 0–10 against the 15 rules below, from three perspectives: the **prospect** (would I reply?), the **skeptic** (what's generic/weak?), the **copy chief** (does it break a rule?).
4. **Adversarial pass, 2–3 cycles MAX** (more = noise). One pass tears the top variant apart — "weakest line? where does it sound like a template? what's the friction in the ask?" — then rewrite.
5. **Ralph loop.** If the best variant scores under the bar (≥8/10 average, zero rule-13 violations), feed the critique back and loop. Cap at 4 passes.
6. **Humanizer pass** on the winner.
7. **Deliver winner + runner-up + a one-line "why this won"** to Reyhan. Nothing else.
8. **Reflexion / control-beating.** After a campaign runs, pull real reply rates from HeyReach/Instantly and log the winners (and losers) back into `swipe-file.md`. **Real reply data is the only true learning signal — LLM self-scoring alone plateaus.**

### B. The 15-point rubric (the scorecard — every rule is checkable)
1. **First line earns the open** — references one specific, recent, verifiable thing about *them*, not a persona. (Ogilvy: the open is 80% of the work.)
2. **One idea only** — one problem, one solution, one ask. Count them.
3. **One concrete signal > five generic lines** — post / hire / launch / funding from the last ~30 days. Signal-based ≈ 15–30% reply; persona-based ≈ 1–3%.
4. **Reads personal, not promotional** — peer-to-peer tone, no corporate voice (Halbert A-pile).
5. **Curiosity gap** — don't dump the full pitch; leave a reason to reply (Sugarman).
6. **One sentence per line, short, slippery-slide** — each line makes the next readable; no paragraph blocks (mobile).
7. **CTC not CTA** — a question, not a calendar link. ("Open to it?" beats "book a call" ~30% vs ~1.4%.)
8. **Low-friction ask** — answerable yes/no in 3 seconds.
9. **Written-for-them feel** — IF…THEN / mirrors their situation (Bencivenga).
10. **Relevant proof** — their niche, real names/numbers, not "200 companies."
11. **Show don't tell** — a number or example, not an adjective.
12. **Acknowledge their actual desire/problem** — they recognize themselves in line 1–2 (Schwartz desire-channel; Nowoslawski problem-sniff).
13. **Zero spam / AI phrases** — hard fail on anything in [[feedback_banned_copy_phrases]] ("quick one", "no pressure either way", "in your corner", etc.).
14. **Urgency natural, not forced scarcity** — real reason it matters now, not "only 5 spots."
15. **One CTA, escalating across the sequence** — msg 1 = interest check · msg 2 = soft value/link · msg 3 = the meeting ask. Never lead with the meeting.

### C2. Numeric scoring gate (added 2026-07-19 — GrowthEngineX rubric, validated on 1,000+ real B2B campaigns)
Score the winning variant 0–100 before delivery, weighted: **Situation Recognition 25 · Value Clarity 25 · Personalization 20 · CTA Effort 15 · Punchiness 10 · Subject Line 5.**
Bands: **85+ = deliver · 70–84 = one more critique loop · under 70 = restart from new angles.** Always report the score alongside the winner. This is the numeric layer ON TOP of the 15-point rubric, not a replacement.

### C3. Cold email structure defaults (added 2026-07-19 — Corey Haines marketingskills, 40k+ stars)
- **Subject lines: 2–4 words, lowercase, internal tone** — reads like a colleague's email ("sourcing velocity", "the mep role"), never "Reaching Out" or anything title-case. (Newsletters keep their own locked hyphen-pattern subject — this rule is for cold/sales email only.)
- **Body skeleton: Observation → Problem → Proof → Ask.** Default shape for message 1; variants may deviate deliberately, never accidentally.
- **Length: 50–90 words** per cold email. Every email stands alone — no "as per my last message".
- **Personalization cap: 1–2 prospect details maximum.** Three or more reads as surveillance, not research.

### C4. Sequence offer rotation — 3-Offers (added 2026-07-19)
Across a follow-up sequence, rotate the value frame: **Save Time → Make Money → Save Money.** Never the same frame twice in a row. Ours map naturally: OperatorOS = time back · OutboundOS/SourcingOS = revenue in · the embedded/AI-native cost maths = money saved.

### C5. Follow-ups + email formatting (added 2026-08-17)
- **Follow-ups are non-apologetic.** Open on the core problem the offer solves, then offer proof as a soft yes/no (e.g. "Want a 2-min recording of it running on a live role?"). BAN apology openers ("no worries if not", "all good if not", "no stress if the timing is off") and self-shrinking closes ("no strings", "no call needed", "my door is open"). → [[feedback_non_apologetic_followups]]
- **Emails are never one block.** Blank line after the greeting, blank line between every paragraph, two-line sign-off (`Best,` then `Reyhan`). HTML email: `<div><br /></div>` between paragraphs + `<div>Best,</div><div>Reyhan</div>`. Trim merge-field values so variables never render a double space. → [[feedback_email_spacing_format]]

### D. Pre-writing discipline + anti-slop craft (added 2026-08-19 — imported from the Kai/Effa cold-email system, run on 171k+ sends)
Slop comes from two habits: **drafting before thinking**, and **describing our product instead of their situation.** These run BEFORE the best-of-N loop (Section A step 2). This is the section to teach the team first — the rubric catches slop, this section *prevents* it.

**D1. The 3 pre-writing questions — answer all three before drafting a single line. No answers = don't write yet.**
1. What is the ONE situation this message is about? (one sentence, plain language, no jargon — this becomes line 1.)
2. What would they say to themselves if they thought "hell no"? (the primary objection — you'll pre-empt it in one sentence.)
3. What is the single most valuable thing you can give them? (NOT the product — an insight, a teardown, a question that makes them think.)

**D2. Situation over claims — the #1 slop fix.** Features are OUR vocabulary; situations are THEIRS. Describe the gap they live with, not what the thing does. The reader recognises the gap; they do not care about our description of ourselves.
- ❌ "We built a Claude ops manager that runs sourcing, outreach and your ATS." *(our story, our taxonomy)*
- ✅ "Most of a recruiter's week goes on admin that never needed a human — sourcing, list-building, the first draft of every outreach." *(their world)*
- Test on every draft: does it describe what we DO, or the situation it resolves? If the former, rewrite.

**D3. The homework test — kills jargon.** How would this person describe the frustration to a stranger at a party (not a colleague — someone with zero context)? That's the register. Every buzzword is a micro-decision ("do I know what this means? do I care?") and each one is an exit ramp.
- ❌ "a candidate correlation engine leveraging your ATS data"
- ✅ "it quietly matches your best candidates to live roles that fit"

**D4. Specificity ladder — climb as high as the data lets you.**
- **L1** (minimum bar): industry — "most {niche} desks we see…"
- **L2** (strong): company-observable — something on their site / LinkedIn / recent post.
- **L3** (strongest): person-observable — a specific thing THEY did, that could not have been sent to anyone else.
- A wrong detail is worse than no detail — **never fake L3.** If you can't be specific, open on the situation instead of faking research.

**D5. Objection pre-emption.** After drafting, read it as the prospect and say "hell no." Spend ONE sentence neutralising the objection that would kill the thread fastest — conversationally, the way you'd answer it to their face. (e.g. "without adding headcount" pre-empts "we'd need more staff".)

**D6. Which rules are hard gates vs judgment.** Not every rule binds equally, and treating a taste preference as a hard gate is how the team ships stiff copy to satisfy a checklist. **Hard fails (never ship):** Section B rules 1, 2, 7, 13 · all 5 anti-slop-rubric layers · [[feedback_banned_copy_phrases]] · the em-dash rule. **Everything else is judgment** — break it only with a stated reason. Real reply data (Section A step 8) is what promotes a rule from judgment to gate; `swipe-file.md` is the evidence base, not taste.

**D7. Teach from annotated pairs, not templates.** Copying a template produces slop; understanding *why* a line works produces copy. Before writing, read `annotated-examples.md` — real bad→good pairs in our voice with the reasoning. When the team returns edited copy that lands, add the pair there.

### C. Defaults
- **Goal of cold copy = a reply, not a booking.** (Allred/Crawford.) Optimise the rubric for reply rate; bookings come from the conversation.
- British/neutral English for Reyhan's voice; match the client's own voice for client campaigns.
- Em dashes per [[feedback_em_dashes]] (default zero).
- When unsure between two winners, ship both as an A/B and let reply data decide (control-beating).

---

## Source frameworks (for the judge's reasoning)
AIDA · Halbert A-pile/B-pile · Sugarman slippery-slide + curiosity gap · Ogilvy headline-80% · Schwartz one-desire · Bencivenga IF…THEN + persuasion equation · Hormozi M.A.G.I.C. hook + value equation · Nick Abraham 3-layer personalization · Nowoslawski problem-sniffing · Crawford specificity · Allred CTC · Josh Braun 4-T + soft ask. Full notes + sources in `research/2026-06-29-copywriting-frameworks.md` (to be saved).

## Ralph loop infrastructure
- The loop above can be run manually per message, or automated with `/loop` (self-paced) over a campaign's lead list, or as a `Workflow` (best-of-N fan-out → judge panel → adversarial verify → synthesize).
- For LinkedIn *content* (not outreach), the standalone `ralph-wiggum-marketer` Claude Code plugin (muratcankoylan) is a separate experiment — point it at the Pulse content calendar (`team_content_posts`), not at client outreach. (Notion Idea Inbox retired 2026-07-19.)
