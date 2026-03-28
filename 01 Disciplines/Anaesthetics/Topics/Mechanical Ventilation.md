---
date: 2026-03-28
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
figureCount: 8
---
# Lung Mechanics
## Definitions
$$\dot{V}=V_\text{T}\times\text{Respiratory Rate}$$
- Where:
	- $\dot{V}$ is the minute ventilation
	- $V_\text{T}$ is the tidal volume
$$\dot{V}_\text{A}=\left(V_\text{T}-V_\text{D}\right)\times\text{Respiratory Rate}$$
- Where:
	- $\dot{V}_\text{A}$ is the alveolar ventilation
	- $V_\text{D}$ is the physiologic dead space
$$\text{Compliance}=\frac{\Delta\ \text{Volume}}{\Delta\ \text{Pressure}}$$
$$Q=\frac{\Delta\ P}{R}$$
- Where
	- $Q$ is airflow
	- $\Delta\ P$ is pressure gradient
	- $R$ is airway resistance
$$\text{Ventilation Pressure}=\text{Resistive Pressure}+\text{Elastic Pressure}$$
- Where
	- Resistive pressure is the pressure required to push airflow through the airways
	- Elastic pressure which is the pressure required to inflate lungs and chest wall

## Monitoring
$$P_\text{Peak}\propto\frac{\text{Airway Resistance}}{\text{Compliance}}$$
$$P_\text{Plateau}\propto\frac{1}{\text{Compliance}}$$
$$R_\text{insp}=\frac{P_\text{peak}-P_\text{plateau}}{Q_\text{end inspiratory}}$$
- An increasing $P_\text{peak}$ in the abscence of an increasing $P_\text{pleateau}$ suggests airway resistance is increasing (e.g. bronchospasm, excessive scretions, mucous plug, foreign body aspiration, extrinsic airway compression)
$$\text{Compliance}=\frac{V_\text{T}}{P_\text{pleateau}-\text{PEEP}}$$
- An increasing $P_\text{pleateau}$ suggests compliance is decreasing (e.g. pulmonary oedema, pleural effusion, pneumothorax, right mainstem bronchus intubation, ascites or other abdominal distension)


| $P_\text{peak}$ | $P_\text{pleateau}$ | Likely problem              |
| --------------- | ------------------- | --------------------------- |
| Increased       | Normal              | Increased airway resistance |
| Increased       | Increased           | Decreased lung compliance   |
# Gas Exchange
## Normal Gas Exchange
- Alveolar ventilation equation

$$
P_\text{a}\ce{CO2}=\frac{\dot{V}\ce{CO2}\times P_{\text{I}}}{\dot{V}_{\text{A}}}
$$

- Where
	- $P_\text{a}\ce{CO2}$ is the partial pressure of $\ce{CO2}$ in arterial blood
	- $\dot{V}\ce{CO2}$ is the rate of systemic $\ce{CO2}$ production
	- $P_{\text{I}}$ is the pressure of inspired air
	- $\dot{V}_{\text{A}}$ is the alveolar ventilation
- Importantly $P_\text{a}\ce{CO2}\propto \frac{1}{\dot{V}_{\text{A}}}$
 
| Mechanism                                      | Examples                                    |
| ---------------------------------------------- | ------------------------------------------- |
| VQ mismatch                                    | Pneumonia, PE, pulmonary oedema, COPD       |
| Shunt                                          | Congenital heart disease, pulmonary AVM     |
| Thickening of the alveolar-capillary membrane  | Interstitial lung disease, pulmonary oedema |
| Destruction of the alveolar capillary membrane | Emphysema                                   |
## Monitoring
- [[Blood Gas Interpretation|ABG Interpretation]]
- Pulse oximetry
- Capnography
	- Note that $P_\text{a}\ce{CO2}\approx P_{\text{ET}}\ce{CO2}+3.5 \pm 1.5$
		- However, the gap can be
			- Increased to >5 mmHg in low cardiac output, COPD, PE, advanced age
			- Decreased to <2 mmHg in high cardiac output states (e.g. septic shock)
# Non-Invasive Ventilation
## CPAP
- Maintains alveolar recruitment and improves pulmonary shunting
- Improves predominantly oxygenation and therefore indicated in type 1 respiratory failure
## BiPAP
$$
\text{Pressure support (PS)}\approx \text{IPAP}-\text{EPAP}
$$
- S/T mode refers to spontaneous and timed mode and therefore has a backup rate
- S mode refers to spontaneous (only)
# Ventilator Modes
- Modes can be partially defined by:
	- Trigger variable: when to initiate a machine-driven breath. Common options include: time triggered, pressure triggered, flow triggered
	- Control variable: defines what aspect of inspiration is the primary variable controlled by the ventilator during inspiration. Common options include: pressure controlled, flow controlled (also known as volume controlled)
	- Cycling variable: defines what signals the ventilator to terminate inspiration. Common options include: volume cycled, flow cycled, time cycled. Uncommon options include: pressure cycled
