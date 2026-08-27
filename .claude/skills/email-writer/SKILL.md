# Email Writer Skill

## What This Skill Does
Writes outbound and reply emails in Reyhan's exact voice. For client emails, proposals, follow-ups, contract sends, and any external communication from RecruiterGTM.

## How to Invoke
Paste the email thread + purpose + key points to hit → `/email-writer`

---

## Locked Rules

### A. Skill invocation (mandatory)
- A1. This skill is MANDATORY for ANY external email — replies, follow-ups, proposal-send notes, contract cover notes, short 3-line replies, anything. No freehand. Flagged repeatedly.
- A2. Run the anti-AI pattern check (section C) on every email before showing to Reyhan. AI fingerprints kill credibility.

### B. Approval flow
- B1. ALWAYS show the email copy (To, Subject, Body) in chat for Reyhan to approve BEFORE creating any Gmail draft.
- B2. Never send emails — only drafts. Reyhan sends. (Cross-cutting rule lives in `/memory/feedback_never_send_emails.md`.)
- B3. When invoked from proposal-generator on finalize, follow proposal-generator section N rules for subject format and template.

### C. Voice (extracted from real threads — Paul Lingle, Duncan Seward)
- C1. Opener: "Hey [first name]," or "Hi [first name],". Never "Dear", never just the first name.
- C2. Short paragraphs. One idea per paragraph. Plain English. Reads like a text message from a smart friend, not a sales rep.
- C3. No corporate fluff. Banned: "Hope this finds you well", "I wanted to reach out", "Just wanted to follow up", "Per my last email", "As discussed", "Excited to share", "Looking forward to your response".
- C4. Parallel-negation patterns auto-cut: "X, not Y" emphasis ("signal, not a full read", "a tool, not a hire", "a pitch, not a conversation"). AI tell. Rewrite as a single positive statement.
- C5. Bullets: plain `•` or `-`. NEVER 🪓 axe bullets in emails — those are LinkedIn / Skool only.
- C6. Max 1 em dash in prose. Default to zero. (Cross-cutting em dash rule in `/memory/feedback_em_dashes.md`.)
- C7. Banned words: same set as content-os section A — no "ship", "leverage", "transformative", "what actually matters", "[X] is real", "no fluff", "not theory not slides" etc.
- C8. NEVER use "tooling" (Reyhan flagged 2026-06-22 — "nobody ever uses it"). Always say "the tech stack", or name the specific tools. Applies to every email.
- C9. NEVER use "honest read" / "the honest read on..." in any email (Reyhan flagged 2026-08-15). It's an AI-opener tell. State the situation plainly instead ("The last few weeks: the list was too small.").
- C10. **Inherit ContentOS taste rules (added 2026-08-15).** Every email runs the content-os **Section A (banned words + phrases), B (banned sentence patterns), C (hollow-line check), and D (em dash limits)** on top of the email-specific rules here — content-os is the source of truth for those bans, so read `.claude/skills/content-os/SKILL.md` Sections A–D and apply them, don't rely on the summary. This is the same "taste rules apply to every channel" rule content-os declares in X5; email is now explicitly wired in. Email STRUCTURE/register stays governed by this file (openers, sign-offs, thread-matched tone) — only the rejection rules are inherited. Channel-only items (LinkedIn hooks, CTA keywords, axe bullets, `——` sign-off separator) do NOT apply to email.

### C2. Voice DNA (added 2026-07-19 — community-validated: "first output already 80% there")
The voice sections below ARE the Voice DNA — but keep them alive: whenever Reyhan approves a new email that he edited before sending, diff his edits against the draft and fold the pattern back into the voice sections. His edits are the highest-signal voice data that exists. When writing for a tone we have no sample of, ask for one real email of his in that register before drafting — imitation beats abstract style rules.

