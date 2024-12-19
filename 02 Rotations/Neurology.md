<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[01 Disciplines/Respiratory/Conditions/Asthma.md|Asthma]]
    - [[01 Disciplines/Respiratory/Conditions/Pulmonary Embolism.md|Pulmonary Embolism]]
    - [[01 Disciplines/Respiratory/Conditions/COPD.md|COPD]]
    - [[01 Disciplines/Respiratory/Conditions/Pneumonia.md|Pneumonia]]
    - [[01 Disciplines/Respiratory/Conditions/Pneumothorax.md|Pneumothorax]]
    - [[01 Disciplines/Respiratory/Conditions/Acute Pulmonary Oedema.md|Acute Pulmonary Oedema]]

- Topics: 
    - [[01 Disciplines/Clinical/Topics/Breaking Bad News.md|Breaking Bad News]]
    - [[01 Disciplines/Clinical/Topics/Palliated Patients.md|Palliated Patients]]

<!-- SerializedQuery END -->
