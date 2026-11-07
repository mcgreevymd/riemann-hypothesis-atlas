import sympy as sp
u,a,b,s,xi,v=sp.symbols('u a b s xi v',real=True); g=sp.Function('g'); F=sp.Function('F')
T=lambda c,h: h.subs(u,u-c)                     # (T_c h)(u)=h(u-c)
Q=lambda h: u*h; D=lambda h: -sp.I*sp.diff(h,u)
G=g(u)
print('[Q,T_a]g - a T_a g =',sp.simplify(Q(T(a,G))-T(a,Q(G))-a*T(a,G)))
print('[D,T_a]g =',sp.simplify(D(T(a,G))-T(a,D(G))))
print('[Q,D]g - i g =',sp.simplify(Q(D(G))-D(Q(G))-sp.I*G))
E=lambda h: sp.exp(sp.I*s*u)*h
print('Weyl e^{isQ}T_a - e^{isa}T_a e^{isQ} =',sp.simplify(E(T(a,G))-sp.exp(sp.I*s*a)*T(a,E(G))))
M=lambda c,h: sp.exp(sp.I*c*sp.exp(u))*h          # additive character x=e^u
print('T_a M_xi T_-a - M_{xi e^-a} =',sp.simplify(T(a,M(xi,T(-a,G)))-M(xi*sp.exp(-a),G)))
# ev_s(T_a F)=e^{(s-1/2)a} ev_s(F); ev_s(DF)=i(s-1/2)ev_s(F) (by parts, compact support): integrand identities
print('T_a on ev_s: integrand shift factor',sp.simplify(sp.exp((s-sp.Rational(1,2))*(v+a))/sp.exp((s-sp.Rational(1,2))*v)))
# adjoint of O(F): <O(F)g,h> = ∫∫F(a)g(u-a)conj h(u); substitute -> O(F)* kernel conj F(-a) = F^sharp
print('O(F)*=O(F#), F#(a)=conj F(-a): standard (convolution adjoint); real F selfadjoint iff even')
