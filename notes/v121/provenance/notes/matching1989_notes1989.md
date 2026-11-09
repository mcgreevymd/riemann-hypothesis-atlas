# matching1989 — full-W matching: FF-calibrated diagonal, primitive projection, two-moment inertia, exactness tolerance
Nov 8 2026 ~6:30–7:15 AM CST. Scratch only; no repo edits, no publication. RH NOT proved. No new constructor of a sign theorem.
Labels: [EXACT] proved here (finite dim / stated hyp.); [THM] cited; [NUM] double precision, uncertified; [HEUR]; [ANALOGY].
Files: ff1989.py/json (FF genus 2, brute force), inertia1989.py/json, nyq1989.py/json, e0tol1989.py/json, mom1975.py (copy, unchanged).

## 1. Bilinear matching equations (polarized; the target is bilinear, not quadratic)
For F,G in D(I) (window width A), real:
 W(F,G) = P(F,G) + B_A(F,G),  P(F,G) = C+(F)C-(G) + C-(F)C+(G),
 B_A(F,G) = ∫_0^∞ k(a)<(1-T_a)F,(1-T_a)G>_sym da + Σ_{log n<A} a_n <(1-T_{log n})F,(1-T_{log n})G>_sym − M_A <F,G>,
 <X,Y>_sym = Re<X,Y> (T_a, T_{-a} both counted via Re). Kernel form: B_A(F,G)=<μ_geo, Re r_{F,G}>,
 μ_geo = K0 δ_0 + [arch FP distribution, density −k(|t|) off 0] − Σ a_n(δ_{log n}+δ_{−log n}).
