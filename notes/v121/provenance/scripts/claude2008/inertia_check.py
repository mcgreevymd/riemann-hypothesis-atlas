"""Finite inertia check (Q = W - P nonsingular, S = C^T Q^-1 C nonsingular, C rank 2):
   n_-(W) = n_-(Q) + n_+(J2 + S) - 1,   n_-(W|E0) = n_-(Q) + n_+(S) - 2.
Ghost (falsifier only): gamma_1 moved to +-gamma_1 +- 0.3i (exact rank-6 zero move); box grid h = 0.01."""
import json, sys, os, numpy as np, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import r33_onemode as r3
from schur_flow import ghost_col
h, t, beta = 0.01, float(mp.im(mp.zetazero(1))), 0.3
J2 = np.array([[0.0, 1.0], [1.0, 0.0]]); rows = []
for ell in (1.00, 1.05, 1.10, 1.12, 1.15, 1.18, 1.22):
    N = int(round(ell / h)); Z, kp, km = r3.grid_Z(N * h, h, r3.Sector("zeta"))
    a = h * np.arange(N); b = a + h; c = ghost_col(a, b, t, beta)
    D = c[np.abs(np.arange(N)[:, None] - np.arange(N)[None, :])]
    Q = Z + D; C = np.column_stack([kp, km]); W = Q + C @ J2 @ C.T
    S = C.T @ np.linalg.solve(Q, C); Qp, _ = np.linalg.qr(C, mode="complete"); E0 = Qp[:, 2:]
    nQ = int((np.linalg.eigvalsh(Q) < 0).sum()); nW = int((np.linalg.eigvalsh(W) < 0).sum())
    nE0 = int((np.linalg.eigvalsh(E0.T @ W @ E0) < 0).sum())
    nJS = int((np.linalg.eigvalsh(J2 + S) > 0).sum()); nS = int((np.linalg.eigvalsh(S) > 0).sum())
    rows.append({"ell": N * h, "n-(Q)": nQ, "n-(W)": nW, "formula n-(Q)+n+(J2+S)-1": nQ + nJS - 1,
                 "n-(W|E0)": nE0, "formula n-(Q)+n+(S)-2": nQ + nS - 2, "eig S": np.linalg.eigvalsh(S).round(5).tolist(),
                 "eig(J2+S)": np.linalg.eigvalsh(J2 + S).tolist(), "lambda_min W": float(np.linalg.eigvalsh(W)[0])})
    print({k: (round(v, 6) if isinstance(v, float) else v) for k, v in rows[-1].items() if k != "eig(J2+S)"},
          "eig(J2+S):", ["%.2e" % x for x in rows[-1]["eig(J2+S)"]])
json.dump(rows, open(os.path.join(HERE, "inertia_check.json"), "w"), indent=1)
