"""Appendix checks for the 'common quadratic geometry' bridge (t1917). Exact sympy."""
import sympy as sp
# Clifford c(v)c(w)+c(w)c(v)=2g(v,w) exists for INDEFINITE g: Cl(1,1) by real 2x2 matrices
e1=sp.Matrix([[0,1],[1,0]]); e2=sp.Matrix([[0,1],[-1,0]])
g=sp.diag(1,-1); E=[e1,e2]
print('Cl(1,1):',all((E[i]*E[j]+E[j]*E[i])==2*g[i,j]*sp.eye(2) for i in range(2) for j in range(2)))
# Dirac square in flat R^2: D = e1 dx + e2' dy with Euclidean Clifford => D^2 = Laplacian (positivity from metric)
f=sp.Function('f'); x,y=sp.symbols('x y'); s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-sp.I],[sp.I,0]])
F=sp.Matrix([f(x,y),0]); D=lambda V: s1*V.diff(x)+s2*V.diff(y)
print('D^2 = Delta (Euclidean):',sp.simplify(D(D(F))-(F.diff(x,2)+F.diff(y,2)))==sp.zeros(2,1))
# Discriminant/determinant is not positivity: same det, opposite definiteness; principal minors decide
for M in [sp.diag(1,1),sp.diag(-1,-1),sp.Matrix([[-2,-1],[-1,-10]])]:
    print(list(M), 'det',M.det(),' leading minors',[M[:k,:k].det() for k in (1,2)])
