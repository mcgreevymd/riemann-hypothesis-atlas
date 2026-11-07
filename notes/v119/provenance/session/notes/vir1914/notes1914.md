# vir1914 — "Or perhaps Virasoro algebra" (t1914; RH not proved). Checks: checks1914.py (Verma engine, exact)
Exact: [L_m,L_n]=(m−n)L_{m+n}+c/12(m³−m)δ_{m+n,0}, L_n†=L_{−n}.
- ‖L_{−n}|h⟩‖² = 2nh + c(n³−n)/12 (n=1,2,3 checked).
- Level 2 Gram (basis L_{−2}, L_{−1}²): [[4h+c/2, 6h],[6h, 8h²+4h]], det = 2h(16h²+2(c−5)h+c) = 32h(h−h₁,₂)(h−h₂,₁) (Kac).
- h=−1 (open-string level 2, intercept a=1): det = 2(c−26); χ=(L_{−2}+3/2 L_{−1}²)|−1⟩ has L₁χ=0 (checked) and ‖χ‖² = (c−26)/2: null exactly at c=26.
Precision: c is the Virasoro central charge — not the speed of light, not an instanton charge. Modular invariance ≠ unitarity. Unitarity (Gram PSD at all levels) is a constraint (Kac/FQS: c≥1,h≥0 or minimal series); positivity of an actual rep comes from a construction (free fields, Sugawara/coset), i.e. an independent positive space. Prior: 2026-11-01 answer (memory) — useful part is Gram positivity; L186 Virasoro↔scaling, c=26 has no ζ analogue.
Arithmetic reading: the scaling generator plays L₀; E0's two moment constraints (ev0, ev1) play the L₁,L₂-type subsidiary conditions only in the sense of cutting the (1,1) boundary (compat1907); there is no known central extension of the C_Q-scaling algebra acting on windows. Sugawara-type positive reps exist but no map to W is built.
