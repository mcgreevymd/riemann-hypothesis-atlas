# t2098 REPORT (scratch only, nothing pushed)
Verdict: (b), sharpened. No CC-definable O(nD) / h^1 on the square gives an n^2 term; the classical n^2 mechanism (fiber-class map into a
continuous Jacobian, Rosati sign) has no CC counterpart because Pic^0(C_p) = Z/(p-1)Z is finite [CC17 Thm 5.6].
- CC23 (arXiv:2205.01391) RR: dim H^0 - dim H^1 = ceil'((deg D+log2)/log3) - 1_L; dims are log_3-cardinality counts; additive under
  products (brute force: box dims 2,4,4,4 = 1D sums for N=1..4) => chi(n(F1+F2)) linear (4,6,10,16,32,60) vs n^2 target.
- CC17 (arXiv:1603.03191) RR on C_p: Dim_R H^0(D) - Dim_R H^0(-D) = deg D; Fr^a_mu scales degree by mu (Lemma 5.7) — honest source of
  bidegree (1,mu). But Psi(mu) Cartier only for mu in Q; distinct radial graphs disjoint (Gram off-diagonal 0, where W needs k_inf(log2)=0.943 and
  p=2 atoms); Leray fibers of primitive nD have degree 0 => Dim 0 for all n => quadratic coefficient 0.
- Classical sanity (C x C): chi(nD) = (1/2)D^2 n^2 + (1-g)^2 exactly on primitive D, D^2 = -W_ff (genus 1: -810,-18630,-89910; genus 2: -378,-4254);
  genus 1: h^1(nD) = deg(n psi) = n^2 * 405 etc. = (W/2) n^2. The sign there is Rosati positivity = closed Jacobian route.
- Dreamer corrections: h^2(nD)=h^0(K-nD) needs H' = D + mH (Hartshorne V.1.8-9) unless K=0; non-effectivity vacuous when principal divisors are too few.
Files: notes2098.md, ccrr2098.py, ccrr2098.json, cc2205.pdf/.txt, cc1603.pdf/.txt.