## Assist Control (AC)
- Mix of mandatory and assisted breaths with all breaths, once triggered, are treated the same and have a consistent tidal volume
- Trigger: time, pressure or flow
- Control: flow (volume)
- Cycling: time

<figure style="text-align: center;">
  <img src="Pasted image 20260328150712.png">
  <figcaption><b>Figure 1.</b> Assist control. Note that the 1st, 3rd and 4th breaths are patient triggered with the second breath being time triggered.</figcaption>
</figure>

- Advantages
	- Guarantees a minimum minute ventilation
	- Low work of breathing
- Disadvantages
	- Can lead to respiratory alkalosis, auto-PEEP and hypotension in hyperventilating patients as every breath leads to a fully supported breath
- Indications
	- Critically ill patients requiring full ventilatory support and in whom fluctuations in $V_{\text{T}}$ is undesirable
## Synchronised Intermittent Mandatory Ventilation (SIMV)
- Mix of mandatory breaths (some of which are synchronised with spontaneous breaths), and assisted breaths
- Mandatory (non-synchronised breaths):
	- Trigger: time
	- Control: flow (volume)
	- Cycling: time
- Synchronised breaths:
	- Trigger: pressure or flow
	- Control: flow (volume)
	- Cycling: time
- Non-synchronised breaths
	- Trigger: pressure or flow
	- Control: pressure
	- Cycling: flow

<figure style="text-align: center;">
  <img src="Pasted image 20260328151410.png">
  <figcaption><b>Figure 2.</b> SIMV (with pressure support). Note that the first and fourth breaths are synchronised pressure triggerred fully supported breath with tidal volume set for ~600 mL. The second, third and fifth breaths are spontaneous non-synchronised breaths assisted with pressure support with 10 cm of water.</figcaption>
</figure>

- Advantage
	- Guarantees a minimum minute ventilation
	- Lower mean airway pressure when compared with AC
	- Can provide a wide range of respiratory support
- Disadvantages
	- Increased work of breathing for patient
	- ? Lower cardiac output in patients with LV dysfunction
- Indications
	- Critically ill patients who are hyperventilating or otherwise prown to auto-PEEP or high airway resistance

> [!NOTE]
> The main difference between SIMV and AC is that spontaneous breaths in excess of the set respiratory rate:
> - In AC receive full support
> - In SIMV receive partial support
> Therefore in a patient with no spontaneous breaths AC = SIMV

## Pressure Control Ventilation (PCV)
- Mandatory breaths only. The patient is unable to trigger the ventilator
- Trigger: time
- Control: pressure
- Cycling: time

<figure style="text-align: center;">
  <img src="Pasted image 20260328151929.png">
  <figcaption><b>Figure 3.</b> Pressure Control Ventilation. Inspiratory pressure is set at 25cm of water. Flow starts high with each breath and rapidly declines (known as a decelerating flow contour).</figcaption>
</figure>

- Advantages:
	- Prevents excessive airway pressures
	- Avoids regional alveolar overdistention
	- May lead to earlier liberation from mechanical ventilation
- Disadvantages
	- Very uncomfortable and requires deep sedation ± paralysis
	- Unable to guarantee a minimum minute ventilation
- Indications
	- Patients who are at a particularly high risk of barotrauma
## Pressure Support Ventilation (PSV)
- There are no mandatory breaths; every breath must be triggered by the patient
- Trigger: Pressure or flow
- Control: Pressure
- Cycling: Flow

<figure style="text-align: center;">
  <img src="Pasted image 20260328152917.png">
  <figcaption><b>Figure 4.</b> Pressure support ventilation. The pressure support is set at ~15cm of water. Inspiration is terminated by the removal of pressure support once the flow drops to 25% of its maximum</figcaption>
</figure>

- Advantages:
	- Probably the most comfortable mode for the awake, conscious patient
- Disadvantages:
	- Patient must trigger each breath
	- A minimum minute ventilation cannot be guaranteed
	- Associated with poorer quality sleep
	- Generally incapable of providing full ventilatory support
- Indications
	- Conscious patient
	- As a stepping stone immediately prior to extubation
# Dual Control modes
- Use instantaneous feedback to control aspects of lung volume and airway pressure simultaneously
- Examples include
	- Pressure-regulated volume control
	- Volume support
	- Volume assured pressure support
