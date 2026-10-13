---
date: 2026-10-14
---
*Main source: Birkett, Pharmacokinetics Made Easy* [@birkettPharmacokineticsMadeEasy2005]
- Drug effect follows the concentration at the site of action (the effect site), not the plasma concentration
	- Whether the two match depends on how quickly the effect site equilibrates with plasma
- The effect site is modelled as an extra compartment of negligible volume linked to the central compartment (see [[Compartment Models#Two-Compartment Model]]), which equilibrates at a rate set by $k_{e0}$:
$$
\frac{dC_{e}}{dt}=k_{e0}\,(C_{p}-C_{e})
$$
	- When $k_{e0}$ is large, $C_{e}$ follows $C_{p}$ almost immediately, so effect follows plasma concentration
	- When $k_{e0}$ is small, $C_{e}$ lags behind $C_{p}$, rising while $C_{p}>C_{e}$ and peaking when $C_{e}=C_{p}$ (where $dC_{e}/dt=0$)
	- The equilibration half-time ($t_{1/2}k_{e0}=0.693/k_{e0}$) describes how quickly the effect catches up with a change in plasma concentration
![[effect-site-lag.svg|Plasma and effect-site concentrations after an IV bolus]]
> [!card]- What equation links plasma and effect-site concentration, and when does effect-site concentration peak?
> $\dfrac{dC_{e}}{dt}=k_{e0}(C_{p}-C_{e})$. After a bolus, $C_{e}$ rises while $C_{p}>C_{e}$ and peaks when $C_{e}=C_{p}$.
# Rapidly Equilibrating Effect Site
- e.g. diazepam used intravenously in status epilepticus:
	- The brain is highly perfused, so brain concentrations and the anticonvulsant effect follow plasma concentrations
	- Plasma concentrations fall rapidly during the distribution phase as diazepam redistributes to other tissues, so the effect falls with them and fitting can recur within 2–4 hours if more drug is not given, even though the elimination half-life is very long
	- The duration of action of a single dose is therefore set by redistribution rather than elimination
- If the site of a toxic effect is rapidly accessible, the peak concentration at the end of a bolus (before distribution, $\approx\text{Dose}/V_{1}$) can cause toxicity
	- The injection is given slowly so distribution happens while the drug is being given, e.g. intravenous theophylline and lignocaine
> [!cloze]
> After a single IV dose of diazepam, the anticonvulsant effect wears off due to ==redistribution==, not elimination, so fitting can recur within ==2–4 hours==
# Slowly Equilibrating Effect Site
- e.g. digoxin given intravenously:
	- Digoxin distributes slowly to its site of action (the inotropic effect) in cardiac muscle, so the effect increases while plasma concentrations are decreasing, both being driven by the same movement of drug from plasma into tissue
	- It takes about 6 hours to reach full effect even when given intravenously, so IV dosing gives no advantage in time to full effect, and loading is best done with divided oral doses at least 6 hours apart so the full effect of each dose can be assessed before more is given
	- In the first 6–8 hours after a dose, plasma concentrations bear no relationship to effect, so levels must be taken at least 6 hours after a dose, preferably as a trough just before the next dose
> [!card]- Why must digoxin levels be taken at least 6 hours after a dose?
> Digoxin equilibrates slowly with its site of action in cardiac muscle, so for the first 6–8 hours plasma concentrations are high while the effect is still rising and bear no relationship to effect. Ideally take a trough level just before the next dose.
