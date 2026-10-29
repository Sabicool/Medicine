# Servier Medical Art

[smart.servier.com](https://smart.servier.com) — medical illustrations under **CC BY 4.0** (same licence as the notes and book), so they can be adapted with credit. The PNGs on the site are only ~500 px; the PowerPoint kits hold the same art as **vector** shapes, which stay sharp in print. Use the kits.

## Already extracted

In `attachments/figures/art/` (vector PDFs, transparent background):

| File | From kit, slide, group |
|---|---|
| `servier-liver.pdf` | Digestive system, 17, "Group 23" (flat liver) |
| `servier-small-intestine.pdf` | Digestive system, 24, "Group 3" |
| `servier-stomach.pdf` | Digestive system, 13, "Group 3" (unlabelled) |
| `servier-villus.pdf` | Digestive system, 26, "Group 3" |
| `servier-kidney.pdf` | Urinary system, 4, "Group 3" |
| `servier-nephron.pdf` | Urinary system, 8, "Group 90" |
| `servier-heart.pdf` | Heart physiology, 3, "Group 3" |
| `servier-brain.pdf` | Nervous system, 3, "Group 3" |
| `servier-artery.pdf` | Arteries physiology, 14, "Group 1179" |
| `servier-muscle.pdf` | Muscles, 4, "Group 3" |
| `servier-fat.pdf` | Lipids, 10, "Group 4846" |
| `servier-capsule.pdf` | Drugs, 6, "Group 15" |

The vault's `.gitignore` ignores `*.pdf` except `attachments/figures/art/*.pdf`; keep new art there so it's committed and the book builds from a clone.

## Getting new art

1. **Find the kit.** Search the site and collect kit links:
   ```sh
   curl -sL "https://smart.servier.com/?s=kidney" | grep -oE 'https://smart.servier.com/wp-content/uploads/[^"]+\.pptx' | sort -u
   ```
   Kits are `SMART-<Topic>.pptx` (e.g. Digestive-system, Urinary-system, Heart-physiology, Arteries-physiology, Nervous-system, Muscles, Lipids, Drugs, Respiratory-system).
2. **Download it into the scratchpad** (not the vault) and export it to PDF through Keynote for a contact sheet:
   ```sh
   osascript -e 'tell application "Keynote"
     set d to open POSIX file "<kit>.pptx"
     export d to POSIX file "<kit>.pdf" as PDF
     close d saving no
   end tell'
   pdftocairo -png -r 40 -f <n> -l <n> -singlefile <kit>.pdf <out>   # one slide
   montage -label '%t' <pngs> -tile 4x -geometry +4+4 sheet.png        # several
   ```
   Slide titles: `unzip` the pptx and grep `<a:t>` in `ppt/slides/slide<n>.xml`.
3. **List the shape groups** on the chosen slide (each illustration is usually one group; labels are separate text boxes):
   ```sh
   python3 -I .claude/skills/note-workup/scripts/extract_servier.py <kit>.pptx <slide> --list
   ```
4. **Extract one group** as a transparent vector PDF, sized to the art:
   ```sh
   python3 -I .claude/skills/note-workup/scripts/extract_servier.py <kit>.pptx <slide> "Group 23" attachments/figures/art/servier-<name>.pdf
   ```
   It keeps only that group, hides the slide master's decoration and background, and exports through Keynote. Check the result: `pdftocairo -png -transp -r 100 -singlefile …` and look at it.
5. Add the new file to the table above.

`pic` entries in `--list` are embedded bitmaps, not vector; avoid them.

## Credit

In the figure caption (visible on all three outputs): `<Caption>. <Liver> adapted from Servier Medical Art, CC BY 4.0`. Use "adapted from", since the art is cut out and annotated. The `.tex` header also names the source, and the textbook README credits Servier under third-party material.