# Ventilator Options
- Mode
- Fraction of inspired oxygen $F_\text{i}\ce{O2}$
- Tidal volume ($V_{\text{T}}$)
- Respiratory rate (RR)
- Positive End-Expiratory Pressure (PEEP)
- Pressure Support (PS)
- Flow shape/contour
- Inspiratory:Expiratory (I:E) ratio
## Fraction of Inspired Oxygen $F_\text{i}\ce{O2}$
- $F_\text{i}\ce{O2}$ should be titrated to the lowest value which still maintains adequate oxygenation
- In common practice, it is set at 100% after the patient is first intubated, and then titrated downward over one to several hours as indicated by pulse oximetry and/or serial ABGs
- $F_\text{i}\ce{O2} > 60\%$ leads to oxygen toxicity in the lungs, therfore if adequate oxygenation requires $F_\text{i}\ce{O2}>60\%$, additional strategies are required:
	- ↑ PEEP
	- Recruitment manoeuvres
	- Trial of a different mode
## Tidal Volume $V_{\text{T}}$
- Most applicable to volume cycled modes (AC, SIMV)
- Initial values should be weight based with:
	- Healthy lungs 10mL/kg of ideal body weight (as in neurological catastrophy, drug overdose)
	- COPD 8mL/kg
	- ARDS 6mL/kg
- Higher $V_{\text{T}}$ leads to ↓ $P_\text{a}\ce{CO2}$, ↑ pH and ↑ $P_{\text{plateau}}$ and vice versa
## Respiratory Rate
- Typical respiratory rate is 10-20 breaths/min in order to provide 7-10 L/min of minute ventilation
- Higher RR leads to ↓ $P_\text{a}\ce{CO2}$, ↑ pH and higher risk of auto-PEEP and vice versa
## Positive End-Expiratory Pressure
- Continuous positive pressure present throughout all of ventilation
- Physiologic effects:
	- ↑ oxygentation
		- ↑ alveolar recruitment
		- ↑ alveolar surface area
	- ↑ cardiac output in CHF patients but can ↓ BP in non CHF patients
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

 - In clinical practice: PEEP is set to the lowest value that allows F$\ce{O2}$ to be ≤ 60% with a minimum value of 5 cm of $\ce{H2O}$
## Pressure Support
- Amount of additional positive pressure beyond PEEP that is provided during inspiration. Important in pressure support ventilation, BiPAP and almost always used in SIMV
- Simple estimate of optimal PS is:
$$
PS_{\text{optimal}}\approx P_{\text{plateau}}-\text{PEEP}
$$
- However in practice, PS is typically set to twice PEEP
## Flow Shape/Contour
- Describes the pattern of airflow during inspiration and is set in volume-targeted ventilator modes
	- Always decelerating shape in pressure-targeted modes as a consequence of lung mechanics
- Options include:

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

- Decelerating flow contour results in:
	- ↓ $P_{\text{peak}}$
	- ↑ $P_{\text{mean}}$
	- ↓ $V_{\text{D}}$
- Constant flow contour results in:
	- ↑ $P_{\text{peak}}$
	- ↓ $P_{\text{mean}}$
	- Less auto-PEEP
## Inspiratory : Expiratory Ratio
- Ratio between the amount of time spent in inspiration and the amount of time spent in expiration
- In AC and SIMV it is usually set indirectly via $V_{\text{T}}$ and flow rate/pattern
- In PCV it is usually set directly
- In PSV it is generally outside of clinician control
- A higher ratio (higher inspiratory time) results in ↑ $P_{\text{mean}}$ and higher risk of auto-PEEP and vice versa
## Typical Initial Ventilator Settings
| Option                              | Typical Settings                                                                                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mode**                            | Intrinsic hyperventilation → SIMV  <br>No intrinsic hyperventilation → AC or SIMV                                                                                                           |
| **FiO₂**                            | Start at 100%  <br>Taper as able to 35–60% to keep PaO₂ >60–80 mmHg                                                                                                                         |
| **Tidal Volume (V_T)**              | ~10 cc/kg for normal patients  <br>~8 cc/kg for COPD  <br>~6 cc/kg for ARDS  <br>_(Use ideal body weight)_  <br>Adjust as needed based on pH; consider lowering V_T if P_plateau > 30 cmH₂O |
| **Rate**                            | 10–20 breaths/min to achieve MV of 7–10 L/min; adjust based on pH                                                                                                                           |
| **PEEP**                            | Start at 5 cmH₂O  <br>Titrate up if PaO₂ <60 on >60% FiO₂  <br>May start with no PEEP in pure hypoventilation                                                                               |
| **Pressure Support** _(n/a for AC)_ | 5–20 cmH₂O  <br>Optimal PS ≈ P_plateau − PEEP  <br>_(Minimum 5 cmH₂O PS always to overcome ETT resistance)_                                                                                 |
# Lung Protective Ventilation
## Ventilator Associated Lung Injury
- Most frequently complicates ALI and [[Acute Respiratory Distress Syndrome|ARDS]] 
- Types include
	- Barotrauma: caused by excessively airway pressures
	- Volutrauma: caused by excessive $V_{\text{T}}$
	- Biotrauma
	- Cyclic atelactasis
