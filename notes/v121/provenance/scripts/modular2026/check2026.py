import sympy as s, json
q=s.symbols('q'); N=16
E2=1-24*sum(s.divisor_sigma(n,1)*q**n for n in range(1,N+1))
E4=1+240*sum(s.divisor_sigma(n,3)*q**n for n in range(1,N+1))
E6=1-504*sum(s.divisor_sigma(n,5)*q**n for n in range(1,N+1))
tr=lambda x:s.series(s.expand(x),q,0,N+1).removeO()
theta=lambda x:q*s.diff(x,q)
Delta=tr((E4**3-E6**2)/1728)
checks={'thetaE2':tr(theta(E2)-(E2**2-E4)/12),'thetaE4':tr(theta(E4)-(E2*E4-E6)/3),'thetaE6':tr(theta(E6)-(E2*E6-E4**2)/2),'D4E4':tr(theta(E4)-E2*E4/3+E6/3),'D6E6':tr(theta(E6)-E2*E6/2+E4**2/2),'D12Delta':tr(theta(Delta)-E2*Delta)}
y=s.symbols('y',positive=True); G=s.Function('G'); u=s.symbols('u',real=True)
# Generic differential coefficient check, using a dummy G(log y).
rad=s.simplify(-y*y*s.diff(s.sqrt(y)*G(s.log(y)),y,2)/s.sqrt(y))
checks['radial_cusp_identity']=str(rad)
out={'exact_coefficient_checks_through_q_power':N,'residuals':{k:str(v) for k,v in checks.items()},'Delta_initial_terms':str(s.series(Delta,q,0,6))}
print(json.dumps(out,indent=2));open('../modular2026/check2026.json','w').write(json.dumps(out,indent=2))
