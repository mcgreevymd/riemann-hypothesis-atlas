# Reusable research prompt — the missing independent sign of the Weil pairing
You are given the Weil pairing W for ζ restricted to E0 = {F : ∫F e^{±u/2} = 0} on finite windows of the log line, with the exact
decomposition W(f)/‖f‖² = K(0) + ∫k_∞(a)(2 − 2ρ_f(a))da − 2Σ a_n ρ_f(log n). Known: (i) Tate's boundary data (f(0), ∫f) transform by
Fourier (swap) and unitary scaling (diag(|a|^{−1/2}, |a|^{1/2})), and the only invariant boundary form is hyperbolic (1,1), so the
boundary cannot supply a sign; (ii) over F_q the sign is the Hodge index theorem: D² = 2b₀b₁ + D_⊥² with D_⊥² ≤ 0; (iii) every
physics positivity mechanism (RS, BPS/instanton, Witten, no-ghost, SUSY) is a square of an independently positive structure plus an
indefinite boundary/charge term.
Task: propose and test a construction of a Hilbert space H₊ and a map Φ: E0 ∩ C_c^∞(window) → H₊, built only from Euler factors and
Γ data, scaling-equivariant and window-consistent, with ‖Φg‖² = W(g∗g^♯) exactly (counterterm handled as in Connes' cutoff), failing
for Davenport–Heilbronn. Keep separate: covariance (a state's two-point function), stiffness (a Hamiltonian's quadratic form), poles
(boundary pair), zeros (spectral data). Label each claim exact / cited / numerical / analogy / open. Galerkin positivity is never a
certificate. Do not claim RH; existence of Φ is equivalent to RH, so only an independent construction counts. First control: S = {∞}
against Connes–Consani 2021 Thm 1; then S = {∞, 2}, without repeating the naive semilocal-Sonin difference that already fails.
