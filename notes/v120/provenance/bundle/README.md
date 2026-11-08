# atlas1987 research bundle (Nov 7 2026 CST). RH is not proved. Start with SYNTHESIS.md, then AUDIT.md (binding).
Smoke test (run from bundle root): python3 SMOKE_TEST.py   (exact sympy checks + kink check; ~10 s). Long/interrupted scripts NOT run by smoke test:
jointmatrix1944/scan1944.py (long LP scan), eisenstein1954/fam1954.py numerical part (interrupted; use fam1954_exact.py), moment1975/lower1975.py (Nyström, minutes).
Scripts write outputs to their CWD; run copies in a scratch dir to keep archived data pristine.
