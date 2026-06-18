---
title: Home
description: Clinical notes maintained by a junior doctor in Australia, with a focus on acute and critical care medicine — emergency, intensive care and anaesthetics.
date: 2026-06-18
---
# Rotations and Disciplines
<!-- QueryToSerialize: LIST FROM "02 Rotations" sort file.name asc -->
<!-- SerializedQuery: LIST FROM "02 Rotations" sort file.name asc -->
- [[Anaesthetics]]
- [[Cardiology]]
- [[Common Ward Calls]]
- [[Emergency Medicine]]
- [[Gastroenterology]]
- [[Intensive Care Unit]]
- [[Nephrology]]
- [[Neurology]]
- [[Paediatrics]]
- [[Psychiatry]]
- [[Respiratory]]
<!-- SerializedQuery END -->
# About these notes
A working clinical reference maintained by a junior doctor in Australia, with a focus on **acute and critical care medicine** — emergency, intensive care and anaesthetics. The notes are written to be useful at the bedside: structured approaches to the unwell patient, the common after-hours calls, and the investigations and procedures that actually come up on the floor. They are formatted in markdown and kept as accurate and presentable as I can manage.

> [!note] Disclaimer
> This information is for educational purposes only and should not be construed as medical advice. While I strive for accuracy, I make no guarantees regarding the completeness or reliability of the content. I do not claim copyright for any images included unless explicitly stated. To request a correction, removal or alteration of any content, please contact me or submit an issue via the associated [GitHub repository](https://github.com/Sabicool/Medicine).

# Acute & Critical Care
The notes most relevant to the deteriorating and critically unwell patient:
- **Resuscitation & emergencies** — [[Advanced Life Support]], [[Shock]], [[Sepsis]], and structured approaches to [[Acute Airway Failure]] and [[Acute Respiratory Failure]]
- **Airway & ventilation** — [[Intubation]], the [[Post-Induction Checklist]], and a full [[Mechanical Ventilation]] series covering modes, settings, waveform interpretation, troubleshooting and weaning
- **Bedside investigations** — [[Blood Gas Interpretation|ABG interpretation]], [[ECG Interpretation]], [[Echocardiogram]] and [[Lung POCUS]]
- **By rotation** — [[Intensive Care Unit|ICU]], [[Emergency Medicine]], [[Anaesthetics]] and [[Common Ward Calls]]

# Quick Reference
Consider taking a look through my [[Intern Reference]] if you are an intern yourself, otherwise here is a list of notes in my rotations folder. Click on whatever rotation you might be on right now:
## Useful Notes
Mainly for the admin side of things as a junior doctor
- [[Intern Reference]]
- [[iSBAR Handover]]
- [[Pronouncing Death]]
- [[Writing Discharge Summaries]]
- [[Advanced Life Support]]
- [[Blood Gas Interpretation|ABG Interpretation]]

Some other administrative notes:
<!-- QueryToSerialize: List from "00 Reference/Administrative" sort file.name asc -->
<!-- SerializedQuery: List from "00 Reference/Administrative" sort file.name asc -->
- [[Administrative Notes on Radiology]]
- [[Consults and Referrals]]
- [[End-of-life orders]]
- [[Finding Notes and Documents]]
- [[Home Screen]]
- [[Ordering Investigations]]
- [[Patient Lists]]
- [[Useful Numbers to Save on Your Phone]]
- [[Viewing Investigations]]
- [[Writing Discharge Summaries]]
<!-- SerializedQuery END -->
## Rotations
If you'd rather just find notes on medicine relevant to the particular rotation you are on look below:
<!-- QueryToSerialize: LIST FROM "02 Rotations" sort file.name asc -->
<!-- SerializedQuery: LIST FROM "02 Rotations" sort file.name asc -->
- [[Anaesthetics]]
- [[Cardiology]]
- [[Common Ward Calls]]
- [[Emergency Medicine]]
- [[Gastroenterology]]
- [[Intensive Care Unit]]
- [[Nephrology]]
- [[Neurology]]
- [[Paediatrics]]
- [[Psychiatry]]
- [[Respiratory]]
<!-- SerializedQuery END -->

Otherwise have a look through the "01 Disciplines" on the left panel (on desktop).
## Medications
Non-exhaustive list of medications that are commonly prescribed. Consider navigating for more medications using the file browser on the left (on desktop).
![[03 Medications/index#^handy-medications|index]]
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
- Qbanks: I used eMedici but there also exists passmedicine and armadex
# How I made these notes
These notes are for the most part formatted in markdown and hopefully made to be quite presentable and accurate. The colour theme for this website is based off [catppuccin](https://github.com/catppuccin/catppuccin).

I use a mixture of Emacs and Obsidian to take these notes[^1][^3]. Emacs has been wonderful to use especially with [obsidian.el](https://github.com/licht1stein/obsidian.el). After a year of using Vanilla Emacs, I got tired of configuring everything myself and switched to [Doom Emacs](https://github.com/doomemacs/doomemacs) and have been quite happy with it.

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
    - [Dataview serializer](https://github.com/dsebastien/obsidian-dataview-serializer)[^4]
    - Excalidraw
    - Footnote shortcut
    - Git
    - Iconize 
    - Obsidian_to_Anki
    - Omnisearch
    - Recent Files
    - Style Settings
    - Text Extractor
    - Vimrc Support[^3]

In particular for the discipline notes I use this kind of format with the dataview serializer plugin to display lists of the relevant notes.

```
list rows.file.link 
    from "01 Disciplines" 
    where  
        contains(Rotations, "[" + this.file.name + "]("
            + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20") 
            + ")") OR contains(Rotations, this.file.link) or 
        contains(file.path,this.file.name) 
    sort file.name asc 
    group by reverse(split(file.folder, "/"))[0] 
```


[^1]: Both are great applications for note taking but unfortunately there might be some barrier to using either application because of the initial learning to use either program. If that is the case for you, I'd recommend something like notion or remnote to take notes on
[^2]: I should generally be adding these cards to the Malleus Clinical Medicine Anki project
[^3]: Man vim support in obsidian sucks. Just use emacs with evil mode and obsidian.el.
[^4]: This is how I make autogenerated lists on a lot of different pages (e.g. this page's rotations list)