### C3. Cold/sales email structure (added 2026-07-19 — see copy-engine C2–C4 for the full rules)
For outbound and sales emails: subject 2–4 words lowercase internal-tone · body Observation → Problem → Proof → Ask · 50–90 words · max 1–2 prospect details · score 0–100 via copy-engine's gate, deliver at 85+. Relationship/client-thread emails (the core of this skill) keep the thread-matched register — these rules are for net-new sales email only.

### C4. Voice DNA additions from the 2026-07-21 newsletter JOIN replies (Reyhan's edits vs draft)
- Fit line stays humble and personal: "I feel like this community can be the right fit for you" — NOT absolute claims like "you're exactly who this is built for".
- Plain verbs over clever framing: "we help you setup" beat "setup is included — that's the point of the DFY layer". Cut aphorisms ("you learn on a running engine instead of building one alone") in favour of concrete continuation: "You continue using the same engines and build new campaigns, automations etc with our ongoing support for 12 months."
- Canonical cost breakdown for the community offer: "$1,497 covers 3 system setups and support for 12 months" (+ deadline if live). Not "covers all of it".
- Casual "etc" mid-sentence is authentic Reyhan; keep it.

### C5. Voice DNA additions from the 2026-08-03 community reoffer edits (Reyhan's rewrite vs draft)
- State the reason for the outreach plainly and up front: "I'm reaching out because our community pricing went up to $4,497/year." Beat the draft's scarcity framing ("Before that locks in for good, I'm opening one last window").
- Name deliverables in compact parenthetical shorthand: "3 systems (Claude, market map, SEO) set up for you" — not the full formal list ("Claude AI Ops Manager, your 1st intent-based BD campaign, and a website/SEO redo").
- Price format on offers: "$4,497/year" with the /year suffix.
- Cut social-proof tail lines from short reoffers (dropped "We're at 82 recruitment businesses inside now").
- CTA variant: "Lmk if this is of interest." is approved alongside "Lmk if that's of interest".

### C6. Substance + Voice DNA from the 2026-08-25 Pat Corrigan reply (Reyhan's rewrite vs draft)
Highest-signal lesson: **Reyhan answers with substance and pushes back — he does NOT reflexively agree when a prospect rescopes the deal.** The draft gave "yes / yes / yes" to his three asks; Reyhan's sent reply held the frame. When a reply-to-inbound involves scope/pricing, default to holding the offer structure, not accommodating.
- **Answer the questions in-thread, briefly, then take depth to the call.** Don't defer all of them ("I'll walk you through it live"). A short real answer per question, then the call for detail.
- **Give honest directional truths about our own business; don't go silent on a "how many have you done" question.** Reyhan answered "we've built multiple DFY engines with teams of 2-3 recruiters; we mostly deal with small businesses with teams of 2-5." The no-invented-stats rule bans fabricating precise/false numbers, NOT answering. Offer Reyhan a directional line or a `[fill number]` placeholder, never a blanket deferral.
- **Protect the model; push back on scope that strips out proof.** To "price Claude Code DFY + ATS work standalone, without SourcingOS?" Reyhan declined: "We always set these up with either Outbound or Sourcing as the main goal because without that, there isn't enough proof after setting the engine up." Never soft-commit "yes, that's a real standalone scope and probably right for you" — hold the structure and explain why.
- **Correct the buyer's cost assumptions instead of mirroring their spec.** He clarified dedicated vs shared: "each recruiter needs their own dedicated Claude and sequencing seat, the research and enrichment tools can be shared." Add real operating detail; flag when scope changes pricing ("the scope and pricing will need adjustment").
- **Bound over-accommodating asks with a concrete limit.** 3 seats → "group calls instead of 1:1, but we won't support three people separately 1:1 at the same price," not "yes, we can structure it that way."

