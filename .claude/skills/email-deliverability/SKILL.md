# Skill: Email Deliverability

Diagnose, fix, and monitor email deliverability for RecruiterGTM's sending domains. Covers Reyhan's main Gmail (Google Workspace on `recruitergtm.com`) plus any cold outbound infrastructure used for community/pilot client campaigns.

This is a discrete operational skill. Email deliverability is its own world. It doesn't get baked into proposal-generator or sourcing-os.

---

## How to Invoke

`/email-deliverability` followed by:
- `audit` — full diagnostic on the main domain
- `audit <domain>` — same but on a specific cold domain
- `mail-tester` — run the one-shot mail-tester score from Reyhan's primary inbox
- `dmarc-reports` — pull the latest aggregate reports from operations@recruitergtm.com (or whatever mailbox is set as `rua`)
- `add cold domain <new-domain>` — set up auth on a new cold outbound domain
- `escalate` — produce a Folderly/MailBrace handoff brief with current state + history

---

## Locked Facts (Reyhan's setup, locked 2026-06-12)

- **Primary sending domain:** `recruitergtm.com` on Google Workspace
- **Primary sending address:** `reyhan@recruitergtm.com`
- **Domain age:** registered ~December 2025 (6 months old as of June 2026)
- **Cold outbound from `recruitergtm.com`:** NEVER. Strict rule. Cold goes on separate lookalike domains.
- **Cold outbound stack:** Instantly, Smartlead, Lemlist (per `reference_tool_stack.md`)
- **Postmaster Tools verified:** 12 June 2026 (data populates 24-48h after verification + minimum daily volume to Gmail)
- **DMARC aggregate reports route to:** `operations@recruitergtm.com` (Daniyal's mailbox)
- **Current DMARC state:** `p=none` (monitoring only, no enforcement)

---

## Locked Rules

### A. Never run cold campaigns from recruitergtm.com

- A1. The main domain hosts business mail only: client comms, proposals, internal team, replies. Anything sent through Reyhan's Instantly/Smartlead/Lemlist accounts uses a SEPARATE domain (e.g. `recruitergtm.co`, `recruitergtm-team.com`, `getrecruitergtm.com`).
- A2. Buying a separate cold domain is the prerequisite to running any volume campaign. Without it, every cold burn damages the main domain's reputation for proposal sends, client mail, and inbound replies.
- A3. Use 3-5 separate cold domains across rotating inboxes. Per cold domain, max 3-5 inboxes. Per inbox, max 30-50 sends/day on cold mail.

### B. Proposal HTML files are never email attachments

- B1. The 1.6MB HTML proposals we generate (community-proposals-batch, etc.) MUST be hosted on `recruitergtm.com/proposals/<client-slug>` and sent as a link. Never attached.
- B2. Large HTML attachments are a top Gmail 2026 spam signal. We have lost inbox placement to this multiple times.
- B3. The proposal-send email template (per `reference_proposal_send_email_template.md`) already says "Proposal HTML file is attached" — this instruction needs updating to "Proposal is at this link, please open in browser." Pending fix.

### C. Batched proposal sends are spaced, not blasted

- C1. When sending a batch of similar proposals (Quentin, Syra, John, Matt, Dan, Leanne — all on the same day), space sends at least 30 minutes apart per recipient.
- C2. Better: stagger the batch across 2-3 days. Same template + same domain + same hour = Gmail flags it as bulk pattern.
- C3. Or use slight personalization in subject + opener variations to break pattern-similarity detection.

### D. DMARC migration path

- D1. Stay at `p=none` until DMARC reports are being read for at least 14 consecutive days with clean results (no third-party spoofing, all legit senders authenticated).
- D2. Move to `p=quarantine; pct=10` (quarantine 10% of failed mail). Monitor 7 days.
- D3. Step pct up to 25 → 50 → 100 over 4 weeks if no false-quarantine of legit mail.
- D4. Final state: `p=reject; pct=100`. Provides strongest protection. Don't skip the gradient — going straight to reject can blackhole legit mail from third-party senders we forgot to authenticate (e.g. Lemlist, Beehiiv, Whop).
- D5. EVERY external sender (Lemlist, Beehiiv, Instantly, Whop, Smartlead) that sends from `@recruitergtm.com` needs to be added to SPF + have its own DKIM CNAME before DMARC enforces.

### E. Tooling allowlist (the only tools we use for diagnostics)

- E1. **[Google Postmaster Tools v2](https://postmaster.google.com)** — official Gmail reputation feedback. Free. Definitive.
- E2. **[Microsoft SNDS](https://sendersupport.olc.protection.outlook.com/snds/)** — Outlook/Hotmail equivalent. Free.
- E3. **[mail-tester.com](https://mail-tester.com)** — one-shot 10-point score. Use after any auth change.
- E4. **[MXToolbox SuperTool](https://mxtoolbox.com/SuperTool.aspx)** — DNS + blacklist check. Free.
- E5. **[GlockApps](https://glockapps.com)** — multi-provider seed test. ~$59/mo. Use only when running real campaigns and want true inbox placement data.
- E6. **[Mailmodo's DMARC report parser](https://dmarcian.com)** OR **[Postmark's DMARC](https://dmarc.postmarkapp.com/)** for reading aggregate reports — manual parsing of raw XML is masochism.
- E7. Anything else (random "deliverability score" websites, free spam checkers, "DKIM analyzers") is bullshit. Don't use.

### F. Paid services tier (escalation path)

If diagnostics show real damage and we can't fix in 2 weeks:

- F1. **[MailBrace](https://mailbrace.com)** — best fit for our cold outbound use case (Instantly/Smartlead/Lemlist managed). $1k-3k/mo.
- F2. **[Folderly](https://folderly.com)** — pure deliverability consultancy with cold-outreach module. $200-600/mo managed, $2k+ enterprise.
- F3. **[Mailsoar](https://mailsoar.com)** — premium, 20+ yr team, enterprise pricing.
- F4. Never engage a consultant without running E1-E4 first. The consultant will charge $2k to run them for you.

---

## The Diagnostic Flow (in this order, no shortcuts)

### Step 1: Auth state (always start here)

Run via Bash:
```bash
echo "--- SPF ---" && dig +short TXT <domain> | grep -i spf
echo "--- DMARC ---" && dig +short TXT _dmarc.<domain>
echo "--- MX ---" && dig +short MX <domain>
echo "--- DKIM google ---" && dig +short TXT google._domainkey.<domain> | head -1
```

Pass conditions:
- SPF includes `_spf.google.com` (for Google Workspace) plus any other authorized senders
- DMARC record exists with valid `v=DMARC1` syntax
- MX points to expected provider
- DKIM `google._domainkey` selector resolves to a `v=DKIM1; k=rsa; p=...` record

If any of those fail, that's the issue. Stop here and fix.

### Step 2: Blacklist + DNS health

Check [MXToolbox SuperTool](https://mxtoolbox.com/SuperTool.aspx?action=blacklist:<domain>) for the domain. Any blacklist hits = immediate problem.

### Step 3: One-shot send score

From the primary inbox, send a single email to the address mail-tester.com gives. Read the report. Anything below 9/10 = something specific to fix (it'll tell you exactly what).

### Step 4: Postmaster Tools data (24-48h after verification + with volume)

Open https://postmaster.google.com → pick the domain → review:
- **IP reputation:** High / Medium / Low / Bad
- **Domain reputation:** same scale
- **Spam rate:** target <0.10%, danger >0.30%
- **Authentication:** % of SPF, DKIM, DMARC pass rate
- **Encryption:** % TLS encrypted

If any reputation = Low or Bad, document the trend and move to step 5.

### Step 5: DMARC report review

The `rua=mailto:` address (currently `operations@recruitergtm.com`) receives aggregate XML reports daily from Gmail/Outlook/Yahoo. Set them up to feed into [dmarcian](https://dmarcian.com) or [postmarkapp.com/dmarc](https://dmarc.postmarkapp.com/) (free) so they're readable.

Look for:
- Spoofing attempts (third party sending as @recruitergtm.com)
- Legitimate senders failing alignment (e.g. Beehiiv sends mail but DKIM doesn't align — that's a fix)
- Volume per source

### Step 6: Multi-provider seed test (only if real campaign issue)

[GlockApps](https://glockapps.com) sends a test campaign from your sending infrastructure to a seed list across 50+ inbox providers. Tells you actual inbox vs spam vs missing placement per provider. Useful when:
- You're running a real cold campaign and want true placement data
- You suspect Outlook is blocking but Gmail is fine (or vice versa)
- You're about to launch a major campaign and want to validate first

---

## Google Workspace Auth Setup (reference, if a new domain joins the stack)

For any new domain on Google Workspace:

1. **MX records:** Use Google Workspace's setup wizard. Standard Google MX records.
2. **SPF:** Add `v=spf1 include:_spf.google.com ~all` as TXT on root.
3. **DKIM:** Admin console → Apps → Google Workspace → Gmail → Authenticate email → Generate new record (2048-bit). Add the returned CNAME (selector: `google`, target: `google._domainkey.<domain>.gappssmtp.com`). Click "Start authentication" once DNS propagates.
4. **DMARC:** Add TXT on `_dmarc.<domain>` with: `v=DMARC1; p=none; rua=mailto:operations@recruitergtm.com; ruf=mailto:operations@recruitergtm.com; fo=1; adkim=r; aspf=r; pct=100`
5. **Wait 24h**, then verify all four with `dig`.

---

## Cold Outbound Domain Setup

For separate cold infrastructure (Instantly/Smartlead/Lemlist):

1. **Buy 3-5 lookalike domains** (e.g. `recruitergtm.co`, `getrecruitergtm.com`, `recruitergtm-team.com`). Avoid `mail.recruitergtm.com` or any subdomain of the main — main domain reputation is shared with subdomains.
2. **3-5 inboxes per cold domain**. Standard names: `reyhan@`, `r.khan@`, `outreach@`.
3. **SPF + DKIM + DMARC on each cold domain.** SPF includes the cold-tool's IPs (Instantly, Smartlead, Lemlist each give specific includes). DKIM via their setup. DMARC at `p=none` for first 30 days, then graduate.
4. **Custom tracking domain on each cold domain.** Set CNAME `track.<cold-domain>` per tool's instructions. Never use the tool's shared tracking domain.
5. **Warmup 4 weeks minimum** before any real send. Smartlead and Instantly have built-in warmup. Lemlist has lemwarm. Never stop warmup, even after launching real campaigns.
6. **Volume cap:** 30-50 sends/inbox/day on cold mail. Never above 100/inbox even at peak.

---

## Sending Hygiene Rules

These apply to BOTH main domain and cold domains:

- **No URL shorteners.** No bit.ly, no t.ly. Use bare URLs or your own custom tracking domain.
- **Plain text or minimal HTML.** No tracking pixels. No images in cold mail.
- **No attachments above 200KB** in cold mail. For proposal sends, host on `recruitergtm.com/proposals/` and link.
- **One link max** in cold mail (or zero in the first touch).
- **Real reply-to address** — never `noreply@` for outbound business mail.
- **One-click unsubscribe header** (RFC 8058) on every cold send. Most cold tools add this automatically in 2026 — verify in raw headers.
- **List hygiene** — verify every address via Million Verifier or ZeroBounce before send. Drop catch-alls, risky, role-based, unknown.
- **Bounce rate above 2%** = stop campaign immediately, clean list, re-warm.

---

## Reputation Rebuild Playbook (if domain rep is damaged)

If Postmaster shows Low or Bad reputation on the main domain:

1. **Stop all bulk sends** for 14 days. Including proposal blasts.
2. **Send only 1:1, value-first replies** during the freeze (real human conversations).
3. **Confirm all auth still passes** (Postmaster Authentication tab).
4. **Move proposal HTML to hosted links** (kill the attachment habit).
5. **After 14 days clean**, resume sends slowly — 5/day, then 10, then 20, ramping over 2 weeks back to normal volume.
6. **If rep doesn't recover after 30 days**, escalate to paid help (F1-F3 above).

---

## Standard Operating Cadence

- **Daily:** Glance Postmaster Tools for spam rate spikes.
- **Weekly:** Run Step 1 (auth check) + Step 2 (blacklist) on the main domain and every cold domain. Log results to `projects/email-deliverability/health-log.csv`.
- **Monthly:** Read aggregated DMARC report summary. Add any newly-discovered legitimate senders to SPF.
- **Quarterly:** Run Step 6 (GlockApps seed test) if running active cold campaigns.

---

## What NOT To Do

- Don't pay for "free deliverability score" tools that aren't on the E1-E7 list. They're affiliate-driven SEO bait.
- Don't change DMARC policy in big jumps. Always step gradient.
- Don't add cold tools to the main domain's SPF — that's how main domain reputation gets contaminated.
- Don't engage a paid consultant before running steps 1-4 yourself.
- Don't troubleshoot deliverability by guessing. Always start with data (Postmaster, mail-tester).

---

## Files

- `projects/email-deliverability/health-log.csv` — weekly diagnostic log (to be created)
- `projects/email-deliverability/cold-domains.csv` — list of authorized cold outbound domains + their auth state
- `projects/email-deliverability/dmarc-reports/` — archive of weekly DMARC summaries (when set up)
