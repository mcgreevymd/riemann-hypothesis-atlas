# atlas1987 — SYNTHESIS: proposed ranked front section for RH Atlas v1.20 (post-v1.19)
Prepared Nov 7 2026 ~10:30 PM CST (America/Chicago) for cloud repo integration. Composition of existing scratch work only:
no new hypotheses, no proof claims. **The Riemann Hypothesis is not proved.** Status labels follow AUDIT.md:
[THEOREM] standard/cited; [EXACT] hand algebra and/or sympy-verified identity; [NUM] double-precision, uncertified;
[SKETCH] argument outlined only; [CONJ] heuristic; [MODEL] analogy/calibration with no arithmetic map; [CLOSED] route tested and closed (scope stated).
Baseline: release v1.19 (main 65153b7…, 1025 concepts / 1990 relations — figures supplied by the parent; NOT re-verified locally,
the cloud agent must read them from the live repo). Local STATE.md has no v1.19 entry; the developments below come from per-directory notes.

## Central aim (unchanged; must head the section)
TAA thermodynamic / RH-unitarity programme: realise the Weil quadratic form W on log-window tests as an energy/free-energy
with an *independently constructed* positive structure, so that W ≥ 0 on E0 = {ev+ = ev− = 0} (equivalent, window by window, to the RH window
statement) follows from a sign mechanism rather than being assumed. Everything below is ledger, calibration, or a closed route
measured against that aim. The conic/Hodge material is a *model of the sign pattern*, not a constructor.

## Ranked items (for an independent reader; strongest first)
1. **Exact window energy ledger** [EXACT] (ghostfloor1934, bulk1919, moment1975, covariance1956).
   W = P + B,  P = 2 ev+ ev− = 2(C² − S²) = 2Re(C+ · conj C−) in complex form,  B = H_A − M_A‖F‖² = (1/2π)∫ m_A |F̂|²,
   H_A = E_∞ + Σ_{log n<A} a_n ‖F − T_{log n}F‖² ≥ 0 (Gamma Lévy springs + prime springs), M_A = −K0 + 2Σ a_n, K0 = ψ(1/4) − log π = −5.37218.
   B formula valid for every window F (off E0 too); W = B only on ker ev+ ∪ ker ev− ⊇ E0. E0 kills P, *not* the diagonal M_A‖F‖².
   Reflection splits even/odd: W_e = B_e + 2cc^T (rank-one positive), W_o = B_o − 2ss^T (rank-one negative); E0_A = one constraint per sector.
2. **Local product-state reading of every term** [EXACT identities, NUM agreement] (covariance1956, heis1921).
   W_p = log p (‖F‖² − ⟨F, P_p F⟩), P_p = Σ_k p^{−|k|/2} T_{k log p} ≥ 0 (AR(1)/critical-boson covariance); arch = OU tower with rates 2j+1/2;
   M_A = −2 Σ_v E_v[log|x|_v^{(A)}] as a sum of independent LOCAL mean statistics (no coupling on principal ideles, so not a proved "product-formula defect"). E0 ⇔ rate-1/2 OU response window-supported; per-prime responses leak (local poles
   1 + 2πim/log p cancel only globally). Verdict: covariances enter SUBTRACTED → no sign mechanism [CLOSED as sign source].
