"""
Per-client candidate list — Batch N

Copy this file to projects/generate_[client-slug]_candidates_batch[N].py and
fill in the CFG. The generator owns all HTML and copy locks.

See SKILL.md in the candidate-list skill folder for locked rules.
"""
import os
import sys

sys.path.insert(0, os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-reyhan@recruitergtm.com/My Drive/EA Demo/"
    ".claude/skills/candidate-list"
))
from generate import render  # noqa: E402

CFG = {
    "client_name": "First Last",                   # display name in "Prepared for"
    "client_slug": "first-last",                   # lowercase-hyphenated for filenames
    "company": "Company Inc.",                     # used in header co-branding + heading
    "role_title": "GTM Engineer",                  # appears in H1 + meta block
    "batch_num": 1,                                # 1, 2, 3...
    "date_str": "Month D, YYYY",                   # delivery date
    "candidates": [
        {
            "initial": "X",
            "name": "Candidate Full Name",
            "rank": "Option 01 · GTM Engineer",
            "headline": "One-line positioning, broad GTM/ops framing.",
            "summary": (
                "4-6 sentences with concrete numbers from CV. Lead with most "
                "transferable skill, not the recruitment niche of last employer. "
                "<strong>Bold the headline metric.</strong>"
            ),
            "fit": (
                "Best fit if [client] needs someone who can [specific capability]."
            ),
            # Loom: convert /share/ to /embed/   |   Tella: append /embed
            "video": "https://www.loom.com/embed/REPLACE",
            "linkedin": "https://www.linkedin.com/in/REPLACE/",
            "comp": "$X,XXX/mo",
        },
        # add 2-5 more candidates...
    ],
}

if __name__ == "__main__":
    render(CFG)
