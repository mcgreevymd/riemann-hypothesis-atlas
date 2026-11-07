# CLAIM_AUDIT — 6 Nov 2026 session (status per claim; corrections marked). RH is not proved.
Status keys: EXACT (proved here / checked), CITED (theorem in a source, location given), NUM (finite numerics), ANALOGY, OPEN, PRIOR (literature/atlas), CORRECTED (earlier wording withdrawn).

| # | Claim | Status | Where / note |
|---|---|---|---|
| 1 | L=∂²−¼ bijects C_c^∞ onto E0∩C_c^∞, support-hull preserving; W|E0≥0 ⇔ W∘L-type form ≥0 | EXACT; PRIOR | paired1888; Connes–Consani 2021 Lemma 3.3, Prop. 3.5 (verified 6 Nov) |
| 2 | E0 = kernel of two characters ⇒ convolution ideal, ♯-stable; tangent of polar-normalized units | EXACT | deform1894 |
| 3 | Cutoff-free spring decomposition of W/‖f‖² on windows | EXACT; PRIOR (r341, r423) | spring1891, interactions1890 |
| 4 | Positive Galerkin minima on windows | NUM — upper bounds, NOT certificates | spring1891; reproduction tonight |
| 5 | Hess Φ_N(0)=W for an explicit anharmonic functional | EXACT (restatement, gives no sign) | interactions1890 |
| 6 | Boundary laws b(Ff)=σb, b(U_af)=D_a b, FU_a=U_{a⁻¹}F, smearing = diag(ev₀,ev₁) | EXACT | compat1907; Connes 1999 eqs (6),(10),(11) |
| 7 | Invariant Hermitian boundary forms are z·hyperbolic, sig (1,1) | EXACT | compat1907 check (6) |
| 8 | S₀, E0 dense in L²; window kernel closed codim 2 | EXACT | compat1907 (7),(8). CORRECTED: E0 is not "closed codim 2" globally; smooth E0 is not L²-closed |
| 9 | "P" = global orthogonal pole projection | CORRECTED → moment map b / window projection P_L |
| 10 | Fourier conjugation vs adjoint | EXACT: FΘ_FF⁻¹=Θ_{F(−·)} (linear); Θ_F*=Θ_{F^♯} (antilinear) |
| 11 | Commutative positive functional cannot be independent ("Bochner trap") | CORRECTED (pairs1904 C1): it CAN be independent (positive tempered measure); non-commutativity only needed for nonzero RS commutator |
| 12 | W as a normalized state on bounded translations | CORRECTED: W unbounded; use a weight / positive functional on the test-function *-algebra with domains |
| 13 | Vacuum spectral density of global adelic vector ∝ |ĥ|²|Λ(½+it)|² | OMITTED (not source-verified in context) | tate1905 F3a withdrawn from synthesis |
| 14 | "Theta functional changes sign at zeros" | CORRECTED: not true in that generality; omitted |
| 15 | Delay positivity of full phase Λ(½−iτ)/Λ(½+iτ) ⇔ RH | CORRECTED: that ratio ≡ 1 by FE; no delay inference. Local γ-phase delay = K stays (EXACT, quartet1906; PRIOR atlas archimedean_weyl_kernel) |
| 16 | FE ⇔ modularity | CORRECTED: theta inversion ⇒ FE one way; converse theorems separate (pairs1904 C3) |
| 17 | RS with local σ_∂ excludes a normalization | EXACT as normalization exclusion only; no sign info (pairs1904 C4) |
| 18 | Heisenberg 1925 ground-state condition | CITED (Aitchison–MacManus–Snyder 2004 Eqs 51,52,89); positivity source = Hilbert norms. CORRECTED: Wikipedia's "E_n=ħω₀(n+½) to λ²" inaccurate |
| 19 | Witten positive energy: spinor alone gives sign | CORRECTED: sign from DEC + existence of Witten spinor + asymptotics; spinor gives the square |
| 20 | Semilocal Sonin inequality = THE arithmetic DEC | CORRECTED → one candidate; OPEN (atlas needed_semilocal_sonin_inequality); naive 2-place version fails (R26, λ_min=−log2/√2) |
| 21 | Bogomolny |F|²∓F∧F/vol=2|F^∓|²; S≥8π²|k|/g² (conventional normalization) | EXACT (pointwise checked); topological term Hess = 0; metric from ⋆ |
| 22 | Primitive real (1,1) ⇒ ASD ⇒ α∧α=−|α|²vol | EXACT (checked on C²) |
| 23 | Integral c₁ ⇒ ample | FALSE (Bl_pt P² example; Nakai–Moishezon) |
| 24 | "Only Hodge produces a sign" | FALSE: positive representations, metrics, positive states also do |
| 25 | F_q split D²=2b₀b₁+D_⊥², ⊥-Gram negative semidefinite ⇔ a²≤4q | EXACT (Test 1); Hasse/Weil via Hodge index (Mattuck–Tate, Grothendieck 1958) |
| 26 | F_q Frobenius samples = continuous Mellin moments | CORRECTED: same diagonal law, discrete samples vs continuous moments |
| 27 | Pole pair = II₁,₁ lattice | ANALOGY only (no lattice); atlas v1.15 wording "as the II₁,₁ part" is analogy |
| 28 | Virasoro level-2 null at c=26 above h=−1 | EXACT algebra; NOT a positive-representation proof; critical-dimension statements only as cited GT theorem |
| 29 | SUSY H≥|Z| | EXACT (2×2 block); central charge not identified with root number ε |
| 30 | Root number / topological charge as sign source | NO: orientation/sector labels, |ε|=1 also for DH |
| 31 | Connes 1999 Thm 5: Q′_{Λ,0}≤S_Λ ⇒ Δ_Λ positive type; global ⇔ RH | CITED (char p; eqs (21)-(25)); Tr(S_ΛV(f))=2f(1)log′Λ; Thm 4 S-local normalization 2h(1)log′Λ re-checked 6 Nov |
| 32 | CC21 Thm 1: W_∞(g∗g*) ≥ Tr(ϑ(g)Sϑ(g)*), supp g⊂[2^{−1/2},2^{1/2}], ĝ(i/2)=ĝ(0)=0; Thm 6.11 with constant 13<c<17 | CITED (verified 6 Nov); CC21 §3 also gives f=g∗g* satisfying (54) but without the support condition (ĝ(t)=(1+4t²)e^{−t²/4}) with W_∞(f)≈−28.90<0: the support condition is needed |
| 33 | CCM 2023 strategy: compare positive trace functional with Weil functional; semilocal Sonin stability (Thm 2) | CITED |
| 34 | Geometry forces torsion absent | NOT CLAIMED |
| 35 | Discriminant>0 ⇒ positivity | FALSE (det>0 with negative definite, Test 1); use inertia |
| 36 | Clifford relation is a positivity source | FALSE: exists for indefinite g (Cl(1,1) check) |
| 37 | Existence of an exact factorization W=‖Φ·‖² on E0 | ⇔ RH (restatement); construction OPEN |
| 38 | New ample class / J matching W for ζ | NONE found |
