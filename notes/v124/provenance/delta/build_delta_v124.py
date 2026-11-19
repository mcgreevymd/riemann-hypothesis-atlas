#!/usr/bin/env python3
"""Build delta/atlas_delta_v124.json (v1.24 concepts) against the live v1.23 atlas.json.
Priority and ranking are copied from a template concept (never set by hand). rank is null; the insert script assigns it.
No backslashes (build_public_md.py rejects them)."""
import json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ATLAS=Path(sys.argv[1]) if len(sys.argv)>1 else HERE.parents[3]/'atlas.json'
D=json.loads(ATLAS.read_text(encoding='utf-8')); by={c['id']:c for c in D['concepts']}
NOTRH='RH is not proved; Φ is not constructed; there is no Hodge-type sign.'
def R(t,to,note=''): return dict(type=t,to=to,note=note)
C=[]
def add(id,tmpl,label,name,plain,core,axes,rels,numbers=(),pitfalls=(),uncertain='',proved='',tests='',aliases=(),formula='',lemmas=()):
    C.append(dict(id=id,_template=tmpl,label=label,name=name,aliases=list(aliases),plain=plain,core=core,formula=formula,numbers=list(numbers),
                  axes=axes,uncertain=uncertain,proved=proved,tests=tests,pitfalls=list(pitfalls)+([NOTRH] if label in ('Open','Analogy','Restatement','Numerical') else []),lemmas=list(lemmas),rels=rels))
# ---------------- L194 ----------------
add('cosh_ample_direction_weil_equivalence','hodge_index_zeta_restatement','Restatement',
 'Ample direction = cosh(u/2): RH ⇔ Q ≥ 0 on cosh(u/2)^⊥ for every window; Q ≥ 0 on the Perron complement h_r^⊥ is only implied (TAA Lemma 194)',
 'The pole form P = 2C₊C₋ has one positive eigenvector on every window, cosh(u/2), and one negative one, sinh(u/2). Taking cosh as the ample class of the function-field dictionary, the Hodge-index-type statement "Q ≥ 0 on the L² complement of cosh" for every window is equivalent to RH, like Weil positivity on E0 = ker C₊ ∩ ker C₋. The statement relative to Q’s own ground state h_r (index 1, λ₁(Q) ≥ 0), which has the same inertia condition as Q ≥ 0 on the Q-orthogonal complement of cosh when Q(cosh) < 0, is implied by RH but not equivalent to it. Translation acts on the pole plane as a boost and maps E0 of one window to E0 of the shifted window.',
 'P eigenvalues r ± 2sinh(r/2) with eigenvectors cosh, sinh (exact). Sandwich e₀(W) − λmax(P) ≤ λ₀(Q) ≤ W(ĉ) − λmax(P). Haynsworth: n−(Q|ker L) = n−(Q) − n−(LᵀQ⁻¹L); for one vector v, n−(Q|v^{⊥_Q}) = n−(Q) − [Q(v) < 0]. Parity split G_e, G_o: W > 0 ⇔ G_e < −½ and G_o < ½ (index-1 case); Q > 0 on E0 ⇔ G_e < 0. W ≥ 0 ⇒ Q ≥ 0 on cosh^⊥ ⇒ Q ≥ 0 on E0. Over all windows: RH ⇔ Q ≥ 0 on E0 ∀r (Weil; Bombieri; Yoshida) ⇔ Q ≥ 0 on cosh^⊥ ∀r; RH ⇒ λ₁(Q_r) ≥ 0 ∀r only one-way. Q is Markov on every window (Λ ≥ 0), so h_r is positive and even for every r; corr(h_r, cosh) ≥ 0.993 (r = 1–10).',
 ['restatement ⇔ RH','reference/pole/cusp','structure/frame (Ax1)'],
 [R('refines','hodge_index_zeta_restatement','ample class read as cosh, not as h_r'),R('related','single_null_hyperplane_weil','third equivalent hyperplane form'),R('refines','pole_perron_one_mode','h_r positive for every r (Markov Q)'),R('analogue-of','hodge_index','f₁ + f₂ ↔ cosh, primitive part ↔ E0'),R('corrects','ms2253_review_verdicts','Hodge index relative to h_r is not RH')],
 numbers=['λmax(P) = r + 2sinh(r/2)','corr(h_r, cosh) ≥ 0.993'],
 pitfalls=['Per window, Q ≥ 0 on E0 does not imply W ≥ 0; the equivalences are over all windows.','Q ≥ 0 on E0 for every r is equivalent to RH (not merely implied); the one-way statement is index 1 (λ₁ ≥ 0).','λ₀(Q) < 0 is observed at every tested r but not proved for all r.'],
 proved='Finite linear algebra (lem194 LEMMA_194.md (a), (e)); Weil’s criterion cited for (b).',lemmas=['L194'])
