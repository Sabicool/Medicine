---
date: 2026-10-28
---
*Main source: Birkett, Pharmacokinetics Made Easy* [@birkettPharmacokineticsMadeEasy2005]
- At steady state the dose rate going in equals the elimination rate coming out (see [[Elimination and Clearance#Clearance at Steady State]]), so for intravenous dosing:
$$
\text{Maintenance Dose Rate }(DR)=CL\times \text{Steady State Concentration }(C_{SS})
$$
- The unbound steady state concentration is $Cu_{SS}=f_{u}\cdot C_{SS}$, and it's the unbound concentration which drives the effect
- The rest of this note is for a drug cleared by the liver, where only unbound drug is metabolised, so clearance follows the well-stirred model (see [[Elimination and Clearance#Hepatic Extraction Ratio (Well-Stirred Model)]]):
$$
CL=\frac{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}
$$
# Determinants of Steady State Concentration
![[steady-state-determinants.svg|Determinants of total and unbound steady state concentration for a hepatically cleared drug]] ^fig-steady-state-determinants
- For drugs given orally, the unbound concentration depends only on intrinsic clearance (and the fraction absorbed), and the total concentration depends on intrinsic clearance and fraction unbound, whatever the hepatic extraction ratio
- For drugs given intravenously, it depends on the hepatic extraction ratio:
	- Low hepatic extraction ratio: the unbound concentration depends on intrinsic clearance, and the total concentration depends on intrinsic clearance and fraction unbound
	- High hepatic extraction ratio: the unbound concentration depends on hepatic blood flow and fraction unbound, and the total concentration depends on hepatic blood flow
- Hence hepatic blood flow only matters for a high extraction ratio drug given intravenously
## Intravenous Dosing
- For low hepatic extraction ratio drugs $CL\approx f_{u}\cdot CL_{\text{int}}$, so:
$$
\begin{aligned}
C_{SS} & \approx\frac{DR}{f_{u}\cdot CL_{\text{int}}} \\
Cu_{SS} & = f_{u}\times C_{SS} \approx\frac{DR}{CL_{\text{int}}}
\end{aligned}
$$
- For high hepatic extraction ratio drugs $CL\approx Q_{H}$, so:
$$
\begin{aligned}
C_{SS} & \approx \frac{DR}{Q_{H}} \\
Cu_{SS} & \approx \frac{f_{u}\cdot DR}{Q_{H}}
\end{aligned}
$$

> [!card]- What determines the total and unbound steady state concentration of a low hepatic extraction ratio drug given IV?
> $CL\approx f_{u}\cdot CL_{\text{int}}$, so $C_{SS}\approx\dfrac{DR}{f_{u}\cdot CL_{\text{int}}}$ (intrinsic clearance and fraction unbound) and $Cu_{SS}\approx\dfrac{DR}{CL_{\text{int}}}$ (intrinsic clearance only)
> %% anki: 1793136947939 %%

> [!card]- What determines the total and unbound steady state concentration of a high hepatic extraction ratio drug given IV?
> $CL\approx Q_{H}$, so $C_{SS}\approx\dfrac{DR}{Q_{H}}$ (hepatic blood flow only) and $Cu_{SS}\approx\dfrac{f_{u}\cdot DR}{Q_{H}}$ (hepatic blood flow and fraction unbound)
> %% anki: 1793136948041 %%
## Oral Dosing
- Only the bioavailable fraction of each dose reaches the systemic circulation (see [[Bioavailability]]), so:
$$
\begin{aligned}
F\times DR & =CL\times C_{SS} \\
\therefore\quad C_{SS} & =\frac{F\times DR}{CL}=\frac{f_{g}\cdot f_{H}\cdot DR}{CL}
\end{aligned}
$$
- Substituting the well-stirred model for both $CL$ and $f_{H}=1-E_{H}=\dfrac{Q_{H}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}$:
$$
\begin{aligned}
C_{SS} & = (f_{g}\cdot f_{H}\cdot DR)\times \frac{Q_{H}+f_{u}\cdot CL_{\text{int}}}{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}} \\
 & = (f_{g}\cdot DR)\times \frac{Q_{H}}{Q_{H}+f_{u}\cdot CL_{\text{int}}} \times \frac{Q_{H}+f_{u}\cdot CL_{\text{int}}}{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}} \\
 & =\frac{f_{g}\cdot DR}{f_{u}\cdot CL_{\text{int}}} \\
\therefore \quad Cu_{SS} & =\frac{f_{g}\cdot DR}{CL_{\text{int}}}
\end{aligned}
$$
- Hepatic blood flow drops out because it changes bioavailability and clearance by the same proportion, so a fall in blood flow lowers clearance but lets proportionally less drug through the liver on its first pass, and the two cancel
- This holds whatever the extraction ratio, as the approximations for low and high extraction drugs were never needed

> [!card]- Derive the unbound steady state concentration of a hepatically cleared drug given orally
> $F\cdot DR=CL\cdot C_{SS}$ with $F=f_{g}\cdot f_{H}$. Substituting $f_{H}=\dfrac{Q_{H}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}$ and $CL=\dfrac{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}$, the $Q_{H}+f_{u}\cdot CL_{\text{int}}$ and $Q_{H}$ terms cancel:
> $$
> C_{SS}=\frac{f_{g}\cdot DR}{f_{u}\cdot CL_{\text{int}}},\qquad Cu_{SS}=\frac{f_{g}\cdot DR}{CL_{\text{int}}}
> $$
> %% anki: 1793136948141 %%

> [!cloze]
> After oral dosing of a hepatically cleared drug, the unbound steady state concentration depends only on ==intrinsic clearance==, whatever the hepatic extraction ratio
> %% anki: 1793136948240 %%

> [!card]- Why doesn't hepatic blood flow affect the steady state concentration of a high extraction drug given orally?
> A fall in hepatic blood flow lowers clearance ($CL\approx Q_{H}$) but also lowers the fraction escaping first-pass ($f_{H}\approx\dfrac{Q_{H}}{f_{u}\cdot CL_{\text{int}}}$) by the same proportion, so $F/CL$, and hence $C_{SS}=F\cdot DR/CL$, is unchanged
> %% anki: 1793136948340 %%
# Clinical Consequences
- These follow from the figure above ([[#^fig-steady-state-determinants|Figure]]):
	- **Enzyme induction or inhibition** (changing $CL_{\text{int}}$) changes the unbound steady state concentration in every case except a high extraction ratio drug given intravenously
	- **Displacement from plasma proteins** (raising $f_{u}$) lowers the total concentration but leaves the unbound concentration unchanged for low extraction ratio drugs and for oral dosing, so it's mostly of no clinical consequence; the exception is a high extraction ratio drug given intravenously, where the unbound concentration rises
	- **A fall in hepatic blood flow** (e.g. low cardiac output) only raises the steady state concentration of a high extraction ratio drug given intravenously, e.g. a lignocaine infusion

> [!card]- When does displacement of a drug from plasma proteins raise its unbound steady state concentration?
> Only for a high hepatic extraction ratio drug given IV ($Cu_{SS}\approx f_{u}\cdot DR/Q_{H}$). For low extraction drugs and oral dosing, clearance rises with $f_{u}$, so the total concentration falls and the unbound concentration is unchanged
> %% anki: 1793136948440 %%

> [!card]- Which steady state concentrations change with a fall in hepatic blood flow?
> Only those of a high hepatic extraction ratio drug given IV, as $C_{SS}\approx DR/Q_{H}$ (e.g. lignocaine in low cardiac output states). Low extraction drugs and oral dosing are unaffected
> %% anki: 1793136948540 %%
