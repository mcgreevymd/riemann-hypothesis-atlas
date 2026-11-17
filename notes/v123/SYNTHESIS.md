# v1.23 synthesis (t2249–t2253, 14–17 Nov 2026, America/Chicago)

**RH is not proved. Φ is not constructed. No Hodge-type sign. Nothing here touches (D).**

1. **Where this thread sits.** The CCM programme needs the lowest eigenvalue of the truncated Weil form QW to be simple with an even eigenvector. That is a statement about the approximants. It would not produce Φ, ω, J, or the commutation (D). It was pursued because the rank-one/Krein picture of the pole plane (v1.22) applies to it directly.
2. **Markov half.** The pole-free form Q is a jump Dirichlet form (kernel J = k∞ > 0, prime jumps Λ(n)/√n) plus a potential bounded below. So its ground state is Perron on every window. This is de Andrade Silva's theorem (June 2026), with TAA L180 as the earlier numerical form. The poles add 2cosh(w/2) off the diagonal; the full form stays Markov exactly up to A = log P (L188, plastic number).
3. **Beyond log P.** The parity split (de Andrade Silva) gives Q + 2|c⟩⟨c| on even functions and Q − 2|s⟩⟨s| on odd ones. Even-simplicity is then a secular-function sign (L191). High-precision Galerkin runs (hp2251, lem2253) find it true for A ≤ 6 with a margin of 10²–10⁴ in eigenvalue ratio. There is no proof beyond log P.
4. **Control.** L(s, χ₄) has no poles. It is Markov to log 3 and numerically shows the same even-below-odd pattern through A = 4 (L193). So the pattern is not a pole effect, which is consistent with the N-L necessary condition.
5. **Manuscript.** See REVIEW_ms2253v2.md. Its single-null-hyperplane criterion is exact and elementary (L189). Its Hilbert-transform question is answered negatively (L192). Its trivial-zero reading is corrected at n = 0 (L190).
6. **Target.** No TARGET edits. The proposed rows (closed-route annotations, a CCM diagnostic line, change-log C17) await J.W.'s OK. The t2245 commentary on (D) is carried as the restatement concept `d_normalization_not_offset`.
