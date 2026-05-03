#!/usr/bin/env python3
"""Post-process pdf2svg output for adaptive light/dark display.

Replaces hardcoded rgb(0%,0%,0%) stroke/fill with currentColor and
injects a <style> block so the SVG respects prefers-color-scheme.
Colors: Catppuccin Latte text (#4c4f69) for light, Mocha text (#cdd6f4) for dark.
"""
import re
import sys
from pathlib import Path

STYLE = (
    "<style>"
    "svg{color:#4c4f69}"
    "@media(prefers-color-scheme:dark){svg{color:#cdd6f4}}"
    "</style>"
)


def fix(path: str) -> None:
    p = Path(path)
    t = p.read_text()
    t = t.replace('stroke="rgb(0%, 0%, 0%)"', 'stroke="currentColor"')
    t = t.replace('fill="rgb(0%, 0%, 0%)"', 'fill="currentColor"')
    t = re.sub(r"(<svg\b[^>]*>)", r"\1" + STYLE, t, count=1)
    p.write_text(t)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.svg>", file=sys.stderr)
        sys.exit(1)
    fix(sys.argv[1])