# ---------------- L195 draft ----------------
add('onset_law_conductor_not_sigma_r','ghost_onset','Numerical',
 'The ghost onset is set by the analytic conductor, not by σ′·r* = const (TAA Lemma 195 draft, T1)',
 'A proposed "uncertainty relation" σ′·r* ≈ c for the first window that sees an off-line zero at distance σ′ from the line fails. Across 15 certified Davenport–Heilbronn quartets σ′r* ranges over 0.09–1.58 with no trend in log γ, and at fixed height r* moves only about 0.8 over a 49-fold change in σ′. The ledger’s onset law r* ≈ A·log(qγ/2π) + B − (0.1–0.3)·ln σ′ fits with R² = 0.90–0.98. Z₂’s early onset comes from its lowest zero 2.079 + 7.629i, which lies outside the critical strip.',
 'DH 15 quartets: σ′r* mean 1.02, sd 0.48, R²(log γ) = 0.02. Fixed-γ scans: dr*/d ln σ′ = −0.06 to −0.21. Fits A = 0.82/0.99/0.90, κ = −0.29/−0.11/−0.15 (DH/ζ/L5). Same quartet in ζ vs L5 background shifts by ≈ log 5. Z₁ ghost 0.93297 + 15.66825i: r* = 3.0 (W) / 3.175 (E0, cosh^⊥). Z₂ ghost σ′ = 1.579: 0.85 / 1.35 / 1.15.',
 ['ghost-sensitive','numerics/certificate','sign/positivity (Ax2)'],
 [R('reconfirms','ghost_onset','107-onset law of the ledger'),R('refines','conductor_not_ghost_predictor',''),R('tests','davenport_heilbronn',''),R('tests','epstein','Z₁, Z₂')],
 numbers=['σ′r* ∈ [0.09, 1.58]','R² = 0.02','DH r* = 3.575'],
 pitfalls=['Prime-side B-spline onsets are basis-sensitive upper bounds (DH 3.85 at h = .025, 5.7 at h = .05, 3.58 fine).'],
 tests='t2273 dscan.py, fit_t1.py, epstein12.py.',lemmas=['L195'])
add('matched_entire_control_chi5_vs_dh','conductor_not_ghost_predictor','Numerical',
 'Matched entire control: L(s, χ mod 5, χ(2) = i) stays positive to window 8 on W, E0 and cosh^⊥ while Davenport–Heilbronn fails at 3.58 (TAA Lemma 195 draft, T3)',
 'With the same Gamma factor, conductor 5 and no poles, the Euler product L(χ) (complex, signed coefficients, Hermitian Weil form) has no negative direction up to r = 8, while DH (also signed, but supported on composites) fails. So the separator is prime-power support together with the functional equation, not the sign of the coefficients.',
 'DH: Λ_DH(49)/log 7 = −(2 + κ²) = −2.0807009; of 1361 nonzero c(n) ≤ e⁸, 677 negative and 900 at non-prime-powers (first 6, 12, 14). L(χ): 461 nonzero, all at prime powers, 232 non-real, 116 real negative. DH onset 3.85 (h = .025), fine 3.579–3.580.',
 ['ghost-sensitive','numerics/certificate','sign/positivity (Ax2)'],
 [R('refines','conductor_not_ghost_predictor','E0 and cosh^⊥ restrictions added'),R('instance','euler_fe_conjunction',''),R('tests','davenport_heilbronn','')],
 pitfalls=['Does not show multiplicativity suffices (Beurling and random Euler products are counterexamples in the ledger).'],lemmas=['L195'])
