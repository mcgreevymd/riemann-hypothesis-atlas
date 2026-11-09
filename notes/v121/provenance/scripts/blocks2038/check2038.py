import mpmath as m, sympy as s, json
m.mp.dps=50
T5=lambda x:m.atanh(m.exp(-x/2))+m.atan(m.exp(-x/2))-2*m.exp(-x/2)
def atoms(B):
 return [(n,m.log(list(s.factorint(n))[0])/m.sqrt(n),m.log(n)) for n in range(2,int(m.exp(B))+1) if len(s.factorint(n))==1 and m.log(n)<B]
B=m.mpf(2); pp=atoms(B); rows=[]
for text in ['0.5','1','1.96']:
 x=m.mpf(text); g=T5(x); p=sum(w for n,w,b in pp if b>=x); d=2*(m.exp(B/2)-m.exp(x/2)); a=g+p
 mat=m.matrix([[a,-d],[-d,d]])
 vals=m.eigsy(mat,eigvals_only=True)
 sat=(m.sqrt(a)-m.sqrt(d))**2
 rows.append({'s':text,'Gamma5_weight':str(g),'prime_tail_weight':str(p),'smooth_density_weight':str(d),'exact_signed_storage_weight':str(a-d),'exact_match_block_determinant':str(d*(a-d)),'exact_match_block_eigenvalues':[str(v) for v in vals],'PSD_saturation_storage_weight':str(sat),'rho_required_for_exact_match':str(m.sqrt(d/a))})
K0=m.digamma(m.mpf(1)/4)-m.log(m.pi); M=-K0+2*sum(w for n,w,b in pp); Mt=M-4*m.exp(B/2)
ghost_s=m.mpf('0.5'); ghost_g=T5(ghost_s); ghost_p=sum(w for n,w,b in pp if b>=ghost_s and n!=2); ghost_d=2*(m.exp(B/2)-m.exp(ghost_s/2)); ghost_weight=ghost_g+ghost_p-ghost_d
print('Ghost at s=.5 signed weight:',ghost_weight)
out={'drop2_at_s_half_signed_weight':str(ghost_weight),'drop2_at_s_half_match_block_det':str(ghost_d*ghost_weight),'prime_atoms':[(n,str(w)) for n,w,b in pp],'B':'2','rows':rows,'Mtilde':str(Mt),'q_EB_at_zero':str(-Mt/2),'q_EB_drop2_at_zero':str(-Mt/2+m.log(2)/m.sqrt(2))}
print(json.dumps(out,indent=2));open('../blocks2038/check2038.json','w').write(json.dumps(out,indent=2))
