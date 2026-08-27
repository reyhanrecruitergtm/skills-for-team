# Personalization Sub-Agent Pattern Skill

## What This Skill Does

The reusable **approval-loop + parallel-fan-out** pattern for generating per-lead personalisation at scale — without hand-writing every line and without discovering the prompt was wrong after 500 leads. It's the **scaled final mile** in our outbound architecture ([[reference_nowoslawski_architecture]]): the qualified list comes out of Claude Code enrichment, this pattern produces the prospect-facing lines, `copy-engine` enforces quality, and the [list-quality-scorecard](../list-quality-scorecard/SKILL.md) gate clears it before send.

Adapted for RecruiterGTM from GrowthEngineX's open-source `personalization-subagent-pattern` (github.com/growthenginenowoslawski/coldoutboundskills). Invoked by `outbound-os-claude`, `sourcing-os`, `gtm-engine`, or any skill that needs per-lead custom variables.

---

## Locked Rules

### A. Always Task/Agent sub-agents — never an external API key
Run entirely inside Claude Code via the **Task/Agent tool**. No Anthropic SDK calls, no OpenAI key.
- **No extra spend** — uses the Claude Code plan.
- **Parallel by design** — spawn many sub-agents in one message; 100 leads finish in the time it takes to do 10.
- Only at 1,000+ leads, after the prompt is tuned, may the locked prompt optionally ship to the Anthropic API for throughput. Tuning + normal runs (<500) always use sub-agents.

### B. Loop first, then scale (never scale a wrong prompt)
1. **Round 0 — sample on 1.** Pick one lead with a rich signal/description. Show Reyhan (or the operator) the source data + what you'd generate for each variable. Ask: "does this feel right?"
2. **Rounds 1-N — batch of 10 with approval.** Spawn ONE sub-agent with the current prompt + 10 leads. Display all 10 in a table. Ask for edits by row number. Fold edits back into the prompt (or add rules like "never use word X").
3. **Lock.** When there are **zero edits for 2 consecutive rounds**, the prompt is locked.
4. **Scale.** Split the rest into batches of 10-20, launch 3-10 parallel sub-agents (one per variant × batch), merge by `lead_id`.

### C. Every line obeys `copy-engine`
The sub-agent prompt embeds the `copy-engine` rules — [[feedback_banned_copy_phrases]] (hard fail on "quick one", "no pressure either way", etc.), the 15-point rubric, British/neutral English, em dashes default zero. Personalisation at scale does NOT get a pass on the copy standard.

### D. Ground every line in a real signal
No generic "I loved your work" filler. Each line ties to the lead's actual signal — the TA-ratio gap, an open req, a leadership change, a funding round, a recent post. If there's no signal, the lead shouldn't be in the batch.

---

## Variables produced (default)
Per qualified lead: `situation_line` (their specific situation), `value_line` (the relevant proof/offer), `cta_soft` (a question, not a calendar link). For `outbound-os-claude` these map to `personalisation_line_1` / `personalisation_line_2`. Merge back to the JSONL/CSV by `lead_id`.

## When to use
- Any campaign with 50+ leads needing more than `{first_name}`.
- When `outbound-os-claude` / `sourcing-os` reach the personalisation step.
- When the TA Ratio (or any) signal has produced a qualified list and each row needs a tailored opener.

## When NOT to use
- Under ~20 leads — just write them by hand through `copy-engine`.
- Prospect-facing lines that need Clay's Claygent final-mile — run this to draft, then Clay + human QA before send (the prospect boundary).

## Related
- [[reference_nowoslawski_architecture]] · `copy-engine` · [list-quality-scorecard](../list-quality-scorecard/SKILL.md) · [outbound-os-claude](../outbound-os-claude/SKILL.md)
