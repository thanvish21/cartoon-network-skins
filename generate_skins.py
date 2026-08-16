#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Cartoon Network-themed Hermes skins.

Reads the show databases in shows_data1.py / shows_data2.py and emits:
  - skins/<slug>.yaml   (one Hermes skin per show, full 28-color schema)
  - README.md           (gallery grouped by category)
  - SCHEMA.md           (schema reference)
  - LICENSE             (MIT)

Usage:
  python3 generate_skins.py          # generate everything + validate
  python3 generate_skins.py --check  # validate existing skins/ only
"""

import os
import re
import sys

import yaml

from shows_data1 import SHOWS_A
from shows_data2 import SHOWS_B
from hero_icons import ICONS
from character_art import CHARACTERS
from show_extras import ICON_MAP, SKILLS_MAP, CHARACTER_MAP

SHOWS = SHOWS_A + SHOWS_B

# Logo gradient end per category: s (secondary), text, or white
LOGO_GRADIENT = {
    "Ben 10 Universe": "s",
    "Cartoon Cartoons & Classics": "text",
    "Modern Cartoon Network": "s",
    "DC Super Heroes": "text",
    "Star Wars & LEGO": "s",
    "Toonami & Action": "white",
    "Adult Swim": "s",
    "Acquired & International": "text",
    "Cartoon Network India": "s",
}

CATEGORY_ORDER = [
    "Ben 10 Universe",
    "Cartoon Cartoons & Classics",
    "Modern Cartoon Network",
    "DC Super Heroes",
    "Star Wars & LEGO",
    "Toonami & Action",
    "Adult Swim",
    "Acquired & International",
    "Cartoon Network India",
]

CATEGORY_FRAME = {
    "Ben 10 Universe": "─",
    "Cartoon Cartoons & Classics": "─",
    "Modern Cartoon Network": "┄",
    "DC Super Heroes": "═",
    "Star Wars & LEGO": "═",
    "Toonami & Action": "┈",
    "Adult Swim": "╌",
    "Acquired & International": "─",
    "Cartoon Network India": "┄",
}

# ---------------------------------------------------------------- color utils

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*[max(0, min(255, int(round(c)))) for c in rgb])


def mix(c1, c2, t):
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    return rgb_to_hex(tuple(a[i] + (b[i] - a[i]) * t for i in range(3)))


def lighten(h, amt):
    return mix(h, "#FFFFFF", amt)


def darken(h, amt):
    return mix(h, "#000000", amt)


def luminance(h):
    r, g, b = hex_to_rgb(h)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255.0


def ensure_light(h, min_lum=0.55):
    """Brighten until the color is readable against a dark background."""
    cur = h
    for _ in range(12):
        if luminance(cur) >= min_lum:
            break
        cur = lighten(cur, 0.12)
    return cur


HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")

# ---------------------------------------------------------------- ASCII font

FONT = {
    "A": [".###.", "#...#", "#####", "#...#", "#...#"],
    "B": ["####.", "#...#", "####.", "#...#", "####."],
    "C": [".####", "#....", "#....", "#....", ".####"],
    "D": ["####.", "#...#", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "####.", "#....", "#####"],
    "F": ["#####", "#....", "####.", "#....", "#...."],
    "G": [".####", "#....", "#..##", "#...#", ".####"],
    "H": ["#...#", "#...#", "#####", "#...#", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "#####"],
    "J": ["..###", "...#.", "...#.", "#..#.", ".##.."],
    "K": ["#...#", "#..#.", "###..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#...#", "#...#"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "####.", "#....", "#...."],
    "Q": [".###.", "#...#", "#.#.#", "#..##", ".##.#"],
    "R": ["####.", "#...#", "####.", "#..#.", "#...#"],
    "S": [".####", "#....", ".###.", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#.#.#", "##.##", "#...#"],
    "X": ["#...#", ".#.#.", "..#..", ".#.#.", "#...#"],
    "Y": ["#...#", ".#.#.", "..#..", "..#..", "..#.."],
    "Z": ["#####", "...#.", "..#..", ".#...", "#####"],
    "0": [".###.", "#..##", "#.#.#", "##..#", ".###."],
    "1": ["..#..", ".##..", "..#..", "..#..", "#####"],
    "2": [".###.", "....#", ".###.", "#....", "#####"],
    "3": ["####.", "....#", ".###.", "....#", "####."],
    "4": ["#..#.", "#..#.", "#####", "...#.", "...#."],
    "5": ["#####", "#....", "####.", "....#", "####."],
    "6": [".###.", "#....", "####.", "#...#", ".###."],
    "7": ["#####", "...#.", "..#..", ".#...", ".#..."],
    "8": [".###.", "#...#", ".###.", "#...#", ".###."],
    "9": [".###.", "#...#", ".####", "....#", ".###."],
    "-": [".....", ".....", "#####", ".....", "....."],
    ".": [".....", ".....", ".....", "..##.", "..##."],
    "!": ["..#..", "..#..", "..#..", ".....", "..#.."],
    "?": [".###.", "....#", "..##.", ".....", "..#.."],
    "&": [".###.", "#...#", "..#..", ".#.#.", "##..#"],
    "'": ["..#..", "..#..", ".....", ".....", "....."],
    " ": [".....", ".....", ".....", ".....", "....."],
}


def gradient_colors(text, c1, c2, n=1):
    """Per-character colors from c1 -> c2 with t^1.5 easing."""
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    out = []
    for i in range(len(text)):
        t = (i / max(len(text) - 1, 1)) ** 1.5
        out.append(rgb_to_hex(tuple(a[j] + (b[j] - a[j]) * t for j in range(3))))
    return out


def render_logo(text, c1, c2, underline=None):
    """Render TEXT as a colored 5-row ASCII block logo with per-char gradient."""
    text = text.upper()
    colors = gradient_colors(text, c1, c2)
    rows = []
    for row in range(5):
        line = ""
        for i, ch in enumerate(text):
            glyph = FONT.get(ch, FONT[" "])
            line += f"[{colors[i]}]{glyph[row]}[/] "
        rows.append(line.rstrip())
    if underline:
        width = sum(len(FONT.get(ch, FONT[" "])[0]) + 1 for ch in text) - 1
        rows.append(f"[{underline}]{'─' * width}[/]")
    return "\n".join(rows)


def _frame_hero(rows, caption, width, p, a):
    cap = caption.upper()
    if len(cap) > width:
        cap = cap[: width - 1] + "…"
    return ([f"[{p}]{'─' * width}[/]"] + rows +
            [f"[bold {a}]{cap.center(width)}[/]", f"[{p}]{'─' * width}[/]"])


def render_hero_art(art, caption, p, s, a, muted):
    """Render hand-drawn hero art with a per-row palette ramp and caption."""
    ramp = [muted, p, s, a]
    n = len(art)

    def ramp_color(t):
        pos = t * (len(ramp) - 1)
        i = min(int(pos), len(ramp) - 2)
        f = pos - i
        return mix(ramp[i], ramp[i + 1], f)

    width = max(len(r) for r in art)
    rows = []
    for i, row in enumerate(art):
        t = i / max(n - 1, 1)
        rows.append(f"[{ramp_color(t)}]{row}[/]")
    return "\n".join(_frame_hero(rows, caption, width, p, a))


def render_character(art, caption, p, s, a, bg, tx):
    """Render a main-character portrait with per-cell palette colors."""
    def cell_color(ch):
        if ch == "#":
            return mix(bg, tx, 0.5)
        if ch == "S":
            return lighten(p, 0.68)
        if ch == "H":
            return s
        if ch == "E":
            return a
        if ch == "M":
            return mix(a, bg, 0.3)
        if ch == "W":
            return lighten(a, 0.55)
        return None

    width = max(len(r) for r in art)
    rows = []
    for row in art:
        line = ""
        for ch in row:
            col = cell_color(ch)
            if col:
                line += f"[{col}]{ch}[/]"
            else:
                line += " "
        rows.append(line)
    return "\n".join(_frame_hero(rows, caption, width, p, a))


# ---------------------------------------------------------------- skin builder

DEFAULT_TOOL_EMOJIS = {
    "terminal": "⌁",
    "web_search": "◎",
    "read_file": "◇",
    "write_file": "◆",
    "search_files": "▷",
    "execute_code": "⚡",
    "browser_navigate": "◈",
    "delegate_task": "▣",
    "mixture_of_agents": "⚗",
    "memory": "◐",
    "clarify": "?",
    "cronjob": "↻",
    "process": "⚙",
    "todo": "☐",
}

COLOR_KEYS = [
    "banner_border", "banner_title", "banner_accent", "banner_dim", "banner_text",
    "ui_accent", "ui_label", "ui_ok", "ui_error", "ui_warn",
    "prompt", "input_rule", "response_border",
    "status_bar_bg", "status_bar_text", "status_bar_strong", "status_bar_dim",
    "status_bar_good", "status_bar_warn", "status_bar_bad", "status_bar_critical",
    "voice_status_bg",
    "completion_menu_bg", "completion_menu_current_bg",
    "completion_menu_meta_bg", "completion_menu_meta_current_bg",
    "session_label", "session_border",
]


def derive_colors(show):
    (slug, title, desc, agent, welcome, goodbye, sym, verbs,
     p, s, a, bg, tx, cat, logo) = show
    muted = mix(bg, tx, 0.35)
    bar_bg = lighten(bg, 0.08)
    return {
        "banner_border": p,
        "banner_title": ensure_light(a),
        "banner_accent": ensure_light(a),
        "banner_dim": muted,
        "banner_text": tx,
        "ui_accent": a,
        "ui_label": s,
        "ui_ok": "#4CAF50",
        "ui_error": "#EF5350",
        "ui_warn": "#FFA726",
        "prompt": tx,
        "input_rule": p,
        "response_border": a,
        "status_bar_bg": bar_bg,
        "status_bar_text": tx,
        "status_bar_strong": a,
        "status_bar_dim": muted,
        "status_bar_good": "#8FBC8F",
        "status_bar_warn": "#FFA726",
        "status_bar_bad": "#FF8C00",
        "status_bar_critical": "#EF5350",
        "voice_status_bg": bar_bg,
        "completion_menu_bg": bg,
        "completion_menu_current_bg": mix(bg, a, 0.32),
        "completion_menu_meta_bg": darken(bg, 0.15),
        "completion_menu_meta_current_bg": mix(bg, a, 0.28),
        "session_label": s,
        "session_border": muted,
    }


def build_skin(show):
    (slug, title, desc, agent, welcome, goodbye, sym, verbs,
     p, s, a, bg, tx, cat, logo) = show
    if not logo:
        logo = title if len(title) <= 14 else title.split()[-1].upper()

    colors = derive_colors(show)
    muted = mix(bg, tx, 0.35)
    grad_end = LOGO_GRADIENT.get(cat, "s")
    if grad_end == "text":
        logo_c2 = tx
    elif grad_end == "white":
        logo_c2 = "#FFFFFF"
    else:
        logo_c2 = s
    char_key = CHARACTER_MAP.get(slug)
    if char_key and char_key in CHARACTERS:
        banner_hero = render_character(CHARACTERS[char_key], title, p, s, a, bg, tx)
    else:
        icon = ICON_MAP.get(slug, "star")
        art = ICONS.get(icon, ICONS["star"])
        banner_hero = render_hero_art(art, title, p, s, a, mix(bg, tx, 0.35))
    skin = {
        "name": slug,
        "description": desc,
        "colors": colors,
        "spinner": {
            "waiting_faces": [f"({sym})", "(◉)", "(◎)", "(◯)", "(●)"],
            "thinking_faces": [f"({sym})", "(◉)", "(⌁)", "(<>)"],
            "thinking_verbs": verbs,
            "wings": [
                [f"⟪{sym}", f"{sym}⟫"],
                ["⟪◉", "◉⟫"],
                ["⟪●", "●⟫"],
            ],
        },
        "branding": {
            "agent_name": agent,
            "welcome": welcome,
            "goodbye": goodbye,
            "response_label": f" {sym} {logo} ",
            "prompt_symbol": f"{sym} ❯ ",
            "help_header": f"({sym}) {logo} Commands",
        },
        "tool_prefix": "┊",
        "tool_emojis": dict(DEFAULT_TOOL_EMOJIS),
        "banner_logo": render_logo(logo, a, logo_c2, underline=muted),
        "banner_hero": banner_hero,
    }
    return skin


class LiteralStr(str):
    """Marker type: force YAML literal-block style for multi-line strings."""


def _represent_literal(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(LiteralStr, _represent_literal, Dumper=yaml.SafeDumper)


def dump_yaml(skin):
    skin = dict(skin)
    skin["banner_logo"] = LiteralStr(skin["banner_logo"])
    skin["banner_hero"] = LiteralStr(skin["banner_hero"])
    return yaml.safe_dump(
        skin,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=10000,
        indent=2,
    )


# ---------------------------------------------------------------- validation

def validate_skin(path):
    errors = []
    with open(path, encoding="utf-8") as fh:
        try:
            data = yaml.safe_load(fh)
        except yaml.YAMLError as e:
            return [f"YAML parse error: {e}"]

    stem = os.path.splitext(os.path.basename(path))[0]
    if data.get("name") != stem:
        errors.append(f"name {data.get('name')!r} != filename {stem!r}")

    colors = data.get("colors") or {}
    missing = [k for k in COLOR_KEYS if k not in colors]
    if missing:
        errors.append(f"missing color keys: {missing}")
    for k, v in colors.items():
        if not isinstance(v, str) or not HEX_RE.match(v):
            errors.append(f"bad hex for {k}: {v!r}")

    spin = data.get("spinner") or {}
    for k in ("waiting_faces", "thinking_faces", "thinking_verbs", "wings"):
        if not isinstance(spin.get(k), list) or not spin[k]:
            errors.append(f"spinner.{k} missing/empty")

    brand = data.get("branding") or {}
    for k in ("agent_name", "welcome", "goodbye", "response_label", "prompt_symbol", "help_header"):
        if not brand.get(k):
            errors.append(f"branding.{k} missing")

    if not data.get("tool_prefix"):
        errors.append("tool_prefix missing")
    emojis = data.get("tool_emojis") or {}
    if set(emojis) != set(DEFAULT_TOOL_EMOJIS):
        errors.append("tool_emojis keys mismatch")

    if not data.get("banner_logo") or not data.get("banner_hero"):
        errors.append("banner_logo/banner_hero missing")

    return errors


# ---------------------------------------------------------------- docs

def build_readme():
    lines = []
    lines.append("# Cartoon Network Hermes Skins")
    lines.append("")
    lines.append(
        "Custom skins (visual themes) for the "
        "[Hermes](https://github.com/NousResearch/hermes-agent) CLI agent, "
        "themed after Cartoon Network shows — from Ben 10 to Roll No. 21, "
        "Powerpuff Girls to Toonami classics, and everything in between."
    )
    lines.append("")
    lines.append("Skins control the **visual presentation** of Hermes: banner colors, spinner faces/verbs, "
                 "response-box labels, branding text, tool activity prefix, and ASCII art banners. "
                 "They don't affect personality or behavior — just how things look.")
    lines.append("")
    lines.append(f"**{len(SHOWS)} skins** — every one defines the full 28-color schema, a themed spinner, "
                 "branding with show-flavored welcome/goodbye lines, a colored ASCII logo, a **unique hand-drawn "
                 "hero icon themed to the show** (Omnitrix, bat, skull, dragon ball, paw, spiral, portal…), "
                 "show-specific skills, and a rendered banner screenshot (see `screenshots/`).")
    lines.append("")
    lines.append("Screenshots are rendered straight from each skin's YAML — palette, ASCII logo, hero art and "
                 "branding — via `make_screenshots.py` (headless Chromium), so what you see is what the skin looks like.")
    lines.append("")
    lines.append("## Quick Start")
    lines.append("")
    lines.append("1. Browse the `skins/` directory and pick one you like")
    lines.append("2. Copy the `.yaml` file to `~/.hermes/skins/`")
    lines.append("3. Activate it:")
    lines.append("")
    lines.append("```bash")
    lines.append("# Session-only")
    lines.append("/skin ben-10")
    lines.append("# Permanent (add to ~/.hermes/config.yaml)")
    lines.append("display:")
    lines.append("  skin: ben-10")
    lines.append("```")
    lines.append("")
    lines.append("Missing values inherit from the default skin, so partial skins work too — "
                 "but these all define the complete schema, so they look right out of the box.")
    lines.append("")
    lines.append("## Available Skins")
    lines.append("")

    by_cat = {}
    for show in SHOWS:
        by_cat.setdefault(show[13], []).append(show)

    for cat in CATEGORY_ORDER:
        shows = by_cat.get(cat, [])
        if not shows:
            continue
        lines.append(f"### {cat}")
        lines.append("")
        lines.append("| Skin | Description | File | Screenshot |")
        lines.append("|------|-------------|------|------------|")
        for show in shows:
            slug, title, desc = show[0], show[1], show[2]
            lines.append(
                f"| **{title}** | {desc} | [`{slug}.yaml`](skins/{slug}.yaml) | "
                f"<img src=\"screenshots/{slug}.png\" width=\"180\" alt=\"{title} skin\"> |"
            )
        lines.append("")

    lines.append("## Themes for Other AI Coding Tools")
    lines.append("")
    lines.append("Every show also ships as a ready-to-use theme for Claude Code and OpenCode "
                 "(same palette, ported from the Hermes skin).")
    lines.append("")
    lines.append("### Claude Code")
    lines.append("")
    lines.append("Each theme is a JSON file in `themes/claude-code/` with the official Claude Code format "
                 "(`base: dark` + color token `overrides`). Install:")
    lines.append("")
    lines.append("```bash")
    lines.append("mkdir -p ~/.claude/themes")
    lines.append("cp themes/claude-code/ben-10.json ~/.claude/themes/")
    lines.append("claude   # then run /theme and pick 'Ben 10'")
    lines.append("```")
    lines.append("")
    lines.append("### OpenCode")
    lines.append("")
    lines.append("Each theme is a JSON file in `themes/opencode/` following the official `theme.json` schema "
                 "(dark/light pairs, markdown + syntax tokens). Install:")
    lines.append("")
    lines.append("```bash")
    lines.append("mkdir -p ~/.config/opencode/themes")
    lines.append("cp themes/opencode/ben-10.json ~/.config/opencode/themes/")
    lines.append("opencode   # then run /theme and pick 'Ben 10'")
    lines.append("```")
    lines.append("")
    lines.append("Regenerate them any time with `python3 generate_themes.py`.")
    lines.append("")
    lines.append("### Freebuff")
    lines.append("")
    lines.append("Freebuff is a terminal-based AI coding agent and does not expose a theme file format "
                 "to customize — the pack's palettes still apply to whatever terminal you run it in "
                 "(see the Hermes skin colors for the hex values).")
    lines.append("")
    lines.append("## How Skins Work")
    lines.append("")
    lines.append("Hermes loads skins from two locations (user skins take priority):")
    lines.append("")
    lines.append("1. `~/.hermes/skins/<name>.yaml` (user custom)")
    lines.append("2. Built-in skins hardcoded in `skin_engine.py`")
    lines.append("")
    lines.append("The engine merges your skin on top of `default`, so partial skins work fine. "
                 "Unknown skin names silently fall back to `default`.")
    lines.append("")
    lines.append("## Creating Your Own")
    lines.append("")
    lines.append("Drop a YAML file in `~/.hermes/skins/<name>.yaml`. The `name:` field inside must match the filename. "
                 "See [SCHEMA.md](SCHEMA.md) for the complete list of configurable keys, or regenerate everything "
                 "after editing the databases:")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 generate_skins.py   # regenerate skins/ + docs + validate")
    lines.append("python3 generate_skins.py --check   # validate existing skins/ only")
    lines.append("```")
    lines.append("")
    lines.append("## Disclaimer")
    lines.append("")
    lines.append("This is a fan-made project. Cartoon Network, and all show names, characters and related properties "
                 "are trademarks of their respective owners (Warner Bros. Discovery and others). This project is not "
                 "affiliated with, endorsed by, or sponsored by Cartoon Network or Warner Bros. Discovery. "
                 "The skin YAML files themselves are original creations released under the MIT license.")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("[MIT](LICENSE)")
    lines.append("")
    return "\n".join(lines)


SCHEMA_MD = """# Hermes Skin Schema
Complete reference for all configurable skin keys. Every skin in this repo defines the full schema below.

