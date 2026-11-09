import numpy as np,scipy.linalg as la,json
from scipy.special import digamma

def run(A,J,hgoal,kappa=4):
 b=np.log(2);c3=np.log(3);eps=A-c3;dlt=c3-b;L2=A-b
 if not(0<eps<dlt and L2<b):raise ValueError('partition regime')
 mq=max(1,int(np.ceil(eps/hgoal)));mm=int(np.ceil((dlt-eps)/hgoal));mc=int(np.ceil((b-L2)/hgoal))
 seg=[(0,eps,mq),(eps,dlt,mm),(dlt,L2,mq),(L2,b,mc),(b,b+eps,mq),(b+eps,c3,mm),(c3,A,mq)]
 ll=[];rr=[];inds=[];pos=0
 for l,r,nc in seg:
  e=np.linspace(l-A/2,r-A/2,nc+1);ll.extend(e[:-1]);rr.extend(e[1:]);inds.append(np.arange(pos,pos+nc));pos+=nc
 l=np.array(ll);r=np.array(rr);h=r-l;n=len(h);C=np.zeros((n,n));dd=digamma(.25)-np.log(np.pi);sc=0;sumc=0
 for j in range(J):
  c=2*j+.5;sc+=2/c;sumc+=c;dd+=2/c
  qq=-np.expm1(-c*h)/(c*np.sqrt(h));aa=qq*np.exp(c*r);bb=qq*np.exp(-c*l)
  term=np.triu(np.outer(aa,bb),1);term+=term.T;np.fill_diagonal(term,2/c+2*np.expm1(-c*h)/(c*c*h));C+=term
 R=np.array([np.exp(sign*l/2)*np.expm1(sign*h/2)/(sign*.5*np.sqrt(h)) for sign in [1,-1]]).T
 M=dd*np.eye(n)-C+kappa*R@R.T
 a=np.log(2)/np.sqrt(2);b3=np.log(3)/np.sqrt(3)
 for i,j,w in [(0,4,a),(1,5,a),(2,6,a),(0,6,b3)]:
  M[inds[i],inds[j]]-=w;M[inds[j],inds[i]]-=w
 v=la.eigvalsh(M,subset_by_index=[0,2]);hm=max(h);epsC=2*sumc*(hm/np.pi)**2;rn=4*np.sinh(A/2);epsR=(hm/(2*np.pi))**2*rn
 cross=np.sqrt(sc*epsC)+kappa*np.sqrt(rn*epsR);sn=(b3+np.sqrt(b3*b3+4*a*a))/2;high=dd-sn-epsC
 low=(v[0]+high-np.sqrt((high-v[0])**2+4*cross**2))/2
 out={'A':A,'J':J,'hgoal':hgoal,'kappa':kappa,'n':n,'eig':v.tolist(),'cross':cross,'high':high,'S_norm':sn,'lower_expression':low};print(json.dumps(out));return out
out=[run(A,J,h,k) for A,J,h,k in [(1.1,48,.0012,4),(1.1,96,.0006,4),(1.099,96,.0006,4)]]
json.dump(out,open('../multiprime2047/twoprime_experiment2047.json','w'),indent=2)
