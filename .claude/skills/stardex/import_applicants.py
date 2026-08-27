#!/usr/bin/env python3
"""
Import enriched applicants CSV into Stardex:
  - POST /v1/persons (with job_id → auto-attaches as candidate at Sourced)
  - PATCH /v1/candidates/{id}/stage → move to Applied
  - PATCH /v1/persons/{id} → set custom fields

For candidates with no real LinkedIn URL, generate a synthetic /in/applicant-{slug}-{hash}
and mark them with notes="MISSING LINKEDIN URL — synthetic placeholder, please review".

Usage:
  python3 import_applicants.py <enriched.csv> <out_log.csv> [--limit N] [--dry-run]
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# ---------- Config ----------
SENIOR_RECRUITER_JOB_ID = "47281aab-7496-45af-9a3a-363804f341b8"
APPLIED_STAGE_ID = "396ade5a-2328-4d3a-941d-bcd909aeb181"

CUSTOM_FIELDS = {
    "headshot_url":       "7e4f5a9b-0fa1-49cf-8bcd-c55c853714ca",  # url
    "tools_experience":   "f871dea0-b9fb-44a4-b614-03761baab2fe",  # string
    "international":      "5eae5d37-8557-49b1-ac4f-283ee5c54523",  # single-select Yes/No
    "job_experience":     "253c01bb-9702-4bf5-bf90-943a29112fd6",  # string
    "roles_recruited":    "5dc92314-91bb-4b39-b2b8-68f0e24ce596",  # string
    "video_comfort":      "d65329e5-94fb-443e-8bb6-d8ca599a2dfe",  # string
    "submitted_on":       "c677e732-7540-43da-989b-a53c6ce5d4ab",  # date
    "resume_url":         "0912860e-c5ee-419e-8b59-c9483332fbf0",  # url
    "biggest_achievement":"d09bff4f-6172-4b1d-8577-2b1243c2ee50",  # string
    "video_url":          "ada33d57-3fea-41ae-86df-f4d1a4a7b541",  # url
}

# CSV header → field key
CSV_MAP = {
    "Submission time":                                       "submitted_on",
    "Video Intro Link (use Loom or Tella)":                  "video_url",
    "Resume Link (Make sure it's a public link)":            "resume_url",
    "Upload your Professional Headshot (it can also be a semi formal picture)": "headshot_url",
    "Which of these tools do you have experience with":      "tools_experience",
    "Have you worked in recruitment, sales, marketing, or any people-focused role before? Please describe your experience.": "job_experience",
    "Are you comfortable recording personalised video messages for candidates and clients as part of your daily workflow? Please answer in detail": "video_comfort",
    "What is the biggest achievement of your career so far?": "biggest_achievement",
    "Have you worked for an International client in freelance or fulltime capacity before?": "international",
    "Mention all the roles you have recruited for in the past": "roles_recruited",
}

URL_FIELDS = {"headshot_url", "resume_url", "video_url"}
SINGLE_SELECT_TRUE_FALSE = {"international"}

# ---------- Stardex client ----------
BASE = "https://api.stardex.ai/v1"


def _api_key() -> str:
    import os
    if os.environ.get("STARDEX_API_KEY"):
        return os.environ["STARDEX_API_KEY"]
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        env = parent / ".env"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("STARDEX_API_KEY="):
                    return line.split("=", 1)[1].strip()
    raise SystemExit("STARDEX_API_KEY missing")


API_KEY = _api_key()


def _request(method: str, path: str, body: dict | None = None) -> dict:
    url = BASE + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {API_KEY}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body_txt = e.read().decode("utf-8", "replace")
        try:
            return json.loads(body_txt)
        except Exception:
            return {"success": False, "error": {"status": e.code, "raw": body_txt[:300]}}


# ---------- Helpers ----------
def _append_err(existing: str, label: str, resp: dict) -> str:
    """Stardex returns error envelopes in 2 shapes:
      A: {success:False, error:{code, message}}
      B: {message, error, statusCode}  (Fastify-style 404s/500s)
    Render either to a short string and chain onto existing.
    """
    msg = ""
    err = resp.get("error")
    if isinstance(err, dict):
        msg = err.get("message") or json.dumps(err)[:80]
    elif isinstance(err, str):
        msg = err
    if not msg:
        msg = resp.get("message") or "unknown"
    txt = f"{label}: {msg}"
    return f"{existing} | {txt}" if existing else txt


def kebab(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "applicant"


def synthetic_slug(name: str, email: str) -> str:
    h = hashlib.md5(email.lower().encode()).hexdigest()[:6]
    return f"https://www.linkedin.com/in/applicant-{kebab(name)}-{h}"


def normalize_url(u: str) -> str | None:
    """Return a usable URL, or None if it's junk."""
    u = (u or "").strip()
    if not u:
        return None
    if u.lower() in {"www.google.com", "localhost.com", "www.naukri.com", "n/a", "na", "none"}:
        return None
    if not u.startswith(("http://", "https://")):
        u = "https://" + u
    return u


def normalize_date(s: str) -> str | None:
    """Submission time is 'YYYY-MM-DD HH:MM:SS' → return 'YYYY-MM-DD'."""
    s = (s or "").strip()
    if not s:
        return None
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", s)
    return m.group(1) if m else None


def split_name(full: str) -> tuple[str, str]:
    full = (full or "").strip()
    if not full:
        return ("", "")
    parts = full.split()
    if len(parts) == 1:
        return (parts[0], "")
    return (parts[0], " ".join(parts[1:]))


