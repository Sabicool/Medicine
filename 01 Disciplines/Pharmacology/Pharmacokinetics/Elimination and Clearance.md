---
date: 2026-10-11
---
- Elimination refers to the irreversible excretion of unchanged drug or conversion to a metabolically inactive product
- Clearance refers to the efficiency of elimination and is broadly defined as a volume of plasma that is cleared of the drug per unit time (L/hr or mL/min)

| Quantity | Definition | Units |
| --- | --- | --- |
| Elimination rate | Amount of drug irreversibly removed per unit time | mg/hour |
| Clearance ($CL$) | Elimination rate divided by plasma concentration | L/hour |
| Extraction ratio ($E$) | Fraction of drug entering an organ that is removed in a single pass | none (0 to 1) |
| Elimination rate constant ($k$) | Elimination rate divided by the amount of drug in the body | hour⁻¹ |
| Volume of distribution ($V_{D}$) | Amount of drug in the body divided by plasma concentration | L |

# Definitions
## Elimination Rate
- If $A(t)$ is the amount of drug eliminated by time $t$, the elimination rate is how fast that amount grows:
$$
\text{Elimination Rate}=\frac{dA(t)}{dt}\quad\text{(mg/hour)}
$$
## Clearance
- Clearance is defined as the elimination rate divided by the plasma concentration:
$$
\underset{ \text{(L/hour)} }{ \text{Clearance }(CL) } = 
\underset{ \text{(mg/hour)} }{ \text{Elimination Rate} } 
\div
\underset{ \text{(mg/L)} }{ \text{Drug Concentration }(C) }
$$
- The reason clearance is defined as a ratio is that in first-order (linear) kinetics the elimination rate is proportional to concentration, so the ratio stays constant regardless of dose or concentration and describes the drug and the patient rather than the moment
	- Doubling the concentration doubles the elimination rate in mg/hour, but the same volume of plasma is still cleared each hour
	- When elimination saturates (zero-order kinetics, e.g. phenytoin, ethanol) the elimination rate stops rising with concentration, so clearance falls as concentration rises and is no longer a constant
- The "volume cleared per unit time" description is just the interpretation of the units (mg/hour ÷ mg/L = L/hour), i.e. the volume of plasma that would need to be completely emptied of drug each hour to account for the elimination rate

> [!card]- Describe what clearance is?
> The volume of plasma completely cleared of drug per unit time (L/hr or mL/min), i.e. elimination rate divided by plasma concentration. In first-order kinetics it is constant, as elimination rate is proportional to concentration.
> %% anki: 1791646840531 %%

