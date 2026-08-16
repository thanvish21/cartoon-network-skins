#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a Hermes-style banner screenshot for every skin.

Builds one HTML page per skin (logo + hero art + palette + branding,
mimicking the Hermes CLI startup banner), then captures it with headless
Chromium into screenshots/<slug>.png.

Usage:
  python3 make_screenshots.py            # render all skins
  python3 make_screenshots.py --slug X   # render one skin only
  python3 make_screenshots.py --html-only # write HTML only (no chromium)
"""

import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

import yaml

CHROME = shutil.which("chromium") or shutil.which("google-chrome") or "chromium"
WIN_W, WIN_H = 960, 660
SCALE = 1.5

TOOLS_LINE_1 = ["terminal", "web_search", "read_file", "write_file", "search_files"]
TOOLS_LINE_2 = ["execute_code", "browser_navigate", "delegate_task", "memory", "cronjob"]

TAG_RE = re.compile(r"\[(bold )?#([0-9A-Fa-f]{6})\](.*?)\[/\]", re.S)


def rich_to_segments(text):
    """Split Rich markup into (text, (color, bold)) segments."""
    segs = []
    pos = 0
    for m in TAG_RE.finditer(text):
        if m.start() > pos:
            segs.append((text[pos:m.start()], None))
        bold = bool(m.group(1))
        color = m.group(2)
        segs.append((m.group(3), (color, bold)))
        pos = m.end()
    if pos < len(text):
        segs.append((text[pos:], None))
    return segs


def segs_html(segs):
    out = []
    for txt, style in segs:
        t = html.escape(txt)
        if style:
            color, bold = style
            s = "color:#%s" % color
            if bold:
                s += ";font-weight:bold"
            out.append('<span style="%s">%s</span>' % (s, t))
        else:
            out.append(t)
    return "".join(out)


def plain_width(segs):
    return sum(len(t) for t, _ in segs)


def seg(txt, color=None, bold=False):
    return [(txt, (color, bold) if color else None)]


def fit(txt, width):
    return txt if len(txt) <= width else txt[: width - 1] + "…"


def build_banner(skin):
    c = skin["colors"]
    logo = skin["banner_logo"]
    hero = skin["banner_hero"]

    logo_rows = [rich_to_segments(line) for line in logo.split("\n")]
    hero_rows = [rich_to_segments(line) for line in hero.split("\n")]
    W = max([plain_width(r) for r in logo_rows + hero_rows] + [58])

    def pad_segs(segs, width, align="center"):
        w = plain_width(segs)
        if align == "center":
            left = (width - w) // 2
            right = width - w - left
            return seg(" " * left, c["banner_dim"]) + segs + seg(" " * right, c["banner_dim"])
        return segs + seg(" " * (width - w), c["banner_dim"])

    def border_line(left, right):
        return [(left + "─" * W + right, (c["banner_border"], False))]

    def content_line(segs):
        return [("│", (c["banner_border"], False))] + segs + [("│", (c["banner_border"], False))]

    rows = []
    rows.append(border_line("╭", "╮"))

    blank = lambda: content_line(pad_segs([], W))
    rows.append(blank())

    for r in logo_rows:
        rows.append(content_line(pad_segs(r, W)))
    rows.append(blank())

    for r in hero_rows:
        rows.append(content_line(pad_segs(r, W)))
    rows.append(blank())

    # Available tools
    rows.append(content_line(pad_segs(seg("AVAILABLE TOOLS", c["banner_accent"]), W, "left")))
    for names in (TOOLS_LINE_1, TOOLS_LINE_2):
        tool_segs = []
        for i, name in enumerate(names):
            emoji = skin["tool_emojis"].get(name, "•")
            tool_segs += seg(emoji + " ", c["ui_accent"])
            tool_segs += seg(name, c["banner_text"])
            if i < len(names) - 1:
                tool_segs += seg("   ", c["banner_dim"])
        rows.append(content_line(pad_segs(tool_segs, W, "left")))
    rows.append(blank())

    # Divider
    rows.append(content_line(seg("─" * W, c["banner_dim"])))
    rows.append(blank())

    # Branding
    agent = skin["branding"]["agent_name"]
    desc = fit(skin["description"], W - 4)
    welcome = fit(skin["branding"]["welcome"], W - 4)
    rows.append(content_line(pad_segs(seg(agent, c["banner_title"], bold=True), W)))
    rows.append(content_line(pad_segs(seg(desc, c["banner_dim"]), W)))
    rows.append(content_line(pad_segs(seg(welcome, c["banner_text"]), W)))
    rows.append(blank())

    # Input rule + prompt
    rows.append(content_line(seg("─" * W, c["input_rule"])))
    sym = skin["branding"]["prompt_symbol"]
    rows.append(content_line(seg(sym, c["prompt"]) + seg("_", c["banner_dim"])))
    rows.append(border_line("╰", "╯"))

    html_rows = []
    for segs in rows:
        html_rows.append(segs_html(segs))
    return html_rows, W


HTML_TMPL = """<!doctype html>
<html><head><meta charset="utf-8"><style>
  body {{
    margin: 0; background: #000;
    display: flex; align-items: center; justify-content: center;
    height: 100vh; overflow: hidden;
  }}
  pre {{
    margin: 0;
    font-family: 'DejaVu Sans Mono', 'Noto Sans Mono', monospace;
    font-size: 14px; line-height: 1.2;
  }}
</style></head><body><pre>{body}</pre></body></html>"""


def skin_html(skin):
    rows, _ = build_banner(skin)
    return HTML_TMPL.format(body="\n".join(rows))


def screenshot(slug, html_path, png_path):
    subprocess.run(
        [
            CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--hide-scrollbars", "--force-device-scale-factor=%s" % SCALE,
            "--screenshot=" + png_path, "--window-size=%d,%d" % (WIN_W, WIN_H),
            "file://" + html_path,
        ],
        check=True, capture_output=True,
    )


def main():
    only_html = "--html-only" in sys.argv
    slug_filter = None
    if "--slug" in sys.argv:
        slug_filter = sys.argv[sys.argv.index("--slug") + 1]

    os.makedirs("screenshots", exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="skin_html_")

    skins = []
    for fname in sorted(os.listdir("skins")):
        if not fname.endswith(".yaml"):
            continue
        with open(os.path.join("skins", fname), encoding="utf-8") as fh:
            skins.append(yaml.safe_load(fh))

    if slug_filter:
        skins = [s for s in skins if s["name"] == slug_filter]

    total = len(skins)

    def render_one(args):
        i, skin = args
        slug = skin["name"]
        html_path = os.path.join(tmp, slug + ".html")
        with open(html_path, "w", encoding="utf-8") as fh:
            fh.write(skin_html(skin))
        if only_html:
            print("html:", slug)
            return
        png_path = os.path.abspath(os.path.join("screenshots", slug + ".png"))
        screenshot(slug, html_path, png_path)
        print("[%d/%d] %s" % (i, total, slug), flush=True)

    workers = int(os.environ.get("SCREENSHOT_WORKERS", "8"))
    if only_html:
        for args in enumerate(skins, 1):
            render_one(args)
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            list(pool.map(render_one, enumerate(skins, 1)))

    shutil.rmtree(tmp, ignore_errors=True)
    if not only_html:
        print("Done: %d screenshots in screenshots/" % total)


if __name__ == "__main__":
    main()
