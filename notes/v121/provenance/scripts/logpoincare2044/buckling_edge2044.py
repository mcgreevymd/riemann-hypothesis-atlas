import mpmath as m,json
m.mp.dps=50
K0=m.digamma(m.mpf(1)/4)-m.log(m.pi)
T=lambda a:m.atanh(m.exp(-a/2))+m.atan(m.exp(-a/2))
K=lambda t:m.re(m.digamma(m.mpf(1)/4+m.j*t/2))-m.log(m.pi)
def run(text):
 A=m.mpf(text); b=m.log(2); delta=A-b
 k0=2*m.pi/A-A/(4*m.pi)
 kl=2*m.pi/A-1/(4*k0) # elementary rigorous lower k, when k0>0
 kg=K(kl); vm=2*T(A/2); base=K0+vm
 if delta>0:
  Delta=T(delta)+T(A)-vm
  weight=m.log(2)/m.sqrt(2)
  theta=weight/Delta
  bound=(1-theta)*kg+theta*base if Delta>0 and 0<=theta<=1 else None
 else:Delta=theta=bound=m.nan
 return dict(A=text,k_lower=str(kl),Gamma_constrained_lower=str(kg),potential_baseline=str(base),edge_delta=str(delta),potential_gain=str(Delta),theta=str(theta),W_lower=(str(bound) if bound is not None else None),admissible=(bound is not None and not m.isnan(bound)))
rows=[run(x) for x in ['0.5','0.69','0.69315','0.6932','0.6935','0.694','0.695','0.7','0.75','1']]
print(json.dumps(rows,indent=2));json.dump(rows,open('../logpoincare2044/buckling_edge2044.json','w'),indent=2)
