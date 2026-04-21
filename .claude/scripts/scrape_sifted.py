"""
Sifted Funding Scraper
Scrapes funding/deals articles from sifted.eu RSS feed + article pages
Outputs: sifted_funded.csv

Usage: python3 scrape_sifted.py
Options:
  --london-only  Filter to London/UK mentions only (default: False — tag all)

Note: Sifted's main site uses Cloudflare JS challenge — RSS feed is used instead,
which gives ~24 recent articles. Article pages are then scraped for content.
"""

import requests
import csv
import time
import re
import sys
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
RSS_URL = "https://sifted.eu/feed"
OUTPUT = "/tmp/sifted_funded.csv"

LONDON_ONLY = "--london-only" in sys.argv

# Keywords that indicate a funding article
FUNDING_KEYWORDS = [
    "raises", "raise", "raised", "funding", "investment", "invests",
    "series a", "series b", "series c", "seed", "pre-seed", "pre seed",
    "round", "backed", "secures", "closes", "million", "unicorn"
]


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


def is_funding_article(title, description=""):
    text = (title + " " + description).lower()
    return any(kw in text for kw in FUNDING_KEYWORDS)


def parse_title(title):
    """Extract company, amount, stage from title."""
    company = ""
    amount = ""
    stage = ""

    amount_match = re.search(
        r"[£$€]\s?[\d,]+(?:\.\d+)?(?:\s?(?:million|billion|M|B|K|k))?|"
        r"[\d,]+(?:\.\d+)?\s?(?:million|billion)\s?(?:pounds|dollars|euros)?",
        title, re.IGNORECASE
    )
    if amount_match:
        amount = amount_match.group(0).strip()

    stage_patterns = [
        r"\bpre[-\s]?seed\b", r"\bseed\b", r"\bseries\s[a-e]\b",
        r"\bgrowth\b", r"\bbridge\b", r"\bstrategic\b",
    ]
    for pat in stage_patterns:
        m = re.search(pat, title, re.IGNORECASE)
        if m:
            stage = m.group(0).strip().title()
            break

    action_verbs = r"\braises?\b|\bsecures?\b|\bcloses?\b|\blands?\b|\bwins?\b|\bhits?\b|\bscores?\b|\bbacked\b"
    verb_match = re.search(action_verbs, title, re.IGNORECASE)
    if verb_match:
        company = title[:verb_match.start()].strip().rstrip(",")
    else:
        company = " ".join(title.split()[:4])

    return company.strip(), amount.strip(), stage.strip()


def scrape_article(url):
    html = get(url)
    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    # Sifted article body
    # Try common content containers
    content = (
        soup.find("div", class_=re.compile(r"article|content|body|prose", re.I)) or
        soup.find("main") or
        soup.find("article")
    )

    paragraphs = content.find_all("p") if content else soup.find_all("p")
    description_parts = []
    for p in paragraphs:
        text = p.get_text(strip=True)
        if len(text) > 40:  # skip short/nav paragraphs
            description_parts.append(text)
        if len(description_parts) >= 3:
            break

    description = " ".join(description_parts)

    # Date — look for <time> tag or meta
    date = ""
    time_tag = soup.find("time")
    if time_tag:
        date = time_tag.get("datetime") or time_tag.get_text(strip=True)
    if not date:
        meta_date = soup.find("meta", property="article:published_time")
        if meta_date:
            date = meta_date.get("content", "")[:10]  # YYYY-MM-DD

    # Location
    location_text = description.lower()
    if "london" in location_text:
        location = "London"
    elif any(w in location_text for w in ["uk ", "u.k.", "united kingdom", "britain", "british"]):
        location = "UK"
    elif "europe" in location_text or "european" in location_text:
        location = "Europe"
    else:
        location = ""

    return description, date, location


def main():
    print(f"Scraping Sifted RSS{'  [London only]' if LONDON_ONLY else ''}")

    rss = get(RSS_URL)
    if not rss:
        print("Could not fetch RSS feed.")
        return

    soup = BeautifulSoup(rss, "xml")
    items = soup.find_all("item")
    print(f"  RSS items: {len(items)}")

    funding_items = []
    for item in items:
        title_tag = item.find("title")
        desc_tag = item.find("description")
        link_tag = item.find("link")
        pub_tag = item.find("pubDate")

        title = title_tag.get_text(strip=True) if title_tag else ""
        desc = desc_tag.get_text(strip=True) if desc_tag else ""
        link = link_tag.get_text(strip=True) if link_tag else ""
        pub_date = pub_tag.get_text(strip=True) if pub_tag else ""

        if is_funding_article(title, desc):
            funding_items.append((title, link, pub_date))

    print(f"  Funding articles found: {len(funding_items)}")

    rows = []
    for i, (title, url, pub_date) in enumerate(funding_items, 1):
        print(f"  [{i}/{len(funding_items)}] {title[:65]}")
        company, amount, stage = parse_title(title)

        description, date, location = scrape_article(url)
        if not date:
            date = pub_date[:16] if pub_date else ""

        if LONDON_ONLY and location not in ("London", "UK"):
            print(f"    → Skipped (location: {location or 'unknown'})")
            continue

        rows.append({
            "company_name": company,
            "funding_amount": amount,
            "funding_stage": stage,
            "location": location,
            "description": (description or "")[:500],
            "date": date,
            "source_url": url,
            "title": title,
        })
        time.sleep(0.5)

    if not rows:
        print("No results.")
        return

    fields = ["company_name", "funding_amount", "funding_stage", "location", "description", "date", "source_url", "title"]
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    london = sum(1 for r in rows if r["location"] in ("London", "UK"))
    print(f"\nDone. {len(rows)} articles saved → {OUTPUT}")
    print(f"London/UK mentions: {london} / {len(rows)}")


if __name__ == "__main__":
    main()
