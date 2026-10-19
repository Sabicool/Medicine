---
date: 2026-10-19
---
- Compartment models describe the body as one or more well-mixed spaces the drug moves between, so that plasma concentrations over time can be described mathematically
	- The compartments are mathematical rather than anatomical, although they loosely correspond to groups of tissues with similar blood flow
# One-Compartment Model
- The drug distributes instantly and evenly through a single volume ($V_{D}$), so after an IV bolus the only process is elimination:
$$
\frac{dA}{dt}=-CL\cdot C=-k\cdot A\qquad\therefore\qquad C(t)=C_{0}\,e^{-kt},\quad k=\frac{CL}{V_{D}}
$$
- A plot of log concentration against time is a straight line with slope $-k$, and extrapolating it back to $t=0$ gives $C_{0}=\text{Dose}/V_{D}$
# Two-Compartment Model
- The drug is given into a small central compartment ($V_{1}$: plasma and well-perfused organs such as the brain, heart, liver and kidney) and distributes to a peripheral compartment ($V_{2}$: poorly perfused tissue such as muscle and fat)
	- Elimination is assumed to happen from the central compartment
![[two-compartment-model.svg|Two-compartment model with an effect site]]
- Writing the amount of drug in each compartment as $X_{1}$ and $X_{2}$:
$$
\begin{aligned}
\frac{dX_{1}}{dt} & =-(k_{10}+k_{12})\,X_{1}+k_{21}\,X_{2} \\
\frac{dX_{2}}{dt} & =k_{12}\,X_{1}-k_{21}\,X_{2}
\end{aligned}
$$
- The solution after an IV bolus is the sum of two exponentials (biexponential):
$$
C(t)=A\,e^{-\alpha t}+B\,e^{-\beta t},\qquad \alpha+\beta=k_{10}+k_{12}+k_{21},\quad \alpha\beta=k_{10}\,k_{21}
$$
	- **Distribution phase ($\alpha$, fast):** plasma concentration falls steeply as drug moves out to the peripheral compartment, even though little has been eliminated yet
	- **Elimination phase ($\beta$, slow):** once the compartments have equilibrated, plasma concentration falls at a rate set by clearance; the elimination (terminal) half-life is $0.693/\beta$
> [!card]- What equation describes plasma concentration after an IV bolus in a two-compartment model, and what does each phase represent?
> $C(t)=A\,e^{-\alpha t}+B\,e^{-\beta t}$. The fast $\alpha$ phase is distribution from the central to the peripheral compartment; the slow $\beta$ phase is elimination after the compartments have equilibrated (terminal half-life $=0.693/\beta$).
## Volumes in a Two-Compartment Model
- With two compartments, "the" volume of distribution depends on when it is measured, since the ratio of amount in the body to plasma concentration changes as the drug distributes:

| Volume | Formula | Meaning |
| --- | --- | --- |
| Central ($V_{1}$) | $\dfrac{\text{Dose}}{A+B}$ | Volume at the moment of injection, before any distribution |
| Steady state ($V_{SS}$) | $V_{1}+V_{2}$ | Amount in the body divided by plasma concentration at steady state |
| Area ($V_{\text{area}}$ or $V_{\beta}$) | $\dfrac{CL}{\beta}=\dfrac{\text{Dose}}{\beta\cdot\text{AUC}}$ | Relates amount to concentration during the elimination phase |
| Extrapolated ($V_{\text{extrap}}$) | $\dfrac{\text{Dose}}{B}$ | What back-extrapolating the terminal phase gives |

- In order of size: $V_{1}<V_{SS}\le V_{\text{area}}<V_{\text{extrap}}$
- Back-extrapolating the terminal phase to $t=0$ gives its intercept ($B$) rather than the true initial concentration ($A+B$), which overestimates the volume:
![[biexponential-extrapolation.svg|Back-extrapolating the elimination phase]]
- How much it overestimates depends on how fast distribution is compared with elimination. Integrating the biexponential for the AUC:
$$
\begin{aligned}
\text{AUC} & =\int_{0}^{\infty}\left(A\,e^{-\alpha t}+B\,e^{-\beta t}\right)dt=\frac{A}{\alpha}+\frac{B}{\beta} \\
\therefore\quad V_{\text{area}} & =\frac{\text{Dose}}{\beta\cdot\text{AUC}}=\frac{\text{Dose}}{B+A\,\dfrac{\beta}{\alpha}}
\end{aligned}
$$
	- When distribution is much faster than elimination ($\alpha\gg\beta$), the $A\beta/\alpha$ term is negligible and $V_{\text{extrap}}\approx V_{\text{area}}$, which is why the one-compartment back-extrapolation is usually good enough
	- When distribution is slow or large (e.g. digoxin), the extrapolated volume overestimates
- The central volume determines the peak concentration straight after a bolus ($\text{Dose}/V_{1}$), whereas $V_{SS}$ is the one to use for a loading dose
> [!card]- Why does back-extrapolating the terminal phase overestimate the volume of distribution in a two-compartment model?
> It gives the intercept of the elimination phase ($B$) rather than the true initial concentration ($A+B$), so $V_{\text{extrap}}=\text{Dose}/B$ is larger than $V_{\text{area}}=\text{Dose}/(B+A\beta/\alpha)$. The error is small when $\alpha\gg\beta$.
