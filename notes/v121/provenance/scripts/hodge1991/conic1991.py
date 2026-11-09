# hodge1991 part C: binary quadratic forms = Sym^2 model; mod-691 Hecke Jordan block. RH not proved.
import sympy as sp, json
X,Y=sp.symbols('X Y',real=True); a,b=sp.symbols('a b',real=True); z=sp.symbols('z'); x,y=sp.symbols('x y',real=True)
out={}
def coords(f):  # f = Q X^2 + T XY + Z Y^2
    P=sp.Poly(sp.expand(f),X,Y); return (P.coeff_monomial(X**2),P.coeff_monomial(X*Y),P.coeff_monomial(Y**2))
def B(f,g):  # polar of Q(f) = T^2 - 4QZ : B(f,f)=2 Q(f)? use B(f,g)=2T1T2-4(Q1Z2+Q2Z1) so B(f,f)=2*disc
    Q1,T1,Z1=coords(f); Q2,T2,Z2=coords(g); return sp.expand(2*T1*T2-4*(Q1*Z2+Q2*Z1))
zz=x+sp.I*y
v=sp.expand((X-zz*Y)**2); xz=sp.expand((X-zz*Y)*(X-sp.conjugate(zz)*Y)/y); l2=sp.expand((a*X+b*Y)**2)
out['B(v,v) (isotropic F^2)']=str(sp.simplify(B(v,v)))
out['B(xz,xz) = 2*disc']=str(sp.simplify(B(xz,xz)))
out['B(xz,v) (x_z on polar of v)']=str(sp.simplify(B(xz,v)))
out['B(v,vbar)']=str(sp.simplify(B(v,sp.conjugate(v))))
out['B(l^2,xz)+(2/y)|az+b|^2']=str(sp.simplify(B(l2,xz)+2/y*((a*x+b)**2+(a*y)**2)))
out['B(X^2,xz) [cusp 0 null vector]']=str(sp.simplify(B(X**2,xz)))
out['B(Y^2,xz) [cusp inf null vector]']=str(sp.simplify(B(Y**2,xz)))
out['B(X^2+Y^2, X^2+Y^2) at z=i (h point)']=str(B(X**2+Y**2,X**2+Y**2))
# SL2 invariance of disc
al,be,ga,de=sp.symbols('al be ga de')
f=sp.symbols('q t r'); F=f[0]*X**2+f[1]*X*Y+f[2]*Y**2
Fg=sp.expand(F.subs({X:al*X+be*Y,Y:ga*X+de*Y},simultaneous=True))
Qd=lambda g: (lambda c: c[1]**2-4*c[0]*c[2])(coords(g))
out['disc(f|g) - det(g)^2 disc(f)']=str(sp.factor(sp.expand(Qd(Fg)-(al*de-be*ga)**2*Qd(F))))
# unipotent monodromy at cusp inf on Sym^2: T: X->X+Y ; N=log T; weight flag
Tm=lambda g: sp.expand(g.subs({X:X+Y},simultaneous=True))
out['T fixes Y^2? (null cusp vector)']=Tm(Y**2)==Y**2
out['(T-1)^2 X^2 , (T-1)^3 X^2']=[str(sp.expand(Tm(Tm(X**2))-2*Tm(X**2)+X**2)), str(sp.expand(Tm(Tm(Tm(X**2)))-3*Tm(Tm(X**2))+3*Tm(X**2)-X**2))]
out['im N^2 = span Y^2 ; ker N = span Y^2 ; im N = span{XY,Y^2} = polar of Y^2']=[str(sp.simplify(B(Y**2,X*Y))),str(B(Y**2,Y**2)),str(B(Y**2,X**2))]
# mod 691 Hecke Jordan block on M12(Z) basis (E4^3, Delta)
T2=sp.Matrix([[2049,0],[-1296000,-24]])
N=(T2+24*sp.eye(2)).applyfunc(lambda t: t%691)
out['(T2+24) mod 691']=str(N.tolist()); out['((T2+24) mod 691)^2 mod 691']=str((N*N).applyfunc(lambda t:t%691).tolist())
out['T2 eigenvalues over Q']=str(T2.eigenvals()); out['2049 + 24 = 3*691']=2049+24==3*691
json.dump(out,open('conic1991.json','w'),indent=1); print(json.dumps(out,indent=1))
