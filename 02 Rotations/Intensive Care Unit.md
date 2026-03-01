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
	- All ICU patients should receive DVT prophylaxis unless there is a contraindication[^2]
		- Haemorrahge
		- Thrombocytopenia (platelet count <~30,000 or <~50,000 and falling
		- Planned procedure (e.g. lumbar puncture, IR procedure)
	- GFR >30 ml/min: Generally enoxaparin 40 mg daily
		- Weight <50 kg: use enoxaparin 20 mg daily
		- Weight >120 kg: consider ~0.25 mg/kg q12hr
		- Monitor anti-factor Xa levels for patients with unusual weight, pregnancy or borderline renal function; check four hours after the third dose
	- GFR <30 ml/min: Use heparin 5,000 IU TDS/BD
- GI prophylaxis
	- As a simple rule of thumb, use GI prophylaxis only for intubated patients
	- Preferred agent is pantoprazole 40 mg PO/IV daily
- Medications to avoid in ICU
	- NSAIDs (renal failure, bleeding).
	- ACEi/ARBs (avoid unless there is a specific strong indication for them, such as [[Acute Pulmonary Oedema|Sympathetic crashing APO]] or severe systolic heart failure)
	- Fluoroquinolones[^1]
	- Benzodiazepines, zolpidem, diphenhydramine (delirium). (However, for patients on these medications _chronically_ they often must be continued)
		- Should be restricted to use in:
			- Status epilepticus.
			- Ketamine re-emergence, procedural sedation.
			- Patients who are chronically on benzodiazepines as a home medication.
			- Palliative sedation.
			- Occasional cases of complicated alcohol withdrawal
		- Better alternatives:
			- For insomnia: quetiapine, guanfacine.
			- For acute agitation: haloperidol, olanzapine, dexmedetomidine.
			- For sedation: dexmedetomidine, propofol, possibly quetiapine.
	- Tramadol
- Anaemia
	- Avoid transfusions if hemoglobin is >70
	- Only transfuse one unit at a time (unless hemodynamically unstable, or severe anaemia)
- Volume Status & Hypotension
	- ICU patients usually retain fluid and develop volume overload.
	- Avoid giving fluid boluses unless the patient is clearly volume depleted.
	- Follow I/O balance daily and avoid progressive volume overload (e.g., with diuresis).
- [[Hyponatraemia]]
	- Hypernatraemia should _not_ be tolerated, as it will make patients delirious and miserable (thirsty) (One exception = intracranial pressure elevation)
	- Calculate the amount of free deficit (otherwise we tend to underestimate water requirements)
	- Provide free water in the form of oral water (e.g., via enteral tube) or as D5W intravenously
- [[Hypokalaemia]]
	- - Generally target **K>3.5** (not >4, this makes your life easier!)
	- Whenever possible use enteral potassium (it's safer and doesn't sclerose veins)
	- Be cautious in renal failure
- [[Hypocalcaemia]]
	- Most critically ill patients are hypocalcemic, and the best thing is usually to _ignore it._
	- Avoid administration of IV calcium in response to a low calcium level unless the patient is symptomatic or the ionized calcium is extremely low (e.g., perhaps <0.8 mM). IV calcium is primarily useful for massive transfusion protocols or hyperkalemia
	- IV calcium is relatively contraindicated in hyperphosphatemia (risk of calciphylaxis)
- Trops and Ischaemic evaulation
	- Screen for ischemia with a good history and careful evaluation of the ECG
	- Don't measure troponin unless there is a legitimate concern for MI based on history and/or ECG and/or echocardiogram.
	- Most critically ill patients will have elevated troponin levels. Checking troponin on every patient will generate false-positive results and lead to iatrogenic harm
- Sedation
	- Propofol
		- Easily & rapidly titrated.
		- May cause hypotension, but this can be counteracted with an infusion of low-dose norepinephrine (e.g. ~0-8 mcg/min).
		- Use of high propofol doses for prolonged periods of time may cause hypertriglyceridemia and a risk of propofol infusion syndrome. Over extended periods of time, it's ideal to wean the dose down to <50 mcg/kg/min.
	- Dexmedetomidine
		 - The major advantage of dexmedetomidine is that it doesn't suppress respiration, making it safe to use in a non-intubated patient
			 - Therefore, dexmedetomidine may be continued _throughout_ the weaning process (unlike propofol, which must be shut off prior to extubation)
			 - This is an excellent option for patients who develop anxiety and tachypnea whenever sedation is lifted, making it difficult to extubate them
		- Dexmedetomidine may cause hypotension due to bradycardia, but this can be counteracted with an infusion of low-dose epinephrine if the use of dexmedetomidine is critical.

[^1]: See here [PulmCrit - Six reasons to avoid fluoroquinolones in the critically ill](https://emcrit.org/pulmcrit/fluoroquinolone-critical-illness/)
[^2]: Patients with cirrhosis and elevated INR are generally not coagulopathic and generally do require DVT prophylaxis