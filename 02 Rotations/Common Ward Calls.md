---
aliases:
  - On call
---
## Auto Generated List
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
6. Note relevant laboratory, ECG or X-ray findings
