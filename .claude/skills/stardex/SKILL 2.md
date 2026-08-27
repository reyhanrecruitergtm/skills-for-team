# Stardex Skill

Programmatic access to Stardex ATS. Use whenever a candidate, job, person, or pipeline action needs to be read from or written to Stardex.

## How to Invoke

```bash
python3 .claude/skills/stardex/stardex.py <command> <subcommand> [args]
```

Or import as a module from other skills:

```python
import sys; sys.path.insert(0, ".claude/skills/stardex")
import stardex
stardex.jobs_get("47281aab-7496-45af-9a3a-363804f341b8")
```

## Auth

Reads `STARDEX_API_KEY` from `.env` at project root (`ats-...`). Base URL `https://api.stardex.ai/v1`. Bearer token. Never paste the key into chat or commit it.

## Anchor IDs (current state, 2026-05-15)

| Thing | ID |
|---|---|
| Senior Recruiter job | `47281aab-7496-45af-9a3a-363804f341b8` |
| RecruiterGTM company | `0768dd25-c9f5-4ef7-91cb-cd711284b7d4` |
| Reyhan (team member) | `00d76c08-49b2-4a29-b889-07636066306d` |
| Team Lead role | `4b97e45e-50d9-4e2b-8f87-2cc2a9c584ed` |

### Senior Recruiter pipeline stage IDs

| Stage | ID |
|---|---|
| Sourced | `d95ee5e7-d11a-4501-a299-a2bfedf49041` |
| Applied | `396ade5a-2328-4d3a-941d-bcd909aeb181` |
| Contacted | `54b84a24-5fef-4a6e-8e29-60f45e836850` |
| Interested | `62a7c5fa-5cc6-4b6a-ad4f-9d891875ccfa` |
| Screen | `87bc6dbe-ecf1-41d0-a370-0dc29fc2721c` |
| Internal Interview | `52b0a331-2b35-436a-bf17-7f73fd71d94f` |
| Final Interview | `514a8dcb-b257-4154-90f6-764be90e4b30` |
| Offer | `bed1997c-2887-4058-9c07-8a33bc5bc946` |
| Placed | `8235e953-d31f-439f-ad7c-7148b82dd761` |
| Rejected | `4230cb8e-34fd-481b-85a6-51ff22f1a156` |

Refresh anchors by running `jobs get <job_id>` — IDs change per job.

## Commands

### Jobs
```bash
python3 stardex.py jobs get <job_id>
python3 stardex.py jobs search --keywords "senior recruiter" --limit 10
python3 stardex.py jobs candidates <job_id>
python3 stardex.py jobs create --title "..." --company_name "..." \
    --pipeline_template_name "Default Template" --location "Remote"
```

### Persons (candidates / contacts)
```bash
python3 stardex.py persons create --first_name Alex --last_name Doe \
    --email a@b.com --linkedin_url https://linkedin.com/in/alexdoe
python3 stardex.py persons get <person_id>
python3 stardex.py persons search --keywords "senior recruiter london"
python3 stardex.py persons update <person_id> --first_name Alex
```

### Candidates (a person attached to a job)
```bash
python3 stardex.py candidates stage <candidate_id> <stage_id> <job_id>
python3 stardex.py candidates get <candidate_id>
```
Stage update hits `POST /v1/candidates/update-stage` — all three IDs (`job_id`, `candidate_id`, `stage_id`) are required.

### Companies
```bash
python3 stardex.py companies upsert --name "Acme" --domain acme.com
python3 stardex.py companies search --keywords "acme"
```

### Team
```bash
python3 stardex.py team list
```

## Locked Rules

### A. Auth + safety
- A1. Never paste `STARDEX_API_KEY` into chat output, commits, or proposals. Read from `.env` only.
- A2. Never commit `.env` to git — already gitignored.
- A3. Use the Python CLI (not raw curl) inside skills — error envelope handling is baked in.

### B. Pipelines
- B1. Pipeline templates can ONLY be edited in the Stardex UI. The API has no create-pipeline endpoint. If a new pipeline is needed, ask Reyhan to set it up in Settings → Pipelines first.
- B2. A job snapshots stages from the template at creation time. Editing the template afterwards does NOT retroactively update stages on existing jobs. Edit stages per-job in the UI if changes are needed.
- B3. Always re-fetch stage IDs from the live job before moving candidates — don't trust cached IDs from this file blindly.

### C. CSV imports
- C1. Bulk-create candidates from CSV: loop `persons_create` first (gets a `person_id`), then attach to the job. Never run `persons_create` with `dry_run=False` on a CSV without first sampling 1–2 rows.
- C2. If a CSV is large (>200 rows), batch with rate limiting (10/sec max) and log every failure to `~/Desktop/stardex-import-failures.csv` for re-runs.

### D. Custom fields
- D1. Custom fields live per object type (job/person/company/deal). Pull definitions with `/v1/custom-fields/{type}` before writing — schema enforces type and option IDs.

## Reference

Full API docs: https://docs.stardex.com/api-reference/introduction
OpenAPI spec: https://docs.stardex.com/llms.txt
