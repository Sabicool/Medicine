---
date: 2026-03-28
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
figureCount: 4
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
	- $V_\text{D}$ is teh physiologic dead space
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
	- Control variable: defines what aspect of inspiration is the primary variable controlled by the ventilator during inspiration. Common options include: pressure controlled, volume controlled (also known as volume controlled)
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
- 
# Source
- Strong Medicine Playlist: [Mechanical Ventilation - YouTube](https://www.youtube.com/playlist?list=PLBA5A30910F1FBF47)