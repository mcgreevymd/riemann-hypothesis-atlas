# bernoulli1946 (t1946; Nov 7 2026 CST; RH not proved). b1946.py/json (sympy exact).
Normalization: G_k = −B_k/(2k) + Σσ_{k−1}(n)qⁿ = ζ(1−k)/2 + …. Primes p | num(B_k) with p | k CANCEL (k=10: 5; 14: 7; 22: 11;
 26: 13; 28: 7; 30: 5); these are never Eisenstein-congruence primes (B_k/k is p-integral; Kummer: B10/10 ≡ B2/2 ≡ 3 mod 5).
 num(G_k const) = 1 exactly for k = 4,6,8,10,14 = weights with S_k(SL2Z) = 0 (k ≤ 32 table); nonunit numerators
 (691@12, 3617@16, 43867@18, 283·617@20, 131·593@22, …) occur only where cusp forms exist ⇒ cusp form ≡ Eisenstein.
 Herbrand–Ribet needs 2 ≤ k ≤ ℓ−3: 5 | B10 is outside (10 > 2); 5 is regular.
Signature (Hirzebruch): x/tanh x = 1 + x²/3 − x⁴/45 + 2x⁶/945 − x⁸/4725 + 2x¹⁰/93555 (= Σ 2^{2j}B_{2j}x^{2j}/(2j)!);
 top coefficient of L_j: s_j = 2^{2j}(2^{2j−1}−1)|B_{2j}|/(2j)! = 1/3, 7/45, 62/945, 127/4725, 146/13365 (j=5, dim 20, B10).
 Kervaire–Milnor |bP_{4k}| = 2^{2k−2}(2^{2k−1}−1)·num(4B_{2k}/k): 28, 992, 8128, 261632 (k=5: 4B10/5 = 2/33, the 5
 cancels again), 1448424448 — matches https://en.wikipedia.org/wiki/Exotic_sphere table (bP_20 = 261632; Θ19 = 523264).
 (My first script used an extra a_k factor: wrong for odd k; corrected.)
 Signature is an index (n₊ − n₋) computed from Bernoulli numbers; positivity of a form is a separate input (Hodge index/HR:
 σ = Σ(−1)^p h^{p,q} on Kähler, needs the polarization). Bernoulli numbers count, they do not sign.
Arch link (exact, checked): Binet ψ(z) = log z − 1/(2z) − 2∫₀^∞ t dt/((t²+z²)(e^{2πt}−1)), Re z>0, at z = ¼ + ix/2 (x=0,3,10
 to 12 digits); Stirling series ψ ~ log z − 1/(2z) − ΣB_{2j}/(2j z^{2j}) enveloping on the real axis. ψ(¼) = −γ − π/2 − 3log2,
 so K0 = −γ − π/2 − 3log2 − log π. Use: validated tail bounds for Ω in window certificates; no sign for W.
