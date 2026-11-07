# deform1894 — deformation tangent = E0, trace pairing, positivity source (scratch; RH is not proved)
J. W. McGreevy; work by Grok Bot. Read-only atlas/STATE/lemmas. verify1894.py.
Conventions: log line F(u)=e^{u/2}f(e^u) ⇒ ev_s(F)=∫F e^{(s−½)u}du = CC f̂(s) (L187 l.41), F^♯(u)=conj F(−u) = L187 f^♯.
A (THM, analytic): ev_s multiplicative on (E,*); E0=ker ev_0∩ker ev_1 ideal, ♯-stable (ev_s(F^♯)=conj ev_{1−s̄}F);
 0→E —L→E —(ev_0,ev_1)→R²→0, ev_s(LF)=s(s−1)ev_s(F) (sympy) ⇒ E0 = (δ''−¼δ)*E free rank 1.
 Dual numbers: δ+εF polar-normalized (ev_0=ev_1=1) ⇔ F∈E0: E0 = tangent at δ of polar-normalized convolution units; unobstructed (commutative; exp).
 Translations δ_a: (ev_0,ev_1)=(e^{−a/2},e^{a/2}) boost on E/E0 (= NOTATION Lemma 15), act on E0 by convolution.
A (THM): B(F,G)=τ(F*G^♯), τ = Weil distribution (pole+Γ+primes) = L17/L187 S. Laws: B(k*F,G)=B(F,k^♯*G); FE ⇔ B Hermitian;
 F∈E0 ⇒ pole part of B(F,·) = 0; B(LF,LG)=τ(L²*F*G^♯). Laws hold for DH too (r246 negatives) ⇒ do not imply positivity.
C (THM, F_q, = r151/r445): D_F=Σ F(n log q) q^{−n/2}Γ_{F^n}; (D·v,D·h)=(ev_0,ev_1); D²−2d1d2 = −2AB (sympy, any a,b with ab=q).
 Positivity needs b=ā (Hodge index/Rosati). Genuine a=1±2i: max D² on degree-0 −0.044 (<0); real ghost (3,5/3): +1.72.
Ranking: C (both tasks literal over F_q; Q needs surface+quadratic RR, r14/r229/r230/r997/r1011) > A (exact interface) > B (TW: counting/flat, r798; no real sign).
