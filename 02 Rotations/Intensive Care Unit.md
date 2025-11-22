---
date: 2025-10-25
---
# Common Conditions and Presentations
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) sort file.name asc group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[01 Disciplines/Respiratory/Conditions/Acute Pulmonary Oedema.md|Acute Pulmonary Oedema]]
    - [[01 Disciplines/Endocrinology/Conditions/Hypercalcaemia.md|Hypercalcaemia]]
    - [[01 Disciplines/Clinical/Conditions/Hyperkalaemia.md|Hyperkalaemia]]
    - [[01 Disciplines/Infectious Disease/Conditions/Sepsis.md|Sepsis]]
    - [[01 Disciplines/Cardiology/Conditions/Ventricular Tachycardia.md|Ventricular Tachycardia]]

- Emergencies: 
    - [[01 Disciplines/Clinical/Emergencies/Acute Airway Failure.md|Acute Airway Failure]]
    - [[01 Disciplines/Respiratory/Emergencies/Acute Respiratory Failure.md|Acute Respiratory Failure]]
    - [[01 Disciplines/Clinical/Emergencies/Advanced Life Support.md|Advanced Life Support]]
    - [[01 Disciplines/Clinical/Emergencies/Shock.md|Shock]]

- Investigations: 
    - [[01 Disciplines/Respiratory/Investigations/Blood Gas Interpretation.md|Blood Gas Interpretation]]
    - [[01 Disciplines/Cardiology/Investigations/ECG Interpretation.md|ECG Interpretation]]

- Presenting Complaints: 
    - [[01 Disciplines/Neurology/Presenting Complaints/Altered Mental Status.md|Altered Mental Status]]

- Procedures: 
    - [[01 Disciplines/Clinical/Procedures/Lung POCUS.md|Lung POCUS]]

<!-- SerializedQuery END -->

# Medications to Know
<!-- QueryToSerialize: list rows.file.link from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
- Cardiology: 
    - [[03 Medications/Cardiology/Antiarrhythmics.md|Antiarrhythmics]]
    - [[03 Medications/Cardiology/Drugs in Cardiac Arrest.md|Drugs in Cardiac Arrest]]

<!-- SerializedQuery END -->
