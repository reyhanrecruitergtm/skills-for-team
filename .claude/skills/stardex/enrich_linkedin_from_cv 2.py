#!/usr/bin/env python3
"""
Extract LinkedIn URL from each applicant's CV/resume link.

Strategy per row:
  1. Skip junk (www.google.com, localhost, video-only platforms with no resume).
  2. If resume_url is already a linkedin.com/in/ URL → use directly.
  3. Google Drive folder → list contents, find first PDF/DOC, download.
  4. Google Drive file → convert to uc?export=download.
  5. Google Docs → convert to /export?format=pdf.
  6. Otherwise → fetch URL directly (HTML/PDF/DOCX).
  7. Parse text from response (pdftotext / python-docx / raw HTML), regex for LinkedIn URL.

Usage:
  python3 enrich_linkedin_from_cv.py <input.csv> <output.csv> [--limit N] [--dry-run]
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import tempfile
import time
import urllib.parse
from pathlib import Path

import urllib.request
import urllib.error

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

LINKEDIN_RE = re.compile(
    r"https?://(?:[\w-]+\.)*linkedin\.com/in/[A-Za-z0-9_\-%.]+",
    re.IGNORECASE,
)
# Bare "linkedin.com/in/foo" (no protocol)
LINKEDIN_BARE_RE = re.compile(
    r"(?:^|[\s\(/>])((?:[\w-]+\.)*linkedin\.com/in/[A-Za-z0-9_\-%.]+)",
    re.IGNORECASE,
)

JUNK_HOSTS = {
    "google.com",      # www.google.com placeholder
    "localhost.com",
    "naukri.com",      # just root, not a CV
    "loom.com",        # video, not CV
    "whatsapp.com",
    "link.camscanner.com",
}

JUNK_URLS = {"www.google.com", "localhost.com", "www.naukri.com"}


def _fetch(url: str, timeout: int = 25) -> tuple[bytes, str]:
    """Fetch URL, return (body, content_type). Raises on error."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
        ct = r.headers.get("Content-Type", "").lower()
        return body, ct


def _drive_to_download(url: str) -> str | None:
    """Convert various Google Drive URL forms to direct download."""
    m = re.search(r"/file/d/([A-Za-z0-9_\-]+)", url)
    if m:
        return f"https://drive.google.com/uc?export=download&id={m.group(1)}"
    m = re.search(r"[?&]id=([A-Za-z0-9_\-]+)", url)
    if m and "drive.google.com" in url:
        return f"https://drive.google.com/uc?export=download&id={m.group(1)}"
    return None


def _docs_to_pdf(url: str) -> str | None:
    """Convert Google Docs editor URL to direct PDF export."""
    m = re.search(r"/document/d/([A-Za-z0-9_\-]+)", url)
    if m:
        return f"https://docs.google.com/document/d/{m.group(1)}/export?format=pdf"
    return None


def _pdf_to_text(body: bytes) -> str:
    """Extract text + embedded URI annotations from a PDF.

    pdftotext only returns visible text. PDF hyperlinks live as `/URI (...)` annotations
    that aren't surfaced. So we also scan the raw bytes for those — most candidates who
    add a clickable LinkedIn link in a CV won't have the URL as visible text.
    """
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(body)
        pdf_path = f.name
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", pdf_path, "-"],
            capture_output=True, timeout=30,
        )
        visible = result.stdout.decode("utf-8", "replace")
    except Exception:
        visible = ""
    finally:
        Path(pdf_path).unlink(missing_ok=True)

    # Also extract any embedded /URI (...) annotations from raw bytes
    uri_blob = ""
    try:
        raw = body.decode("latin-1", "replace")
        uris = re.findall(r"/URI\s*\(([^)]+)\)", raw)
        uri_blob = "\n".join(uris)
    except Exception:
        pass
    return visible + "\n" + uri_blob


