---
date: 2026-04-16
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
---
> Full notes: [[Mechanical Ventilation]]

# Ventilator Modes at a Glance

| Mode     | Trigger       | Control           | Cycle       | Key Feature                     | Use When                                  |
|----------|---------------|-------------------|-------------|---------------------------------|-------------------------------------------|
| **AC**   | Time/P/Flow   | Volume            | Time        | All breaths fully supported     | Full support needed, no hyperventilation  |
| **SIMV** | Time + P/Flow | Volume + Pressure | Time + Flow | Mandatory + partial spontaneous | Hyperventilating patients, auto-PEEP risk |
| **PCV**  | Time only     | Pressure          | Time        | No patient triggering           | High barotrauma risk                      |
| **PSV**  | P/Flow        | Pressure          | Flow        | All breaths patient-triggered   | Conscious, pre-extubation                 |
| **PRVC** | Time          | Adaptive P→V      | Time        | Guarantees VT, minimises P      | Best of both worlds                       |

> **AC vs SIMV:** In excess of set RR — AC gives *full* support; SIMV gives *partial* support

---

# Initial Ventilator Settings

| Parameter | Normal                   | COPD             | ARDS                |
| --------- | ------------------------ | ---------------- | ------------------- |
| **Mode**  | AC or SIMV               | SIMV             | AC or SIMV          |
| **FiO₂**  | Start 100%, wean to ≤60% | Start 100%, wean | Start 100%, wean    |
| **VT**    | 10 mL/kg IBW             | 8 mL/kg IBW      | 6 mL/kg IBW         |
| **RR**    | 10–20                    | Avoid ↑ RR       | 10–20               |
| **PEEP**  | 5–8 cm $\ce{H2O}$        | Low/ZEEP         | ≥8–12 cm $\ce{H2O}$ |
| **PS**    | 5–20 cm $\ce{H2O}$       | —                | —                   |
| **I:E**   | 1:2                      | 1:3 or 1:4       | 1:2                 |

> **FiO₂ >60%** → add strategies: ↑ PEEP, recruitment manoeuvres, change mode  
> **Pplateau >30 cm $\ce{H2O}$** → ↓ VT in 1 mL/kg steps

---

# Pressure Interpretation (Volume Control Modes)

```
P_peak ↑, P_plateau normal  →  Airway resistance ↑ (bronchospasm, secretions, kink)
P_peak ↑, P_plateau ↑       →  Lung compliance ↓ (pulmonary oedema, pneumothorax, ARDS)
```

$$P_\text{Peak}\propto\frac{\text{Airway Resistance}}{\text{Compliance}} \qquad P_\text{Plateau}\propto\frac{1}{\text{Compliance}}$$

$$\text{Compliance}=\frac{V_\text{T}}{P_\text{plateau}-\text{PEEP}} \qquad \text{Driving Pressure}=P_\text{plateau}-\text{PEEP}$$

---

# Phase Variables Summary

| Phase       | Variable                                           | Types                           | Key Point                                                           |
|-------------|----------------------------------------------------|---------------------------------|---------------------------------------------------------------------|
| **Trigger** | What starts a breath                               | Time / Flow / Pressure          | Flow trigger most comfortable; pressure trigger for auto-triggering |
| **Limit**   | Max value during inspiration (does not end breath) | Pressure / Flow / Volume        | —                                                                   |
| **Cycle**   | What ends a breath                                 | Time / Flow / Pressure / Volume | Flow cycling most comfortable; time cycling best for CO₂ control    |

---

# PEEP Effects

| Effect | Low-Mid PEEP | High PEEP |
|--------|-------------|-----------|
| Oxygenation | ↑ (alveolar recruitment) | ↓ (overdistension of healthy alveoli → ↑ dead space) |
| Preload | ↓ (↑ CVP, ↑ RV afterload) | ↓↓ |
| LV afterload | ↓ (↓ Ptransmural) | ↓ |
| ICP | Possible ↑ (↓ venous return) | — |

