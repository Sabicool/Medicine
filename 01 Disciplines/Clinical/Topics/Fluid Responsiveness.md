---
date: 2026-06-13
Rotations:
  - "[[Emergency Medicine]]"
  - "[[Intensive Care Unit]]"
---
- Most healthy individuals and stable hospitalized patients have native preload reserve and will show positive fluid responsiveness on a PLR or dynamic test
- Being "responsive" does not automatically mean a patient _needs_ volume
- **The Unified Framework**:
	1. Use **Static Indices** (physical exam markers, lactate, basic static ultrasound) as a screening tool to establish a high **pre-test probability** of shock or tissue hypoperfusion
	2. Once a perfusion deficit is confirmed, deploy **Dynamic Science** (PLR, EEOT, PPV, or echo stroke volume calculations) to confirm if a fluid bolus will successfully increase cardiac output or if you must switch to early vasoactive medications


![[Pasted image 20260502230540.png]]
- Fluid responsiveness is 10-15% increase in cardiac output in response to a fluid challenge or pre-load augmentation manoeuvre
- Fluid tolerance is the absence of harm (e.g. pulmonary oedema) when fluid is administered
- Not the same as needing fluid:
	- **Is the patient fluid responsive?** (Will CO rise with fluid?)
	- **Does the patient need fluid?** (Is tissue perfusion inadequate and likely to improve with more preload?)
- Clinical parameters (e.g. hourly urine output and MAP) tend to lag and do not reliably predict fluid responsiveness
# Measures
- There exists dynamic and static measures
	- Dynamic measures rely on the respiratory cycle and how it effects changes with cardiac preload buy generally require mechanical ventilation
		- Increasing intrathoracic pressure with positive pressure (mechanical ventilation) → ↓ venous return → ↑ RV afterload → ↓ LV filling
	- Static measures do not require this
- Generally dynamic predictors are better than static predictors (e.g. CVP[^2], PCWP, RAP/LVEDP)
- Some measures can predict fluid responsiveness in isolation but some need to be combined with a challenge; with the level of evidence varying for each combination (see ICU one pager top right)
## Pulse Pressure Variation
- Swing of the A-line
- Requirements
	- Sinus rhythm without significant ectopy
	- Normal abdominal pressure
	- No RV dysfunction
	- Synchronous with the ventilator (mechanically ventilated without spontaneous breaths)
	- Receiving 8mL/kg of tidal volume
	- PEEP of 5-10 cm of $\ce{H2O}$
	- Closed chest (open chest post-cardiotomy invalidates)
- PPV > 12% means the patient is probably fluid responsive
![[Pasted image 20260612222728.png]]

## Pulse Contour Cardiac Output
- Computer does uses some proprietary formulas to analyse the waveform of the arterial line to estimate stroke volume variation or cardiac output (e.g. FloTrac, LiDCO, PiCCO)
- Can be performed in spontaneously breathing patients
- Optimal threshold to predict fluid responsiveness varies by device but generally good predictor
## Thermodilution Measurement of Cardiac Output or Index
- Pulmonary artery catheter used to inject cold saline proximally and measure temperature distally. Formulas are then used to calculate the amount of blood required to dilute the cold bolus based on the temperature to figure out cardiac output and index
- A 10-15% increase in cardiac output/index before & after a challenge
- Considered the gold standard but limited by potential causes of error:
	- Catheter malposition
	- Variation in injectate temperature
	- Shunt
	- Very low cardiac output
	- Vavlulopathy
## IVC Size & Distensibility Index
- Positive intrathoracic pressure during inhalation (mechanical ventilation) causes IVC to become larger and on releasing, IVC returns to normal size
- Requirements
	- Sinus rhythm
	- Normal abdominal pressure
	- No RV dysfunction
	- Synchronous with the ventilator
	- Receiving 8mL/kg of tidal volume
	- PEEP of 5-10 cm of $\ce{H2O}$
- Use M-mode to track the size of the IVC over time
- In spontaneously breathing patients using the collapsibility index
	- Measured in the subxiphoid view 
	- Collapsibility > 50% suggests fluid responsiveness
	- Collapsibility <15-20% suggests volume overload/non-responsiveness
$$
\text{IVC collapsibility}=\frac{\text{IVC}_{\text{max}}-\text{IVC}_{\text{min}}}{\text{IVC}_{\text{max}}}\times 100\%
$$
- In mechanically ventilating patients use the distensibility index
	- Distensibility >18% predicts fluid responsiveness
$$
\text{IVC distensibility}=\frac{\text{IVC}_{\text{max}}-\text{IVC}_{\text{min}}}{\text{IVC}_{\text{min}}}\times 100\%
$$

![[Pasted image 20260612223237.png]]
## Sub-Aortic Peak Velocity
- Obtain a apical 5 chamber view (4-chamber view tilted anteriorly to see the LVOT)
- Requirements
	- Sinus rhythm
	- Normal abdominal pressure
	- No RV dysfunction
	- Synchronous with the ventilator
	- Receiving 8mL/kg of tidal volume
	- PEEP of 5-10 cm of $\ce{H2O}$
- Place a pulse wave doppler in the LVOT
![[Pasted image 20260612223630.png]]

- Review peak velocity difference between highest and minimum

![[Pasted image 20260612223720.png]]

$$
\frac{\text{Maximum}-\text{Minimum}}{\text{Average}}>12 \%
$$
- >12% predicts fluid responsiveness

