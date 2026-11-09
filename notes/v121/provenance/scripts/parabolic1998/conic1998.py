# parabolic1998: affine-vs-projective classification of one smooth conic with a moving line at infinity;
# three discriminants (ternary det, pole/polar binary restriction, envelope/caustic); h_s gauge; pencil discriminant of J.
import sympy as sp, json
X,Y,Z,x,y,t,k,s,u=sp.symbols('X Y Z x y t k s u',real=True)
out={}
def inertia(Mn):
    ev=[complex(e).real for e in sp.Matrix(Mn).evalf().eigenvals(multiple=True)]
    return (sum(e>1e-12 for e in ev),sum(e<-1e-12 for e in ev),sum(abs(e)<=1e-12 for e in ev))
# 1. pencil x^2 - y + k y^2 = 0  <->  X^2 + kY^2 - YZ = 0 ; k=0 is y=x^2
M=sp.Matrix([[1,0,0],[0,k,-sp.Rational(1,2)],[0,-sp.Rational(1,2),0]])
v=sp.Matrix([X,Y,Z]); Q=sp.expand((v.T*M*v)[0])
out['1 Q_k']=str(Q); out['1 det M_k (ternary discriminant D1)']=str(M.det())
out['1 inertia k=1,0,-1']=[inertia(M.subs(k,kk)) for kk in (1,0,-1)]
Qinf=Q.subs(Z,0); out['1 Q|line_inf']=str(Qinf); out['1 binary disc of Q|line_inf (D3)']=str(sp.discriminant(Qinf.subs(Y,1),X))
adj=M.adjugate(); l_inf=sp.Matrix([0,0,1])
out['1 dual form Q*(l_inf)=l^T adj l']=str((l_inf.T*adj*l_inf)[0])
c=M.inv()*l_inf; out['1 pole of line_inf (center)']=str(list(c)); out['1 Q(center)']=str(sp.simplify((c.T*M*c)[0]))
# 2. tangents and limits
P=lambda pt: sp.Matrix(pt)
tan0=(M.subs(k,0)*P([t,t**2,1])); out['2 parabola tangent at t (coeffs of X,Y,Z)']=str(list(tan0))
out['2 affine form']=str(sp.solve(tan0[0]*x+tan0[1]*y+tan0[2],y)[0])
out['2 projective limit t->oo (normalized by t^2)']=str([sp.limit(e/t**2,t,sp.oo) for e in tan0])
# ellipse k>0: far vertex (0,1/k); vertical tangents
kk=sp.symbols('kk',positive=True)
Me=M.subs(k,kk); far=Me*P([0,1/kk,1]); out['2 ellipse far-vertex tangent']=str(list(sp.simplify(far*kk)))
out['2 ellipse far tangent k->0+']=str([sp.limit(e*kk,kk,0) for e in far])
xs=sp.solve(sp.diff(x**2-y+kk*y**2,y),y); out['2 ellipse vertical tangents at y=']=str(xs)
out['2 ellipse vertical tangent x=']=str(sp.solve((x**2-y+kk*y**2).subs(y,xs[0]),x))
# hyperbola k=-m^2
m=sp.symbols('m',positive=True); Mh=M.subs(k,-m**2)
asym=[sp.simplify(Mh*P([sg*m,1,0])) for sg in (1,-1)]
out['2 hyperbola asymptotes (polars of real points at inf)']=[str(list(a_)) for a_ in asym]
out['2 asymptote affine']=[str(sp.solve(a_[0]*x+a_[1]*y+a_[2],y)[0]) for a_ in asym]
out['2 asymptotes as m->0 (normalize by m^2)']=[str([sp.limit(e,m,0) for e in a_]) for a_ in asym]
# hyperbola branch param, tangent limit along branch = asymptote (finite line)
yb=sp.symbols('yb'); xb=sp.sqrt(yb+m**2*yb**2)
tb=Mh*sp.Matrix([xb,yb,1]); tbn=[sp.limit(e/yb,yb,sp.oo) for e in tb]
out['2 hyperbola tangent along branch y->+oo (normalized)']=str(tbn)
# 3. h_s gauge (user coords Q=X^2-YZ): h_s=(0,1,s)
M0=M.subs(k,0); hs=sp.Matrix([0,1,s]); out['3 Q(h_s)']=str((hs.T*M0*hs)[0])
pol=M0*hs; out['3 polar of h_s']=str(list(pol)); out['3 polar affine: y=']=str(sp.solve(pol[1]*y+pol[2],y)[0])
out['3 affine rep of h_s: (0,1/s)'],out['3 Q at affine rep (0,1/s,1)']='interior axis point',str(((sp.Matrix([0,1/s,1])).T*M0*sp.Matrix([0,1/s,1]))[0])
b1=sp.Matrix([1,0,0]); b2=sp.Matrix([0,1,-s])   # basis of h_s^perp (pol . v = 0)
G=sp.Matrix([[ (a.T*M0*b)[0] for b in (b1,b2)] for a in (b1,b2)]); out['3 Gram of Q on h_s^perp']=str(G.tolist())
out['3 classification']='s>0: definite (ellipse-type complement); s=0: [[1,0],[0,0]] null (tangent line at infinity, parabola); s<0: (1,1) (hyperbola-type)'
# 4. adjugate identity: Gram det on span(p1,p2) = (p1 x p2)^T adj(M) (p1 x p2)  (pole/polar discriminant)
a=sp.symbols('a0:6'); Mg=sp.Matrix([[a[0],a[1],a[2]],[a[1],a[3],a[4]],[a[2],a[4],a[5]]])
p1=sp.Matrix(sp.symbols('p0:3')); p2=sp.Matrix(sp.symbols('q0:3'))
Pm=p1.row_join(p2); lhs=(Pm.T*Mg*Pm).det(); L=p1.cross(p2); rhs=(L.T*Mg.adjugate()*L)[0]
out['4 det(P^T M P) - l^T adj(M) l']=str(sp.expand(lhs-rhs))
out['4 consequence']='binary disc(Q|l) = -4 l^T adj(M) l = -4 det(M) Q(pole(l)); with In(M)=(2,1): Q(pole)<0 <=> Q|l definite (ellipse), =0 tangent (parabola), >0 (1,1) (hyperbola)'
# envelope/caustic discriminant of the tangent family y-2tx+t^2 (D2)
Fam=y-2*t*x+t**2; out['5 envelope disc_t']=str(sp.factor(sp.discriminant(Fam,t)))
out['5 projection Jacobian of incidence (x,t)->(x,y=2tx-t^2) d y/dt']=str(sp.diff(2*t*x-t**2,t))
# 6. pencil discriminant through e=h+v for the extended form J (abstract scalars)
Bf,cp,cm,al,be,tt=sp.symbols('B c_p c_m alpha beta tau',real=True)
Jxx=-Bf+2*al*cp+2*be*cm+2*al*be; Jex=cp+cm+al+be; Jee=2
disc=sp.expand(Jex**2-Jee*Jxx)   # (1/4) disc_tau J(x+tau e)
sol=sp.solve([sp.diff(disc,al),sp.diff(disc,be)],[al,be],dict=True)
crit=sp.Matrix([[sp.diff(disc,al,2),sp.diff(disc,al,be)],[sp.diff(disc,al,be),sp.diff(disc,be,2)]])
# minimize along u=alpha-beta (Hessian PSD rank 1, alpha+beta direction is flat)
dsub=sp.expand(disc.subs({al:(tt+u)/2,be:(tt-u)/2}))
umin=sp.solve(sp.diff(dsub,u),u)[0]; out['6 disc (quarter) in (alpha,beta)']=str(disc)
out['6 Hessian in alpha,beta']=str(crit.tolist()); out['6 min over U-part']=str(sp.factor(sp.expand(dsub.subs(u,umin))))
out['6 compare 2W=2(B+2c_p c_m)']=str(sp.expand(2*(Bf+2*cp*cm)))
json.dump(out,open('conic1998.json','w'),indent=1); print(json.dumps(out,indent=1))
