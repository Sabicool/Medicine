---
date: 2026-10-10
---
- Elimination refers to the irreversible excretion of unchanged drug or conversion to a metabolically inactive product
- Clearance refers to the efficiency of elimination and is broadly defined as a volume of blood that is cleared of the drug per unit time (L/hr or mL/min)
	- Clearance of an organ is therefore dependent on the blood flow to that organ
	- Clearance can also be defined by the elimination rate:
$$
\underset{ \text{(mg/hour)} }{ \text{Elimination Rate} }=\underset{ \text{(mL/hour)} }{ \text{Clearance }(CL) }\times \underset{ \text{(mg/mL)} }{ \text{Drug Concentration }(C) }
$$


> [!card]- Describe what clearance is?
> Clearance is the efficiency of elimination and is broadly defined as the volume of blood that is cleared of the drug per unit time and therefore has units like L/hr or mL/min

> [!card]- How are elimination rate and clearance related mathematically?
> $$
> \underset{ \text{(mg/hour)} }{ \text{Elimination Rate} }=\underset{ \text{(mL/hour)} }{ \text{Clearance }(CL) }\times \underset{ \text{(mg/mL)} }{ \text{Drug Concentration }(C) }
> $$
- The extraction ratio refers to ratio of elimination of the drug through the organ of interest and is given by:
$$
\text{Extraction Ratio }(E_{H})=1-\frac{\text{Concentration Out}}{\text{Concentration In}}
$$
- The extraction ratio can be related to the clearance of an organ by the following derivation:
$$
\begin{align}
\text{Elimination Rate} & = Q\cdot C_{\text{in}}-Q\cdot C_{\text{out}}=Q (C_{in}-C_{out}) \\
CL = \frac{\text{Elimination Rate}}{C_{\text{in}}} & =\frac{Q(C_{\text{in}}-C_{\text{out}})}{C_{\text{in}}} \\
 & =Q\left( 1-\frac{C_{\text{out}}}{C_{\text{in}}} \right) \\
  & =Q\cdot E
\end{align}
$$

> [!card]- What is the mathematical definition of extraction ratio?
> $$
> \text{Extraction Ratio }(E_{H})=1-\frac{\text{Concentration Out}}{\text{Concentration In}} 
> $$

> [!card]- How is clearance and extraction ratio for an organ related?
> $$
> CL = Q\cdot E
> $$
# Clearance at Steady State
- At steady state infusions:
$$
\begin{align*}
\text{Maintenance Dose Rate }(DR)&=\text{Elimination Rate}\\
&=\text{Clearance }(CL)\times \text{Steady State Drug Concentration }(C_{SS})\\
\therefore\quad C_{SS}&\propto \frac{1}{CL} \quad\text{(where }DR\text{ is constant)}
\end{align*}
$$
# Measuring Clearance
- Whole body clearance be determined using the steady state formula:
$$
CL=\frac{DR}{C_{SS}}
$$

> [!card]- How is clearance mathematically defined at steady state?
> $$
> \text{Clearance }(CL)=\frac{\text{Maintenance Dose Rate }(DR)}{\text{Steady State Drug Concentration }(C_{SS})}
> $$

- Renal clearance can be derived from the definition of clearance based on elimination rate:
$$
\begin{align*}
\text{Clearance }(CL)&=\frac{\text{Elimination Rate}}{\text{Drug Concentration}}\\
&=\frac{\text{Urine Concentration }(U)\times \text{Urine Flow }(V)}{\text{Plasma Concentration}}
\end{align*}
$$
- An IV bolus can be used to determine clearance where after given enough time, all of it is eliminated therefore (see [[#Mathematical Derivation]]):
$$
\begin{align}
\text{Dose} & = CL \cdot \text{AUC}  \\
CL & = \frac{\text{Dose}}{\text{AUC}}
\end{align}
$$

> [!card]- How is clearance calculated from a single IV dose?
> $CL = \dfrac{\text{Dose}}{\text{AUC}_{0\to\infty}}$, because total amount eliminated $= \int_0^\infty CL \cdot C(t)\,dt = CL \cdot \text{AUC}$, and after an IV dose that equals the dose.
# Mathematical Derivation
- Let $A(t)$ be the amount of drug eliminated by time $t$, its rate of change is the elimination rate:
$$
\frac{dA(t)}{dt}=CL\cdot C(t)
$$
- To get the total amount ever eliminated, integrate from 0 to infinity:
$$
\begin{align}
A_{\text{total}} &=\int_{0}^\infty CL\cdot C(t)\cdot dt  \\
 & =CL \cdot \int_{0}^\infty C(t)\cdot dt \\
  & =CL\cdot \text{AUC}
\end{align}
$$
- For a one-compartment IV bolus, $C(t)=C_{0}e^{-kt}$ where $C_{0}=\text{Dose} / V_{D}$ and $k$ is the elimination rate constant
$$
\begin{align}
\text{AUC} &= \int_{0}^\infty C_{0}e^{-kt}\cdot dt=C_{0} \left[ -\frac{e^{-kt}}{k} \right]_{0}^{\infty}=\frac{C_{0}}{k} \\
\therefore\quad CL & =\frac{\text{Dose}}{C_{0} / k} = k \cdot \left( \frac{\text{Dose}}{C_{0}} \right) \\
 & = k \cdot V_{D}
\end{align}
$$