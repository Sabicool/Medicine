---
date: 2026-04-14
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
figureCount: 18
---
![[Pasted image 20260329010927.png]]
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
$$
Q=\frac{V}{T}
$$
$$
P=Q\times R
$$
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
## Phases of Mechanical Ventilation
- Four distinct phases, each of which has a governing variable which determines how that phase proceeds:
	- Initiate phase controlled by the trigger variable
	- Inspiratory phase controlled by the limit variable
	- Cycling phase controlled by the cycle variable
	- Expiratory phase governed by the PEEP variable; the patient exhales passively

![[Pasted image 20260404113909.png|697]]


## Monitoring
![[Pasted image 20260329183832.png]]

$$P_\text{Peak}\propto\frac{\text{Airway Resistance}}{\text{Compliance}}$$
$$P_\text{Plateau}\propto\frac{1}{\text{Compliance}}$$
$$R_\text{insp}=\frac{P_\text{peak}-P_\text{plateau}}{Q_\text{end inspiratory}}$$
- An increasing $P_\text{peak}$ in the absence of an increasing $P_\text{pleateau}$ suggests airway resistance is increasing (e.g. bronchospasm, excessive secretions, mucous plug, foreign body aspiration, extrinsic airway compression)
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
- Ventilator modes are just pre-set combinations of ventilator settings
- Generally classified according to their major characteristics:
	- The control variable: pressure vs. volume
	- Breath sequence: spontaneous vs. mandatory
	- Targeting scheme: set point, dual targeting, servo control, adaptive etc.
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

![[SIMV.jpg]]

- User sets a rate and volume 
- There is a window of opportunity around each timed breath, during which a patient effort will be converted into a mandatory breath
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
## Pressure Regulated Volume Control
- The user sets a target tidal volume (as in volume control modes)
- The ventilator performs an assessment of the dynamic lung compliance over the course of three initial calibrating breaths
- Using this data, it then determines the appropriate pressure level required to achieve the prescribed tidal volume
- Advantages:
	- Square pressure waveform favours early and sustained lung unit recruitment
	- Mean airway pressure is as high as with PCV
	- Pressure is minimised for any given prescribed tidal volume
	- A minute volume is guaranteed, preserving a degree of control over PaCO2
# Ventilator Options
- Mode
- Fraction of inspired oxygen $F_\text{i}\ce{O2}$
- Tidal volume ($V_{\text{T}}$)
- Respiratory rate (RR)
- Positive End-Expiratory Pressure (PEEP)
- Pressure Support (PS)
- Flow shape/contour
- Inspiratory:Expiratory (I:E) ratio
## Control Variables
- The variable which the ventilator uses as feedback signal for controlling inspiration
$$
P_{\text{vent}}+P_{\text{muscles}}=\text{elastance}\times \text{volume}+\text{resistance}\times \text{flow}
$$
- Flow cannot be a control variable because flow is a volume over time and thus when volume is controlled, flow is controlled indirectly
- Controlling the pressure variable is beneficial because it maintains a stable pressure in the face of fluctuating respiratory performance, which prevents lung injury from excess pressure but doesn’t give a consistent minute ventilation
	- Advantages
		- Increased mean airway pressure ⇒ improves oxygenation but not a massive advantage compared to PEEP until higher I:E ratios are used
		- Increased duration of alveolar recruitment ⇒ square pressure waveform causes alveoli to open earlier and remain open for longer allowing for better gas exchange
		- Prevents excessive airway pressures thereby protecting against barotrauma
		- Avoids regional alveolar overdistention
		- May lead to earlier liberation from mechanical ventilation
		- The pressure control variable allows for significant air leak (e.g. during bronchoscopy or while ventilating a patient with a bronchopleural fistula)
	- Disadvantages
		- Tidal volume is variable and dependent on respiratory compliance
		- Uncontrolled volume may result in “volutrauma“ (overdistension)
		- A high early inspiratory flow may breach the pressure limit if airway resistance is high

![[Pressure control modes of ventilation 2.jpg]]


- Controlling the volume variable gives a more stable minute ventilation, which keeps the $P_\text{a}\ce{CO2}$ at the desired level, but which may play havoc with respiratory system pressures
	- Advantages:
		- Guaranteed tidal volumes produces a more stable minute volume
		- The minute volume remains stable over a range of changing pulmonary characteristics.
		- The initial flow rate is lower than in pressure-controlled modes, i.e. it avoids a high resistance-related early pressure peak
	- Disadvantages:
		- The mean airway pressure is lower with volume control ventilation
		- Recruitment may be poorer in lung units with poor compliance.
		- In the presence of a leak, the mean airway pressure may be unstable.
		- Insufficient flow may give rise to patient-ventilator dyssynchrony

