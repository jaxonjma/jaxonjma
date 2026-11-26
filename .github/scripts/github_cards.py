#!/usr/bin/env python3
"""Generate profile cards (languages + GitHub stats) as themed SVGs.

Runs in GitHub Actions with GITHUB_TOKEN. Stdlib only.
Usage: python github_cards.py <username> <outdir> [--mock data.json]
"""
import datetime as dt
import json
import os
import sys
import urllib.request
from xml.sax.saxutils import escape as esc

API = "https://api.github.com"

THEMES = {
    "dark": dict(bg1="#15171b", bg2="#0f1013", card="#1b1e23", line="#2a2e35", hi="#f3f4f6", txt="#d1d5db",
                 dim="#8b93a0", faint="#5b6370", cyan="#7fd6ff", blue="#2f6bff", track="#262a31"),
    "light": dict(bg1="#fbfbfc", bg2="#f1f3f6", card="#ffffff", line="#e2e5ea", hi="#111418", txt="#2b3038",
                  dim="#5f6774", faint="#9aa2ad", cyan="#0b8fd6", blue="#2459e0", track="#eef1f5"),
}
# Brand-leaning palette for language segments (ordered by rank, not by language)
SEG = ["#2f6bff", "#7fd6ff", "#94a3b8", "#1e40af", "#5eead4", "#cbd5e1", "#60a5fa", "#64748b"]
FONTS = (".sans{font-family:'Inter','Segoe UI',-apple-system,Helvetica,Arial,sans-serif}"
         ".mono{font-family:'JetBrains Mono','SFMono-Regular',Menlo,Consolas,monospace}")


