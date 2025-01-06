---
title: Home
date: 2025-01-03
---
# About this Website
This is the note database of a junior doctor in Australia. The information contained in these notes is for educational purposes only and should not be construed as medical advice. While I strive for accuracy, I make no guarantees regarding the completeness or reliability of the content provided. Additionally, I do not claim copyright for any images included herein unless explicitly stated. If you wish to request a correction, removal, or alteration of any content, please feel free to contact me or submit an issue via the associated [github repository](https://github.com/Sabicool/Medicine). The colour theme for this website is based off [catppuccin](https://github.com/catppuccin/catppuccin).
# Quick Reference
Consider taking a look through my [Intern Reference file](00%20Reference/Junior%20Doctor/Intern%20Reference.md) if you are an intern yourself, otherwise here is a list of notes in my rotations folder. Click on whatever rotation you might be on right now:
## Useful Notes
Mainly for the admin side of things as a junior doctor
- [Intern Reference](00%20Reference/Junior%20Doctor/Intern%20Reference.md)
- [iSBAR Handover](00%20Reference/Clinical/iSBAR%20Handover.md)
- [Pronouncing Death](00%20Reference/Clinical/Pronouncing%20Death.md)
- [Writing Discharge Summaries](00%20Reference/Administrative/Writing%20Discharge%20Summaries.md)
## Rotations
If you'd rather just find notes on medicine relevant to the particular rotation you are on look below:
<!-- QueryToSerialize: LIST FROM "02 Rotations" -->
<!-- SerializedQuery: LIST FROM "02 Rotations" -->
- [[Emergency Medicine]]
- [[Intensive Care Unit]]
- [[Neurology]]
- [[Paediatrics]]
- [[Nephrology]]
- [[Respiratory]]
- [[Common Ward Calls]]
- [[Cardiology]]
<!-- SerializedQuery END -->

Otherwise have a look through the "01 Disciplines" on the left panel.
# How I Studied in Medical School
This is a non-exhaustive guide to studying in medical school. I do plan on making a more complete guide one day but until then here's some words of wisdom.

I rarely made comprehensive notes. I mainly studied by doing pre-made flashcard decks, my own flashcards and a bunch of practice questions. Closer to exams for my OSCE exams in particular, I would try to learn by approaches to presenting complaints.

> [!TIP] 
> I used to take notes using notion during medical school. I found it to be fairly reliable and meant that I did not need to bring a laptop to placement to take notes. I could simply just login to notion and take notes or even review my notes from any computer I had access to on placement. You can find my notes here [https://mango-cellar-b90.notion.site/](https://mango-cellar-b90.notion.site/ "my medicine notes on notion"). Another alternative is Remnote, which provides a more unified experience with flashcard support but it can be a bit buggy at times. Personally I have been moving towards trying to use more FOSS (hence this website).

## Useful Resources
- Your university resources (my university resources have been kept private)
- State based/hospital based guidelines (e.g. RCH, ACI, PCH, KEMH guidelines) 
- National guidelines (e.g. RACGP Red Book, RANZCOG guidelines)
- Other national resources (e.g. eTG, AMH Online)
- Other useful Australian resources: LITFL
- Other useful resources: Teach Me Series (e.g. Teach me surgery, Teach me Obgyn), Amboss
- I mainly used emedici as my question bank during medical school although passmedicine and armadex are probably better
# How I made these notes
These notes are for the most part formatted in markdown and hopefully made to be quite presentable and accurate.

I use a mixture of Emacs and Obsidian to take these notes[^1]. Emacs has been wonderful to use especially with [obsidian.el](https://github.com/licht1stein/obsidian.el). After a year of using Vanilla Emacs, I got tired of configuring everything myself and switched to [Doom Emacs](https://github.com/doomemacs/doomemacs) and have been quite happy with it.

Obsidian has been a great to use on my other devices (namely, my iPad and my phone synced to my computer using [syncthing](https://syncthing.net/)). I use a few plugins to make my use of obsidian more palatable including but not limited to:
- Core plugins:
    - Backlinks
    - Bookmarks
    - Command palette
    - File recovery
    - Files
- Community plugins:
    - Advanced tables
    - Code editor shortcuts
    - Dataview
    - [Dataview serializer](https://github.com/dsebastien/obsidian-dataview-serializer)
    - Excalidraw
    - Footnote shortcut
    - Git
    - Iconize 
    - Obsidian_to_Anki
    - Omnisearch
    - Recent Files
    - Style Settings
    - Text Extractor
    - Vimrc Support

i do want to add some improvements to the notes:

- [x] Make a functional website; something like quartz might work well
- [x] Add a date last updated to all the notes
- [x] Implement way to add cards from Obsidian to Anki[^2]
    - Anything surrounded by curly braces is likely a card that has been incorporated into the Malleus anki deck *(I can't demonstrate here, otherwise it'll create a card)*
# Footnotes

[^1]: Both are great applications for note taking but unfortunately there might be some barrier to using either application because of the initial learning to use either program. If that is the case for you, I'd recommend something like notion or remnote to take notes on
[^2]: I should generally be adding these cards to the Malleus Clinical Medicine Anki project
