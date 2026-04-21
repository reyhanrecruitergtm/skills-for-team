# Agreement Generator Skill

Generate PDF service agreements for RecruiterGTM managed pilots.

---

## How to Invoke

"Generate agreement for [client name]" or "Build contract for [client]" → `/agreement-generator`

---

## Standard Agreement Template

Every agreement follows the Daniel Cheetham template structure:

### Header
- Title: "GTM Engine Management Service Agreement"
- Subtitle: "90-Day Managed Pilot - [Service(s)]"
- Effective Date + Service Commencement Date

### Parties Table
- SERVICE PROVIDER: The Ops Agent Lda. (trading as RecruiterGTM), Almada, Portugal, Reyhan Khan, CEO
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
- Network of 50+ recruitment agency owners

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
- Portugal

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
- Governing law (always Portugal)
- Limitation of liability (always 3 months fees)
- IP ownership structure (frameworks = ours, builds = theirs)
- Auto-renewal structure (90 days → 6 months)

---

## Template Location

Master template: `projects/generate_daniel_cheetham_agreement.py`
All agreements stored in: `projects/` and copied to `~/Desktop/`
