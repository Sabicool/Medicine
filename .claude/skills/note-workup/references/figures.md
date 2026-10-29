# Figure house style

Every figure is a standalone TikZ/pgfplots file in `attachments/figures/` that loads the shared style:

```latex
% One-line description of what the figure shows
% Art credit if any: Liver: Servier Medical Art (smart.servier.com), CC BY 4.0 (art/servier-liver.pdf)
\documentclass[11pt, border=2mm]{standalone}
\usepackage{cicm-figure}
\begin{document}
\begin{tikzpicture}
  ...
\end{tikzpicture}
\end{document}
```

`make figures` compiles it to `build/figures/<name>.pdf` (the book uses that) and writes `<name>.svg` beside the source (Obsidian and the website use that). The SVG is drawn 1.2× larger so labels match body text on screen.

## Style (from `cicm-figure.sty`)

| Colour | Use |
|---|---|
| `cicmink` | text, default lines |
| `cicmaccent` (crimson) | the main flow, drug movement, emphasis, "on" states |
| `cicmblue` | metabolism, distribution, the second process |
| `cicmgrey` | losses, "off" states, secondary labels |
| `cicmochre`, `cicmsage` | third and fourth series in graphs |
| `cicmbluetint`, `cicmaccenttint`, `cicmpaper` | panel and band fills |

- Line weights: `thin` 0.4 pt, default 0.8 pt, `thick` 1.2 pt. Arrows are Stealth (default).
- Styles: `box`, `accent box`, `label` (`\small`); graphs `\begin{axis}[cicm, …]`.
- Fonts come from the book (EB Garamond); maths is typeset by LaTeX, so `$k_{12}$` works in labels.
- Width: the text block is 150 mm. Aim for ≤ 15 cm wide; wider figures get scaled down and their labels shrink.
- Dark mode: SVGs get a paper backing on the website and in Obsidian, so draw dark on transparent.

## Patterns that worked

**Organ or object pictures** — vector art from `art/servier-*.pdf` (see `servier.md`):

```latex
\newcommand\organ[2]{\includegraphics[height=#1]{servier-#2.pdf}}
\node at (0,0) {\organ{14mm}{liver}};
```

`TEXINPUTS` searches `attachments/figures//`, so the `art/` subfolder needs no path.

**Arrows that meet an organ's edge** — measure where the outline is rather than guessing:

```sh
python3 -I .claude/skills/note-workup/scripts/outline.py attachments/figures/art/servier-liver.pdf
```

prints the left and right edge at each height as fractions. For a node of width `W` cm and height `H` cm centred at the origin, a fraction `(fx, fy)` sits at `((fx − 0.5)·W, (fy − 0.5)·H)`. Put the in and out arrows at a height where both edges reach out, so they line up. Use `--grid out.png` for an image with a 10% grid over it.

**Label inside an organ** — white `\small` text, centred in the largest flat region (for the liver, the big lobe at about `(-0.85, 0.25)` on a 52 mm liver).

**Comparison grid** (`steady-state-determinants.tex`) — tinted column panels, a formula per cell, and on/off "chips" showing which parameters matter, with a key:

```latex
chip/.style = {rounded corners=1.2mm, inner sep=1.5pt, minimum height=4.8mm, minimum width=9.5mm, font=\footnotesize, thin},
on/.style   = {chip, fill=cicmaccent, draw=cicmaccent, text=white},
off/.style  = {chip, draw=cicmgrey!55, text=cicmgrey!85},
```

**Flow of a dose** (`absorption-determinants.tex`) — a pale band whose width is the fraction remaining, grey branches peeling off below for losses, organs sitting on the band, numbered titles with keyword tags above each stop. Tags, not sentences: the detail belongs in the note.

**Two compartments side by side** (`plasma-tissue-binding.tex`, `two-compartment-model.tex`) — tinted rounded panels or `box` nodes with icons inside, a double arrow between them, the equation underneath.

**Concentration–time curves** (`bioavailability-auc.tex`, `auc-iv-bolus.tex`) — `axis[cicm]` with no ticks, shaded areas (`\closedcycle`, `fill opacity`), labels placed in empty space with a thin leader arrow if needed.

## Pitfalls

- TikZ already defines some style names: `step` is taken (use `stopnum`, `badge`, …).
- Don't name a `\foreach` variable after a TikZ command: `\foreach \x/\fill in …` breaks `\fill`; use `\tint`.
- `(a -| b)` needs both sides to be coordinates or node anchors, not bare numbers: define `\coordinate (mid) at (6,0);` and use `(mid |- k1.south)`.
- `\tikz` badges inside text inflate the line height: wrap them in `\smash{…}`.
- Narrow text boxes hyphenate; use wider boxes or `execute at begin node=\raggedright\hyphenpenalty=10000`.
- Pale organs (stomach, intestine) vanish on pink fills; use `cicmbluetint` or `cicmpaper` behind them.
- Text placed at fixed coordinates under a block of variable height collides; anchor it to the block (`[yshift=-3mm]node.south`).
- After any edit, rebuild and look at the PNG; don't assume.
