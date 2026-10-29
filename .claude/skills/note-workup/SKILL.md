---
name: note-workup
description: Work up study notes Sab has just written (e.g. after finishing a Birkett chapter or a CICM syllabus topic) into finished notes for his vault, juniordoctornotes.com and the CICM Primary textbook. Checks the content for errors, rewords and restructures where it reads badly, draws figures in the textbook's TikZ house style (with Servier Medical Art organ illustrations where they help), writes [!card]/[!cloze] flashcards, embeds the notes under the right syllabus dot points, and verifies everything in the book, the website and Anki. Use when he says he's finished a chapter or section, asks for cards or diagrams for a note, asks to tidy or correct notes, or asks for "what we did" on a new topic.
---

# Note work-up

Sab writes notes in Obsidian; the same Markdown becomes three things, and every change has to look right in all of them:

| Output | Built by | Where |
|---|---|---|
| Obsidian | the vault itself | `~/Documents/02 areas/Medicine` (this repo; auto-committed and pushed by obsidian-git) |
| Website | Quartz | `~/Documents/02 areas/A Junior Doctor's Notes` (branch `v4`; `content/` is a symlink to the vault) |
| Textbook PDF and Anki | pandoc + LuaLaTeX, AnkiConnect | `~/Documents/01 projects/CICM Primary Textbook` (`make`, `make figures`, `make anki`) |

The textbook README ("Writing notes") is the reference for card, citation, figure and syllabus conventions. Read it if anything here seems out of date.

## Workflow

Keep a task list. Work through these in order; skip what the request doesn't need.

### 1. Find what's new

- `git log --since=… --name-status` and `git status` in the vault (new notes are often untracked), plus file mtimes in the topic folder.
- Read every new or changed note in full, its sibling notes (for structure and notation), and the syllabus file it belongs under (`05 CICM Study/Primary/<Section>/<Code> <Title>.md`).
- If a note is in the wrong folder (e.g. a pharmacokinetics note outside `Pharmacokinetics/`), say so; move it only when asked. Wikilinks resolve by name, so a move breaks nothing.
- Run the coverage check for the subsection to see where things stand before starting, and again at the end (step 8):
  ```sh
  python3 -I .claude/skills/note-workup/scripts/coverage.py B1          # one subsection
  python3 -I .claude/skills/note-workup/scripts/coverage.py B --gaps    # a section's gaps
  ```
  Each dot point (and each pharmacopeia drug, by level) shows words written, figures and cards (synced/total): ✓ all three, · written but missing figures or cards, ✗ nothing written, ↓ content is in its sub-points. `--markdown` prints a table. Use it when he asks what's left, what to read next, or which dot points have no cards.

### 2. Check the content

- Work every formula through. Derivations should follow; check approximations go the right way (e.g. high extraction: $CL\approx Q_H$, $f_H\approx Q_H/(f_u\cdot CL_{\text{int}})$).
- Look for statements that conflate two things. For example, the Bioavailability note once said "hepatic blood flow does not affect bioavailability" for high-extraction drugs, when it's the *oral steady-state concentration* that's unaffected; $F$ changes.
- Wrong anatomy or terms (e.g. gut wall metabolism is in the *epithelium*, not endothelium).
- **Never invent clinical content**: no doses, statistics, trial results or examples he didn't give, beyond standard textbook facts that follow from what's written. Arithmetic examples that illustrate his own formulas are fine.
- List every correction in the final report, with the reason, so he can check it.

### 3. Reword and restructure

Load the `sab-voice` skill first; these notes are his and publish under his name.

- Keep his register: terse bullets with connectors (*so*, *hence*, *since*), first-order reasoning inside the sentence, Australian spelling. Don't turn bullets into prose.
- Fix typos and wording only when he's asked for editing (this skill counts). Keep his structure where it works.
- Match sibling notes: `*Main source: …* [@citekey]` line, a `# Definitions` section first when the note opens with definitions, `# …` / `## …` sections in a logical order (definitions → mechanism/derivation → determinants → clinical consequences).
- Bold lead-ins on enumerable lists (e.g. **Dissolution:** …).
- Maths: `$$…$$` display blocks; use `\begin{aligned}` not `align` (matches the rest of the vault). `\dfrac` inside inline maths in cards.
- Don't touch `%% anki: … %%` lines or block IDs.

