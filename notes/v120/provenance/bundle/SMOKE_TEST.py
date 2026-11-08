import subprocess, shutil, tempfile, os, sys
root=os.path.dirname(os.path.abspath(__file__)); tmp=tempfile.mkdtemp()
jobs=[('incidence1964','inc1964.py'),('duality1967','dual1967.py'),('gradient1963','g1963.py'),('pqr1947','pqr.py'),
      ('iwasawa1958','iw1958.py'),('eisenstein1954','fam1954_exact.py'),('matching1983','kink1983.py')]
ok=True
for d,s in jobs:
    w=os.path.join(tmp,d); shutil.copytree(os.path.join(root,'scripts',d),w)
    r=subprocess.run([sys.executable,s],cwd=w,capture_output=True,text=True,timeout=300)
    print(f'{d}/{s}: exit {r.returncode}'); ok&=r.returncode==0
    if r.returncode: print(r.stderr[-500:])
print('SMOKE', 'PASS' if ok else 'FAIL')
