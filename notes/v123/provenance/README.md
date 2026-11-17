# lem2253: research bundle for RH Atlas v1.23

Prepared 16–17 Nov 2026 (America/Chicago). Covers t2249–t2253: the AHK/tropical question (no new atlas entry; the CC square stays genus 0, see v1.22), the CCM even-simplicity thread (Suzuki, de Andrade Silva, hp2251 high-precision run), J.W.'s manuscript "Nested Hyperbolae, Null Poles, and the Missing H¹" (v2), and TAA Lemmas 188–193.

**RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity.**

Read in this order: ../SYNTHESIS.md, AUDIT.md (binding), notes/LEMMAS_2253.md, notes/REVIEW_ms2253v2.md, notes/hp2251_REPORT.md, delta/atlas_delta_v123.json, RELEASE_NOTES_v123.md.

Reproduce: `python3 SMOKE_TEST.py` (about 30 s; needs python3 + mpmath). Full tables: `cd scripts/lem2253 && python3 lemtest.py <A> <N> <digits> [chi4]` (A = 4, N = 150, 250 digits takes about 35 s), then `summ.py` over the outputs. The hp2251 sine-basis runs: `scripts/hp2251/sine.py <A> <N> <digits>`. The Legendre-basis runs (hp.py) depend on the earlier Arb assembly and are not included; their Q ground states are quoted from hp2251_REPORT.md.
