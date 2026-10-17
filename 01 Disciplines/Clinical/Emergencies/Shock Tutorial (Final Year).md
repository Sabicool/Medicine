---
title: Approach to Undifferentiated Shock
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
> This is the outline for review, not the finished deck. Each `##` is one slide (`###` is a branch beneath it), `---` forces a slide break, `> [!notes]` is what I'd say (speaker notes: press S) and `> [!question]` is what I'd put to the group. `[GAP: …]` marks something still to sort out. `draft: true` keeps it off the site until we're happy with it.
>
> **Session plan (~85 min)**
> - Opening and objectives (5 min)
> - The framework: one equation, four mechanisms (8 min)
> - Recognising shock (5 min)
> - The approach: resuscitate while you differentiate (10 min)
> - Case 1: Mrs P (18 min)
> - Case 2: Mr T (16 min)
> - Case 3: Mr K, including the obstructive mimic (16 min)
> - Putting it together and quick-fire (5 min)
> - Wrap-up: your first 15 minutes (2 min)
>
> The cases are headed by patient rather than by shock type, so the slide title doesn't give the answer away. Each case opens on a live monitor and a board of face-down findings: tiles only turn over (click, or press 1–9) when someone asks for that finding. Each case then has one decision slide; clicking a choice jumps to that branch, where the monitor trends to the new numbers, and "Continue →" rejoins the main path (right arrow skips the branches). Press A to turn on the QRS tone, whose pitch falls with the SpO₂.
>
> Syntax: `> [!monitor] Patient` with `- HR:`, `- BP:`, `- SpO2:`, `- RR:`, `- Temp:`, and optionally `- ART:`, `- EtCO2:`, `- Rhythm: AF`, `- ST: elevated`, `- Time: 02:04`, `- Over: 20` (seconds to trend from the last slide for the same patient). `> [!findings] Prompt` with `- Label: finding`. `> [!choice] Prompt` with a list of `[[#Heading|Label]]` links.

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

- Recognise shock before the blood pressure falls
- Classify shock by mechanism using one equation
- Use a structured approach to the undifferentiated shocked patient: resuscitate while you work out the type
- Tell the types apart at the bedside, and know when to escalate

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

> [!question]
> If perfusion pressure is low, which terms could be responsible?

## Where it can fail

![[shock-equation.svg]]

> [!notes]
> This is the answer to the last question drawn out. Each red arrow is a fall in one term and the shock type it produces. Tachycardia sits under heart rate here, but it really causes shock by shortening diastolic filling time, so it's a preload problem too ([[Shock#Pathophysiology]]).

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
> Panel A is a 68-year-old woman in cardiogenic shock from adenoviral myocarditis (BP 70/50, HR 125, lactate 4.5, LVEF 25%). Panel B is the same legs within 24 hours of treatment with ventilation, volume expansion and inotropes, and her EF had recovered to 60% by day 3. Mottling is violaceous discolouration from skin hypoperfusion, and it's most often seen around the knees (also the ears and fingers), so the knees are the place to look. In [[Shock#Clinical Features]] I've noted mottling suggests active vasoconstriction and a need for inotropy, which is exactly what this patient got, and it comes back in Case 3.

---

# The Approach

## Resuscitate while you differentiate

1. **Recognise** it's shock and call for help
2. **Primary survey:** ABC, monitoring, exclude the immediate killers
3. **Differentiate at the bedside:** peripheries, heart rate, filling (PUMPS), POCUS
4. **Empirical resuscitation:** fluid challenge, vasopressor, specific treatment
5. **Secondary survey:** history, examination and investigations for the cause
6. **Reassess and escalate**

