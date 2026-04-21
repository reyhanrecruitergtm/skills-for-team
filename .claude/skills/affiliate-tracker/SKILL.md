# Skill: Affiliate Tracker

Track and manage affiliate referrals for Pin.com, Clay, Lemlist, Recruiterflow, and other tools.

## When to invoke
- When a new client is onboarded and recommended any affiliate tool
- When Reyhan says "log affiliate", "track referral", or mentions a client using Pin.com/Clay/Lemlist/Recruiterflow
- When generating a list to send to affiliate reps for attribution claims
- When checking affiliate status or reviewing pending referrals

## Tracking Sheets (one per platform)
All sheets live in the **Affiliate Trackers** folder (ID: 1w877ZJ1SBFzb1Mijxx3WKeOSDOtq7QSV).

| Platform | Sheet Name | Sheet ID |
|----------|-----------|----------|
| Pin.com | Pin.com Affiliate Tracker 2026 | 1bsjVhbgqEzjqPZWKfTkxQ2Wnjh3o0se2GgspqbCjItY |
| Recruiterflow | Recruiterflow Affiliate Tracker 2026 | 1Hb_2urzY9a-AkLbFNVdV64JJg_JoU8QO6Ccb-GIB26o |
| Lemlist | Lemlist Affiliate Tracker 2026 | 1a98XlzL2YDC1uuvXxnQ_-MlMwvdiZbSFUMhT9R3jHOY |
| Clay | Clay Affiliate Tracker 2026 | 1PGfngPA0VfgXn_ujHiqmD7EI_Um9s1Z02gRYQE47N1I |

Each sheet is shared separately with the platform's team.

## Columns
| Column | Description |
|--------|-------------|
| Client Name | Full name of the referred client |
| Client Email | Client's email address |
| Status | Community Member / Retainer Client |
| Date Submitted | Date the referral was logged (YYYY-MM-DD) |
| Notes | Context: how they were referred, onboarding details |

## Commands

### Log a referral
When Reyhan mentions a client using an affiliate tool:
1. Identify the correct platform sheet from the table above
2. Collect: client name, email, status, and any notes
3. Append row to the platform's sheet using `manage_sheets` append operation
4. Confirm the entry was added

### Review all referrals
1. Read all 4 sheets
2. Present summary grouped by platform
3. Flag any missing emails or incomplete entries

### Generate rep email list
When Reyhan wants to send a list to a platform rep:
1. Read the specific platform's sheet
2. Format as a clean list: Client Name, Client Email, Status
3. Draft an email using the email-writer skill addressed to the rep

### Add new platform
When a new affiliate partnership is established:
1. Create a new sheet named "[Platform] Affiliate Tracker 2026"
2. Copy to the Affiliate Trackers folder
3. Add headers: Client Name, Client Email, Status, Date Submitted, Notes
4. Update this SKILL.md table with the new sheet ID

## Related Resources
- Affiliate links sheet (ID: 1Oc7s-CKyBRVhDNEk4yuGUWthod9yIoznFOO1WOd_ofw)
- Affiliate logins sheet (ID: 1qhaU2O93Zvq2YK_0M9qH_ae9yUeAibRE_lVEDqrkAGI)

## Revenue Context
Affiliates represent ~10% of RecruiterGTM revenue and growing. Every client setup with Clay, Lemlist, Pin.com, or Recruiterflow should trigger a referral log. This is passive revenue attached to fulfillment and content.
