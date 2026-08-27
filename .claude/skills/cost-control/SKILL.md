# Skill: Cost Control

Keep Claude Code **and** every connected tool cheap by default. There are two places money leaks: **Claude usage** (which model runs, how hard it thinks, how many subagents fan out, how much it re-reads) and **third-party tool credits** (Apollo, Clay, Prospeo, Instantly, and any enrichment/data API). This skill sets the defaults and the confirm-before-spend rules for both.

**Invoke when:**
- Setting up a new workspace ("apply cost-control", read this once, then it runs in the background).
- Starting anything credit-heavy — enrichment runs, big list builds, multi-agent work: `/cost-control` for a pre-flight estimate.
- Auditing a session: "run cost-control" → report what was spent and where.

**Also ships an always-on CORE.md line** (Section G) — paste it into `memory/wiki/CORE.md` so the core behaviors fire every session without invoking the skill.

> Fill in Section F with the paid tools **you** actually use before handing this to anyone — the tool list here is an example, not a fixed set.

---

## Locked Rules

### A. Model tier — use the cheapest model that fits
- A1. **Default to the smallest capable model.** Routine work — reading, drafting, admin, file edits, summaries, simple research — runs fine on Haiku/Sonnet. Reserve the top tier (Opus/Fable) for genuinely hard work: strategy, complex builds, nuanced client-facing copy, ambiguous problems.
- A2. **If an expensive model is running on cheap work, say so once** ("`/model sonnet` is enough for this") then proceed — don't nag every turn.
- A3. **Personal/admin tasks never run on the top tier** — immigration, banking, document prep, payslips. → [[feedback_no_fable_for_personal_tasks]]
- A4. **Push heavy lifting down, not up.** File sweeps, bulk research, first-draft passes → delegate to Haiku/Sonnet subagents via the Agent tool instead of burning the expensive main loop on them.

### B. Effort & fan-out discipline
- B1. **Don't crank reasoning effort for simple tasks.** High effort multiplies token cost; save it for the hard 10%.
- B2. **No speculative multi-agent fan-out.** Parallel subagents and workflows multiply spend — only use them when the task genuinely needs breadth (wide search, independent verification) or the user explicitly asks. One focused pass beats five hopeful ones.
- B3. **Prefer the direct tool over the agent** for a single known lookup — spinning a subagent to fetch one fact you can grep is pure overhead.

### C. Context hygiene (the quiet token drain)
- C1. **Don't re-read what's already in context.** Files you just wrote/edited are tracked — re-reading to "verify" wastes tokens.
- C2. **Read the slice, not the whole file.** Use offset/limit on large files; read the 1–3 notes a task needs, never a whole folder or vault.
- C3. **Don't dump tool output you won't use.** Narrow searches, filter early, summarize rather than paste raw.

### D. Third-party tool credits (Apollo / Clay / Prospeo / Instantly / any data API)
- D1. **Know the cost before you run it.** For any credit-consuming call, state the estimate first. When a response returns a credit block (e.g. `mcp_credits`: estimated cost, actual spend, balance), **surface it unprompted** — before-spend estimate and, once settled, credits used + new balance.
- D2. **Free surface first.** Use free search/read tiers before paid enrichment (e.g. Clay `search filters-mode`, WebSearch, read-only queries). Never reach for a metered call when a free one answers it.
- D3. **Gate-order the spend.** Filter on free data first → enrich survivors only → verified emails/phones **last, qualifiers only**. Enrichment cost scales linearly with rows carried past each gate, so cut rows before you enrich, not after.
- D4. **Never trigger bulk enrichment, waterfalls, or AI columns silently.** Anything that meters credits at scale stops and confirms first. → [[feedback_flag_blockers_never_workaround]]
- D5. **Never invent a tool's price** to justify a spend — check or ask. → [[feedback_never_assume_tool_prices]]

### E. Confirm & report
- E1. **Confirm before a large single spend.** Before any one action expected to cost real money (a bulk enrich, a big send, a wide agent fan-out), state the estimate and get a yes.
- E2. **Bookend credit-heavy builds.** Check balance at the start AND end; report the delta in the final message and explain any surprise.
- E3. **When unsure whether something is expensive, ask** — a one-line question is cheaper than an unwanted run.

### F. Your paid-tool map (fill this in per workspace)
List the metered tools this workspace actually uses, what each meters on, and the free alternative.

**RecruiterGTM stack (Reyhan's workspace):**

| Tool | Meters on | Free-first alternative |
|------|-----------|------------------------|
| Apollo | per org/person enrich, people_match, job-postings | `clay search filters-mode`, WebSearch |
| Clay | enrichment / AI / Claygent columns, in-app waterfalls | `clay search filters-mode`, `clay tables` reads, `clay credits` |
| Prospeo | per verified-email lookup | Apollo `people_match` fallback |
| Exa | per research/verification call | free WebSearch first |
| Apify | per LinkedIn scrape / URL-verify run | verify only survivors, batch runs |
| Instantly | sending volume, email verification | verify qualifiers only |
| HeyReach | LinkedIn send volume / seats | draft first, activate on approval |

> **Attendees: replace this whole table with your own stack.** A member who doesn't use Clay shouldn't carry Clay rules — delete rows you don't use, add the ones you do. If you're unsure what a tool meters on, ask before your first big run.

### G. Always-on CORE line (paste into CORE.md)
Add this under a **Cost & credits** heading in `memory/wiki/CORE.md` so the defaults fire every session, not just when the skill is invoked:

> - **Default to the cheapest capable model + lowest effort**; reserve top tier for hard/strategic/published work, and never for personal admin. Don't fan out subagents or run metered enrichment without a clear need. For any paid tool call: know the cost first, surface the credit block unprompted, free surface before paid, confirm before any large single spend. → `.claude/skills/cost-control/SKILL.md`

---

## Notes
- This skill is behavioral, not a script — there's nothing to run. It's a set of defaults Claude follows.
- Skill-specific credit policies (e.g. `clay-table-builder`'s zero-credit runbook) still own the fine detail for their workflow; this skill is the umbrella everyone inherits.
