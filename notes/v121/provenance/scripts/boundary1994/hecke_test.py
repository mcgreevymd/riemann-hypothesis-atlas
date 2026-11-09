import sympy as sp
X=sp.symbols('X'); w=10
def act(P,g):
    (a,b),(c,d)=g
    return sp.expand(sp.cancel((c*X+d)**w*sp.sympify(P).subs(X,(a*X+b)/(c*X+d))))
S=[[0,-1],[1,0]]; U=[[1,-1],[1,0]]; U2=[[0,-1],[1,-1]]
def inW(P): return sp.expand(P+act(P,S))==0 and sp.expand(P+act(P,U)+act(P,U2))==0
e=X**10-1; c1=X**2*(X**2-1)**3; m1=4*X**9-25*X**7+42*X**5-25*X**3+4*X
def zagier(n):
    M=[]
    for a in range(1,n*2+3):
     for d in range(1,n*2+3):
      for b in range(0,d):
       for c in range(0,a):
        if a*d-b*c==n and a>c>0 and d>b>0: M+= [[[a,b],[c,d]],[[a,-b],[-c,d]]]
    for a in range(1,n+1):
        if n%a: continue
        d=n//a
        for b in range(-d,d+1):
            if -d<2*b<=d: M.append([[a,b],[0,d]])
        for c in range(-a,a+1):
            if -a<2*c<=a and c!=0: M.append([[a,0],[c,d]])
    return M
def T(P,M): return sp.expand(sum(act(P,g) for g in M))
M=zagier(2); print(len(M),M)
for name,P in [('e',e),('c1',c1),('m1',m1)]:
    Q=T(P,M); print(name,'inW',inW(Q))
    a_,b_,c_=sp.symbols('a_ b_ c_'); sol=sp.solve(sp.Poly(Q-(a_*e+b_*c1+c_*m1),X).coeffs(),[a_,b_,c_]); print(' =',sol)