![[volume controlled mode of ventilation.jpg]]
## Targeting Scheme
- Set point: the ventilator will try to achieve the parameter (control variable chosen) (e.g. the pressure level in a pressure control mode of ventilation)
- Dual targeting: the ventilator switch from targeting one control variable to another in the middle of the breath
	- For example of breath may start with a pressure control variable using a decelerating flow away form, then reach the pressure limit mid breath and change to volume control until the target volume is reached
- Adaptive targeting:
	- For example in pressure regulated volume control mode, the inspiratory pressure is automatically adjusted to achieve an average tidal volume target; this varies from breath to breath adapting to the changing compliance (it guarantees a prescribed volume while maintaining a square pressure volume)
## Phase Variables

### Trigger Variable

- Determines when a breath is delivered distinguishing ‘mandatory’ and ‘spontaneous’ modes of ventilation
- Sensitivity affects:
    - Work of breathing
    - Patient-ventilator synchrony
#### Time Triggered
- Mandatory ventilation
- Guarantees a minute volume offering predictable $\ce{CO2}$ removal and decreased work of breathing
- Less comfortable and sedation requirements are higher
#### Flow triggered
- Patient effort changes circuit flow[^1]
- Most comfortable but can be over-sensitive leading to dyssynchrony
- Ventilation is triggered when flow is diverted to the patient when the patient begins inspiration
	- The exact threshold value can be altered but is generally 1-2 L/min[^2]
- Some machines indicate spontaneous respiratory effort by colouring the waveform

![[pink indicator for patient-triggered breaths (SERVO-i).jpg]]

- Advantages:
	- Generally quite sensitive meaning that patient’s work of breathing is not wasted on triggering the ventilator
	- Allows the patient to have control over their minute volume
	- May decrease the work of breathing
	- More comfortable
	- Permits a lower level of sedation
- Disadvantages:
	- May be too sensitive, giving rise to auto-triggering (this is probably the only use case for pressure trigger)
	- Does not guarantee a minute volume
		- Therefore unsuitable for patients with a diminished or unreliable respiratory drive
#### Pressure triggered 
- Patient generates negative pressure
- A typical pressure trigger threshold would be 1 cm $\ce{H2O}$
![[Pressure triggering diagram.jpg]]
- Disadvantages
	- Requires more effort to trigger the ventilator
	- Represents a wasted respiratory effort
	- Less comfortable for the patient
- Use cases
	- Can be used to decrease auto-triggering (e.g. circuit leak, bronchopleural fistula or hyperdynamic circulation)
	- Can be used to test the power of respiratory musculature, in the context of an assessment of readiness for extubation (e.g. a patient who is able to trigger the ventilator by generating a negative intrathoracic pressure of -20 cm $\ce{H2O}$ is unlikely to fail extubation due to the weakness of their respiratory muscles)
#### Shape-signal triggering
- May decrease wasted effort by “predicting” the next respiratory effort but not widely available
![[shape signal triggering.jpg]]
### Limit/Target Variable

- Refers to the maximum value a variable can reach during inspiration but importantly, it does not end inspiration
- Common limit variables include pressure, flow and volume
	- For example, continue holding this pressure or flow value (don’t exceed it) during the rest of inspiration
![[ventilator waveforms with different limit variables.jpg]]
### Cycling Variable
#### Time-Cycled
- Feature of mandatory modes
- Usually set by setting a respiratory rate and the I:E ratio
- Advantages:
	- **A careful control of minute volume can be achieved**, with obvious advantages for scenarios where tight PaCO2 control is desirable (eg. traumatic brain injury)
	- **Ventilation is unaffected by changes in lung compliance or airway resistance** because the timing of the breath is unrelated to any of the respiratory system parameters, instead being controlled by a timer
	- **Minute ventilation is not affected by an unreliable respiratory drive**, making this method suitable for paralysed or deeply unconscious patients
- Disadvantanges:
	- Unsuitable for likely sedated and awake patients
	- May result in patient-ventilator dyssynchrony particularly if the patient tries to exhale before the cycle time runs out
		- This appears as a pressurise at the end of inspiration either because the lung compliance has reached a point of a distinction or in spontaneously breathing patience, the patient had decided they want to exhale before the breath is over
