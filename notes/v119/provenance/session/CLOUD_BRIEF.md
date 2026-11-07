# Integration brief for the atlas maintainer (path-independent)
Goal: integrate the 6 Nov 2026 night synthesis into the RH atlas as one new perspective entry plus figures, without changing existing
verdicts. RH is not proved; the entry adds no claim of progress.
1. Add a front-section text from SYNTHESIS.md §0 and §3 ("The missing law — a target"). Keep the status box verbatim.
2. Add figures fig1_springs, fig2_boundary, fig3_mechanisms (SVG editable, text as text; PNG previews). Regenerate from figs/make_figs.py if data paths change (inputs: spring1891 controls/conv JSON; compat1907 check log; tests/test1_result.json).
3. Add tests/test1_boundary_defect_Fq.py and tests/test2_signature_dictionary.py with their JSON outputs; mark Test 1 EXACT (finite control), Test 2 consistency check (uses W itself; positive Galerkin minima are not certificates).
4. Apply CLAIM_AUDIT.md: items marked CORRECTED/OMITTED must not be reintroduced (notably: vacuum spectral density claim, theta sign-change generality, completed-ζ delay ratio, "Bochner trap", global orthogonal pole projection, II₁,₁ as a literal lattice, Sonin = unique DEC analogue, "only Hodge gives a sign").
5. Cross-link: v1.15 refined missing piece (H₊ four conditions) ↔ SYNTHESIS §3; Connes 1999 Thm 5 and CC21 Thm 1 ↔ Fig. 3; atlas r329 ↔ Test 2; L162 ↔ Test 1.
6. Before publishing, re-verify the textbook citations listed as "not opened" in SOURCE_MANIFEST §9.
7. Proposed next test (not run): S = {∞, 2} projection-order leakage (SYNTHESIS §5).
