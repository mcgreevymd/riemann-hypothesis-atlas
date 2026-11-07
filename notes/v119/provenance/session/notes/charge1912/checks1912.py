import sympy as sp, itertools
# (a) Bogomolny pointwise in R^4: 2-forms F_ij, Euclidean, vol=e1234
F=sp.symbols('f12 f13 f14 f23 f24 f34',real=True); f12,f13,f14,f23,f24,f34=F
norm2=sum(c**2 for c in F)                      # |F|^2 with <e_ij,e_ij>=1
wedge=2*(f12*f34-f13*f24+f14*f23)                # F∧F = wedge * vol
hodge={'12':f34,'13':-f24,'14':f23,'23':f14,'24':-f13,'34':f12}  # *F components
Fp=[(F[i]+list(hodge.values())[i])/2 for i in range(6)]; Fm=[(F[i]-list(hodge.values())[i])/2 for i in range(6)]
np2=sum(c**2 for c in Fp); nm2=sum(c**2 for c in Fm)
print('(a) |F|^2-(|F+|^2+|F-|^2)=',sp.simplify(norm2-np2-nm2),' F∧F/vol-(|F+|^2-|F-|^2)=',sp.simplify(wedge-(np2-nm2)))
print('    |F|^2 - |F∧F|/vol = 2|F∓|^2 >=0:',sp.simplify(norm2-wedge-2*nm2),sp.simplify(norm2+wedge-2*np2))
# (b) C^2, z1=x1+ix2, z2=x3+ix4, J e1=e2, J e3=e4. omega=e12+e34 SD. real (1,1) <=> J-invariant
J={1:(2,1),2:(1,-1),3:(4,1),4:(3,-1)}  # J e_i = s e_j
idx=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
def Jact(vec):
    out=[0]*6
    for k,(i,j) in enumerate(idx):
        (a,sa),(b,sb)=J[i],J[j]; s=sa*sb
        if a>b: a,b,s=b,a,-s
        out[idx.index((a,b))]+=s*vec[k]
    return out
inv=sp.solve([sp.expand(x-y) for x,y in zip(Jact(list(F)),F)],F,dict=True)[0]
G=[sp.sympify(c).subs(inv) for c in F]           # general real (1,1)
prim={f12:-f34}                                   # <G,omega>=0 => f12+f34=0
Gp=[c.subs(prim) for c in G]
w=2*(Gp[0]*Gp[5]-Gp[1]*Gp[4]+Gp[2]*Gp[3]); n=sum(c**2 for c in Gp)
hG=[Gp[5],-Gp[4],Gp[3],Gp[2],-Gp[1],Gp[0]]
print('(b) real(1,1):',G,' primitive α: *α+α =',[sp.simplify(a+b) for a,b in zip(hG,Gp)],' α∧α/vol+|α|^2 =',sp.simplify(w+n))
# (c) BPS Hessian toy: Phi = |M(x)|^2 + C_top, M(x)=Jx+Q(x)
x=sp.symbols('x1:4',real=True); Jm=sp.Matrix([[1,2,0],[0,1,-1]])
M=Jm*sp.Matrix(x)+sp.Matrix([x[0]*x[1],x[2]**2]); Phi=(M.T*M)[0]+sp.Symbol('k')
H=sp.hessian(Phi,x).subs({xi:0 for xi in x})
print('(c) Hess at BPS =2J^TJ:',sp.simplify(H-2*Jm.T*Jm)==sp.zeros(3),' eig',[sp.nsimplify(e) for e in (2*Jm.T*Jm).eigenvals()])
X,Y=sp.symbols('X Y',real=True); P2=(X**2+Y**2-1)**2
print('    non-BPS crit pt origin of (x^2+y^2-1)^2: Hess eig',list(sp.hessian(P2,(X,Y)).subs({X:0,Y:0}).eigenvals()))
# (d) intersection numbers
NS=sp.Matrix([[0,1],[1,0]]); H=sp.Matrix([1,1]); D=sp.Matrix([1,-1])
print('(d) P1xP1: H.D=',(H.T*NS*D)[0],' D^2=',(D.T*NS*D)[0],' signature eig',list(NS.eigenvals()))
B=sp.diag(1,-1); D2=sp.Matrix([2,1]); E=sp.Matrix([0,1])  # Bl_pt P2 basis H,E
print('    Bl P2: D=2H+E D^2=',(D2.T*B*D2)[0],' D.E=',(D2.T*B*E)[0],' (not ample by Nakai)')
# (e) E×E over F_p, basis h=E×pt, v=pt×E, Δ, Γ (Frobenius graph)
a,p=sp.symbols('a p',real=True)
Gm=sp.Matrix([[0,1,1,p],[1,0,1,1],[1,1,0,p+1-a],[p,1,p+1-a,0]])
hv=[sp.Matrix([1,0,0,0]),sp.Matrix([0,1,0,0])]; Ghv=sp.Matrix(2,2,lambda i,j:(hv[i].T*Gm*hv[j])[0])
def perp(c):
    c=sp.Matrix(c); r=sp.Matrix([(hv[i].T*Gm*c)[0] for i in range(2)]); co=Ghv.inv()*r
    return c-co[0]*hv[0]-co[1]*hv[1]
Pr=[perp(c) for c in ([0,0,1,0],[0,0,0,1])]
Pg=sp.Matrix(2,2,lambda i,j:sp.expand((Pr[i].T*Gm*Pr[j])[0]))
print('(e) <h,v>-perp Gram of Δ,Γ:',Pg,' det=',sp.factor(Pg.det()))
for pa in [(5,2),(5,4),(5,5)]:
    print('    p,a=',pa,' eig',[round(float(e),4) for e in Pg.subs({p:pa[0],a:pa[1]}).eigenvals()])
