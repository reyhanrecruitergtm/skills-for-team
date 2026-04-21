"""
TechRound Funding Scraper
Scrapes recently funded startups from techround.co.uk/category/funding/
Outputs: techround_funded.csv

Usage: python3 scrape_techround.py
Options:
  --pages N     Number of listing pages to scrape (default: 5, ~50 articles)
  --london-only Filter to London mentions only (default: False — keep all, tag location)
"""

import requests
import csv
import time
import re
import sys
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
BASE = "https://techround.co.uk"
OUTPUT = "/tmp/techround_funded.csv"
PAGES = 5  # ~10 articles per page = 50 articles

# Override with --pages N
for i, arg in enumerate(sys.argv):
    if arg == "--pages" and i + 1 < len(sys.argv):
        PAGES = int(sys.argv[i + 1])

LONDON_ONLY = "--london-only" in sys.argv


def get(url, retries=3):
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            r.raise_for_status()
            return r.text
        except Exception as e:
            if attempt == retries - 1:
                print(f"  FAILED: {url} — {e}")
                return None
            time.sleep(2)


def get_article_urls(page_num):
    url = f"{BASE}/category/funding/" if page_num == 1 else f"{BASE}/category/funding/page/{page_num}/"
    html = get(url)
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for a in soup.find_all("a"):
        h2 = a.find("h2")
        if h2:
            href = a.get("href", "")
            if href and "/funding/" in href and href not in urls:
                urls.append(href)
    return urls


def parse_title(title):
    """Extract company name, amount, and stage from article title."""
    company = ""
    amount = ""
    stage = ""

    # Amount: match £/$€ + number + M/K/m/k/million/thousand
    amount_match = re.search(
        r"[£$€]\s?[\d,]+(?:\.\d+)?(?:\s?(?:million|billion|M|B|K|k))?|"
        r"[\d,]+(?:\.\d+)?\s?(?:million|billion)\s?(?:pounds|dollars|euros)?",
        title, re.IGNORECASE
    )
    if amount_match:
        amount = amount_match.group(0).strip()

    # Stage: look for known keywords
    stage_patterns = [
        r"\bpre[-\s]?seed\b", r"\bseed\b", r"\bseries\s[a-e]\b",
        r"\bgrowth\b", r"\bbridge\b", r"\bstrategic\b", r"\bventure\b",
        r"\bfriend[s]?\s(?:and|&)\s(?:family|families)\b"
    ]
    for pat in stage_patterns:
        m = re.search(pat, title, re.IGNORECASE)
        if m:
            stage = m.group(0).strip().title()
            break

    # Company name: everything before the first action verb
    action_verbs = r"\braises?\b|\bsecures?\b|\bcloses?\b|\blands?\b|\bwins?\b|\bgets?\b|\bscores?\b|\bannounces?\b"
    verb_match = re.search(action_verbs, title, re.IGNORECASE)
    if verb_match:
        company = title[:verb_match.start()].strip().rstrip(",")
    else:
        # Fallback: first 4 words
        company = " ".join(title.split()[:4])

    return company.strip(), amount.strip(), stage.strip()


def scrape_article(url):
    html = get(url)
    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    # Title
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else ""

    # Article body
    art = soup.find("article")
    paragraphs = art.find_all("p") if art else soup.find_all("p")

    # Date — TechRound first paragraph is "AuthorNameMonthDay, Year" (no space between author and month)
    # e.g. "Gina MarrsMarch 17, 2026" — use a loose date search across all text
    date = ""
    all_text = " ".join(p.get_text(strip=True) for p in paragraphs[:3])
    date_match = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}",
        all_text
    )
    if date_match:
        date = date_match.group(0)

    # Description — skip first paragraph (author/date line), take next 3 substantive paragraphs
    description_parts = []
    for i, p in enumerate(paragraphs):
        if i == 0:
            continue  # always skip author/date paragraph
        text = p.get_text(strip=True)
        if len(text) < 40:
            continue  # skip short/empty paragraphs
        description_parts.append(text)
        if len(description_parts) >= 3:
            break

    description = " ".join(description_parts)

    # Location — search title + all paragraphs (not just description)
    full_text = (title + " " + " ".join(p.get_text(strip=True) for p in paragraphs)).lower()
    if "london" in full_text:
        location = "London"
    elif "united kingdom" in full_text or "britain" in full_text or re.search(r"\buk\b|\bu\.k\.", full_text):
        location = "UK"
    else:
        location = ""

    company, amount, stage = parse_title(title)

    return {
        "company_name": company,
        "funding_amount": amount,
        "funding_stage": stage,
        "location": location,
        "description": description[:500],
        "date": date,
        "source_url": url,
        "title": title,
    }


def main():
    print(f"Scraping TechRound — {PAGES} pages{'  [London only]' if LONDON_ONLY else ''}")
    all_urls = []

    for page in range(1, PAGES + 1):
        urls = get_article_urls(page)
        print(f"  Page {page}: {len(urls)} articles")
        all_urls.extend(urls)
        time.sleep(0.5)

    print(f"\nTotal articles to scrape: {len(all_urls)}")

    rows = []
    for i, url in enumerate(all_urls, 1):
        print(f"  [{i}/{len(all_urls)}] {url.split('/')[-2][:60]}")
        data = scrape_article(url)
        if data:
            if LONDON_ONLY and data["location"] != "London":
                continue
            rows.append(data)
        time.sleep(0.4)

    if not rows:
        print("No results.")
        return

    fields = ["company_name", "funding_amount", "funding_stage", "location", "description", "date", "source_url", "title"]
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    london = sum(1 for r in rows if r["location"] == "London")
    print(f"\nDone. {len(rows)} articles saved → {OUTPUT}")
    print(f"London mentions: {london} / {len(rows)}")


if __name__ == "__main__":
    main()