Matching target (bilinear): −I(ΦF,ΦG) = W(F,G) for all F,G in E0 (or, stronger, all of D(I) after projection, §3).
E0 parameterization (Prop. D, CC2021 L3.3): F=DF~, D=∂²−1/4 ⇒ W(DF~,DG~) = <(∂²−1/4)² μ_geo, r_{F~,G~}> (D kills 2cosh(t/2)=pole kernel).
 Diagonal in this picture [EXACT, IBP]: −M_A||DF~||² = −M_A(||F~''||² + ½||F~'||² + (1/16)||F~||²): a local H²-type form, still SUBTRACTED.
Window consistency [EXACT]: for I ⊂ I' (widths A ≤ A'), B_{A'}|_{D(I)} = B_A (new springs have zero overlap: ||F−T F||² = 2||F||², cancelled by
 2a_n in M_{A'}); C± are window-free. Hence the inductive system (D(I), B, C±) is isometric; any Φ must be compatible: Φ_{I'}|_{D(I)} = Φ_I.

## 2. FF calibration: the diagonal is the k=0 Lefschetz term (adjunction), and its sign is irrelevant to positivity [THM + EXACT + NUM-verified]
Curve C/F_q, γ_n = q^{−n/2}Γ_{Frob^n} on C×C, h=C×pt, v=pt×C: γ_n·γ_m = q^{−|n−m|/2}N_{|n−m|} (n≠m), γ_n² = 2−2g (adjunction, Hartshorne V),
 γ_n·h = q^{n/2}, γ_n·v = q^{−n/2}. Uniform Toeplitz law, k=0 INCLUDED: G(k) = q^{k/2}+q^{−k/2} − S_k, S_k = Σ_i β_i^k, S_0 = 2g.
 So the diagonal Δ² = 2 − (#zeros) = Euler characteristic; it is NOT a separate renormalization.
FF spring ledger [EXACT]: B_FF = W−P = Σ_{k≥1} G(k)||c−T_k c||² − M_L||c||²,  M_L = (2−2g) + 2Σ_{1≤k<L} q^{−k/2}N_k.
 Dictionary (term by term, same algebra as NF ledger): a_n=Λ(n)/√n ↔ q^{−k/2}N_k (both von-Mangoldt-weighted fixed-point counts);
 2Σa_n ↔ 2Σ q^{−k/2}N_k; −K0 ↔ Δ² = 2−2g; P ↔ intersection form of U=span(h,v); E0 ↔ primitive. The archimedean springs have no FF analogue.
Verified on y²=x⁵+2x⁴+x+1 over F_3 (g=2): brute-force N_1..N_4 = 5,19,23,75; N_3,N_4 predicted from the L-polynomial (built from N_1,N_2) exactly;
 |β_i|=1 (to 1e−15); D² = P − W (err 1e−14); spring ledger (err 7e−15); n_+(J)=1, n_−(W)=0, rank W = 4 = 2g; Δ² = −2 < 0.
LESSON [EXACT]: here the diagonal subtraction has the "wrong" sign (Δ²=−2, M_L contains −2) and W ≥ 0 anyway; for g=0 Δ²=+2. The sign of the
 diagonal is a calibration of χ, never the sign source. The sign is the Hodge index (Castelnuovo; Hartshorne V Thm 1.9, Ex. 1.10).
 ⇒ No quotient/renormalization of the diagonal alone can supply positivity; it can only fix a constant.

## 3. Primitive projection gives the FULL W (all F, not only E0) [EXACT, both FF and formal NF]
Extended form J on V_I = D(I) ⊕ U: J(F,G) = −B_A(F,G) (= Connes semilocal trace pairing I_S, classes1966 L1–L4, zeros-free), J(h,F)=C+(F),
 J(v,F)=C−(F), J(h,h)=J(v,v)=0, J(h,v)=1. Projection πF = F − C−(F)h − C+(F)v ∈ U^⊥. Then
   −J(πF,πG) = B(F,G) + C+(F)C−(G) + C−(F)C+(G) = W(F,G)   for ALL F,G in D(I)   (bilinear).
 P is exactly the U-part; both moments enter, jointly. (map1965 had only "E0 = primitive"; this is the stronger full-space statement.)
Inertia (Haynsworth 1968, Schur complements; finite Galerkin) [EXACT]:
 (a) n_+(J) = 1 + n_−(W|D(I))      (Schur on U, σ=[[0,1],[1,0]] has In=(1,1,0))  ⇒ window RH ⟺ "Hodge index" n_+(J_I)=1.
 (b) n_−(W) = n_−(B) − 1 + n_+(Q+σ),  Q_ab = c_a^T B^{−1} c_b (a,b ∈ {+,−})    (Schur on −B; needs B invertible)
 (c) n_−(B|E0) = n_−(B) − 2 + n_+(Q)                                           (two-constraint bordered form)
 (d) centered window: eig(Q+σ) = {2q_e+1, 2q_o−1}, eig(Q) = {2q_e, 2q_o}: recovers PUBLICATION_AUDIT Lemma 2 (q_e ≤ −1/2, q_o ≤ 1/2) covariantly.
 RH-window (W≥0 on D(I) and B≥0 on E0) ⇒ n_+(Q+σ) = 1 − n_−(B), n_+(Q) = 2 − n_−(B), so n_+(Q) = n_+(Q+σ)+1; with n_−(B)=1: n_+(Q)=1, Q+σ ≤ 0.
NUM (sine J=24,40): A=0.6, 1.0: n_−(B)=1, n_+(Q)=1, n_+(Q+σ)=0, n_−(W)=0, n_+(J)=1; (a),(b),(c) all hold; (d) matches to 1e−15.
 q_e = −0.50404 (A=0.6), −0.5000004 (A=1.0): the even condition is nearly SATURATED at A=1; q_o = 0.016, 0.494.
 A=2: ill-conditioned (min eig ~1e−14 = machine floor); (b) fails numerically ⇒ A=2 remains UNRESOLVED (consistent with prior).

## 4. Exactness tolerance: the subtraction must be exact, not approximately renormalized [NUM + EXACT logic]
By Weyl/Courant: replacing M_A by M_A+δ makes B|E0 indefinite as soon as δ > λ_min(B|E0) (L²-normalized).
 λ_min(B|E0) [NUM, J=40]: A=0.6: 0.70; A=1.0: 0.014; A=1.5: 9.0e−10 (next 1.1e−7, 4.3e−5, 3.1e−3, 0.10).
 Full W (no E0): A=0.6: 0.0082; A=1.0: 1.06e−6; A=1.5: 1.3e−14 (machine floor).
 Hence a candidate diagonal constant must equal K0 (and the cocycle 2Σa_n) to relative accuracy ~1e−10 already at A=1.5, decreasing
 super-exponentially in A. Any "approximate" renormalization, scheme constant, or modular-anomaly constant is falsified unless it is EXACTLY K0.
 [HEUR] The geometric ladder of small eigenvalues (count ≈ 2, 3, 6 below 1e−2 at A=0.6, 1, 1.5) behaves like a Slepian/prolate concentration
 ladder for the zero-free band |x|<γ1=14.13 (count ~Aγ1/π = 2.7, 4.5, 6.7; Landau–Widom). Uses zeros only as a diagnostic.
 Consequence for the target: no coercive (uniform-gap) polarization; −I(ΦF,ΦF) must be super-exponentially small on prolate-type F.

## 5. Covariance counterterm vs invariant diagonal; modular-anomaly analogy (steering t1990) [EXACT + ANALOGY]
Springs alone are not window-covariant: H_{A'}(F) − H_A(F) = 2Σ_{A≤log n<A'} a_n||F||² =: c(A,A')||F||² for F in D(I), width ≤ A.
 c is an additive cocycle (c(A,A'') = c(A,A') + c(A',A'')); M_A' − M_A = c(A,A') makes it a coboundary. The covariant completion
 B = H − M||·||² is UNIQUE up to adding κ||F||² with κ window-independent [EXACT]. That one free constant is −K0 (the FF Δ²).
 Analogy [ANALOGY, cited]: E2(−1/τ) = τ²E2(τ) + 6τ/(πi); E2* = E2 − 3/(π y) is weight-2 covariant, unique up to M_2(SL2(Z)) = 0
 (Zagier, 1-2-3 of Modular Forms, §2.3). Same pattern: an anomaly cocycle trivialized by a non-holomorphic/non-local counterterm.
 What the analogy does NOT give: (i) a sign (E2* is not positive; Petersson positivity is a separate theorem); (ii) the invariant constant
 (modular covariance fixes E2*'s correction completely because M_2=0, whereas window covariance leaves exactly κ free). Anomaly correction ≠ sign ≠ matching.
Invariant constant, exact [EXACT, NUM-checked 1e−9]: with unit-cutoff Hadamard finite part,
 FP∫_0^∞ 2k(a)da = −ψ(1/4) − γ − log 2 = 2.957090687...,  hence  −K0 = (γ + log 2π) + FP∫_0^∞2k  (confirms map1965/classes1966 L3 in closed form).
 Under cutoff rescaling ε→ε/λ: FP_λ = FP_1 − log λ and the δ_0 coefficient γ + log 2π + log λ: only the PAIR is canonical ("difference must
 remain paired"). Unlike FF, there is no scheme-free number Δ²_reg: the NF δ_0 coefficient is an RG-family, fixed only by Connes' α-normalization.
 Renormalized-Eisenstein check [NEGATIVE, limited]: Kronecker-limit/Chowla–Selberg constants at z=i involve log Γ(1/4) (|η(i)| = Γ(1/4)/(2π^{3/4}));
 K0 = −γ − π/2 − 3log2 − logπ involves π/2. No identity found; it would need an unknown linear relation among log Γ(1/4), π, γ, log 2, log π.
 (Broad Eisenstein work left to eisenstein1990.)

## 6. Constructive candidate (honest) — "Lefschetz–Castelnuovo window space" (KΠ1)
 Inputs (zeros-free, no positivity): primes ≤ e^A (shells of Q_p^*), archimedean transverse weight 2k(|t|), Connes α-normalization (δ_0 coeff),
  two moments C±. Target: V = colim_I D(I) ⊕ U (U hyperbolic plane), form J as §3 (Connes trace pairing on D(I), border by C±).
 Map: Φ = inclusion; primitive part πF. Prime contribution: transverse p-adic fixed points (a_n δ_{±log n}). Gamma: transverse R^* weight + FP.
 Subtraction: δ_0 term = non-transverse (excess) intersection ↔ FF adjunction Δ²; prime cocycle 2Σa_n = covariance coboundary.
 Matching: −J(πF,πG) = W(F,G) on ALL D(I), exact, bilinear, window-compatible.
 Sign theorem required: n_+(J_I) = 1 for every window (V is a Pontryagin Π_1 space with positive line in U) ⟺ W ≥ 0 on all windows ⟺ RH.
 Status: matching EXACT (trace formula + explicit formula); independence OK (zeros-free); SIGN = OPEN and RH-equivalent; no cycles/Num/ample class.
 Not new as an object (Connes 1999 trace pairing; map1965/classes1966 extended form); new here: full-space projection identity, inertia formulas
 (a)–(d), invariant-vs-cocycle split, tolerance data. This is a reorganization, NOT a constructor of the sign.

## 7. Precise next missing theorem
 (Hodge index for the window Lefschetz space) For each window I, the form J_I on D(I) ⊕ U, defined by Connes' semilocal trace pairing
 (S ⊇ {∞} ∪ {p < e^A}, α-normalized) bordered by C±, has exactly one positive direction — proved from an INDEPENDENT positivity source
 (an effective cone / Riemann–Roch growth as in map1965's acceptance criterion, or a positive compression B ⊂ range S_Λ as in classes1966 A1)
 whose deficit reproduces K0 exactly (tolerance §4) and the prime cocycle exactly (§5). Equivalent quantitative form: Q+σ ≤ 0 with n_−(B)=1
 (q_e ≤ −1/2, q_o ≤ 1/2), the even inequality being nearly saturated (A=1: q_e+1/2 ≈ −4e−7).

## Sources (opened/used)
 Local: arithmetic_unification_VI/sections/02,03,08; matching1983/PUBLICATION_AUDIT.md, notes1983.md; map1965/notes1965.md; classes1966/notes1966.md;
  geometry1897/notes1897.md; tate1905/notes1905.md; atlas1987/SYNTHESIS.md; hodge1979/1981, polarity1980.
 Lit: Connes, Selecta Math. 5 (1999) 29–106 (math/9811068), Thm VII.4; Connes–Consani, Selecta Math. 27 (2021) 77, arXiv:2006.13771 (Thm 1, Sonin);
  Hartshorne, Algebraic Geometry, V Thm 1.9, Ex. 1.10; E. Haynsworth, Linear Algebra Appl. 1 (1968) 73–81; Zagier, "Elliptic modular forms and their
  applications" in The 1-2-3 of Modular Forms (Springer 2008) §2.3; Landau–Widom, J. Math. Anal. Appl. 77 (1980) 469–481 (heuristic only); DLMF §5.4 (ψ(1/4)).
