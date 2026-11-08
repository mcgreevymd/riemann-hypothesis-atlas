# atlas1987 — AUDIT: exact overrides and claim statuses (binding on cloud text, Atlas nodes and manuscript)
Nov 7 2026 ~10:35 PM CST. **RH is not proved.** All numerics are double precision and uncertified unless marked otherwise.
Label note (10:40 PM CST): conic figures use the neutral label "model discriminant conic"; h_s=(0,1,s) has Q=−4s homogeneously, affine representative (0,1/s,1) has Q=−4/s. M_A local-mean reading is not a proved product-formula defect.
Precedence: PUBLICATION_AUDIT_matching1983.md (parent math audit, 10:25 PM CST) overrides raw/superseded notes for matching1983 and moment1975 criteria.
Labels: THEOREM / EXACT / NUM / SKETCH / CONJ / MODEL / CLOSED / WRONG(superseded).

## A. Overrides of earlier scratch wording (the newer statement wins)
| # | Source | Old wording | Binding wording | Status |
|---|---|---|---|---|
| A1 | map1965 | Q "graph-of-flow" Φ(F) gives cycles / divisor classes | Formal graph integral only; pairing was defined from bulk; no cycles, no Num, no Hodge structure | WRONG→formal |
| A2 | map1965 | "Hodge-side form is W" | −I = W − P (bulk); equal to W only on E0 | EXACT correction |
| A3 | classes1966 §1 | I_S(h1,h2)=τ_S(h1*h2^*) | I_S(f1,f2)=τ_S(χ·(f1*f2^*)), χ=e^{−u/2}; h = g*g^# with g=χf, g^#(u)=e^{−u}conj g(−u) (twisted star) ≠ (χf)*(χf)^* (standard star). Numbers in classes1966 used the correct h and stand | EXACT correction (localization1970 §0) |
| A4 | classes1966 L1–L5 | — | Trace identity −I_S = W − P is SEMILOCAL (finite S ⊇ {∞}∪{p<e^A}, window support). Not a Hodge/sign theorem | THEOREM+EXACT, scope-limited |
| A5 | localization1970 §1 | "globally c=1 ⇒ F=J" | Formal only: no global Gamma–Euler-product c≡1 statement is claimed | FORMAL |
| A6 | localization1970 §3 | — | Q=S P̂ S positive compression: D ≥ W on 3 tests at A=1 and D depends on S while W does not (A=0.6) — numerical mismatch with W. NOT a universal "no single compression works" theorem | NUM, CLOSED (tested cases) |
| A7 | localization1970 §4 | W − P = D_c − D_cbar − X | Exact as a trace identity under the assumption that the limiting traces exist/converge for the test class (trace-class/limit assumptions FLAGGED for "signed leakage"); X numbers NUM | EXACT given assumptions |
| A8 | moment1975 | E0 minima "A=0.6 ≈ .69, A=1 ≈ .012" | Estimated, uncertified; NOT certified brackets (Ritz 0.6971/0.01315 upper; 0.6919/0.0119 lower-bound-inspired). Ritz (Galerkin) values are UPPER bounds on minima; lower brackets rely on numerical tail estimates; no lower-bound proof. A=2 UNRESOLVED (near-null cluster ~1e−15). No automatic gap from moments | NUM |
| A9 | moment1975 sector line + matching1983 raw notes l.36 (both now corrected; raw kept as notes1983_raw_superseded.md) | "B ≥ 0 on E0_A ⇔ n−(B_e) ≤ 1 & q_e ≤ 0" (blanket; fails at index 0 where q>0) | Lemma 1 of PUBLICATION_AUDIT: finite real symmetric INVERTIBLE B: n−(B|ker c)=n−(B)−1+[q>0], n0=[q=0]. Bordered inertia requires finite dimension (or compressed discrete-spectrum setting) and B invertible on the sector. Then: n−=0 ⇒ PSD on c⊥ already, q of either sign; n−=1 ⇒ need q ≤ 0; n− ≥ 2 ⇒ fail. Even test alone ≠ full E0: odd sector controlled separately. B⁻¹ / representer h*=B⁻¹cosh exists only under invertibility/domain assumptions; not universally asserted | THEOREM (Haynsworth) with hypotheses |
| A10 | ghostfloor1934/compat1907 | E0 "codim 2" | Global E0 (all test functions) is DENSE (ev± unbounded); on a fixed window E0_A is CLOSED codim 2 (cosh, sinh ∈ L²) | EXACT |
| A11 | all | "W = B" | Full W = B + P off E0; P = 2ev+ev− = 2(C²−S²) = 2Re(C+·conj C−). W and B NOT equated off E0 (full-W and E0-bulk are different jobs, moment1975 controls) | EXACT |
| A12 | all | "E0 removes the counterterm" | E0 kills P only; diagonal M_A‖F‖² remains (bulk) | EXACT |
| A13 | hodge1979/restframe1928 | "ample ⇒ Hessian positive" | Hodge index concerns the particular intersection pairing on a finite-dim Num of a projective surface; not arbitrary Hessians; ample ⇒ some positive curvature representative (Kodaira), not every one | THEOREM, scope |
| A14 | hodge1981 | "H^{1,0}⊗H^{0,1} all negative" | Curve product: mixed real primitive (1,1) vector (dz⊗dz̄ + dz̄⊗dz) gives I = −8 <0; (2,0)+(0,2) real vector gives +8 > 0. Not all of H¹⊗H¹ negative; mixed sector ≠ whole primitive H^{1,1} in general (algebraic classes / Néron–Severi) | EXACT (elliptic, area-1 normalization) |
| A15 | jacobian1950/iwasawa1958 | — | Noetherian ring ≠ Noether charges (pun only). Regular local ⇒ UFD (Auslander–Buchsbaum) ≠ global principal (Z[√−5] class number 2) | THEOREM |
| A16 | boundary1982 (user resource) | conic degenerates at ∞ = modular cusp; y-intercept −∞; Petersson norm of Δ degenerates; σ11/E12 gives positivity | FALSE: conic is smooth at ∞ (affine-chart artifact; x∞ is a smooth point of the projective conic); not a modular cusp; no literal "y-intercept ∞"; ‖Δ‖_Pet finite positive; E12/σ11 (691) is an arithmetic congruence, not real positivity | WRONG |
| A17 | boundary1982 | — | Rankin–Selberg unfolding: square-coefficient calibration GENUINE; gives NO W identity | THEOREM, no bridge |
| A18 | walls1960/hero_v111 | "two walls = Beurling primary/secondary" | Keep distinct: Hasse wall (Δ=0 in pencil/conic), hero parabolic wall a²=4q and Routh (Krein-collision) wall, primary/secondary Σ sheets | CLARIFIED |
| A19 | polarity1980–hodge1981 | conic "constructs" positivity | Conic is a model of the sign pattern only, not a constructor of h or of positivity for W | MODEL |
| A20 | matching1983 | "all representers have singular prime-edge orbit"; Gamma-only no-go; edge-orbit ansatz | SKETCH/CONJ only: needs boundary-regularity + singularity-propagation proof. Verified: exactly TWO explicit candidates (h1, h2) fail; kink mechanism legitimate (jump a_2 sinh(A/4)/2 = 0.06191 EXACT; FD 0.06189). h2 A=0.6 residual 6.92% NUM only. Full response must include W/B response with M_A cancellation (the resp() formula includes −M_A h and paired Gamma integrand) | EXACT/NUM/CONJ split |
| A20b | matching1983 test domain | — | h1, h2 ∈ form domain D_A (finitely many jumps/kinks). Polynomial E0 tests F=(∂²−1/4)G, G=(1−t²)²t^k are piecewise polynomial with jumps at ±A/2: NOT C^∞/C_c^∞. Exact E0 membership by integration by parts using only G=G'=0 at edges. Disproof is on D_A∩E0; C_c^∞ version via annihilator Lemma 3 (props 4–5); density C_c^∞∩E0 in D_A∩E0 plausible, NOT proved. Operator-level discrete spectrum and existence of B⁻¹cosh in infinite dimensions: UNPROVED assumptions. h2 at A=1 EXACT only under A=1 (only n=2 enters); for general A shifts may cancel jumps, no claim | EXACT/UNPROVED split |
| A21 | geometric map | E0 → finite H^{1,1} / conic | A map from infinite-dim analytic E0 to finite H^{1,1} cannot be faithful with full-rank W. Any target must be an appropriate infinite-dim / ind-limit / cohomological space with domain specified | EXACT (dimension) |
| A22 | map1965 | "I_ext npos=1" at A=2 | Fragile: prime couplings ×1.002 → npos 7; 9–10 near-null eigenvalues; signature not certified | NUM, fragile |
| A23 | synthesis1953 | σ-convexity / weight-12 selects polarization | log|ξ(σ+it)| not σ-convex near zeros (xi_sigma_check.txt); 2(ψ(k/2)−log2π) ≠ k/12 (k0_weight.txt) | NUM, CLOSED |
| A24 | eisenstein1954 | [H] hand identities | Now sympy-verified (fam1954_exact.py, tonight): Serre/Maass raising, D12Δ=0, R12Δ=E2*Δ, Wronskians, E10=E4E6 (q-series), B10=5/66. Numerical Wronskian part of fam1954.py was interrupted and remains UNRUN | EXACT (symbolic) / UNRUN |

