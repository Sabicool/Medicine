---
date: 2026-04-16
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
  - "[[Anaesthetics]]"
---
> Part of: [[Mechanical Ventilation]]

# Complications from Intubation

- Dental trauma
- Aspiration
- Laryngeal damage
- Bronchospasm
- Oesophageal intubation
- Right main bronchus intubation

# Physiological Consequences

# Effects on Gas Exchange

- At **low and medium levels of PEEP:** ↑ alveolar recruitment → larger surface area for gas diffusion → ↑ oxygenation
- At **high levels of PEEP:** alveolar dead space increases dramatically
	- PEEP has a greater effect on normal compliant alveoli than on stiff/fluid-filled alveoli
	- At high PEEP, healthy alveoli become overdistended → ↑ resistance to blood flow → blood shunts towards poorly ventilated alveoli → ↑ physiologic dead space → worsened V/Q mismatch
	- High PEEP can also increase pulmonary vascular resistance, worsening intracardiac R-L shunts

<figure style="text-align: center;">
  <img src="Pasted image 20260328195659.png" width="75%">
</figure>

# Effects on Haemodynamics

- **Preload:** PEEP can decrease preload because:
	- ↑ CVP → ↓ venous return to RA
	- ↑ RV afterload → ↓ blood exiting RV
	- ↑ RV afterload → leftward displacement of the IV septum → impairs LV diastolic filling
- **LV Afterload:** PEEP decreases $P_{\text{transmural}}$ which leads to decreased afterload (as per law of Laplace)

$$
\underset{\text{(AKA afterload)}}{\text{LV Wall Tension}}\approx \frac{P_{\text{transmural}}\times R}{\text{LV wall thickness}}
$$

- The effect on cardiac output and blood pressure is **highly dependent on volume status:**
	- Hypovolaemic or euvolaemic → ↓ preload significantly → ↓ cardiac output and blood pressure
	- Hypervolaemic → cardiac output increases, blood pressure may increase or remain unchanged

# Effects on Monitoring

- High levels of PEEP impair the usual means of assessing cardiac preload (i.e. CVP and PCWP)
- Alternative strategies include:
	- Calculating $\text{PCWP}_{\text{adjusted}}$
		- With normal lung compliance: $\text{PCWP}_{\text{adjusted}}\approx \text{PCWP}_{\text{measured}}-\frac{\text{PEEP}}{2}$
		- With abnormal lung compliance: $\text{PCWP}_{adjusted}\approx \text{PCWP}_{\text{measured}}-\frac{\text{PEEP}}{4}$
	- Right ventricular end diastolic volume
	- Intrathoracic blood volume
	- Respiratory variation in aortic blood velocity

# Effects on Cerebral Perfusion

$$
\underset{ \substack{\text{Cerebral}\\\text{Perfusion Pressure}}  }{ \text{CPP} } = \text{MAP} - \text{ICP}
$$

- PEEP can in some circumstances decrease cerebral perfusion (variable)
	- PEEP increases ICP due to decreased venous return

---

# Auto-PEEP (aka Intrinsic PEEP)

![[expiratory hold manoeuvre.jpg]]

- Auto-PEEP is positive airway pressure that occurs at the end of expiration due to **incomplete exhalation**
- Consequences include:
	- ↑ Risk of barotrauma
	- ↓ Venous return → ↓ cardiac output → hypotension
	- Worsened V/Q mismatch
	- Patient-ventilator dyssynchrony
	- ↑ Patient's work of breathing

## Mechanisms

| Mechanism | Examples |
| --- | --- |
| High minute ventilation | High $V_{\text{T}}$ and/or high respiratory rate |
| Expiratory flow limitation | High airway resistance in COPD |
| Expiratory resistance | Kinked ET tube, patient-ventilator dyssynchrony |

## Detection

- Examine for audible air flow extending to the end of expiration on auscultation

$$
\text{Auto-PEEP}=\substack{\text{End-expiratory}\\\text{Alveolar Pressure}}-\substack{\text{Applied}\\\text{PEEP}}
$$

- Quantify using an **end-expiratory breath hold** — the rise in pressure above the applied PEEP represents the auto-PEEP

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

## Treatment

| Mechanism | Treatment |
| --- | --- |
| High minute ventilation | ↓ $V_{\text{T}}$, ↓ respiratory rate, or ↓ I:E ratio (permits permissive hypercapnoea) |
| Expiratory flow limitation | Bronchodilators, secretion management, ↑ applied PEEP |
| Expiratory resistance | Upsize ET tube, ↑ sedation, paralytics |

---

# Patient-Ventilator Dyssynchrony

- Dyssynchrony is a state in which the respiratory cycle of the patient does not always match that of the ventilator
- General signs of possible dyssynchrony: increased HR, increased RR, decreased $S_\text{p}\ce{O2}$, increased expiratory muscle activity, coughing, agitation and visible inspiratory effort without triggering the ventilator

| Phase | Type | Fix |
| --- | --- | --- |
| **Inspiration** | **Trigger Delay** — extra delay between patient effort and ventilator response | ↓ trigger pressure, ↓ sedation, correct electrolytes, bronchodilators, ↑ ETT size, correct auto-PEEP |
| **Inspiration** | **Missed Trigger** — insufficient effort to reach threshold | Same as above |
| **Inspiration** | **Auto-Triggering** — non-patient signals trigger a breath | ↓ triggering sensitivity, address noise |
| **Inspiration** | **Double Triggering** — two breaths delivered for one effort | Usually consequence of premature termination; ↑ inspiratory time |
| **Inspiration** | **Flow Dyssynchrony** — flow rate set too low for patient demand (volume control) | ↑ inspiratory flow rate, change flow pattern, change mode |
| **Expiration** | **Delayed Termination** — ventilator inspires longer than patient wants | ↑ cycling threshold (earlier), change to time cycling |
| **Expiration** | **Premature Termination** — ventilator ceases before patient has finished inspiring | ↓ cycling threshold (later), change to time cycling |

<figure style="text-align: center;">
  <img src="Pasted image 20260329005150.png">
  <figcaption><b>Figure 11.</b> Flow dyssynchrony. Note the concave or scalloped appearance of the inspiration waveform</figcaption>
</figure>

- **Delayed termination** identified by a sharp spike in airway pressure at the end of inspiration

---

# Ventilator-Associated Pneumonia (VAP)

- Any pneumonia that occurs **>48 hours** after intubation

<figure style="text-align: center;">
  <img src="Pasted image 20260329005934.png">
  <figcaption><b>Figure 12.</b> Mechanism of ventilator associated pneumonia</figcaption>
</figure>
