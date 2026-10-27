---
date: 2026-10-28
---
# Determinants of Steady State Concentration
- For drugs administered orally, the unbound concentration depends mostly on intrinsic hepatic clearance and total concentration depends on intrinsic clearance and fraction unbound
- For drugs administered intravenously, it varies depending on the hepatic extraction ratio:
	- Drugs with low hepatic extraction ratio: unbound concentration depends on intrinsic clearance and total concentration depends on intrinsic clearance and fraction unbound
	- Drugs with high hepatic extraction ratio: unbound concentration depends on hepatic blood flow and fraction unbound and total concentration depends on hepatic blood flow
- For intravenous dosing:
$$
\text{Maintenance Dose Rate (DR)}=CL\times \text{Steady State Cocnentration }(C_{SS})
$$
- For low hepatic extraction ratio drugs $CL\approx f_{u}\cdot CL_{\text{int}}$ so intravenously:
$$
\begin{align}
C_{SS} & \approx\frac{\text{DR}}{f_{u}\cdot CL_{\text{int}}} \\
Cu_{SS} & \approx f_{u}\times C_{SS} \\
 & =\frac{\text{DR}}{CL_{\text{int}}}
\end{align}
$$
- For high hepatic extraction ratio drugs $CL\approx Q_{H}$ so intravenously:
$$
\begin{align}
C_{SS} & \approx \frac{\text{DR}}{Q_{H}} \\
Cu_{SS} & \approx \frac{f_{u}\cdot \text{DR}}{Q_{H}}
\end{align}
$$

- For oral dosing:
$$
\text{DR}\times F=CL\times C_{SS}
$$
- Therefore it follows that:
$$
\begin{align}
C_{SS} & =\frac{\text{DR}\times F}{CL} \\
 & =\frac{f_{g}\cdot f_{H}\cdot \text{DR}}{CL}
\end{align}
$$
- As we know $CL=\frac{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}$ and $f_{H}=1-E_{H}=\frac{Q_{H}}{Q_{H}+f_{u}\cdot CL_{\text{int}}}$, therefore:
$$
\begin{align}
C_{SS} & = (f_{g}\cdot f_{H}\cdot \text{DR})\times \frac{{Q_{H}+f_{u}\cdot CL_{\text{int}}}}{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}} \\
 & = (f_{g}\cdot \text{DR})\times \frac{Q_{H}}{Q_{H}+f_{u}\cdot CL_{\text{int}}} \times \frac{{Q_{H}+f_{u}\cdot CL_{\text{int}}}}{Q_{H}\cdot f_{u}\cdot CL_{\text{int}}} \\
 & =\frac{f_{g}\cdot \text{DR}}{f_{u}\cdot CL_{\text{int}}} \\
 \therefore \quad Cu_{SS} & =\frac{f_{g}\cdot \text{DR}}{CL_{\text{int}}}
\end{align}
$$