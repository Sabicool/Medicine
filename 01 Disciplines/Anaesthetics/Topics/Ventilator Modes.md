---
date: 2026-04-19
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
tags:
  - cards
---
> Part of: [[Mechanical Ventilation]]

![[Pasted image 20260417201104.png]]

- Ventilator modes are just pre-set combinations of ventilator settings
- Generally classified according to their major characteristics:
	- The control variable: pressure vs. volume
	- Breath sequence: spontaneous vs. mandatory
	- Targeting scheme: set point, dual targeting, servo control, adaptive etc.
# Continuous Mnadatory Ventilation (CMV)
![[Pasted image 20260418193629.png]]

- The main feature is that it ignores attempts at breathing and all components of the respiratory phase delivered by the ventilator are mandatory (i.e. controlled by time)
	- This means it is time triggered and typically time cycled
- Control variable: Typically volume controlled but can be pressure
- Time triggered
- Volume, pressure or flow limited
- Time-cycled but can be volume cycled to avoid an inspiratory pause
- Advantages:
	- Gives optimal control over minute volume; therefore useful when maintaining a narrow $\ce{CO2}$ range (e.g. in a paralysed sedated head injury patient)
- Disadvantages
	- Uncomfortable; requires decent sedation

# Assist Control (AC)

- Mix of mandatory and assisted breaths with all breaths, once triggered, are treated the same and have a consistent tidal volume
- Trigger: time, pressure or flow
- Control: flow (volume)
- Cycling: time but can be volume cycled to avoid inspiratory pauses

<figure style="text-align: center;">
  <img src="Pasted image 20260328150712.png">
  <figcaption><b>Figure 1.</b> Assist control. Note that the 1st, 3rd and 4th breaths are patient triggered with the second breath being time triggered.</figcaption>
</figure>

- Advantages
	- Guarantees a minimum minute ventilation
	- Low work of breathing
- Disadvantages
	- Can lead to respiratory alkalosis, auto-PEEP and hypotension in hyperventilating patients as every breath leads to a fully supported breath
	- Uncomfortable
- Indications
	- Critically ill patients requiring full ventilatory support and in whom fluctuations in $V_{\text{T}}$ is undesirable

![[Pasted image 20260415224535.png]]
# Intermittent Mandatory Ventilation (IMV)
- Not continuously mandatory, the patient can decide their own respiratory rate and take a number of pressure supported breaths; the machine also gives a set number of mandatory breaths
- Advantages:
	- Guarantees a minimum minute ventilation
![[Pasted image 20260418195327.png]]
- Mandatory breaths are volume controlled
- Mandatory breaths are time triggered and the pressure supported breaths are flow triggered
- Time cycled but can be volume cycled to avoid inspiratory pauses
# Synchronised Intermittent Mandatory Ventilation (SIMV)

- Main difference with IMV is that it is synchronised (as in the name); the patient can decide their own respiratory rate and they can take a number of pressure-supported breaths
- Among these breaths, the machine also gives a set number of mandatory breaths and if the patient makes an effort around the same time the next mandatory breath is due, the ventilator delivers to them an assist-control breath, with volume control
- Mix of mandatory breaths (some of which are synchronised with spontaneous breaths), and assisted breaths
- Mandatory (non-synchronised breaths):
	- Trigger: time
	- Control: volume
	- Cycling: time or volume
- Synchronised breaths:
	- Trigger: pressure or flow
	- Control: volume
	- Cycling: time or volume
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
	- Comfortable for the patient
- Disadvantages
	- Increased work of breathing for patient
	- ? Lower cardiac output in patients with LV dysfunction
	- Limited control over the minute ventilation
- Indications
	- Critically ill patients who are hyperventilating or otherwise prone to auto-PEEP or high airway resistance

> [!NOTE]
> The main difference between SIMV and AC is that spontaneous breaths in excess of the set respiratory rate:
> - In AC receive full support
> - In SIMV receive partial support
> 
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
	- Patients who are at a particularly high risk of barotrauma (i.e. those with low compliance)

# Pressure Support Ventilation (PSV)
- The ventilator only controls the pressure support level and the rate, volume, cycling time etc are controlled by the patient
	- You can only control the the pressure support value (indirectly controlling the tidal volume) and the flow cycling trigger (decreasing it will make the breath last longer)
- There are no mandatory breaths; every breath must be triggered by the patient
	- This mode is typically combined with SIMV as the non-mandatory component
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
	- First breath tests compliance and is typically a low volume low pressure calibration breath
	- The next breath is delivered at a calculated pressure depending on the compliance from the previous breath; if the controlled target volume is exceeded, the ventilator adjusts the flow rate so that the next breath the pressure is slightly lower
- Using this data, it then determines the appropriate pressure level required to achieve the prescribed tidal volume
- The main feature is that the lowest possible pressure to achieve the volume control target is applied
![[Pasted image 20260419194520.png]]

- Advantages and disadvantages are similar to SIMV with the added benefits from PCV
- Advantages:
	- Mean airway pressure is as high as with PCV
	- Pressure is minimised for any given prescribed tidal volume
	- A minimum minute volume is guaranteed, preserving a degree of control over PaCO2