Voice edits from the same rewrite:
- **Open with a genuine human line, never commentary about their email or your own process.** Cut "I read your email a few times, and this reframe is the right one" → "Hey Pat, back from the mastermind; it went really well!"
- **Cut clever-framing tails/aphorisms.** Deleted "that's how the engagements that actually stick get set up"; "I build and teach, your team runs it" → plain "We build the engine and teach your team to run it" (prefers "we").
- **Real proof beats aspirational architecture.** The speculative Crelate paragraph → "Let's see what the Crelate MCP can do for us. I'm excited too because another one of my longterm clients has Crelate."
- **Keep CTAs bare.** Timezone logistics cut → "Let's chat this Thursday? Lmk what time works for you guys." "you guys" is authentic; don't over-engineer scheduling.
- Prefers "I'll quickly cover your three questions" over "Quick read on your three questions"; likes semicolons; echoes the buyer's own plan back verbatim when it's already right (the pilot paragraph survived unedited).

### Email type: Community Join Reply (newsletter JOIN CTA) — locked from real sends 2026-07-21
Structure Reyhan used for William/Lisa/Simon: thanks for interest → (answer their specific questions directly, one per paragraph, if they asked any) → custom niche line citing real member feedback in THEIR niche (never invented; verify the member evidence first) → cost breakdown + deadline if price-sensitive → "Here is the Community Link" → "I'd also like to know more about your business and give you a quick walkthrough before you join. I'll also need to reduce our community price and add you live on a call; it doesn't have to be too long." → "Do you have time to speak tomorrow or Friday?" → Calendly line → "Lmk."

### D. Preserve all explicit points
- D1. When Reyhan lists multiple specific points to hit in an email, every one must survive into the final draft. Never silently drop or merge points across revisions. Especially "dogfood" + proof references — those get cut most often, never let it happen.

### E. Plain sentence construction (added 2026-08-25 — Reyhan flagged: "you always structure sentences wrong, like passive voice")
Every sentence is plain **subject → verb → object**. Lead with the thing, say what it does, stop. Read each sentence back: if it inverts, hedges, or hides who is doing the action, rewrite it.
- E1. **No fronted "What X is:" / label-then-colon constructions.** Write "A meaningful conversation is someone replying with positive intent." NEVER "What a meaningful conversation is: someone replying…" or "The way this works is:" or "Where this lands is:". Delete the scaffold and state the thing directly.
- E2. **No passive voice — name the actor.** "We build the domains on your accounts", not "the domains are built". "We bill at the start of each month", not "billed at the start of each month". If the sentence doesn't say who does it, it's wrong.
- E3. **No nominalizations that bury the verb.** "we configure it" not "we do the configuration of it"; "we decide" not "we make a decision".
- E4. **Front the subject, not a throat-clear.** Cut openers like "In terms of…", "When it comes to…", "The thing to note is…" — start with the noun that acts.
- E5. This applies to EVERY sentence in EVERY email, and reinforces content-os Section B (banned sentence patterns), which email inherits via C10. When in doubt, the shortest subject-verb-object version wins.

---

## Reyhan's Email Voice (Extracted from Real Threads)

### The core register
Reyhan emails like a founder who respects the reader's time and his own. He's warm but not gushing. Direct but not cold. He writes like he texts — short paragraphs, casual openers, real specifics.

Think: smart friend updating you on something, not a sales rep closing a deal.

### Opener style
- "Hey [first name]," — almost always
- "Hi [first name]," — acceptable for more formal contexts
- Never: "Dear Paul," / "I hope this email finds you well." / "I wanted to reach out..."

### Closing style
- "Lmk your thoughts" or "Lmk" — for casual/warm threads
- "Best, Reyhan" — standard close
- "Let me know if you have any questions." — fine when sending a formal doc
- Never: "Kind regards" / "Warm regards" / "I look forward to hearing from you"

### Paragraph structure
- One point per paragraph. Max 3 lines per paragraph.
- White space between every paragraph — never a wall of text.
- If you have 4+ points, consider whether a short bullet list makes it cleaner. Don't over-bullet.

