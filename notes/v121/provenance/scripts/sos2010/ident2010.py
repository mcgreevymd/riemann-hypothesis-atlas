# sos2010: exact identities (sympy) for the E0 reparametrization and the Gamma pole split.
import sympy as sp, mpmath as mp, json
u,t,a,s=sp.symbols('u t a s',real=True); r={}
# (1) k_inf = k5 + e^{-a/2}, with k_x(a)=e^{-2xa}/(1-e^{-2a})
kinf=sp.exp(-a/2)/(1-sp.exp(-2*a)); k5=sp.exp(-sp.Rational(5,2)*a)/(1-sp.exp(-2*a))
r['kinf-k5-exp(-a/2)']=str(sp.simplify(kinf-k5-sp.exp(-a/2)))
# (2) 2∫_0^∞ e^{-a/2}(1-cos ta)da = 4 - 1/(t^2+1/4)
I=sp.integrate(2*sp.exp(-a/2)*(1-sp.cos(t*a)),(a,0,sp.oo),conds='none')
r['pole_part_symbol']=str(sp.simplify(I)); r['pole_part_check']=str(sp.simplify(I-(4-1/(t**2+sp.Rational(1,4)))))
# (3) Re psi(1/4+it/2) = Re psi(5/4+it/2) - 1/(t^2+1/4) (numeric at several t)
mp.mp.dps=30
r['psi_shift_resid']=[float(mp.re(mp.digamma(0.25+0.5j*tt))-(mp.re(mp.digamma(1.25+0.5j*tt))-1/(tt**2+0.25))) for tt in (0,0.7,3,20)]
r['K5(0)=psi(5/4)-log pi']=float(mp.digamma(1.25)-mp.log(mp.pi)); r['K0+4']=float(mp.digamma(0.25)-mp.log(mp.pi)+4)
# (4) E0 parametrization: F=(d^2-1/4)G => moments vanish; factorization (d-1/2)(d+1/2)=e^{u/2} d e^{-u} d e^{u/2}
G=sp.Function('G')(u)
lhs=sp.diff(G,u,2)-G/4
rhs=sp.exp(u/2)*sp.diff(sp.exp(-u)*sp.diff(sp.exp(u/2)*G,u),u)
r['twisted_factorization_resid']=str(sp.simplify(sp.expand(rhs-lhs)))
# Green's inverse: G(u)=2∫_{-∞}^u sinh((u-s)/2)F(s)ds; right of support: G = e^{u/2}C_- - e^{-u/2}C_+
Fs=sp.Function('F')
r['green_tail']='G(u>supp) = e^{u/2}∫e^{-s/2}F - e^{-u/2}∫e^{s/2}F  (expand 2sinh((u-s)/2))'
# (5) sample polynomial G on [-1,1]: moments of F zero exactly; R(F)=<G,(1/4-d^2)G>=(1/2π)∫|F^|^2/(t^2+1/4)
Gp=(1-u**2)**4*(u**3+2*u+1); Fp=sp.diff(Gp,u,2)-Gp/4
r['moments']=[str(sp.simplify(sp.integrate(Fp*sp.exp(c*u/2),(u,-1,1)))) for c in (1,-1)]
R_local=sp.integrate(sp.diff(Gp,u)**2+Gp**2/4,(u,-1,1))
R_kernel=mp.quad(lambda x,y: mp.e**(-abs(x-y)/2)*float(Fp.subs(u,x))*float(Fp.subs(u,y)) ,[-1,1],[-1,1]) if False else None
fF=sp.lambdify(u,Fp,'mpmath')
R_ker=mp.quad(lambda x: fF(x)*mp.quad(lambda y: mp.e**(-abs(x-y)/2)*fF(y),[-1,x,1]),[-1,1])
r['R_local_exact']=str(R_local); r['R_local']=float(R_local); r['R_kernel_numeric']=float(R_ker)
# ||F||^2 = ||G''||^2 + 1/2||G'||^2 + 1/16||G||^2
r['normF_identity_resid']=str(sp.simplify(sp.integrate(Fp**2,(u,-1,1))-sp.integrate(sp.diff(Gp,u,2)**2+sp.diff(Gp,u)**2/2+Gp**2/16,(u,-1,1))))
json.dump(r,open('ident2010.json','w'),indent=1); print(json.dumps(r,indent=1))
