import sympy as s, mpmath as m, json
z,w,b=s.symbols('z w b',positive=True) # w stands for conjugate of second spectral variable
q=lambda x:1-s.exp(-b*x)
res=s.simplify((q(z)+q(w))/(z+w)-(1-s.exp(-(z+w)*b))/(z+w)-q(z)*q(w)/(z+w))
r=lambda x:1/(x-s.Rational(1,2))+1/(x+s.Rational(1,2))
rres=s.factor((r(z)+r(w))/(z+w)-1/((z-s.Rational(1,2))*(w+s.Rational(1,2)))-1/((z+s.Rational(1,2))*(w-s.Rational(1,2))))
A=s.diag(s.Rational(1,2),-s.Rational(1,2)); P=s.Matrix([[0,1],[1,0]]); B=s.Matrix([1,1]); C=s.Matrix([[1,1]])
m.mp.dps=60
xi=lambda t:m.mpf('.5')*t*(t-1)*m.pi**(-t/2)*m.gamma(t/2)*m.zeta(t)
x0=xi(m.mpf('.5')); x2=m.diff(xi,m.mpf('.5'),2)
out={'delay_kernel_identity_residual':str(res),'boundary_kernel_identity_residual':str(rres),'AstarPplusPA':str(A.T*P+P*A),'PBminusCstar':str(P*B-C.T),'xi_center':str(x0),'q_at_center':'0 exactly by FE','qprime_at_center':str(x2/x0),'cubic_low_frequency_control_q(1+2i)':str((1+2j)+(1+2j)**3)}
print(json.dumps(out,indent=2));open('../realization2033/check2033.json','w').write(json.dumps(out,indent=2))