### What Reyhan actually does in emails
- **Gives real numbers.** "I've had 20 good conversations with agency owners like yourself." Not "I've had a lot of conversations."
- **Drops personal asides naturally.** "Btw me and you..." / "Ps: Clay event yesterday was crazy, I'm a celebrity in Islamabad haha." These land because they're genuine — not forced.
- **States the situation plainly.** "The scope has moved beyond the original engagement" — not "I wanted to make you aware that the work has expanded."
- **Uses "we" for the team, "I" for personal views.** "We can set up the Slack channel" vs "I think the timing makes sense."
- **Gating language is direct but not aggressive.** "I'd like to get a retained agreement in place before we spend more time on this." Not "Unfortunately we are unable to proceed without..."

---

## Voice Rules (from LinkedIn Content Skill — apply to email too)

**DO:**
- One idea per paragraph
- Short declarative sentences — subject + verb + object
- Real specifics: names, numbers, timelines, tool names
- Em dashes: maximum 1 per entire email. Default to zero. Only use if no other punctuation works. Never use to connect a clause that could just be a new sentence.
- British/neutral English: "recognise" not "recognize", "behaviour" not "behavior"
- Use "lol" or casual asides when genuinely appropriate — signals a real person

**DON'T:**
- **No 🪓 axe bullets in emails.** Axe bullets are reserved for LinkedIn posts and Skool content. In emails, use `•` (default), `-`, `→`, or numbered lists. See `feedback_axe_bullets_no_email.md`.
- No "I hope this finds you well" or any variant
- No "I wanted to reach out / circle back / touch base"
- No "Please don't hesitate to"
- No "As discussed" as an opener (lazy, sounds robotic)
- No "I'm excited to share" or corporate openers
- No generic CTAs ("Let me know what you think!")
- No AI vocabulary: leverage, delve, crucial, pivotal, landscape, testament, underscore
- No rule of three padding: "fast, reliable, and scalable" — just say the thing
- No negative parallelism: "It's not just about X, it's about Y"
- No em dashes unless absolutely necessary. Default is zero. Max one per email, hard limit. Every em dash is a candidate to be cut or rewritten as a new sentence.
- Don't explain what you're about to say — just say it
- Don't write "transparent" when you mean direct
- Don't add a call to action if you've already made the ask clear

---

## Email Types & Patterns

### Contract / Next Steps Send
**Purpose:** Send the agreement, set expectations, keep momentum.

**Structure:**
1. One line saying what you're sending and the start date
2. 2-3 lines covering the key terms (rate, structure, what happens next)
3. Ask for confirmation or signature
4. Optional: one genuine aside (deal progress, team, excitement — keep it real)
5. Sign-off + "Lmk" or "Let me know if you have questions"

**Real example (Paul Lingle):**
> Hey Paul, I have sent you a detailed contract to sign with a start date of 1st April for this new engagement, please let me know if you have any questions.
>
> Btw me and you, I've had like 20 good conversations with recruitment agency owners like yourself who are more interested in a managed service instead of them having to handle a GTM resource internally, and I will price this at $2.5k - $3k when pitching them.
>
> Also, I'm in conversations with Salar, the best GTM in my network to come work for RecruiterGTM with another guy I've hired this week. So we will have 2 GTM Engineers with 6 years of experience running these scenarios and many others along with me overseeing strategy.
>
> Once you sign, I'll shoot over the payment link for 3 months. Goal will be to prove this concept and have a lucrative Engine delivering conversations in these 3 months so both of us are confident in turning this into a longterm partnership.
>
> Lmk your thoughts or if you want any changes.
>
> Ps: Clay event yesterday was crazy, I'm a celebrity in Islamabad haha
>
> Best,
> Reyhan

**Notes on this example:**
- Casual, warm, but all the key info is in there
- The personal asides (20 conversations, Salar, Clay event) build confidence without being sales-y
- "Btw me and you" creates a conspiratorial warmth — feels exclusive
- "Prove this concept" is honest about where they are — not overselling
- Ps is genuine, not forced

---

### Scope Gating / Boundary-Setting Email
**Purpose:** Flag that work has grown beyond the original scope, gate further execution on a signed agreement. Must be firm without being transactional.

