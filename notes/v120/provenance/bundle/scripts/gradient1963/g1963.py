import sympy as sp
q,p,a,b,t,tau,u=sp.symbols('q p a b t tau u',real=True)
J=sp.Matrix([[0,-1],[1,0]]); H=(a*q**2+b*p**2)/2
grad=sp.Matrix([sp.diff(H,q),sp.diff(H,p)])
X=sp.Matrix([sp.diff(H,p),-sp.diff(H,q)])          # i_X(dq^dp)=dH
w=lambda U,V:(J*U).dot(V)                             # omega(U,V)=g(JU,V)
U=sp.Matrix(sp.symbols('u1 u2')); 
print('omega=dq^dp:',sp.expand(w(sp.Matrix([1,0]),sp.Matrix([0,1]))))
print('i_X omega = dH:',sp.simplify(sp.Matrix([w(X,sp.Matrix([1,0])),w(X,sp.Matrix([0,1]))])-grad).T)
print('X=-J grad:',sp.simplify(X+J*grad).T,' JX=grad:',sp.simplify(J*X-grad).T,' grad.X=',sp.simplify(grad.dot(X)))
AH=sp.Matrix([[0,b],[-a,0]]); AG=-sp.diag(a,b)
print('ham eig',AH.eigenvals(),' det exp(tA_H)=',sp.simplify(sp.exp(AH.trace()*t)))
print('neg-grad det=',sp.exp(AG.trace()*tau),' = exp(-int Lap H)')
s={a:2,b:-1}
print('saddle a=2,b=-1: ham eig',AH.subs(s).eigenvals(),' grad eig',AG.subs(s).eigenvals(),' det',sp.exp(AG.subs(s).trace()*tau))
# xi toy overlaps
print('Gaussian overlap',sp.simplify(sp.integrate(sp.exp(sp.I*t*u)*sp.exp(-u**2/2)/sp.sqrt(2*sp.pi),(u,-sp.oo,sp.oo))))
print('uniform overlap',sp.simplify(sp.integrate(sp.exp(sp.I*t*u)/2,(u,-1,1)).rewrite(sp.sin)))
