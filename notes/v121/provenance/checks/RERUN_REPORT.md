# Rerun report (reproducibility)

Full rerun finished 8 Nov 2026 at about 10:20 PM CST (America/Chicago) on a shared, loaded machine.
Command: `OPENBLAS_NUM_THREADS=1 python3 rerun_all.py`. The harness also sets OMP_NUM_THREADS and MKL_NUM_THREADS to 1.

## Method
- The harness rebuilds every source directory in a scratch tree from `scripts/<dir>/` plus the archived inputs `data/<dir>_*.json`. The scripts use sibling-relative paths.
- It runs each script. An output that is not rewritten during the run is flagged `NOT REGENERATED`.
- For each regenerated JSON it records two things:
  - the maximum relative difference over all numeric fields;
  - exact equality of the non-numeric string fields. These hold the interval enclosures of the certificates.

## Skipped
Two long 2048-cell scans were not re-run: `inertia2057.py` and `scan2057.py`. Their outputs are archived, and `check2057.py` re-verifies 117 of their rows.

## Summary
- **47 script runs (48 JSON comparisons). All exit 0, and none was flagged as not regenerated.**
- 1553 numeric fields and 264 string/interval fields were compared.
- Every non-time field is identical, with two exceptions:
  - `osc2006` differs at 2.7e−14 (rounding);
  - `ma_explicit1990`: the archived JSON came from a 3000-zero run, while the archived script uses 400 zeros. All zero-free fields match. Zero tables are diagnostic only.
- All certificate scripts pass their internal assertions (`all_assertions_passed: true`): `certify2044`, `certify2047`, `certify_two2047`, `certify_inertia2057` and `check2057`. Their interval enclosures reproduce verbatim.

## Certificate timings
| script | seconds | note |
|---|---|---|
| certify2044 | 0.1 | |
| certify2047 | 5.9 | archived run took 5.2 s |
| certify_two2047 | 89.3 | |
| certify_inertia2057 | 102.7 | writes both the A = 1 and the A = 1.1 index certificates |
| check2057 | 6.9 | |

