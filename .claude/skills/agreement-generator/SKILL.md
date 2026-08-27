# Agreement Generator Skill

Generate PDF service agreements for RecruiterGTM managed pilots.

---

## Locked Rules

### A. No outcome commitments inside the agreement
- A1. NEVER add target conversation counts, placement counts, meeting volumes, or revenue figures to any section of a signed agreement. Benchmarks (5-10 DM convos/mo, 30-50 candidate convos/mo, 50k-100k impressions/mo) live in proposals and sales conversations ONLY.
- A2. Section 1 (Scope) lists ONLY: 1.1 What Is Included · 1.2 Community Access · 1.3 What Is Not Included · 1.4 Additional Projects. No "Target Outcome" subsection. Ever.
- A3. The ONLY place outcome language appears in the contract is Section 8 (Limitation of Liability), which DISCLAIMS guarantees ("RecruiterGTM makes no guarantees regarding specific revenue outcomes, response rates, or meeting volumes…").
- A4. Sole exception: client explicitly asks for a benchmark in the contract AND Reyhan confirms for that specific deal. Justin Daleo's "5 qualified conversations/month" in Section 2.2 was an exception — never copy into other agreements. If another client asks, flag to Reyhan before adding.

### B. Legal entity
- B1. Use RecruiterGTM LLC, 447 Broadway, NY 10013. **WYOMING governing law** (state of formation). Old entity (The Ops Agent Lda.) is retired — never use on new agreements.
- B0. **Agreement naming (locked 2026-07-02).** Every agreement title AND PDF filename starts with **"RecruiterGTM"**, never a bare "GTM". E.g. "RecruiterGTM Talent Placement Agreement - [Client]", "RecruiterGTM Engine Management Service Agreement". Applies to both the on-page header title and the saved filename. Rename any "GTM ..." title/filename to "RecruiterGTM ...".
- B0-2. **Save location (locked 2026-07-02).** Every agreement PDF copies to **`~/Desktop/agreements/`** — the canonical home for ALL agreements. This is the exception to the general `~/Desktop/Clients/<client>/` deliverable rule; agreements do NOT go in per-client Desktop folders. Keep the source generator script in `projects/<client>/`.
- B2. **Client service agreements use the SHORT address and NO EIN.** The SERVICE PROVIDER block reads only "RecruiterGTM LLC / 447 Broadway / New York, NY 10013, USA / Represented by: Reyhan Khan, CEO / reyhan@recruitergtm.com". Do NOT add "2nd Floor, 3452" suite detail. Do NOT add EIN 35-2960233. The full address + EIN are reserved for invoices, the officer employment contract, and banking/KYC docs — never on client-facing service agreements. (Locked 2026-06-01.)
- B3. **Governing law is Wyoming (locked 2026-06-04).** RecruiterGTM LLC is a Wyoming-formed LLC (filed 2026-04-30). All new agreements use Wyoming governing law and Wyoming court jurisdiction. NY is the mailing address only. Do NOT use New York governing law on any new agreement. Standard clause: *"This Agreement shall be governed by and construed in accordance with the laws of the State of Wyoming, USA (the state of formation of RecruiterGTM LLC). Any disputes arising under this Agreement shall be subject to the exclusive jurisdiction of the courts of Wyoming."*

### C. Community access clause
- C1. Every pilot agreement MUST include the 12-month community access clause (Q&As, courses, 1:1 messaging from Reyhan + GTM Manager). Never skip. Detail in `/memory/reference_agreement_community_clause.md`.
- C2. **Existing community members (locked 2026-08-05, Reyhan — Youri Pinard agreement):** when the client already holds a community membership from a prior purchase, Section 1.2 references that membership as SEPARATE, running on its own original 12-month term, and states the agreement "does not modify, extend, or renew" it. Never restate the 12 months as starting from the agreement's Effective Date — that silently renews a membership they already paid for.

### D. Standard deliverables — cross-check before shipping (locked 2026-06-04)
- D1. **Before finalizing Section 1.1 "What Is Included" for ANY OutboundOS or SourcingOS agreement, cross-check `/memory/reference_standard_deliverables.md`.** Every locked deliverable in that file must appear in the agreement. No exceptions.
- D2. **SourcingOS-specific reminder:** the deliverables list MUST include **"4 evergreen role pipelines running in parallel"** (one funnel per repeatable open role). Always **4**. After listing the 4 roles, ALWAYS add that they can be swapped for any other roles at the client's preference during the engagement. Non-negotiable and was missed once already — never skip again.
- D3. **OutboundOS-specific reminder:** the deliverables list MUST include **4 custom intent playbooks (signal-triggered sequences)** plus value-first copywriting per playbook. Always say **4** — never "3-4" or any range. Don't compress these into one line.
- D4. **Why locked:** Reyhan flagged 2026-06-04 that the 4 SourcingOS role pipelines were missed in Mo Adris's agreement. The standard deliverables memory file is the canonical source — always check it before locking Section 1.1.

