import mpmath as m, json
m.mp.dps=40
T=lambda a:m.atanh(m.exp(-a/2))+m.atan(m.exp(-a/2))
K0=m.digamma(m.mpf(1)/4)-m.log(m.pi)
out={'K0':str(K0),'small_window_exact_margin_lower_expression':'log(5*sqrt(2)/pi)-EulerGamma-3/80','small_window_margin_lower':str(m.log(5*m.sqrt(2)/m.pi)-m.euler-m.mpf(3)/80),'rows':[]}
for text in ['0.01','0.1','0.25','0.5','1','2','3']:
 A=m.mpf(text)
 # deliberately finite sums: omitted Gamma terms are nonnegative
 gam=2*T(A)
 for n in range(2,1001):
  lam=2-2*m.cos(m.pi/(n+1))
  gam+=lam*(T(A/n)-T(A/(n-1)))
 pp=[]
 for p in [2,3,5,7,11,13,17,19]:
  n=p
  while m.log(n)<A:
   pp.append((n,m.log(p)/m.sqrt(n))); n*=p
 prime=sum(w*(2-2*m.cos(m.pi/(int(m.ceil(A/m.log(n)))+1))) for n,w in pp)
 M=-K0+2*sum(w for n,w in pp)
 out['rows'].append({'A':text,'Gamma_tail_bound':str(2*T(A)),'Gamma_two_scale_bound':str(T(A)+T(A/2)),'Gamma_chain_1000_lower':str(gam),'prime_chain_lower':str(prime),'H_chain_1000_lower':str(gam+prime),'M':str(M)})
print(json.dumps(out,indent=2));open('../poincare2024/check2024.json','w').write(json.dumps(out,indent=2))