# ---------------------------------------------------------------- data
def _req(url, token, body=None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-cards"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def fetch(user, token):
    repos, page = [], 1
    while True:
        batch = _req(f"{API}/users/{user}/repos?per_page=100&type=owner&page={page}", token)
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    own = [r for r in repos if not r.get("fork") and r["name"].lower() != user.lower()]
    langs = {}
    for r in own:
        for k, v in _req(r["languages_url"], token).items():
            langs[k] = langs.get(k, 0) + v
    stars = sum(r.get("stargazers_count", 0) for r in own)
    q = """query($login:String!){user(login:$login){
      contributionsCollection{totalCommitContributions totalPullRequestContributions totalIssueContributions
        totalRepositoryContributions contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}
      followers{totalCount}}}"""
    g = _req(f"{API}/graphql", token, {"query": q, "variables": {"login": user}})["data"]["user"]
    cc = g["contributionsCollection"]
    days = [d for w in cc["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
    return dict(languages=langs, repos=len(own), stars=stars, followers=g["followers"]["totalCount"],
                commits=cc["totalCommitContributions"], prs=cc["totalPullRequestContributions"],
                issues=cc["totalIssueContributions"], total=cc["contributionCalendar"]["totalContributions"],
                days=[(d["date"], d["contributionCount"]) for d in days])


def streaks(days):
    today = dt.date.today().isoformat()
    longest = cur = run = 0
    for date, c in days:
        run = run + 1 if c > 0 else 0
        longest = max(longest, run)
    for date, c in reversed(days):
        if date == today and c == 0:
            continue  # today not over yet
        if c > 0:
            cur += 1
        else:
            break
    return cur, longest


# ---------------------------------------------------------------- render
def head(w, h, t, label, css=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">'
            f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg1"]}"/><stop offset="1" stop-color="{t["bg2"]}"/></linearGradient>'
            f'<linearGradient id="rb" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2f6bff"/><stop offset="1" stop-color="{t["cyan"]}"/></linearGradient>'
            f'<style>{FONTS}{css}</style></defs><rect width="{w}" height="{h}" rx="18" fill="url(#bg)"/>'
            f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="18" fill="none" stroke="{t["line"]}"/>')


def languages_svg(t, langs):
    W, H = 590, 300
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:8]
    css = (".seg{animation:grow 1.1s cubic-bezier(.2,.7,.2,1) backwards;transform-origin:left;transform-box:fill-box}"
           "@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}"
           ".lg{animation:in .6s ease-out backwards}@keyframes in{from{opacity:0}to{opacity:1}}")
    o = [head(W, H, t, "Most used languages across public repositories", css)]
    o.append(f'<text class="mono" x="28" y="40" font-size="11.5" fill="{t["cyan"]}" letter-spacing=".2em">LANGUAGES</text>')
    o.append(f'<text class="sans" x="28" y="68" font-size="20" font-weight="800" fill="{t["hi"]}">Across my public repositories</text>')
    x, bw, by = 28, W - 56, 92
    o.append(f'<rect x="{x}" y="{by}" width="{bw}" height="12" rx="6" fill="{t["track"]}"/>')
    o.append(f'<clipPath id="bar"><rect x="{x}" y="{by}" width="{bw}" height="12" rx="6"/></clipPath><g clip-path="url(#bar)">')
    cx = x
    for i, (name, v) in enumerate(top):
        w = bw * v / total
        o.append(f'<rect class="seg" style="animation-delay:{i*0.08:.2f}s" x="{cx:.2f}" y="{by}" width="{w:.2f}" height="12" fill="{SEG[i % len(SEG)]}"/>')
        cx += w
    o.append("</g>")
    col_w = (W - 56) / 2
    for i, (name, v) in enumerate(top):
        r, c = divmod(i, 2)
        lx, ly = 28 + c * col_w, 140 + r * 38
        pct = 100 * v / total
        o.append(f'<g class="lg" style="animation-delay:{0.4+i*0.06:.2f}s">'
                 f'<circle cx="{lx+6}" cy="{ly-5}" r="6" fill="{SEG[i % len(SEG)]}"/>'
                 f'<text class="sans" x="{lx+20}" y="{ly}" font-size="14.5" font-weight="600" fill="{t["hi"]}">{esc(name)}</text>'
                 f'<text class="mono" x="{lx+col_w-24}" y="{ly}" text-anchor="end" font-size="13" fill="{t["dim"]}">{pct:.1f}%</text></g>')
    if not top:
        o.append(f'<text class="sans" x="28" y="150" font-size="14" fill="{t["dim"]}">No public code yet.</text>')
    o.append("</svg>")
    return "".join(o)


def stats_svg(t, d):
    W, H = 590, 300
    cur, longest = streaks(d["days"])
    active = sum(1 for _, c in d["days"] if c > 0)
    busiest = max((c for _, c in d["days"]), default=0)
    items = [("Contributions", d["total"], "1y"), ("Active days", active, "1y"),
             ("Busiest day", busiest, "contribs"), ("Current streak", cur, "days"),
             ("Longest streak", longest, "days"), ("Public repos", d["repos"], "")]
    css = ".st{animation:up .7s cubic-bezier(.2,.7,.2,1) backwards}@keyframes up{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}"
    o = [head(W, H, t, "GitHub activity statistics", css)]
    o.append(f'<text class="mono" x="28" y="40" font-size="11.5" fill="{t["cyan"]}" letter-spacing=".2em">GITHUB ACTIVITY</text>')
    o.append(f'<text class="sans" x="28" y="68" font-size="20" font-weight="800" fill="{t["hi"]}">Updated daily by a workflow</text>')
    cw, ch, gx, gy = (W - 56 - 24) / 3, 88, 12, 14
    for i, (label, val, sub) in enumerate(items):
        r, c = divmod(i, 3)
        x, y = 28 + c * (cw + gx), 90 + r * (ch + gy)
        o.append(f'<g class="st" style="animation-delay:{i*0.07:.2f}s">'
                 f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="{ch}" rx="12" fill="{t["card"]}" stroke="{t["line"]}"/>'
                 f'<text class="sans" x="{x+16:.1f}" y="{y+40}" font-size="28" font-weight="800" fill="{t["hi"]}">{val:,}</text>'
                 f'<rect x="{x+16:.1f}" y="{y+50}" width="26" height="3" rx="1.5" fill="url(#rb)"/>'
                 f'<text class="sans" x="{x+16:.1f}" y="{y+70}" font-size="12.5" fill="{t["txt"]}">{esc(label)}{f' <tspan fill="{t["faint"]}">· {esc(sub)}</tspan>' if sub else ""}</text></g>')
    o.append("</svg>")
    return "".join(o)


def main():
    user, out = sys.argv[1], sys.argv[2]
    if "--mock" in sys.argv:
        data = json.load(open(sys.argv[sys.argv.index("--mock") + 1]))
    else:
        data = fetch(user, os.environ.get("GITHUB_TOKEN", ""))
    os.makedirs(out, exist_ok=True)
    for name, t in THEMES.items():
        open(f"{out}/languages-{name}.svg", "w").write(languages_svg(t, data["languages"]))
        open(f"{out}/stats-{name}.svg", "w").write(stats_svg(t, data))
    print(f"cards written to {out}: {len(data['languages'])} languages, {data['repos']} repos")


if __name__ == "__main__":
    main()
