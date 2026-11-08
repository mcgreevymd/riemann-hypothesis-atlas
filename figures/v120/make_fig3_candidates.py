#!/usr/bin/env python3
"""Figure 3. Two explicit representer candidates fail. RH is not proved.

h1: exact edge-log mechanism, curve is numerical.
h2 at A = 1: exact slope jump under log 2 < A < log 3.
h2 at A = 0.6 is numerical only and is not drawn as a proof.
No universal Gamma-only no-go is claimed.
"""
import os
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parents[1] / "notes" / "v120" / "provenance" / "bundle" / "scripts" / "matching1983"
sys.path.insert(0, str(SCRIPT))
from match1983 import resp  # noqa: E402

fig, ax = plt.subplots(1, 2, figsize=(13.2, 5.6))
A = 0.6
d = np.geomspace(1e-4, 0.25, 28)
v = A / 2 - d
phi = np.array([resp(A, float(x), "h1") / np.cosh(float(x) / 2) for x in v])
ax[0].semilogx(d, phi, "o-", ms=3.5, color="#d7191c", label="response / cosh, A = 0.6")
slope = phi[-1] + 0.5 * np.log(d[-1] / d)
ax[0].semilogx(d, slope, "k--", lw=1.0, label="slope (1/2) log(1/d), from k(a) ~ 1/(2a)")
ax[0].set_xlabel("distance d to the window edge")
ax[0].set_ylabel("response / cosh")
ax[0].set_title("h1 = cosh · 1_window\nlog edge, so not a multiple of cosh", loc="left", fontsize=11)
ax[0].legend(fontsize=8, loc="upper right")
ax[0].text(
    0.02,
    0.02,
    "Exact only after a split at fixed small a0.\nThe untruncated cosh–Gamma integral diverges.",
    transform=ax[0].transAxes,
    fontsize=8,
)

A = 1.0
v0 = np.log(2) - A / 2
vv = np.linspace(-A / 2 + 0.02, A / 2 - 0.02, 121)
r = np.array([resp(A, float(x), "h2") for x in vv])
c = np.cosh(vv / 2)
kappa = float((r * c).sum() / (c * c).sum())
ax[1].plot(vv, r - kappa * c, color="#2b83ba", label="residual after least-squares κ, A = 1")
for s in (1, -1):
    ax[1].axvline(s * v0, color="#c47b2b", ls=":")
ax[1].text(
    0.02,
    0.98,
    "kinks at ±(log 2 − A/2)\njump 0.06191 exact; difference 0.06189",
    transform=ax[1].transAxes,
    fontsize=8.5,
    color="#8a4b08",
    va="top",
)
ax[1].set_xlabel("v on the window")
ax[1].set_title("h2 = Dirichlet cosh, only prime 2 inside\nedge kink translated by log 2", loc="left", fontsize=11)
ax[1].legend(fontsize=8, loc="upper center")
fig.text(
    0.01,
    0.012,
    "Only these two candidates. h2 at A = 0.6 is a 6.92% residual, numerical only. No general no-go.",
    fontsize=8.5,
)
fig.text(0.99, 0.012, "The Riemann Hypothesis is not proved.", ha="right", color="#9b2c2c", fontsize=9)
fig.tight_layout(rect=(0, 0.05, 1, 1))
fig.savefig(HERE / "fig3_candidates.svg")
fig.savefig(HERE / "fig3_candidates.png", dpi=140)
print("ok")
