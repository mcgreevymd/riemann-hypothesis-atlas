# effectivity2001: surface RR / Hodge index calibration on C x C over F_q, and the RELATIVE (GRR-for-a-fibration) effectivity mechanism.
import sympy as sp, json, itertools
q,a,g,n,eps=sp.symbols('q a g n epsilon',real=True)
out={}
# NS lattice span(h,v,Delta,Gamma) on C x C (C genus g over F_q; Gamma = graph of q-Frobenius). h = C x pt (fibre of pr2), v = pt x C (fibre of pr1).
# Intersections (Hartshorne V Ex.1.9/1.10): h^2=v^2=0, h.v=1, D.h=D.v=1, D^2=2-2g, G.h=q? : Gamma=(x,F(x)): Gamma.(C x pt)=deg of F = q ; Gamma.(pt x C)=1
# Gamma^2 = q(2-2g), Delta.Gamma = N_1 = q+1-a.
names=['h','v','D','G']
Gm=sp.Matrix([[0,1,1,q],[1,0,1,1],[1,1,2-2*g,q+1-a],[q,1,q+1-a,q*(2-2*g)]])
out['Gram(h,v,Delta,Gamma)']=str(Gm.tolist())
H=sp.Matrix([1,1,0,0])  # ample h+v
# primitive part w.r.t. U=span(h,v): x' = x - (x.v)h - (x.h)v
def prim(x): return x-(x.T*Gm*sp.Matrix([0,1,0,0]))[0]*sp.Matrix([1,0,0,0])-(x.T*Gm*sp.Matrix([1,0,0,0]))[0]*sp.Matrix([0,1,0,0])
Dp=prim(sp.Matrix([0,0,1,0])); Gp=prim(sp.Matrix([0,0,0,1]))
P=sp.Matrix([[ (x.T*Gm*y)[0] for y in (Dp,Gp)] for x in (Dp,Gp)]).applyfunc(sp.expand)
out['primitive Gram (Delta\',Gamma\')']=str(P.tolist()); out['det primitive (g=1)']=str(sp.factor(P.det().subs(g,1)))
out['Hodge index on primitive (g=1) <=> det>=0 & trace<0']='det = 4q - a^2 (g=1): >=0 iff |a| <= 2 sqrt q (Hasse)'
# fake curve: g=1,q=5,a=5 (> 2 sqrt 5): find D perp U with D^2>0
vals={g:1,q:5,a:5}; Pn=P.subs(vals); ev=Pn.eigenvects()
out['fake q=5,a=5 primitive Gram']=str(Pn.tolist()); out['fake eigen']=str([(e,m) for e,m,_ in ev])
pos=[vv for e,m,vv in ev if e>0][0][0]; Dbad=(pos[0]*Dp+pos[1]*Gp).subs(vals)
Gn=Gm.subs(vals); ip=lambda x,y:(x.T*Gn*y)[0]
out['fake D (coords h,v,Delta,Gamma)']=str(list(Dbad)); out['fake D.h, D.v, D.H, D^2']=[str(sp.nsimplify(ip(Dbad,sp.Matrix(c)))) for c in ([1,0,0,0],[0,1,0,0],[1,1,0,0])]+[str(sp.simplify(ip(Dbad,Dbad)))]
# relative tilt D' = D + eps(h - v): fibre degrees (+eps on pr1-fibre v? ) ; D'.H = 0 ; D'^2 = D^2 - 2 eps^2
Dt=Dbad+eps*sp.Matrix([1,-1,0,0])
out['tilt: D\'.h (deg on fibre h of pr2)']=str(sp.simplify(ip(Dt,sp.Matrix([1,0,0,0])))); out['tilt: D\'.v (deg on fibre v of pr1)']=str(sp.simplify(ip(Dt,sp.Matrix([0,1,0,0]))))
out['tilt: D\'.H']=str(sp.simplify(ip(Dt,H))); out['tilt: D\'^2']=str(sp.expand(ip(Dt,Dt)))
# GRR for f = pr1 : X -> C (fibre class v): for L=O(nD'), rank f_*L = n D'.v + 1 - g, R^1 f_*L = 0 once n D'.v > 2g-2,
# chi(X,L) = chi(C, f_*L) = deg f_*L + rank (1-g)  and chi(X,L) = (1/2) L.(L-K) + chi(O_X),  K_X = (2g-2)(h+v)
Dsym=sp.symbols('x0:4'); Dv=sp.Matrix(Dsym); K=(2*g-2)*sp.Matrix([1,1,0,0]); chiO=(1-g)**2
GmS=Gm; ipS=lambda x,y:sp.expand((x.T*GmS*y)[0])
chiX=sp.expand(sp.Rational(1,2)*ipS(n*Dv,n*Dv-K)+chiO); rk=n*ipS(Dv,sp.Matrix([0,1,0,0]))+1-g   # CORRECTED 2002: fibre RR (deg>2g-2) gives rank nD.v+1-g
degf=sp.expand(chiX-rk*(1-g))
out['GRR deg det f_*O(nD) (pr1)']=str(sp.collect(degf,n)); out['n^2 coefficient']=str(sp.factor(degf.coeff(n,2)))
out['n^2 coeff equals D^2/2']=str(sp.simplify(degf.coeff(n,2)-ipS(Dv,Dv)/2)==0)
# relative adjunction for the section Delta of pr2: Delta^2 = -deg(sigma^* omega_{X/B}) = -(2g-2)
out['section adjunction Delta^2 + (2g-2)']=str(sp.simplify(Gm[2,2]+(2*g-2)))
json.dump(out,open('relrr2001.json','w'),indent=1); print(json.dumps(out,indent=1))