> [!card]- What is the mathematical definition of clearance?
> $$
> \text{Clearance }(CL)=\frac{\text{Elimination Rate}}{\text{Drug Concentration }(C)}\qquad\text{(mg/hour ÷ mg/L = L/hour)}
> $$
> %% anki: 1791646840627 %%
## Extraction Ratio
- The extraction ratio refers to ratio of elimination of the drug through the organ of interest and is given by:
$$
\text{Extraction Ratio }(E_{H})=\frac{C_{\text{in}}-C_{\text{out}}}{C_{\text{in}}}=1-\frac{\text{Concentration Out}}{\text{Concentration In}}
$$
- Unlike clearance, the extraction ratio belongs to a single organ and has no units, it is the fraction of drug delivered to the organ that does not come back out in the venous blood
	- $E=0$ means the organ removes nothing, $E=1$ means the organ removes everything delivered to it
	- It is converted into a clearance by multiplying by organ blood flow (see [[#Organ Clearance]])

> [!card]- What is the mathematical definition of extraction ratio?
> The fraction of drug entering an organ that is removed in a single pass:
> $$
> E=\frac{C_{\text{in}}-C_{\text{out}}}{C_{\text{in}}}=1-\frac{C_{\text{out}}}{C_{\text{in}}}
> $$
> %% anki: 1791646840673 %%
## Elimination Rate Constant
- The elimination rate constant ($k$) is the fraction of the drug in the body removed per unit time, i.e. the elimination rate divided by the amount of drug in the body ($A_{\text{body}}$):
$$
k=\frac{\text{Elimination Rate}}{A_{\text{body}}}\quad\text{(hour}^{-1}\text{)}
$$
- Since $A_{\text{body}}=V_{D}\cdot C$ (the definition of volume of distribution), clearance and $k$ are linked directly:
$$
\begin{aligned}
\text{Elimination Rate} & = CL\cdot C=k\cdot A_{\text{body}}=k\cdot V_{D}\cdot C \\
\therefore\quad CL & =k\cdot V_{D}
\end{aligned}
$$
- This is also why half-life depends on both clearance and volume of distribution, as $t_{1/2}=\ln 2/k$:
$$
t_{1/2}=\frac{0.693\cdot V_{D}}{CL}
$$
- So a drug can have a long half-life either because it is cleared slowly or because most of it sits outside the plasma where the clearing organs can't get to it

> [!card]- Derive the relationship between clearance, elimination rate constant and volume of distribution
> Elimination rate $=CL\cdot C=k\cdot A_{\text{body}}$, and $A_{\text{body}}=V_{D}\cdot C$, so $CL=k\cdot V_{D}$ (and therefore $t_{1/2}=0.693\cdot V_{D}/CL$)
> %% anki: 1791646840729 %%
# Clearance at Steady State
- The amount of drug in the body changes by whatever goes in minus whatever is eliminated:
$$
\frac{dA_{\text{body}}}{dt}=\text{Dose Rate}-CL\cdot C
$$
- At steady state the amount in the body is no longer changing, so $dA_{\text{body}}/dt=0$ and the dose rate in equals the elimination rate out:
$$
\begin{aligned}
\text{Maintenance Dose Rate }(DR)&=\text{Elimination Rate}\\
&=\text{Clearance }(CL)\times \text{Steady State Drug Concentration }(C_{SS})\\
\therefore\quad C_{SS}&\propto \frac{1}{CL} \quad\text{(where }DR\text{ is constant)}
\end{aligned}
$$
# Measuring Clearance
- Every method below is the definition $CL=\text{Elimination Rate}/C$ applied to a situation where the elimination rate can be worked out
## Steady State Infusion
- Whole body clearance be determined using the steady state formula:
$$
CL=\frac{DR}{C_{SS}}
$$
> [!card]- How is clearance mathematically defined at steady state?
> $$
> \text{Clearance }(CL)=\frac{\text{Maintenance Dose Rate }(DR)}{\text{Steady State Drug Concentration }(C_{SS})}
> $$
> %% anki: 1791646840772 %%

## Renal Clearance
- Renal clearance can be derived from the definition of clearance based on elimination rate, where the elimination rate is the amount of drug appearing in urine per unit time:
$$
\begin{aligned}
\text{Clearance }(CL)&=\frac{\text{Elimination Rate}}{\text{Drug Concentration}}\\
&=\frac{\text{Urine Concentration }(U)\times \text{Urine Flow }(V)}{\text{Plasma Concentration}}
\end{aligned}
$$
## Single IV Bolus and AUC
![[auc-iv-bolus.svg|Clearance from a single IV bolus]]
- An IV bolus can be used to determine clearance where after given enough time, all of it is eliminated therefore:
$$
\begin{aligned}
\text{Dose} & = CL \cdot \text{AUC}  \\
CL & = \frac{\text{Dose}}{\text{AUC}}
\end{aligned}
$$
> [!card]- How is clearance calculated from a single IV dose?
> $CL = \dfrac{\text{Dose}}{\text{AUC}_{0\to\infty}}$, because total amount eliminated $= \int_0^\infty CL \cdot C(t)\,dt = CL \cdot \text{AUC}$, and after an IV dose that equals the dose.
> %% anki: 1791646840820 %%
### Mathematical Derivation
- Let $A(t)$ be the amount of drug eliminated by time $t$, its rate of change is the elimination rate:
$$
\frac{dA(t)}{dt}=CL\cdot C(t)
$$
- To get the total amount ever eliminated, integrate from 0 to infinity:
$$
\begin{aligned}
A_{\text{total}} &=\int_{0}^\infty CL\cdot C(t)\cdot dt  \\
 & =CL \cdot \int_{0}^\infty C(t)\cdot dt \\
  & =CL\cdot \text{AUC}
\end{aligned}
$$
- After an IV dose all of the drug is eventually eliminated, so $A_{\text{total}}=\text{Dose}$
	- This doesn't assume any compartment model, only that $CL$ is constant so it can come out of the integral, hence it is the "model-independent" way of measuring clearance
	- For an oral dose only the bioavailable fraction ever reaches the plasma, so $F\cdot\text{Dose}=CL\cdot\text{AUC}$
- For a one-compartment IV bolus, $C(t)=C_{0}e^{-kt}$ where $C_{0}=\text{Dose} / V_{D}$ and $k$ is the elimination rate constant, which gives the same $CL=k\cdot V_{D}$ result as [[#Elimination Rate Constant]]:
$$
\begin{aligned}
\text{AUC} &= \int_{0}^\infty C_{0}e^{-kt}\cdot dt=C_{0} \left[ -\frac{e^{-kt}}{k} \right]_{0}^{\infty}=\frac{C_{0}}{k} \\
\therefore\quad CL & =\frac{\text{Dose}}{C_{0} / k} = k \cdot \left( \frac{\text{Dose}}{C_{0}} \right) \\
 & = k \cdot V_{D}
\end{aligned}
$$
# Organ Clearance
- Whole body clearance is the sum of the clearances of each eliminating organ, since each organ's elimination rate adds to the total and they all divide by the same plasma concentration:
$$
CL_{\text{total}}=CL_{\text{hepatic}}+CL_{\text{renal}}+CL_{\text{other}}
$$
## Clearance = Blood Flow × Extraction Ratio
- For blood ($Q$) flowing through an organ, the organ's elimination rate is the drug delivered minus the drug leaving (Fick principle), and blood flow in equals blood flow out as blood isn't stored in the organ:
$$
\text{Elimination Rate}=Q\cdot C_{\text{in}}-Q\cdot C_{\text{out}}=Q\,(C_{\text{in}}-C_{\text{out}})
$$
- Dividing by the concentration delivered to the organ (the definition of clearance) gives:
$$
\begin{aligned}
CL_{\text{organ}} &= \frac{Q\,(C_{\text{in}}-C_{\text{out}})}{C_{\text{in}}} \\
 &= Q\cdot E
\end{aligned}
$$
![[organ-clearance-fick.svg|Organ clearance from the Fick principle]]
- Clearance of an organ is dependent on the blood flow to that organ
- So the maximum possible clearance of an organ is its blood flow ($E=1$), which for the liver is roughly 1.5 L/min (about 90 L/hour)
- Strictly $Q\cdot E$ is a blood clearance ($CL_{b}$), since it uses blood flow and blood concentrations. The elimination rate is the same whichever concentration it is divided by, so using the blood:plasma ratio ($\lambda$, see [[Pharmacology Basics]]):
$$
CL\cdot C=CL_{b}\cdot C_{b}=CL_{b}\cdot\lambda\cdot C\qquad\therefore\qquad CL=\lambda\cdot CL_{b}
$$
- Hence plasma clearance can appear to exceed hepatic blood flow for drugs that concentrate in red cells ($\lambda>1$)
> [!card]- Derive organ clearance in terms of blood flow and extraction ratio
> Elimination rate $=Q(C_{\text{in}}-C_{\text{out}})$ (Fick principle), so $CL=\dfrac{Q(C_{\text{in}}-C_{\text{out}})}{C_{\text{in}}}=Q\cdot E$
> %% anki: 1791646840951 %%
## Hepatic Extraction Ratio (Well-Stirred Model)
- The well-stirred model treats the liver as a single well-mixed compartment, so the concentration the hepatocytes see is the same as the concentration leaving in the hepatic vein ($C_{\text{out}}$)
- At steady state, drug entering the liver must leave by one of two routes:
	- Washed out in hepatic venous blood at a rate of $Q_{H}\cdot C_{\text{out}}$
	- Metabolised by hepatocytes, which only see unbound drug ($f_{u}\cdot C_{\text{out}}$) and clear it at their intrinsic clearance ($CL_{\text{int}}$, the clearance of the liver if blood flow were not limiting), at a rate of $f_{u}\cdot CL_{\text{int}}\cdot C_{\text{out}}$
$$
\begin{aligned}
Q_{H}\cdot C_{\text{in}} & =Q_{H}\cdot C_{\text{out}}+f_{u}\cdot CL_{\text{int}}\cdot C_{\text{out}} \\
\therefore\quad C_{\text{out}} & =\frac{Q_{H}\cdot C_{\text{in}}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}
\end{aligned}
$$
- Substituting into the definition of extraction ratio:
$$
\begin{aligned}
E_{H} &= 1 - \frac{C_{\text{out}}}{C_{\text{in}}} = 1 - \frac{Q_{H}}{Q_{H} + f_{u}\cdot CL_{\text{int}}} \\
&= \frac{f_{u}\cdot CL_{\text{int}}}{Q_{H} + f_{u}\cdot CL_{\text{int}}} \\
\therefore\quad CL_{H} &= Q_{H}\cdot E_{H}=\frac{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}
\end{aligned}
$$
![[well-stirred-liver.svg|Well-stirred model of the liver]]
- The denominator is not hepatic blood flow, it is the sum of the two exits from the liver
	- Each exit is a rate divided by $C_{\text{out}}$, so both have units of L/hour and can be added: $Q_{H}$ is the volume of liver blood emptied of drug per hour by being carried away, $f_{u}\cdot CL_{\text{int}}$ is the volume emptied per hour by metabolism
	- $E_{H}$ is therefore the share of drug that takes the metabolism exit rather than the washout exit
	- e.g. with $Q_{H}=90$ L/hour, $f_{u}\cdot CL_{\text{int}}=10$ L/hour and $C_{\text{out}}=1$ mg/L, 90 mg/hour leaves in hepatic venous blood and 10 mg/hour is metabolised, so 100 mg/hour must be entering ($C_{\text{in}}\approx1.11$ mg/L) and $E_{H}=10/100=0.1$
- Assumptions of the model:
	- The liver is well-stirred (other models such as the parallel-tube model give a different formula)
	- Only unbound drug is metabolised
	- Kinetics are linear, so $CL_{\text{int}}$ is constant (roughly $V_{\max}/K_{m}$ at concentrations well below $K_{m}$)
> [!card]- What is the hepatic extraction ratio in the well-stirred model, and what does its denominator represent?
> $$
> E_{H}=\frac{f_{u}\cdot CL_{\text{int}}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}
> $$
> The denominator is the two competing routes for drug to leave the liver: washout in hepatic venous blood ($Q_{H}$) and metabolism of unbound drug ($f_{u}\cdot CL_{\text{int}}$)
> %% anki: 1791646840995 %%
## Flow-Limited vs Capacity-Limited Clearance
- The two extremes of the well-stirred model are where it becomes clinically useful:

| | High extraction ($E>0.7$) | Low extraction ($E<0.3$) |
| --- | --- | --- |
| When | $f_{u}\cdot CL_{\text{int}}\gg Q_{H}$ | $f_{u}\cdot CL_{\text{int}}\ll Q_{H}$ |
| $CL_{H}$ simplifies to | $\approx Q_{H}$ (flow-limited) | $\approx f_{u}\cdot CL_{\text{int}}$ (capacity-limited) |
| Clearance changed by | Hepatic blood flow (shock, low cardiac output, β-blockers, ageing) | Enzyme induction or inhibition, protein binding |
| First-pass metabolism | Large, so low oral bioavailability ($F_{H}=1-E_{H}$) | Small, so high oral bioavailability |
| Examples | Propofol, lignocaine, morphine, fentanyl, GTN, propranolol, verapamil | Phenytoin, warfarin, diazepam, theophylline |

![[hepatic-clearance-flow-capacity.svg|Hepatic clearance against unbound intrinsic clearance]]
- e.g. lignocaine can accumulate in low cardiac output states as its clearance follows hepatic blood flow, whereas enzyme induction (e.g. rifampicin) speeds up the clearance of warfarin but makes little difference to high extraction drugs
> [!cloze]
> High extraction drugs have ==flow-limited== hepatic clearance, whereas low extraction drugs have ==capacity-limited== hepatic clearance
> %% anki: 1791646841050 %%
