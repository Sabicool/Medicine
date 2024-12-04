## Common Conditions
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
