## Presenting Complaints
- [Chest Pain](01%20Disciplines/Cardiology/Presenting%20Complaints/Chest%20Pain.md)
## Disease Reference
Curated list:
- [Acute Coronary Syndromes](01%20Disciplines/Cardiology/Conditions/Acute%20Coronary%20Syndromes.md)
- [Hypertensive crisis](01%20Disciplines/Cardiology/Conditions/Hypertensive%20crisis.md)

Other automatically generated:
```dataview
list from "01 Disciplines"
group by file.name
```

```dataview
list file.inlinks
where file.name = this.file.name
```
```dataview
list from "01 Disciplines"
```
```dataview
table file.inlinks, Location
FROM "01 Disciplines"
FLATTEN regexreplace(file.folder, ".*\/([^\/]+)$", "$1") as Location
SORT Location
```

## Common Investigations
- [ECG Interpretation](01%20Disciplines/Cardiology/Investigations/ECG%20Interpretation.md)
- [Chest X-ray](Chest%20X-ray.md)
## Useful Resources
- NSW ECI/ACI clinical guidelines
- Toxicology guidelines: [Austin Health Toxicology Guidelines](https://www.austin.org.au/clinical-toxicology-guidelines/) *one pager Australian guidelines on toxicology for most medications that people overdose on and come through the ED with*