> Optimal PEEP = best compliance = highest O₂ delivery (sweet spot)

---

# Auto-PEEP

**Cause:** Incomplete exhalation → gas trapping

**Detect:** End-expiratory hold → rise in pressure above set PEEP

**Consequences:** Barotrauma, ↓ CO/hypotension, V/Q mismatch, dyssynchrony, ↑ WOB

| Mechanism | Fix |
|-----------|-----|
| High minute ventilation | ↓ VT, ↓ RR, ↓ I:E ratio |
| Expiratory flow limitation | Bronchodilators, secretion management, ↑ applied PEEP |
| Expiratory resistance | Upsize ETT, ↑ sedation/paralytics |

---

# Patient-Ventilator Dyssynchrony

| Type | Sign | Fix |
|------|------|-----|
| Trigger delay / Missed trigger | Effort without breath | ↓ trigger threshold, ↓ sedation, fix auto-PEEP |
| Auto-triggering | Breaths without effort | ↑ trigger threshold, address leak/noise |
| Flow dyssynchrony | Scalloped/concave pressure curve | ↑ flow rate, change pattern/mode |
| Delayed termination | Pressure spike end of inspiration | Cycle earlier, use time cycling |
| Premature termination | Pressure drops below baseline → double triggering | Cycle later |

---

# Crashing Patient — DOPES

| Letter | Problem                       | Action                         |
| ------ | ----------------------------- | ------------------------------ |
| **D**  | Dislodged ETT                 | Confirm position, reintubate   |
| **O**  | Obstructed ETT                | Suction, bougie, bronchoscope  |
| **P**  | Pneumothorax                  | USS → finger thoracostomy      |
| **E**  | Equipment failure             | Disconnect, BMV 100% $\ce{O2}$ |
| **S**  | Stacked breathing (auto-PEEP) | Disconnect, allow exhalation   |

---

# SBT Readiness Criteria

- **Respiratory:** FiO₂ <50%, PEEP ≤10 cm $\ce{H2O}$, $\ce{CO2}$ at baseline
- **CVS:** No ischaemia, HR <140, low vasopressors
- **Neuro:** Arousable, following commands
- **Renal:** No uncontrolled acid-base disturbance

**SBT Settings:** PSV 5/5 (PS 5 cm $\ce{H2O}$ + PEEP 5 cm $\ce{H2O}$) for 30 minutes

**Pass criteria:** $S_\text{p}\ce{O2}$ >88%, no ↑ Et$\ce{CO2}$ >10 mmHg, RSBI <105, no arrhythmia/haemodynamic instability

---

# High Pressure Alarm Troubleshooting

```
SpO₂ falling? → Crashing patient protocol (DOPES)
      ↓
Assess patient → Check ETT → Inspect circuit → Suction
      ↓
Inspiratory hold → measure P_plateau
      ↓
P_peak - P_plateau < 5 cm H₂O (↑ plateau)?
  → Rule out auto-PEEP → USS/CXR → ↓ VT until Pplateau <30
P_peak - P_plateau > 5 cm H₂O (↑ peak only)?
  → Bronchodilators → Check circuit → OK if Pplateau <30
```

---

# Ventilator Alarm Quick Reference

| Alarm | Common Causes | First Step |
|-------|--------------|-----------|
| High pressure | ↑ resistance, ↓ compliance, coughing | Assess patient, suction, inspiratory hold |
| Low pressure | Circuit disconnect, cuff leak | Check circuit connections |
| Low VT | Leak, malpositioned ETT | Check circuit, cuff, position |
| High frequency | Distress, auto-triggering, secretions | Assess patient, check airway |
| Apnoea | Disconnect, ↓ respiratory drive | Manual ventilation, check circuit |
| High PEEP | Auto-PEEP, air trapping, bronchospasm | ↑ expiratory time, ↓ RR, bronchodilators |
| Low PEEP | Circuit leak, cuff leak | Check circuit and cuff |