# ---------------- filter sort, closed routes ----------------
add('multiplicativity_filter_sort_2271','ms2253_review_verdicts','Restatement',
 'Ledger lemmas sorted by whether their proof step uses the Euler product (filter 2271): none of the Euler-using steps produces the sign',
 'A proposed filter says a mechanism must use multiplicativity, because the d = −20 Epstein zetas share Gamma factor, conductor and functional equation with ζ_K and still fail. This is the ledger’s standing control. About 75 ledger lemmas were binned: E (really uses the Euler product), S (structure, holds for Epstein/DH), D (Deligne-torus / boost bookkeeping), C (closed routes), P (p-adic), N (Euler-sensitive numerics). No E-bin lemma produces a sign; several show the Euler product is insufficient.',
 'Bins: E 12, S 16, D 24, C 9, P 10, N 4 (approximate, by table rows). Corrections to the filter: the genus L-function L(χ₋₄)L(χ₅) is entire (no pole plane); the ζ_K and genus passes are GRH-numerical; Λ ≥ 0 is neither multiplicativity nor necessary; a compact quarter-turn on E0 repeats TARGET error C6.',
 ['no-go / refuted','structure/frame (Ax1)','Spec ℤ gap'],
 [R('restates','euler_fe_conjunction','standing control'),R('related','epstein',''),R('related','davenport_heilbronn','')],
 pitfalls=['A bookkeeping sort, not a theorem; bin boundaries are editorial.'],lemmas=[])
add('closed_routes_t2271_2284','ms2253_review_verdicts','Restatement',
 'Routes re-checked and closed, 17–18 Nov 2026: Maass–Selberg/Witten, Ruppeiner/Lee–Yang/Fisher, photon duality, f∗f̃, rest-energy framing',
 'Proposals relayed in this period were checked against the ledger. Each is a restatement or a closed route: Maass–Selberg/Witten positivity holds for DH too, and its unitary axis sits half a unit off ζ’s line (the “½ offset” of TARGET C16); thermodynamic curvature (Ruppeiner) is flat for an Euler field and real-β positivity is ghost-blind, and ζ zeros are Fisher zeros, not Lee–Yang zeros; the Hodge star on 2-forms has *² = +1, not the complex-structure identity *² = −1; f∗f̃ is positive-definite but not an effective class; the gravity reading of E0 (P = invariant mass², E0 = zero 2-momentum, Q = internal energy) is framing; degree sets the quartet density and conductor the resolution scale.',
 'Zero count N(T) ≈ (T/2π)·log(q T^d/(2πe)^d). Maass–Selberg (ledger §335; DH analogue also positive). Ruppeiner (L116), Fisher vs Lee–Yang (L124). On a Riemannian 4-manifold ∫F∧*F = ‖F‖² ≥ 0; it is ∫F∧F (the intersection pairing) that can be indefinite. Thus the earlier statement that ∫F∧*F is indefinite was wrong. This supplied Riemannian metric is not the missing arithmetic sign.',
 ['no-go / refuted','physics analogue','ghost-blind'],
 [R('reconfirms','maass_selberg_positivity_blind_to_rh',''),R('reconfirms','ruppeiner_stability_not_RH',''),R('reconfirms','fisher_curvature_operator_ghost_blind',''),R('related','hodge_star_square_fermion_parity','photon duality'),R('related','d_normalization_not_offset','½ offset'),R('related','product_formula_rest_frame','rest-energy framing')],
 pitfalls=['Framing items are labelled as such; none supplies the sign.'],lemmas=[])
add('window_equivalence_principle_framing','lrl_hidden_symmetry_trichotomy','Analogy',
 'Equivalence-principle framing of the window form: short windows see only the archimedean background; primes enter one at a time at r = log n',
 'In the window form the prime term at n is present only when the window exceeds log n, so below log 2 the ζ form is the archimedean term plus poles. The analogy reads this as local flatness, with the primes as tidal curvature. The facts are exact; the reading is framing. Two corrections: the prime-free background of the ζ class is itself positive only up to r ≈ 0.78, so the prime 2 is load-bearing almost at once; and agreement at short windows holds only inside a class with the same Gamma factor and the same poles.',
 'Prime support: log n < r (exact). ζ-class flat form (no primes) fails at r = 0.775 (W, cosh^⊥), 1.225 (E0); q = 5 odd entire class 1.725 / 5.775 / 4.3; ζ_K class (q = 20) 2.5 / 4.675 / 3.3 (Galerkin, h = .025). Z₂ = 2x² + 2xy + 3y² has a₁ = 0, Z₂ = 2·2^{−s}G(s), and its prime side lives at frequencies log(m/2^k), the first being log(3/2) ≈ 0.405. Positivity of W on E0 is certified only for A ≤ 1.1; 0.2812 (log of the plastic number) is the Markov threshold, not a positivity threshold.',
 ['physics analogue','reference/pole/cusp','numerics/certificate'],
 [R('related','plastic_threshold_ccm_markov','Markov, not positivity'),R('related','ghost_onset',''),R('illustrates','euler_fe_conjunction','')],
 pitfalls=['Framing; does not touch (D).','An earlier check wrongly put Z₂’s first frequency at log 2; it is log(3/2) (generalized frequencies).'],lemmas=['L197'])