## LVOT VTI
- Conceptual framework
	- The Left Ventricular Outflow Tract (LVOT) is modeled as a geometric cylinder
	- The volume of blood propelled through this cylinder during a single systole represents one Stroke Volume (SV)
		- To determine the volume of this cylinder, the clinician must solve for two metrics: the **width** (diameter) of the cylinder and the **height** (stroke distance) of the blood column
1. Measure cylinder width (LVOT diameter)
	- Freeze the ultrasound frame precisely at **mid-systole** when the aortic valve leaflets are completely open
	- ![[Pasted image 20260612234119.png|645]]
	- Zoom in specifically on the LVOT area to optimise spatial resolution
	- Carefully measure the diameter of the LVOT from the white inner edge to the opposite white inner edge (inner-to-inner border), parallel to the aortic valve plane
2. Measure cylinder height (stroke distance via VIT)
	- Obtain an apical 5 chamber view 
	- Activate **Pulse Wave (PW) Doppler** and position the sample gate within the LVOT, just proximal to the aortic valve annulus
		![[Pasted image 20260612234244.png]]
	- Obtain a clean spectral Doppler tracing
		- This will display a series of inverted, envelope-like waveforms reflecting blood flowing away from the probe
	- Caliper-trace the perimeter of these waveforms across a few cardiac cycles (not some machines can do auto VTI tracing and calculate the LVOT VTI for you); normal VTI measurement is 18-22 cm
		- LVOT VTI < 18cm suggests reduced cardiac output shock (e.g. cardiogenic, obstructive, hypovolaemic)
		- LVOT VTI ≥18cm suggests normal or increased cardiac output (e.g. early distributive or septic shock)
		![[Pasted image 20260612234330.png]]
	- The ultrasound machine automatically integrates the velocity over time to calculate the **Velocity Time Integral (VTI)**, which is displayed in centimetres
		- This represents the total distance the red blood cells travel in one beat (cylinder height)
3. Calculation and dynamic application
	- Deriving stroke volume using the formula $\text{Stroke Volume}=\pi \times\left( \frac{\text{LVOT Diameter}}{2} \right)^2\times \text{LVOT VTI}$ 
	- Assessing fluid responsiveness:
		- Calculate the baseline SV and re-evaluate it during a dynamic manoeuvre like a passive leg raise or a mini fluid challenge
		- A **≥ 12% increase in Stroke Volume** indicates a positive response, demonstrating that the patient has preload reserve and will tolerate/benefit from fluid resuscitation
		- If the increase is **< 12%**, the patient is on the flat portion of the Frank-Starling curve; withhold fluids and look toward vasopressors or inotropes instead
## Carotid VTI
- Can use a linear probe
- Find the carotid bifurcation in short axis view

## End Expiratory Occlusion Test
- Perform an expiratory pause for 15s
- Look for a pulse pressure variation >5%
- Patients can be breathing above the ventilator and don’t have to be sinus rhythm
## Passive Leg Raise
- Don’t have to be in sinus rhythm and don’t have to be mechanically ventilated
- Sit the patient upright at 45° and measure stroke volume then lie then flat and lift up their legs to 45° and measure stroke volume 

## Challenges
### Passive leg raise
- Method
	- Start with the patient semi-recumbent at 45°
	- Raise legs to 45° while simultaneously lowering the torso to flat (or raise legs from flat if already supine)
	- This transfers ~300 mL of venous blood from the lower limbs into the central circulation — an autologous, reversible fluid challenge
	- Assess CO or a surrogate at baseline and at **60–90 seconds** after position change (effect is transient)
	- Return patient to original position — the effect is fully reversible
- Positive: ≥10% increase in cardiac output (or arterial pulse pressure as a surrogate)
- Limitations
	- Cannot be performed if: raised intracranial pressure, unstable pelvic/femoral fractures, intra-abdominal hypertension (may not transfer adequate volume)
	- Requires real-time CO measurement — qualitative BP change alone is insufficient
	- Must measure CO response within 60–90 seconds (effect wanes)
### Mini Fluid Challenge
- Technique: Give 100 mL of crystalloid over 1 minute and assess CO response (via arterial PP or POCUS VTI)
- Positive: ≥6% increase in PP or VTI → likely fluid responsive
## Measures
- Best: POCUS VTI (left ventricular outflow tract velocity-time integral) — multiply by LVOT area for CO; serial VTI alone is sufficient for trending
- Acceptable: arterial pulse pressure change (less precise but reasonable)
- Pulse oximetry pleth waveform: some evidence but unreliable in vasoconstriction
- Avoid: relying on BP alone — MAP change is an insensitive surrogate for CO change

# Sources
- [Haney Mallemat The Art and Science of Fluid Responsiveness - YouTube](https://www.youtube.com/watch?v=HdT6T65dUP0)
- [How to use the LVOT VTI to determine fluid responsiveness for the critically ill patient - YouTube](http://www.youtube.com/watch?v=B4bt76CaZFk)
- [LVOT VTI Explained Clearly \| Master Cardiac Output with Bedside Ultrasound POCUS \| 2026 - YouTube](https://www.youtube.com/watch?v=aRlTgP3BdYQ)
- [Ultrasound Podcast - CAROTID VTI PASSIVE LEG RAISE FOR VOLUME RESPONSIVENESS. - YouTube](https://www.youtube.com/watch?v=ML_3w7UUIls)