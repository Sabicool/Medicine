---
date: 2026-10-14
---
*Main source: Birkett, Pharmacokinetics Made Easy* [@birkettPharmacokineticsMadeEasy2005]
- Volume of distribution is the apparent volume the drug would have to be dissolved in to give the measured plasma concentration, and is defined as the amount of drug in the body divided by the plasma concentration:
$$
\text{Volume of Distribution }(V_{D})=\frac{\text{Amount of Drug in Body }(A_{\text{body}})}{\text{Plasma Drug Concentration }(C)}
$$
	- Immediately after an IV bolus, before any drug has been eliminated, the amount in the body is the dose, hence $V_{D}=\text{Dose}/C_{0}$
	- It is an apparent volume rather than a real one, so it can be far larger than total body water (e.g. digoxin, amiodarone)
- The volume of distribution depends on where the drug sits, which mostly comes down to binding:
	- If a drug is tightly bound to plasma proteins (e.g. warfarin), most of it stays in the plasma, so the plasma concentration is high and it will appear as though the medication is dissolved in a smaller volume
	- If a drug is bound to tissue (e.g. digoxin to muscle, amiodarone to fat), little of it is left in the plasma, so the plasma concentration is low and the volume appears very large
- For reference, in a 70 kg adult plasma is about 3 L, extracellular fluid about 14 L and total body water about 42 L, so:

| $V_{D}$ | Interpretation | Examples (approximate) |
| --- | --- | --- |
| $\approx$ Plasma volume | Mostly confined to plasma (highly protein bound or very large molecules) | Warfarin $\approx$ 0.1 L/kg, heparin |
| $\approx$ Extracellular fluid | Polar drugs that cross capillaries but not cell membranes | Gentamicin $\approx$ 0.25 L/kg |
| $\approx$ Total body water | Small lipid soluble drugs distributed evenly | Ethanol $\approx$ 0.6 L/kg |
| $\gg$ Total body water | Concentrated in tissue | Digoxin $\approx$ 7 L/kg, amiodarone $\approx$ 60 L/kg |

> [!card]- What is the definition of volume of distribution?
> The amount of drug in the body divided by the plasma drug concentration ($V_{D}=A_{\text{body}}/C$). It is an apparent volume, so it can exceed total body water.

> [!cloze]
> A drug highly bound to ==plasma proteins (e.g. warfarin)== has a small volume of distribution, whereas a drug highly bound to ==tissue (e.g. digoxin)== has a large volume of distribution
## Plasma and Tissue Binding
- The components of volume of distribution are the plasma volume and the tissue volume, weighted by the ratio of the fraction of the drug unbound in plasma to the fraction of the drug unbound in tissue:
$$
V_{D}=\text{Plasma Volume }(V_{P})+\frac{\text{Fraction unbound in plasma }(f_{u})}{\text{Fraction unbound in tissue }(f_{u_{T}})}\times \text{Tissue Volume }(V_{T})
$$
- This comes from splitting the amount in the body into what is in the plasma and what is in the tissue, then using the fact that only unbound drug crosses between them, so at equilibrium the unbound concentrations are equal:
$$
\begin{aligned}
f_{u}\cdot C & =f_{u_{T}}\cdot C_{T}\qquad\therefore\qquad C_{T}=\frac{f_{u}}{f_{u_{T}}}\cdot C \\
V_{D}=\frac{A_{\text{body}}}{C} & =\frac{C\cdot V_{P}+C_{T}\cdot V_{T}}{C}=V_{P}+\frac{f_{u}}{f_{u_{T}}}\cdot V_{T}
\end{aligned}
$$
![[plasma-tissue-binding.svg|Volume of distribution from plasma and tissue binding]]
- Hence:
	- More plasma protein binding (lower $f_{u}$) shrinks $V_{D}$ towards $V_{P}$
	- More tissue binding (lower $f_{u_{T}}$) makes $V_{D}$ larger, without limit
