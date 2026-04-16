---
date: 2026-04-16
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
---
![[Pasted image 20260329010927.png]]

# Mechanical Ventilation

> Quick reference: [[Mechanical Ventilation - Quick Reference]]

## Sub-Notes

| Note                                      | Contents                                                                                                   |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [[Physiology of Mechanical Ventilation]]  | Lung mechanics, gas exchange, phases of MV, monitoring                                                     |
| [[Ventilator Modes]]                      | AC, SIMV, PCV, PSV, PRVC — trigger/control/cycle, pros/cons, indications                                   |
| [[Ventilator Settings]]                   | Control variables, targeting schemes, phase variables, FiO₂, VT, RR, PEEP, PS, I:E ratio, initial settings |
| [[Ventilator Waveform Interpretation]]    | Pressure and flow waveforms, P-V loops, work of breathing                                                  |
| [[Lung Protective Ventilation]]           | VALI, barotrauma, biotrauma, ARDS protocol, permissive hypercapnoea                                        |
| [[Ventilator Consequences]]               | Effects on gas exchange, haemodynamics, ICP; auto-PEEP, dyssynchrony, VAP                                  |
| [[Ventilatory Weaning]]                   | SBT readiness, passing/failing SBT, extubation checklist, post-extubation                                  |
| [[Ventilator Troubleshooting and Alarms]] | Crashing patient, DOPES, COPD, all alarm types                                                             |

---

## Ventilator Modes Overview

| Mode | Control | Trigger | Cycle | Key Use |
| --- | --- | --- | --- | --- |
| **AC** | Volume | Time/P/Flow | Time | Full support, no hyperventilation |
| **SIMV** | Volume + Pressure | Time + P/Flow | Time + Flow | Hyperventilating patient, auto-PEEP risk |
| **PCV** | Pressure | Time only | Time | High barotrauma risk |
| **PSV** | Pressure | P/Flow | Flow | Conscious patient, pre-extubation |
| **PRVC** | Adaptive (P→V) | Time | Time | Guarantees VT, minimises P |

> AC vs SIMV: excess spontaneous breaths get **full** support in AC, **partial** support in SIMV

---

## Initial Settings at a Glance

| Parameter | Normal | COPD | ARDS |
| --- | --- | --- | --- |
| **VT** | 10 mL/kg IBW | 8 mL/kg IBW | 6 mL/kg IBW |
| **RR** | 10–20 | Avoid ↑ | 10–20 |
| **FiO₂** | Start 100%, wean to ≤60% | ← | ← |
| **PEEP** | 5–8 cmH₂O | Low/ZEEP | ≥8–12 cmH₂O |
| **I:E** | 1:2 | 1:3 or 1:4 | 1:2 |

---

## Pressure Interpretation

| $P_\text{peak}$ | $P_\text{plateau}$ | Meaning |
| --- | --- | --- |
| ↑ | Normal | ↑ Airway resistance (bronchospasm, secretions, kink) |
| ↑ | ↑ | ↓ Lung compliance (oedema, pneumothorax, ARDS) |

$$\text{Compliance}=\frac{V_\text{T}}{P_\text{plateau}-\text{PEEP}} \qquad \text{Driving Pressure}=P_\text{plateau}-\text{PEEP}$$

---

## Sources

- Strong Medicine Playlist: [Mechanical Ventilation - YouTube](https://www.youtube.com/playlist?list=PLBA5A30910F1FBF47)
- ICU One Pager
	- [Mechanical Ventilator Basics — ICU One Pager](https://onepagericu.com/vent-basics)
	- [Ventilator Weaning — ICU One Pager](https://onepagericu.com/vent-weaning)
	- [Vent Troubleshooting: High Peak Pressures — ICU One Pager](https://static1.squarespace.com/static/5e6d5df1ff954d5b7b139463/t/5e8f9a20e9d767577ce33da7/1586469408605/ICU_one_pager_vent_troubleshooting_1.pdf)
	- [Volume Assist/Control Ventilation — ICU One Pager](https://static1.squarespace.com/static/5e6d5df1ff954d5b7b139463/t/60bc536cf8f9a34b0e38757c/1622954861065/ICU_one_pager_volume_control.pdf)
- Deranged Physiology
	- [Flow, volume, pressure, resistance and compliance](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-531/flow-volume-pressure-resistance-and-compliance)
	- [Phases of a mechanical breath](https://derangedphysiology.com/main/cicm-primary-exam/respiratory-system/Chapter-532/phases-mechanical-breath)
	- [Basics of Mechanical Ventilation](https://derangedphysiology.com/files/Basics%20of%20Mechanical%20Ventilation.pdf)
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
- [Liberation from the ventilator - EMCrit Project](https://emcrit.org/ibcc/extubation/)
