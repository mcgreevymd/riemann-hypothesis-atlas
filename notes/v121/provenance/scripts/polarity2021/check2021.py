import sympy as s, mpmath as m, json
m.mp.dps=40
u,b=s.symbols('u b',real=True)
G=(1-u*u)**4
F=s.expand(s.diff(G,u,2)-G/4)
c=s.Poly(s.integrate(s.expand(F*F.subs(u,u-b)),(u,b-1,1)),b)
cf=s.lambdify(b,c.as_expr(),'mpmath'); n=cf(0)
k=lambda a:m.exp(-a/2)/(1-m.exp(-2*a))
J=m.quad(lambda a:k(a)*(2*n-2*cf(a)),[0,.25,.5,1,1.5,2])+2*n*m.quad(k,[2,m.inf])
pp=[(n,m.log(list(s.factorint(n))[0])/m.sqrt(n)) for n in range(2,8) if len(s.factorint(n))==1]
K0=m.digamma(m.mpf(1)/4)-m.log(m.pi)
W=K0*n+J-2*sum(w*cf(m.log(q)) for q,w in pp)
delta=2*m.log(2)/m.sqrt(2)*cf(m.log(2))
out={'G':str(G),'F':str(F),'norm2':str(n),'corr_log2':str(cf(m.log(2))),'W_original':str(W),'drop2_change':str(delta),'W_drop2':str(W+delta),'W_over_norm':str(W/n),'drop2_over_norm':str((W+delta)/n),'Cplus':str(s.integrate(F*s.exp(u/2),(u,-1,1))),'Cminus':str(s.integrate(F*s.exp(-u/2),(u,-1,1)))}
print(json.dumps(out,indent=2)); Path=None
open('../polarity2021/check2021.json','w').write(json.dumps(out,indent=2))