![[pressure waveform change with active expiratory effort.jpg]]
#### Flow Cycled
- The ventilator cycles into the the expiratory phase once the flow has decreased to a predetermined value during inspiration
	- It can either be expressed as a fixed value in litres per minute or a percentage fraction of the peak flow rate achieved during inspiration
![[flow-cycled ventilation.jpg]]

- in patients with restrictive lung disease, their lungs have poor respiratory compliance and their flow rate will drop quickly; therefore their tidal volumes will be lower with flow cycling
- in patients with emphysema lung disease, their lungs will have high lung compliance and their flow rate to drop slowly; therefore there tidal volumes will be higher with flow cycling
- Advantages:
	- More comfortable for the patient (if the patient neesd to terminate a breath and exhale, the inspiratory flow ceases and the ventilator cycles to expiration rapidly)
	- Limited by changes in lung compliance and airway resistance and therefore prevents inadvertent ventilatory-induced lung injury (i.e. in poorly compliant lungs, the ventilator will cycle to expiration rather than continue to apply distending pressure)
- Disadvantages
	- Tidal volumes may be poor in patients with poor lung compliance, resulting in inadequate minute volume
	- Patient comfort depends on intelligent settings; inappropriately low and inappropriately high settings could result in uncomfortably deep and prolonged inspiration or "double triggering" due to insufficient inspiratory time and tidal volume
#### Pressure Cycled
- Largely obsolete in the modern era
- Advantages:
	- Safety from pressure-related lung injury
	- Decelerating ramp pattern for flow waveform which supposedly results in even distribution of gas in lung units
	- Compliance determines cycling
- Disadvantages
	- Volume is determined by compliance
	- Respiratory rate may fluctuate
	- May increase the respiratory effort (patent needs to exhale forcefully against the pressure valve to trigger expiration)
	- Pressure cannot be a control variable (duh)
#### Volume Cycled
- Largely obsolete in the modern era
- Inspiratory phase ends when the specified volume has been delivered
- Major disadvantage is related to safety as it has a propensity to generate high peak airway pressures when the lung compliance decreases
### Fraction of Inspired Oxygen $F_\text{i}\ce{O2}$
- $F_\text{i}\ce{O2}$ should be titrated to the lowest value which still maintains adequate oxygenation
- In common practice, it is set at 100% after the patient is first intubated, and then titrated downward over one to several hours as indicated by pulse oximetry and/or serial ABGs
- $F_\text{i}\ce{O2} > 60\%$ leads to oxygen toxicity in the lungs, therfore if adequate oxygenation requires $F_\text{i}\ce{O2}>60\%$, additional strategies are required:
	- ↑ PEEP
	- Recruitment manoeuvres
	- Trial of a different mode
### Tidal Volume $V_{\text{T}}$
- The tidal volume is 7 mL/kg in a normally breathing patient
- Most applicable to volume cycled modes (AC, SIMV)
- Initial values should be weight based with:
	- Healthy lungs 10 mL/kg of ideal body weight (as in neurological catastrophe, drug overdose)
	- COPD 8 mL/kg
	- ARDS 6 mL/kg
- Higher $V_{\text{T}}$ leads to ↓ $P_\text{a}\ce{CO2}$, ↑ pH and ↑ $P_{\text{plateau}}$ and vice versa
### Respiratory Rate
- Typical respiratory rate is 10-20 breaths/min in order to provide 7-10 L/min of minute ventilation
- The normal resting minute volume is 70-100 mL/kg/min; therefore to produce tidal volumes of 6-8 mL/kg, a respiratory rate of between 12-16 breaths per minute
- Higher RR leads to ↓ $P_\text{a}\ce{CO2}$, ↑ pH and higher risk of auto-PEEP and vice versa
### Positive End-Expiratory Pressure

- Continuous positive pressure present throughout all of ventilation
- Physiologic effects:
	- ↑ oxygenation
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
 - The healthy lung should be ventilated with 5-8 cm of $\ce{H2O}$ of PEEP
 - ARDS patients will require higher PEEP (usually > 12 cm of $\ce{H2O}$)
 - With bronchospasm, low PEEP or zero PEEP (ZEEP) is often warranted (< 5 cm of $\ce{H2O}$)
### Pressure Support

