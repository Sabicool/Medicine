"""Syllabus coverage: for each CICM dot point, whether it has notes, figures and cards.

    python3 coverage.py              every subsection
    python3 coverage.py B1 C         only these subsections or whole sections
    python3 coverage.py B --gaps     only dot points missing notes, figures or cards
    python3 coverage.py B1 --markdown   a Markdown table, to paste into a note

Reads the vault the way the textbook build does (its tools/vault.py): a dot
point's content is everything under its heading, with embedded notes expanded.
Columns: notes embedded, figures, cards (synced to Anki / total), and words
written. A parent dot point whose content sits in its sub-points shows "↓".
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TEXTBOOK = Path("~/Documents/01 projects/CICM Primary Textbook").expanduser()
sys.path.insert(0, str(TEXTBOOK / "tools"))
from vault import COMMENT, EMBED_LINE, HEADING, IMAGE_EMBED, Vault, cards_in, syllabus  # noqa: E402

CODE = re.compile(r"^([A-Q][0-9P]+(?:\.[0-9a-z]+)+)\s+(.*)$")  # B1.i, B1.viii.a
LEVEL = re.compile(r"^Level\s+(\d)$")                                # pharmacopeia: # Level 2
WORD = re.compile(r"[A-Za-z]{2,}")
PLACEHOLDER = re.compile(r"^\s*_Nil_\s*$")


def dot_points(lines):
    """[(code, title, level, own lines)] for each item, in order.

    Syllabus files: each dot-point heading (# B1.i …). Pharmacopeia files have
    no codes: each drug-class or drug heading under "# Level n" is an item,
    labelled Ln. The syllabus's own [!note] callouts and _Nil_ placeholders
    aren't content, so they're dropped.
    """
    points, tier, in_note = [], None, False
    for line in lines:
        h = HEADING.match(line.text)
        if h and (m := CODE.match(h[2])):
            points.append([m[1], m[2], len(h[1]), []])
        elif h and (m := LEVEL.match(h[2])):
            tier = f"L{m[1]}"
            points.append(None)  # ends the item before it
        elif h and tier:
            points.append([tier, h[2], len(h[1]) - 1, []])
        elif points and points[-1] is not None:
            in_note = in_note and line.text.lstrip().startswith(">") or line.text.lstrip().startswith("> [!note]")
            if not in_note and not PLACEHOLDER.match(line.text):
                points[-1][3].append(line)
    return [p for p in points if p is not None]


def measure(vault, path, own):
    expanded = vault.expand(path, own)
    notes = [m["target"] for l in own if (m := EMBED_LINE.match(l.text)) and not IMAGE_EMBED.search(l.text)]
    cards = cards_in(expanded)
    text = COMMENT.sub("", "\n".join(l.text for l in expanded))
    return {
        "notes": len(notes),
        "figures": len({m[1] for m in IMAGE_EMBED.finditer(text)}),
        "cards": len(cards),
        "synced": sum(1 for c in cards if c.meta.get("anki")),
        "words": len(WORD.findall(text)),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("only", nargs="*", help="subsection codes (B1) or sections (B)")
    ap.add_argument("--gaps", action="store_true", help="only dot points missing notes, figures or cards")
    ap.add_argument("--markdown", action="store_true", help="print a Markdown table")
    args = ap.parse_args()

    vault = Vault()
    subs = [s for s in syllabus(vault)
            if not args.only or s.code in args.only or s.section in args.only]
    if not subs:
        raise SystemExit("No matching syllabus files.")

    rows = []
    totals = {"points": 0, "written": 0, "figures": 0, "cards": 0, "synced": 0}
    for sub in subs:
        _, body = vault.note(sub.path)
        points = dot_points(body)
        stats = [measure(vault, sub.path, own) for _, _, _, own in points]
        for i, ((code, title, level, _), s) in enumerate(zip(points, stats)):
            # A parent with nothing of its own but content in its sub-points
            children = []
            for (_, _, lv, _), t in zip(points[i + 1:], stats[i + 1:]):
                if lv <= level:
                    break
                children.append(t)
            deferred = s["words"] == 0 and any(c["words"] for c in children)
            written = s["words"] > 0
            totals["points"] += 1
            totals["written"] += written or deferred
            for k in ("figures", "cards", "synced"):
                totals[k] += s[k]
            missing = [] if deferred else [k for k, ok in (("notes", written), ("figures", s["figures"]),
                                                           ("cards", s["cards"])) if not ok]
            if args.gaps and not missing:
                continue
            rows.append((sub.code, code, "  " * (level - 1) + title, s, deferred, missing))

    if args.markdown:
        print("| Dot point | Notes | Figures | Cards | Missing |")
        print("| --- | --- | --- | --- | --- |")
        for _, code, title, s, deferred, missing in rows:
            notes = "↓" if deferred else (f"{s['words']} words" if s["words"] else "—")
            cards = f"{s['synced']}/{s['cards']}" if s["cards"] else "—"
            print(f"| **{code}** {title.strip()} | {notes} | {s['figures'] or '—'} | {cards} | {', '.join(missing)} |")
    else:
        current = None
        for sub_code, code, title, s, deferred, missing in rows:
            if sub_code != current:
                current = sub_code
                print(f"\n{sub_code}")
            mark = "↓" if deferred else ("✓" if not missing else ("✗" if "notes" in missing else "·"))
            cards = f"{s['synced']}/{s['cards']}" if s["cards"] else "-"
            fig = s["figures"] or "-"
            words = s["words"] or "-"
            short = title if len(title) <= 70 else title[:69] + "…"
            print(f"  {mark} {code:<12} words {words!s:>5}  figs {fig!s:>2}  cards {cards:>5}  {short}")
        print("\n✓ notes, figures and cards   · notes but missing figures or cards   ✗ nothing written   ↓ see sub-points")

    print(f"\n{totals['written']}/{totals['points']} syllabus items written, "
          f"{totals['figures']} figures, {totals['cards']} cards ({totals['synced']} in Anki)")
    for w in vault.warnings:
        print(f"warning: {w}", file=sys.stderr)


if __name__ == "__main__":
    main()
