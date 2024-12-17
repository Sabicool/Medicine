<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[Pulmonary Hypertension]]
    - [[Asthma]]
    - [[Acute Pulmonary Oedema]]
    - [[Pneumothorax]]
    - [[Pulmonary Embolism]]
    - [[COPD]]
    - [[Pneumonia]]

- Emergencies: 
    - [[Acute Respiratory Failure]]

- Presenting Complaints: 
    - [[Shortness of Breath]]

<!-- SerializedQuery END -->