**Structure:**
1. Acknowledge what's been done / the progress (genuine)
2. Name the scope creep clearly and specifically — don't hedge it
3. State what you need before continuing (signature, agreement)
4. Make the ask easy — no setup fee, clear next step
5. Keep the tone collaborative — you're protecting both parties, not just yourself

**Key rules for this type:**
- Don't say "transparent" — just be direct
- Don't pitch on a call — if the deal is live, an email CTA is cleaner
- Don't shrink the email to appear non-threatening — clarity is respect
- Name the specific work that's been done (e.g. "33k law firms scraped, 1,700 solicitors identified")
- Gate on a signed agreement, not on a payment

**Duncan Seward example principles (from real thread):**
- Acknowledge Shmookh's proof of concept work specifically
- Flag that this has moved beyond the original engagement scope
- State: no setup fee, respecting Duncan's earlier investment
- Ask: retained agreement in place before more work, April 1st start
- Ask for Duncan's thoughts on timing — don't unilaterally declare

---

### Price-Increase Reoffer — LOCKED template (Reyhan-approved 2026-08-04, community reoffer campaign)
**Use this exact structure for ANY reoffer** (community, DFY, retainer win-back) whenever pricing changes and past leads get a held-price window. Final version after Reyhan's own edits:

> Hey Daniel,
>
> We spoke in May about the PRS build and I know timing was the question.
>
> I'm reaching out because our community + DFY pricing went up to $4,497/year. I'm holding the original $1,497/year open for the people I already spoke with in the past months. This is exactly what it covers:
>
> - 3 systems set up for you: Claude AI Ops Manager, your market map, and SEO
> - 12 months of support
> - Early access to our product launches
> - Discounts on offshore talent
> - Ongoing systems benchmarking
>
> This closes Friday, then it's $4,497 for everyone.
>
> Lmk if this is of interest.
>
> Best,
> Reyhan

**Structure (swap the variables, keep the bones):**
1. "Hey {first}," + ONE personalized line from the last real interaction: "We spoke in {month} about {their thing}" + the stall reason if known.
2. Plain reason: "I'm reaching out because our {offer name} pricing went up to {new price}/year. I'm holding the original {old price}/year open for the people I already spoke with in the past months."
3. "This is exactly what it covers:" + bullet list of the EXACT deliverables (never vague).
4. Deadline line that backs the subject: "This closes {day}, then it's {new price} for everyone."
5. "Lmk if this is of interest." → "Best,\nReyhan"

**Locked details from Reyhan's edits:**
- Name the offer precisely: "community + DFY pricing", never just "community pricing".
- Both prices carry "/year" ("$1,497/year", "$4,497/year").
- Subject pattern (approved over 5 variants): "{$ amount} off until {day}" — e.g. "$3,000 off until Friday". Deadline in subject REQUIRES the matching deadline line in the body.
- Leads quoted a different price get "the price we discussed" instead of the dollar figure.
- LinkedIn variant = same structure inline as one block, ending "Lmk if this is of interest."
- Day-2 follow-up (both channels): "Sending this again in case it got buried. The window to join at {old price} instead of {new price}/year is still open." / LinkedIn: "Floating this back up in case it got lost."
- Custom rows (e.g. a lead with a detailed prior call) keep the same skeleton but swap the generic bullets for call-specific deliverables, and open with the honest reason for the gap if there is one.

---

### Follow-Up / Proposal Follow-Up
**Purpose:** Re-engage a lead who hasn't replied. Short. No pressure.

**Structure:**
1. One line — what you sent, when
2. One line — the specific thing you want them to react to
3. Optional: one new piece of context that adds value (new client result, update)
4. Simple ask: "Thoughts?" or "Happy to jump on a quick call if easier."

**Rules:**
- Never say "just following up" — lead with the value or question
- Never apologise for following up
- Keep it to 3-4 sentences max
- If it's the second follow-up, add something new — don't repeat the first email

---

