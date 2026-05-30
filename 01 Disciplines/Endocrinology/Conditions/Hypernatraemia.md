---
Rotations:
  - "[[Intensive Care Unit]]"
date: 2026-05-30
---
# Aetiologies
- [[Diabetes insipidus]]
![[Pasted image 20260530190028.png]]
# Clinical Features
- Similar to [[Hyponatraemia]], mostly neurological:
	- Increased temperature
	- Restlessness
	- Irritability
	- Confusion
	- Drowsiness
	- Coma
	- Seizures
	- Subarachnoid haemorrhage (due to brain shrinkage and vascular rupture)
# Workup
1. Consider history
	- Loss of solute poor water + primary neurologic disease or lack of access to water
	- As a result most patients are very young or very old
2. Urine osmolality
	- Low urine osmolality (<300 mOsm/kg): [[Diabetes insipidus]]
	- High urine osmolality (>600 mOsm/kg): impaired thirst or access to water
3. If [[Diabetes insipidus]], determine type using response to administration of desmopressin
![[Pasted image 20260530191027.png]]
# Management
- Chronic hypernatraemia (>48 hours): correction rate ≤10 mmol/L each 24 hours
- Acute hypernatraemia (<48 hours): correction to normal over 24 hour period
- Choice of fluid
	- Normal saline should be used only as initial therapy in patients with end-organ dysfunction secondary to depletion 
	- 5% glucose should be used in situations of pure water loss (e.g. [[Diabetes insipidus]])
	- Hypotonic fluid (e.g. half normal saline, quarter normal saline) should be used in situations with hypotonic fluid losses (e.g. diarrhoea)
- Calculate rate
$$
\text{Total body water (L)}\approx \text{Lean body weight (kg)} \times \underset{\text{Proprotionality Constant}}{k}\begin{cases}
k=0.6\text{ in children} \\
k=0.5\text{ in non-elderly adults} \\
k=0.45\text{ in elderly}
\end{cases}
$$
$$
\Delta [\ce{Na+}]\text{ from 1L of IV fluid}=\frac{([\ce{Na+}])_{\text{infusate}}-[\ce{K+}]_{\text{infusate}}-[\ce{Na+}]_{\text{serum}}}{\text{Total body water (L)}+1}
$$

> [!EXAMPLE]
> An 85 year old woman 70kg with dementia develops diarrhoea while living at a nursing facility. After 4 days, she is unrousable by staff and brought to the emergency department. She appears hypovolaemic on examination and has a serum sodium of 170 mmol/L and a serum potassium of 2.8 mmol/L. What rate of what fluid should be chosen to correct this?
> - Hypotonic fluid loss without mention of end-organ dysfunction with hypokalaemia ⇒ 1/2 normal saline + 20 mmol/L $\ce{KCl}$
> - Rate calculation as follows:
> $$
> \begin{align}
>  \Delta [\ce{Na+}]\text{ from 1L of IV fluid}&=\frac{([\ce{Na+}])_{\text{infusate}}-[\ce{K+}]_{\text{infusate}}-[\ce{Na+}]_{\text{serum}}}{\text{Total body water (L)}+1} \\
>  &=\frac{(77+20)-170}{70\times 0.45 +1} \\
>  &=-2.2 \text{ mmol/L for each 1L of IVF}
> \end{align}
> $$
> 
> To reduce her sodium by 5 mmol/L over 12 hours, we would therefore need to give $\frac{5}{2.2}\approx 2.3\text{ L}$ of fluid. To account for ongoing losses via diarrhoea, we might want to give another 1 L resulting in a total of 3.3 L over 12 hours giving an infusion rate of 275 mL/hr


> [!Example]
> A 45 year old 75kg man with diabetes insipidus presents tot he hospital after 4 days of worsening abdominal pain and fever. He is in early shock with HR 115, BP 85/55, creatinine of 140 and undetectable JVP. His serum sodium on presentation is 165 mmol/L. What is the appropriate IV fluid therapy?
> - Bolus of isotonic fluid to restore haemodynamics (e.g. MAP > 60 mmHg, urine output > 30 mL/hr) ⇒ 1 L normal saline every 30 minutes x 4 L
> - Appropriate fluid in diabetes insipidus is glucose 5%
> - Calculate the expected sodium change per litre of glucose 5%:
> $$
> \frac{(0-0)-165}{75\times 0.5 + 1}=-4.3 \text{ mmol/L for each 1L of IVF}
> $$
> To reduce sodium by 5 mmol/L over 12 hours, we therefore need to give $\frac{5}{4.3}=1.2 \text{ L}$ of fluid. To account for ongoing losses due to DI, we might want to give another 2L, for a total of 3.2 L over 12 hours which is approximately 260 mL/hr
> - We can therefore give both fluids simultaneously or give the boluses of normal saline first then the glucose 5%

- Alternatively and much easily use the [free water calculator on MDCalc](https://www.mdcalc.com/calc/113/free-water-deficit-hypernatremia) making sure to plugin in an appropriate desired sodium target (i.e. 10 mmol/24 hours)
	1. Assess volume status and resuscitate appropriately with normal saline
	2. Establish acute vs chronic to determine rate (acute ≈ 1 mmol/L/hr and chronic < 24 mmol/L over 24 hours); when in doubt assume chronic
	3. Set a safe 24-hour target sodium (i.e. in chronic $\text{Target Na}=\text{Current Na}-10$)
	4. Use this as the sodium desired value in the above calculator in MDCalc
	5. Divide this volume by 24 hours to get the mL/hr of pure free water
	6. Add maintenance and ongoing free water losses 
		- Insensible losses (skin + respiratory) is roughly 0.5-1 mL/kg/hr and are electrolyte free so also contribute to hypernatraemia
			- Add 10% per °C above 37°C for fever, and more for tachypnoea, burns, open abdomen or unhumidified ventilation
		- Determine the electrolyte free water clearance by the kidney $\text{EFWC}=V_{\text{urine}}\times (1-\frac{\ce{Na+_{\text{urine}} + K+_{\text{urine}}}}{\ce{Na+_{\text{serum}}}}$
			- A positive EFWC is the volume of pure water the kidney is dumping per unit time and should be matched by the IVF replacement
		- Do not add isotonic losses to this (e.g. GI output, drain fluid, blood)
	7. Adjust this for the fluid’s actual free-water fraction: 5% dextrose = 1.0 (rate unchanged), 0.45% saline = 0.5 (double it), 0.18–0.225% saline = ~0.75. This gives the volume of _that fluid_ to run
		- $\text{Free Water Fraction}=1-\frac{\ce{Na+}_{\text{fluid}}+\ce{K+}_{\text{fluid}}}{154}$
		- For example, 2.8L of free water over 24h via 0.45% saline is $2.8/0.5 = 5.6 \text{ L}$ or 230 mL/hr
	8. Cross check with formula above
	9. Recheck sodium at 4-6 hours and titrate
# Sources
- Youtube Videos
	- [Hypernatremia - YouTube](https://www.youtube.com/watch?v=UuJXQdDFgoA&list=PLYojB5NEEakXVIAapcSEleP4doUdHVtld&index=3)
	- [Hypernatremia - Examples - YouTube](https://www.youtube.com/watch?v=Pls0fjsthlA&list=PLYojB5NEEakXVIAapcSEleP4doUdHVtld&index=4)
- Deranged Physiology: [Hypernatraemia](https://derangedphysiology.com/main/required-reading/electrolyte-disorders/Chapter-541/hypernatremia)