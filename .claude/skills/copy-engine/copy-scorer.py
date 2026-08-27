#!/usr/bin/env python3
"""Deterministic copy linter — the MECHANICAL enforcement layer for copy-engine + content-os.
Catches the checkable rule violations that LLM self-audit keeps missing (desk, lane, front-tokens,
em dashes, banned words, telegram fragments). NOT a replacement for the copy-engine judge — it's
the hard gate that runs first. Mirrors content-os Section A–M; keep the lists in sync with that file.

Usage:
  echo "<copy>" | python3 copy-scorer.py --label "play1-A" --channel linkedin [--log scores.csv]
  python3 copy-scorer.py --file draft.txt --label "play1-A"
Score starts 100; hard flags -20 each (and fail), em dash -15 each, soft -8 each. PASS = no hard flags AND score >= 85.
"""
import sys, re, csv, argparse, os
from datetime import datetime, timezone

# --- HARD flags (fail the copy) — mirror content-os Section A + audience + banned copy phrases ---
HARD = {
    r"\bdesk\b": "‘desk’ — big-firm framing (audience is solo/boutique)",
    r"\blane\b": "‘lane’ metaphor (banned)",
    r"\bleverage\b": "‘leverage’ (AI/consultant word)",
    r"\bdelve\b": "‘delve’", r"\btransformative\b": "‘transformative’",
    r"\brobust\b": "‘robust’", r"\bseamless\b": "‘seamless’", r"\bsynergy\b": "‘synergy’",
    r"\bvalutainment\b": "‘valutainment’ (made-up word)",
    r"\bquick one\b": "‘quick one’ (banned CTA phrase)",
    r"no pressure either way": "‘no pressure either way’ (banned)",
    r"in your corner": "‘in your corner’ (banned)",
    r"that'?s the send": "‘that’s the send’ (banned)",
    r"\bseat\b": "‘seat’ for a role — use role/position/hire",
    r"—": "em dash (default zero in outbound copy)",
    r"#\w+": "hashtag (never in outbound copy)",
    r"(?im)^\s*for\s+[^,\n]{1,45},\s+(is|are|what|where|how|do|does|whats|what's)\b":
        "front-token opener ‘For {X}, <question>’ — dead mail-merge token",
    r"\bNot\s+(a\s+)?\w+\.\s+Not\s+(a\s+)?\w+": "parallel-negation ‘Not X. Not Y.’ (AI tell)",
    r"\bNot just\s+[^.]+\.\s": "‘Not just X. Y.’ pattern (AI tell)",
}
# --- SOFT flags (deduct, don't hard-fail) ---
SOFT = {
    r"what actually matters": "‘what actually matters’ (vague)",
    r"\bno fluff\b": "‘no fluff’", r"\bno hype\b": "‘no hype’", r"\bno bs\b": "‘no BS’",
    r"here'?s? the kicker": "‘here’s the kicker’ fragment",
    r"here'?s? the (part|thing) most people (miss|get wrong)": "‘the part most people miss’ (AI tell)",
    r"great question": "‘great question’ (corporate opener)",
    r"hope this helps": "‘hope this helps’", r"excited to share": "‘excited to share’",
    r"let me know what you think": "generic CTA",
    r"\bit'?s worth noting\b": "‘it’s worth noting’",
    r"in today'?s ": "‘in today’s …’ filler",
    r"\bsurfacing\b": "‘surfacing’ — jargon, prefer ‘finding’",
    r"getting (them|him|her|people) to\b": "causative/indirect ‘getting them to …’ — use a direct verb",
    r"\blanded\b": "‘landed’ as a win verb (AI tell)",
    r"\breal\s+(access|results|impact|value)\b": "‘real’ booster before a noun — cut it",
    r"\bHR teams\b": "‘HR teams’ — use ‘recruitment agencies’",
}

def analyse(text):
    flags = []
    for pat, msg in HARD.items():
        for m in re.finditer(pat, text):
            flags.append(("HARD", msg, m.group(0).strip()[:40]))
    for pat, msg in SOFT.items():
        for m in re.finditer(pat, text, re.I):
            flags.append(("SOFT", msg, m.group(0).strip()[:40]))
    # telegram fragments: a "sentence" of <=3 words that isn't a question/greeting
    for seg in re.split(r"(?<=[.!?])\s+|\n", text):
        s = seg.strip()
        if s and s.endswith(".") and 0 < len(s.split()) <= 3 and not s.lower().startswith(("hey", "hi", "best")):
            flags.append(("SOFT", f"telegram fragment ‘{s}’ — write a full sentence", s[:40]))
    score = 100
    hard = 0
    for lvl, msg, _ in flags:
        if "em dash" in msg: score -= 15
        elif lvl == "HARD": score -= 20; hard += 1
        else: score -= 8
    score = max(0, score)
    verdict = "PASS" if (hard == 0 and score >= 85) else "FAIL"
    return score, verdict, hard, flags

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file"); ap.add_argument("--text"); ap.add_argument("--label", default="")
    ap.add_argument("--channel", default=""); ap.add_argument("--log")
    a = ap.parse_args()
    text = a.text or (open(a.file).read() if a.file else sys.stdin.read())
    score, verdict, hard, flags = analyse(text)
    mark = "✅" if verdict == "PASS" else "❌"
    print(f"{mark} {a.label or 'copy'} [{a.channel}] — score {score}/100 — {verdict} ({hard} hard, {len(flags)} flags)")
    for lvl, msg, hit in flags:
        print(f"   {'🔴' if lvl=='HARD' else '🟡'} {msg}" + (f"  →  “{hit}”" if hit and hit not in msg else ""))
    if a.log:
        new = not os.path.exists(a.log)
        with open(a.log, "a", newline="") as f:
            w = csv.writer(f)
            if new: w.writerow(["timestamp", "label", "channel", "score", "verdict", "hard", "flags"])
            w.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"), a.label, a.channel,
                        score, verdict, hard, " | ".join(m for _, m, _ in flags)])
    sys.exit(0 if verdict == "PASS" else 1)

if __name__ == "__main__":
    main()
