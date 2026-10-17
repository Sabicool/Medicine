---
aliases:
  - Shock Teaching
Rotations:
  - "[[02 Rotations/Emergency Medicine|Emergency Medicine]]"
  - "[[02 Rotations/Intensive Care Unit|Intensive Care Unit]]"
date: 2026-10-17
description: A case-based tutorial for final year medical students
draft: true
slides: true
---
> [!info] Outline status
> This is the outline for review, not the finished deck. Each `##` is one slide, `---` forces a slide break, `> [!notes]` is what I'd say (speaker notes, once the emitter supports them) and `> [!question]` is what I'd put to the group. `[GAP: …]` marks something still to sort out. `draft: true` keeps it off the site until we're happy with it.
>
> **Session plan (~80 min)**
> - Opening and objectives (7 min)
> - The framework: one equation, four mechanisms (10 min)
> - Recognising shock (5 min)
> - Case 1: septic shock (18 min)
> - Case 2: haemorrhagic shock (14 min)
> - Case 3: cardiogenic shock (12 min)
> - Case 4: obstructive shock, the twist (8 min)
> - Quick-fire: the ones you can't miss (4 min)
> - Wrap-up: your first 15 minutes (2 min)

# Opening

## Rapid response call, 0200

- Ward 7, bed 12: "BP 78/40"
- You're the first doctor there

> [!question]
> What are the first three things you'd do when you walk into the room?

> [!notes]
> I'd let them answer before showing anything else. The point is to see whether anyone says "call for help" or "look at the patient" before "give fluids", and I'll come back to their answers at the very end.

## What if the BP was 93/60?

- Does that change anything?
- What if the patient is 22? What if they're 85?

> [!question]
> Is 93/60 "normal"? What else would you want to know?

