---
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
date: 2026-01-16
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
# A-a Gradient and Oxygenation
- Hypoxia = pathophysiological state of inadequate oxygenation for aerobic metabolism; aetiologies include hypoxaemia, anaemia, dyshaemoglobinaemia, histotoxic hypoxia (e.g. cyanide poisoning)
- Hypoxaemia = ↓ concentration of oxygen in arterial blood
- $P_\text{a}\ce{O2}$ is the amount of oxygen dissolved in the blood and is measured directly from the ABG (normal >85 mmHg for young adult, child and >75 mmHg for elderly)
- $\ce{O2}$ sat commonly refers to the oxygen bound to haemoglobin:
	- $S_{\text{p}}\ce{O2}$ is the amount of oxygen bound to haemoglobin as measured from pulse oximetry
	- $S_\text{a}\ce{O2}$ is the amount of oxygen bound to haemoglobin as calculated from the ABG or measured by co-oximetry
- $P_{\text{A}}\ce{O2}$ is the partial pressure of oxygen in the alveolar gas
$$\text{A-a gradient} = \underset{\substack{\text{Estimated from the}\\\text{alveolar gas equation}}} {P_{\text{A}}\ce{O2}} - \underset{\substack{\text{Measured directly}\\\text{via ABG}}} {P_{\text{a}}\ce{O2}}$$
![[Pasted image 20260116200257.png|400]]
$$ P_{\text{A}}\ce{O2} = \left( \underset{\substack{\text{Fractional concentration}\\\text{of inspired } \ce{O2}}} {F_{\text{I}}\ce{O2}} \; \times \left( \underset{\substack{\text{Total pressure}\\\text{of inspired air}}} {P_{\text{I}}} - \underset{\substack{\text{Partial pressure}\\\text{of water vapour}}} {P_{\ce{H2O}}} \right) \right) - \left( \underset{\substack{\text{Arterial } \ce{CO2}\\\text{tension}}} {P_{\text{a}}\ce{CO2}} \Big/ \underset{\substack{\text{Respiratory}\\\text{Quotient}}} {\text{RQ}} \right) $$
- At sea level $F_\text{i}\ce{O2}=21\%$ (when not on oxygen), $P_\text{I}=760\;\text{mm}\ce{Hg}$, $P_\ce{H2O}=47\;\text{mm}\ce{Hg}$ and for most patients $\text{RQ}=0.8$[^1]so the above equation simplifies to: $P_{\text{A}}\ce{O2}=150-\frac{P_{\text{a}}\ce{CO2}}{0.8}$

| Oxygen Supply          | Approximate Maximum $F_\text{I}\ce{O2}$ |
| ---------------------- | --------------------------------------- |
| Room air               | 0.21                                    |
| Nasal cannula          | 0.50                                    |
| Venturi mask           | 0.50                                    |
| Simple face mask       | 0.60                                    |
| Non-rebreather         | 0.80-0.90                               |
| Mechanical ventilation | >0.90                                   |
- Variation of $F_\text{I}\ce{O2}$ with flow rate and respiratory rate for nasal prongs:
	- ![[Pasted image 20260116205713.png]]
	- Can be estimated with the following formula (use 0.03 for patients with increased respiratory rate and 0.05 for patients with normal respiratory rate):
	- $$F_\text{I}\ce{CO2}\approx 0.21 + (0.03 \to 0.05) \times \underset{(\text{L}/\text{min})}{\text{Flow rate}}$$
- Variation of $F_\text{I}\ce{O2}$ with respiratory rate
	- High flow systems are able to meet the patient’s full inspiratory flow requirement (i.e. $F_\text{I}\ce{O2}$ is independent of respiratory rate) (e.g. venturi mask, HFNP, mechanical ventilation)
	- Low flow systems are not able to meet the full inspiratory flow requirement (i.e. $F_\text{I}\ce{O2}$ varies with respiratory rate) 
- The normal A-a gradient increases with age[^2] and can be calculated by the following equation when there is no supplemental oxygen:
$$\text{Normal A-a gradient}=\left(\frac{\text{Age}}{4}\right)+4$$
- Due to physiological shunting caused by supplemental oxygen, the adjust A-a gradient can be approximated by:
$$
\text{Adjust Normal A-a gradient}\approx\left(\frac{Age}{4}+4\right)+50\times\left(F_\text{I}\ce{O2}-0.21\right)
$$
> [!NOTE] 
> If a patient has both a low $P_\text{a}\ce{CO2}$ and a low $P_\text{a}\ce{O2}$, then the A-a gradient must be elevated

- If the A-a gradient is normal then the cause of the hypoxaemia must be either:
	- Hypoventilation (i.e. ↑ $P_\text{a}\ce{CO2}$)
	- Low $P_{\text{I}}$ (e.g. extreme altitudes)
- If the A-a gradient is elevated then the cause of the hypoxaemia must be either:
	- V/Q mismatch
	- Shunt (i.e. there exists perfused alveoli with zero ventilation e.g. cardiac shunts, lobar pneumonia ARDS)
		- Importantly when $F_\text{I}\ce{O2}$ is increased, there is an increase in the A-a gradient as $P_\text{a}\ce{O2}$ can not be further increased
	- Impaired diffusion