- Amount of additional positive pressure beyond PEEP that is provided during inspiration. Important in pressure support ventilation, BiPAP and almost always used in SIMV
- Simple estimate of optimal PS is:
$$
PS_{\text{optimal}}\approx P_{\text{plateau}}-\text{PEEP}
$$
- However in practice, PS is typically set to twice PEEP

### Flow Shape/Contour

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

### Inspiratory : Expiratory Ratio

- Ratio between the amount of time spent in inspiration and the amount of time spent in expiration
- The normal I:E ratio is 1:2 with deviations from this being uncomfortable, often requiring deep sedation
- Increased inspiratory time:
	- Advantages
		- Increases mean airway pressure  and favours better oxygenation
			- May paradoxically worsen due to changes in pulmonary blood flow; particularly in volume depleted patients
	- Disadvantages
		- Decrease $\ce{CO2}$ clearance
		- More haemodynamic instability 
		- Increased gas trapping
	- Uses
		- Situations where severe hypoxia is the primary problem and lung compliance is poor
			- Volume inspired is usually quite small with the period of air flow being short; therefore, there is often an inspiratory pause during the inspiratory phase, where the pressure level is maintained in the absence of any flow, with a close expiatory valve – a breath hold
![[an example of an inspiratory phase which is too long.jpg]]
- Increased expiratory time
	- Increases $\ce{CO2}$ clearance and favours better ventilation
	- Increases probability of atelactasis
- Inspiratory pause
	- The end-inspiratory positive airway pressure drives passive expiration 
	- Pressure loss during an inspiratory pause causes energy loss in the system
- In AC and SIMV it is usually set indirectly via $V_{\text{T}}$ and flow rate/pattern
- In PCV it is usually set directly
- In PSV it is generally outside of clinician control
- A higher ratio (higher inspiratory time) results in ↑ $P_{\text{mean}}$ and higher risk of auto-PEEP and vice versa

### Typical Initial Ventilator Settings

| Option                              | Typical Settings                                                                                                                                                                                                          |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mode**                            | Intrinsic hyperventilation → SIMV  <br>No intrinsic hyperventilation → AC or SIMV                                                                                                                                         |
| **FiO₂**                            | Start at 100%  <br>Taper as able to 35–60% to keep $P_\text{a}\ce{O2}$ >60–80 mmHg                                                                                                                                        |
| **Tidal Volume ($V_{\text{T}}$)**   | ~10 cc/kg for normal patients  <br>~8 cc/kg for COPD  <br>~6 cc/kg for ARDS  <br>_(Use ideal body weight)_  <br>Adjust as needed based on pH; consider lowering $V_{\text{T}}$ if $P_{\text{plateau}}$ > 30 cm $\ce{H2O}$ |
| **Rate**                            | 10–20 breaths/min to achieve MV of 7–10 L/min; adjust based on pH                                                                                                                                                         |
| **PEEP**                            | Start at 5 cm $\ce{H2O}$<br>Titrate up if $P_\text{a}\ce{O2}$ <60 on >60% FiO₂  <br>May start with no PEEP in pure hypoventilation                                                                                        |
| **Pressure Support** _(n/a for AC)_ | 5–20 cm $\ce{H2O}$<br>Optimal $\text{PS} \approx P_{\text{plateau}} - \text{PEEP}$  <br>_(Minimum 5 cm $\ce{H2O}$ PS always to overcome ETT resistance)_                                                                  |
- Typical initial ventilator alarm settings:
	- **High pressure limit:** 10–15 cm H₂O above PIP
	- **Low pressure limit:** 5–10 cm H₂O below PIP
	- **Low PEEP limit:** 3–5 cm H₂O below set PEEP
	- **Low exhaled tidal volume:** 100 mL or 50% below set VT
	- **Low minute ventilation:** 2–5 L/min or 50% below baseline
	- **High minute ventilation:** 50% above baseline
	- **FiO₂ alarm:** ±5% from set oxygen concentration
	- **Temperature alarm:** ±2°C from set temperature
	- **Apnea delay:** About 20 seconds
# Ventilator Waveform Interpretation
## Pressure Waveform
![[ventilator pressure waveform.jpg]]
### Peak Pressure
- High peak pressure suggests possibility of airway narrowing (e.g. ET tube being kinked, ventilator tubing being full of fluid or bronchospasm)
![[pressure ciurve high vs normal airway resistance.jpg]]
### Plateau Pressure
- Pressure int he lung after all flow has stopped and is directly related to the compliance of the lung parenchyma
$$
\begin{align*}
\text{Plateau Pressure}&=\frac{\text{Tidal Volume}}{\text{Static Compliance}} & \text{Static Pressure}&=\frac{\text{Tidal Volume}}{\text{Driving Pressure}} \\
\text{Driving Pressure} & = \text{Plateau Pressure}- \text{PEEP}
\end{align*}
$$

