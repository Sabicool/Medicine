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
> This is the outline for review, not the finished deck. Each `##` is one slide, `---` forces a slide break, `> [!notes]` is what I'd say (speaker notes, once the emitter supports them) and `> [!question]` is what I'd put to the group. `[GAP: …]` marks content that isn't in [[Shock]] yet and needs a source before it goes on a slide. `draft: true` keeps it off the site until we're happy with it.
>
> **Session plan (~75 min)**
> - Opening and objectives (5 min)
> - The framework: one equation, four mechanisms (10 min)
> - Recognising shock (5 min)
> - Case 1: septic shock (15 min)
> - Case 2: haemorrhagic shock (12 min)
> - Case 3: cardiogenic shock (12 min)
> - Case 4: obstructive shock, the twist (8 min)
> - Quick-fire: the ones you can't miss (5 min)
> - Wrap-up: your first 15 minutes (5 min)

# Opening

## You're the night intern

- Ward call at 0200: "Bed 12's BP is 78/40"
- You're the first doctor there

> [!question]
> What are the first three things you'd do when you walk into the room?

> [!notes]
> I'd let them answer before showing anything else. The point is to see whether anyone says "call for help" or "look at the patient" before "give fluids", and I'll come back to their answers at the very end.

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
> Source: [[Shock#Definition]]. I want them to leave thinking of shock as a supply–demand problem, which is why the haemorrhage case later starts with a normal BP.

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

`[IMAGE: mottling score / knee mottling photo. Replace the pasted image in Shock with one we're allowed to show]`

> [!notes]
> Source: [[Shock#Clinical Features]]. I'd spend most of the time on the skin, since it's free, fast and the thing students under-examine.

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

## Fluids, done properly

- Give as a challenge: 250–500 mL over 10–15 min, then reassess
- Generally 30 mL/kg in the first 3 hours for sepsis
- Balanced crystalloid (Hartmann's, Plasma-Lyte) over saline in most patients
- Fluid overload is harmful too

> [!question]
> What would make you choose normal saline instead?

> [!notes]
> Answer from [[Shock#Empirical Resuscitation]]: hypochloraemic alkalosis, hyperkalaemia, TBI, meningitis.

## She's had 2 L and her MAP is 60

- Start noradrenaline early; don't wait for large fluid volumes
- Peripheral noradrenaline is acceptable short-term through a large proximal vein
- Target MAP 65 (SEPSISPAM: no benefit at 80–85)
- Antibiotics after cultures
- Escalate to ICU

> [!notes]
> From [[Shock#Vasopressors and Ionotropes]]. `[GAP: antibiotic timing target for septic shock, with source]`. I'd mention hydrocortisone for vasopressor-refractory septic shock only briefly, since that's an ICU decision.

---

# Case 2: Haemorrhagic Shock

## Mr T, 34

- Motorbike vs car at 60 km/h, brought in by ambulance
- HR 124, BP 108/84, RR 28, SpO₂ 97%
- Pale, cool to the knees, anxious
- Obvious deformity of the left thigh

> [!question]
> His BP is normal. Is he shocked?

> [!notes]
> The narrow pulse pressure and shock index of 1.15 are the point. Hypotension is a late sign in a young patient, so I want someone to say "yes" before the next slide.

## Where's the blood? SCALPeR

- **S**calp / **S**treet
- **C**hest
- **A**bdomen
- **L**ong bones
- **P**elvis
- **R**etroperitoneum

> [!question]
> How would you look for each at the bedside in the first 10 minutes?

## Management

- Stop the bleeding: that's the definitive treatment
- `[GAP: blood products vs crystalloid, massive transfusion protocol, permissive hypotension, TXA. None of this is in Shock yet; add it there first, with a source, then pull it here]`
- Vasopressors aren't the answer to an empty tank

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

## Cold and wet

`[FIGURE: haemodynamic-profiles.svg, TikZ. 2×2 grid, warm/cold (perfusion) × dry/wet (congestion), with each shock type placed on it]`

> [!notes]
> I'd use this to compare him with Mrs P: she was warm and dry, he's cold and wet. That contrast is most of the bedside differentiation they need.

## Management

- 12-lead ECG and POCUS early
- Noradrenaline for MAP, then an inotrope (dobutamine or milrinone)
- Mottling suggests he needs inotropy more than vasoconstriction
- Fix the cause: `[GAP: revascularisation for ACS-related cardiogenic shock, with source]`
- Escalate early: ICU, cardiology, mechanical support is a specialist decision

> [!notes]
> From the table in [[Shock#Vasopressors and Ionotropes]] and [[Shock#Approach to Refractory Shock]]. I'd name IABP/Impella/ECMO only so they've heard of them.

---

# Case 4: The Twist

## Mrs D, 58

- Day 4 after a hip replacement, sudden breathlessness
- HR 128, BP 80/50, RR 32, SpO₂ 86% on 6 L
- Cool peripheries, JVP up, chest clear

> [!question]
> Cold, raised JVP. Is this cardiogenic?

## Obstructive shock mimics pump failure

- Cold and congested, but the heart isn't the problem
- POCUS: dilated RV, or pericardial effusion, or no lung sliding
- Causes: PE, tamponade, tension pneumothorax
- Fluids and pressors only buy time; the obstruction has to be relieved

`[GAP: specific treatments (thrombolysis for massive PE, pericardiocentesis, decompression of tension pneumothorax), with sources]`

> [!notes]
> The clear chest is what I'd want them to notice. This is the case where POCUS earns its place, so I'd show a RUSH clip if I can find one we're allowed to use. `[IMAGE: RUSH exam overview from Rush Exam note; check the source]`

---

# Quick-Fire

## Don't miss these

| Situation | Clue | First move |
| --- | --- | --- |
| Anaphylaxis | Exposure, urticaria, wheeze | Adrenaline 0.5 mg IM |
| Adrenal crisis | Steroid use, ↓Na ↑K | Hydrocortisone 100 mg IV + saline |
| Neurogenic | Spinal injury, warm + bradycardic | `[GAP: source]` |
| Bradycardic | Heart block on ECG | Atropine → isoprenaline, pacing |
| "Is it real?" | Patient looks well | Recheck the cuff or line |

> [!notes]
> Drug doses taken from the table in [[Shock#Vasopressors and Ionotropes]]. I'd run this as a quick-fire round, reading out the clue and having them call the diagnosis.

---

# Wrap-Up

## Your first 15 minutes

1. Call for help
2. ABC, monitoring, access, VBG with lactate
3. Three questions: peripheries, heart rate, filling
4. Treat the type: fluid challenge, pressor, inotrope, or fix the obstruction
5. Reassess, and escalate

> [!notes]
> Back to the opening question: compare this list with what they said at 0200.

## Take-home

- Shock is a failure of oxygen delivery; BP falls late
- $\text{MAP} - \text{CVP} = \text{CO} \times \text{SVR}$ tells you where to look
- Warm vs cold, fast vs slow, full vs empty
- More than one type can co-exist (e.g. sepsis + hypovolaemia)
- Full notes: [[Shock]]
