---
date: 2026-03-01
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
    - [[Hyponatraemia]]
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
    - [[Sodium and Potassium Homeostasis]]

<!-- SerializedQuery END -->
# Medications to Know
<!-- QueryToSerialize: list rows.file.link from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "03 Medications" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
- Cardiology: 
    - [[Antiarrhythmics]]
    - [[Drugs in Cardiac Arrest]]
    - [[Inotropes]]

<!-- SerializedQuery END -->
# Principles
- DVT prophylaxis
	- All ICU patients should receive DVT prophylaxis unless there is a contraindication (e.g., hemorrhage, platelet count <30-50, planned lumbar puncture)
	- GFR >30 ml/min: Generally enoxaparin 40 mg daily
		- Weight <50 kg: use enoxaparin 30 mg daily
		- Weight >120 kg: consider ~0.25 mg/kg q12hr
	- GFR <30 ml/min: Use heparin 5,000 IU TID
- GI prophylaxis
	- As a simple rule of thumb, use GI prophylaxis only for intubated patients.
	- Preferred agent is pantoprazole 40 mg PO/IV daily.
- Medications to avoid in ICU
	- NSAIDs (renal failure, bleeding).
	- ACEi/ARBs (avoid unless there is a specific strong indication for them, such as flash pulmonary edema or severe systolic heart failure).
	- Fluoroquinolones[^1]
	- Benzodiazepines, zolpidem, diphenhydramine (delirium). (However, for patients on these medications _chronically_ they often must be continued).
- Anaemia
	- Avoid transfusions if hemoglobin is >70
	- Only transfuse one unit at a time (unless hemodynamically unstable, or severe anaemia)
- Volume Status & Hypotension
	- ICU patients usually retain fluid and develop volume overload.
	- Avoid giving fluid boluses unless the patient is clearly volume depleted.
	- Follow I/O balance daily and avoid progressive volume overload (e.g., with diuresis).


[^1]: See here [PulmCrit - Six reasons to avoid fluoroquinolones in the critically ill](https://emcrit.org/pulmcrit/fluoroquinolone-critical-illness/)