## Top-Level Structure
```yaml
name: myskin          # Required. Must match filename.
description: Short description
colors: { ... }       # 28 color keys (hex strings)
spinner: { ... }      # 4 spinner keys (lists)
branding: { ... }     # 6 branding keys (strings)
tool_prefix: "┊"      # Character prefixed to tool output lines
tool_emojis: { ... }  # Per-tool emoji overrides
banner_logo: |        # Rich-markup ASCII art logo (replaces HERMES_AGENT banner)
banner_hero: |        # Rich-markup hero art (replaces caduceus art)
```

## Colors (28 keys)
| Key | What it colors |
|-----|----------------|
| `banner_border` | Panel border around startup banner |
| `banner_title` | Title text in banner |
| `banner_accent` | Section headers in banner |
| `banner_dim` | Muted text (separators, secondary labels) |
| `banner_text` | Body text (tool names, skill names) |
| `ui_accent` | General UI accent (highlights, active elements) |
| `ui_label` | UI labels and tags |
| `ui_ok` | Success indicators |
| `ui_error` | Error indicators |
| `ui_warn` | Warning indicators |
| `prompt` | Interactive prompt text |
| `input_rule` | Horizontal rule above input area |
| `response_border` | Response box border (ANSI escape) |
| `status_bar_bg` | Prompt/TUI status bar background |
| `status_bar_text` | Status bar default text |
| `status_bar_strong` | Status bar highlighted text |
| `status_bar_dim` | Status bar separators/muted text |
| `status_bar_good` | Healthy context/status indicators |
| `status_bar_warn` | Warning context/status indicators |
| `status_bar_bad` | High-usage context/status indicators |
| `status_bar_critical` | Critical context/status indicators |
| `voice_status_bg` | Voice status pill background |
| `completion_menu_bg` | Completion menu background |
| `completion_menu_current_bg` | Active completion row background |
| `completion_menu_meta_bg` | Completion metadata background |
| `completion_menu_meta_current_bg` | Active completion metadata background |
| `session_label` | Session label color |
| `session_border` | Session ID dim border color |

