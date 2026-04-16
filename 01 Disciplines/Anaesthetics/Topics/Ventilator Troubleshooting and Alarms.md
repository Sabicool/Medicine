---
date: 2026-04-16
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
---
> Part of: [[Mechanical Ventilation]]

> [!WARNING] Ventilation alarms should be treated with great attention — often demanding the same attention as a code blue.

# Crashing Patient on the Ventilator

1. Call for help, airway cart, ultrasound and scalpel
2. If patient arrests, start CPR, delegate two staff members to chest compressions and continue to seek underlying cause
3. **Disconnect patient from ventilator and allow exhalation**
4. BMV 100% oxygen with PEEP valve at 10 breaths/min (if PEEP valve available)
5. Confirm endotracheal tube position with waveform capnography
6. Listen for any air leak from the mouth or neck
7. Pass a bronchoscope, tube exchanger, bougie or suction catheter to exclude obstruction
8. Consider re-intubation unless a patent, correctly positioned tube is directly visualised
9. Use bedside ultrasound to diagnose pneumothorax and if confirmed, treat with **finger thoracostomy**
10. If no pneumothorax, review the list of common causes

![[Pasted image 20260414005005.png]]

## DOPES Mnemonic

| Letter | Problem | Action |
| --- | --- | --- |
| **D** | **D**islodged or displaced ETT | Confirm position; re-intubate if necessary |
| **O** | **O**bstructed ETT (mucous, blood, kinking) | Pass suction catheter, bougie or bronchoscope |
| **P** | **P**neumothorax | USS → finger thoracostomy if confirmed |
| **E** | **E**quipment failure | Disconnect from ventilator → try BMV |
| **S** | **S**tacked breathing (auto-PEEP) | Disconnect and allow full exhalation |

---

# COPD on the Ventilator

- Increase inspiratory flow rate to **80-100 L/min** to shorten the inspiratory time
- Avoid increasing respiratory rate
- Ensure adequate bronchodilators
- Ensure flow is returning to 0 before next inspiration

---

# High Pressure Alarm

**Common causes:**
- ↑ Airway resistance (secretions, bronchospasm, biting on ETT, obstruction of exhalation valve, ETT too small)
- ↓ Lung compliance (pulmonary oedema, pneumonia, ARDS, pneumothorax, haemothorax, abdominal distension, chest wall rigidity)
- Patient-related (coughing, patient-ventilator dyssynchrony)

