# Sources for the v1.19 integration

The 6 Nov 2026 session opened the items in §1–§4 and recorded equation-level readings. This integration uses those readings where they agree with the atlas, and it qualifies anything that was not re-opened. RH is not proved.

## 1. Opened in the session, and already carried by the atlas

1. A. Connes, “Trace formula in noncommutative geometry and the zeros of the Riemann zeta function,” Selecta Mathematica (N.S.) 5 (1999) 29–106. Atlas entry `connes_trace`: the global trace formula is equivalent to RH; Theorem 5 is the characteristic-p statement. This integration keeps that distinction. Projection order in characteristic p is a theorem there. It is not the number-field result. Subtraction of the pole contribution is not, by itself, a positivity proof.
2. A. Connes and C. Consani, “Weil positivity and trace formula, the archimedean place,” Selecta Mathematica 27 (2021), arXiv:2006.13771. Atlas entry `cc21_archimedean_positivity`: Theorem 1, small support, vanishing conditions. Lemma 3.3 and Proposition 3.5 are the prior L-bijection and the transport of positivity onto E0. Not re-proved here.
3. A. Connes, C. Consani, and H. Moscovici, “Zeta zeros and prolate wave operators,” arXiv:2310.18423. The semilocal Sonin space is a cited construction. The inequality that would compare it with the Weil form is open in the atlas (`needed_semilocal_sonin_inequality`). It is one candidate, not a unique energy condition.
4. C. Deninger, “Some analogies between number theory and dynamical systems on foliated spaces,” Documenta Mathematica, Extra Volume ICM 1998, Vol. I, 163–186. Atlas entry `deninger`: a positive leafwise star commuting with the flow would force the critical line; the star is conjectural.

## 2. Session readings not re-opened here

Tate’s thesis is used through the atlas entry `xi_global_product_over_places` and through the elementary boundary identities re-checked in `notes/v119/tests/audit_v119.py` (Fourier swap, scaling, invariant form). Poonen’s notes and Garrett’s notes were opened in the session. This integration does not add a claim that depends on a page of those notes beyond the identities re-checked.

Faltings, “Calculus on arithmetic surfaces,” Annals of Mathematics 119 (1984) 387–424, and Hriljac, American Journal of Mathematics 107 (1985) 23–38, are the literature behind the atlas entry `faltings_hriljac_statement`. The session consulted them at statement level. No finer claim is added.

Aitchison, MacManus, and Snyder, American Journal of Physics 72 (2004) 1370, is the session’s reading of Heisenberg’s 1925 termination condition: the sign is a Hilbert-space norm. Not re-opened here. Not a construction for W.

## 3. Textbook and journal background — verified at citation level, not re-proved

These were listed as “not opened” in the session manifest. Citation details below were checked against public bibliographic records for this integration. The mathematical use is the standard one already in the atlas, or an elementary identity re-checked in the audit script. Nothing here is a new proof of those theorems.

- Mattuck and Tate, “On the inequality of Castelnuovo–Severi,” Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 22 (1958) 295. Grothendieck, “Sur une note de Mattuck–Tate,” Journal für die reine und angewandte Mathematik 200 (1958) 208–215. Grothendieck’s opening paragraph, in the public transcription of that note, says Mattuck–Tate deduce Weil’s Riemann hypothesis for function fields from the Riemann–Roch theorem on the surface. The atlas states the same sign as the Hodge index on the Néron–Severi space of C×C, and TAA Lemma 162 records the E×E Gram. This integration re-checks that Gram’s inertia. It does not re-prove the surface theorem.
- Goddard and Thorn, “Compatibility of the dual Pomeron with unitarity and the absence of ghosts in the dual resonance model,” Physics Letters B 40 (1972) 235–238. Brower, “Spectrum-generating algebra and no-ghost theorem for the dual model,” Physical Review D 6 (1972) 1655–1662. The theorem transports positivity from a positive transverse space. The session’s h = −1, c = 26 calculation is an elementary Gram identity (re-checked in the audit script), not that theorem. Central charge, a speed, and a topological charge are different quantities.
- Witten, “A new proof of the positive energy theorem,” Communications in Mathematical Physics 80 (1981) 381. Standard name for the positive-energy theorem. The session’s point, kept here only as an analogy, is that the spinor supplies a square and the sign also uses an energy condition, existence, and asymptotics. The paper was not re-opened for this integration; no equation number is claimed from it.
- Unitarity of Virasoro representations is literature (the Kac determinant; Friedan, Qiu, and Shenker, Physical Review Letters 52 (1984) 1575). Not re-proved here. The audit script checks only the level-2 norm at h = −1.
- Rodgers and Tao, arXiv:1801.05914, Λ ≥ 0 for the de Bruijn–Newman constant. Already cited in the atlas. Not used as a new input.

## 4. Atlas entries this integration cross-links

`kahler_triple_polarization` (rank 1), `no_ghost_missing_piece` (v1.15, four construction criteria, with the correction that the norm identity alone is the equivalence and the four criteria are not automatic), `pole_plane_hyperbolic_complement_positive` (the free-basis one-negative direction), `hodge_index` and TAA Lemma 162, `connes_trace`, `cc21_archimedean_positivity`, `deninger`, `weil_positivity`, `levy_khintchine_mass_gap`, `arch_levy_khintchine_sos`, `weil_kernel_is_levy_measure`, `margins_force_identity`, `archimedean_weyl_kernel`, `needed_semilocal_sonin_inequality`, `ii11_pole_pair`, `einstein_cartan_torsion_spin`.

## 5. Scripts

Runnable copies with repository-relative paths:

- `notes/v119/tests/audit_v119.py`
- `notes/v119/tests/test2_signature_dictionary.py` (imports the archived `spring_mp.py`)
- `notes/v119/provenance/session/tests/test1_boundary_defect_Fq.py`
- `notes/v119/provenance/session/tests/appendix_quadratic_checks.py`
- `figures/v119/make_figs.py`

Session scripts under `provenance/session/notes/` were re-run for the algebra checks. Their prose is superseded. See `provenance/SUPERSEDED.md`.
