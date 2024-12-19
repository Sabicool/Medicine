## Common Conditions
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[01 Disciplines/Infectious Disease/Conditions/Septicaemia.md|Septicaemia]]

- Emergencies: 
    - [[01 Disciplines/Clinical/Emergencies/Shock.md|Shock]]
    - [[01 Disciplines/Clinical/Emergencies/Acute Airway Failure.md|Acute Airway Failure]]

- Investigations: 
    - [[01 Disciplines/Cardiology/Investigations/ECG Interpretation.md|ECG Interpretation]]

<!-- SerializedQuery END -->