> [!notes]
> What I'm after is that a number on its own doesn't make the diagnosis. The definition in [[Shock#Clinical Features]] is MAP < 65 *or a significant drop from baseline*, so I'd want to know their usual BP and, more importantly, whether they look perfused. A young patient can sit at 93/60 while compensating with tachycardia and vasoconstriction, and hypotension comes late for them, which sets up Case 2. An older patient who usually runs at 160 systolic may be shocked at a BP that looks fine on the chart.

## By the end of this session you should be able to

- Define shock in terms of oxygen delivery, not blood pressure
- Classify shock by mechanism using one equation
- Tell the types apart at the bedside with three questions
- Start resuscitation in the first 15 minutes, and know when to escalate

# The Framework

## What is shock?

- Inadequate tissue oxygen delivery: $DO_{2}<\dot{V}O_{2}$
- Almost always mediated by low blood pressure, but hypotension is the consequence, not the definition

> [!notes]
> Source: [[Shock#Definition]]. I want them to leave thinking of shock as a supply–demand problem, which is why the haemorrhage case starts with a normal BP.

## One equation

$$
\underset{\text{Perfusion Pressure}}{\text{MAP} - \text{CVP}} = \text{CO} \times \text{SVR}
$$

- $\text{CO}=\text{HR}\times \text{SV}$
- SV depends on preload, contractility and afterload

`[FIGURE: shock-equation.svg, TikZ. The equation with each term branching to the shock type it causes: ↓preload → hypovolaemic/obstructive, ↓contractility → cardiogenic, ↓/↑HR → arrhythmic, ↓SVR → distributive]`

> [!question]
> If perfusion pressure is low, which terms could be responsible?

## Four mechanisms

| Mechanism | Problem | Examples |
| --- | --- | --- |
| Hypovolaemic | ↓ preload | Haemorrhage, GI losses, burns |
| Cardiogenic | ↓ contractility / rhythm | Acute MI, myocarditis, heart block |
| Obstructive | ↓ venous return / outflow | PE, tamponade, tension pneumothorax |
| Distributive | ↓ SVR | Sepsis, anaphylaxis, spinal injury |

> [!notes]
> Condensed from [[Shock#Classification]]. The full list stays in the note and I'll point them to it at the end, rather than putting four screens of causes on a slide.

## A better mnemonic: PROVED?

- **P**ump
- **R**hythm
- **O**bstructive
- **V**olume
- **E**ndocrine
- **D**istributive
- **?** Is it real?

> [!notes]
> I prefer PROVED? over CHOD because it makes you think of rhythm and endocrine causes, and the "?" is something I actually see on the ward: a cuff that's too big or an art line transducer sitting at the wrong height.

# Recognising Shock

## Shock is a clinical diagnosis

- **Haemodynamics:** MAP < 65 or a big drop from baseline, shock index (HR/SBP) > 0.8
- **Skin:** cool knees and hands, mottling, CRT > 5 s
- **Kidneys:** urine output < 0.5 mL/kg/h
- **Brain:** agitation → delirium → drowsiness
- **Blood:** ↑ lactate, ↓ HCO₃⁻

> [!notes]
> Source: [[Shock#Clinical Features]]. I'd spend most of the time on the skin, since it's free, fast and the thing students under-examine.

## Look at the knees

![[NEJM skin mottling Contou 2016.webp]]

*Contou D, de Prost N. Skin Mottling. N Engl J Med 2016;375:2187. doi:[10.1056/NEJMicm1602055](https://doi.org/10.1056/NEJMicm1602055)*

> [!question]
> What's the difference between A and B?

> [!notes]
> `[GAP: confirm what panel B shows in the original (same patient after resuscitation?) so I describe it correctly]`. Mottling starts around the knees and spreads outwards, so the knees are the place to look. In [[Shock#Clinical Features]] I've noted mottling suggests active vasoconstriction, which comes back in Case 3.

---

# Case 1: Septic Shock

## Mrs P, 78

- Day 2 of admission for a UTI, nurse calls because she's "not herself"
- HR 118, BP 82/45 (MAP 57), RR 26, T 38.9 °C, SpO₂ 94% on room air
- Confused, warm peripheries, CRT 2 s
- VBG: lactate 4.6

> [!question]
> Is she shocked? What type? What's your next move?

## Approach: the primary survey

- Call for senior help early
- A, B, C with monitoring on
- Exclude the things that kill quickly: tension pneumothorax, haemorrhage, anaphylaxis, tamponade
- IV access, bloods including cultures, ABG/VBG with lactate, ECG

> [!notes]
> Condensed from [[Shock#Primary Survey]]. For final years I'd leave out ETCO₂ and the equipment checks and keep the "exclude the reversible killers" framing.

## Three bedside questions

- **Peripheries:** warm or cold? (SVR)
- **Heart rate:** fast, slow or normal?
- **Filling:** JVP, response to passive leg raise

> [!notes]
> This is the callout in [[Shock#Primary Survey]] and I'd like it to be the spine of every case from here on. Warm peripheries, tachycardia and low filling fits distributive.

## Sepsis and septic shock (Sepsis-3)

- **Sepsis:** life-threatening organ dysfunction due to a dysregulated host response to infection
	- Organ dysfunction = increase in SOFA score ≥ 2
- **Septic shock:** sepsis plus both
	- Hypotension requiring vasopressors
	- Lactate > 2 mmol/L

> [!notes]
> From [[Sepsis#Diagnostic Criteria]]. Mrs P has sepsis now, and becomes septic shock if she still needs a vasopressor after fluid, which is where this case goes. Worth saying that we screen with SIRS or MEWS on the ward rather than qSOFA.

## Fluids, done properly

- Give as a challenge: 250–500 mL over 10–15 min, then reassess
- 30 mL/kg within the first 3 hours for sepsis
- Balanced crystalloid (Hartmann's, Plasma-Lyte) in most patients

> [!question]
> "Don't we always give normal saline?"

## Saline or balanced crystalloid?

- Balanced crystalloid is generally preferred in septic shock
	- A conditional recommendation from the Surviving Sepsis Campaign, based on low quality evidence
- Normal saline is preferred in:
	- Hypochloraemic alkalosis (e.g. vomiting, NGT losses)
	- Hyperkalaemia
	- Traumatic brain injury
	- Meningitis

> [!notes]
> From [[Shock#Empirical Resuscitation]] and [[Sepsis#Fluid Resuscitation]]. I'd say plainly that the evidence here isn't strong, so they shouldn't be surprised to see saline used a lot. What matters more is the volume and reassessing after each bolus.

## We're bad at predicting who needs fluid

- Being fluid responsive doesn't mean the patient *needs* fluid
- MAP and urine output lag behind and don't reliably predict fluid responsiveness
- So give a bolus, then ask whether the patient actually got better:
	- Capillary refill time and mottling
	- Urine output
	- Repeat lactate at 2 hours (aim for > 10% clearance)
	- Mental state

> [!notes]
> From [[Fluid Responsiveness]] and [[Sepsis#Assess Need for Further Fluid Resuscitation]]. The line from my note I'd paraphrase is: don't be the person who decides a patient is fluid responsive, gives the bolus, and never checks whether they improved. I'd mention passive leg raise as the one dynamic test they can do on the ward, but I wouldn't go into PPV or VTI.

## She's had 2 L and her MAP is 60

- Start noradrenaline early; don't wait for large fluid volumes
- Peripheral vasopressors are acceptable short-term through a large proximal vein
- Target MAP 65 (60–65 if aged ≥ 65)
- Antibiotics within 1 hour, after cultures
- Escalate to ICU

> [!notes]
> From [[Shock#Vasopressors and Ionotropes]] and [[Sepsis#Management]]. SEPSISPAM showed no benefit at MAP 80–85. Also worth mentioning that ARISE FLUIDS (2026) found no mortality difference between a restrictive fluid/early vasopressor approach and the usual approach, so there isn't a single right answer on how much fluid before starting a pressor. I'd mention hydrocortisone for vasopressor-refractory septic shock only briefly, since that's an ICU decision.

---

# Case 2: Haemorrhagic Shock

## Mr T, 34

- Motorbike vs car at 60 km/h, brought in by ambulance
- HR 124, BP 108/84, RR 28, SpO₂ 97%
- Pale, cool to the knees, anxious
- Obvious deformity of the left thigh

> [!question]
> His BP is normal. Is he shocked?

## The shock index

$$
\text{Shock index} = \frac{\text{HR}}{\text{SBP}}
$$

- > 0.8 is elevated
- Mr T: 124 ÷ 108 ≈ 1.15
- Also look at his pulse pressure: 108 − 84 = 24 mmHg, which is narrow

> [!notes]
> From [[Shock#Haemorrhagic Shock]]. The European trauma guideline recommends shock index and pulse pressure to judge how hypovolaemic someone is. He's young, so he's holding his BP up by vasoconstricting and getting tachycardic, and that's what the narrow pulse pressure is showing. Hypotension in someone like him means he's lost a lot.

## Where's the blood? SCALPeR

- **S**calp / **S**treet
- **C**hest
- **A**bdomen
- **L**ong bones
- **P**elvis
- **R**etroperitoneum

> [!question]
> How would you look for each at the bedside in the first 10 minutes?

## Looking for it at the bedside

| Site | How |
| --- | --- |
| Scalp / street | Ambulance handover (blood at the scene), look at the scalp and under dressings |
| Chest | Examine, CXR, eFAST for haemothorax |
| Abdomen | Examine, eFAST for free fluid (Morison's pouch first) |
| Long bones | Examine for deformity, X-ray |
| Pelvis | Pelvic X-ray, binder if suspected |
| Retroperitoneum | Hard to find at the bedside: POCUS isn't sensitive, needs CT |

> [!notes]
> The eFAST and retroperitoneum points come from [[Rush Exam]]. `[GAP: the clinical-exam answers (scalp, long bones, pelvis) are my wording rather than from your notes. Check you're happy with them, particularly the pelvic binder]`

## Management

- Stop the bleeding: that's the definitive treatment
- Permissive hypotension: target SBP 80–90 until bleeding is controlled
	- Not in TBI: keep MAP ≥ 80
- Activate the major haemorrhage protocol
- Tranexamic acid within 3 hours: 1 g over 10 min, then 1 g over 8 h
- Noradrenaline only if restricted fluid can't hold the target

> [!notes]
> From [[Shock#Haemorrhagic Shock]]. Vasopressors aren't the answer to an empty tank, so the emphasis is on getting the bleeding stopped (theatre, IR, a binder) and replacing what's lost with blood rather than crystalloid.

## The major haemorrhage protocol

- Blood, not crystalloid
- RBC:FFP:PLT no lower than 2:1:1
	- At least 1 FFP for every 2 RBC
	- At least 1 adult unit of platelets for every 8 RBC
- Fibrinogen 3–4 g (cryoprecipitate or concentrate)
- Keep warm (≥ 35 °C), calcium up (iCa ≥ 1), and recheck bloods every 4 units

> [!notes]
> From the National Blood Authority guideline summarised in [[Shock#Haemorrhagic Shock]]. The ratio is the bit students ask about. The guideline says a high ratio may help but there's no good evidence for 1:1:1 over 2:1:1. I'd also mention the "lethal" triad of hypothermia, acidosis and coagulopathy, since the MHP thresholds (temp < 35, pH < 7.2, INR > 1.5) are really just that triad with numbers on it.

`[IMAGE: trauma shock algorithm. Currently a pasted image in Shock#Trauma Related Shock; check the source before showing it]`

---

# Case 3: Cardiogenic Shock

## Mr K, 66

- 2 hours of central chest pain, sweaty
- HR 108, BP 84/60, RR 30, SpO₂ 89% on room air
- Cold, clammy, mottled knees
- JVP up, bibasal crackles

> [!question]
> Would you give him a fluid bolus?

## Probably not

Only give fluid if all of these are true:
- End-organ perfusion is inadequate
- No pulmonary congestion (e.g. no B-lines)
- The overall picture suggests true hypovolaemia
- Dynamic indices suggest he's fluid responsive

> [!notes]
> From [[Acute Heart Failure#Management]]. Mr K has crackles and a raised JVP, so he fails at least two of these.

## Cold and wet

`[FIGURE: haemodynamic-profiles.svg, TikZ. 2×2 grid, warm/cold (perfusion) × dry/wet (congestion), with each shock type placed on it]`

> [!notes]
> I'd use this to compare him with Mrs P: she was warm and dry, he's cold and wet. That contrast is most of the bedside differentiation they need.

## Management

- 12-lead ECG and POCUS early
- Support the lungs: CPAP/BiPAP
- Noradrenaline first to restore MAP (and coronary perfusion)
- Then dobutamine if still poorly perfused (cold, mottled)
- Adrenaline alone is reasonable as a short-term bridge
- Treat the cause: revascularisation for ACS
- Escalate early: ICU and cardiology

> [!notes]
> From [[Acute Heart Failure#Management]]. The order matters: in a hypotensive patient you get the MAP up with noradrenaline first, since dobutamine can drop the BP further, then add dobutamine for perfusion. I'd name IABP, Impella and ECMO only so they've heard of them, and mention that IABP-SHOCK II showed an IABP isn't for everyone.

---

# Case 4: The Twist

## Mrs D, 58

- Day 4 after a hip replacement, sudden breathlessness
- HR 128, BP 80/50, RR 32, SpO₂ 86% on 6 L
- Cool peripheries, JVP up, chest clear

> [!question]
> Cold, raised JVP. Is this cardiogenic?

## Obstructive shock mimics pump failure

- Cold and congested, but the heart muscle isn't the problem
- The clear chest is the clue
- Causes: PE, tamponade, tension pneumothorax
- Fluids and pressors only buy time; the obstruction has to be relieved

## RUSH: pump, tank, pipes

![[Rush Exam#^overview]]

> [!notes]
> From [[Rush Exam]]. For Mrs D I'd expect a dilated RV (maybe McConnell's sign) and a plethoric IVC, which points to obstruction rather than an empty tank. The ultrasound images in that note are from The POCUS Atlas (CC BY-NC 4.0), so they're fine to show with attribution.

## Relieve the obstruction

| Cause | POCUS | Treatment |
| --- | --- | --- |
| Massive PE | Dilated RV, McConnell's sign | Thrombolysis (alteplase 100 mg: 10–20 mg bolus, rest over 2 h) |
| Tamponade | Effusion, RV diastolic collapse | Pericardiocentesis |
| Tension pneumothorax | No lung sliding | Needle decompression |

> [!notes]
> From [[Pulmonary Embolism]], [[Emergency Pericardiocentesis]] and [[Pneumothorax#Decompensated (Tension) Pneumothorax]]. In massive PE the risk of fluid generally outweighs the benefit, which is the same "don't flood the RV" message as Case 3.

---

# Quick-Fire

## Don't miss these

| Situation | Clue | First move |
| --- | --- | --- |
| Anaphylaxis | Exposure, urticaria, wheeze | Adrenaline 0.5 mg IM |
| Adrenal crisis | Steroid use, ↓Na ↑K | Hydrocortisone 100 mg IV + saline |
| Neurogenic | Spinal injury, warm + bradycardic | Exclude haemorrhage; fluid, then vasopressor (MAP 85–90) |
| Bradycardic | Heart block on ECG | Atropine → isoprenaline, pacing |
| "Is it real?" | Patient looks well | Recheck the cuff or line |

> [!notes]
> Drug doses from the table in [[Shock#Vasopressors and Ionotropes]], neurogenic from [[Shock#Neurogenic Shock]]. I'd run this as a quick-fire round, reading out the clue and having them call the diagnosis.

---

# Wrap-Up

## Your first 15 minutes

1. Call for help
2. ABC, monitoring, access, VBG with lactate
3. Three questions: peripheries, heart rate, filling
4. Treat the type: fluid challenge, pressor, inotrope, blood, or fix the obstruction
5. Reassess, and escalate

> [!notes]
> Back to the opening question: compare this list with what they said at 0200.

## Take-home

- Shock is a failure of oxygen delivery; BP falls late
- $\text{MAP} - \text{CVP} = \text{CO} \times \text{SVR}$ tells you where to look
- Warm vs cold, fast vs slow, full vs empty
- More than one type can co-exist (e.g. sepsis + hypovolaemia)
- Full notes: [[Shock]]