### 4. Figures

Read `references/figures.md` (house style, patterns, pitfalls) before drawing, and `references/servier.md` when an organ, drug or tissue picture would help.

- One figure per idea that's easier seen than read: a mechanism (flow through organs), a comparison grid (which parameters matter where), a curve (concentration–time, AUC).
- Source in `attachments/figures/<name>.tex`; notes embed the generated `![[<name>.svg|Caption]]` on its own line.
- Caption every figure. Credit adapted art in the caption: `… Liver adapted from Servier Medical Art, CC BY 4.0`.
- Give a figure a `^fig-<name>` block ID at the end of the embed line when anything refers to it; refer with `[[#^fig-<name>|Figure]]` or `[[Note#^fig-<name>|Figure]]` (book and website turn these into "Figure B1.3" / "Figure 3").
- Build with `make -C "<textbook>" figures`, render the PDF to PNG (`pdftocairo -png -r 110 -singlefile build/figures/<name>.pdf …`) and **look at it**. Iterate until nothing overlaps, labels are legible at book size and it reads at a glance. Expect 2–4 rounds.
- Prefer a diagram over a wall of text: if a figure needs paragraphs, put the detail in the note and keep keywords (tags) in the figure.
- **The textbook comes first.** Size and lay out figures for the 150 mm A4 page, not for phones; never make a figure narrower or sparser to suit small screens (the website has tap-to-enlarge for that).

### 5. Flashcards

Card syntax (one blank line before and after each callout; no Anki ID — the sync adds it):

```markdown
> [!card]- Question ending in a question mark?
> Answer. Maths, lists and images allowed.

> [!cloze]
> Sentence with the ==key term== blanked.
```

- Put each card straight after the content it tests, not in a block at the end.
- One idea per card; answers short enough to recall in one go. Derivation cards ("Derive …") give the key steps, not the whole working.
- Cloze for single facts, terms or the one variable that matters; cards for "why", "how", "what determines".
- A figure can go on the back of a card (`> ![[name.svg|Caption]]` after the answer). The book and website show that copy unnumbered.
- Cover everything new he wrote, including older sections that never had cards if he asks.

### 6. Link into the syllabus

- Embed each note under the dot point it answers: `![[Note]]` on its own line under `# B1.ii …` in the syllabus file. Several notes can sit under one dot point, in reading order.
- If a note fits two dot points, pick one and mention the other in the report.

### 7. Verify everything

- **Book:** `make -C "<textbook>" book` (the whole book; `ONLY=B1` overwrites the PDF with one chapter, so finish with a full build). Then check with `pdftotext`: figure references resolved (`Figure B1.n`, no `??`), no literal `- ` bullets, captions present. Render a page or two with new figures and look.
- **Website:** `npx quartz build -o <scratchpad>/public` from the website repo, then grep the page HTML for `<figcaption>` and figure links; view a page in the browser pane via the `deck-preview` config in `.claude/launch.json` (point its directory at the scratch build).
- **Anki:** `make -C "<textbook>" anki-dry` and show him what it would add/update; run `make anki` (Anki open with AnkiConnect) when he asks for cards in Anki. Check a card with an image via AnkiConnect `notesInfo`.
- Obsidian can't be checked from here unless he grants screen access; say so.

### 8. Report

Rerun the coverage check for the subsection and include its lines for the dot points touched. Say what changed in each note, list every correction with why, list new figures and cards, say where the notes are embedded, and what was verified (and what wasn't). The vault commits itself; **commit the textbook or website repos only when asked, as Sab only — no co-author lines.**

## Pitfalls seen before

- The textbook build used to drop the blank line before a list after a callout (fixed in `build_book.py`); if bullets print as `- text`, check `build/md/<code>.md`.
- `make <target>` from outside Nix needs the target in the Makefile's `TARGETS` list.
- Quartz: a caption ending in a number used to be eaten as an image width (fixed in `ofm.ts`). Figures are numbered per page; a page that embeds other notes renumbers after embedding.
- Obsidian caches images: after regenerating an SVG, reopen the note to see it.
- Obsidian's editing view lays image embeds out as a flex row; the `cicm-notes.css` snippet stacks the caption under it.