![[pressure curve high vs normal lung compliance.jpg]]
### Plateau Decay
- In an inspiratory pause, the pressure will gradually decrease from the initial plateau pressure; this occurs because of:
	- Elastic energy stored int he lung tissue and chest wall is dissipating
	- Lung units with different time constants are exchanging gas
	- Some of the gas is being absorbed into the pulmonary circulation
	- Some of the gas is leaking out of the circuit tubing
## Flow Waveform
![[ventilator flow waveform.jpg]]
### Maximum Flow
- In pressure control modes, the flow waveform is decelerating
	- A rapid deceleration of this flow indicates either that the lung compliance is poor or that airway resistance is high
### End-Inspiratory Flow
- If the end inspiratory flow is positive, then increasing inspiratory time will produce larger tidal volumes
### Peak Expiratory Flow
- The rate of expiratory flow is determined by the resistance of the airways and the elastic recoil of the lungs and chest wall
	- A low expiratory peak flow suggests there may be airway obstruction (e.g. bronchospasm) or an over-compliant chest wall
- If an expiratory flow is prolonged, the airway resistance must be increased
- If flow does not reach zero by the beginning of the next breath, there must be gas trapping

![[flow curves in increased airway resistance and gas trapping.jpg]]
## Pressure-Volume Loop

![[anatomy of the pressure-volume loop.jpg]]

