# RecruiterGTM — Skills for Team

The current, **safe** slice of Reyhan's Claude Code toolkit — Content, Outbound, Research and Sourcing, plus shared building blocks. Auto-refreshed on the 1st of each month.

**Excluded by design:** finance (finance-ops, invoicing, payslips), personal (mortgage, immigration, car), internal product (pulse-*), maintenance (skill-audit), and client-private content instances. Never contains `.env` or keys.

## Install
```bash
git clone git@github.com:reyhanrecruitergtm/skills-for-team.git
cd skills-for-team
cp .env.example .env      # add your own keys
claude                    # skills auto-load from .claude/
```
Or copy `.claude/skills/*` + `.claude/agents/*` into your own `~/.claude/`.

## What's inside (45 skills)
- affiliate-tracker
- agreement-generator
- april-weekly-leads
- browser-use
- business-mentor-advisor
- candidate-list
- candidate-sourcing
- clay-table-builder
- client-fulfillment
- community-os
- competitor-research
- content-os
- copy-engine
- cost-control
- email-deliverability
- email-writer
- event-planner
- graphic-generation
- gtm-delivery
- gtm-engine
- gtme-training
- humanizer
- launch-plan
- list-quality-scorecard
- market-pulse
- newsletter-writer
- outbound-os-claude
- outbound-os-setup
- personalization-subagent-pattern
- pipeline-cleanup
- pipeline-nudge
- proposal-followup-sequence
- proposal-generator
- qa-deck-generator
- qa-topic-scout
- research
- rgtm-outbound
- roadmap-generator
- seo-engine
- skool-classroom
- sourcing-os
- stardex
- website
- youtube-content
- youtube-planner

Plus `.claude/agents/` (research + the two ContentOS QA gates), `.claude/rules/`, and `context/` (business context, no finance).

> Snapshot of Reyhan's workspace. Improvements flow one way (his workspace -> here) each month. Open an issue/PR to suggest changes.
