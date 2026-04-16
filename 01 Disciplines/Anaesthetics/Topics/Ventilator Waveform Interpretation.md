---
date: 2026-04-16
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
---
> Part of: [[Mechanical Ventilation]]

# Pressure Waveform

![[ventilator pressure waveform.jpg]]

# Peak Pressure

- High peak pressure suggests possibility of airway narrowing (e.g. ET tube being kinked, ventilator tubing being full of fluid or bronchospasm)

![[pressure ciurve high vs normal airway resistance.jpg]]

# Plateau Pressure

- Pressure in the lung after all flow has stopped; directly related to the compliance of the lung parenchyma

$$
\begin{align*}
\text{Plateau Pressure}&=\frac{\text{Tidal Volume}}{\text{Static Compliance}} & \text{Static Pressure}&=\frac{\text{Tidal Volume}}{\text{Driving Pressure}} \\
\text{Driving Pressure} & = \text{Plateau Pressure}- \text{PEEP}
\end{align*}
$$

![[pressure curve high vs normal lung compliance.jpg]]

# Plateau Decay

- In an inspiratory pause, the pressure will gradually decrease from the initial plateau pressure; this occurs because of:
	- Elastic energy stored in the lung tissue and chest wall is dissipating
	- Lung units with different time constants are exchanging gas
	- Some of the gas is being absorbed into the pulmonary circulation
	- Some of the gas is leaking out of the circuit tubing

# Flow Waveform

![[ventilator flow waveform.jpg]]

# Maximum Flow

- In pressure control modes, the flow waveform is decelerating
	- A rapid deceleration of this flow indicates either that the lung compliance is poor or that airway resistance is high

# End-Inspiratory Flow

- If the end inspiratory flow is positive, then increasing inspiratory time will produce larger tidal volumes

# Peak Expiratory Flow

- The rate of expiratory flow is determined by the resistance of the airways and the elastic recoil of the lungs and chest wall
	- A low expiratory peak flow suggests airway obstruction (e.g. bronchospasm) or an over-compliant chest wall
- If expiratory flow is prolonged, the airway resistance must be increased
- If flow does not reach zero by the beginning of the next breath, there must be gas trapping

![[flow curves in increased airway resistance and gas trapping.jpg]]

# Pressure-Volume Loop

![[anatomy of the pressure-volume loop.jpg]]

- Above mode is mandatory with volume as the control variable and flow as constant
- **Lower inflection point ($P_{\text{flex}}$):** the airway pressure which designates the critical opening pressure (takes more pressure to re-inflate a collapsed alveolus than it takes to distend a deflated one)
- **Upper inflection point:** corresponds to the deflation of the most hyperinflated lung units

## Idealised Pressure-Volume Loop of Volume-Controlled Ventilation

![[pressure-volume loop of an ideal CMV patient.jpg]]

## Idealised Pressure-Volume Loop of Pressure-Controlled Ventilation

![pressure-volume loop of an ideal PCV patient](https://www.derangedphysiology.com/main/sites/default/files/php/Respiratory-failure-and-mechanical-ventilation/images/pressure-volume%20loop%20of%20an%20ideal%20PCV%20patient.jpg)

## Realistic Pressure-Volume Loop of Pressure-Controlled Ventilation

![[pressure volume loop in SIMV-PRVC.jpg]]

# Changes with Respiratory Compliance

- As lungs decrease in compliance, in volume-controlled mode higher peak airway pressures will develop and a beaked region will develop indicating alveolar overdistention

![[influence of changes in lung compliance on the pressure-volume curve in CMV.jpg]]

- In pressure-controlled mode, the volume generated will decrease resulting in hypoventilation and hypercapnoea

![[influence of changes in lung compliance on the pressure-volume curve in PCV.jpg]]

# Air Leak

- With an air leak in the circuit, the volume does not return to zero

![[pressure volume loop with a leak.jpg]]

# Patient-Ventilator Dyssynchrony

![[A pressure-volume loop with patient-ventilator dyssynchrony.jpg]]

# Work of Breathing

$$
\begin{align*} 
W &= \int Fdx \\
W &= \int (P\cdot A)dx & \left( P=\frac{F}{A} \right) \\
W &= \int PdV  & (dV=Adx)\\
\end{align*}
$$

- Hence the work of breathing is the area to the left of the pressure-volume loop
- Anything that increases the convexity of the inspiratory curve or pushes the whole loop to the right increases the work of breathing

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
