"""
Canonical candidate-list HTML generator.

Per-client scripts in projects/ call render(CFG). Generator owns all HTML, CSS,
copy locks, and sanity checks. Per-client scripts only supply CFG.

Usage:
    import sys, os
    sys.path.insert(0, os.path.expanduser(
        "~/Library/CloudStorage/GoogleDrive-reyhan@recruitergtm.com/"
        "My Drive/EA Demo/.claude/skills/candidate-list"
    ))
    from generate import render
    render(CFG)

See SKILL.md (next to this file) for locked rules.
"""
import os
import re
import shutil

CAROLYN = os.path.expanduser("~/Desktop/proposals/carolyn-cope-proposal.html")

# ─── Locked copy (never edit per-client; raise to Reyhan if change needed) ──
# The sentence structure is locked. The talent descriptor is role-aware: it MUST
# match the job type / JD in Pulse (e.g. "recruitment talent" for recruiter
# placements, "GTM talent" for GTM Engineer / ops roles). Set via
# CFG["talent_descriptor"]; defaults to "GTM talent".
LOCKED_HERO_SUB_TEMPLATE = (
    "We are continuously engaging and pre-screening qualified {talent_descriptor} from our "
    "active Academy bench and extended network. Below is the latest batch we have lined up "
    "for your review. Watch each video and reply with the candidates you would like to "
    "interview &mdash; let us know if you would like to see additional profiles."
)


def _stash_base64(html):
    pattern = re.compile(r"data:image/[a-zA-Z+]+;base64,[A-Za-z0-9+/=\s]+")
    blobs = []

    def sub(m):
        blobs.append(m.group(0))
        return f"__B_{len(blobs)-1}__"

    return pattern.sub(sub, html), blobs


def _restore_base64(html, blobs):
    for i, blob in enumerate(blobs):
        html = html.replace(f"__B_{i}__", blob)
    return html


def _linkedin_btn(c):
    # Optional — omitted when a candidate doesn't have/use LinkedIn (rule D exception)
    if not c.get("linkedin"):
        return ""
    return (
        f'<a href="{c["linkedin"]}" target="_blank" '
        'style="display:flex;align-items:center;justify-content:center;gap:10px;'
        'background:#0A66C2;color:white;text-decoration:none;font-weight:700;font-size:14px;'
        'padding:14px 20px;border-radius:12px;letter-spacing:0.01em;'
        'box-shadow:0 4px 12px rgba(10,102,194,0.25);transition:transform 0.15s, box-shadow 0.15s;">'
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="white" style="flex-shrink:0;">'
        '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 '
        '2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 '
        '5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.063 2.063 0 112.063 2.065zm1.782 '
        '13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 '
        '24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'
        'View LinkedIn Profile &rarr;'
        '</a>'
    )


def _cv_btn(c):
    # Optional — rendered when a CV / resume link is provided
    if not c.get("cv"):
        return ""
    return (
        f'<a href="{c["cv"]}" target="_blank" '
        'style="display:flex;align-items:center;justify-content:center;gap:10px;'
        'background:rgba(255,255,255,0.06);color:var(--white);text-decoration:none;font-weight:700;font-size:14px;'
        'padding:14px 20px;border-radius:12px;letter-spacing:0.01em;border:1px solid var(--border);'
        'transition:transform 0.15s, background 0.15s;">'
        '&#128196; View CV &rarr;'
        '</a>'
    )


def _video_watch_url(video):
    # Convert an embeddable iframe URL into an open-in-browser watch/share URL.
    v = video
    if "/embed/" in v:                       # Loom
        return v.replace("/embed/", "/share/")
    if v.endswith("/embed"):                 # Tella
        return v[: -len("/embed")]
    if v.endswith("/preview"):               # Google Drive
        return v[: -len("/preview")] + "/view"
    return v