add('kepler_perpendicularity_framing','lrl_hidden_symmetry_trichotomy','Analogy',
 'Kepler perpendicularity dictionary: cosh ↔ angular momentum L, sinh ↔ Runge–Lenz A, cosh^⊥ ↔ orbital plane; positivity there is inherited from the Euclidean ambient, which the window form lacks',
 'In Kepler’s problem the orbit lies in the plane perpendicular to L, the rotation J = L̂× is the 3D Hodge star of the normal, and the Kustaanheimo–Stiefel lift turns fixed-negative-energy motion (after time change and a constraint) into an oscillator on ℂ² with a compatible positive metric: an analogue of (D), not an arithmetic realization. With ω = dx∧dy and J multiplication by i, ½ω(z,Jz) > 0; the Hamiltonian flow is e^{−it} under i_Xω = dH, up to frequency normalization. It does not transfer: in infinite dimensions there is no canonical J on a complement; the ambient form Q is indefinite (one negative direction from the pole plane), so nothing is inherited; and ζ’s scaling flow is a boost, so asking for a hidden rotation with positive generator is Hilbert–Pólya.',
 'The L²-complement statement ⟨F, cosh(u/2)⟩ = 0, i.e. f̂(0) = −f̂(1) with f̂(s) = ∫F e^{(s−½)u}du, is the RH-equivalent one (over all windows); the Q-orthogonal complement of cosh gives n−(Q) − 1 = index 1, implied only. E0 = ker C₊ ∩ ker C₋ is neither complement (it is codim 1 inside cosh^⊥). The Q-orthogonal conclusion assumes Q(cosh) < 0 and a nondegenerate restriction. KS for E > 0 is an inverted oscillator (boost).',
 ['physics analogue','phase/unitarity (Ax3)','restatement ⇔ RH'],
 [R('related','ks_quaternion_lift',''),R('related','moser_orbit_space_s2xs2',''),R('related','kepler_so4_contraction',''),R('restates','hilbert_polya','secret rotation with positive generator'),R('related','hilbert_J_full_line_restates_weil','free J')],
 pitfalls=['Framing plus a restatement; explains the gap and does not close it.','Rotating-frame/Lagrange variants are closed (TAA Lemma 161; TARGET C14).'],lemmas=[])
# ---------------- L196 ----------------
add('fq_genus2_sign_anatomy','fq_ensemble_aggregation','Theorem',
 'Anatomy of the sign over F_q (genus 2): no count-level rung kills the fakes; the first rung that does is Hodge index on C×C (TAA Lemma 196)',
 'For genus-2 curves over F_q (q = 3–13), candidate L-polynomials were filtered by a ladder of ingredients: functional-equation shape, integrality, nonnegative point counts, nonnegative closed-point counts (a genuine Euler product), the hyperelliptic twist, and Jacobian group orders. Thousands of off-circle fakes survive every rung. Hodge index on C×C at a single n is equivalent to the Weil bound at n, and the depth needed to kill every fake grows with q. The sign comes from Frobenius being a morphism (effective graph classes, Riemann–Roch, an ample class), not from any property of the counts.',
 'Thm 196.1: N_n ≥ 0 for all n ⇒ max|α| ≤ q (box complete). Off-circle survivors after all count rungs: 12/172/586/2555/4322 (q = 3/5/7/11/13). Rung (iv) reproduces L166, now certified for all d. Hodge index at n ⇔ 16qⁿ − S_n² ≥ 0 (0 mismatches over 201,800 pairs). Depth N*(q) = 4/5/7/9/12. 196.6: adding a point fails at windows 1–4; removing one stays positive but is not pure; the FE is needed for positivity ⇒ purity.',
 ['geometry over F_q','sign/positivity (Ax2)','no-go / refuted'],
 [R('refines','fq_ensemble_aggregation',''),R('refines','beurling_curve_fakes','all-d certification'),R('uses','hodge_index',''),R('uses','frobenius_graph_lattice',''),R('constrains','euler_fe_conjunction','Euler × FE does not carry the sign over F_q')],
 numbers=['N*(q) = 4, 5, 7, 9, 12','off-circle survivors 4322 at q = 13'],
 pitfalls=['Nothing is claimed about ζ.','Honda–Tate/Rück classification of non-Jacobian survivors not done.','(B) restates T-D2; (D) is framing.'],
 proved='196.1, 196.3(a,b), 196.4 by hand (lem196 LEMMA_196.md); census in exact integer arithmetic with tail bounds.',lemmas=['L196'])
