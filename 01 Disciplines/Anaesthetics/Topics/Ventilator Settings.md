---
date: 2026-04-19
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
---
> Part of: [[Mechanical Ventilation]]

- Mode
- Fraction of inspired oxygen $F_\text{i}\ce{O2}$
- Tidal volume ($V_{\text{T}}$)
- Respiratory rate (RR)
- Positive End-Expiratory Pressure (PEEP)
- Pressure Support (PS)
- Flow shape/contour
- Inspiratory:Expiratory (I:E) ratio

# Control Variables

- The variable which the ventilator uses as feedback signal for controlling inspiration
$$
P_{\text{vent}}+P_{\text{muscles}}=\text{elastance}\times \text{volume}+\text{resistance}\times \text{flow}
$$
- Flow cannot be a control variable because flow is a volume over time and thus when volume is controlled, flow is controlled indirectly
- **Pressure control** maintains a stable pressure in the face of fluctuating respiratory performance, which prevents lung injury from excess pressure but doesn't give a consistent minute ventilation
	- Advantages
		- Increased mean airway pressure ⇒ improves oxygenation
		- Increased duration of alveolar recruitment ⇒ square pressure waveform causes alveoli to open earlier and remain open for longer allowing for better gas exchange
		- Prevents excessive airway pressures thereby protecting against barotrauma
		- Avoids regional alveolar overdistention
		- May lead to earlier liberation from mechanical ventilation
		- Allows for significant air leak (e.g. during bronchoscopy or bronchopleural fistula)
	- Disadvantages
		- Tidal volume is variable and dependent on respiratory compliance
		- Uncontrolled volume may result in "volutrauma" (overdistension)
		- A high early inspiratory flow may breach the pressure limit if airway resistance is high

![[Pasted image 20260419203246.png]]

![[Pressure control modes of ventilation 2.jpg]]

- **Volume control** gives a more stable minute ventilation, keeping $P_\text{a}\ce{CO2}$ at the desired level
	- Advantages:
		- Guaranteed tidal volumes produces a more stable minute volume
		- The minute volume remains stable over a range of changing pulmonary characteristics
		- The initial flow rate is lower than in pressure-controlled modes, avoiding a high resistance-related early pressure peak
	- Disadvantages:
		- The mean airway pressure is lower with volume control ventilation
		- Recruitment may be poorer in lung units with poor compliance
		- In the presence of a leak, the mean airway pressure may be unstable
		- Insufficient flow may give rise to patient-ventilator dyssynchrony
![[Pasted image 20260419203227.png]]

![[volume controlled mode of ventilation.jpg]]

# Targeting Scheme
- **Set point:** the ventilator will try to achieve the parameter (control variable chosen)
- **Dual targeting:** the ventilator switches from targeting one control variable to another in the middle of the breath
	- For example a breath may start with a pressure control variable using a decelerating flow waveform, then reach the pressure limit mid breath and change to volume control until the target volume is reached
- **Adaptive targeting:**
	- For example in PRVC, the inspiratory pressure is automatically adjusted to achieve an average tidal volume target; this varies from breath to breath adapting to the changing compliance (guarantees a prescribed volume while maintaining a square pressure waveform)

# Phase Variables

## Trigger Variable

- Determines when a breath is delivered, distinguishing 'mandatory' and 'spontaneous' modes of ventilation
- Sensitivity affects:
    - Work of breathing
    - Patient-ventilator synchrony

### Time Triggered

- Mandatory ventilation
- Guarantees a minute volume offering predictable $\ce{CO2}$ removal and decreased work of breathing
- Less comfortable and sedation requirements are higher

### Flow Triggered

- Patient effort changes circuit flow
- Most comfortable but can be over-sensitive leading to dyssynchrony
- Ventilation is triggered when flow is diverted to the patient when the patient begins inspiration
	- The exact threshold value can be altered but is generally 1-2 L/min[^1]
- Some machines indicate spontaneous respiratory effort by colouring the waveform

![[pink indicator for patient-triggered breaths (SERVO-i).jpg]]

- Advantages:
	- Generally quite sensitive meaning that patient's work of breathing is not wasted on triggering the ventilator
	- Allows the patient to have control over their minute volume
	- May decrease the work of breathing
	- More comfortable
	- Permits a lower level of sedation
- Disadvantages:
	- May be too sensitive, giving rise to auto-triggering (this is probably the only use case for pressure trigger)
	- Does not guarantee a minute volume — therefore unsuitable for patients with a diminished or unreliable respiratory drive

### Pressure Triggered

- Patient generates negative pressure
- A typical pressure trigger threshold would be 1 cm $\ce{H2O}$

![[Pressure triggering diagram.jpg]]

- Disadvantages
	- Requires more effort to trigger the ventilator
	- Represents a wasted respiratory effort
	- Less comfortable for the patient