> [!notes]
> This is the structure of [[Shock#Approach to Undifferentiated Shock]] and every case from here follows it. The point I'd make is that steps 2–4 happen at the same time: you don't wait to know the type before starting to resuscitate, but you also don't keep pouring fluid in without asking why they're shocked.

## The primary survey

- Call for senior help early
- A, B, C with monitoring on
- Exclude the things that kill quickly: tension pneumothorax, massive haemothorax, external haemorrhage, anaphylaxis, tamponade, massive PE
- IV access, bloods including cultures, ABG/VBG with lactate, 12-lead ECG
- Peri-arrest? Adrenaline 0.1 mg boluses to buy time while setting up an infusion

> [!notes]
> Condensed from [[Shock#Primary Survey]] and [[Shock#Empirical Resuscitation]]. For final years I'd leave out ETCO₂ and the equipment checks and keep the "exclude the reversible killers" framing.

## Three bedside questions

- **Peripheries:** warm or cold? (SVR)
- **Heart rate:** fast, slow or normal?
- **Filling:** full or empty?

> [!notes]
> This is the callout in [[Shock#Primary Survey]] and I'd like it to be the spine of every case from here on. The first two are quick; filling is the one people struggle with, hence the next slide.

## Assessing filling: PUMPS

- **P**eripheral perfusion: capillary refill time, systolic BP, pulse pressure
- **U**rine output
- **M**ucous membranes and skin turgor
- **P**ressure in the neck: JVP
- **S**igns of volume overload: peripheral oedema, hepatojugular reflux, S3 gallop, lung crackles

> [!question]
> Which of these can you check in the first two minutes?

> [!notes]
> This is the mnemonic I use myself. None of these are good at predicting whether a bolus will help on their own, which comes up again in Case 1, but together they give you a reasonable idea of whether the patient is dry or overloaded. Passive leg raise is the dynamic test they can do on the ward.

## History that points to the type

| Ask about | Think |
| --- | --- |
| Chest pain, diaphoresis, known cardiac disease | Cardiogenic |
| Fevers, rigors, immunosuppression | Septic |
| Allergen exposure | Anaphylaxis |
| Trauma, blood loss | Hypovolaemic |
| Recent chest procedure, malignancy | Obstructive |
| Exogenous steroids, adrenal disease | Adrenal crisis |

> [!notes]
> From the important history points in [[Shock#Secondary Survey]]. Also worth reminding them to look at the drug chart and what's happened in the last few hours (recent procedures, new drugs, collateral from the nurse), since on the ward that's often where the answer is.

---

# Case 1: Mrs P

## Mrs P, 78
<!-- slide: fragments=none -->

Rapid response call, ward 7. Day 2 of an admission for a UTI, and the nurse says she's "not herself".

> [!findings] Ask for it
> - General: confused, flushed
> - Peripheries: warm, CRT 2 s
> - Knees: no mottling
> - JVP: not visible
> - Mucous membranes: dry
> - Chest: clear
> - Urine output: 40 mL in 4 hours (60 kg)
> - VBG: lactate 4.6

> [!monitor] Mrs P, 78
> - HR: 118
> - BP: 82/45
> - SpO2: 94
> - RR: 26
> - Temp: 38.9
> - Time: 02:04

> [!notes]
> Don't turn a tile over until someone asks for it (click it, or press its number). If nobody asks about the knees, the JVP or the urine output, that's the teaching point. Is she shocked? Run the approach: what are the peripheries, heart rate and filling telling you?

## Warm, fast, empty: distributive

- **Peripheries:** warm, CRT 2 s → low SVR
- **Heart rate:** 118 → fast
- **Filling (PUMPS):** dry mucous membranes, JVP not visible, no signs of overload, urine output ≈ 0.17 mL/kg/h → empty
- With a fever and a known UTI, this is septic shock until proven otherwise

> [!notes]
> Worth pointing out that she's both vasodilated *and* dry, probably from not drinking much while unwell. That's the "more than one type can co-exist" point from [[Shock#Secondary Survey]], and it's why she'll respond to some fluid before she needs a pressor.

## Sepsis and septic shock (Sepsis-3)

- **Sepsis:** life-threatening organ dysfunction due to a dysregulated host response to infection
	- Organ dysfunction = increase in SOFA score ≥ 2
- **Septic shock:** sepsis plus both
	- Hypotension requiring vasopressors
	- Lactate > 2 mmol/L

> [!notes]
> From [[Sepsis#Diagnostic Criteria]]. Mrs P has sepsis now, and becomes septic shock if she still needs a vasopressor after fluid, which is where this case goes. Worth saying that we screen with SIRS or MEWS on the ward rather than qSOFA.

## Mrs P: what do you do first?
<!-- slide: fragments=none -->

> [!choice] Pick one
> - [[#A bolus, then reassess|500 mL Hartmann's over 15 min, then reassess]]
> - [[#Two litres stat|2 L of fluid stat]]
> - [[#Noradrenaline straight away|Start noradrenaline now]]
> - [[#Waiting for the bloods|Take bloods and wait for the results]]

> [!monitor] Mrs P, 78
> - HR: 118
> - BP: 82/45
> - SpO2: 94
> - RR: 26
> - Temp: 38.9

> [!notes]
> Take a vote, then click the choice. Whatever they pick, someone should say cultures and antibiotics within the hour; if nobody does, ask. Right arrow skips the branches and carries on.

### A bolus, then reassess

> [!monitor] Mrs P, 78
> - HR: 106
> - BP: 96/52
> - SpO2: 95
> - RR: 23
> - Temp: 38.9
> - Over: 20

- MAP 67, CRT faster, a bit more alert
- That's a fluid challenge: give it, then look at the patient again
- Is she still underfilled? Then another bolus, and reassess again

[[#Fluids, done properly|Continue →]]

> [!notes]
> The answer I'm hoping for. The point to draw out is the reassessment rather than the volume: perfusion, mental state and urine output, not just the BP.

### Two litres stat

> [!monitor] Mrs P, 78
> - HR: 112
> - BP: 92/50
> - SpO2: 89
> - RR: 32
> - Temp: 38.9
> - Over: 25

- MAP up a little, but she's now short of breath
- Crackles at both bases, SpO₂ 89%
- She's 78: fluid overload is harmful too
- Give fluid as a challenge, and reassess after each one

[[#Fluids, done properly|Continue →]]

> [!notes]
> From [[Shock#Vasopressors and Ionotropes]] (fluid overload is harmful) and [[Fluid Responsiveness#Fluid Tolerance]]: B-lines on lung ultrasound appear before the other signs of overload.

### Noradrenaline straight away

> [!monitor] Mrs P, 78
> - HR: 114
> - BP: 90/50
> - SpO2: 94
> - RR: 26
> - Temp: 38.9
> - Over: 20

- Not wrong: start noradrenaline early, and peripherally is fine short-term
- But she's dry as well as vasodilated, so she needs some fluid too
- Her urine output hasn't picked up

[[#Fluids, done properly|Continue →]]

> [!notes]
> From [[Shock#Vasopressors and Ionotropes]]. ARISE FLUIDS (2026) found no mortality difference between restrictive fluid with early vasopressors and the usual approach ([[Sepsis#Assess Need for Further Fluid Resuscitation]]), so this is a defensible choice. The PUMPS findings are what tell you she's also empty.

### Waiting for the bloods

> [!monitor] Mrs P, 78
> - HR: 132
> - BP: 74/38
> - SpO2: 91
> - RR: 32
> - Temp: 39.2
> - Over: 25

- 40 minutes later: more confused, MAP 50
- You already had a lactate from the VBG
- Shock doesn't wait for a lab result
- Antibiotics within 1 hour of recognising septic shock, after cultures

[[#Fluids, done properly|Continue →]]

> [!notes]
> From [[Sepsis#Fluid Resuscitation]]. Resuscitation and investigations happen at the same time.

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

## An hour later: 2 L in, MAP 58

> [!monitor] Mrs P, 78
> - HR: 112
> - BP: 86/44
> - SpO2: 94
> - RR: 25
> - Temp: 38.7
> - Time: 03:05
> - Over: 10

- Start noradrenaline; don't wait for large fluid volumes
- Peripheral vasopressors are acceptable short-term through a large proximal vein
- Target MAP 65 (60–65 if aged ≥ 65)
- Escalate to ICU

> [!notes]
> From [[Shock#Vasopressors and Ionotropes]] and [[Sepsis#Management]]. SEPSISPAM showed no benefit at MAP 80–85. She now meets the Sepsis-3 definition of septic shock. I'd mention hydrocortisone for vasopressor-refractory septic shock only briefly, since that's an ICU decision.

## Noradrenaline running

> [!monitor] Mrs P, 78
> - HR: 102
> - BP: 104/54
> - SpO2: 95
> - RR: 22
> - Temp: 38.5
> - Over: 30

- MAP 71: at target
- Now reassess perfusion: CRT, mental state, urine output, repeat lactate
- ICU review for ongoing vasopressor needs

> [!notes]
> Let the monitor settle in silence for a few seconds; it's a nice end to the case. Then ask what they'd hand over to ICU.

---

# Case 2: Mr T

## Mr T, 34
<!-- slide: fragments=none -->

Motorbike vs car at 60 km/h. Ambulance handover in resus.

> [!findings] Ask for it
> - Airway: talking, anxious
> - Chest: equal air entry, no crepitus
> - Peripheries: cool to the knees, CRT 4 s
> - JVP: not visible
> - Abdomen: soft, non-tender
> - Pelvis: no pain on palpation
> - Left thigh: deformed, swollen, tense
> - eFAST: no free fluid or haemothorax

> [!monitor] Mr T, 34
> - HR: 124
> - BP: 108/84
> - SpO2: 97
> - RR: 28
> - Time: 14:20

> [!notes]
> His BP is normal. Is he shocked? Same rule as before: tiles only turn over when they're asked for.

## Cold, fast, empty: hypovolaemic

- **Peripheries:** cool to the knees, CRT 4 s → vasoconstricted
- **Heart rate:** 124 → fast
- **Filling (PUMPS):** narrow pulse pressure, JVP not visible → empty
- In trauma, that's haemorrhage until proven otherwise

> [!notes]
> The thing I want them to notice is that he's cold and empty, which looks the same as Mrs P on the filling question but the opposite on the peripheries. That's the SVR question doing the work.

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
> The eFAST and retroperitoneum points come from [[Rush Exam]]. For Mr T it's the thigh.

## Mr T: what now?
<!-- slide: fragments=none -->

> [!choice] Pick one
> - [[#Two litres of crystalloid|2 L of crystalloid to get his BP up]]
> - [[#Major haemorrhage protocol|Activate the MHP, give TXA, splint the femur, call ortho]]
> - [[#A pressor for Mr T|Start noradrenaline]]
> - [[#Off to CT|Send him to CT to find the source]]

> [!monitor] Mr T, 34
> - HR: 128
> - BP: 102/82
> - SpO2: 97
> - RR: 28
> - Over: 40

> [!notes]
> His numbers drift while they argue, which is the point.

### Two litres of crystalloid

> [!monitor] Mr T, 34
> - HR: 136
> - BP: 84/62
> - SpO2: 96
> - RR: 30
> - Temp: 35.4
> - Over: 30

- BP rose for ten minutes, then fell further
- Now 35.4 °C, and his INR is 1.6
- Crystalloid carries no oxygen and no clotting factors
- Bleeding patients need blood, with restricted volume replacement

[[#Managing haemorrhagic shock|Continue →]]

> [!notes]
> From [[Shock#Haemorrhagic Shock]]: temperature < 35 °C and INR > 1.5 are both MHP markers of critical physiological derangement. The European guideline recommends restricted volume replacement.

### Major haemorrhage protocol

> [!monitor] Mr T, 34
> - HR: 112
> - BP: 92/64
> - SpO2: 98
> - RR: 24
> - Over: 30

- Blood products in a ratio no lower than 2:1:1, through a warmer
- TXA within 3 hours of injury
- Splinting the femur and getting him to definitive haemorrhage control
- SBP 92: no need to push higher until the bleeding is stopped

[[#Managing haemorrhagic shock|Continue →]]

> [!notes]
> The answer I'm hoping for. Permissive hypotension (SBP 80–90) is a good one to make them justify: what would change if he had a head injury? (MAP ≥ 80.)

### A pressor for Mr T

> [!monitor] Mr T, 34
> - HR: 130
> - BP: 112/88
> - SpO2: 97
> - RR: 28
> - Over: 15

- The BP looks better…
- …but he's still bleeding and still empty: HR 130, pulse pressure 24
- Vasopressors aren't the answer to an empty tank
- Noradrenaline only if restricted fluid can't hold the target

[[#Managing haemorrhagic shock|Continue →]]

> [!notes]
> From the European guideline (Recommendation 14) in [[Shock#Haemorrhagic Shock]].

### Off to CT

> [!monitor] Mr T, 34
> - HR: 142
> - BP: 76/58
> - SpO2: 95
> - RR: 32
> - Over: 30

- Halfway through the scan, the radiographer calls: BP 76/58
- He's in a corridor with no blood running
- Resuscitate and control the bleeding first; CT is for once he's stable

[[#Managing haemorrhagic shock|Continue →]]

> [!notes]
> `[GAP: "CT is for the stable patient" is my wording, from general trauma teaching rather than your notes. Check you're happy with it]`

## Managing haemorrhagic shock

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

---

# Case 3: Mr K

## Mr K, 66
<!-- slide: fragments=none -->

ED. Two hours of central chest pain, and he's sweaty.

> [!findings] Ask for it
> - Peripheries: cold, clammy, CRT 5 s
> - Knees: mottled
> - JVP: raised, 6 cm
> - Chest: bibasal crackles
> - Legs: pitting oedema to the shins
> - Heart sounds: soft, no murmur
> - 12-lead ECG: anterior ST elevation
> - VBG: lactate 5.2

> [!monitor] Mr K, 66
> - HR: 108
> - BP: 84/60
> - SpO2: 89
> - RR: 30
> - Time: 10:15

> [!notes]
> Same again: they ask, you turn tiles over.

## Cold, fast, full

- **Peripheries:** cold, mottled → vasoconstricted, low output
- **Heart rate:** 108 → fast
- **Filling (PUMPS):** JVP up, crackles, oedema → full
- With chest pain and ST elevation, cardiogenic shock is most likely…
- …but obstructive shock is cold and full too

> [!notes]
> I'd leave the "but" hanging; it's what the POCUS branch answers.

## Mr K: what next?
<!-- slide: fragments=none -->

> [!choice] Pick one
> - [[#A bolus for Mr K|500 mL fluid bolus]]
> - [[#Noradrenaline, then dobutamine|Noradrenaline, then dobutamine]]
> - [[#POCUS first|Bedside POCUS first]]

> [!monitor] Mr K, 66
> - HR: 110
> - BP: 82/58
> - SpO2: 88
> - RR: 30
> - Over: 30

### A bolus for Mr K

> [!monitor] Mr K, 66
> - HR: 116
> - BP: 82/58
> - SpO2: 82
> - RR: 36
> - Over: 20

- No change in BP
- Crackles now to the mid zones, SpO₂ 82%
- He was already full: this is the fluid you can't take back

[[#Probably not|Continue →]]

### Noradrenaline, then dobutamine

> [!monitor] Mr K, 66
> - HR: 104
> - BP: 98/64
> - SpO2: 91
> - RR: 28
> - Over: 25

- MAP up first with noradrenaline, then dobutamine for perfusion
- Right drugs, right order
- But nobody has looked at the heart yet. Is it really pump failure?

[[#POCUS first|Look with POCUS]] · [[#Probably not|Continue →]]

> [!notes]
> From [[Acute Heart Failure#Management]]. In a hypotensive patient, MAP comes first with noradrenaline, since dobutamine can drop the BP further.

### POCUS first

> [!findings] What does the probe show?
> - LV: severely impaired, anterior wall not moving
> - RV: normal size
> - Pericardium: no effusion
> - IVC: plethoric
> - Lungs: bilateral B-lines

- Pump failure: this is cardiogenic shock

[[#What if it had looked like this?|What if it hadn't been the pump?]] · [[#Probably not|Continue →]]

> [!notes]
> From [[Rush Exam]]. A plethoric IVC fits cardiogenic or obstructive, so it's the LV and the pericardium that decide it here.

### What if it had looked like this?

| Cause | POCUS | Treatment |
| --- | --- | --- |
| Massive PE | Dilated RV, McConnell's sign | Thrombolysis (alteplase 100 mg: 10–20 mg bolus, rest over 2 h) |
| Tamponade | Effusion, RV diastolic collapse | Pericardiocentesis |
| Tension pneumothorax | No lung sliding | Needle decompression |

- Obstructive shock: cold and full, but the heart muscle isn't the problem
- Fluids and pressors only buy time; the obstruction has to be relieved

[[#RUSH, pump, tank, pipes|The RUSH exam]] · [[#Probably not|Continue →]]

> [!notes]
> From [[Pulmonary Embolism]], [[Emergency Pericardiocentesis]] and [[Pneumothorax#Decompensated (Tension) Pneumothorax]]. In massive PE the risk of fluid generally outweighs the benefit, the same "don't flood the RV" message as the bolus branch.

### RUSH, pump, tank, pipes

![[Rush Exam#^overview]]

[[#Probably not|Continue →]]

> [!notes]
> From [[Rush Exam]]. The ultrasound images in that note are from The POCUS Atlas (CC BY-NC 4.0), so they're fine to show with attribution.

## Probably not

Only give fluid if all of these are true:
- End-organ perfusion is inadequate
- No pulmonary congestion (e.g. no B-lines)
- The overall picture suggests true hypovolaemia
- Dynamic indices suggest he's fluid responsive

> [!notes]
> From [[Acute Heart Failure#Management]]. Mr K has crackles and a raised JVP, so he fails at least two of these.

## Cold and wet

![[haemodynamic-profiles.svg]]

> [!notes]
> I'd use this to compare him with Mrs P: she was warm and dry, he's cold and wet. That contrast is most of the bedside differentiation they need.

## Managing cardiogenic shock

- 12-lead ECG and POCUS early
- Support the lungs: CPAP/BiPAP
- Noradrenaline first to restore MAP (and coronary perfusion)
- Then dobutamine if still poorly perfused (cold, mottled)
- Adrenaline alone is reasonable as a short-term bridge
- Treat the cause: revascularisation for ACS
- Escalate early: ICU and cardiology

> [!notes]
> From [[Acute Heart Failure#Management]]. I'd name IABP, Impella and ECMO only so they've heard of them, and mention that IABP-SHOCK II showed an IABP isn't for everyone.

---

# Putting It Together

## Same three questions, different answers

| | Peripheries | Heart rate | Filling | Clue |
| --- | --- | --- | --- | --- |
| Mrs P: distributive | Warm | Fast | Empty | Fever, source |
| Mr T: hypovolaemic | Cold | Fast | Empty | Trauma, blood loss |
| Mr K: cardiogenic | Cold | Fast | Full | Chest pain, crackles |
| Obstructive | Cold | Fast | Full | Often a clear chest; POCUS |
| Neurogenic | Warm | **Slow** | Empty | Spinal injury |

> [!notes]
> The three cases side by side, plus obstructive (Mr K's mimic) and neurogenic, since that's the one where heart rate is the giveaway. Cardiogenic and obstructive look the same on the three questions, which is why POCUS matters. Real patients are messier than this table, and mixed shock is common, so I'd present it as a starting point rather than a rule.

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

1. Recognise it and call for help
2. Primary survey: ABC, monitoring, access, VBG with lactate, ECG
3. Differentiate: peripheries, heart rate, filling (PUMPS), POCUS
4. Resuscitate: fluid challenge, pressor, inotrope, blood, or fix the obstruction
5. Secondary survey: history, examination, investigations
6. Reassess, and escalate

> [!notes]
> Back to the opening question: compare this list with what they said at 0200.

## Take-home

- Shock is a failure of oxygen delivery; BP falls late
- $\text{MAP} - \text{CVP} = \text{CO} \times \text{SVR}$ tells you where to look
- Warm vs cold, fast vs slow, full vs empty (PUMPS)
- Resuscitate while you differentiate, and reassess after everything you give
- More than one type can co-exist (e.g. sepsis + hypovolaemia)
- Full notes: [[Shock]]
