---
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
date: 2026-01-22
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
1. Determine the adequacy of oxygenation 
	- Refer to the $S_\text{p}\ce{O2}$ from the sats probe or $S_\text{a}\ce{O2}$ as calculated from the ABG or measured from co-oximetry to observe for hypoxaemia
	- Calculate the A-a gradient
		1. Calculate the $F_{I}\ce{O2}$ (see below for calculations and suggested values)
		2. Calculate $P_\text{A}\ce{O2}$ using the alveolar gas equation which takes the following values for most patients at sea level
			$$
			\begin{align*}
			P_\text{A}\ce{O2}&=F_\text{I}\ce{O2}\times\left[P_\text{I}-P_\ce{H2O}\right]-\left(\frac{P_\text{a}\ce{CO2}}{\text{RQ}}\right)\\
			&\approx F_\text{I}\ce{O2}\times\left[760-47\right]-\left(\frac{P_\text{a}\ce{CO2}}{0.8}\right)
			\end{align*}
			$$
		3. Calculate the A-a gradient
		4. Estimate the adjusted normal A-a gradient
			$$
			\text{Normal A-a gradient}\approx\frac{\text{Age}}{4}+4+50\times\left(F_\text{I}\ce{O2}-0.21\right)
			$$
		5. Compare the A-a gradient (<10 mmHg normal)
			- If normal, either due to hypoventilation (observe $P_\text{a}\ce{CO2}$) or low atmospheric pressure
			- If elevated, observe for correction of $\ce{O2}$ sats with 100% $F_\text{I}\ce{O2}$
				- If corrects, suggestive of V/Q mismatch and/or diffusion impairment
				- If doesn’t correct, suggestive of right to left shunt
				- Correlate with history, exam and chest X-ray
		6. Check for dyshaemoglobinaemia from the co-oximetry
2. Determine pH status (7.35-7.45)
	- pH <7.35: acidaemia: increase in the serum hydrogen ion concentration, lowers the pH
	 - pH >7.45: alkalaemia: decreases the hydrogen ion concentration, raises the pH
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
	- If the pH is normal, there is another primary acid/base disorder as compensation will _never_ bring the pH back to adequacy (e.g. if there is respiratory acidosis and the pH is normal, there must also be a primary metabolic alkalosis)
	- Metabolic compensation takes 12 hours - 5 days to take peak effect (generally $\pm5$ for metabolic compensation formulas)
		- Metabolic acidosis:$P\rm{a}\ce{CO2}=1.5\times\ce{HCO3}+8\pm2$ (Winter’s formula) or $P\rm{a}\ce{CO2}=\ce{HCO3}+15$
		- Metabolic alkalosis: $P\rm{a}\ce{CO2}=0.7\times\ce{HCO3}+20\pm5$ or $P_\text{a}\ce{CO2}=40+0.7\times\left(\ce{[HCO_3^-]}-24\right)$
			- Compensation for a metabolic alkalosis is relatively poor because hypoventilation as a compensation mechanism results in hypoxaemia 
		- Easier rule for compensation in metabolic disorders: $P_\text{a}\ce{CO2}$ is approximately the same as the first two digits of the pH after the decimal point
			- e.g ABG: pH 7.27 / $P_\text{a}\ce{CO2}$ 25 / $\ce{HCO_3^-}$ 11 ⇒ decimals of pH is 27 and $P_\text{a}\ce{CO2}$ is 25 so approximately equal, hence physiologic compensation is adequate
	- Respiratory compensation takes 1 - 24 hours to take peak effect (generally $\pm3$ for respiratory compensation formulas)
		- Respiratory acidosis
			- Acute: $\Delta\ce{HCO3}=0.1\times\Delta P\rm{a}\ce{CO2}$ or $\ce{[HCO_3^-]}=24+\frac{P_\text{a}\ce{CO2}-40}{10}$
			- Chronic: $\Delta\ce{HCO3}=0.4\times\Delta P\rm{a}\ce{CO2}$ or $\ce{[HCO_3^-]}=24+4\times\frac{P_\text{a}\ce{CO2}-40}{10}$
		- Respiratory alkalosis
			- Acute: $\Delta\ce{HCO3}=0.2\times\Delta P\rm{a}\ce{CO2}$ or $\ce{[HCO_3^-]}=24-2\times\frac{4-P_\text{a}\ce{CO2}}{10}$
			- Chronic: $\Delta\ce{HCO3}=0.5\times\Delta P\rm{a}\ce{CO2}$ or $\ce{[HCO_3^-]}=24-5\times\frac{4-P_\text{a}\ce{CO2}}{10}$