add('fq_window_finite_rank_onset','fq_ensemble_aggregation','Theorem',
 'Over F_q the window form has finite rank ≤ 2g and the pole plane is a real off-circle FE pair: n−(Q) = n−(W) + 1 and onset ≤ 2g − 1 for every fake (TAA Lemma 196.4)',
 'In normalized coordinates the function-field window form is W(c) = Σ_j ĉ(β_j)ĉ(1/β_j), a form of rank at most 2g, and the pole term is the same expression at the real pair β = q^{±½} with multiplicity −1. So every fake fails by window 2g − 1 regardless of how close its roots are to the circle, and the failure is one root, not one place. True curves are rigidly, not robustly, positive: W is singular off 2g directions. Naming: TARGET’s Q_ff is this W.',
 'Signatures: on-circle pair (2,0); real off-circle pair (1,1); complex quadruple (2,2). L*_W ≤ 3, L*_E0 ≤ 5 (g = 2). 600/600 sampled fakes: rank 4, n−(W) = #{|β| > 1}, n−(Q) = n−(W) + 1. No onset law in δ (corr ≤ 0.30). Degree-2 share of the negative vector 0.46 vs 0.23 random (×2.0, at the §351 threshold): no robust localization.',
 ['geometry over F_q','reference/pole/cusp','ghost-sensitive'],
 [R('analogue-of','cosh_ample_direction_weil_equivalence','exact over F_q'),R('contrasts-with','onset_law_conductor_not_sigma_r','finite genus makes onset immediate'),R('refines','pole_perron_one_mode','pole pair = off-circle FE pair')],
 pitfalls=['Exact over F_q only.'],lemmas=['L196'])
# ---------------- L197 ----------------
add('euler_fe_ablation_localization','ghost_onset','Numerical',
 'Euler × FE ablation with failure localization on ζ, ζ_K (d = −20) and L(χ mod 5): every single-ingredient fake fails by window 5.7, but the localization is tautological or diffuse (TAA Lemma 197)',
 'Matched families on the same Gamma factor and conductor were ablated: functional equation kept with the Euler product broken (DH, the d = −20 pencil ζ_K + λ·L(χ₋₄)L(χ₅) including Z₁ and Z₂), and Euler product kept with the functional equation lost (one perturbed local factor, a deleted prime, Beurling primes, a rotated χ(2), a wrong conductor). The four true members stay positive to window 8; all 36 fakes fail. For a one-prime perturbation the negative direction sits on that prime by construction, so a "share" test is vacuous; the informative number is the detection lag, which grows with the analytic conductor. For the FE-only fakes, composites carry 0–87% of the defect depending on the member.',
 'Fakes: (b) r* 0.85–5.7, (c) 0.78–4.6 (W). ζ × (1 − ε2^{−s})^{−1}: r* = 0.775–1.125 for |ε| = 0.2 → 10⁻⁴ (lag ≈ 0.03–0.06 per e-fold of 1/|ε|); ζ_K: 2.5–4.5. Truncations: r* − log(next prime power) = 0.027–0.051 (restates ledger §304). Pencil λ < 0 branch: λ = −0.3 → 2.0, −0.7 → 1.15, −1 (Z₂) → 1.35 (E0). Composite share of the defect: DH 74%, Z₁ 47%, λ = .02 87%, λ = 3 25%, λ = −0.7 0%. Eigenvector peak: DH 84.5 (ghost 85.70), Z₁ 14.3 (15.67). True-member Galerkin minima fall to 10⁻⁸–10⁻¹⁰ by r = 8.',
 ['ghost-sensitive','numerics/certificate','sign/positivity (Ax2)'],
 [R('tests','euler_fe_conjunction','§351 design run'),R('reconfirms','ghost_onset',''),R('refines','conductor_uniform_shift','detection lag grows with log conductor'),R('tests','davenport_heilbronn',''),R('tests','epstein','pencil incl. Z₁, Z₂')],
 numbers=['36/36 fakes fail by r = 5.7','ζ flat region ends at r = 0.775'],
 pitfalls=['Galerkin onsets are upper bounds; DH and the λ = .02 member are basis-sensitive (3.85 vs 5.7; 5.675 vs 6.8).','Mostly a restatement of the standing control; does not touch (D).'],
 tests='notes/v124/provenance/scripts/lem197 (l197.py, extra197.py, conv196.py).',lemmas=['L197'])
