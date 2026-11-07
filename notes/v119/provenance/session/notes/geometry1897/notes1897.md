# geometry1897 — what geometry produces the sign of the Weil pairing (t1897, brainstorm)
Read-only. RH not proved. Labels: [EXACT-SRC] source theorem, [EXACT-TOY] verified here, [CONJ] candidate, [ANALOGY].

## Sources checked
- Deninger, "Some analogies between number theory and dynamical systems on foliated spaces", Doc. Math. Extra Vol. ICM 1998 I, 163-186, https://emis.de/ft/10155 (pp.168-169: positive Hodge * commuting with flow ⇒ Θ=1/2+A, A skew; p.~170: ψ^t* = e^t*ψ^t "flow changes the metric defining * by the conformal factor e^t"; p.180: Álvarez López–Kordyukov leafwise Hodge theorem gives * from leaf metrics for Riemannian foliations).
- Connes–Consani, "Weil positivity and trace formula, the archimedean place", arXiv:2006.13771 (Thm 1 Sonin positivity; Lemma 3 / Prop 5 = our L/Q0 construction -> PRIOR ART for paired1888).
- Connes–Consani, "The scaling site", arXiv:1507.05818 (periodic orbits C_p = R+*/p^Z, RR with real dimensions).
- Rodgers–Tao, de Bruijn–Newman constant is non-negative, arXiv:1801.05914 (Λ ≥ 0).

## Toy check star1897.py
(a) V=R^6, ω=cup, Θ conformal-symplectic (ω(Θx,y)+ω(x,Θy)=ω(x,y)) and [Θ,J]=0, J compatible: Θ+Θ^T=I, Re spec = 1/2 exactly.
(b) ghost Θ=diag(β,1−β): conformal-symplectic ✓ (FE-level law holds), commutant = diagonals, J²=−1 has only imaginary solutions -> no positive *;
    but an invariant Krein form h=[[0,1],[1,0]] exists. => sign comes from POSITIVITY of the polarization, not from invariance/compatibility.

## Ranked ideas
1 [EXACT-TOY/CONJ] Conformal polarization: positive * on H^1 with ψ^t scaling the metric by e^t. Observation: e^t is exactly the Haar module |λ| of scaling on A_Q (product formula makes it Q*-invariant) – but Haar is a measure not a metric (atlas r185), compact manifolds can't do it (r157).
   Task: on the adele class space / CC scaling site, find a leafwise Hermitian structure (not only density) whose scaling factor equals the module; test on the solenoid quotient whether the induced form on a finite window space is positive and reproduces W_L.
2 [EXACT-SRC/CONJ] Trace-of-positive-operator by compression (CC Sonin): W_∞(g*g*) ≥ Tr(ϑ(g)Sϑ(g)*) ≥ 0 for supp g ⊂[2^-1/2,2^1/2], ĝ(i/2)=ĝ(0)=0. Same form as Deninger's Tr(ψ(f)ψ(f)^†) with † from *.
   Task: semi-local S={∞,2}, support up to log 4: compute the compression remainder; falsified if remainder sign fails on explicit windows.
3 [EXACT-SRC F_q / CONJ Q] Hodge index on a square: F_q via ample class (D²−2d1d2=−2AB, needs b=ā). Over Q missing theorem: quadratic RR + Hodge index on (scaling site)² with intersection defined independently of the explicit formula.
   Task: q→1 limit of Castelnuovo on C_p×C_p as a LIMIT (not equating continuous Mellin with discrete Frobenius samples); falsified if limit form is indefinite on E0.
4 [ANALOGY] Chambers: local elliptic/Krein chambers are definable; global chamber = component of FE-compatible deformations containing a positive anchor with no signature collision. ζ lies on the de Bruijn–Newman wall (Λ ≥ 0), so any argument must be non-perturbative.
   Task: path from G0 / Sonin functional to W on windows; track inertia + Krein signature; falsified if ghost and ζ are indistinguishable by every invariant.
5 [ANALOGY, low] Reflection positivity / A†A: only via 2; OS as stated fails (r175).

## Dictionary
cup/ω ↔ intersection ↔ trace pairing B; Θ|H²=1 ↔ pole/weight ↔ pole term P; * (=J on H¹) ↔ Rosati/ample ↔ missing; g=tr(f∪*f') ↔ Hodge index ↔ W on E0; ψ^t ↔ Frobenius graphs Γ_{F^n} ↔ scaling T_b; conformal factor e^t ↔ q^{n} ↔ Haar module |λ|; periodic orbits ↔ closed points ↔ primes (length log p).
g/J/ω arises after primitive polarization: ω=cup, J=*, g=ω(·,J·). Ample (algebraic integral class, Hodge index) ≠ analytic positive metric (leafwise Hodge *); Deninger needs only the latter + conformality.
