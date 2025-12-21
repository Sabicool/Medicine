---
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
date: 2025-12-21
aliases:
  - ABG Interpretation
tags:
  - notes
---
![Blood Gas Interpretation Acid Base LITFL Rogers 2024](https://litfl.com/wp-content/uploads/2019/01/Blood-Gas-Interpretation-Acid-Base-LITFL-Rogers-2024-1024x709.png)
![[Pasted image 20251125193546.png]]
# Useful information
- With respiratory problems, $p\ce{CO2}$ and pH change in different directions
- With metabolic problems, $p\ce{CO2}$ and pH change in the same direction
# Introduction
- Make sure you understand the difference between oxygenation and ventilation
- Have a good understanding of [[Acute Respiratory Failure]]
# Approach
1. $P\rm{a}\ce{O2}$: Determine the adequacy of oxygenation (80-100 mmHg)
2. Determine pH status (7.35-7.45)
	- pH <7.35: Acidosis: increase in the serum hydrogen ion concentration, lowers the pH and results in acidaemia
	 - pH >7.45: Alkalosis: decreases the hydrogen ion concentration and results in alkalaemia
3. Determine the primary disorder
	- $P\rm{a}\ce{CO2}$: Determine the respiratory component (35-45 mmHg)
		- $P\rm{a}\ce{CO2}$ <35 ⇒ ↑ respiratory rate ⇒ alkalotic change
			+ If pH >7.45: primary respiratory alkalosis (especially if $\ce{HCO3-}$ normal)
			+ If pH <7.35 and ↓ $\ce{HCO3-}$: respiratory compensation for metabolic acidosis
		- $P\rm{a}\ce{CO2}$ >45 ⇒ ↓ respiratory rate ⇒ acidotic change
			 + If pH <7.35 and $\ce{HCO3-}$ normal: hypoventilation
			 + If pH >7.45 and ↑ $\ce{HCO3-}$: respiratory compensation for metabolic alkalosis
	- $\ce{HCO3-}$: Determine the metabolic component (22-26 mmol/L)
		- $\ce{HCO3-}$<22 ⇒ acidotic change
			- If pH <7.35: primary metabolic acidosis
			- If pH >7.45: metabolic compensation for respiratory alkalosis
		- $\ce{HCO3-}$ >26 ⇒ alkalotic change
			- If pH >7.45: primary metabolic alkalaosis
			- If pH <7.35: metabolic compensation for respiratory acidosis
	- If both $P\rm{a}\ce{CO2}$ and $\ce{HCO3}$ are causing the same disturbance (i.e. both acidotic or alkalotic changes) there is co-existing primary respiratory and metabolic disorders
		- There is limited utility in calculating expected compensation
4. Is the compensation adequate
	- Metabolic acidosis: $P\rm{a}\ce{CO2}=\ce{HCO3}+15$ or $P\rm{a}\ce{CO2}=1.5\times\ce{HCO3}+8\pm2$
	- Metabolic alkalosis: $P\rm{a}\ce{CO2}=0.7\times\ce{HCO3}+20\pm5$
	- Respiratory acidosis
		- Acute: $\Delta\ce{HCO3}=0.1\times\Delta P\rm{a}\ce{CO2}$
		- Chronic: $\Delta\ce{HCO3}=0.4\times\Delta P\rm{a}\ce{CO2}$
	- Respiratory alkalosis
		- Acute: $\Delta\ce{HCO3}=0.2\times\Delta P\rm{a}\ce{CO2}$
		- Chronic: $\Delta\ce{HCO3}=0.5\times\Delta P\rm{a}\ce{CO2}$
5. Calculate the anion gap
	- High anion gap acidosis ⇒ addition of anions (conjugate bases of acids added to serum e.g. ketones or lactate)
	- Normal anion gap acidosis ⇒ loss of $\ce{HCO3}$ in urine or GI tract
$$
\rm{Anion\;Gap}=\ce{Na+}-\left(\ce{Cl-}+\ce{HCO3}\right)=12\pm4
$$
6. Delta ratio
	- Check delta ratio in the presence of a high anion gap metabolic acidosis to determine if it is a pure HAGMA or if there is co-existent normal anion gap metabolic acidosis or metabolic alkalosis
	- <0.4 ⇒ normal anion gap metabolic acidosis
	- 0.4-0.8 ⇒ combined HAGMA + NAGMA, but ratio is often <1 in acidosis associated with renal failure
	- 1-2 ⇒ uncomplicated HAGMA
	- ≥2 ⇒ pre-existing metabolic alkalosis or to compensation for a pre-existing respiratory acidosis (i.e. compensated chronic respiratory acidosis)
$$
\rm{Delta\;Ratio}=\frac{AG-12}{24-\ce{HCO3}}=\frac{\Delta AG}{\Delta\ce{HCO3}}
$$
7. Apply corrections to certain measured values
	1. 

![[Pasted image 20250125184001.png]]
- As an extra step you can determine the consistency of the values from the machine and confirm that the derrived $[\ce{HCO3}]$ is correct using:
$$
p\ce{H}=-\log_{10}\left(24\times\frac{Pa\ce{CO2}}{[\ce{HCO3}]}\times10^{-9}\right)
$$
# 12345 Rule
- Respiratory acidosis :: For every 10 mmHg rise in PaCO2, there should be 1 increase in $\ce{HCO3-}$ for acute and 4 increase in chronic
- Respiratory alkalosis :: For every 10mmHg rise in PaCO2, there should be 2 decrease in $\ce{HCO3-}$ for acute and 5 decrease in chronic
![[2024-04-24_09-21-18_screenshot.png]]
# Anion Gap
- Given by the formula:
$$
\rm{Anion\; Gap}=\ce{Na+ - (Cl- + HCO3^-)}
$$
- The normal value varies between machine and technique used (4-12 if measured by ion selective electrode or 8-16 if measured by flame photometry)
- If AG >30 mmol/L then metabolic acidosis is invariably present
- Importantly albumin is the major unmeasured anion and contributes most to the anion gap value, so in hypoalbuminaemia patients may appear as a normal anion gap acidosis but actually have a high anion gap acidosis
$$
\rm{Corrected\;Anion\;Gap}=\rm{Measured\;Anion\;Gap}+\frac{40-\rm{Albumin}}{4}
$$
- Additionally, you can correct for phosphate as well because hypophosphateaemia also lowers the expected anion gap
$$
\rm{Corrected\;Anion\;Gap}=0.25\times\rm{Albumin}+1.5\times\ce{PO4^{3-}}
$$
- High anion gap metabolic acidosis :: Accumulation of organic acids or impaired $\ce{H+}$ excretion
- Normal anion gap metabolic acidosis :: Loss of $\ce{HCO3-}$ from ECF
See: https://litfl.com/anion-gap/
# Corrected Values
- $\ce{Na+}$ for glucose
	- In patients with marked hyperglycaemia, the elevated serum glucose raises the serum tonicity (as the glucose cannot enter cells) which pulls water out of cells and expands the extracellular water compartment – thereby lowering the concentration of sodium
	- The corrected serum sodium can be calculated, which represents what the serum sodium concentration would be if the glucose level was reduced back to normal
	- If the corrected sodium is in a normal range – the patient does not have a concurrent hypotonic hyponatraemia
$$
\rm{Corrected}\;\ce{Na+}=\ce{Na+}+1.5\times\frac{glucose-5.5}{5.5}\approx\ce{Na+}+\frac{\rm{glcuose}-5}{3}
$$
- $\ce{K+}$ for pH
	- For each 0.1 pH drop below 7.4, $\ce{K+}$ rises by 0.6 mmol/L
	- e.g. For a patient with a $\ce{K+}$ of 4 mmol/L at pH 7.2, the corrected $\ce{K+}$ is 2.8, hence the patient is hypokalaemic and $\ce{K+}$ should be monitored and replaced as pH is corrected
$$
\rm{Corrected}\;\ce{K+}=\ce{K+}-0.6\times\frac{7.4-pH}{0.1}
$$
- Correcting $\ce{Ca+}$ for albumin, however evidence demonstrates that formulas actually perform worse than uncorrected calcium levels
$$
\rm{Corrected\;Calcium}=0.8\times(40-\rm{Albumin})+\ce{Ca^{2+}}
$$
# Sources
- https://litfl.com/acid-base-disorders/
# Useful resources
- https://onepagericu.com/acid-base
![[2024-04-24_09-38-53_screenshot.png]]