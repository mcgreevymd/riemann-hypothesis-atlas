# exact asymptotic of chihat(O(n)) on P^1_Z with FS L2 metric (derived via Stirling + Barnes G):
# chihat = N^2/4 + (N/4)log N - (N/4)log 2pi + (1/12)log N + 1/24 - zeta'(-1) + o(1),  N=n+1
import mpmath as mp, json
mp.mp.dps=40
def closed(n): N=n+1; return 0.5*(N*mp.log(mp.factorial(N))-2*mp.log(mp.barnesg(N+1)))
def asym(n): N=mp.mpf(n+1); return N**2/4+N/4*mp.log(N)-N/4*mp.log(2*mp.pi)+mp.log(N)/12+mp.mpf(1)/24-mp.zeta(-1,derivative=1)
r={str(n):float(closed(n)-asym(n)) for n in (10,100,1000,10000)}
json.dump(r,open('p1asym2001.json','w'),indent=1); print(r)