- Above mode is mandatory with volume is the control variable and flow as constant
- Lower inflection point ($P_{\text{flex}}$) is the airway pressure which designates the critical opening pressure (takes more pressure to re-inflate a collapsed alveolus than it takes to distend a deflated one)
- Upper inflection point corresponds to the deflation of the most hyperinflated lung units 
### Idealised Pressure-Volume Loop of Volume-Controlled Ventilation
![[pressure-volume loop of an ideal CMV patient.jpg]]
### Idealised Pressure-Volume Loop of Pressure-Controlled Ventilation
![pressure-volume loop of an ideal PCV patient](https://www.derangedphysiology.com/main/sites/default/files/php/Respiratory-failure-and-mechanical-ventilation/images/pressure-volume%20loop%20of%20an%20ideal%20PCV%20patient.jpg)
### Realistic Pressure-Volume Loop of Pressure-Controlled Ventilation
![[pressure volume loop in SIMV-PRVC.jpg]]
### Changes with Respiratory Compliance
- As lungs decrease in compliance, in volume-controlled mode higher peak airway pressures will develop and a beaked region will develop indicating alveolar overdistention
![[influence of changes in lung compliance on the pressure-volume curve in CMV.jpg]]
- In pressure-controlled mode, the volume generated will decrease resulting in hypoventilation and hypercapnoea
![[influence of changes in lung compliance on the pressure-volume curve in PCV.jpg]]
### Air Leak
- With an air-leak in the circuit, the volume does not return to zero
![[pressure volume loop with a leak.jpg]]
### Patient-Ventilator Dyssynchrony
![[A pressure-volume loop with patient-ventilator dyssynchrony.jpg]]
## Pressure and Volume and Work of Breathing
$$
\begin{align*} 
W &= \int Fdx \\
W &= \int (P\cdot A)dx & \left( P=\frac{F}{A} \right) \\
W &= \int PdV  & (dV=Adx)\\
\end{align*}
$$
- Hence the work of breathing is the area to the left of the pressure-volume loop
- Anything that increases the convexity of the inspiratory curve or anything that pushes the whole loop to the right to the right increases the work of breathing

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
  <figure style="text-align: center;">
    <img src="work of breathing on a pressure-volume loop.jpg" style="width: 100%;">
    <figcaption><b>Figure 17.</b> Work of Breathing (normal)</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="work of breathing and intrinsic peep.jpg" style="width: 100%;">
    <figcaption><b>Figure 18.</b> Work of Breathing in asthma</figcaption>
  </figure>
</div>
# Intrinsic PEEP
![[expiratory hold manoeuvre.jpg]]
# Ventilation in Certain Pathological Processes
## Improving $\ce{CO2}$ Clearance
- Expiration is a passive process depending ont he pressure generated by the recoil of the chest wall and lung tissue and in the presence of significant airway resistance (e.g. [[Asthma Exacerbation]] or [[COPD Exacerbation]]) not enough pressure is generated to adequately empty the lung in reasonable amounts of time
- Decrease the I:E ratio (e.g. to 1:3 or 1:4):
	- Increases clearance of $\ce{CO2}$
	- Decreases gas trapping and auto-PEEP
	- Poorer oxygenation because of decreased mean airway pressure (although usually offset by intrinsic PEEP)
	- Decreased haemodynamic impact of positive pressure
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
9. Adjust the $F_\text{i}\ce{O2}$ to achieve $S_\text{p}\ce{O2}$ of 88-95% and/or $P_\text{a}\ce{O2}$ of 55-80 mmHg
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
- Left ventricular afterload
	- PEEP decreases $P_{\text{transmural}}$ which leads to decreased afterload (as per law of laplace before)
$$
\underset{\text{(AKA afterload)}}{\text{LV Wall Tension}}\approx \frac{P_{\text{transmural}}\times R}{\text{LV wall thickness}}
$$
- The effect on cardiac output and blood pressure is highly dependent on the patient’s volume status
	- If the patient is hypovolaemic or euvolaemic, the decreased preload will significantly decreased cardiac output and blood pressure
	- If the patient is hypervolaemic, the cardiac output will increase and the blood pressure may increase or remain unchanged
## Affects on Positive Pressure on Monitoring
- High levels of PEEP impair the usual means of assessing cardiac preload (i.e. CVP and PCWP)
- Alternative strategies include:
	- Calculating $\text{PCWP}_{\text{adjusted}}$
		- With normal lung compliance: $\text{PCWP}_{\text{adjusted}}\approx \text{PCWP}_{\text{measured}}-\frac{\text{PEEP}}{2}$
		- With abnormal lung compliance: $\text{PCWP}_{adjusted}\approx \text{PCWP}_{\text{measured}}-\frac{\text{PEEP}}{4}$
	- Right ventricular end diastolic volume
	- Intrathoracic blood volume
	- Respiratory variation in aortic blood velocity
## Affects on Cerebral Perfusion
$$
\underset{ \substack{\text{Cerebral}\\\text{Perfusion Pressure}}  }{ \text{CPP} } = \text{MAP} - \text{ICP}
$$
- Can in some circumstances decrease cerebral perfusion although this is variable
	- Derranged physiology says that PEEP increases ICP due to decreased venous return
# Pathologic Consequences
- Complications from [[Intubation]]:
	- Dental trauma
	- Aspiration
	- Laryngeal damage
	- Bronchospasm
	- Oesophageal intubation
	- Right main bronchus intubation
## Auto-PEEP (aka Intrinsic PEEP)
- Auto-PEEP is positive airway pressure that occurs at the end of expiration due to incomplete exhalation
- Consequences include:
	- ↑ Risk of barotrauma
	- ↓ Venous return → ↓ cardiac output → hypotension
	- Worsened V/Q mismatch
	- Patient-ventilator dyssynchrony
	- ↑ in patient’s work of breathing
- Mechanisms by which auto-PEEP develop:
	- High minute ventilation (e.g. high $V_{\text{T}}$ and/or high respiratory rate)
	- Expiratory flow limitation (e.g. high airway resistance in COPD)
	- Expiratory resistance (e.g. kinked ET tube, patient-ventilator dyssynchrony)
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
  <figure style="text-align: center;">
    <img src="Pasted image 20260328234056.png" style="width: 100%;">
    <figcaption><b>Figure 9.</b> Auto-PEEP absent</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="Pasted image 20260328234107.png" style="width: 100%;">
    <figcaption><b>Figure 10.</b> Auto-PEEP present</figcaption>
  </figure>
</div>
- Examine for audible air flow extending to the end of expiration on auscultation

$$
\text{Auto-PEEP}=\substack{\text{End-expiratory}\\\text{Alveolar Pressure}}-\substack{\text{Applied}\\\text{PEEP}}
$$

- It can be quantified using an end-expiratory breath hold where the rise in pressure above the applied PEEP represents the auto-PEEP
- Treatment strategies:
	- For high minute ventilation: ↓ $V_{\text{T}}$, ↓ respiratory rate or ↓ I:E ratio (these strategies allow for some permissive hypercapnoea)
	- Expiratory flow limitation: bronchodilators, secretion management, ↑ Applied PEEP
	- Expiration resistance: upsize ET tube, ↑ sedation, paralytics
## Patient-Ventilator Dyssynchrony
- Dyssynchrony is a state in which the respiratory cycle of the patient does not always match that of the ventilator
- General signs of possible dyssynchrony include increased heart rate, increased respiratory rate, decreased $S_\text{p}\ce{O2}$, increased expiratory muscle activity, coughing, agitation and visible inspiratory effort without triggering the ventilator

| Phase of Respiration | Types and Subtypes of Dyssynchrony                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Inspiration**      | **Trigger Dyssynchrony**<br>- Trigger Delay<br>- Missed Trigger<br>- Auto-Triggering<br>- Double-Triggering      |
| **Inspiration**      | **Flow Dyssynchrony**                                                                                            |
| **Expiration**       | **Cycling Dyssynchrony** *(a.k.a. Termination Dyssynchrony)*<br>- Premature Termination<br>- Delayed Termination |
- Trigger delay: an extra delay occurs between when the patient attempts to initiate a breath and when the ventilator begins to deliver it
	- Fixes include: ↓ trigger pressure, ↓ sedation, correction electrolyte abnormalities, bronchodilators or ↑ ET tube size, or correcting auto-PEEP
- Missed trigger: Insufficient respiratory effort fails to reach threshold for triggering ventilator
	- Fixes include: ↓ trigger pressure, ↓ sedation, correction electrolyte abnormalities, bronchodilators or ↑ ET tube size, or correcting auto-PEEP
- Auto-triggering: Occurs when the ventilator interprets signals other than the patient’s attempt to initiate a breath as signal deliver an inspiration
	- Fixes include: ↓ triggering sensitivity or addressing noise
- Flow dyssynchrony: occurs when the flow rate is set too low for the patient’s respiratory demand (seen in volume control modes)
	- Fixes include: ↑ inspiratory flow rate, changing inspiratory flow pattern or changing the ventilator mode

<figure style="text-align: center;">
  <img src="Pasted image 20260329005150.png">
  <figcaption><b>Figure 11.</b> Flow dyssynchrony. Note the concave or scalloped appearance of the inspiration waveform</figcaption>
</figure>

- Cycling dyssynchrony
	- Delayed termination
		- Here the ventilator inspiratory time exceeds that of the patient (i.e. patient tries to initiate expiration while the ventilator is still delivering inspiration)
		- It can be identified by a sharp spike in airway pressure at the end of inspiration
		- Fixes include: changing cycling threshold to cycle earlier, changing ventilator mode to time cycled in order to match the patient inspiratory time
	- Premature termination
		- The ventilator ceases delivery of air while the patient is trying to inspire
		- This can cause the pressure to drop below baseline and trigger another ventilator delivered inspiration (known as double triggering)
		- Fixes include: changing cycling threshold to cycle earlier, changing ventilator mode to time cycled in order to match the patient inspiratory time
## Ventilator-Associated Pneumonia
- Any pneumonia that occurs >48 hours after intubation

<figure style="text-align: center;">
  <img src="Pasted image 20260329005934.png">
  <figcaption><b>Figure 12.</b> Mechanism of ventilator associated pneumonia</figcaption>
</figure>

# COPD
- Increase inspiratory flow rate to 80-100 L/min to shorten the inspiratory time
- Avoid increasing respiratory rate
- Ensure adequate bronchodilators
- Ensure flow is returning to 0 before next inspiration
# 🙌 Liberation from the Ventilator
- Everyday someone is on the ventilator assess unless patient is on $F_\text{i}\ce{O2}>45\%$, patient is unstable or on high amounts of vasopressors
	- Lifting sedation
	- Weaning/liberation trial
## Spontaneous Breathing Trial
- Switch to some pressure support mode with some PEEP or to tube compensation
- Complete an ABG
	- If pH > 7.35 and $P_\text{a}\ce{CO2}<45$ and $P\ce{O2}>60$ ⇒ good trial, will likely succeed
- Rapid shallow breathing index (RSBI or Tobin index): RR/$V_{\text{T}}$ 
	- If while off the ventilator, the RSBI > 105 suggests the patient will fail the trial
- NIF ~ -30 suggests good trial
- Minute ventilation <15L/min
## Checklist
1. Mechanics of ventilation in the spontaneous breathing trial (as above)
2. Mental status: is the patient mentally alert enough to protect their airway
3. Secretions
4. Airleak on deflation of ETT balloon suggests absence of tracheal swelling
# Crashing Patient on the Ventilator
1. Call for help, airway cart, ultrasound and scalpel
2. If patient arrests, start CPR, delegate two staff members to chest compressions and continue to seek underlying cause
3. Disconnect patient from ventilator and allow exhalation
4. BMV 100% oxygen with PEEP valve at 10 breaths/min (if PEEP valve available)
5. Confirm endotracheal tube position with waveform capnography
6. Listen for any air leak from the mouth or neck
7. Pass a bronchoscope, tube exchanger, bougie or suction catheter to exclude obstruction
8. Consider reintubation unless a patent, correctly positioned tube is directly visualised
9. Use bedside ultrasound to diagnose pneumothorax and if confirmed, treat with finger thoracostomy
10. If no pneumothorax, review the list of common causes

![[Pasted image 20260414005005.png]]

- If the patient is crashing use the DOPES mnemonic
	- D: Dislodged or displaced ETT
	- O: Obstructed ETT by mucous, blood or kinking
	- P: Pneumothorax; check for any signs of decreased breath soudns or chest asymmetry
	- E: Equipment failure; rarely ventilator malfunction can be the cause of the alarm, if this is suspected disconnect the patient from the ventilator and try BVM ventilation
	- S: Stacked breathing (auto-PEEP); check for signs of increased work of breathing or decreased tidal volume

# Troubleshooting Ventilator Alarms
Ventilation alarms should be treated with great attention (often demanding the same attention as a code blue).


![[Pasted image 20260331214059.png]]

## High Peak Pressures
- Check the circuit:
	- Fluid pooling in circuit or filter
	- Kinking of the circuit
- Tube too small or biofilmed
- Bronchospasm
- Biting on ETT
## High Peak and Plateau Pressures
- Tube in mainstem
- Pneumothorax
- Poor lung compliance → ↓ $V_{\text{T}}$
- Abdominal compartment syndrome
## Low $\dot{V}/V_{\text{T}}$
- Circuit leak, ETT cuff leak
- Disconnection
- Patient fatigue or apnoea
- Poor coompliance (ARDS, pneumothorax)
## Low Peak Pressures
- Circuit disconnect
- ETT cuff deflated
- Pt effort
## Low Oxygen Alarm
- Circuit disconnect
- Incorrect gases
- Sensor malfunction
# Sources
- Strong Medicine Playlist: [Mechanical Ventilation - YouTube](https://www.youtube.com/playlist?list=PLBA5A30910F1FBF47)
- [Mechanical Ventilator Basics — ICU One Pager](https://onepagericu.com/vent-basics)
- Deranged physiology
	- [Flow, volume, pressure, resistance and compliance](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-531/flow-volume-pressure-resistance-and-compliance)
	- [Phases of a mechanical breath](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-532/phases-mechanical-breath)
	- [Basics of Mechanical Ventilation - Deranged Physiology](https://derangedphysiology.com/files/Basics%20of%20Mechanical%20Ventilation.pdf)
	- [Phase variables: triggering, limits, cycling and PEEP](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-533/phase-variables-triggering-limits-cycling-and-peep)
	- [Control variables: volume and pressure](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-534/control-variables-volume-and-pressure)
	- [Triggering of a mechanically supported breath](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-535/triggering-mechanically-supported-breath)
	- [Limit (target) variables in mechanical ventilation](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-536/limit-target-variables-mechanical-ventilation)
	- [Selecting and adjusting PEEP](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-538/selecting-and-adjusting-peep)
	- [Inspiratory pause, I:E ratio and inspiratory rise time](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-539/inspiratory-pause-ie-ratio-and-inspiratory-rise-time)
	- [Practical differences between pressure and volume controlled ventilation](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-542/practical-differences-between-pressure-and-volume-controlled-ventilation)
	- [Mandatory and spontaneous modes of ventilation](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-543/mandatory-and-spontaneous-modes-ventilation)
- [Ventilator Alarm (DOPES) - YouTube](https://www.youtube.com/watch?v=la4EPaPBc14)
- [EMCrit 239 - Vent Alarms = Code Blue](https://emcrit.org/emcrit/vent-alarms/)
- [Ventilator Alarms: Types, Causes, and Troubleshooting (2026)](https://www.respiratorytherapyzone.com/ventilator-alarms/)

[^1]: There is some low quality evidence suggesting postiive effect on ICU stay and duration of ventilator weaning in spontaneously breathing patients
[^2]: Normal mean inspiratory flow rate at rest is around 15 L/min with a peak of around 30-35 L/min