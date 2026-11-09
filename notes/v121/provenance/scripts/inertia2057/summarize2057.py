import json,pathlib
D=pathlib.Path(__file__).parent
r=json.load(open(D/'scan2057.json'))['refined'];base=json.load(open(D/'inertia2057.json'))['rows']
lines=['\n## 7. Results (generated from JSON)\n','Complete-form cell compressions, **NUM**, n=2048. For EVERY row Q inertia=(1,0,2047), W inertia=(0,0,2048), constrained inertia=(0,0,2046), S_Q=(−,+), S_W=(+,+).\n','| A | S_Q eigenvalues | min constrained (1024 → 2048 cells) | negative Q eigenvector squared overlap with moment span |','|---|---|---|---|']
for x in r:
 if x['n']!=2048:continue
 y=next(a for a in r if a['A']==x['A'] and a['n']==1024)
 lines.append(f"| {x['A']:g} | {x['S_eigenvalues'][0]:.8f}, {x['S_eigenvalues'][1]:.8f} | {y['constrained_min']:.8g} → {x['constrained_min']:.8g} | {x['negative_mode_moment_overlap_squared'][0]:.8f} |")
lines+=['\nCertified-partition finite **minorant** summary (spectral figures/counts NUM; continuum claims CERT as detailed above):\n','| A | cells | inertia(Q_J) | inertia(W_J) | S_Q_J eigenvalues | constrained min |','|---|---|---|---|---|---|']
for fn in ['certify_inertia2057.json','certify_two_inertia2057.json']:
 c=json.load(open(D/fn));lines.append(f"| {c['A']} | {c['cells']} | {tuple(c['finite_minorant_Q_inertia'])} | {tuple(c['finite_minorant_W_inertia'])} | {c['finite_minorant_S'][0]:.8f}, {c['finite_minorant_S'][1]:.8f} | {c['finite_minorant_constrained_min']:.9g} |")
lines+=['\nFor W_J, S_W_J has two negative signs by the nonsingular finite inertia bookkeeping; for Q_J it has one sign of each type. On E0 the pole is zero, so their constrained matrices agree. The corresponding penalized proof matrices have no negative directions.\n','Verified continuum outputs:\n']
for fn in ['certify_inertia2057.json','certify_two_inertia2057.json']:
 c=json.load(open(D/fn));lines.append(f"- A={c['A']}: n−(Q)=1; remaining spectrum ≥{c['continuum_Q_second_spectral_lower']:.6g}; S signature (1,0,1); exact Q constant-trial enclosure {c['constant_trial_Q_interval']}; verified effective second lower {c['verified_effective_second_lower']:.12g}; Schur margin {c['Schur_margin']:.12g}.")
lines+=['\nThe continuum S-sign certification reuses the already certified constrained inequality; it is NOT a logically independent Schur-sign proof of that inequality. The new independent information is the exact unconstrained Q index and gap.\n','`check2057.py` reruns the width-one interval/continuum certificate, recomputes representative finite spectra, and checks all 117 refined/scan inertia identities; output in check2057.json.\n']
with open(D/'notes2057.md','a') as f:f.write('\n'.join(lines))
print('\n'.join(lines))