> [!card]- Derive volume of distribution in terms of plasma and tissue binding
> Only unbound drug equilibrates, so $f_{u}\cdot C=f_{u_{T}}\cdot C_{T}$. Then $V_{D}=\dfrac{C\cdot V_{P}+C_{T}\cdot V_{T}}{C}=V_{P}+\dfrac{f_{u}}{f_{u_{T}}}\cdot V_{T}$
## Factors Affecting Volume of Distribution
- Drug factors:
	- Lipid solubility: lipid soluble drugs cross membranes and distribute into fat, polar drugs stay largely extracellular
	- Ionisation (pKa relative to the local pH): only the unionised form crosses membranes
	- Plasma protein and tissue binding (see above)
	- Molecular size: very large molecules (e.g. heparin) stay in the plasma
- Patient factors:
	- Body composition: obesity increases $V_{D}$ for lipophilic drugs, and neonates have a larger proportion of body water
	- Fluid status: fluid resuscitation, oedema and capillary leak in critical illness increase $V_{D}$ for hydrophilic drugs (e.g. aminoglycosides, β-lactams)
	- Plasma proteins: hypoalbuminaemia increases $f_{u}$ and hence $V_{D}$ for drugs bound to albumin
	- Pregnancy increases plasma volume and body water
# Measuring Volume of Distribution
- Serial plasma concentrations are taken after an IV bolus and plotted as log concentration against time
	- The line of best fit is extrapolated to $t=0$ to find the plasma concentration at time zero ($C_{0}$)
	- This is used to calculate the volume of distribution ($V_{D}=\frac{\text{Dose}}{C_{0}}$)
- This assumes a one-compartment model, i.e. that the drug distributes instantly
	- Most drugs take time to distribute, so the samples are taken after distribution is complete and the extrapolated $C_{0}$ is lower than the true initial concentration, which overestimates $V_{D}$ (see [[Compartment Models#Volumes in a Two-Compartment Model]])
- Volume of distribution can also be calculated from clearance and the elimination rate constant ($k$), using the AUC (see [[Elimination and Clearance#Elimination Rate Constant]]):
$$
V_{D}=\frac{CL}{k}=\frac{\text{Dose}}{k\cdot\text{AUC}}
$$
# Clinical Significance
- **Loading dose:** the amount of drug needed to fill the volume of distribution to a target concentration straight away, rather than waiting about 4–5 half-lives for steady state:
$$
\text{Loading Dose}=V_{D}\times \text{Target Plasma Concentration}
$$
	- The loading dose depends only on $V_{D}$, whereas the maintenance dose depends only on clearance ($DR=CL\times C_{SS}$)
	- For an oral loading dose, divide by the bioavailability ($F$)
- **Half-life:** for a given clearance, a larger volume means a longer half-life, since less of the drug is in the plasma where the clearing organs can reach it:
$$
t_{1/2}=\frac{0.693\cdot V_{D}}{CL}
$$
- **Dialysis and haemofiltration** remove little of a drug with a large $V_{D}$, since only a small fraction of the total amount is in the plasma at any time
	- Plasma concentrations can also rebound after a session as drug redistributes back out of the tissues
- **Critical illness:** fluid shifts and hypoalbuminaemia increase $V_{D}$ for hydrophilic drugs, so a larger loading dose is often needed even though the maintenance dose depends on clearance
> [!card]- How is a loading dose calculated, and why does it not depend on clearance?
> $\text{Loading Dose}=V_{D}\times\text{Target Concentration}$ (divided by $F$ if oral). It only has to fill the volume of distribution to the target once; clearance determines the maintenance dose needed to replace what is eliminated.

> [!card]- Why are drugs with a large volume of distribution poorly removed by dialysis?
> Only a small fraction of the total amount in the body is in the plasma, which is all that dialysis can reach. Concentrations can also rebound afterwards as drug redistributes from the tissues.