**Troubleshooting:**
1. If $S_\text{p}\ce{O2}$ low or falling → [[Ventilator Troubleshooting and Alarms#Crashing Patient on the Ventilator|crashing on the ventilator]]
2. Assess the patient: respiratory distress, cyanosis, agitation, ↓ SpO₂
3. Check for capnograph waveform
4. Check the airway — inspect ETT for obstruction, kinking, displacement; suction if secretions present
5. Inspect circuit for kinks, water accumulation or disconnections
6. Change tidal volume to ≤ 8 mL/kg predicted body weight
7. Increase the ventilator peak pressure alarm limit until entire set volume is delivered without triggering
8. Perform **inspiratory hold** on ventilator to assess plateau pressure:

```
P_peak - P_plateau < 5 cmH₂O (↑ plateau)?
  → Rule out dynamic hyperinflation (lower RR or disconnect)
  → If no dynamic hyperinflation: USS/CXR to exclude pneumothorax and mainstem intubation
  → Consider atelectasis, pneumonia, mucous plugging or ARDS
  → Reduce VT until Pplateau < 30 cmH₂O

P_peak - P_plateau > 5 cmH₂O (↑ peak only)?
  → Auscultate: bronchodilators if obstructive disease
  → Check each piece of circuit for obstruction
  → OK to leave peak pressure limit high if Pplateau remains < 30 cmH₂O
```

![[Pasted image 20260415215827.png]]

![[Pasted image 20260414225715.png]]

---

# Low Pressure Alarm

**Common causes:**
- Circuit disconnection (ventilator tubing, loose humidifier, disconnected exhalation valve)
- Airway leaks (ETT cuff leak, deflated cuff, improperly positioned ETT)
- System failure (loss of gas supply, power failure, air compressor malfunction)
- Incorrect ventilator settings (pressure limit set too high, VT set too low, excessively sensitive trigger)

**Troubleshooting:**
1. Consider manual ventilation with resuscitation bag while troubleshooting
2. Check for circuit disconnection
3. Inspect all ventilator tubing and connections
4. Examine the ETT cuff for leaks
5. Confirm that the ETT is correctly positioned
6. Ensure the ventilator is receiving adequate gas supply and power

---

# Low $V_{\text{T}}$ Alarm

**Common causes:**
- Leaks in system
- Patient disconnection
- Airway problems (malpositioned ETT, partial extubation, deflated cuff, tracheostomy tube leak)
- Inadequate ventilator settings (VT set too low, premature cycling, inappropriate inspiratory time, excessive respiratory demand)

**Troubleshooting:**
1. Assess patient: chest movement, SpO₂, overall stability — if inadequate or crashing → [[Ventilator Troubleshooting and Alarms#Crashing Patient on the Ventilator|crashing patient]]
2. Inspect for disconnection — entire circuit from ventilator to patient
3. Check for leaks — evaluate cuff pressure, inspect for air leaks around ETT or tracheostomy tube
4. Confirm airway position
5. Evaluate ventilator settings and mode

---

# High Frequency Alarm

**Common causes:**
- Respiratory distress (hypoxaemia, pain, fever, metabolic acidosis, inadequate pressure support)
- Airway narrowing (secretions, mucous plugging, bronchospasm)
- Auto-triggering (sensitivity set too high, circuit leaks, water in tubing, cardiac oscillations, external movement)

**Troubleshooting:**
1. Assess the patient: accessory muscle use, low SpO₂, diaphoresis, increased WOB
2. Evaluate oxygenation and ventilation (review recent blood gas results)
3. Check the airway for bronchospasm, mucous plugging; suction if indicated
4. Review ventilator sensitivity if auto-triggering is suspected
5. Optimise support: ↑ $F_\text{i}\ce{O2}$, inspiratory flow, pressure support; treat pain/anxiety; correct acid-base disorders

---

# Apnoea Alarm

**Common causes:**
- Circuit disconnection
- Depressed respiratory drive
- Fatigue or neuromuscular weakness
- Inadequate sensitivity

**Troubleshooting:**
1. Assess the patient: chest rise, respiratory effort, SpO₂, signs of instability
2. Confirm circuit integrity: disconnection, loose tubing or major leaks
3. Provide manual ventilation while identifying the source of the problem
4. Evaluate sedation and respiratory drive; consider contributing medications
5. Review trigger settings and backup ventilation

---

# High PEEP Alarm

**Common causes:**
- Auto-PEEP / air trapping
- High respiratory rate
- Short expiratory time
- Insufficient inspiratory flow (prolonged inspiratory time)
- Obstructive lung disease / bronchospasm
- Excessive tidal volume
- Inappropriate I:E ratio

**Troubleshooting:**
- Prolong expiratory time
- Reduce respiratory rate
- Reduce tidal volume
- Increase inspiratory flow to shorten inspiratory time
- Treat bronchospasm with bronchodilators
- Suction retained secretions if indicated
- Reassess the set PEEP level

---

# Low PEEP Alarm

**Common causes:**
- Leak in the ventilator circuit
- Loose tubing connection
- ETT cuff leak
- Leak around tracheostomy tube
- Faulty valve or humidifier connection
- Strong patient inspiratory effort

**Troubleshooting:**
1. Inspect the circuit for leaks or loose connections
2. Evaluate cuff inflation and airway integrity
3. Confirm that the ventilator valves are functioning properly
4. Assess inspiratory flow settings
5. Adjust settings to better match patient demand if needed

---

# Low Oxygen Alarm

**Common causes:**
- Circuit disconnect
- Incorrect gases
- Sensor malfunction
