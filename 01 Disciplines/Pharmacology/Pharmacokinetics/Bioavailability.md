---
date: 2026-10-28
---
*Main source: Birkett, Pharmacokinetics Made Easy* [@birkettPharmacokineticsMadeEasy2005]
# Definitions
- Absorption is the fraction of the dose absorbed intact from the gut into the portal circulation ($f_{g}$)
- First-pass clearance is the extent to which the liver removes the drug on its first passage through the liver in the portal blood, before it reaches the systemic circulation; the fraction escaping it is $f_{H}=1-E_{H}$
- Bioavailability ($F$) is the fraction of the dose which reaches the systemic circulation as intact drug:
$$
\text{Bioavailability }(F)=\text{Fraction Absorbed }(f_{g})\times \text{Fraction Escaping First-Pass Clearance }(f_{H})
$$
![[first-pass-bioavailability.svg|Oral bioavailability and first-pass metabolism. Gut and liver adapted from Servier Medical Art, CC BY 4.0]]

- Two formulations of a drug are bioequivalent if the extent and rate of absorption from them are similar enough that there is no clinically important difference in their effects (either therapeutic or adverse)

> [!card]- What is bioavailability and what determines it?
> The fraction of the dose which reaches the systemic circulation as intact drug. It is the fraction absorbed from the gut multiplied by the fraction escaping first-pass clearance by the liver:
> $$
> F=f_{g}\cdot f_{H},\qquad f_{H}=1-E_{H}
> $$

> [!card]- When are two formulations of a drug bioequivalent?
> When the extent and rate of absorption from them are similar enough that there is no clinically important difference in their therapeutic or adverse effects

# Measuring Bioavailability
- Bioavailability is measured by giving the same dose IV and orally and comparing the area under the plasma concentration versus time curves ($\text{AUC}$); clearance is the same both times, so it cancels:
$$
\begin{aligned}
\text{AUC}_{\text{oral}} & = \frac{F\times \text{Dose}}{CL} \\
\text{AUC}_{\text{IV}}  & = \frac{\text{Dose}}{CL} \\
\therefore\quad F & = \frac{\text{AUC}_{\text{oral}}}{\text{AUC}_{\text{IV}}}
\end{aligned}
$$
![[bioavailability-auc.svg|Measuring bioavailability from the AUC after the same dose given IV and orally]]
- Similarly, the relative bioavailability of two formulations given by the same route is:
$$
\text{Relative Bioavailability}=\frac{\text{AUC}_{\text{test}}}{\text{AUC}_{\text{reference}}}
$$

> [!card]- How is the absolute bioavailability of a drug measured?
> Give the same dose IV and orally and compare the areas under the curve. Since $\text{AUC}=F\cdot\text{Dose}/CL$ and clearance is the same both times:
> $$
> F=\frac{\text{AUC}_{\text{oral}}}{\text{AUC}_{\text{IV}}}
> $$
# Determinants of Drug Absorption
- **Dissolution:** properties of the drug including particle size and form, excipients, special dosage forms (e.g. sustained release), and stomach and small intestine pH
- **Gastric emptying rate:** affects how long the drug sits in acid (which matters for drugs unstable at acid pH) and how soon it reaches the small intestine; liquids and small particles empty more quickly than solid dosage forms, and emptying is slowed or sped up by antacids, drugs (opioids and anticholinergics slow it, metoclopramide speeds it up) and disease (e.g. autonomic neuropathy)
- **Intestinal motility:** affects how long slowly soluble drugs (e.g. digoxin, sustained release formulations) have to dissolve, and how long the drug is exposed to chemical degradation or metabolism by gut flora
- **Drug interactions in the gut lumen:** complexation (e.g. tetracyclines with divalent metal ions), adsorption (e.g. anion exchange resins), and interactions with food (e.g. some antibiotics)
- **Passage through the gut wall:** physicochemical characteristics of the drug (e.g. quaternary ammonium compounds are permanently charged so cross poorly), and metabolism by enzymes in the intestinal epithelium

> [!card]- What determines how well a drug is absorbed from the gut?
> Dissolution, gastric emptying rate, intestinal motility, interactions in the gut lumen (complexation, adsorption, food) and passage through the gut wall (physicochemical properties of the drug and metabolism by the intestinal epithelium)
# Determinants of First-Pass Clearance
- In low hepatic extraction ratio drugs (e.g. theophylline), nearly all of the dose gets through the liver on its first pass ($f_{H}\approx 1$), so $F\approx f_{g}$
	- Doubling or halving the small fraction the liver extracts makes little difference to $F$, e.g. $E_{H}$ rising from 0.1 to 0.2 only lowers $f_{H}$ from 0.9 to 0.8
- In high hepatic extraction ratio drugs (e.g. verapamil), only a minor proportion of the dose reaches the systemic circulation intact
	- Inducing or inhibiting the metabolising enzymes has only a small effect on the hepatic extraction ratio, and so on systemic clearance ($CL\approx Q_{H}$), but **has a major effect on the proportion escaping extraction ($f_{H}$), and so a major effect on bioavailability**, e.g. $E_{H}$ falling from 0.95 to 0.90 doubles $f_{H}$ from 0.05 to 0.10
	- Hepatic blood flow does change bioavailability in these drugs, as $f_{H}=\dfrac{Q_{H}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}\approx\dfrac{Q_{H}}{f_{u}\cdot CL_{\text{int}}}$, but it changes systemic clearance ($\approx Q_{H}$) by the same proportion, so the two cancel and the steady state concentration after oral dosing is unaffected (see [[Steady State#^fig-steady-state-determinants|Figure]])
- In chronic liver disease, a substantial portion of the portal circulation doesn't perfuse functional liver because of intrahepatic functional shunts or extrahepatic anatomical shunts, which increases bioavailability markedly; hence high hepatic extraction ratio drugs given to patients with liver disease are particularly liable to cause adverse effects

> [!cloze]
> In a low hepatic extraction ratio drug, bioavailability is set mostly by ==absorption from the gut ($f_{g}$)==, since nearly all of the absorbed dose escapes first-pass clearance

> [!card]- Why does enzyme induction or inhibition change the bioavailability of a high extraction drug much more than its clearance?
> Clearance is close to hepatic blood flow, so it barely moves. The fraction escaping first-pass ($f_{H}=1-E_{H}$) is small, so a small change in $E_{H}$ is a large proportional change in $f_{H}$, e.g. $E_{H}$ falling from 0.95 to 0.90 doubles $f_{H}$ (0.05 to 0.10) and so doubles $F$

> [!card]- Why does chronic liver disease increase the bioavailability of high extraction drugs?
> Intrahepatic functional shunts and extrahepatic anatomical (portosystemic) shunts let portal blood bypass functioning liver, so more of the dose escapes first-pass extraction. These drugs are therefore more likely to cause adverse effects in liver disease