### Referral / Reference Intro — LOCKED template (proven, repeated in sent mail)
**Purpose:** Connect a prospect who wants a reference to an existing client who'll vouch. Addressed TO the prospect, CC the reference client, then step back and let them coordinate directly. This is the mechanic Reyhan has used with Patrick Schildmann as reference for Justin (Ethix), Daniel (Captains Club), Kylie, Oliver Zauritz, Patrick How.

**Subject:** `RecruiterGTM Experience - Referral Intro`
**To:** the prospect(s) · **Cc:** the reference client

**Locked structure (Reyhan's exact sent copy):**
> Hi {Prospect}, I'm copying {Reference}, one of our oldest clients, who'd be happy to share his experience with you. We've helped him with {what we did for them} and he's also one of the most active members of our community.
>
> @{Reference} {Prospect} is exploring the potential for us to run their {engine} engine.
>
> I'll let you take it from here.
>
> Best,
> Reyhan

**Rules:**
- Describe the reference accurately — only claim engines we actually ran for them (Patrick = Outbound + Content + active community member; don't copy that line onto a different reference).
- Never promise results or numbers on the reference's behalf. "Happy to share his experience" only.
- One reference per email/thread (don't cc two references on the same thread). Multiple prospects at the same firm go in the To together ("Hi Lauren and Mark,").
- The cc IS the heads-up — the reference is looped straight into the thread, so no separate "look out for this" email is needed. If Reyhan wants to pre-warm the reference, that's a short WhatsApp/Slack line, not another email.

---

### Reply to Inbound Interest
**Purpose:** Respond to a warm lead who has expressed interest. Build clarity, move to next step.

**Structure:**
1. Acknowledge their specific question or concern directly
2. Give the honest answer — don't oversell, don't undersell
3. If there are two options, explain both clearly and give a recommendation
4. Suggest next step (call or send more info)

**Rules:**
- Never open with "Great question!" or "Thanks for your message!"
- Address their actual concern, not a sanitised version of it
- If they're confused, clarify plainly — don't pad with reassurance
- End with one clear CTA, not two

---

## Anti-AI Patterns to Catch Before Sending

Run a mental check before finalising any draft:

| ❌ AI Tell | ✅ Fix |
|-----------|--------|
| "I wanted to reach out" | "Hey [name]," → get to the point |
| "Please find attached" | "I've sent the contract over" |
| "As per our conversation" | "Following our call last week..." |
| "I hope this email finds you well" | Delete entirely |
| "Please don't hesitate to contact me" | "Lmk if you have questions" |
| "I look forward to hearing from you" | "Lmk your thoughts" |
| "It would be remiss of me not to mention" | Just say the thing |
| "Circling back on this" | "Sending this again in case it got buried" |
| Three-part lists everywhere | Cut to two or say it in a sentence |
| Every paragraph the same length | Vary it — short punchy paragraph, then a longer one |
| Explaining the email before writing it | Delete the preamble, start at the point |

---

## Generation Process

When asked to write an email:

1. **Read the thread.** Understand what's been said, what the relationship is, what tone has been established.
2. **Identify the purpose.** What is this email trying to do? (Send info / Gate on action / Re-engage / Reply to concern)
3. **List the key points to hit.** Don't add points Reyhan didn't ask for.
4. **Draft in Reyhan's voice.** Use the patterns above. Short paragraphs, real specifics, casual opener.
5. **Run the anti-AI check.** Scan for every pattern in the table above.
6. **Check tone.** Read it aloud. Would a smart, busy founder send this? Would it feel warm but efficient?
7. **Output the final email only.** No preamble, no "here's a draft", just the email.

---

## What NOT to Do

- Don't add information Reyhan didn't provide (don't invent details or numbers)
- Don't make the email longer than it needs to be — if the point is made in 3 paragraphs, stop at 3
- Don't add a call to action if Reyhan has already made the ask
- Don't soften firm asks — if the email is gating on a signature, make that clear
- Don't write multiple versions — write one version, make it right
- Don't add a subject line unless asked
