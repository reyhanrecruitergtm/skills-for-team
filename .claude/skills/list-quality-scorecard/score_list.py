#!/usr/bin/env python3
"""List Quality Scorecard — grade a lead/candidate CSV across 8 dimensions before sending.

Adapted for RecruiterGTM from GrowthEngineX's `list-quality-scorecard` (open source,
github.com/growthenginenowoslawski/coldoutboundskills). Stdlib only — no deps.

Usage:
  python3 score_list.py --list leads.csv [--out scorecard.md] \
      [--titles "Founder,CEO,Head of Talent"] \
      [--industries "Software,Staffing"] \
      [--headcount-min 30 --headcount-max 150]

Weights (per source): Email verification 2x, ICP fit 2x, Title relevance 1.5x, rest 1x.
Grades: A+>=93, A>=90, B>=80, C>=70, D>=60, F<60.
"""
import argparse
import csv
import re
from collections import Counter

VERIFY_COLS = ["verified", "email_status", "verification_status", "esp_status",
               "email_verification", "verification", "status"]
VERIFY_GOOD = {"valid", "verified", "deliverable", "safe", "true", "ok", "pass", "good", "accept_all_but_deliverable"}
GENERIC_LOCALPARTS = {"info", "contact", "hello", "admin", "sales", "support",
                      "team", "office", "mail", "help", "enquiries", "inquiries", "hi"}
BAD_TITLE_PATTERNS = ["intern", "assistant", "coordinator", "student", "part-time",
                      "part time", "retired", "trainee", "apprentice", "volunteer"]
FAKE_NAMES = {"admin", "info", "sales", "contact", "hello", "team", "support", "test", "user", "na", "n/a"}


def pick(header_map, *names):
    for n in names:
        if n.lower() in header_map:
            return header_map[n.lower()]
    return None


