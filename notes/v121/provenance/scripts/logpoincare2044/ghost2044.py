import sympy as s,mpmath as m,json
m.mp.dps=40
u,b=s.symbols('u b',real=True);G=(1-u*u)**4;F=s.expand(s.diff(G,u,2)-G/4)
c=s.lambdify(b,s.integrate(s.expand(F*F.subs(u,u-b)),(u,b-1,1)),'mpmath');N=c(0)
k=lambda a:m.exp(-a/2)/(1-m.exp(-2*a))
J=m.quad(lambda a:k(a)*(2*N-2*c(a)),[0,.25,.5,1,1.5,2])+2*N*m.quad(k,[2,m.inf])
K0=m.digamma(m.mpf(1)/4)-m.log(m.pi)
atoms=[(n,m.log(next(iter(s.factorint(n))))/m.sqrt(n)) for n in range(2,8) if len(s.factorint(n))==1]
W=K0*N+J-2*sum(a*c(m.log(n)) for n,a in atoms)
D=2*m.log(2)/m.sqrt(2)*c(m.log(2))
out={'A':2,'Cplus_exact':str(s.integrate(F*s.exp(u/2),(u,-1,1))),'Cminus_exact':str(s.integrate(F*s.exp(-u/2),(u,-1,1))),'W_original_over_norm':str(W/N),'W_drop2_over_norm':str((W+D)/N),'status':'quadrature, not interval-certified; fixed trial upper bounds, not lower certificates'}
print(json.dumps(out,indent=2));json.dump(out,open('../logpoincare2044/ghost2044.json','w'),indent=2)
