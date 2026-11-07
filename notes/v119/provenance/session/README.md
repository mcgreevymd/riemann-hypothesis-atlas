# night1916 research bundle (6 Nov 2026, CST). RH is not proved.
Read in order: SYNTHESIS.md → figs/*.png → CLAIM_AUDIT.md → SOURCE_MANIFEST.md. Reusable prompt: OVERVIEW_PROMPT.md. Integrator: CLOUD_BRIEF.md.
tests/: test1 (exact F_q split), test2 (signature dictionary, Galerkin), appendix_quadratic_checks.py. src/: run logs (reproductions, compat1907 rerun).
notes/: original session folders. They are working notes and contain statements later superseded; CLAIM_AUDIT.md governs.
Reproduce: python3 tests/test1_boundary_defect_Fq.py; python3 tests/test2_signature_dictionary.py (needs notes/spring1891 on sys.path; ~1 min); python3 figs/make_figs.py (run inside figs/, expects ../../spring1891 and ../src, ../tests).
