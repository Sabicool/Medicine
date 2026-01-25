---
date: 2026-01-25
aliases:
  - ICU
---
# Common Conditions and Presentations
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[Acute Pulmonary Oedema]]
    - [[Adrenal Crisis]]
    - [[Adrenal Insufficiency]]
    - [[COPD Exacerbation]]
    - [[Hypercalcaemia]]
    - [[Hyperkalaemia]]
    - [[Necrotising Skin Infections]]
    - [[Sepsis]]
    - [[Ventricular Tachycardia]]

- Emergencies: 
    - [[Acute Airway Failure]]
    - [[Acute Respiratory Failure]]
    - [[Advanced Life Support]]
    - [[Shock]]
    - [[Unconsciousness]]

- Investigations: 
    - [[Blood Gas Interpretation]]
    - [[ECG Interpretation]]
    - [[Neuroimaging]]

- Presenting Complaints: 
    - [[Altered Mental Status]]

- Procedures: 
    - [[General Anaesthesia]]
    - [[Lung POCUS]]

- Topics: 
    - [[Respiratory Physiology]]

<!-- SerializedQuery END -->
# Medications to Know
<!-- QueryToSerialize: list rows.file.link from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
- Cardiology: 
    - [[Antiarrhythmics]]
    - [[Drugs in Cardiac Arrest]]
    - [[Inotropes]]

<!-- SerializedQuery END -->
