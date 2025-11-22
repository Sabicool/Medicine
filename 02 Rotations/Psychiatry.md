---
date: 2025-04-26
---
# Common Conditions and Presentations
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[01 Disciplines/Psychiatry/Conditions/Acute Stress Disorder.md|Acute Stress Disorder]]
    - [[01 Disciplines/Psychiatry/Conditions/Major Depressive Disorder.md|Major Depressive Disorder]]
    - [[01 Disciplines/Psychiatry/Conditions/Persistent Depressive Disorder.md|Persistent Depressive Disorder]]

- Presenting Complaints: 
    - [[01 Disciplines/Psychiatry/Presenting Complaints/Anxiety.md|Anxiety]]

- Topics: 
    - [[01 Disciplines/Psychiatry/Topics/Mental Health Assessment.md|Mental Health Assessment]]
    - [[01 Disciplines/Psychiatry/Topics/Mental State Examination.md|Mental State Examination]]

<!-- SerializedQuery END -->

# Medications to Know
<!-- QueryToSerialize: list from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc -->
<!-- SerializedQuery: list from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc -->
- [[03 Medications/Psychiatry/Antidepressants.md|Antidepressants]]
<!-- SerializedQuery END -->
