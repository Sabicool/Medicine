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
	- Follow I/O balance daily and avoid progressive volume overload (e.g., with diuresis)
	- LR is generally the fluid of choice in the ICU with the following two exceptions:
		1.  Patients with elevated intracranial pressure (normal saline may be preferable).
		2. Patients with metformin-induced lactic acidosis (optimal fluid in this situation is hotly debated, but it's not LR
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
		- Dexmedetomidine may cause hypotension due to bradycardia, but this can be counteracted with an infusion of low-dose epinephrine if the use of dexmedetomidine is critical
- Ventilation
	- etCO2
		- etCO2 will always _underestimate_ blood pCO2, because gas in the trachea _dilutes_ CO2 as it travels from the alveoli to the ventilator.
		    - If the etCO2 is >45 mm, then the patient is definitely hypercapneic.
		- The gap between etCO2 and pCO2 depends on how healthy the lungs are:
		    - In healthy lungs, this gap is usually <15 mm.
		    - In patients with lung disease (e.g., COPD, pneumonia, ARDS, PE, pulmonary contusion) the gap will widen.
		- For most patients, after intubation the respiratory rate should usually be adjusted to achieve an etCO2 of ~30 mm. This should put the pCO2 in a safe range (~35-50 mm).
		    - One exception would be in patients with severe metabolic acidosis, in whom the respiratory rate should initially be _maximized_ in efforts to provide a compensatory respiratory alkalosis
	- Titrating NIV settings
		- **Cardiogenic pulmonary edema**
			- Key here is the _expiratory pressure_ (this increases the mean airway pressure and thereby decreases preload & afterload).
			- Ramp up expiratory pressure until the patient improves (e.g. 10/5 ==> 15/10 ==> 18/15), It’s also fine to simply use continuous positive airway pressure (CPAP). In that case, escalate CPAP pressure from 5 ==> 10 ==> 15 cm.
		- **Hypercapnia (e.g., COPD or obesity hypoventilation syndrome)**
			- The key here is _driving pressure_ (inspiratory pressure _minus_ expiratory pressure), which supports the work of breathing.
			- Ramp up the driving pressure until the patient improves (e.g. 10/5 ==> 15/5 ==> 18/5)
- Fevers
	- Causes
		- Infection: (~50% of cases)
		    - Pneumonia.
		    - C. difficile, Acalculous cholecystitis.
		    - Line infection.
		    - Surgical site infection.
		- Non-infectious: (~50% of cases)
		    - Procedure-related (hemodialysis, bronchoscopy, 1-3 days post-surgery).
		    - Drug fever.
		    - Febrile transfusion reaction.
		    - Sterile inflammation (pancreatitis, aspiration pneumonitis, ARDS).
		    - Pulmonary embolism.
		    - Alcohol withdrawal.
		    - Central fever (intracranial hemorrhage).
	- Workup
		- Physical examination, focusing on:
		    - Sites of any intravascular catheter or surgical incision.
		    - Abdomen (distension or tenderness)?
		    - Sputum quality and volume.
		- Chest radiograph if intubated or symptoms of pneumonia.
		- Blood cultures:
		    - At least two sets of cultures from different venipuncture sites, with at least one peripheral culture.
		    - Any line in place >48 hours should be cultured.
		- C. difficile testing, if diarrhea.
		- Further testing per clinical judgement (e.g. abdominal CT scan, CT angio for PE).
- Transferring patients out of ICU (Very Lazy Rabbits Rarely Make Lemonade)
	- **V**itals:
	    - Evaluate vital signs for any worrisome trends (especially unexplained/worsening tachycardia or tachypnea).
	    - Vital signs _don't_ need to be normal for patients leaving the ICU. However, abnormalities should be adequately investigated and not deteriorating.
	- **L**abs:
	    - Look at the latest labs for any values that require intervention before transfer.
	    - Labs most likely to hold up a transfer: potassium, lactate, hemoglobin, and blood gas values.
	    - Like vitals, labs _don't_ need to be normal. However, abnormalities should be appropriately investigated and managed.
	- **R**N:
	    - Discuss with the bedside RN whether there are any barriers to transferring to the floor.
	    - RNs know precisely how much care the patient requires and whether they are floor-appropriate.
	- **R**T:
	    - Discuss with the RT whether the respiratory care needs can be met on the floor.
	    - (Only necessary for patients with respiratory dysfunction.)
	- **M**eds:
	    - Review the medication list.
	    - Remove any ICU-specific medications (e.g., GI prophylaxis).
	    - Remove PRN medications that could be misused.
	- **L**ines:
	    - Remove any arterial lines.
	    - Remove central lines or HD catheters if possible. If the line must remain, ensure that another service is aware of the line and is responsible for removing it promptly

[^1]: See here [PulmCrit - Six reasons to avoid fluoroquinolones in the critically ill](https://emcrit.org/pulmcrit/fluoroquinolone-critical-illness/)
[^2]: Patients with cirrhosis and elevated INR are generally not coagulopathic and generally do require DVT prophylaxis