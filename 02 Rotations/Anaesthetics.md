---
date: 2026-01-24
---
# Common Conditions and Presentations
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
- Investigations: 
    - [[01 Disciplines/Respiratory/Investigations/Blood Gas Interpretation.md|Blood Gas Interpretation]]

- Procedures: 
    - [[01 Disciplines/Anaesthetics/Procedures/General Anaesthesia.md|General Anaesthesia]]
    - [[01 Disciplines/Anaesthetics/Procedures/Intubation.md|Intubation]]
    - [[01 Disciplines/Anaesthetics/Procedures/Post-Induction Checklist.md|Post-Induction Checklist]]

- Topics: 
    - [[01 Disciplines/Anaesthetics/Topics/Mechanical Ventilation.md|Mechanical Ventilation]]
    - [[01 Disciplines/Respiratory/Topics/Respiratory Physiology.md|Respiratory Physiology]]
    - [[01 Disciplines/Nephrology/Topics/Sodium and Potassium Homeostasis.md|Sodium and Potassium Homeostasis]]

<!-- SerializedQuery END -->
# Medications
 <!-- QueryToSerialize: list from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc -->
<!-- SerializedQuery: list from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc -->
- [[03 Medications/Anaesthetics/Acetylcholinesterase Inhibitor.md|Acetylcholinesterase Inhibitor]]
<!-- SerializedQuery END -->
# Other
- [[Anaesthetics Training]]