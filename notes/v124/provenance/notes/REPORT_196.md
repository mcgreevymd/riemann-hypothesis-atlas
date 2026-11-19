# REPORT: Lemma 196 (G1 function-field anatomy), 18 Nov 2026, approx. 22:20–22:55 CST

- **Authorization:** J.W. pt2283u, "Yes run it here".
- **Scope:** scratch only, lem196/. STATE.md, TARGET.md, atlas and push were not touched. **RH is not proved.**
- **Files:** LEMMA_196.md (statements 196.0–196.7 with tags and tests), and the scripts census_curves.py, ladder.py, summarize.py, window.py, window_run.py, extras.py, rankcheck.py, which write out/*.json.

## Headline
Over F_q (genus 2, q = 3, 5, 7, 11, 13), every count-level condition leaves off-circle fakes:
- FE + integrality;
- N_n ≥ 0;
- a genuine Euler product with a_d ≥ 0 for all d (certified, not truncated);
- hyperelliptic-twist positivity;
- Jacobian group orders.

Survivors: 12 / 172 / 586 / 2555 / 4322. The first rung that kills all of them is Hodge index on C×C at depth n ≤ N*(q) = 4/5/7/9/12. For all n this is RH(C) itself, and its content is the existence of Γ_{F^n} as effective curves on a projective surface (T-D2). No new mechanism appears.

## New exact pieces
1. **Box completeness:** N_n ≥ 0 for all n ⇒ |α| ≤ q.
2. **The L166 census is reproduced to the unit and certified for all d.**
3. **Finite-rank window theorem:** W(c) = Σ_j ĉ(β_j)ĉ(1/β_j) and P = 2ĉ(√q)ĉ(1/√q). So the pole plane is an off-circle FE pair of multiplicity −1. n−(W) = #{|β| > 1}, n−(Q) = n−(W)+1, and onset L* ≤ 2g−1 regardless of δ.
4. **Positivity needs the FE:** removing one closed point keeps W > 0 on every window even though purity fails.
5. **No robust degree localization:** degree-2 enrichment is ×1.76–2.04, which sits at §351's 2× threshold.

## Ledger check
- **No errors found.** L166's numbers (675/2935/4961 off, 205/401/513 on) are confirmed exactly.
- **Notational caveat:** TARGET §2 Prop. 1's "Q_ff" is L194's W (= Q+P) on all c, and equals Q only on E₀.
- **Upgrades:** L194(d) dictionary rows are now exact (196.0). L194(e)7's Perron property has an exact F_q twin: Q's off-diagonal kernel −q^{min}N_m ≤ 0 ⇔ rung (iii).

## Suggested next steps (not run)
- Genus-3 version, where L166 found off-circle pencils, to test N*(q,g) growth.
- A Rück/Honda–Tate filter on the on-circle non-Jacobians.
- §351 on the ℚ side, now with the F_q baseline that Euler × FE separates nothing.