3. **Semilocal trace identity and Connes cutoff pair** [THEOREM (Connes 1999 Thm VII.4) + EXACT dictionary + NUM] (classes1966, localization1970).
   −I_S(F,F) = W(F) − P(F) on windows with S ⊇ {∞} ∪ {p < e^A}; corrected twisted star: h = χ·(f * f^*), χ(u)=e^{−u/2} (equivalently h = g * g^#, g = χf,
   g^#(u)=e^{−u} conj g(−u)), not (χf)*(χf)^*. Semilocal Fourier F_S = M_c J with phase c_S; −i d/dy log c_S = −m_S: W symbol = −(Wigner time delay).
   Trace identity is semilocal only; it is not a Hodge/sign theorem. Global c ≡ 1 is formal only.
4. **Bordered-inertia criterion and the moment-count picture** [THEOREM (Haynsworth) + EXACT specialization; NUM tables] (moment1975, parent override).
   For a finite-dimensional *invertible* sector form B with constraint vector c, q = ⟨c, B⁻¹c⟩: n−(B|c⊥) = n−(B) − 1 + [q > 0].
   Hence B ≥ 0 on c⊥ iff n−(B) = 0 (q of either sign allowed), or n−(B) = 1 and q ≤ 0. n−(B) ≥ 2 fails regardless of c.
   Both sectors must be controlled separately (even test alone ≠ E0). Stated for finite Galerkin matrices / explicit invertibility hypotheses;
   operator-level discrete spectrum and B⁻¹cosh in infinite dimensions are UNPROVED (PUBLICATION_AUDIT Lemmas 1–2). Numerically: one negative even mode, alignment of cosh with it 0.970 (A=0.6), 0.991 (A=1);
   E0 minimum ESTIMATES near 0.69 (A=0.6) and 0.012 (A=1) [NUM; Ritz values 0.6971/0.01315 are upper bounds; lower-bound-inspired values 0.6919/0.0119 are NOT certified brackets];
   A=2 near-null cluster: UNRESOLVED. Prime-2 scaling λ≈1.07 fails by count (λ2(B_e) crossing 0), not misalignment. No automatic gap from moments.
5. **Independent-representer (matching) test: two explicit candidates fail** [EXACT mechanisms; NUM residuals] (matching1983, finished 10:24 PM CST; governed by PUBLICATION_AUDIT_matching1983.md).
   Necessary identity B(h,·) = κ·C(·) on the window ⇔ response r_h = κ cosh(v/2) a.e. h1 = cosh·1_win: log edge divergence (k(a) ~ 1/2a) [EXACT mechanism].
   h2 = Dirichlet cosh: removes edge log; A=0.6 residual 6.92% [NUM only]; A=1: prime-2 translate of the edge kink at ±(log 2 − A/2) with derivative jump
   a_2 sinh(A/4)/2 = 0.06191 [EXACT under A=1, only n=2 entering], finite-difference 0.06189. h1 failure EXACT at A=0.6 and 1.0 (annihilator Lemma 3).
   Test functions: h1,h2 in form domain D_A; polynomial E0 tests piecewise polynomial (not C^∞), E0 membership exact by IBP with G=G'=0. Strong verified result: only these TWO candidates fail. Structural claim
   "every representer carries a prime-edge singular orbit" is [SKETCH/CONJ] (needs boundary regularity + propagation proof); no universal Gamma-only no-go.
6. **One form, two jobs: conic polarity and Hodge-index sign pattern** [EXACT, MODEL] (incidence1964, duality1967, polarity1980, hodge1981, hodge1979).
   B(v,v) = v_T² − 4 v_Q v_Z on P²: the null conic (model discriminant conic Δ = t² − 4q = 0) is tangency; the timelike interior h = (0:1:1) (focus) has Q(h) = −4, its polar
   is the directrix with Q|_{h⊥} = v_T² + 4 v_Z² > 0; x∞ = (0:1:0) is null and its polar Z = 0 contains it (degenerate complement). Family h_s = (0,1,s):
   Q(h_s) = −4s in homogeneous coordinates (affine representative (0,1/s,1) has Q = −4/s; same projective point, different gauge), complement v_Z = −s v_Q, Q(v) = v_T² + 4s v_Q², degenerating as s → 0. Legendre tangent slopes = Frobenius roots (dual conic).
   Curve product: E alternating on H¹, I(a⊗b, c⊗d) = −E(a,c)E(b,d) symmetric on H¹⊗H¹; mixed real (1,1) primitive vector I = −8 < 0, (2,0)+(0,2) vector +8 > 0.
   Sylvester lemma: n−(B) = 1, B(h,h) < 0 ⇒ B ≥ 0 on h^{⊥B}. This is the *shape* sought, nothing more.
7. **Kähler / Hamiltonian–gradient / uncertainty refinements** [EXACT finite-dim; MODEL for W] (gradient1963, antihol1962, restframe1928, pqr1947, eisenstein1954).
   X_H = −J∇H, J X_H = ∇H; real/imaginary time related by J; Robertson–Schrödinger as PSD covariance (diagonals + determinant); Mandelstam–Tamm needs a
   specified observable (no canonical time operator). Translation-invariant J (Hilbert transform) exists for any g ≥ 0 but does not preserve compact support/E0:
   a compatible J for the window sector must be non-stationary [EXACT obstruction]. Ramanujan system, Serre/Maass raising, E10 = E4E6, B10 = 5/66,
   Wronskian(Q³,R²) = −Q²R(Q³ − R²) = −1728 Q²RΔ: sympy-verified tonight (fam1954_exact.py). Weight-12 calibration ≠ archimedean counterterm (k0_weight.txt).
8. **Local–global rings, principalization, Iwasawa calibration** [EXACT toys; THEOREM citations] (jacobian1950, iwasawa1958, transv1949).
   Λ = Z_p[[T]] regular local dim 2; Λ/(f) regular ⇔ f ∉ m² ("Jacobian" class in m/m²). T² − 27 singular (arithmetic cusp). (μ, λ, ν) ≠ regularity, carry no sign.
   Regular local ⇒ UFD (Auslander–Buchsbaum); does not imply global principality (Z[√−5]). Noetherian ring ≠ Noether charges.
9. **Rankin–Selberg as genuine square-coefficient calibration** [THEOREM] (boundary1982): ∫ y¹²|Δ|² E(z,s) dμ = Γ(s+11)(4π)^{−(s+11)} Σ τ(n)² n^{−(s+11)};
   positive interior pairing → square coefficients; Hecke self-adjointness → real τ(p). No W identity.

## Closed routes that remain closed (scope as stated in AUDIT.md §C)
single positive compression Q = S P̂ S (numerical mismatch with W on the tested cases; NOT a universal impossibility) · local covariance/product state as sign source ·
σ-convexity of log|ξ| (fails near zeros) · weight-12/Petersson as selector of the polarization · Iwasawa invariants as sign · translation-invariant J on E0 ·
moments alone ⇒ gap · formal global c ≡ 1 Gamma–Euler product · map1965 graph-of-flow "cycles" (formal graph only) · user "boundary blueprint"
(conic smooth at ∞, not a modular cusp; Petersson ‖Δ‖ finite positive; σ11 congruence not positivity) · naive star (χf)*(χf)^* · h1, h2 as representers.

## Next missing theorem (precise)
**Matching/representer theorem.** On a fixed window (closed codim-2 E0_A, with stated domain and invertibility hypotheses), construct h_A from Gamma/prime/boundary data
*independently of B⁻¹* such that (i) B(h_A, F) = κ C(F) + κ' S(F) for all window F, including the full response with the M_A diagonal and every prime edge orbit
(the matching1983 kink shows prime-translated edge layers are required in the tested class); (ii) B(h_A, h_A) < 0; and separately (iii) n−(B_e) = 1 and odd-sector control
(n−(B_o) = 0, or n−(B_o) = 1 with q_o ≤ 0). (i)+(ii)+(iii) ⇒ B ≥ 0 on E0_A by Sylvester/Haynsworth; (iii) is the fragile, RH-strength part. The sharp open question from
matching1983 is whether h*_A = B_A⁻¹cosh (when it exists) equals cosh minus a finite prime-indexed sum of edge-layer profiles with one Gamma-determined profile [CONJ].
Any geometric map must land in an appropriate infinite-dimensional (ind-limit / cohomological, domain-specified) space: a finite conic or finite H^{1,1} cannot carry
a faithful full-rank W on the infinite-dimensional analytic E0.

## Proposed Atlas delta (names for cloud; verify none collide with existing v1.19 nodes)
Concepts: `window_energy_ledger`, `pole_form_P_2ReCplusCminus`, `bulk_form_B_off_E0`, `local_product_state_covariance`, `product_formula_defect_mean`,
`twisted_star_convolution`, `semilocal_scattering_phase_time_delay`, `connes_cutoff_pair_two_hankel`, `bordered_inertia_moment_criterion`,
`even_odd_sector_constraints`, `near_null_cluster_A2`, `independent_representer_test`, `prime_edge_kink_orbit`, `conic_polarity_one_form`,
`polar_family_h_s_degeneration`, `kunneth_skew_to_symmetric`, `nonstationary_J_obstruction`, `iwasawa_regularity_class`, `rankin_selberg_square_calibration`.
Relations (subject —type→ object): window_energy_ledger —decomposes→ Weil form; pole_form_P —vanishes_on→ E0; bulk_form_B —survives_on→ E0 (diagonal M_A);
local_product_state —reproduces_terms_of→ window_energy_ledger; local_product_state —fails_as_sign_source→ RH positivity; twisted_star —corrects→ classes1966 pairing;
semilocal_scattering_phase —generates_symbol→ bulk_form_B; connes_cutoff_pair —decomposes_as(D_c − D_cbar − X)→ W−P; bordered_inertia —reduces→ E0 positivity to (count, sign of q);
near_null_cluster_A2 —blocks_certification_of→ bordered_inertia count; independent_representer_test —instantiates→ Sylvester lemma; prime_edge_kink_orbit —obstructs(h2)→ independent_representer_test;
conic_polarity_one_form —models→ Hodge index sign pattern; polar_family_h_s —degenerates_to→ null boundary x∞; kunneth_skew_to_symmetric —produces→ (1,1) negative / (2,0)+(0,2) positive;
nonstationary_J_obstruction —constrains→ Kähler compatible J on E0; iwasawa_regularity_class —separates→ growth invariants from Jacobian rank; rankin_selberg —calibrates(no W identity)→ square coefficients;
Hasse wall / hero parabolic wall / Routh wall / primary–secondary Σ sheets —distinct_from→ each other (keep four separate nodes).
