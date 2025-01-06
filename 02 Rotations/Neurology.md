---
date: 2025-01-03
---
<!-- QueryToSerialize: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
<!-- SerializedQuery: list rows.file.link from "01 Disciplines" where  contains(Rotations, "[" + this.file.name + "](" + replace(this.file.folder + "/" + this.file.name + "." + this.file.ext, " ", "%20")   + ")") OR contains(Rotations, this.file.link) or contains(file.path,this.file.name) group by reverse(split(file.folder, "/"))[0] -->
- Conditions: 
    - [[Subarachnoid Haemorrhage]]

- Emergencies: 
    - [[Unconsciousness]]

- Presenting Complaints: 
    - [[Altered Mental Status]]
    - [[Collapse, Syncope, Mechanical Falls]]

<!-- SerializedQuery END -->
