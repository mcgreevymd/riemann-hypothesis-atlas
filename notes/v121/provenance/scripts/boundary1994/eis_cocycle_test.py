import sympy as sp
X=sp.symbols('X'); w=10; pi=sp.pi
def act(P,g):
    (a,b),(c,d)=g
    return sp.expand(sp.cancel((c*X+d)**w*sp.sympify(P).subs(X,(a*X+b)/(c*X+d))))
S=[[0,-1],[1,0]]; U=[[1,-1],[1,0]]; U2=[[0,-1],[1,-1]]
def r(n): return sp.nsimplify(sp.simplify((2*pi)**(-(n+1))*sp.factorial(n)*sp.zeta(n+1)*sp.zeta(n-10)))
rodd=sp.expand(sum(sp.binomial(w,n)*(-1)**n*sp.I**(n+1)*r(n)*X**(w-n) for n in range(1,w,2)))
print('odd Eisenstein period (exact rational):',rodd)
c=sp.symbols('c')
phiS=rodd; phiT=c*sp.expand((X+1)**11-X**11)
phiU=sp.expand(act(phiT,S)+phiS)
eqs=sp.Poly(sp.expand(phiS+act(phiS,S)),X).coeffs()+sp.Poly(sp.expand(phiU+act(phiU,U)+act(phiU,U2)),X).coeffs()
print(sp.solve(eqs,c))
