Provenance for v1.24.

Read in this order:
1. ../SYNTHESIS.md
2. AUDIT.md (binding)
3. notes/LEMMA_194.md, notes/LEMMA_195_draft.md (with REPORT_195_t2273.md), notes/LEMMA_196.md (with REPORT_196.md), notes/LEMMA_197.md (with REPORT_197.md)
4. notes/FILTER_2271_SORT.md
5. notes/CHECKS_t2271_2286.md
6. delta/atlas_delta_v124.json
7. RELEASE_NOTES_v124.md

Reproduce:
- `python3 SMOKE_TEST.py` takes about 20 s and needs python3 with numpy and scipy.
- L197, from `scripts/lem197/`:
  - `python3 l197.py 0.025` and `python3 l197.py 0.05` take a few seconds each.
  - `python3 extra197.py` and `python3 conv196.py` take about 30 s.
  - The included `l149_small/` holds the ledger's L149 Toeplitz rows and the Λ and DH coefficient tables, truncated to n ≤ 6000 (enough for r ≤ 8).
- L196, from `scripts/lem196/`: census_curves.py, ladder.py 3 5 7 11 13, summarize.py, window.py, window_run.py, extras.py, rankcheck.py. These need mpmath and take about 10 min.
  - The 41 MB raw ladder output, the mpmath fallback cache and the large run files are not redistributed. `data/lem196/` keeps curves.json, ladder_table.json, rankcheck.json and window.json.
- The L194 and L195 scripts depend on the ledger's high-precision assembly and are not included. Their tables are quoted in the notes.
