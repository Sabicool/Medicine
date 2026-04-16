---
date: 2026-04-16
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
tags:
  - complete
---
> Part of: [[Mechanical Ventilation]]

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

$$Q=\frac{V}{T}$$

$$P=Q\times R$$

$$\text{Compliance}=\frac{\Delta\ \text{Volume}}{\Delta\ \text{Pressure}}$$

$$Q=\frac{\Delta\ P}{R}$$

- Where
	- $Q$ is airflow
	- $\Delta\ P$ is pressure gradient
	- $R$ is airway resistance

$$\text{Ventilation Pressure}=\text{Resistive Pressure}+\text{Elastic Pressure}$$

- Where
	- Resistive pressure is the pressure required to push airflow through the airways
	- Elastic pressure is the pressure required to inflate lungs and chest wall

# Phases of Mechanical Ventilation

- Four distinct phases, each of which has a governing variable which determines how that phase proceeds:
	- **Trigger** phase: initiate phase controlled by the trigger variable
	- **Inspiratory** phase: controlled by the limit variable
	- **Cycling** phase: controlled by the cycle variable
	- **Expiratory** phase: governed by the PEEP variable; the patient exhales passively

![[Pasted image 20260404113909.png|697]]

# Monitoring

![[Pasted image 20260329183832.png]]

$$P_\text{Peak}\propto\frac{\text{Airway Resistance}}{\text{Compliance}}$$
$$P_\text{Plateau}\propto\frac{1}{\text{Compliance}}$$
$$R_\text{insp}=\frac{P_\text{peak}-P_\text{plateau}}{Q_\text{end inspiratory}}$$

- An increasing $P_\text{peak}$ in the **absence** of an increasing $P_\text{plateau}$ suggests airway resistance is increasing (e.g. bronchospasm, excessive secretions, mucous plug, foreign body aspiration, extrinsic airway compression)

$$\text{Compliance}=\frac{V_\text{T}}{P_\text{plateau}-\text{PEEP}}$$

- An increasing $P_\text{plateau}$ suggests compliance is decreasing (e.g. pulmonary oedema, pleural effusion, pneumothorax, right mainstem bronchus intubation, ascites or other abdominal distension)

| $P_\text{peak}$ | $P_\text{plateau}$ | Likely problem |
| --- | --- | --- |
| Increased | Normal | Increased airway resistance |
| Increased | Increased | Decreased lung compliance |

---

# Gas Exchange

## Normal Gas Exchange

- Alveolar ventilation equation:

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
		- However, the gap can be:
			- Increased to >5 mmHg in low cardiac output, COPD, PE, advanced age
			- Decreased to <2 mmHg in high cardiac output states (e.g. septic shock)