def _docx_to_text(body: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as f:
        f.write(body)
        path = f.name
    try:
        import docx
        d = docx.Document(path)
        parts = [p.text for p in d.paragraphs]
        # Hyperlinks live in r:hyperlink elements — XML scan as fallback
        xml = ""
        try:
            xml = d.part.element.xml
        except Exception:
            pass
        return "\n".join(parts) + "\n" + xml
    except Exception:
        return ""
    finally:
        Path(path).unlink(missing_ok=True)


def _extract_linkedin(text: str) -> str | None:
    m = LINKEDIN_RE.search(text)
    if m:
        return _clean_url(m.group(0))
    m = LINKEDIN_BARE_RE.search(text)
    if m:
        return _clean_url("https://" + m.group(1))
    return None


def _clean_url(url: str) -> str:
    # Strip trailing punctuation & utm/share params
    url = url.rstrip(").,;:'\"")
    # Normalise country subdomain (uk.linkedin.com → linkedin.com is risky; leave as-is)
    # Strip query string except keep the in/* slug
    if "?" in url:
        url = url.split("?")[0]
    return url


def enrich_one(resume_url: str) -> dict:
    """Return {linkedin_url, method, status, error}."""
    out = {"linkedin_url": None, "method": "", "status": "", "error": ""}
    if not resume_url:
        out["status"] = "skipped-empty"
        return out

    raw = resume_url.strip()
    if not raw.startswith(("http://", "https://")):
        raw = "https://" + raw

    # Junk check
    host = urllib.parse.urlparse(raw).hostname or ""
    host = host.lower().replace("www.", "")
    if host in JUNK_HOSTS or raw.lower().rstrip("/") in JUNK_URLS:
        out["status"] = "skipped-junk"
        return out

    # Already a LinkedIn URL — done
    if re.search(r"linkedin\.com/in/", raw, re.IGNORECASE):
        out["linkedin_url"] = _clean_url(raw)
        out["method"] = "direct"
        out["status"] = "ok"
        return out

    # Google Drive folder (any variant including /drive/u/N/folders/)
    if re.search(r"drive\.google\.com/drive/(?:u/\d+/)?folders/", raw):
        out["status"] = "skipped-drive-folder"
        out["error"] = "Drive folder, cannot auto-pick file"
        return out

    # linkyhost.com serves PDF at ?raw=true
    if "linkyhost.com" in raw:
        raw = re.sub(r"\?.*$", "", raw).rstrip("/") + "/?raw=true"

    # Google Drive file → direct download
    download_url = _drive_to_download(raw)
    if download_url:
        raw = download_url
    elif "docs.google.com/document" in raw:
        pdf = _docs_to_pdf(raw)
        if pdf:
            raw = pdf

    try:
        body, ct = _fetch(raw)
    except urllib.error.HTTPError as e:
        out["status"] = "fetch-failed"
        out["error"] = f"HTTP {e.code}"
        return out
    except Exception as e:
        out["status"] = "fetch-failed"
        out["error"] = str(e)[:120]
        return out

    text, method = _parse_body(body, ct, raw)
    out["method"] = method

    found = _extract_linkedin(text)

    # HTML fallback: if no match, look for an embedded PDF iframe/object/embed and fetch it
    if not found and method == "html":
        pdf_url = _find_embedded_pdf(text, raw)
        if pdf_url:
            try:
                body2, ct2 = _fetch(pdf_url)
                text2, method2 = _parse_body(body2, ct2, pdf_url)
                out["method"] = f"html→{method2}"
                found = _extract_linkedin(text2)
            except Exception:
                pass

    if found:
        out["linkedin_url"] = found
        out["status"] = "ok"
    else:
        out["status"] = "no-match"
    return out


def _parse_body(body: bytes, ct: str, source_url: str) -> tuple[str, str]:
    """Parse PDF / DOCX / HTML body to text. Returns (text, method)."""
    # Drive sometimes returns an HTML virus-scan confirmation for large files
    looks_like_pdf = body[:4] == b"%PDF" or "pdf" in ct
    looks_like_zip_office = body[:2] == b"PK" and ("wordprocessingml" in ct or source_url.endswith(".docx"))

    if looks_like_pdf:
        return _pdf_to_text(body), "pdf"
    if looks_like_zip_office:
        return _docx_to_text(body), "docx"
    try:
        return body.decode("utf-8", "replace"), "html"
    except Exception:
        return "", "html"


def _find_embedded_pdf(html: str, base_url: str) -> str | None:
    """Look for iframe/embed/object src or anchor href that points to a PDF."""
    for pat in (
        r'<iframe[^>]+src="([^"]+)"',
        r'<embed[^>]+src="([^"]+)"',
        r'<object[^>]+data="([^"]+)"',
        r'<a[^>]+href="([^"]+\.pdf[^"]*)"',
    ):
        for m in re.finditer(pat, html, re.IGNORECASE):
            url = m.group(1)
            if url.startswith("/"):
                base = re.match(r"(https?://[^/]+)", base_url)
                if base:
                    url = base.group(1) + url
            if url.startswith(("http://", "https://")):
                return url
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--name-col", default="Full Name")
    ap.add_argument("--email-col", default="Email")
    ap.add_argument("--resume-col", default="Resume Link (Make sure it's a public link)")
    args = ap.parse_args()

    with open(args.inp) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fields = reader.fieldnames or []

    out_fields = fields + ["linkedin_url", "enrichment_method", "enrichment_status", "enrichment_error"]

    stats = {"ok": 0, "no-match": 0, "fetch-failed": 0, "skipped-junk": 0,
             "skipped-empty": 0, "skipped-drive-folder": 0}

    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()

        for i, row in enumerate(rows):
            if args.limit and i >= args.limit:
                break
            name = row.get(args.name_col, "")
            resume = row.get(args.resume_col, "")
            res = enrich_one(resume)
            row.update({
                "linkedin_url": res["linkedin_url"] or "",
                "enrichment_method": res["method"],
                "enrichment_status": res["status"],
                "enrichment_error": res["error"],
            })
            w.writerow(row)
            stats[res["status"]] = stats.get(res["status"], 0) + 1
            print(f"  [{i+1:>3}] {name[:30]:<32} {res['status']:<22} {res['linkedin_url'] or ''}")
            time.sleep(0.3)  # gentle rate limit on Drive

    print("\nSummary:")
    for k, v in sorted(stats.items(), key=lambda kv: -kv[1]):
        print(f"  {k:<22} {v}")


if __name__ == "__main__":
    main()