def _video_btn(c):
    # Backup "View Video" link — opens the recording in a new tab if the inline
    # embed is blocked (e.g. Loom embedding disabled). Video is a required field.
    url = _video_watch_url(c["video"])
    return (
        f'<a href="{url}" target="_blank" '
        'style="display:flex;align-items:center;justify-content:center;gap:10px;'
        'background:rgba(255,255,255,0.06);color:var(--white);text-decoration:none;font-weight:700;font-size:14px;'
        'padding:14px 20px;border-radius:12px;letter-spacing:0.01em;border:1px solid var(--border);'
        'transition:transform 0.15s, background 0.15s;">'
        '&#9654;&#65039; View Video &rarr;'
        '</a>'
    )


def _candidate_html(c):
    # Locked field checks (rule D) — linkedin is optional (see _linkedin_btn)
    for f in ("initial", "name", "rank", "headline", "summary", "fit", "video", "comp"):
        assert c.get(f), f"Candidate {c.get('name', '?')} is missing required field: {f}"
    # Locked video format (rule I) — Loom/Tella use /embed, Google Drive uses /preview
    assert ("/embed" in c["video"] or "/preview" in c["video"]), (
        f"Candidate {c['name']} video URL must be an embeddable iframe URL "
        f"(Loom/Tella /embed or Google Drive /preview). Got: {c['video']}"
    )

    meta_row = (
        '<div style="display:flex;flex-direction:column;gap:12px;margin-top:18px;">'
        # Expected comp stat card (locked design)
        '<div style="background:linear-gradient(135deg,rgba(138,0,255,0.18) 0%,rgba(138,0,255,0.04) 100%);'
        'border:1.5px solid rgba(138,0,255,0.45);border-radius:14px;padding:16px 20px;'
        'display:flex;align-items:center;justify-content:space-between;gap:12px;'
        'box-shadow:0 4px 12px rgba(138,0,255,0.08);">'
        '<div>'
        '<div style="font-size:10px;color:var(--ink-soft);text-transform:uppercase;'
        'letter-spacing:0.12em;font-weight:700;margin-bottom:4px;">Expected Monthly Comp</div>'
        f'<div style="font-size:24px;color:var(--white);font-weight:800;letter-spacing:-0.02em;'
        'line-height:1;">' + c["comp"] + '</div>'
        '</div>'
        '<div style="font-size:28px;line-height:1;">&#128176;</div>'
        '</div>'
        # CV button (optional) + View Video backup link + LinkedIn CTA button (locked design)
        + _cv_btn(c) + _video_btn(c) + _linkedin_btn(c) +
        '</div>'
    )

    return f"""
      <div class="candidate">
        <div class="candidate-info">
          <div class="candidate-head">
            <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,var(--violet) 0%,#6500BD 100%);display:flex;align-items:center;justify-content:center;font-weight:800;color:white;font-size:24px;flex-shrink:0;border:1.5px solid var(--border);">{c['initial']}</div>
            <div class="candidate-name-block">
              <span class="candidate-rank">{c['rank']}</span>
              <h3 class="candidate-name">{c['name']}</h3>
              <p class="candidate-headline">{c['headline']}</p>
            </div>
          </div>
          <p class="candidate-summary">{c['summary']}</p>
          <div class="candidate-fit">
            <strong>Best fit for</strong>
            {c['fit']}
          </div>
          {meta_row}
        </div>
        <div class="candidate-video">
          <iframe src="{c['video']}" allowfullscreen frameborder="0"></iframe>
        </div>
      </div>"""


