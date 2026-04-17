---
date: 2026-04-17
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
tags:
  - cards
---
> Part of: [[Mechanical Ventilation]]

- Ventilator modes are just pre-set combinations of ventilator settings
- Generally classified according to their major characteristics:
	- The control variable: pressure vs. volume
	- Breath sequence: spontaneous vs. mandatory
	- Targeting scheme: set point, dual targeting, servo control, adaptive etc.

# Assist Control (AC)

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

![[Pasted image 20260415224535.png]]

# Synchronised Intermittent Mandatory Ventilation (SIMV)

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
  <figcaption><b>Figure 2.</b> SIMV (with pressure support). Note that the first and fourth breaths are synchronised pressure triggered fully supported breath with tidal volume set for ~600 mL. The second, third and fifth breaths are spontaneous non-synchronised breaths assisted with pressure support with 10 cm of water.</figcaption>
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
	- Critically ill patients who are hyperventilating or otherwise prone to auto-PEEP or high airway resistance

> [!NOTE]
> The main difference between SIMV and AC is that spontaneous breaths in excess of the set respiratory rate:
> - In AC receive full support
> - In SIMV receive partial support
> Therefore in a patient with no spontaneous breaths AC = SIMV

# Pressure Control Ventilation (PCV)

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

# Pressure Support Ventilation (PSV)

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

# Dual Control Modes

- Use instantaneous feedback to control aspects of lung volume and airway pressure simultaneously
- Examples include
	- Pressure-regulated volume control
	- Volume support
	- Volume assured pressure support

## Pressure Regulated Volume Control (PRVC)

- The user sets a target tidal volume (as in volume control modes)
- The ventilator performs an assessment of the dynamic lung compliance over the course of three initial calibrating breaths
- Using this data, it then determines the appropriate pressure level required to achieve the prescribed tidal volume
- Advantages:
	- Square pressure waveform favours early and sustained lung unit recruitment
	- Mean airway pressure is as high as with PCV
	- Pressure is minimised for any given prescribed tidal volume
	- A minute volume is guaranteed, preserving a degree of control over PaCO2
