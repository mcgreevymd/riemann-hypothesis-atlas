# t2072: the u → 0 non-transverse regularization of the t2068 pairing, matched term by term against W
Nov 9 2026 (CST). Scratch only. Nothing pushed (no Atlas, repo, Page or manuscript edits). RH is NOT proved. Φ is NOT
constructed as a map into a sign-controlled (1,1) sector. W is NOT shown to be positive.
Labels: [EXACT] = closed-form identity checked here; [THM] = cited theorem; [NUM] = mpmath numerics (residual stated);
[CONV] = depends on a normalization choice; [NOT PRODUCED] = absent from the fixed-point trace.

## 0. What W is (from the project, not from the outside checklist)
- counterterm1995/notes1995.md l.7: `W = P + B_A, B_A = H_A - M_A||F||^2, M_A = -K0 + 2 sum_{log n<A} Lambda(n)/sqrt n,
  K0 = psi(1/4) - log pi = -5.37218341922567.`
- multiprime2047/notes2047.md §A (working form used by the certificates, also inertia2057 §1 "Q = W − P = H_A − M_A I"):
  `Q_A(F) = K0||F||^2 + J_inf(F) - 2 sum_{log n<A} a_n Re<F,T_{log n}F>,  a_n = Lambda(n)/sqrt n,
   J_inf = int_0^inf k(a)||EF - T_a EF||^2 da;  on E0, W = Q_A; in jump form W = H_A - M_A||F||^2.`
- atlas2060 README/FRONT notation: `I_A = [−A/2, A/2], C± = ∫F e^{±u/2}, E0 = ker C+ ∩ ker C−, P = 2 Re C+ conj C−,
  K0 = −γ − π/2 − 3 log 2 − log π, k∞(a) = e^{−a/2}/(1−e^{−2a})`.
So, with E = zero extension to R and T_bF(u) = F(u−b):
  H_A(F,G) = ∫_0^∞ k∞(a)⟨(I−T_a)EF,(I−T_a)EG⟩da + Σ_{log n<A} a_n⟨(I−T_{log n})EF,(I−T_{log n})EG⟩   (jump energy, H_A(F,F) ≥ 0)
  M_A      = −K0 + 2Σ_{log n<A} a_n                                                              (mass; K0 lives HERE)
  P(F,G)   = C+(F)conj C−(G) + C−(F)conj C+(G).
Only one normalization of W is used by the certificates (inertia2057, multiprime2047, logpoincare2044); this is it.
Sign of W [NUM, convention check only, zeros not used in any construction]: W(g) = +Σ_ρ ĝ(γ_ρ) (Weil zero side), residual 7e-26
(check2072_zeros_signconv.py, Gaussian s = 0.1, 119 zeros). So W ≥ 0 on E0 ⇔ RH (Weil criterion).

## 1. The pairing and its conventions (t2068, unchanged)
θ_u ξ(x) = e^{−u/2} ξ(λ_u^{−1}x), λ_u = (e^u,1,1,…). For g := F ∗ G̃, G̃(x) = conj G(−x):  g(b) = ⟨F, T_bG⟩, g(0) = ⟨F,G⟩,
⟨Φ(F),Φ(G)⟩ = Tr θ(g) = ∫ g(a) τ(a) da.
θ(g) = Connes' U(h) with h(x) = |x|^{−1/2} g(log|x|) (Ẑ^×-invariant; this is the symmetric σ = ½ map), so h(1) = g(0).
Haar on K_v^* is Connes' normalization ∫_{1≤|u|≤Λ} d*u ~ log Λ: on R^* this is d*u = du/(2|u|) — exactly the "average over the
two signs" factor ½ in t2068 — and on Q_p^* it gives vol(Z_p^*) = log p, i.e. the log p in Λ(n). [CONV, but forced to be the same
normalization in all three sectors; dropping the ½ would double the archimedean kernel to 2k∞ and break the match.]

## 2. The regularization actually implicit in t2068 (Connes 1999, Selecta 5, Thm 3 local / Thm 4 semilocal) [THM]
  Tr(R_Λ U(h)) = 2 h(1) log'Λ + Σ_v ∫'_v h(u^{−1})/|1−u| d*u + o(1),   R_Λ = P̂_Λ P_Λ.