def render(cfg):
    # Required CFG fields
    for f in ("client_name", "client_slug", "company", "role_title", "batch_num", "date_str", "candidates"):
        assert cfg.get(f) is not None, f"CFG missing required field: {f}"
    assert len(cfg["candidates"]) >= 1, "CFG['candidates'] must have at least 1 candidate"

    # Load Carolyn HEAD for CSS
    if not os.path.exists(CAROLYN):
        raise FileNotFoundError(
            f"candidate-list skill depends on {CAROLYN}. "
            "Restore the Carolyn proposal HTML or update CAROLYN path in generate.py."
        )
    with open(CAROLYN, "r") as f:
        carolyn = f.read()
    carolyn_stash, blobs = _stash_base64(carolyn)
    head_end = carolyn_stash.find("</head>") + len("</head>")
    HEAD = carolyn_stash[:head_end]

    candidates_html = "\n".join(_candidate_html(c) for c in cfg["candidates"])

    # Batch label is shown by default; set cfg["show_batch"] = False to omit it (e.g. replacement batches)
    show_batch = cfg.get("show_batch", True)
    hero_batch = f" &mdash; Batch {cfg['batch_num']}" if show_batch else ""
    hero_sub = LOCKED_HERO_SUB_TEMPLATE.format(
        talent_descriptor=cfg.get("talent_descriptor", "GTM talent")
    )
    meta_batch = f" &middot; Batch {cfg['batch_num']}" if show_batch else ""
    title_batch = f" (Batch {cfg['batch_num']})" if show_batch else ""

    body = f"""
<body>

<header class="site-header">
  <div class="header-inner">
    <div class="header-brand">
      <div class="r-badge">R</div>
      <span class="header-wordmark">RecruiterGTM</span>
      <span class="header-x">&times;</span>
      <span class="header-client">{cfg['company']}</span>
    </div>
    <span class="header-for">Prepared for {cfg['client_name']}</span>
  </div>
</header>

<div class="page">

  <!-- HERO -->
  <section class="hero">
    <p class="eyebrow"><span class="eyebrow-dot"></span> RecruiterGTM &times; {cfg['company']}</p>
    <h1 class="hero-title">{cfg['role_title']} Candidates for {cfg['company']}{hero_batch}</h1>
    <p class="hero-sub">{hero_sub}</p>
    <div class="hero-meta">
      <div class="meta-item">
        <span class="meta-label">Prepared for</span>
        <span class="meta-value">{cfg['client_name']}</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Company</span>
        <span class="meta-value">{cfg['company']}</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Role</span>
        <span class="meta-value">{cfg['role_title']}</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Date</span>
        <span class="meta-value">{cfg['date_str']}{meta_batch}</span>
      </div>
    </div>
  </section>

  <!-- CANDIDATES -->
  <section class="section">
    <div class="candidates">
{candidates_html}
    </div>
  </section>

</div>

<footer>
  <p>RecruiterGTM &middot; <span>Talent Academy</span></p>
</footer>
</body>
</html>
"""

    # Update head title
    TITLE_RE = re.compile(r"<title>[^<]*</title>")
    head_final = TITLE_RE.sub(
        f"<title>RecruiterGTM Talent Academy | {cfg['role_title']} Candidates for {cfg['company']}{title_batch}</title>",
        HEAD,
    )

    final_stashed = head_final + body
    final = _restore_base64(final_stashed, blobs)

    # Sanity checks
    opens = final.count("<div")
    closes = final.count("</div>")
    assert opens == closes, f"Div imbalance: opens={opens}, closes={closes}"
    assert "__B_" not in final, "Unrestored base64 placeholder"

    # Write to Desktop + projects mirror
    out_desk = os.path.expanduser(
        f"~/Desktop/proposals/{cfg['client_slug']}-candidates-batch{cfg['batch_num']}.html"
    )
    out_proj = os.path.expanduser(
        "~/Library/CloudStorage/GoogleDrive-reyhan@recruitergtm.com/My Drive/EA Demo/projects/"
        f"{cfg['client_slug']}-candidates-batch{cfg['batch_num']}.html"
    )
    os.makedirs(os.path.dirname(out_desk), exist_ok=True)
    with open(out_desk, "w") as f:
        f.write(final)
    shutil.copyfile(out_desk, out_proj)

    print(f"OK · {len(final):,} chars · {len(cfg['candidates'])} candidates · divs balanced ({opens}={closes})")
    print(f"Wrote {out_desk}")
    print(f"Wrote {out_proj}")
    return final
