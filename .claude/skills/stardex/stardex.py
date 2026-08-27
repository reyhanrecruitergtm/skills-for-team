#!/usr/bin/env python3
"""
Stardex ATS CLI wrapper.

Reads STARDEX_API_KEY from .env (project root). Supports the endpoints we use
day-to-day: jobs, persons, candidates, companies, deals, tasks, custom fields,
team members, webhooks.

Usage examples:
  python3 stardex.py jobs search --title "Senior Recruiter"
  python3 stardex.py jobs get 47281aab-7496-45af-9a3a-363804f341b8
  python3 stardex.py jobs candidates 47281aab-7496-45af-9a3a-363804f341b8
  python3 stardex.py persons create --first Alex --last Doe --email a@b.com
  python3 stardex.py persons search --keywords "senior recruiter london"
  python3 stardex.py candidates stage <candidate_id> <stage_id>
  python3 stardex.py team list

Or import as a module:
  from stardex import client
  client.jobs_get("47281aab-...")
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import urllib.request
import urllib.parse
import urllib.error

BASE = "https://api.stardex.ai/v1"


def _load_env_key() -> str:
    key = os.environ.get("STARDEX_API_KEY")
    if key:
        return key
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        env = parent / ".env"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("STARDEX_API_KEY="):
                    return line.split("=", 1)[1].strip()
    raise SystemExit("STARDEX_API_KEY not set in env or .env")


API_KEY = _load_env_key()


def _request(method: str, path: str, body: dict | None = None, query: dict | None = None) -> dict:
    url = f"{BASE}{path}"
    if query:
        url += "?" + urllib.parse.urlencode({k: v for k, v in query.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {API_KEY}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body_txt = e.read().decode("utf-8", "replace")
        try:
            return json.loads(body_txt)
        except Exception:
            return {"success": False, "error": {"status": e.code, "raw": body_txt}}


# ---------- Jobs ----------
def jobs_create(**kwargs) -> dict:
    return _request("POST", "/jobs", body=kwargs)


def jobs_get(job_id: str) -> dict:
    return _request("GET", f"/jobs/{job_id}")


def jobs_search(**body) -> dict:
    body.setdefault("limit", 25)
    return _request("POST", "/jobs/search", body=body)


def jobs_candidates(job_id: str, limit: int = 100, offset: int = 0) -> dict:
    return _request("GET", f"/jobs/{job_id}/candidates", query={"limit": limit, "offset": offset})


# ---------- Persons ----------
def persons_create(**kwargs) -> dict:
    return _request("POST", "/persons", body=kwargs)


def persons_get(person_id: str) -> dict:
    return _request("GET", f"/persons/{person_id}")


def persons_update(person_id: str, **kwargs) -> dict:
    return _request("PATCH", f"/persons/{person_id}", body=kwargs)


def persons_search(**body) -> dict:
    body.setdefault("limit", 25)
    return _request("POST", "/persons/search", body=body)


# ---------- Candidates ----------
def candidate_stage(candidate_id: str, stage_id: str, job_id: str) -> dict:
    """Move a candidate to a different pipeline stage. All three IDs required."""
    return _request("POST", "/candidates/update-stage",
                    body={"job_id": job_id, "candidate_id": candidate_id, "stage_id": stage_id})


def candidate_get(candidate_id: str) -> dict:
    return _request("GET", f"/candidates/{candidate_id}")


# ---------- Companies ----------
def companies_upsert(**kwargs) -> dict:
    return _request("POST", "/companies", body=kwargs)


def companies_search(**body) -> dict:
    body.setdefault("limit", 25)
    return _request("POST", "/companies/search", body=body)


# ---------- Team ----------
def team_list() -> dict:
    return _request("GET", "/team-members")


# ---------- CLI ----------
def _pp(obj):
    print(json.dumps(obj, indent=2, default=str))


def _cli(argv: list[str]) -> None:
    if not argv:
        print(__doc__)
        return
    cmd = argv[0]
    if cmd == "jobs":
        sub = argv[1]
        if sub == "get":
            _pp(jobs_get(argv[2]))
        elif sub == "search":
            args = _parse_kv(argv[2:])
            _pp(jobs_search(**args))
        elif sub == "candidates":
            _pp(jobs_candidates(argv[2]))
        elif sub == "create":
            _pp(jobs_create(**_parse_kv(argv[2:])))
        else:
            sys.exit(f"unknown jobs subcommand: {sub}")
    elif cmd == "persons":
        sub = argv[1]
        if sub == "get":
            _pp(persons_get(argv[2]))
        elif sub == "create":
            _pp(persons_create(**_parse_kv(argv[2:])))
        elif sub == "update":
            _pp(persons_update(argv[2], **_parse_kv(argv[3:])))
        elif sub == "search":
            _pp(persons_search(**_parse_kv(argv[2:])))
        else:
            sys.exit(f"unknown persons subcommand: {sub}")
    elif cmd == "candidates":
        sub = argv[1]
        if sub == "stage":
            _pp(candidate_stage(argv[2], argv[3], argv[4]))
        elif sub == "get":
            _pp(candidate_get(argv[2]))
        else:
            sys.exit(f"unknown candidates subcommand: {sub}")
    elif cmd == "companies":
        sub = argv[1]
        if sub == "upsert":
            _pp(companies_upsert(**_parse_kv(argv[2:])))
        elif sub == "search":
            _pp(companies_search(**_parse_kv(argv[2:])))
    elif cmd == "team":
        if argv[1] == "list":
            _pp(team_list())
    else:
        sys.exit(f"unknown command: {cmd}")


def _parse_kv(argv: list[str]) -> dict:
    out = {}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--"):
            key = a[2:].replace("-", "_")
            val = argv[i + 1] if i + 1 < len(argv) else ""
            if val.lower() in {"true", "false"}:
                val = val.lower() == "true"
            elif val.isdigit():
                val = int(val)
            out[key] = val
            i += 2
        else:
            i += 1
    return out


if __name__ == "__main__":
    _cli(sys.argv[1:])
