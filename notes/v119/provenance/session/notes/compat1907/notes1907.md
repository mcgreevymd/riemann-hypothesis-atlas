# compat1907 — additive Fourier × multiplicative evolution × two Poisson boundary functionals (t1907; RH not proved)
Checks: checks1907.py (R model = archimedean place; ψ(x)=e^{−2πixy}; self-dual dx). All items below marked EXACT are proved here (elementary) and checked.

## 1. Boundary map and its transformation law [EXACT]
b(f) := (f(0), ∫f dx) ∈ C², f ∈ S(A_Q) (or S(R)).
- Fourier: b(Ff) = σ b(f), σ=[[0,1],[1,0]]  (f̂(0)=∫f, ∫f̂=f(0) by inversion).      check (1)
- R_a f(x)=f(a⁻¹x): b(R_a f)=diag(1,|a|) b(f)  (Connes 1999 eq (11): C ⊕ C(1)).    check (2)
- U_a=|a|^{-1/2}R_a (unitary): b(U_a f)=D_a b(f), D_a=diag(|a|^{-1/2},|a|^{1/2});  F U_a = U_{a⁻¹} F.   check (3)
  Consistency: σ D_a = D_{a⁻¹} σ.
## 2. Smearing = polar moments [EXACT]
Θ_F := ∫F(t) U_{e^t} dt (F on log line). b(Θ_F f) = diag(ev_0(F), ev_1(F)) b(f), ev_s(F)=∫F e^{(s−½)t}dt.   check (4)
Hence Θ_F(S(R)) ⊂ S(R)_0 for all f  ⇔  F ∈ E0 = {ev_0=ev_1=0}. (Converse: take f with b(f)=(1,0),(0,1).)
- Fourier conjugation: F Θ_F F⁻¹ = Θ_{F(−·)}  (LINEAR reflection, no conjugation); ev_s(F(−·)) = ev_{1−s}(F).   check (5)
- Adjoint: Θ_F* = Θ_{F^♯}, F^♯(t)=conj F(−t) (ANTILINEAR); ev_s(F^♯)=conj ev_{1−s̄}(F). Coincide only for real F.
- E0 is a convolution ideal: ev_s(F*G)=ev_s(F)ev_s(G). L=∂²−¼: ev_s(LF)=s(s−1)ev_s(F), so L: C_c^∞ → E0∩C_c^∞ (bijection, CC21 Lemma 3).
## 3. Topology: algebraic codim 2, Hilbert-dense [EXACT, explicit construction]
R model: f ↦ f(0) and f ↦ ∫f are unbounded on L²(R), so S(R)_0 is dense. Construction: η,κ ∈ C_c^∞, η(0)=1, κ supported away from 0, ∫κ=1;
n_δ(x)=η(x/δ), w_R(x)=R⁻¹κ(x/R). For φ with c0=φ(0), c1=∫φ:  ψ = φ − c0 n_δ − (c1 − c0 δ∫η) w_R  ⇒ ψ(0)=0, ∫ψ=0,
‖ψ−φ‖₂ ≤ |c0|δ^{1/2}‖η‖₂ + |c1−c0δ∫η| R^{−1/2}‖κ‖₂ → 0.  check (7) (Gaussian-type η,κ numerically): 0.516, 0.145, 0.046, 0.0145 for δ=1/R=10^{−1..−4}.
Log line: ev_0, ev_1 pair with e^{∓u/2} ∉ L²(R) ⇒ E0 dense in L²(R): correctors c₊k(u−R)+c₋k(u+R), c± = O(e^{−R/2}).  check (8): ‖corr‖₂ 2.2e−1, 3.0e−2, 4.0e−3, 5.4e−4 (R=4,8,12,16).
Fixed window [−L,L]: e^{±u/2} ∈ L²(window) ⇒ E0_L closed, codim 2, orthogonal projection P_L EXISTS; dist(Φ,E0_L)=0.820, 0.346, 0.050 (L=2,4,8) → 0 as L→∞.
Consequence: "P" removing poles = moment map b (or window projection P_L, L-dependent, not translation-covariant); NO global orthogonal projection onto a closed pole-free subspace of L²(R).
## 4. Boundary form [EXACT lemma]
Hermitian H on C² invariant under all D_a (a>0) and σ  ⇔  H = z[[0,1],[1,0]], z ∈ R (check (6)): signature (1,1) or 0. The Weil pole term is of this hyperbolic type.
⇒ boundary data + Fourier + scaling cannot source a positive form; any sign must come from the bulk.
## 5. Where an independent sign has come from (sources) and why identities are not enough
- Identities (Fourier, scaling covariance, b-law) are FE-level; DH has an FE of the same archimedean type (atlas: Lemma 153, odd char mod 5) and an indefinite Weil Gram (Lemma 149), so FE + Γ + boundary-type identities alone cannot force the sign. The rational-lattice adelic Poisson Σ_Q f = Σ_Q f̂ is ζ-specific; I make no claim about whether counterfeit FE series admit any adelic Poisson realization.
- Unitary regular rep V on L²(C_k) is positive: Tr(S_Λ V(f*f*)) = 2(f*f*)(1) log'Λ = 2‖f‖² log'Λ ≥ 0 (Connes 1999 Thm 5 proof), but divergent; Weil = limit of Tr((S_Λ − Q'_{Λ,0})V(f*f*)) — a SUBTRACTION. Positivity there comes from ORDER of projections Q'_{Λ,0} ≤ S_Λ (E(B_{Λ,0}) ⊂ S_Λ), proved in char p by RR/dimension count; global number-field formula ⇔ RH (Connes Thm 5 / §VIII).
- CC21 archimedean: W_∞(g*g*) ≥ Tr(ϑ(g)Sϑ(g)*) ≥ 0 (Sonin projection compression; small support, ĝ(i/2)=ĝ(0)=0). CCM 2023 (arXiv 2310.18423): strategy "compare the trace functional of the operator — automatically positive — with the Weil functional"; semilocal Sonin stability (Thm 2), inequality not proved.
## 6. Residual target (explicit)
For number fields Q'_{Λ,0} ≤ S_Λ fails at ∞ (no f with f, f̂ compactly supported; prolate B_Λ is approximate). Define leakage
  ε_Λ(g) := Tr((1−S_Λ) Q'_{Λ,0} (1−S_Λ) V(g*g*))-type remainder,  so  Tr((S_Λ−Q'_{Λ,0})V(g*g*)) = [positive order term] + ε_Λ(g).
Target: ε_Λ(g) ≥ −o(1) uniformly on E0 windows (one candidate route; semilocal Sonin inequality is another; neither proved).
## 7. Next test (proposed, not launched)
S={∞,2}: E_S(f)(u)=u^{1/2}Σ_{k≥0} f(2^k u) (CCM (46)); B_Λ = span of prolates with eigenvalue ≈1 (⊗1_{Z_2}); compute trace-norm leakage ‖(1−S_Λ)E_S Q_{B_Λ}‖₁ vs Λ and sign of Δ_{Λ,S} on E0 windows ≤ log 4. Control: S={∞} (E=w_∞, leakage only from prolate tails). Known: naive W − Son with 2 fails (R26, λ_min=−log2/√2); this test measures a different object (projection order), so it is not a repeat; falsified if leakage stays O(1) negative.