∫'_v is the unique extension of the transverse density whose α-Fourier transform vanishes at 1 (α = standard character, e^{−2πix} at ∞).
This is the direct evaluation of [Γ_a]·Δ with a cutoff on X: the u = 1 (Γ_0 = Δ) fixed point is non-transverse; it contributes
the volume divergence 2h(1)log Λ and, through ∫', a finite δ_0 coefficient. No ε appears.
Split of τ_Λ:
 (a) a ≠ 0 archimedean (locus x_∞ = 0): density k∞(|a|) (two-sided, in a); singular as 1/(2|a|).
 (b) primes (locus x_p = 0, a = ±m log p): atoms a_n δ_{±log n}; p-adic unit diagonal ∫'_{Z_p^*} = 0 (unramified α_p).
 (c) a = 0 remainder: +2⟨F,G⟩ log Λ  plus  (γ + log 2π) δ_0  [from ∫'_R].

## 3. The u → 0 algebra
3.1 Expansion [EXACT, sympy]: k∞(a) = 1/(2a) + 1/4 − a/48 − a²/32 + O(a³);  K := 2k∞ = 1/a + 1/2 − a/24 + ….
3.2 ∫' at ∞ in the log variable [EXACT + NUM]:
   ∫'_R = Pf_1 ∫_R k∞(|a|) g(a) da + (γ + log 2π) g(0),
   where Pf_1 = lim_ε [∫_{|a|≥ε} − g(0) log(1/ε)] (Hadamard at scale 1).
   Derivation: in x = 1 − u the extension is T = Pf_1(1/|x|) + 2(γ+log 2π)δ, because FT[Pf_1 1/|x|](y) = −2γ − 2log 2π − 2log|y|
   (checked on three Gaussians, residual ≤ 2e-31). The ½ in d*u halves it. Jacobian of a ↔ x is 1 at 0, so the δ coefficient
   carries over. Checked x-form = a-form to 1e-14 (check2072_trace.py A), including a non-even g.
3.3 Divergences. Λ-scheme: exactly one divergent term, +2⟨F,G⟩ log Λ (coefficient 2h(1) = 2g(0)). It is not cancelled by anything
   inside the trace; it is removed by subtraction (Connes' renormalization). If one instead excises |a| < ε, the archimedean pairing
   diverges as +g(0) log(1/ε) TWO-SIDED (½ log(1/ε) per side). Both divergences are positive multiples of ⟨F,G⟩; there is no
   cancellation between log Λ and log(1/ε), and in the Λ-scheme the ε-divergence never appears (∫' is already finite).
   Quadratic-form reading: both are pure multiples of the identity on L²(I_A) — a divergent shift M_A → M_A + 2 log Λ if retained.
3.4 Finite part, distribution in a:
   τ_fin = (γ + log 2π) δ_0 + Pf_1 k∞(|a|) + Σ_{n≥2} a_n (δ_{log n} + δ_{−log n}).
   Degree (Laplacian) rewriting, using FP_H ∫_0^∞ K = π/2 + 2 log 2 [EXACT; NUM 4e-31] and ‖T_b EF‖ = ‖EF‖:
   Pf_1 ∫ k∞(|a|) g = ∫_0^∞ K(a)((g(a)+g(−a))/2 − g(0)) da + (π/2 + 2log 2) g(0),
   Σ a_n(g(log n)+g(−log n)) = 2Σ a_n g(0) − Σ a_n⟨(I−T_{log n})F,(I−T_{log n})G⟩.
   Hence
   ⟨Φ(F),Φ(G)⟩_ren := lim_Λ [Tr θ_Λ(F∗G̃) − 2⟨F,G⟩log Λ]
                     = [(γ+log 2π) + (π/2+2log 2) + 2Σ_{log n<A} a_n]⟨F,G⟩ − H_A(F,G)
                     = M_A⟨F,G⟩ − H_A(F,G) = −(W − P)(F,G)   [EXACT]
   since −K0 = γ + log 8π + π/2 = (γ+log 2π) + (π/2 + 2log 2) [EXACT].
   Window: for supp F, G ⊂ I_A, supp g ⊂ [−A, A], so atoms with log n ≥ A vanish automatically; that is the only way A enters.
3.5 Exact window check [NUM, 40 digits]: polynomial bumps F ≠ G, non-even, A = 11/10 (both log 2 and log 3 active), g exact
   piecewise polynomial (sympy), jump identity verified symbolically:
   trace_fin = 0.17213184139248358404, W − P = −0.17213184139248358404, sum = 1.3e-40;
   trace_fin − (−W) = 0.17207485353… = P(F,G) exactly. (check2072_window_exact.py/.json)
   Second, independent nested-quadrature version (C^∞ bumps, jump form computed directly from shifted F, G): residual 1.4e-16.
   (A numerical artefact 1e-4 seen in a first run was catastrophic cancellation in 1 − e^{−2a} near a = 0; fixed with expm1.)

## 4. Sector-by-sector sign table
| sector | renormalized trace | W − P (project) | relation |
|---|---|---|---|
| archimedean transverse | + Pf_1 ∫k∞(|a|)g  (+ jump: −∫_0^∞k∞⟨(I−T_a)F,(I−T_a)G⟩) | +∫_0^∞k∞⟨(I−T_a)F,(I−T_a)G⟩ | −1 |
| primes | + Σ a_n(g(log n)+g(−log n)) | − Σ a_n(g(log n)+g(−log n)) | −1 |
| diagonal (degree form) | + M_A⟨F,G⟩ | − M_A⟨F,G⟩ | −1 |
| pole P | absent | (W itself contains +P) | NOT PRODUCED |
All three sectors flip together: one global sign. The trace never sees P: P = ĝ(i/2) + ĝ(−i/2) is the pole (ĥ(0)+ĥ(1)) contribution,
spectral, not a fixed point.

## 5. Convention dependence (ii) vs output (i) vs not produced (iii)
(i) Follows from the written pairing: the divergence is +2⟨F,G⟩log Λ only; finite part = −(W−P) with the exact project M_A and H_A;
    prime truncation at log n < A from supports; one overall sign.
(ii) Convention: the literal δ_0 coefficient. Connes ∫' / Hadamard at scale 1: γ + log 2π. Laplacian/degree form (scale-free,
    used by W): M_A = −K0 + 2Σa_n. Hadamard at scale ε0 shifts FP and δ coefficient oppositely (only the pair moves).
    Character α → α(c·) at ∞ shifts γ + log 2π by log|c|; the product formula makes Σ_v invariant for c ∈ Q^×, so the standard
    character class fixes K0 (counterterm1995 §2). Λ → λΛ moves only the divergent term. The Haar normalization of §1.
(iii) Not produced: P (hence the trace equals −W only on E0); any positivity/sign; any (1,1)/primitive structure; any window
    information beyond supp F ⊂ I_A. M_A's "window dependence" is not a separate datum — it is the degree rewriting of atoms
    that the support already truncates.

## 6. The four verdicts
1. Divergence cancellation: MISMATCH with the checklist claim. One divergence (+2⟨F,G⟩log Λ), removed by subtraction, not
   cancelled. The ε-pole (if one uses ε) is g(0)log(1/ε) two-sided, same sign; it does not cancel log Λ.
2. Finite diagonal: H_A MATCH exactly (as −H_A); M_A MATCH exactly (= (γ+log 2π) + (π/2+2log 2) + 2Σ_{log n<A}a_n = −K0 + 2Σ a_n),
   in degree form. Literal δ_0 coefficient of the trace is γ + log 2π, not M_A (PARTIAL if one insists on the literal coefficient).
   The checklist's description is wrong: H_A is the nonnegative jump energy, not a digamma constant; the digamma constant
   K0 = ψ(1/4) − log π sits in M_A.
3. Relative signs: MATCH (all three sectors carry the same −1).
4. Overall sign: renormalized pairing = P − W. On E0: = −W (MATCH). Off E0: −W + P (PARTIAL, P not produced).
   So B_W(F,G) = −⟨Φ(F),Φ(G)⟩_ren holds on E0 (and = W − P = B_A everywhere).

## 7. Status reminders
- This is the semilocal theorem (Connes Thm 4, S = {∞} ∪ {p < e^A}, which covers every atom in supp g). The global cutoff
  trace formula on all of X is Connes' RH-equivalent statement; Meyer 2005 has an unconditional non-Hilbert version. The finite
  distribution Σ_v ∫'_v itself is unconditional.
- Full match does not give a sign: W ≥ 0 on E0 ⇔ ⟨Φ(F),Φ(F)⟩_ren ≤ 0 on E0 ⇔ Weil's criterion ⇔ RH. Open ~1.8 (the (1,1)
  intersection home + Hodge-type sign) is untouched.
- Prior work: counterterm1995 §1, §8 (Nov 8) already stated Tr_ren = M_A‖F‖² − H_A = −(W−P) for F = G from Connes' trace.
  t2072 re-derives it in the t2068 [Γ_u] half-density convention, polarizes to F ≠ G, adds the a-variable form of ∫'
  (Pf_1 k∞ + (γ+log 2π)δ), corrects the checklist, and checks the window identity to 1e-40.
- Do not conflate with the CC-2021 semilocal Sonin trace / time-delay object (Lemma 6, README "semilocal trace … equals W − P"):
  different operator, opposite sign convention. The Connes-1999 cutoff trace of U(h) gives −(W − P).
- C± / H⊥ not inspected beyond the fact that P (and only P) vanishes on E0.

## Files
check2072_sym.py/.json (series, K0, FP_H, FT of Pf 1/|x|, Gamma expansion); check2072_trace.py/.json (∫' three forms; window
ledger, nested quadrature); check2072_window_exact.py/.json (exact polynomial window ledger); check2072_zeros_signconv.py/.json
(sign convention of W only).
