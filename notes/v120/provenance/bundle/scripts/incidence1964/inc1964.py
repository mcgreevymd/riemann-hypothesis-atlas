import sympy as sp
t,q,c=sp.symbols('t q c',real=True)
F=4*q-t**2                      # = -Delta = 4 det G ; Jacobi analogue D=4n-r^2
G=sp.Matrix([[1,-t/2],[-t/2,q]])
print('detG*4 - F =',sp.simplify(4*G.det()-F))
gF=sp.Matrix([sp.diff(F,t),sp.diff(F,q)]); print('grad F =',gF.T,' |grad|^2 =',sp.expand(gF.dot(gF)),' (never 0)')
J=sp.Matrix([[0,-1],[1,0]]); X=-J*gF; print('X_F=-J grad =',X.T,' X.grad =',sp.simplify(X.dot(gF)))
print('rank G on wall q=t^2/4:',G.subs(q,t**2/4).rank(simplify=True),' Jacobian rank of F there:',sp.Matrix([gF.T]).subs(q,t**2/4).rank())
v=sp.Matrix([t/2,1]); print('G v on wall =',sp.simplify((G*v).subs(q,t**2/4)).T)
print('Feynman-Hellmann d lam/dq = <v,G_q v>/<v,v> =',sp.simplify(v.dot(sp.diff(G,q)*v)/v.dot(v)))
print('d lam/dt at wall =',sp.simplify((v.dot(sp.diff(G,t)*v)/v.dot(v)).subs(q,t**2/4)))
print('level-set speed for phi=F-c(s): V_n = c\'/|grad F| =',sp.simplify(1/sp.sqrt(gF.dot(gF))),'* c\'(s)')