> [!EXAMPLE] Simple Example
> **Question:** A 56 year old man with a history of CAD, HTN, and 60 pack years of smoking, presents to the ER with a productive cough and dyspnea x 3 days. On exam, his RR=28 and 02 sat = 81% on room air. His breaths are shallow and with pursed lips.
> ABG: pH: 7.31 / $P_\text{a}\ce{CO2}$ 60 / $P_\text{a}\ce{O2}$ 57 on room air
> Likely diagnosis?
> **Answer:**
> 1. Check A-a gradient
> $$
> \begin{align*}
> P_{\text{A}}\ce{O2} &= \left[ F_{\text{I}}\ce{O2} \left( P_{\text{I}} - P_{\ce{H2O}} \right) \right] - \left( \frac{P_{\text{a}}\ce{CO2}}{\text{RQ}} \right)\\
> P_{\text{A}}\ce{O2} &= 150 - \left( \frac{60}{0.8} \right) = 75 \ \text{mmHg} \\
> \text{A--a gradient} &= 75 - 57 = 18 \ \text{mmHg}\\
\end{align*}
> $$
> 2. Estimate normal A-a gradient $(\text{Age}/4)+4=(56/4)+4=18 \ \text{mmHg}$
> 3. Normal A-a gradient with high $P_\text{a}\ce{CO2}$ indicates a COPD exacerbation

 > [!Example] Harder Example
> **Question:** An 80 y/o man with COPD, presents to the ER with progressive dyspnea and cough for 3 days. He appears acutely uncomfortable, and his sitting up, leaning forward with his hands on his knees. Vitals: T=36.9°C, HR=104, BP=135/80, RR=30, 02 saturation=95% on Venturi mask set at 30%.
> ABG: pH: 7.28 / $P_\text{a}\ce{CO2}$ 80 / $P_\text{a}\ce{O2}$ 80 on 30% $F_\text{I}\ce{O2}$
> **Answer:**
> 1. Check A-a gradient
> $$
> \begin{align*}
> P_{\text{A}}\ce{O2} &= \left[ F_{\text{I}}\ce{O2} \left( P_{\text{I}} - P_{\ce{H2O}} \right) \right] - \left( \frac{P_{\text{a}}\ce{CO2}}{\text{RQ}} \right)\\
> &=\left[0.30\times(760-47)\right]-\frac{80}{0.8}=114\ \text{mmHg}\\
> \text{A-a gradient}&=114-80=34\ \text{mmHg}
> \end{align*}
> $$
> 2. Estimate adjusted normal A-a gradient
> $$
> \begin{align*}
> \text{Normal A-a gradient}&\approx\left(\text(Age)/4\right)+4+50\left(F_\text{I}\ce{O2}-0.21\right)\\
> &\approx\left(80/4\right)+4+50\times(0.30-0.21)\approx0.29\ \text{mmHg}
> \end{align*}
> $$
> 3. Pretty much normal A-a gradient with high $P_\text{a}\ce{CO2}$ indicates an acute COPD exacerbation

> [!Example] Harder Example
> **Question:** A 64 y/o man with a history of CAD, presents to the ER with sudden onset of dyspnea 1 hour ago. He is in moderate respiratory distress, with rapid, shallow breaths. Current vitals: T=36.2 °C HR=115, BP=95/40, RR=30, O2 saturation=100% on 6L via nasal prongs.
> ABG: pH 7.54 / $P_\text{a}\ce{CO2}$ 28 / $P_\text{a}\ce{O2}$ 143 on 6L $\ce{O2}$ via NP
> **Answer:**
> 1. Check the A-a gradient
> $$
> \begin{align*}
> F_\text{I}\ce{O2}&\approx0.21+(0.03\times 6)=0.39\\
> P_{\text{A}}\ce{O2} &= \left[ F_{\text{I}}\ce{O2} \left( P_{\text{I}} - P_{\ce{H2O}} \right) \right] - \left( \frac{P_{\text{a}}\ce{CO2}}{\text{RQ}} \right)\\
> &=243\ mmHg\\
> \text{A-a gradient}&=243-143=100\ \text{mmHg}
> \end{align*}
> $$
> 2. Estimate adjusted normal A-a gradient
> $$ 
> \begin{align*}
> \text{Normal A-a gradient}&\approx\left(\text(Age)/4\right)+4+50\left(F_\text{I}\ce{O2}-0.21\right)\\
> &\approx 29\ \text{mmHg}
> \end{align*}
> $$
> 3. Abrupt changes in A-a gradient without symptoms suggestive of hypertensive emergency or mucous plugging can be explained by pulmonary embolism or acute coronary syndrome with secondary pulmonary oedema


> [!Example] Harder Example
> ![[Pasted image 20260116233216.png]]
> - Increase in A-a gradient with increase $F_\text{I}\ce{O2}$ suggests right to left shunting
> - Patient appears to be due to intrapulmonary right to left shunting in a patient with septic shock (most likely severe sepsis and acute lung injury/ARDS secondary to endocarditis)

![[Pasted image 20260116235924.png]]
## Other Measures of Oxygenation
- $P_\text{a}\ce{O2}/F_\text{I}\ce{O2}$ Ratio
	- Used in ICU setting to measure severity of hypoxaemia
	- Normal: $100\;\text{mm}\ce{Hg}/0.21=476\;\text{mm}\ce{Hg}$
	- Abnormal:
		- 200-300 mm$\ce{Hg}$ ⇒ gas exchange abnormal
		- <200 mm$\ce{Hg}$ ⇒ severe abnormality (e.g. more suggestive of ARDS)
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
- [The A-a Gradient (ABG Interpretation - Lesson 16) - YouTube](https://www.youtube.com/watch?v=pEsOv_pdOUQ)
# Useful resources
- https://onepagericu.com/acid-base
![[2024-04-24_09-38-53_screenshot.png]]

[^1]: With the exception being patients with extreme diets (e.g. severe anorexia)
[^2]: The normal A-a gradient also increases with higher $F_\text{I}\ce{O2}$ and may be >100 mmHg in an elderly patient on 100% $\ce{O2}$