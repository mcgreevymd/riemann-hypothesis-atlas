import sympy as s, mpmath as m, json
m.mp.dps=40
rows=[]
for n in range(2,17):
 fs=s.factorint(n)
 if len(fs)==1:
  p,j=next(iter(fs.items()))
  rows.append({'n':n,'boson_coefficient':str(s.log(p)),'fermion_coefficient':str((-1)**(j-1)*s.log(p))})
xi=lambda t:m.mpf('.5')*t*(t-1)*m.pi**(-t/2)*m.gamma(t/2)*m.zeta(t)
q=lambda z:m.diff(xi,m.mpf('.5')+z)/xi(m.mpf('.5')+z)
mu=lambda b:-m.diff(m.zeta,b)/m.zeta(b)
beta=m.mpf(2);z=m.mpf(1);w=m.mpf(2)
out={'prime_power_coefficients':rows,'Gibbs_beta2_kernel_z1_w2':str(m.zeta(beta+z+w)/m.zeta(beta)),'target_Kq_z1_w2':str((q(z)+q(w))/(z+w)),'critical_KMS_prime_kernel_z1_w2':str(mu(m.mpf('.5')+z+w)),'boson_energy_beta2':str(mu(beta)),'fermion_energy_beta2':str(mu(beta)-2*mu(2*beta)),'variance_boson_beta2':str(m.diff(lambda t:m.log(m.zeta(t)),beta,2))}
print(json.dumps(out,indent=2));open('../kms2040/check2040.json','w').write(json.dumps(out,indent=2))