add('poisson_completion_deleted_place_positive','conductor_uniform_shift','Theorem',
 'Deleting a local factor and restoring its diagonal term adds a positive Poisson form: an Euler product without the functional equation can be window-positive (TAA Lemma 197 (vii), the ζ-side twin of Lemma 196.6)',
 'Removing the Euler factor at p from ζ removes the prime-power terms at k·log p, k ≥ 1. Adding back log p times the squared norm completes them to a Poisson sum over all k, which is a positive form. So the modified form is the ζ form plus something positive: positive wherever ζ’s form is, although the modified function has extra zeros on Re s = 0 and no functional equation. Adding an extra factor instead subtracts a Poisson form and fails at once. Over F_q this is Lemma 196.6 (removing a point keeps W > 0; adding one fails).',
 'log p·Σ_{k∈ℤ} p^{−|k|/2} g(k log p) = log p·∫|F̂(t)|² P_p(t) dt/2π, P_p = Poisson kernel at radius p^{−½} (> 0). Numerical: ζ minus p ∈ {2, 3, 5} with + log p diagonal: no onset to r = 8; ζ_K at 2, 5 (ramified) likewise, at 3 (split) after + 2 log 3. With the extra factor and − log p: r* = 0.125–0.175 (ζ), 1.2–1.5 (ζ_K).',
 ['sign/positivity (Ax2)','ghost-blind','reference/pole/cusp'],
 [R('analogue-of','fq_genus2_sign_anatomy','L196.6 convention A'),R('constrains','euler_fe_conjunction','FE loss alone does not force failure'),R('related','euler_fe_ablation_localization','')],
 pitfalls=['Positivity without the FE does not imply purity.','Positivity of the base ζ form on every window is RH; certified only for A ≤ 1.1 on E0.'],
 proved='Poisson completion (two lines; lem197 LEMMA_197.md (vii)).',lemmas=['L197'])
add('euler_fe_split_not_sign_carrier','hodge_index_zeta_restatement','Restatement',
 'The ζ/DH split by Euler product × functional equation is a diagnostic pattern, not evidence that these ingredients carry the sign (Lemmas 196 and 197 reconciled)',
 'Every tested separator of ζ from Davenport–Heilbronn runs through the Euler product together with the functional equation. Over F_q, however, thousands of off-circle fakes have both and still fail; only Hodge index on C×C, from the effectivity of Frobenius graphs, kills them. On the ζ side, ablation shows both ingredients look necessary in windows ≤ 8, but positivity can survive the loss of the functional equation (Poisson completion), and failure localization is tautological or diffuse. Both settings show rigid, marginal positivity in the true cases.',
 'F_q: rungs (iii)–(vi) leave 12–4322 off-circle fakes (q = 3–13). ζ: 36/36 single-ingredient fakes fail by r = 5.7; deleted-place + diagonal stays positive. Answer over F_q (TARGET T-D2): effectivity + Riemann–Roch + an ample class, not a property of the coefficients.',
 ['restatement ⇔ RH','Spec ℤ gap','no-go / refuted'],
 [R('constrains','euler_fe_conjunction','pattern, not mechanism'),R('related','fq_genus2_sign_anatomy',''),R('related','euler_fe_ablation_localization',''),R('related','frobenius_graph_lattice','')],
 pitfalls=['Does not touch (D).'],lemmas=['L196','L197'])
ids={c['id'] for c in C}
for c in C:
    assert c['_template'] in by, c['_template']; t=by[c['_template']]; c['priority']=t['priority']; c['ranking']=t['ranking']; c['rank']=None
    for r in c['rels']: assert r['to'] in by or r['to'] in ids, (c['id'],r['to'])
def hb(o):
    if isinstance(o,str): return chr(92) in o
    if isinstance(o,dict): return any(hb(v) for v in o.values())
    if isinstance(o,list): return any(hb(v) for v in o)
    return False
assert not hb(C)
out=dict(base=dict(version='v1.23',concepts=len(D['concepts']),relations=sum(len(c['rels']) for c in D['concepts'])),proposed='v1.24',
         added_concepts=len(C),added_relations=sum(len(c['rels']) for c in C),concepts=C)
(HERE/'atlas_delta_v124.json').write_text(json.dumps(out,indent=1,ensure_ascii=False)+'\n',encoding='utf-8')
print(out['base'],out['added_concepts'],out['added_relations'])
