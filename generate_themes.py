#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Port every skin palette to Claude Code and OpenCode theme formats.

Emits:
  themes/claude-code/<slug>.json   -> ~/.claude/themes/
  themes/opencode/<slug>.json      -> ~/.config/opencode/themes/

Usage:
  python3 generate_themes.py
"""

import json
import os

from generate_skins import SHOWS, mix, lighten, darken

OUT_CLAUDE = "themes/claude-code"
OUT_OPENCODE = "themes/opencode"

OK = "#4CAF50"
ERR = "#EF5350"
WARN = "#FFA726"


def claude_theme(show):
    slug, title, _, _, _, _, _, _, p, s, a, bg, tx, _, _ = show
    muted = mix(bg, tx, 0.35)
    return {
        "name": title,
        "base": "dark",
        "overrides": {
            # text & accent
            "claude": a,
            "claudeShimmer": lighten(a, 0.35),
            "text": tx,
            "inverseText": darken(tx, 0.75),
            "inactive": muted,
            "subtle": darken(muted, 0.25),
            "suggestion": lighten(a, 0.35),
            "permission": a,
            "remember": a,
            # status
            "success": OK,
            "error": ERR,
            "warning": WARN,
            "merged": "#8FBC8F",
            # input & modes
            "promptBorder": p,
            "promptBorderShimmer": lighten(p, 0.3),
            "planMode": a,
            "autoAccept": a,
            "bashBorder": s,
            "fastMode": a,
            # diffs
            "diffAdded": mix(bg, OK, 0.3),
            "diffRemoved": mix(bg, ERR, 0.3),
            "diffAddedDimmed": mix(bg, OK, 0.18),
            "diffRemovedDimmed": mix(bg, ERR, 0.18),
            "diffAddedWord": lighten(OK, 0.25),
            "diffRemovedWord": lighten(ERR, 0.25),
            # fullscreen surfaces
            "userMessageBackground": lighten(bg, 0.06),
            "userMessageBackgroundHover": lighten(bg, 0.11),
            "bashMessageBackgroundColor": lighten(bg, 0.06),
            "memoryBackgroundColor": lighten(bg, 0.09),
            "selectionBg": mix(bg, a, 0.35),
            # usage meter & labels
            "rate_limit_fill": a,
            "rate_limit_empty": muted,
            "briefLabelYou": tx,
            "briefLabelClaude": a,
            # subagent palette
            "red_FOR_SUBAGENTS_ONLY": "#EF5350",
            "blue_FOR_SUBAGENTS_ONLY": "#60A5FA",
            "green_FOR_SUBAGENTS_ONLY": OK,
            "yellow_FOR_SUBAGENTS_ONLY": "#FFD54F",
            "purple_FOR_SUBAGENTS_ONLY": "#BA68C8",
            "orange_FOR_SUBAGENTS_ONLY": WARN,
            "pink_FOR_SUBAGENTS_ONLY": "#F48FB1",
            "cyan_FOR_SUBAGENTS_ONLY": "#4DD0E1",
            # rainbow (ultrathink keyword)
            "rainbow_red": "#FF5252",
            "rainbow_orange": "#FFA726",
            "rainbow_yellow": "#FFD54F",
            "rainbow_green": "#66BB6A",
            "rainbow_blue": "#42A5F5",
            "rainbow_indigo": "#7E57C2",
            "rainbow_violet": "#AB47BC",
        },
    }


def pair(dark_c, light_c=None):
    return {"dark": dark_c, "light": light_c if light_c else dark_c}


def opencode_theme(show):
    slug, title, _, _, _, _, _, _, p, s, a, bg, tx, _, _ = show
    muted = mix(bg, tx, 0.35)
    light_bg = lighten(bg, 0.88)
    light_text = darken(tx, 0.8)

    def d(hex_c):
        return {"dark": hex_c, "light": darken(hex_c, 0.3)}

    def dd(hex_c):
        return {"dark": hex_c, "light": darken(hex_c, 0.55)}

    return {
        "$schema": "https://opencode.ai/theme.json",
        "theme": {
            "primary": d(a),
            "secondary": d(s),
            "accent": d(a),
            "error": dd(ERR),
            "warning": dd(WARN),
            "success": dd(OK),
            "info": d(a),
            "text": {"dark": tx, "light": light_text},
            "textMuted": {"dark": muted, "light": darken(muted, 0.45)},
            "background": {"dark": bg, "light": light_bg},
            "backgroundPanel": {"dark": lighten(bg, 0.06), "light": lighten(bg, 0.78)},
            "backgroundElement": {"dark": lighten(bg, 0.1), "light": lighten(bg, 0.72)},
            "border": {"dark": mix(bg, tx, 0.3), "light": darken(tx, 0.7)},
            "borderActive": d(a),
            "borderSubtle": {"dark": mix(bg, tx, 0.2), "light": darken(tx, 0.6)},
            "diffAdded": dd(OK),
            "diffRemoved": dd(ERR),
            "diffContext": {"dark": muted, "light": darken(muted, 0.4)},
            "diffHunkHeader": d(a),
            "diffHighlightAdded": dd(lighten(OK, 0.15)),
            "diffHighlightRemoved": dd(lighten(ERR, 0.15)),
            "diffAddedBg": {"dark": mix(bg, OK, 0.18), "light": lighten(OK, 0.7)},
            "diffRemovedBg": {"dark": mix(bg, ERR, 0.18), "light": lighten(ERR, 0.7)},
            "diffContextBg": {"dark": lighten(bg, 0.04), "light": lighten(bg, 0.8)},
            "diffLineNumber": {"dark": muted, "light": darken(muted, 0.4)},
            "diffAddedLineNumberBg": {"dark": mix(bg, OK, 0.15), "light": lighten(OK, 0.7)},
            "diffRemovedLineNumberBg": {"dark": mix(bg, ERR, 0.15), "light": lighten(ERR, 0.7)},
            "markdownText": {"dark": tx, "light": light_text},
            "markdownHeading": d(a),
            "markdownLink": d(a),
            "markdownLinkText": d(a),
            "markdownCode": d(OK),
            "markdownBlockQuote": {"dark": muted, "light": darken(muted, 0.4)},
            "markdownEmph": d(WARN),
            "markdownStrong": d(a),
            "markdownHorizontalRule": {"dark": muted, "light": darken(muted, 0.4)},
            "markdownListItem": d(a),
            "markdownListEnumeration": d(a),
            "markdownImage": d(s),
            "markdownImageText": d(s),
            "markdownCodeBlock": {"dark": tx, "light": light_text},
            "syntaxComment": {"dark": muted, "light": darken(muted, 0.4)},
            "syntaxKeyword": d(s),
            "syntaxFunction": d(a),
            "syntaxVariable": d(tx),
            "syntaxString": d(OK),
            "syntaxNumber": d(WARN),
            "syntaxType": d(s),
            "syntaxOperator": d(a),
            "syntaxPunctuation": {"dark": tx, "light": light_text},
        },
    }


def main():
    os.makedirs(OUT_CLAUDE, exist_ok=True)
    os.makedirs(OUT_OPENCODE, exist_ok=True)
    for show in SHOWS:
        slug = show[0]
        with open(os.path.join(OUT_CLAUDE, f"{slug}.json"), "w", encoding="utf-8") as fh:
            json.dump(claude_theme(show), fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        with open(os.path.join(OUT_OPENCODE, f"{slug}.json"), "w", encoding="utf-8") as fh:
            json.dump(opencode_theme(show), fh, indent=2, ensure_ascii=False)
            fh.write("\n")

    # validate: every file parses and has the required shape
    errors = 0
    for sub, check in ((OUT_CLAUDE, "overrides"), (OUT_OPENCODE, "theme")):
        for fname in sorted(os.listdir(sub)):
            if not fname.endswith(".json"):
                continue
            with open(os.path.join(sub, fname), encoding="utf-8") as fh:
                data = json.load(fh)
            if check not in data:
                print("ERROR", fname, "missing", check)
                errors += 1
    if errors:
        print(f"{errors} validation errors")
        raise SystemExit(1)

    n = len(SHOWS)
    print(f"Wrote {n} Claude Code themes -> themes/claude-code/")
    print(f"Wrote {n} OpenCode themes      -> themes/opencode/")


if __name__ == "__main__":
    main()