## Spinner (4 keys)
| Key | Type | Description |
|-----|------|-------------|
| `waiting_faces` | list of strings | Faces cycled while waiting for API |
| `thinking_faces` | list of strings | Faces cycled during model reasoning |
| `thinking_verbs` | list of strings | Verbs shown in spinner messages |
| `wings` | list of [left, right] | Decorative brackets around spinner |

## Branding (6 keys)
| Key | Description |
|-----|-------------|
| `agent_name` | Banner title and status display |
| `welcome` | CLI startup message |
| `goodbye` | Exit message |
| `response_label` | Response box header label |
| `prompt_symbol` | Symbol before user input |
| `help_header` | /help command header |

## Other Keys
| Key | Type | Description |
|-----|------|-------------|
| `tool_prefix` | string | Character prefixed to tool output lines |
| `tool_emojis` | dict | Per-tool emoji overrides `{tool_name: emoji}` |
| `banner_logo` | string | Rich-markup ASCII art logo |
| `banner_hero` | string | Rich-markup hero art |

Valid tool names: `terminal`, `web_search`, `read_file`, `write_file`, `search_files`, `execute_code`,
`browser_navigate`, `delegate_task`, `mixture_of_agents`, `memory`, `clarify`, `cronjob`, `process`, `todo`.

