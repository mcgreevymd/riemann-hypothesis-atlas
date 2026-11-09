#!/usr/bin/env python3
"""Quick bundle self-check (about 1 min): delta validates, audit re-derivations pass, cited numbers match JSON, figures regenerate,
no machine-local paths in repo-bound text. Full certificate reruns: python3 rerun_all.py (about 10 min; OPENBLAS_NUM_THREADS=1)."""
import subprocess, sys, json, pathlib, re, os
H = pathlib.Path(__file__).resolve().parent
env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
def run(args, cwd=H):
    r = subprocess.run([sys.executable] + args, cwd=cwd, env=env, capture_output=True, text=True, timeout=900)
    print(('OK  ' if r.returncode == 0 else 'FAIL') + ' ' + ' '.join(args), r.stdout.strip().splitlines()[-1:] if r.stdout.strip() else '')
    return r.returncode == 0
ok = run(['delta/build_delta.py'], H)
ok &= run(['audit2060.py'], H / 'checks') and json.load(open(H / 'checks/audit2060.json'))['all_ok']
ok &= run(['checks/numbers_crosscheck.py'])
ok &= run(['figures/make_figures.py'])
bad = [str(p.relative_to(H)) for p in H.rglob('*') if p.is_file() and p.suffix in {'.md', '.py', '.json', '.txt', '.jsonl'}
       and 'rerun_tree' not in p.parts and 'ref' not in p.parts and p.name != 'SMOKE_TEST.py' and re.search(r'/(workspace|home)/', p.read_text(errors='ignore'))]
print(('OK  ' if not bad else 'FAIL') + ' no machine-local paths', bad[:5]); ok &= not bad
print('SMOKE_TEST', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