## Per-script results
| dir | script → json | exit | s | numbers | max rel diff | strings equal | note |
|---|---|---|---|---|---|---|---|
| matching1989 | ff1989.py → ff1989.json | 0 | 0.1 | 21 | 0 | 0 |  |
| matching1989 | inertia1989.py → inertia1989.json | 0 | 13.4 | 84 | 0 | 0 |  |
| matching1989 | e0tol1989.py → e0tol1989.json | 0 | 7.4 | 18 | 0 | 0 |  |
| matching1989 | nyq1989.py → nyq1989.json | 0 | 7.4 | 48 | 0 | 0 |  |
| eisenstein1990 | analytic1990.py → analytic1990.json | 0 | 0.7 | 26 | 0 | 0 |  |
| eisenstein1990 | ma_explicit1990.py → ma_explicit1990.json | 0 | 0.3 | 31 | 0.87 | 1 | archived JSON from a 3000-zero run (see above) |
| eisenstein1990 | eis1990.py → eis1990.json | 0 | 25.8 | 255 | 0 | 44 |  |
| hodge1991 | m12_lattice1991.py → m12_lattice1991.json | 0 | 0.4 | 13 | 0 | 1 |  |
| hodge1991 | periods1991.py → periods1991.json | 0 | 1.2 | 56 | 0 | 3 |  |
| hodge1991 | conic1991.py → conic1991.json | 0 | 0.4 | 9 | 0 | 8 |  |
| boundary1994 | boundary1994.py → boundary1994.json | 0 | 2.6 | 28 | 0 | 42 |  |
| boundary1994 | duality1994.py → duality1994.json | 0 | 2.4 | 18 | 0 | 14 |  |
| counterterm1995 | connes_arch1995.py → connes_arch1995.json | 0 | 217.3 | 12 | 0 | 0 |  |
| counterterm1995 | connes_arch_fft1995.py → connes_arch_fft1995.json | 0 | 2.5 | 12 | 0 | 0 |  |
| counterterm1995 | det_scale1995.py → det_scale1995.json | 0 | 0.1 | 18 | 0 | 0 |  |
| counterterm1995 | maass1995.py → maass1995.json | 0 | 421.2 | 49 | 0 | 0 |  |
| parabolic1998 | conic1998.py → conic1998.json | 0 | 0.8 | 10 | 0 | 35 |  |
| parabolic1998 | pencilW1998.py → pencilW1998.json | 0 | 7.1 | 48 | 0 | 0 |  |
| parabolic1998 | anchor1998.py → anchor1998.json | 0 | 0.3 | 10 | 0 | 2 |  |
| parabolic1998 | hess1998.py → hess1998.json | 0 | 0.1 | 15 | 0 | 0 |  |
| effectivity2001 | relrr2001.py → relrr2001.json | 0 | 0.4 | 5 | 0 | 14 |  |
| effectivity2001 | arith2001.py → arith2001.json | 0 | 0.3 | 50 | 0 | 2 |  |
| effectivity2001 | p1asym2001.py → p1asym2001.json | 0 | 0.0 | 4 | 0 | 0 |  |
| effectivity2001 | selfdual2001.py → selfdual2001.json | 0 | 0.1 | 24 | 0 | 0 |  |
| intersection2002 | tor2002.py → tor2002.json | 0 | 0.3 | 56 | 0 | 3 |  |
| intersection2002 | hecke2002.py → hecke2002.json | 0 | 0.3 | 109 | 0 | 8 |  |
| intersection2002 | lefschetz2002.py → lefschetz2002.json | 0 | 0.1 | 32 | 0 | 4 |  |
| diagonal2003 | arak2003.py → arak2003.json | 0 | 0.0 | 27 | 0 | 0 |  |
| diagonal2003 | spin2004.py → spin2004.json | 0 | 0.4 | 51 | 0 | 6 |  |
| geometry2006 | osc2006.py → osc2006.json | 0 | 0.8 | 27 | 2.7e-14 | 4 | rounding |
| sos2010 | ident2010.py → ident2010.json | 0 | 5.6 | 14 | 0 | 3 |  |
| sos2010 | unconstrained2010.py → unconstrained2010.json | 0 | 1.8 | 12 | 0 | 0 |  |
| sos2010 | buckling2010.py → buckling2010.json | 0 | 0.5 | 40 | 0 | 8 |  |
| polarity2021 | check2021.py → check2021.json | 0 | 0.6 | 9 | 0 | 2 |  |
| poincare2024 | check2024.py → check2024.json | 0 | 0.5 | 51 | 0 | 1 |  |
| modular2026 | check2026.py → check2026.json | 0 | 0.9 | 7 | 0 | 2 |  |
| realization2033 | check2033.py → check2033.json | 0 | 0.5 | 4 | 0 | 4 |  |
| blocks2038 | check2038.py → check2038.json | 0 | 0.2 | 46 | 0 | 0 |  |
| kms2040 | check2040.py → check2040.json | 0 | 0.3 | 16 | 0 | 20 |  |
| logpoincare2044 | certify2044.py → certify2044.json | 0 | 0.1 | 2 | 0 | 13 |  |
| logpoincare2044 | ghost2044.py → ghost2044.json | 0 | 0.9 | 5 | 0 | 1 |  |
| logpoincare2044 | buckling_edge2044.py → buckling_edge2044.json | 0 | 0.1 | 73 | 0 | 0 |  |
| multiprime2047 | certify2047.py → certify2047.json | 0 | 5.9 | 17 | 0.062 | 6 | only wall-clock time differs |
| multiprime2047 | certify_two2047.py → certify_two2047.json | 0 | 89.3 | 24 | 0.016 | 8 | only wall-clock time differs |
| multiprime2047 | ghost2047.py → ghost2047.json | 0 | 1.0 | 5 | 0 | 1 |  |
| inertia2057 | certify_inertia2057.py → certify_inertia2057.json | 0 | 102.7 | 29 | 0 | 2 |  |
| inertia2057 | certify_inertia2057.py → certify_two_inertia2057.json | 0 | 102.7 | 29 | 0 | 2 |  |
| inertia2057 | check2057.py → check2057.json | 0 | 6.9 | 4 | 0 | 0 |  |
