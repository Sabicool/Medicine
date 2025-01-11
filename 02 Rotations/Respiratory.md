---
date: 2025-01-09
---
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[Acute Pulmonary Oedema]]
    - [[Asthma]]
    - [[COPD]]
    - [[Pneumonia]]
    - [[Pneumothorax]]
    - [[Pulmonary Embolism]]
    - [[Pulmonary Hypertension]]

- Emergencies: 
    - [[Acute Respiratory Failure]]

- Investigations: 
    - [[Blood Gas Interpretation]]

- Presenting Complaints: 
    - [[Hiccups]]
    - [[Shortness of Breath, Cough and Haemopytsis]]

<!-- SerializedQuery END -->