## Rich Markup
`banner_logo`, `banner_hero`, `welcome`, and `goodbye` all support Rich console markup:
```
[bold #FFD000]Gold bold text[/]
[dim #555555]Dimmed text[/]
[#FF0000]Red text[/]
```

## Inheritance
Missing values inherit from the `default` skin. You only need to define what you want to change.
"""

LICENSE = """MIT License

Copyright (c) 2026 Thanvish (thanvish21)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

Fan-made project. Cartoon Network and all show names, characters and related
properties are trademarks of their respective owners. This project is not
affiliated with or endorsed by Cartoon Network or Warner Bros. Discovery.
"""


# ---------------------------------------------------------------- main

def validate_db():
    errors = []
    slugs = set()
    for show in SHOWS:
        slug = show[0]
        if slug in slugs:
            errors.append(f"duplicate slug: {slug}")
        slugs.add(slug)
        if not HEX_RE.match(show[8]) or not HEX_RE.match(show[9]) or \
           not HEX_RE.match(show[10]) or not HEX_RE.match(show[11]) or \
           not HEX_RE.match(show[12]):
            errors.append(f"bad palette hex in {slug}")
        if len(show[7]) < 4:
            errors.append(f"too few verbs in {slug}")
    return errors


def main():
    only_check = "--check" in sys.argv

    db_errors = validate_db()
    if db_errors:
        for e in db_errors:
            print("DB ERROR:", e)
        sys.exit(1)

    if only_check:
        check_existing()
        return

    os.makedirs("skins", exist_ok=True)
    total_errors = 0
    for show in SHOWS:
        slug = show[0]
        skin = build_skin(show)
        with open(os.path.join("skins", f"{slug}.yaml"), "w", encoding="utf-8") as fh:
            fh.write(dump_yaml(skin))

    # validation pass
    for show in SHOWS:
        slug = show[0]
        errors = validate_skin(os.path.join("skins", f"{slug}.yaml"))
        for e in errors:
            print(f"ERROR {slug}: {e}")
            total_errors += 1

    if total_errors:
        print(f"\n{total_errors} validation errors — aborting docs write.")
        sys.exit(1)

    with open("README.md", "w", encoding="utf-8") as fh:
        fh.write(build_readme())
    with open("SCHEMA.md", "w", encoding="utf-8") as fh:
        fh.write(SCHEMA_MD)
    with open("LICENSE", "w", encoding="utf-8") as fh:
        fh.write(LICENSE)

    print(f"Generated {len(SHOWS)} skins in skins/ — all validated OK.")
    print("Wrote README.md, SCHEMA.md, LICENSE.")


def check_existing():
    if not os.path.isdir("skins"):
        print("No skins/ directory found.")
        sys.exit(1)
    total = 0
    errors = 0
    for fname in sorted(os.listdir("skins")):
        if not fname.endswith(".yaml"):
            continue
        total += 1
        errs = validate_skin(os.path.join("skins", fname))
        for e in errs:
            print(f"ERROR {fname}: {e}")
            errors += 1
    print(f"Checked {total} skins, {errors} errors.")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