- Oxygen toxicity
	- For patient on bleomycin, oxygen toxicity can occur at lower $F_\text{i}\ce{O2}$
### Barotrauma
- Manifestations
	- Pneumothorax
	- Pneumomediastinum
	- Subcutaneous emphysema
	- Systemic gas embolism
	- Cystic barotrauma
- Risk factors
	- High $P_{\text{plateau}}>32.5\pm 2.5\ \text{cm}\ \ce{H2O}$
	- High minute ventilation
	- Non-homogenous parenchymal disease (e.g. ARDS)
	- Necrotising lung pathology
	- Secretion retention
### Biotrauma
- Release of proinflammatory cytokines in response to supranormal intraalveolar pressures; occurs in the absence of physical damage to lung architecture (as in barotrauma)
- Most clinically relevant manifestation is that of pulmonary and interstitial oedema
## Protective
- Principle feature is low tidal volumes
- Permissive hypercapnoea: $P_\text{a}\ce{CO2}$ is allowed to climb , with a resulting drop in arterial pH
	- Contraindicated in increased ICP, haemodynamic instability, right heart failure, severe metabolic acidosis
- Open lung ventilation
	- Strategy that combines: low tidal volumes and high PEEP
## Protocol for ARDS
1. Choose ventilation mode (typically AC or SIMV)
2. Start with $V_{\text{T}}$ of 6mL/kg of IBW
3. Start with PEEP at ≥ 8cm $\ce{H2O}$
4. Set the I:E ratio of 1:2
5. Measure and record $P_{\text{pleateau}}$ every 4 hours and after any changes in $V_{\text{T}}$ or PEEP
	- If $P_{\text{pleateau}}$ >30 cm $\ce{H2O}$, ↓ $V_{\text{T}}$ in 1mL/kg increments until $P_{\text{plateau}}$ ≤30 cm $\ce{H2O}$ or to minimum of 4mL/kg IBW
	- If $V_{\text{T}}$ < 6mL/kg IBW and $P_{\text{plateau}}$ <25 cm $\ce{H2O}$, ↑ $V_{\text{T}}$ by 1mL/kg IBW increments to a max of 6mL/kg
6. Adjust the RR and $V_{\text{T}}$ according to pH goals:
	- If pH <7.30, consider ↑ RR to as high as 35 breaths/min while monitoring for development of auto-PEEP
	- If pH <7.15 and RR ≥ 35 breaths/min, consider ↑ $V_{\text{T}}$ and suspending $P_{\text{plateau}}$ limit
7. Adjust I:E ratio to avoid auto-PEEP and dysynchrony
8. Adjust PEEP to maximise alveolar recruitment while avoiding over-distention:
	- ↑ or ↓ PEEP in increments of 2-3 cm of $\ce{H2O}$
	- Select PEEP that gives the best compliance
9. Adjust the fi$\ce{O2}$ to achieve $S_\text{p}\ce{O2}$ of 88-95% and/or $P_\text{a}\ce{O2}$ of 55-80 mmHg
# Physiological Consequences
## Affects on Gas Exchange
- At low and medium levels of PEEP, it leads to improved alveolar recruitment which leads to larger surface area for gas diffusing
- At high levels of PEEP, alveolar dead space increases dramatically
	- Occurs because PEEP has a greater effect on normal compliant alveoli than it does on stiff/fluid filled alveoli. This means that at high PEEP, healthy alveoli become overdistended, thereby increasing resistance to blood flow to these units, shunting blood towards poorly ventilated, abnormal alveoli. This increases physiologic dead space, worsening V/Q mismatch
<figure style="text-align: center;">
  <img src="Pasted image 20260328195659.png" width="75%">
</figure>

- High PEEP can also increase pulmonary vascular resistance which can worsen intracardiac R-L shunts
## Affects on Haemodynamics
- Preload
	- PEEP can decrease preload because:
		- ↑ CVP → ↓ venous return to RA
		  ↑ RV afterload → ↓ blood exiting RV
		- ↑ RV afterload → leftward displacement of the IV septum → impairs LV diastolic filling
$$
\underset{\text{AKA afterload}}{\text{LV Wall Tension}}\approx \frac{P_{\text{transmural}}\times R}{\text{LV wall thickness}}
$$

# Source
- Strong Medicine Playlist: [Mechanical Ventilation - YouTube](https://www.youtube.com/playlist?list=PLBA5A30910F1FBF47)