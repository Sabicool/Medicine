---
date: 2026-10-27
---
# Half Life and the Elimination Rate Constant
- $k$ is the fraction of drug in the body eliminated per unit time (see [[Elimination and Clearance#Elimination Rate Constant|Elimination Rate Constant]])
- Fall in plasma concentration after a single dose is given by:
$$
C_{t}=C_{0}\times e^{-kt}
$$
- Differentiating shows the rate of fall is proportional to the concentration at that time:
$$
\begin{align*}
\frac{{dC_{t}}}{dt} & = -k\times C_{0}\times e^{-kt} \\
&= -k \cdot C_{t}
\end{align*}
$$
- Solving the above for when $C_{t}=0.5\times C_{0}$ (i.e. when the plasma concentration falls by half) we get:
$$
\begin{align}
0.5 \times C_{0} & = C_{0}\times e^{-kt_{1/2}} \\
\frac{1}{2} & = e^{-kt_{{1/2}}} \\
-kt_{1 / 2} & = -\ln 2 \\
\therefore \quad k & = \frac{\ln 2}{t_{1 / 2}}
\end{align}
$$
# Determinants of Half Life
$$
\begin{align} 
t_{1 / 2}  & = \frac{\ln 2}{k} \\
 & = \frac{\ln 2 \times V_{D}}{CL}
\end{align}
$$
- Therefore the main determinants of half life ($t_{1 / 2}$) are volume of distribution and clearance
- Volume of distribution in and of itself depends on the initial dose (see [[Volume of Distribution]])
## Determinants from Half Life
- Half life effects:
	- Duration of action after a single dose
	- Time required to reach steady state with chronic drug dosing (generally requiring 3-5 half lives to reach the approximate plasma concentration)
	- Dosing frequency required to avoid too large fluctations in plasma concentrations during the dosing interval