- Use cases
	- Can be used to decrease auto-triggering (e.g. circuit leak, bronchopleural fistula or hyperdynamic circulation)
	- Can be used to test the power of respiratory musculature in the context of an assessment of readiness for extubation (e.g. a patient who is able to trigger the ventilator by generating a negative intrathoracic pressure of -20 cm $\ce{H2O}$ is unlikely to fail extubation due to weakness of their respiratory muscles)

### Shape-Signal Triggering

- May decrease wasted effort by "predicting" the next respiratory effort but not widely available

![[shape signal triggering.jpg]]

## Limit/Target Variable

- Refers to the maximum value a variable can reach during inspiration but importantly, it does not end inspiration
- Common limit variables include pressure, flow and volume
	- For example, continue holding this pressure or flow value (don't exceed it) during the rest of inspiration

![[ventilator waveforms with different limit variables.jpg]]

## Cycling Variable

### Time-Cycled

- Feature of mandatory modes
- Usually set by setting a respiratory rate and the I:E ratio
- Advantages:
	- **Careful control of minute volume**, with obvious advantages for scenarios where tight PaCO2 control is desirable (e.g. traumatic brain injury)
	- **Ventilation is unaffected by changes in lung compliance or airway resistance** because the timing of the breath is unrelated to any respiratory system parameters
	- **Minute ventilation is not affected by an unreliable respiratory drive**, making this method suitable for paralysed or deeply unconscious patients
- Disadvantages:
	- Unsuitable for lightly sedated and awake patients
	- May result in patient-ventilator dyssynchrony particularly if the patient tries to exhale before the cycle time runs out

![[pressure waveform change with active expiratory effort.jpg]]

### Flow Cycled

- The ventilator cycles into the expiratory phase once the flow has decreased to a predetermined value during inspiration
	- Can be expressed as a fixed value in litres per minute or a percentage fraction of the peak flow rate

![[flow-cycled ventilation.jpg]]

- In patients with **restrictive lung disease** (poor compliance), flow rate drops quickly → lower tidal volumes
- In patients with **emphysema** (high compliance), flow rate drops slowly → higher tidal volumes
- Advantages:
	- More comfortable for the patient
	- Limited by changes in lung compliance and airway resistance, preventing inadvertent ventilator-induced lung injury
- Disadvantages
	- Tidal volumes may be poor in patients with poor lung compliance, resulting in inadequate minute volume
	- Patient comfort depends on intelligent settings; inappropriately low or high settings could result in uncomfortably deep inspiration or "double triggering"

### Pressure Cycled

- Largely obsolete in the modern era
- Advantages: Safety from pressure-related lung injury; decelerating ramp flow pattern; compliance determines cycling
- Disadvantages: Volume is determined by compliance; respiratory rate may fluctuate; may increase respiratory effort; pressure cannot also be a control variable

### Volume Cycled

- Largely obsolete in the modern era
- Inspiratory phase ends when the specified volume has been delivered
- Major disadvantage: propensity to generate high peak airway pressures when lung compliance decreases

---

## Fraction of Inspired Oxygen $F_\text{i}\ce{O2}$

- $F_\text{i}\ce{O2}$ should be titrated to the lowest value which still maintains adequate oxygenation
- In common practice, set at 100% after the patient is first intubated, then titrated downward over one to several hours as indicated by pulse oximetry and/or serial ABGs
- $F_\text{i}\ce{O2} > 60\%$ leads to oxygen toxicity; if adequate oxygenation requires $F_\text{i}\ce{O2}>60\%$, additional strategies are required:
	- ↑ PEEP
	- Recruitment manoeuvres
	- Trial of a different mode

## Tidal Volume $V_{\text{T}}$

- The tidal volume is 7 mL/kg in a normally breathing patient
- Most applicable to volume cycled modes (AC, SIMV)
- Initial values should be weight based:

| Patient | $V_{\text{T}}$ |
| --- | --- |
| Healthy lungs (e.g. neurological catastrophe, drug overdose) | 10 mL/kg IBW |
| COPD | 8 mL/kg IBW |
| ARDS | 6 mL/kg IBW |

- Higher $V_{\text{T}}$ leads to ↓ $P_\text{a}\ce{CO2}$, ↑ pH and ↑ $P_{\text{plateau}}$ and vice versa

## Respiratory Rate

- Typical respiratory rate is 10-20 breaths/min in order to provide 7-10 L/min of minute ventilation
- The normal resting minute volume is 70-100 mL/kg/min; therefore to produce tidal volumes of 6-8 mL/kg, a respiratory rate of between 12-16 breaths per minute
- Higher RR leads to ↓ $P_\text{a}\ce{CO2}$, ↑ pH and higher risk of auto-PEEP and vice versa

## Positive End-Expiratory Pressure

- Continuous positive pressure present throughout all of ventilation
- Physiologic effects:
	- ↑ oxygenation
		- ↑ alveolar recruitment
		- ↑ alveolar surface area
	- ↑ cardiac output in CHF patients but can ↓ BP in non-CHF patients
		- ↓ preload
		- ↓ LV afterload
	- ↑ RV afterload → ↑ R-L shunts if present

$$
\ce{O2}\ \text{Delivery}\propto S_\text{a}\ce{O2}\times[\ce{Hb}]\times \text{Cardiac Output}
$$

<figure style="text-align: center;">
  <img src="Pasted image 20260328170450.png" width="75%">
  <figcaption><b>Figure 5.</b> Relationship between oxygen delivery and PEEP. There exists a sweet spot where an optimal PEEP delivers optimised oxygen delivery</figcaption>
</figure>

- In clinical practice: PEEP is set to the lowest value that allows $F_\text{i}\ce{O2}$ to be ≤ 60% with a minimum value of 5 cm of $\ce{H2O}$
- The healthy lung should be ventilated with 5-8 cm of $\ce{H2O}$ of PEEP
- ARDS patients will require higher PEEP (usually > 12 cm of $\ce{H2O}$)
- With bronchospasm, low PEEP or zero PEEP (ZEEP) is often warranted (< 5 cm of $\ce{H2O}$)

## Pressure Support

- Amount of additional positive pressure beyond PEEP that is provided during inspiration. Important in PSV, BiPAP and almost always used in SIMV
- Simple estimate of optimal PS is:
$$
PS_{\text{optimal}}\approx P_{\text{plateau}}-\text{PEEP}
$$
- However in practice, PS is typically set to twice PEEP

## Flow Shape/Contour

- Describes the pattern of airflow during inspiration; set in volume-targeted ventilator modes
	- Always decelerating shape in pressure-targeted modes as a consequence of lung mechanics

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
  <figure style="text-align: center;">
    <img src="Pasted image 20260328171020.png" style="width: 100%;">
    <figcaption><b>Figure 6.</b> Decelerating flow contour</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="Pasted image 20260328171034.png" style="width: 100%;">
    <figcaption><b>Figure 7.</b> Constant flow contour</figcaption>
  </figure>
</div>

| Contour | $P_{\text{peak}}$ | $P_{\text{mean}}$ | Dead space ($V_{\text{D}}$) | Auto-PEEP |
| --- | --- | --- | --- | --- |
| Decelerating | ↓ | ↑ | ↓ | More |
| Constant | ↑ | ↓ | ↑ | Less |

## Inspiratory : Expiratory Ratio

- Ratio between the amount of time spent in inspiration and expiration
- Normal I:E ratio is 1:2; deviations from this are uncomfortable, often requiring deep sedation

| Change | Effects |
| --- | --- |
| ↑ Inspiratory time | ↑ Mean airway pressure → better oxygenation (but ↓ CO₂ clearance, ↑ haemodynamic instability, ↑ gas trapping) |
| ↑ Expiratory time | ↑ CO₂ clearance → better ventilation (but ↑ probability of atelectasis) |

- In AC and SIMV: usually set indirectly via $V_{\text{T}}$ and flow rate/pattern
- In PCV: usually set directly
- In PSV: generally outside of clinician control
- A higher ratio (higher inspiratory time) results in ↑ $P_{\text{mean}}$ and higher risk of auto-PEEP and vice versa

![[an example of an inspiratory phase which is too long.jpg]]

# Typical Initial Ventilator Settings

| Option | Typical Settings |
| --- | --- |
| **Mode** | Intrinsic hyperventilation → SIMV; No intrinsic hyperventilation → AC or SIMV |
| **FiO₂** | Start at 100%; Taper as able to 35–60% to keep $P_\text{a}\ce{O2}$ >60–80 mmHg |
| **Tidal Volume ($V_{\text{T}}$)** | ~10 cc/kg normal; ~8 cc/kg COPD; ~6 cc/kg ARDS _(Use IBW)_; Lower $V_{\text{T}}$ if $P_{\text{plateau}}$ > 30 cm $\ce{H2O}$ |
| **Rate** | 10–20 breaths/min to achieve MV of 7–10 L/min; adjust based on pH |
| **PEEP** | Start at 5 cm $\ce{H2O}$; Titrate up if $P_\text{a}\ce{O2}$ <60 on >60% FiO₂; May start with no PEEP in pure hypoventilation |
| **Pressure Support** _(n/a for AC)_ | 5–20 cm $\ce{H2O}$; Optimal $\text{PS} \approx P_{\text{plateau}} - \text{PEEP}$; _(Minimum 5 cm $\ce{H2O}$ PS always to overcome ETT resistance)_ |

# Typical Initial Ventilator Alarm Settings

- **High pressure limit:** 10–15 cm H₂O above PIP
- **Low pressure limit:** 5–10 cm H₂O below PIP
- **Low PEEP limit:** 3–5 cm H₂O below set PEEP
- **Low exhaled tidal volume:** 100 mL or 50% below set VT
- **Low minute ventilation:** 2–5 L/min or 50% below baseline
- **High minute ventilation:** 50% above baseline
- **FiO₂ alarm:** ±5% from set oxygen concentration
- **Temperature alarm:** ±2°C from set temperature
- **Apnea delay:** About 20 seconds

[^1]: Normal mean inspiratory flow rate at rest is around 15 L/min with a peak of around 30-35 L/min