5. Calculate the anion gap
	- High anion gap acidosis ⇒ addition of anions (conjugate bases of acids added to serum e.g. ketones or lactate)
		- Severe renal failure can lead HAGMA to excrete phosphate and sulphate in the urine resulting in their accumulation
		- Lactic acidosis, ketoacidosis (DKA, ETOH, starvation), methanol ingestion, ethylene glycol ingestion, toluene inhalation (glue sniffing)
	- Normal anion gap acidosis ⇒ decreased renal $\ce{H+}$ excretion or loss of $\ce{HCO3}$ in urine or GI tract 
		- Loss of $\ce{HCO3}$: diarrhoea/GI drainage, Type 2 [[Renal tubular acidosis]], [[Diuretics#Acetazolamide|Acetazolamide]]
		- Decreased $\ce{H+}$ excretion: renal failure, Type 1 [[Renal tubular acidosis]], Type 4 [[Renal tubular acidosis]]/[[Conn syndrome]]
		- Results in decrease in $\ce{HCO3}$ with an increase in $\ce{Cl-}$ a roughly 1:1 ratio (hence NAGMA sometimes called hyperchloraemic acidosis)
		$$
		\rm{Anion\;Gap}=\ce{Na+}-\left(\ce{Cl-}+\ce{HCO3}\right)=12\pm4
		$$
	- Anion gap unrelated to metabolic acidosis:
		- High anion gap can be due to metabolic alkalosis, hyperphosphataemia
		- Low anion gap can be due to hypoalbuminaemia, ↑ $\ce{K+}$, ↑ $\ce{Ca^{2+}}$, ↑ $\ce{Mg^{2+}}$, Severe lithium toxicity, bromide ingestion (some machines mistake bromine for chlorine; [[Myaesthenia gravis]] medications can contain bromine)
	- Adjust anion gap for hypoalbuminaemia:
		$$
		\text{AG}_\text{adjusted}=\text{AG}_\text{measured}+0.25\times(40-[\text{Alb}])
		$$
6. Delta ratio in patients with HAGMA
	- During a HAGMA there should be a 1:1 gap between the ↑ anion gap and ↓ $\ce{HCO3}$
	- Check delta ratio in the presence of a high anion gap metabolic acidosis to determine if it is a pure HAGMA or if there is co-existent normal anion gap metabolic acidosis or metabolic alkalosis
	- The expected delta radio differs by aetiology of HAGMA:
		- Lactic acidosis: 1.6 (1.0 - 2.0) with it initially starting at 1.0 and increasing with time
		- Ketoacidosis: 1.0 (0.8 - 1.2) unless ↓ GFR in which case the ratio may be higher
		- Kidney disease: variable depending on the extent of tubular damage relative to ↓ GFR
		- Methanol, ethylene glycol ingestion: Unknown, probably 1.0 - 2.0
	- Based on the above, the interpretation is made such that if the measured delta ratio is:
		- Lower than the expected range, there is HAGMA and NAGMA
		- Within expected range, there is HAGMA only (although there could be respiratory disorder)
		- Higher than the expected range, there is a HAGMA and metabolic alkalosis
	- A negative delta ratio is possible in the following contexts:
		- High anion gap metabolic acidosis and metabolic alkalosis (can result in a normal or high pH)
		- Mild high anion gap metabolic acidosis and severe chronic respiratory acidosis (usually results in a very low pH)
	- Interpretation
	- <0.4 ⇒ normal anion gap metabolic acidosis
	- 0.4-0.8 ⇒ combined HAGMA + NAGMA, but ratio is often <1 in acidosis associated with renal failure
	- 1-2 ⇒ uncomplicated HAGMA
	- ≥2 ⇒ pre-existing metabolic alkalosis or to compensation for a pre-existing respiratory acidosis (i.e. compensated chronic respiratory acidosis)
	$$
	\rm{Delta\;Ratio}=\frac{AG_\text{adjusted}-12}{24-\ce{HCO3}}=\frac{\Delta AG}{\Delta\ce{HCO3}}
	$$
7. Apply corrections to certain measured values

![[Pasted image 20250125184001.png]]
- As an extra step you can determine the consistency of the values from the machine and confirm that the derrived $[\ce{HCO3}]$ is correct using:
$$
p\ce{H}=-\log_{10}\left(24\times\frac{Pa\ce{CO2}}{[\ce{HCO3}]}\times10^{-9}\right)
$$
# Additional Details
## Differentials
### High Anion Gap Metabolic Acidosis
- Methanol
- Renal failure
- Ketaocidosis
	- Diabetes
	- Starvation
	- Chronic alcoholism
- Paraldehyde
- INH, iron, intoxication, infection
- Lactic acidosis
	- Increased production of lactate:
		- Problem with $\ce{O2}$ delivery (e.g. shock, bowel infarction, hypoxaemia)
		- Problem with $\ce{O2}$ utilisation (e.g. genetic enzymatic defects, mitochondrial toxins, thiamine deficiency)
		- Primary production from tumours
		- Increased motor activity (e.g. seizures, vigorous exercise)
	- Decreased clearance (e.g. liver failure or renal failure although noting that renal failure alone is unlikely to cause lactic acidosis)
	- GI absorption of D-Lactate
- Ethylene glycol, ethanol
- Salicylic acid
## Drug Overdose Changes
- Respiratory alkalosis in the setting of drug overdose can be due to:
	- Aspiration on vomit causing hypoxia induced hyperventilation
	- Aspirin ingestion causing hyperventilation
- Most drug overdose causes respiratory acidosis
## A-a Gradient and Oxygenation
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
	- $$F_\text{I}\ce{O2}\approx 0.21 + (0.03 \to 0.05) \times \underset{(\text{L}/\text{min})}{\text{Flow rate}}$$
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
> &=243\ \text{mmHg}\\
> \text{A-a gradient}&=243-143=100\ \text{mmHg}
> \end{align*}
> $$
> 2. Estimate adjusted normal A-a gradient
> $$ 
> \begin{align*}
> \text{Normal A-a gradient}&\approx\left(\text{Age}/4\right)+4+50\left(F_\text{I}\ce{O2}-0.21\right)\\
> &\approx 29\ \text{mmHg}
> \end{align*}
> $$
> 3. Abrupt changes in A-a gradient without symptoms suggestive of hypertensive emergency or mucous plugging can be explained by pulmonary embolism or acute coronary syndrome with secondary pulmonary oedema


> [!Example] Harder Example
> ![[Pasted image 20260116233216.png]]
> - Increase in A-a gradient with increase $F_\text{I}\ce{O2}$ suggests right to left shunting
> - Patient appears to be due to intrapulmonary right to left shunting in a patient with septic shock (most likely severe sepsis and acute lung injury/ARDS secondary to endocarditis)

![[Pasted image 20260116235924.png]]
![[Pasted image 20260118001321.png]]

### Other Measures of Oxygenation
- $P_\text{a}\ce{O2}/F_\text{I}\ce{O2}$ Ratio
	- Used in ICU setting to measure severity of hypoxaemia
	- Normal: $100\;\text{mm}\ce{Hg}/0.21=476\;\text{mm}\ce{Hg}$
	- Abnormal:
		- 200-300 mm$\ce{Hg}$ ⇒ gas exchange abnormal
		- <200 mm$\ce{Hg}$ ⇒ severe abnormality (e.g. more suggestive of ARDS)
### Effect of Altitude
- Higher altitudes will only decrease $P_\text{I}$ in the alveolar gas equation (no effect on $F_\text{I}\ce{O2}$ or $P_\ce{H2O}$)
- $P_\text{a}\ce{CO2}$ usually decreases at high altitudes due to hypoxia-driven hyperventilation
![[Pasted image 20260118201043.png]]
## 12345 Rule
- Respiratory acidosis :: For every 10 mmHg rise in PaCO2, there should be 1 increase in $\ce{HCO3-}$ for acute and 4 increase in chronic
- Respiratory alkalosis :: For every 10mmHg rise in PaCO2, there should be 2 decrease in $\ce{HCO3-}$ for acute and 5 decrease in chronic
![[2024-04-24_09-21-18_screenshot.png]]

|                       | Acute                   | Chronic                 |
| --------------------- | ----------------------- | ----------------------- |
| Respiratory Acidosis  | ↑ $\ce{[HCO_3^-]}$      | ↑ by 4 $\ce{[HCO_3^-]}$ |
| Respiratory Alkalosis | ↓ by 2 $\ce{[HCO_3^-]}$ | ↓ by 5 $\ce{[HCO_3^-]}$ |

## Anion Gap
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


> [!EXAMPLE]
> **Question**
> A 48 y/o alcoholic man is found unconscious in his apartment, soiled with vomit. He was last seen leaving a party 6 hrs prior.
> ABG: pH 7.17 / $P_\text{a}\ce{CO2}$ 65 / $\ce{HCO_3^-}$ 22 / Na: 136 / Cl 98 / Albumin 16
> What disorders are present?
> **Solution**
> 1. pH suggestive of acidaemia
> 2. $P_\text{a}\ce{CO2}$ elevated suggestive of respiratory acidosis
> 3. Check compensation. $\ce{HCO_3^-}$ should increase by 1 for every 10 $P_\text{a}\ce{CO2}\ 40\pm3$ ⇒ $24+2.5\pm3$ ⇒ lowest allowed value is 23.5, therefore additional metabolic acidosis present
> 4. Calculate anion gap: $\text{AG} = 136 - (98+22)=16$. $\text{AG}_\text{adjusted}=\text{AG}_\text{measured}+0.25\times(40-16)=22$ ⇒ high anion gap metabolic acidosis
> 5. Calculate delta ratio: $\Delta\text{AG}/\Delta\ce{HCO_3^-}=10/2=5$ which is higher than expected irrespective of the aetiology so there is also a metabolic alkalosis present
> 6. Respiratory acidosis (from intoxication from central respiratory depression) + high anion gap metabolic acidosis (from alcoholic ketoacidosis) + metabolic alkalosis (from vomiting)
 
## Corrected Values
- $\ce{Na+}$ for glucose
	- In patients with marked hyperglycaemia, the elevated serum glucose raises the serum tonicity (as the glucose cannot enter cells) which pulls water out of cells and expands the extracellular water compartment – thereby lowering the concentration of sodium
	- The corrected serum sodium can be calculated, which represents what the serum sodium concentration would be if the glucose level was reduced back to normal
	- If the corrected sodium is in a normal range – the patient does not have a concurrent hypotonic hyponatraemia
$$
\rm{Corrected}\;\ce{Na+}=\ce{Na+}+1.5\times\frac{glucose-5.5}{5.5}\approx\ce{Na+}+\frac{\rm{glcuose}-5}{3}
$$
- $\ce{K+}$ for pH (acidaemia causes hyperkalaemia)
	- For each 0.1 pH drop below 7.4, $\ce{K+}$ rises by 0.6 mmol/L
	- e.g. For a patient with a $\ce{K+}$ of 4 mmol/L at pH 7.2, the corrected $\ce{K+}$ is 2.8, hence the patient is hypokalaemic and $\ce{K+}$ should be monitored and replaced as pH is corrected
$$
\rm{Corrected}\;\ce{K+}=\ce{K+}-0.6\times\frac{7.4-pH}{0.1}
$$
	- This occurs because of the exchange of $\ce{H+}$ ions for $\ce{K+}$ ions across the cell membrane which may cause the appearance of hyperkalaemia on serum potassium levels but the patient is actually net hypokalaemic
	- Correcting for potassium in alkalaemia (i.e. alkalaemia causing hypokalaemia) is not often done as the change is quantitatively smaller
- Correcting $\ce{Ca+}$ for albumin, however evidence demonstrates that formulas actually perform worse than uncorrected calcium levels
$$
\rm{Corrected\;Calcium}=0.8\times(40-\rm{Albumin})+\ce{Ca^{2+}}
$$
## Easily Figuring Out Direction of Compensation
- One must just look at the Henderson-Hasselbach equation to determine that for the pH to remain the same, the $\ce{HCO_3^-}$ must move in the same direction as $P_\text{a}\ce{CO2}$ and vice versa
$$
\ce{pH}=6.1+\log\left(\frac{\ce{[HCO_3^-]}}{0.03\times P_\text{a}\ce{CO2}}\right)
$$
# Sources
- https://litfl.com/acid-base-disorders/
- [The A-a Gradient (ABG Interpretation - Lesson 16) - YouTube](https://www.youtube.com/watch?v=pEsOv_pdOUQ)
# Useful resources
- https://onepagericu.com/acid-base
![[2024-04-24_09-38-53_screenshot.png]]

[^1]: With the exception being patients with extreme diets (e.g. severe anorexia)
[^2]: The normal A-a gradient also increases with higher $F_\text{I}\ce{O2}$ and may be >100 mmHg in an elderly patient on 100% $\ce{O2}$