import sympy as sp
x=sp.symbols('x',real=True); W=sp.Function('W')(x); f=sp.Function('f')(x)
A=lambda g: sp.diff(g,x)+sp.diff(W,x)*g; Ad=lambda g: -sp.diff(g,x)+sp.diff(W,x)*g
H1=-sp.diff(f,x,2)+(sp.diff(W,x)**2-sp.diff(W,x,2))*f
print('(1) A†A f = (-d²+W\'²-W\'\') f :',sp.simplify(Ad(A(f))-H1)==0)
# (2) central-charge bound: {Q_a,Q_b^†} = 2(H δ_ab + (Z σ)_ab) with Z real, Q 2-comp; positivity of 2x2 ⇒ H>=|Z|
Hs,Z=sp.symbols('H Z',real=True); Mx=2*sp.Matrix([[Hs,Z],[Z,Hs]])
print('(2) eig of {Q,Q†} block:',Mx.eigenvals(),' ⇒ H ≥ |Z|; BPS (H=|Z|) iff one combination Q_- annihilates')
# (3) transverse-square: light-cone N = Σ_i Σ_n α_{-n}^i α_n^i ; norm of α_{-1}^μ|0> = η^{μμ}
eta=sp.diag(-1,*([1]*3)); print('(3) covariant level-1 norms (D=4 toy):',list(eta.diagonal()),' transverse (i=1..D-2) all +1')
