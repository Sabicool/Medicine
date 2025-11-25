---
date: 2025-09-28
---
# Common Conditions and Presentations
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[Acute Coronary Syndromes]]
    - [[Acute Pulmonary Oedema]]
    - [[Aortic Dissection]]
    - [[Atrial Fibrillation]]
    - [[Atrial Flutter]]
    - [[AV Nodal Re-entry Tachycardia]]
    - [[AV Re-entry Tachycardia]]
    - [[Essential Hypertension]]
    - [[Heart Failure]]
    - [[Hypercalcaemia]]
    - [[Hyperkalaemia]]
    - [[Hypertension]]
    - [[Hypotension]]
    - [[Infective Endocarditis]]
    - [[Pericarditis]]
    - [[Pulmonary Hypertension]]
    - [[Secondary Hypertension]]
    - [[Sepsis]]
    - [[Stable Angina]]
    - [[Supraventricular Tachycardia]]
    - [[Ventricular Tachycardia]]

- Emergencies: 
    - [[Advanced Life Support]]

- Investigations: 
    - [[ECG Interpretation]]
    - [[Echocardiogram]]

- Presenting Complaints: 
    - [[Arrhythmias]]
    - [[Chest Pain]]
    - [[Collapse, Syncope, Mechanical Falls]]
    - [[Shortness of Breath, Cough and Haemopytsis]]

- Procedures: 
    - [[Angiography]]
    - [[Lung POCUS]]
    - [[Transcutaneous Pacing]]

- Topics: 
    - [[Phases of Depolarisation]]

<!-- SerializedQuery END -->
# Medications
 <!-- QueryToSerialize: list from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc -->
<!-- SerializedQuery: list from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc -->
- [[Antiarrhythmics]]
- [[Anticoagulants]]
- [[Diuretics]]
- [[Drugs in Cardiac Arrest]]
- [[Lipid Lowering Therapy]]
<!-- SerializedQuery END -->