# ---------- Per-row import ----------
def import_row(row: dict, dry_run: bool = False) -> dict:
    name = (row.get("Full Name") or "").strip()
    email = (row.get("Email") or "").strip()
    phone = (row.get("Phone number") or "").strip()
    country = (row.get("Which country are you in") or "").strip()
    linkedin = (row.get("linkedin_url") or "").strip()

    log = {
        "name": name,
        "email": email,
        "linkedin_provided": "yes" if linkedin else "no",
        "person_id": "",
        "candidate_id": "",
        "stage_status": "",
        "custom_status": "",
        "error": "",
    }

    if not name or not email:
        log["error"] = "missing name or email"
        return log

    # Generate synthetic slug + notes if no real LinkedIn
    if linkedin:
        linkedin_url = linkedin
        notes = ""
    else:
        linkedin_url = synthetic_slug(name, email)
        notes = "MISSING LINKEDIN URL — synthetic placeholder, please review and update."

    first, last = split_name(name)
    payload = {
        "name": name,
        "first_name": first,
        "last_name": last,
        "linkedin_url": linkedin_url,
        "emails": [email],
        "job_id": SENIOR_RECRUITER_JOB_ID,
    }
    if phone:
        payload["phone_numbers"] = [phone]
    if country:
        payload["linkedin_location"] = country
    if notes:
        payload["notes"] = notes

    if dry_run:
        log["error"] = f"DRY-RUN payload: {json.dumps(payload)[:200]}"
        return log

    # 1. Create person (auto-attaches as candidate at default stage)
    resp = _request("POST", "/persons", body=payload)
    if not resp.get("success"):
        log["error"] = _append_err("", "create", resp)
        return log

    data = resp["data"]
    log["person_id"] = data.get("id", "")
    log["candidate_id"] = data.get("candidate_id") or ""

    # 2. Move candidate to Applied stage
    if log["candidate_id"]:
        stage_resp = _request("POST", "/candidates/update-stage",
                              body={
                                  "job_id": SENIOR_RECRUITER_JOB_ID,
                                  "candidate_id": log["candidate_id"],
                                  "stage_id": APPLIED_STAGE_ID,
                              })
        if stage_resp.get("success") or stage_resp.get("new_stage_id"):
            log["stage_status"] = "Applied"
        else:
            log["stage_status"] = "failed"
            log["error"] = _append_err(log["error"], "stage", stage_resp)
    else:
        log["stage_status"] = "no-candidate-id"

    # 3. Update custom fields
    cf_payload = build_custom_fields(row)
    if cf_payload:
        cf_resp = _request("PATCH", f"/persons/{log['person_id']}",
                           body={"custom_fields": cf_payload})
        if cf_resp.get("success"):
            log["custom_status"] = f"{len(cf_payload)} fields"
        else:
            log["custom_status"] = "failed"
            log["error"] = _append_err(log["error"], "custom", cf_resp)
    else:
        log["custom_status"] = "no-fields"

    return log


def build_custom_fields(row: dict) -> list[dict]:
    out = []
    for csv_col, key in CSV_MAP.items():
        raw = (row.get(csv_col) or "").strip()
        if not raw:
            continue
        attr_id = CUSTOM_FIELDS[key]

        if key == "submitted_on":
            val = normalize_date(raw)
            if val:
                out.append({"attribute_id": attr_id, "value": val})
        elif key in URL_FIELDS:
            val = normalize_url(raw)
            if val:
                out.append({"attribute_id": attr_id, "value": val})
        elif key in SINGLE_SELECT_TRUE_FALSE:
            tag = "Yes" if raw.upper() == "TRUE" else "No"
            out.append({"attribute_id": attr_id, "value": tag})
        else:
            # plain string field
            out.append({"attribute_id": attr_id, "value": raw[:2000]})
    return out


# ---------- Main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--rate", type=float, default=0.4, help="sleep seconds between rows")
    args = ap.parse_args()

    with open(args.inp) as f:
        rows = list(csv.DictReader(f))

    log_fields = ["name", "email", "linkedin_provided", "person_id", "candidate_id",
                  "stage_status", "custom_status", "error"]

    counts = {"ok": 0, "partial": 0, "failed": 0, "skipped": 0}

    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=log_fields)
        w.writeheader()

        for i, row in enumerate(rows):
            if args.limit and i >= args.limit:
                break
            res = import_row(row, dry_run=args.dry_run)
            w.writerow(res)
            f.flush()

            if res["error"] and not res["person_id"]:
                counts["failed"] += 1
                status = "FAIL"
            elif res["error"]:
                counts["partial"] += 1
                status = "PARTIAL"
            elif not res["person_id"]:
                counts["skipped"] += 1
                status = "SKIP"
            else:
                counts["ok"] += 1
                status = "OK"

            print(f"  [{i+1:>3}] {status:<7} {res['name'][:28]:<30} "
                  f"li={res['linkedin_provided']:<3} "
                  f"person={res['person_id'][:8]:<8} "
                  f"stage={res['stage_status']:<10} "
                  f"cf={res['custom_status']:<10} "
                  f"{res['error'][:60]}")

            if not args.dry_run:
                time.sleep(args.rate)

    print("\nSummary:")
    for k, v in counts.items():
        print(f"  {k:<8} {v}")


if __name__ == "__main__":
    main()
