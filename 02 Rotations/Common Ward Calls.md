---
aliases:
  - On call
---
## Auto Generated List
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[01 Disciplines/Cardiology/Conditions/Hypotension.md|Hypotension]]
    - [[01 Disciplines/Cardiology/Conditions/Hypertensive crisis.md|Hypertensive crisis]]
    - [[01 Disciplines/Endocrinology/Conditions/Hyperglycaemia.md|Hyperglycaemia]]

- Emergencies: 
    - [[01 Disciplines/Clinical/Emergencies/Advanced Life Support.md|Advanced Life Support]]
    - [[01 Disciplines/Clinical/Emergencies/Basic Life Support.md|Basic Life Support]]

- Presenting Complaints: 
    - [[01 Disciplines/Cardiology/Presenting Complaints/Chest Pain.md|Chest Pain]]
    - [[01 Disciplines/Neurology/Presenting Complaints/Altered Mental Status.md|Altered Mental Status]]
    - [[01 Disciplines/Nephrology/Presenting Complaints/Decreased Urine Output.md|Decreased Urine Output]]

- Procedures: 
    - [[01 Disciplines/Clinical/Procedures/IV Cannulation.md|IV Cannulation]]

- Topics: 
    - [[01 Disciplines/Paediatrics/Topics/Paediatric Pain Management.md|Paediatric Pain Management]]
    - [[01 Disciplines/Clinical/Topics/Pain Management.md|Pain Management]]
    - [[01 Disciplines/Clinical/Topics/Preparing Patients for Transfer.md|Preparing Patients for Transfer]]

<!-- SerializedQuery END -->

Also see:
- [iSBAR Handover](00%20Reference/Clinical/iSBAR%20Handover.md)
## Documenting on call visits
1. Begin with date, time and who you are: *9 December 2024: 0300 hours. Resident on-call note*
2. State who called you and at what time you were called: *Called by nursing staff at 02:30 hours to see a patient who 'fell out of bed'*. If the assessment was delayed by more pressing matter, say so
3. Brief summary of the patient's admission diagnosis and major medical problems:

> [!EXAMPLE] 
> 74 year old female
> Admitted 10 days ago with joint pain and poor mobility
> Medical history: chronic renal failure, type 2 diabetes mellitus, rehumatoid arthritis

4. HxPC, no different from the documentation in an admission history. Consider any other relevant findings
5. Document the examination findings of your selective physical exam. Consider underlining the abnormal physical findings.
6. Note relevant laboratory, ECG or X-ray findings also underlining the abnormal physical findings
7. Write the provisional or 'working' diagnosis, followed by potential differential diagnosis, listing the most likely alternative explanations in order, then any complications

> [!EXAMPLE] 
> 1. Unwitnessed fall on the way to bathroom
> 	Presumed mechanical fall (?diuretic-induced nocturia, ?contribution of sedation)
> 2. Large bruise to left thigh, but no obvious bony injury. No other findings

8. State the management and measures taken during the night

> [!EXAMPLE]
> - Simple analgesia
> - Ice pack to thigh haematoma
> - Review mobility by inpatient team mane

9. If you informed another resident, registrar or consultant, document the time and whome you spoke and state the recommendations given

> [!EXAMPLE] 
> Discussed with Medical Registrar at 03:30 hours
> Suggests: team to reassess mobility in the morning, and the role of diuretics and sedation

10. Record whether any of the patient's family members were informed of the problem and what they were told
11. Sign the clinical note and print name and designation

# For reference

 ```dataview
list rows.file.link
from "01 Disciplines"
where 
	contains(Rotations, "[" + this.file.name + "]("
		+ replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")  
		+ ")") OR
	contains(Rotations, this.file.link)
group by reverse(split(file.folder, "/"))[0]
```