def letter_grade(score):
    if score >= 93: return "A+"
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    header_map = {}
    if rows:
        for k in rows[0].keys():
            if k is not None:
                header_map[k.strip().lower()] = k
    return rows, header_map


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", required=True)
    ap.add_argument("--out")
    ap.add_argument("--titles", default="")
    ap.add_argument("--industries", default="")
    ap.add_argument("--headcount-min", type=int, default=None)
    ap.add_argument("--headcount-max", type=int, default=None)
    a = ap.parse_args()

    rows, H = load(a.list)
    total = len(rows)
    if total == 0:
        print("Empty list."); return

    c_email = pick(H, "email", "email_address", "work_email")
    c_first = pick(H, "first name", "first_name", "firstname")
    c_last = pick(H, "last name", "last_name", "lastname")
    c_title = pick(H, "job_title", "title", "job title", "position")
    c_domain = pick(H, "company_domain", "domain", "website")
    c_industry = pick(H, "company_industry", "industry")
    c_headcount = pick(H, "company_headcount", "headcount", "employees", "employee_count", "size")
    c_verify = next((H[v] for v in VERIFY_COLS if v in H), None)

    titles = [t.strip().lower() for t in a.titles.split(",") if t.strip()]
    industries = [i.strip().lower() for i in a.industries.split(",") if i.strip()]

    def emails():
        return [(r.get(c_email) or "").strip().lower() for r in rows] if c_email else []

    issues, dims = [], []

    # 1. Email verification coverage (weight 2)
    if c_verify:
        cov = sum(1 for r in rows if (r.get(c_verify) or "").strip())
        good = sum(1 for r in rows if (r.get(c_verify) or "").strip().lower() in VERIFY_GOOD)
        cov_pct = cov / total * 100
        s = round(cov_pct) if cov_pct >= 50 else round(cov_pct * 0.4)
        dims.append(("Email verification", s, 2, f"{cov_pct:.0f}% carry a verification result; {good} marked valid"))
        if cov_pct < 100:
            issues.append(f"{total - cov} of {total} emails are unverified — run your verifier (Instantly / MillionVerifier / ZeroBounce) before sending")
    else:
        dims.append(("Email verification", -1, 2, "no verification column found"))
        issues.append("NO verification data in the list — verify every email before this list touches a campaign")

    # 2. Duplicate emails (weight 1)
    if c_email:
        es = [e for e in emails() if e]
        dupes = len(es) - len(set(es))
        dupe_pct = dupes / total * 100
        s = max(0, round(100 - dupe_pct * 20))
        dims.append(("Duplicate emails", s, 1, f"{dupe_pct:.1f}% duplicate emails ({dupes})"))
        if dupe_pct > 1:
            issues.append(f"{dupes} duplicate emails ({dupe_pct:.1f}%) — deduplicate before upload")
    else:
        dims.append(("Duplicate emails", -1, 1, "no email column"))

    # 3. Duplicate domains (weight 1)
    doms = []
    if c_domain:
        doms = [(r.get(c_domain) or "").strip().lower() for r in rows if (r.get(c_domain) or "").strip()]
    elif c_email:
        doms = [e.split("@")[1] for e in emails() if "@" in e]
    if doms:
        counts = Counter(doms)
        avg = len(doms) / len(counts)
        s = 100 if avg < 2 else (60 if avg <= 5 else 30)
        over = [(d, n) for d, n in counts.items() if n >= 5]
        dims.append(("Duplicate domains", s, 1, f"avg {avg:.1f} leads/domain across {len(counts)} domains"))
        if over:
            hit = sum(n for _, n in over)
            issues.append(f"{hit} leads cluster on {len(over)} domains (5+ each) — cap per-domain concentration (2-3 max)")
    else:
        dims.append(("Duplicate domains", -1, 1, "no domain/email column"))

    # 4. Title relevance (weight 1.5) — needs --titles
    tvals = [(r.get(c_title) or "").strip().lower() for r in rows] if c_title else []
    if c_title and titles:
        match = sum(1 for t in tvals if any(k in t for k in titles))
        pct = match / total * 100
        s = 100 if pct >= 80 else (50 if pct >= 40 else 0)
        dims.append(("Title relevance", s, 1.5, f"{pct:.0f}% of titles match your ICP title list"))
        if pct < 80:
            issues.append(f"{total - match} titles ({100 - pct:.0f}%) don't match your ICP titles — title drift, tighten the source filter")
    else:
        dims.append(("Title relevance", -1, 1.5, "pass --titles to score" if c_title else "no title column"))

    # 5. Bad-title detection (weight 1)
    if c_title:
        bad = sum(1 for t in tvals if any(p in t for p in BAD_TITLE_PATTERNS))
        bad_pct = bad / total * 100
        s = max(0, round(100 - bad_pct * 10))
        dims.append(("Bad-title detection", s, 1, f"{bad_pct:.1f}% match bad-title patterns ({bad})"))
        if bad_pct > 2:
            issues.append(f"{bad} bad titles (intern/assistant/coordinator/etc, {bad_pct:.1f}%) — filter by seniority")
    else:
        dims.append(("Bad-title detection", -1, 1, "no title column"))

    # 6. Catch-all / generic density (weight 1)
    if c_email:
        gen = sum(1 for e in emails() if e and "@" in e and e.split("@")[0] in GENERIC_LOCALPARTS)
        gen_pct = gen / total * 100
        s = 100 if gen_pct < 5 else (50 if gen_pct <= 15 else 0)
        dims.append(("Catch-all/generic density", s, 1, f"{gen_pct:.1f}% generic inboxes ({gen})"))
        if gen_pct >= 5:
            issues.append(f"{gen} generic addresses (info@/contact@/etc, {gen_pct:.1f}%) — drop or deprioritize")
    else:
        dims.append(("Catch-all/generic density", -1, 1, "no email column"))

    # 7. ICP fit (weight 2) — needs industries and/or headcount range
    if (industries or a.headcount_min is not None) and (c_industry or c_headcount):
        fit = 0
        for r in rows:
            ok = True
            if industries and c_industry:
                ind = (r.get(c_industry) or "").strip().lower()
                ok = ok and any(i in ind for i in industries)
            if a.headcount_min is not None and c_headcount:
                hc = re.sub(r"[^0-9]", "", (r.get(c_headcount) or ""))
                hc = int(hc) if hc else 0
                lo = a.headcount_min or 0
                hi = a.headcount_max or 10 ** 9
                ok = ok and (hc == 0 or (lo <= hc <= hi))
            fit += 1 if ok else 0
        pct = fit / total * 100
        s = round(pct)
        dims.append(("ICP fit", s, 2, f"{pct:.0f}% match declared industry/headcount ICP"))
        if pct < 80:
            issues.append(f"{total - fit} leads ({100 - pct:.0f}%) outside your declared ICP — filter by industry + headcount")
    else:
        dims.append(("ICP fit", -1, 2, "pass --industries / --headcount-min|max to score"))

    # 8. Name quality (weight 1) — enforces First/Last split per feedback_csv_names_split
    if c_first and c_last:
        good = 0
        for r in rows:
            fn = (r.get(c_first) or "").strip()
            ln = (r.get(c_last) or "").strip()
            if not fn or not ln:
                continue
            if fn.isupper() and len(fn) > 3:
                continue
            if fn.lower() in FAKE_NAMES or ln.lower() in FAKE_NAMES:
                continue
            if "@" in fn or "@" in ln:
                continue
            good += 1
        pct = good / total * 100
        s = round(pct)
        dims.append(("Name quality", s, 1, f"{pct:.0f}% have clean first + last names"))
        if pct < 95:
            issues.append(f"{total - good} rows have missing/dirty names ({100 - pct:.0f}%) — fix First/Last split before personalizing")
    else:
        dims.append(("Name quality", -1, 1, "missing First Name / Last Name columns — split required (feedback_csv_names_split)"))
        issues.append("List is missing separate First Name + Last Name columns — required before send (feedback_csv_names_split)")

    # Weighted grade
    appl = [d for d in dims if d[1] >= 0]
    tw = sum(d[2] for d in appl)
    overall = round(sum(d[1] * d[2] for d in appl) / tw) if tw else 0
    grade = letter_grade(overall)

    # Output
    out = []
    out.append("# List Quality Scorecard\n")
    out.append(f"**File:** `{a.list}` ({total} rows)")
    out.append(f"**Grade:** {grade} ({overall}/100)\n")
    out.append("| # | Dimension | Score | Note |")
    out.append("|---|-----------|-------|------|")
    for i, (name, s, w, note) in enumerate(dims, 1):
        out.append(f"| {i} | {name} | {'n/a' if s < 0 else f'{s}/100'} | {note} |")
    out.append("")
    if issues:
        out.append("## Top issues to fix")
        for i, iss in enumerate(issues[:6], 1):
            out.append(f"{i}. {iss}")
        out.append("")
    out.append("## Pre-send checklist")
    for line in ["Deduplicate by email", "100% email verification before send",
                 "Drop generic/catch-all if >5%", "Filter bad titles + off-ICP rows",
                 "Cap per-domain concentration (2-3 max)", "First + Last name columns present",
                 "Re-run this scorecard after filtering"]:
        out.append(f"- [ ] {line}")
    out.append("")
    verdict = {"A+": "Ship it.", "A": "Ship it.", "B": "Minor fixes, then send.",
               "C": "Fix the top 3 issues first.", "D": "Serious cleanup required.",
               "F": "Do not send. Rebuild the list."}[grade]
    out.append(f"**Verdict: {grade} — {verdict}**")

    text = "\n".join(out)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"Wrote {a.out}\n")
    print(text)


if __name__ == "__main__":
    main()
