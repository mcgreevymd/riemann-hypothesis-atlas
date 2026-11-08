# bernoulli1945 (t1945; Nov 7 2026 CST; RH not proved). b1945.py/json (sympy exact).
Recovered: Lemma 14 §22 (f) τ ≡ σ11 mod 691 (n<1200), B12 = −691/2730, Ribet ω^{−11} eigenspace; Lemma 68 §77
 (E12 vs ζ zeros, "congruent mod 691 opposite local signature").
Exact: B12 = −691/2730; ζ(−11) = −B12/12 = 691/32760 (≠ 0: odd negative integer); trivial zeros ζ(−2) = ζ(−4) = 0 come from
 Γ(s/2) poles in ξ. E12 = 1 + (65520/691)Σσ11(n)qⁿ (65520/691 = −24/B12); G12 = −B12/24 + Σσ11 qⁿ, constant 691/65520 ≡ 0
 mod 691 ⇒ G12 ≡ Δ mod 691: τ(n) ≡ σ11(n) (n ≤ 60 checked); τ(2) − σ11(2) = −24 − 2049 = −2073 = −3·691.
 Herbrand–Ribet range 2 ≤ 12 ≤ 688 satisfied; even k ≤ 688 with 691 | num B_k: k = 12, 200 (computed).
Mellin, h_s(F) = ∫F e^{(s−½)u}du, D_p = I − p^{−½}T_{log p}:
 h_s(D_pF) = (1 − p^{s−1})h_s(F), h_s(D_p*F) = (1 − p^{−s})h_s(F); D_pD_p* multiplier = −p^{s−1}(1−p^{−s})(1−p^{1−s})
 = −p^{s−1} × (weight-2 Eisenstein Hecke polynomial (1−X)(1−pX) at X = p^{−s}); on s = ½+ix it is |1−p^{−½}p^{ix}|² > 0.
 D_p kills h_s for s ∈ 1 + 2πiZ/log p; D_p* for s ∈ 2πiZ/log p; two primes share only s = 1 (resp. 0).
Precise relation (structural, no hidden equality): E0 = kernel of the two boundary characters (s=0,1) ≈ "cuspidal = constant
 terms killed"; D_p, D_p* = local Euler annihilators of those characters, same algebra as T_p − (1 + p^{k−1}) killing E_k
 (p-depletion f(q)−f(q^p) is different: it kills constant terms only). Eisenstein ideal/congruence mod 691 = cuspidal part
 meeting the boundary mod ℓ; it yields class-group elements, not a sign. The cusp side has the Petersson positive pairing;
 the analogue for E0 (a positive pairing on the boundary-killed quotient, = W ≥ 0) is exactly what is missing. Nothing
 about 691 is special for W.
