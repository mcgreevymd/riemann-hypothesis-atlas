# ground1896 — Heisenberg 1925 "ground-state positivity law" audit + arithmetic analogue (scratch; RH is not proved)
J. W. McGreevy; work by Grok Bot. Read-only atlas/STATE/lemmas. checks1896.py.
Sources read: https://en.wikipedia.org/wiki/Umdeutung_paper ; https://wucj.lab.westlake.edu.cn/Others/Heisenberg_Quantum_Mechanics.pdf
 = scan of Aitchison–MacManus–Snyder, AJP 72, 1370 (2004) [doi 10.1119/1.1775243] + Fedak–Prentis, AJP 77, 128 (2009) [doi 10.1119/1.3009634]. Not Heisenberg's original.
Verified (AMS): force f(x)=ω0²x+λx² (cubic potential; also λx³ case); [a⁰(n,n−1)]² = (h/πmω0)(n+const) (Eq.51); constant fixed by
 "in the ground state there can be no transition to a lower state": [a⁰(0,−1)]²=0 (Eq.52); a¹(0,−1)=0 used again (Eq.79);
 energy to λ²: W(n,n) = (n+½)ħω0 − 5λ²ħ²/(12mω0⁴)(n²+n+11/30) (Eq.89) — Wikipedia's "up to λ², E_n=ħω0(n+½)" is inaccurate.
 Fedak–Prentis: Born–Jordan quantum condition Σ_k(p(nk)q(kn)−q(nk)p(kn)) = h/2πi; in Heisenberg-type sum, elements with negative index set to zero.
Paste errors: "x_{n,n−α}=0 for n<0" is not the stated condition; cutoff doesn't "force harmonic Hessian"; ½ħω is a c-number, no stabilizer;
 double well is bounded below by confinement (E0=−1.71 for −∂²+x⁴−4x², V''(0)=−8); "pole constraint automatically forces W positive" false.
Exact: |a(n,n−1)|² = n+c ≥ 0 (norms) forces ladder termination ⇒ c fixed: positivity source = Hilbert norm + reality X(n−α,n)=X(n,n−α)*.
 Ground-state transform: ∫|f′|²+(V−E0)|f|² = ∫u0²|(f/u0)′|² (num 3.33122 vs 3.33116). Graph Picone identity needs J≥0, h>0 (checked);
 E0 contains no f≥0. G0 (paired1888) = positive CCR rep on E0 with wrong pairing.
Analogue: Heisenberg constant c ↔ ghost displacement; |amplitude|² ≥ 0 ↔ each zero term ev_ρ·conj ev_{1−ρ̄} being a norm ⇔ ρ on line.
 Independent version needed: Hilbert space H + map A: E0→H (primes/Γ only), A T_a = U_a A, ‖Af‖² = W(f) (r219, r323: existence ⇔ positivity; must be constructed).
Prior art: r625, r219, r323, r407, r885, r999, L103 invariant state ⇔ RH (STATE §114).
