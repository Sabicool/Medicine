---
date: 2025-01-04
---
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[Pulmonary Hypertension]]
    - [[Acute Pulmonary Oedema]]
    - [[Asthma]]
    - [[COPD]]
    - [[Pneumonia]]
    - [[Pneumothorax]]
    - [[Pulmonary Embolism]]
    - [[Untitled 1]]
    - [[Untitled]]

- Emergencies: 
    - [[Acute Respiratory Failure]]

- Presenting Complaints: 
    - [[Hiccups]]
    - [[Shortness of Breath, Cough and Haemopytsis]]

<!-- SerializedQuery END -->