## B. Claim status table (headline claims allowed in Atlas/manuscript)
- ALLOWED (EXACT/THEOREM): window ledger (A11, A12); local product-state term-by-term reading (identities); semilocal trace identity with twisted star; semilocal phase ↔ symbol (time delay);
  bordered-inertia criterion with hypotheses; Sylvester lemma; conic polarity algebra and h_s family; Künneth signs; Iwasawa regularity toys; Rankin–Selberg unfolding; prime-2 kink jump.
- ALLOWED ONLY AS NUM (with "uncertified"): per-place cancellation numbers; Connes-model reproduction; D vs W mismatch; E0 minimum brackets; alignment 0.970/0.991; h2 residual 6.92%.
- NOT ALLOWED: any statement that RH, GRH, a window positivity, a spectral gap, a Hodge structure for Q, cycles/Num for Q, or a universal no-go has been proved.

## C. Closed routes (scope) — see SYNTHESIS.md list; each remains closed only within the stated scope (tested candidates / stated hypotheses).

## D. Unresolved mathematical contradictions / tensions (report, do not paper over)
1. Near-null magnitude mismatch at A=2: map1965 (sine Galerkin J=40) reports 9–10 eigenvalues ~8e−4; moment1975 reports ~1e−15. Different bases/quadrature/encoding; both say "uncertified, unresolved"; the cloud must not quote either as an eigenvalue of B.
2. RESOLVED by parent audit: the blanket iff (raw matching1983 l.36, moment1975 sector line) was wrong at index 0; both notes corrected, raw draft archived as superseded; A9/Lemma 1 govern.
3. hero_v111.py labels the parabolic wall "Hasse edge" (|tr|=2) while A18 requires distinct nodes: the cloud should present the hero parabolic wall as *an instance of* the discriminant wall in the torus/trace parameter, kept as a separate node from the Beurling-pencil Hasse wall and the Σ sheets; flag for editorial decision, no mathematical contradiction implied.
4. Sign of q_e ≈ −0.5000004 at A=1 (and −0.5 at A=2) sits at the Sherman–Morrison threshold −1/2 for full W: full W is near-singular there. Not a contradiction, but no claim about full-W positivity may be made.
5. v1.19 baseline (commit, counts) not verifiable locally (STATE.md ends at b1762 / v1.17 staging); cloud must reconcile against the live repo.
