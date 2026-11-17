#!/usr/bin/env python3
"""Build delta/atlas_delta_v123.json (v1.23 concepts) against the live v1.22 atlas.json.
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
# ---------------- lemmas 188-193 ----------------
add('plastic_threshold_ccm_markov','window_shioda_tate_split','Theorem',
 'Plastic-number threshold: CCM’s truncated Weil form is Markov exactly for window length A ≤ log P, P³ = P + 1 (TAA Lemma 188)',
 'Inside a window, the off-diagonal kernel of CCM’s form (pole terms included) is the pole kernel minus the archimedean jump kernel. The n = 0 term of the jump kernel cancels the decaying half of the pole kernel, and what is left is non-positive exactly up to jump length log P, where P is the plastic number. Below that length, and before the first prime enters at log 2, the form is a Dirichlet form plus a potential bounded below, so its ground state is simple, strictly positive and even.',
 '−J(w) + 2cosh(w/2) = e^{|w|/2} − e^{−5|w|/2}/(1 − e^{−2|w|}) ≤ 0 ⇔ y³ − y − 1 ≤ 0 (y = e^{|w|}) ⇔ |w| ≤ log P = 0.28119957432296…; one real root (discriminant −23). CCM λ ≤ √P = 1.15096, Suzuki a ≤ 0.14060. Potential = K₀ + κ + m, bounded below, log-divergent at the edges (not bounded). Perron–Frobenius–Faris ⇒ simple, positive, even ground state (even-simplicity) for A ≤ log P. Positivity of the eigenvalue not claimed.',
 ['sign/positivity (Ax2)','ghost-blind','reference/pole/cusp'],
 [R('refines','pole_perron_one_mode','explicit Markov range with the poles included'),R('uses','arch_levy_khintchine_sos','jump kernel'),R('refines','lit_de_andrade_silva_pole_perron_2026','closed form of his t* = 0.28119957'),R('related','lit_suzuki_screw_function_2026','explicit constant for the small-a regime'),R('related','pole_plane_krein_boundary_condition','')],
 numbers=['log P = 0.28119957432296','√P = 1.1509639','a* = 0.1405998'],
 pitfalls=['The value t* and a ≤ t*/2 are de Andrade Silva’s (Zenodo 20682833, 13 Jun 2026); only the closed form log P is new as far as checked.','A diagnostic for CCM approximants; it does not touch (D).'],
 proved='Hand proof (lem2253 LEMMAS_2253.md, L188); plastic.py checks the root to 50 digits and one sign change on (0, 5].',lemmas=['L188'])
add('single_null_hyperplane_weil','hodge_index_zeta_restatement','Restatement',
 'Single-null-hyperplane form of Weil’s criterion: RH ⇔ Q ≥ 0 on ker C₊ for every window (TAA Lemma 189)',
 'The pole term 2C₊C₋ vanishes on either null hyperplane, so Q equals W there. Since E0 sits inside ker C₊, which sits inside the whole window space, the hyperplane condition is sandwiched between Weil positivity and E0-positivity, so it is equivalent to RH over all windows. The two hyperplanes are swapped by u ↦ −u, so their spectra coincide.',
 'E0 ⊂ ker C₊ ⊂ L²(window); Q = W on ker C±. Interlacing: e₀(W) ≤ min Q|ker C₊ ≤ o₀(W) and ≤ min Q|E0. Galerkin (A = 0.28–5, N ≤ 150): min Q|ker C₊ = (0.96–0.999)·o₀(W), 1.5× (A = 0.28), ≈ 60× (A = 1), ≈ 10⁴× (A = 3–5) below min Q|E0 (= λ₁(Q) for A ≥ 1). The hyperplane removes W’s even Perron direction, not its odd one.',
 ['restatement ⇔ RH','reference/pole/cusp','numerics/certificate'],
 [R('restates','weil_positivity',''),R('refines','pole_plane_krein_boundary_condition','one null direction penalised'),R('contrasts-with','window_shioda_tate_split','codimension 1 vs 2'),R('related','ms2253_review_verdicts','claim (ii)')],
 pitfalls=['Not a mechanism and not stronger than E0-positivity; the per-window margin is smaller.','Galerkin minima are upper bounds.'],lemmas=['L189'])
add('jump_kernel_exponents_gamma_poles','archimedean_weyl_kernel','Theorem',
 'The exponents 2n + ½ of the archimedean jump kernel are the poles of Γ(s/2): n = 0 is the pole s = 0 of Λ, n ≥ 1 the trivial zeros (TAA Lemma 190)',
 'Writing J(w) = Σ e^{−(2n+½)|w|}, each exponent is ½ minus a pole of Γ(s/2). The n = 0 term belongs to s = 0, which is a pole of the completed zeta function (ζ(0) = −½ is not zero), not a trivial zero. That is why it cancels exactly against part of the pole kernel. Reading the tower as discrete-series orbits is a Casimir match (weights 4n + 2), not a derivation, and the kernel depends only on the Γ-factor.',
 'J(w) = e^{|w|/2}/(2 sinh|w|) = k∞(|w|) = Σ_{n≥0} e^{−(2n+½)|w|}; 2n + ½ = ½ − s_n, s_n = −2n. Casimir s(1−s) = ¼ − k², k = 2n + ½ ↔ D_m, m = 4n + 2. Odd characters: Γ_ℝ(s+1) gives exponents 2n + 3/2.',
 ['ghost-blind','reference/pole/cusp','structure/frame (Ax1)'],
 [R('refines','arch_levy_khintchine_sos',''),R('corrects','ms2253_review_verdicts','claim (iii): n = 0 is the pole, not a trivial zero'),R('explains','plastic_threshold_ccm_markov','pole-against-pole cancellation'),R('related','eisenstein_resonances_rho_half','')],
 pitfalls=['The orbit reading is framing; the kernel is the same for any L-function with the same Γ-factor (ghost-blind).'],lemmas=['L190'])
add('odd_sector_scalar_even_simplicity','pole_perron_one_mode','Numerical',
 'Odd-sector scalar criterion for CCM even-simplicity: e₀ < o₀ ⇔ S(A) = 1 − 2⟨s,(Q_odd − e₀)⁻¹s⟩ > 0; S > 0 for A = 0.28–5 (TAA Lemma 191)',
 'By parity CCM’s form is Q plus a positive rank-one term along cosh on even functions and Q minus a rank-one term along sinh on odd ones. The lowest odd eigenvalue is the root of a decreasing secular function, so “even ground state below every odd state” is the sign of that function at the even ground energy. Computed at every tested window it is positive. This complements de Andrade Silva’s even-sector reduction.',
 'h(μ) = 1 − 2⟨s,(Q_o − μ)⁻¹s⟩ strictly decreasing on (−∞, min spec Q_o), root o₀. Sine basis (hp2251 assembly), N = 50/100/150, digits doubled at N = 100 (identical): S(0.28) ≈ 0.9989, S(1) ≈ 0.010, S > 0 through A = 5; o₀/e₀ ≈ 3.9, 29, 210, 370, 920, 2.5e3 at A = 0.28, 0.6, 1, 1.2, 1.5, 2.',
 ['numerics/certificate','sign/positivity (Ax2)','reference/pole/cusp'],
 [R('refines','lit_de_andrade_silva_pole_perron_2026','odd-sector counterpart of his Krein corollary'),R('uses','pole_plane_krein_boundary_condition','rank-one secular equation'),R('tests','ccm_even_simplicity_hp2251','')],
 pitfalls=['Galerkin eigenvalues are upper bounds; nothing is certified beyond A ≤ log P.','A ≥ 2.5 not converged in N.','Diagnostic for CCM approximants; does not touch (D).'],lemmas=['L191'])
add('hilbert_J_full_line_restates_weil','nonstationary_J_obstruction','Theorem',
 'The Hilbert-transform J on the full u-line commutes with scaling for free, and compatibility turns the metric into the Weil symbol: positivity is Weil’s criterion verbatim (TAA Lemma 192)',
 'The Hilbert transform is a Fourier multiplier, so it commutes with every translation, squares to −1, and is compatible with any translation-invariant form. The induced metric is positive exactly when the form’s symbol is a positive measure, and for the Weil distribution that symbol is the zero distribution. So this J makes the commutation in (D) automatic by moving all content into positivity, which is RH. It also lives on the test space, not on the H¹-type space the target asks for.',
 'H = −i sgn D; [H, Θ_t] = 0; ω_B(f,g) = −B(f,Hg) antisymmetric, ω_B(f,Hg) = B(f,g); g > 0 ⇔ b ≥ 0 (Bochner). TARGET C6/C7/C12: J must act on ℋ; ω built from W is circular (t2154); on windows H leaks (atlas #518).',
 ['restatement ⇔ RH','no-go / refuted','phase/unitarity (Ax3)'],
 [R('refines','nonstationary_J_obstruction','full-line version'),R('restates','weil_positivity',''),R('no-progress-on','kahler_triple_polarization','J on the wrong space'),R('corrects','ms2253_review_verdicts','§11 “to check”')],
 pitfalls=['Does not empty (D): it re-encodes RH.'],lemmas=['L192'])
add('chi4_markov_range_log3','pole_perron_one_mode','Numerical',
 'L(s, χ₄): the pole-free Weil form is Markov exactly for A ≤ log 3; its ground state stays even, nodeless and positive through A = 4 (Galerkin) (TAA Lemma 193)',
 'For the odd character mod 4 there are no pole terms; the archimedean jump kernel (Γ_ℝ(s+1)) is positive, and the only positive off-diagonal entries come from primes with χ(p) = −1, the first being 3. So the Perron argument works up to window length log 3. Numerically the ground state stays even and nodeless well beyond, with the same even-below-odd pattern as ζ, so that pattern is not caused by the pole.',
 'K₀^χ = ψ(¾) + log(4/π) = 0.1562; J_χ(w) = Σ e^{−(2n+3/2)|w|}. Galerkin minima (N = 100): 0.3179, 0.1427, 0.0780, 0.0354, 2.143e−3, 6.83e−7, 4.70e−13, 2.12e−23, 1.34e−56 at A = 0.8, 1, 1.09, 1.2, 1.5, 2, 2.5, 3, 4; lowest odd 10²–10⁴ times larger; no negative Galerkin eigenvalue. The manuscript’s χ₄ values equal our N = 50 values (1–6% above N = 100).',
 ['numerics/certificate','ghost-sensitive','sign/positivity (Ax2)'],
 [R('contrasts-with','plastic_threshold_ccm_markov','character sign vs pole'),R('instance','lorentzian_index_pole_free','κ = 0 without a pole plane'),R('related','davenport_heilbronn','DH control not run')],
 pitfalls=['Galerkin upper bounds; A ≥ 2.5 not converged in N.','Consistent with the N-L necessary condition; not a mechanism.'],lemmas=['L193'])
# ---------------- hp2251 ----------------
add('ccm_even_simplicity_hp2251','pole_perron_one_mode','Numerical',
 'High-precision CCM even-simplicity, A = 1–6: lowest eigenvalue even, simple, nodeless; odd 10²–10⁴ above; Q has one negative Galerkin eigenvalue (hp2251)',
 'CCM’s programme needs the lowest eigenvalue of the truncated Weil form to be simple with an even eigenvector. With 60–600 digits and bases up to 200 functions it holds at every window from 1 to 6. The relevant eigenvalues are astronomically small (down to about 1e−242), which is why double precision showed only noise from A = 2 on.',
 'Sine basis N ≤ 200, dps 60–600, every reported run stable under digit doubling (60 digits fails at A ≥ 3). QW e₀: 9.73e−7 (A = 1), 6.5e−30 (2), 2.2e−95 (3), 6.3e−162 (4), 5.5e−207 (5), 6.9e−242 (6) at N = 200; o₀/e₀ ≈ 2.1e2–1.1e4. Q ground states (Legendre, M = 220): −1.98747, −4.30591, −7.23122, −11.2308 (A = 1–4).',
 ['numerics/certificate','reference/pole/cusp','sign/positivity (Ax2)'],
 [R('tests','lit_de_andrade_silva_pole_perron_2026','scalar criterion regime'),R('reconfirms','pole_perron_one_mode',''),R('reconfirms','negdir_is_pole_plane_interlacing','cos(Q-ground, cosh) 0.995 → 0.9999'),R('related','semilocal_prolate_boundary_lead','prolate near-null ladder')],
 pitfalls=['A ≥ 2.5: the tiny eigenvalues still fall with N; they are upper bounds, only the ordering is stable.','Galerkin counts: “one negative eigenvalue” is a lower bound on the true index; positive minima are not certificates.','κ = 1 at A ≤ 6 cannot see off-line zeros above the verified heights; not new evidence for RH.'])
# ---------------- literature ----------------
add('lit_suzuki_screw_function_2026','suzuki_line','Cited',
 'Suzuki (2026), Weil’s quadratic form via the screw function: simplicity, evenness and positivity of the bottom eigenvalue for sufficiently small windows',
 'Suzuki realises the localized Weil form through the screw function, rescales the window to a fixed interval, and gets the form as log(1/a) times the identity plus a fixed limiting form plus a small error. Kato perturbation theory then gives a simple, even, positive lowest eigenvalue for small enough windows, with no explicit threshold.',
 'arXiv:2606.09096, Thm 1.4 (checked t2252/hp2251 literature step). Not checked here: whether the closed form log P appears.',
 ['sign/positivity (Ax2)','reference/pole/cusp'],
 [R('related','suzuki_line','same author, earlier de Branges object'),R('compared_with','plastic_threshold_ccm_markov','')])
add('lit_de_andrade_silva_pole_perron_2026','suzuki_line','Cited',
 'de Andrade Silva (Zenodo, 13 Jun 2026): the pole term is the only obstruction to Perron structure; t* = 0.28119957; Perron for the pole-free part for all a; scalar Krein reduction of even-simplicity',
 'This note splits the localized Weil form into the pole term, which is rank two and splits by parity into +2|C⟩⟨C| and −2|S⟩⟨S|, and a pole-free part that is a positive jump Dirichlet form plus a potential bounded below for every window. It proves the Perron property of the pole-free part and reduces even-simplicity to a one-variable resolvent/nodal question, left open.',
 'Zenodo 10.5281/zenodo.20682833. States the sign change of −g″ at t* = 0.28119957… (2cosh(t*/2) = e^{−t*/2}/(1 − e^{−2t*})) and a ≤ t*/2; Thm (Perron, all a); Cor. (Krein: 1 + 2⟨C,(Ã − λ)⁻¹C⟩ = 0, nodal condition). Abstract and tex read (lem2253).',
 ['sign/positivity (Ax2)','reference/pole/cusp','structure/frame (Ax1)'],
 [R('refines','pole_perron_one_mode','continuum proof of the Perron mode'),R('uses','arch_levy_khintchine_sos',''),R('related','pole_plane_krein_boundary_condition','rank-one Krein reduction')])
add('lit_de_andrade_silva_loewner_2026','suzuki_line','Cited',
 'de Andrade Silva (Zenodo, 17 Jun 2026): a Loewner / operator-monotone framework for even-simplicity; the arithmetic case is the “remaining open core”',
 'The truncated Weil matrix is the divided-difference (Loewner) matrix of an odd function, and its parity sectors are Loewner matrices too. When the underlying function is operator monotone, even ordering follows; the arithmetic matrices are in a doubly critical regime, which the author leaves open.',
 'Zenodo 10.5281/zenodo.20737110 (abstract and tex read). No proof of arithmetic even-simplicity is claimed.',
 ['structure/frame (Ax1)','open target'],
 [R('extends','lit_de_andrade_silva_pole_perron_2026',''),R('related','ccm_even_simplicity_hp2251','')])
add('lit_mehennaoui_evenness_from_simplicity_2026','suzuki_line','Cited',
 'Mehennaoui (Zenodo, 17 Oct 2026): evenness from simplicity in the truncated Weil form; a windowed determinant (Hurwitz) criterion',
 'Under the reflection symmetry and a normalization, a simple lowest eigenvector of the truncated form is even. A spectral-approximation hypothesis gives simplicity for large N, and real-rooted windowed determinants converging to Ξ would give RH by Hurwitz’s theorem. Everything is conditional, as the author says.',
 'Zenodo 10.5281/zenodo.23441945. Abstract and theorem statements read (lem2253); proofs not checked.',
 ['restatement ⇔ RH','structure/frame (Ax1)'],
 [R('related','ccm_even_simplicity_hp2251',''),R('restates','weil_positivity','Hurwitz step = convergence, not sign')],
 uncertain='Proofs not checked by us.')
# ---------------- manuscript + target commentary ----------------
add('ms2253_review_verdicts','hodge_index_zeta_restatement','Restatement',
 'Review of “Nested Hyperbolae, Null Poles, and the Missing H¹” (J.W. with Claude, v2, 16 Nov 2026): one closed form, one elementary restatement, one off-by-one; nothing touches (D)',
 'The manuscript organises three days of work around the pole plane read as 1+1 Minkowski space. Checked: the closed form of the Markov threshold is right and new as a closed form; the single-null-hyperplane criterion is right but a two-line consequence of Weil; the “trivial-zero orbits” reading of the jump kernel is wrong at n = 0. Its restatement of (D) puts J on E0 with Q as the metric, the reading TARGET retired. Most dictionary rows are restatement or framing and several are prior atlas items.',
 'Verdicts: (i) log P exact (value prior: de Andrade Silva); (ii) exact restatement; (iii) n = 0 is the s = 0 pole; Half 1 = de Andrade Silva Thm + TAA L180; κ = 1 + 2# = atlas offline_point_negative_count; Rindler = pole_plane_lorentz_boost; §9.2 Gram is W not Q; §6.1 Selberg ¼ is a conjecture (3/16 proved); hp2251 paragraph accurate but needs the Galerkin caveat and the Legendre attribution. Recommendation: hold; publishable as Arithmetic Unification VIII after revisions (lem2253 REVIEW_ms2253v2.md).',
 ['restatement ⇔ RH','physics analogue','structure/frame (Ax1)'],
 [R('related','pole_plane_lorentz_boost','prior Rindler row'),R('related','offline_point_negative_count','prior κ formula'),R('related','kahler_triple_polarization','(D) misplaced on E0'),R('related','ks_polarization_dictionary','Kepler rows')],
 pitfalls=['Restating (D) with J on E0 and metric Q is the C6 error (TARGET C6/C7/C12).'])
add('d_normalization_not_offset','hodge_index_zeta_restatement','Restatement',
 'TARGET commentary (t2245, C16): (D) asks for a space where the ½ is a normalization, not an offset; Eisenstein constant terms keep ζ’s zeros half a unit off the unitary axis',
 'In the function-field case dividing Frobenius by √q puts the unitarity centre and the functional-equation centre in the same place. For GL(2) Eisenstein series the two centres differ by ½, so ζ’s zeros appear as scattering resonances, never as eigenvalues. The target’s compatibility condition says the two involutions must share a centre.',
 'Unitary axis Re ν = 0 vs zeros of c(ν) = ξ(ν)/ξ(1+ν) at Re ν = ±½ (GL(2) proved; general Langlands–Shahidi recollection). † and ∨ share a centre ⇔ (D). Commentary only; §6 frozen text unchanged.',
 ['restatement ⇔ RH','reference/pole/cusp','Spec ℤ gap'],
 [R('restates','kahler_triple_polarization','(D) as shared centre'),R('related','eisenstein_resonances_rho_half','the offset'),R('related','eisenstein_ct',''),R('uses','half_density','normalization on the test side')],
 pitfalls=['A restatement of (D), not progress on it.'])
for c in C:
    t=by[c['_template']]; c['priority']=t['priority']; c['ranking']=t['ranking']; c['rank']=None
ids=[c['id'] for c in C]; assert len(ids)==len(set(ids)) and not set(ids)&set(by)
allids=set(by)|set(ids)
for c in C:
    for r in c['rels']: assert r['to'] in allids, (c['id'],r['to'])
out=dict(base=dict(version='v1.22',concepts=len(by),relations=sum(len(c['rels']) for c in D['concepts'])),proposed='v1.23',
         added_concepts=len(C),added_relations=sum(len(c['rels']) for c in C),concepts=C)
txt=json.dumps(out,ensure_ascii=False,indent=1)
assert '\\' not in txt
(HERE/'atlas_delta_v123.json').write_text(txt+'\n',encoding='utf-8')
print(out['base'],out['added_concepts'],out['added_relations'])
