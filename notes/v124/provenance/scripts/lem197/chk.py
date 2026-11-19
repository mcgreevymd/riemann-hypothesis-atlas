import sys; sys.argv=['x','0.025']
exec(open('l197.py').read().split("if __name__=='__main__':")[0])
for base,T,A in (('zeta',Tz,AZ),('zeta_K',TK,A20)):
  for eps in (1e-3,1e-4,-1e-4):
    m=member('x',perturb(T,2,eps),A,True,'')
    o=onset(m,'E0'); N=int(round(o/h))-1
    print(base,eps,o,[ '%.2e'%eig(modrow(m,'E0'),N+k,'E0')[0] for k in (0,4,8)])
# flat forms magnitudes
for nm,A,pole in (('zeta flat',AZ,True),('zetaK flat',A20,True)):
  m=member(nm,{},A,pole,'')
  for mo in ('full','coshperp'):
    o=onset(m,mo); N=int(round(o/h))-1; print(nm,mo,o,['%.2e'%eig(modrow(m,mo),N+k,mo)[0] for k in (0,4,12)])