### E. Visual theme — black & white only (locked 2026-07-22)
- E1. Agreements are strictly black & white. Section headings, title, and divider rules are BLACK — never the brand violet (#8A00FF) or any other accent color. Body text black/dark grey only.
- E2. This applies to every agreement output (PDF, docx, HTML print source) — client service agreements, officer/employment agreements, talent placement agreements, all of them. Brand color stays in proposals, decks, and marketing docs; never in agreements.

---

## How to Invoke

"Generate agreement for [client name]" or "Build contract for [client]" → `/agreement-generator`

---

## Standard Agreement Template

Every agreement follows the Daniel Cheetham template structure:

### Header
- Title: "RecruiterGTM Engine Management Service Agreement" (always prefix "RecruiterGTM", never a bare "GTM" — see B0)
- Subtitle: "90-Day Managed Pilot - [Service(s)]"
- Effective Date + Service Commencement Date

### Parties Table
- SERVICE PROVIDER: **RecruiterGTM LLC**, 447 Broadway, New York, NY 10013, USA, Reyhan Khan, CEO, reyhan@recruitergtm.com
  - (Legacy entity "The Ops Agent Lda. (Portugal)" is RETIRED as of May 2026 — never use on new agreements. See `memory/reference_legal_entity.md`.)
- CLIENT: [Name], [Company], [Address if known], [Email]

### Section 1: Scope of Services
1.1 What Is Included:
- Adapt based on service(s): OutboundOS, SourcingOS, ContentOS, or combination
- Standard deliverables from memory (reference_standard_deliverables.md)
- Always include: ICP mapping, intent playbooks, value-first copywriting, multichannel outreach, A/B testing, GTM Engineer, Slack channel, weekly reporting call, monthly performance review

1.2 RecruiterGTM Community Access (ALWAYS INCLUDE):
- 12 months Skool community access
- Weekly Q&A calls with Reyhan
- Full course library
- Templates, playbooks, SOPs
- 1:1 messaging from Reyhan
- 1:1 messaging from GTM Manager
- Network of 72+ recruitment agency owners (community size as of May 2026; update as the community grows)

1.3 What Is Not Included:
- Response handling, follow-up conversations, meeting booking from initial replies

1.4 Additional Projects:
- Separate written scope + additional fees for out-of-scope work

### Section 2: Engagement Structure
2.1 90-Day Managed Pilot (Months 1-3):
- Month 1: Research, Build & First Launch
- Month 2: Optimisation & Split Testing
- Month 3: Validation & Scaling

2.2 Automatic Renewal:
- Auto-renews into 6-month managed service at same rate
- 14 days written notice to discontinue before pilot ends
- 30 days notice to exit during 6-month extension

### Section 3: Fees and Payment
- Monthly retainer based on services:
  - 1 system: $2,500/month
  - 2 systems: $4,000/month
  - 3 systems (full engine): $5,000-$6,500/month (varies by client)
- Charged automatically every 30 days
- 5% late fee after 7 days
- Non-refundable once commenced

### Section 4: Non-Circumvention
- 12 months post-termination
- Buy-out fee: USD $8,000

### Section 5: Intellectual Property
- Frameworks = RecruiterGTM IP
- Everything built in client accounts = client owned
- Full ownership and access at all times

### Section 6: Confidentiality
- Standard mutual NDA clause

### Section 7: Termination
- 90-day pilot = fixed commitment
- 6-month extension = 30 days written notice
- Termination for cause = 10 business days to remedy

### Section 8: Limitation of Liability
- Capped at 3 months fees
- No guarantees on revenue, response rates, or meetings

### Section 9: Governing Law
- **State of Wyoming, USA** (RecruiterGTM LLC is a Wyoming-formed LLC, filed 2026-04-30). NY 447 Broadway is mailing address only. Use the locked B3 clause verbatim.

### Section 10: Entire Agreement
- Standard clause

### Signatures
- Service Provider: Reyhan Khan, CEO, date = agreement date
- Client: [Name], [Company], date = blank

---

## Pricing Reference

| Services | Monthly Rate |
|----------|-------------|
| 1 system (OutboundOS OR SourcingOS OR ContentOS) | $2,500/month |
| 2 systems | $4,000/month |
| 3 systems (full engine) | $5,000-$6,500/month |

Currency: USD unless client is European (then EUR)

### VIP Tier (Skool — Paid in Full)

- **$7,497 USD paid in full upfront via Skool VIP tier checkout** — an alternative to the monthly retainer for 1-system OutboundOS pilots.
- Replaces monthly billing entirely. No recurring charge.
- Buyer benefit: weekly 1:1 strategic calls with Reyhan for the full 12 weeks (vs. monthly review on standard tier).
- All other deliverables identical to the standard 90-day OutboundOS pilot.
- Confirm with Reyhan whether the client agreed VIP tier before applying this pricing — it is not the default.
- First VIP tier agreement: Adrian Muñoz (ALAC HR Solutions), 26 May 2026 — see `projects/adrian-munoz/`.

**When VIP applies, agreement structural differences:**
- Section 3 becomes one-time payment via Skool (not monthly), non-refundable after Service Commencement Date.
- Section 2 drops auto-renewal — pilot ends at 90 days; continuation requires mutual written agreement at standard monthly rate.
- Section 8 (Limitation of Liability) caps at the program fee paid (not 3 months fees).

---

## Generation Process

1. Copy the template Python script from Daniel Cheetham's agreement
2. Swap client name, company, email, address
3. Update subtitle with service(s)
4. Update scope section 1.1 with relevant deliverables
5. Update monthly retainer amount
6. Update signature block
7. Run Python script to generate PDF
8. Copy to ~/Desktop/

---

## What NOT to Change

- Non-circumvention clause (always 12 months, $8k buy-out)
- Community access clause (always 12 months, always included)
- Governing law (always State of Wyoming — RecruiterGTM LLC is Wyoming-formed, filed 2026-04-30)
- Limitation of liability (always 3 months fees)
- IP ownership structure (frameworks = ours, builds = theirs)
- Auto-renewal structure (90 days → 6 months OR month-by-month by mutual agreement, depending on what was agreed in the proposal)

---

## Template Location

Master template: `projects/generate_daniel_cheetham_agreement.py`
All agreements stored in: `projects/` and copied to `~/Desktop/`
