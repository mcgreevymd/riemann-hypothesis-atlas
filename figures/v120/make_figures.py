#!/usr/bin/env python3
"""Atlas v1.20 figures. Values are the audited session numbers. RH is not proved.

The model null conic is labeled "Q = 0 / discriminant boundary".
It is not captioned as a Hasse wall, a parabolic wall, a Routh wall, or a sheet of Sigma.

Animation gauges:
  homogeneous representative h_s = (0, 1, s),  Q(h_s) = -4s
  affine chart Z = 1, plotted height q = 1/s,  Q_aff = -4/s
The sign for s > 0 is negative in both gauges. The projective limit s -> 0 is the
null point x_infinity, independent of the gauge. The magnitudes are not the same number.

Right-hand set:
  level set  v_T^2 + 4 s v_Q^2 = 1  tends to the lines v_T = +/- 1
  sublevel   v_T^2 + 4 s v_Q^2 <= 1 tends to the strip |v_T| <= 1
The level set does not become the strip. The filled region is the sublevel.
"""
import io
import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
os.chdir(HERE)
FOOT = "The Riemann Hypothesis is not proved."
plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "mathtext.fontset": "dejavusans",
})


def save(fig, stem):
    fig.savefig(HERE / f"{stem}.svg")
    fig.savefig(HERE / f"{stem}.png", dpi=140)
    plt.close(fig)


# ---------- Figure 1: exact ledger ----------
fig, ax = plt.subplots(1, 2, figsize=(13.2, 6.2), gridspec_kw={"width_ratios": [1.22, 1]})
ax[0].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[0].axis("off")
lines = [
    r"$W(F)=P(F)+B(F)$",
    r"$P=2\,\mathrm{ev}_+\mathrm{ev}_-=2(C^2-S^2)=2\,\mathrm{Re}(C_+\overline{C_-})$",
    r"$B=H_A-M_A\|F\|^2=\frac{1}{2\pi}\int m_A|\hat F|^2$",
    r"$H_A=$ archimedean springs $+$ prime springs, each $\geq 0$",
    r"$M_A=-K_0+2\sum_{\log n<A}\Lambda(n)\,n^{-1/2}$",
    r"$K_0=\psi(1/4)-\log\pi=-5.37218$",
    r"$E_0$ kills $P$ only. The diagonal $M_A\|F\|^2$ stays in $B$.",
    r"Positive local covariances are subtracted, not added.",
    r"They match terms. They are not a sign mechanism.",
]
for i, s in enumerate(lines):
    ax[0].text(0.02, 0.96 - i * 0.095, s, va="top", fontsize=12, transform=ax[0].transAxes)
ax[0].set_title("Exact window ledger", loc="left", fontweight="bold")

labels = ["arch", "p = 2", "p = 3", "p = 5", "total W"]
values = [0.090, 9.092, -9.001, -0.0016, 0.1788]
colors = ["#2b83ba", "#1a9641", "#d7191c", "#d7191c", "#222222"]
bars = ax[1].bar(labels, values, color=colors, width=0.72)
ax[1].axhline(0, color="#666666", lw=0.8)
for i, v in enumerate(values):
    offset = 0.35 if v >= 0 else -0.55
    ax[1].text(i, v + offset, f"{v:+.4g}", ha="center", va="bottom" if v >= 0 else "top", fontsize=10)
ax[1].annotate(
    "positive covariance\nsubtracted inside each prime",
    xy=(1, 9.092),
    xytext=(2.15, 6.2),
    fontsize=9,
    color="#145c3a",
    arrowprops=dict(arrowstyle="->", color="#145c3a"),
)
ax[1].set_ylim(-11.2, 11.2)
ax[1].set_ylabel("contribution to W(F)")
ax[1].set_title("One window, uncertified", loc="left", fontweight="bold")
fig.text(
    0.08,
    0.02,
    "A = 2, sin⁸ test. Rounded bars sum to 0.1794; session total 0.1788. Not a certificate.",
    fontsize=9,
    va="bottom",
)
fig.text(0.99, 0.02, FOOT, ha="right", color="#9b2c2c", fontsize=10, va="bottom")
fig.tight_layout(rect=(0, 0.07, 1, 1))
save(fig, "fig1_ledger")


# ---------- Figure 2: one form, two jobs ----------
fig, ax = plt.subplots(1, 2, figsize=(13.4, 6.6))
t = np.linspace(-4, 4, 400)
a = ax[0]
a.plot(t, t**2 / 4, color="black", lw=2.0, label="model discriminant conic Q = 0")
a.fill_between(t, t**2 / 4, 6.2, color="#1a9641", alpha=0.12, label="projective form negative (Q < 0)")
for p0 in (-1.5, -0.75, 0.75, 1.5):
    a.plot(t, p0 * t - p0**2, color="#9aa0a6", lw=0.7)
a.plot([0], [1], "o", color="#7b2d8e", ms=8, zorder=3)
a.axhline(-1, color="#7b2d8e", ls="--", lw=1.1)
a.axvline(0, color="#c47b2b", lw=1.0)
a.annotate(
    "h = (0:1:1),  Q = −4",
    xy=(0, 1),
    xytext=(-3.6, 2.4),
    color="#7b2d8e",
    fontsize=9,
    arrowprops=dict(arrowstyle="->", color="#7b2d8e"),
)
a.text(-3.9, -1.55, "polar q = −1 (extra Euclidean directrix)", color="#7b2d8e", fontsize=8)
a.set_xlim(-4, 4)
a.set_ylim(-2.15, 6.15)
a.set_xlabel("affine t")
a.set_ylabel("affine q")
a.legend(loc="upper right", fontsize=8, frameon=True)
a.set_title("Model polarity, not a wall of ζ", loc="left", fontweight="bold")
a.text(
    0.0,
    -0.28,
    "Model discriminant conic. x∞ = (0:1:0) is null; its polar Z = 0 has no affine intercept.\n"
    "Not the parabolic wall, the Routh wall, the Beurling-pencil Hasse wall, or a sheet of Σ.\n"
    "Smooth at x∞. Not a modular cusp. Focus and directrix are extra Euclidean structure.",
    transform=a.transAxes,
    fontsize=8,
    va="top",
)

b = ax[1]
b.axis("off")
rows = [
    "Curve: E alternating on H¹. Weight 1 stays skew.",
    "Product: I(a⊗b, c⊗d) = −E(a,c) E(b,d), symmetric.",
    "Area 1: E(dz, conjugate dz) = −2i.",
    "Mixed real primitive (1,1): I = −8 < 0.",
    "(2,0)+(0,2) real vector: I = +8 > 0.",
    "Only that mixed vector is negative in this pair.",
    "Not every class in H¹⊗H¹ is negative.",
    "A fixed finite H¹,¹ cannot carry W. High frequency, not mere unboundedness.",
    "No geometric map is constructed.",
]
for i, s in enumerate(rows):
    b.text(0.02, 0.96 - i * 0.095, s, transform=b.transAxes, fontsize=12, va="top")
b.set_title("Skew on the curve, symmetric on the product", loc="left", fontweight="bold")
fig.text(0.99, 0.012, FOOT + "  Model only.", ha="right", color="#9b2c2c", fontsize=10)
fig.tight_layout(rect=(0, 0.14, 1, 1))
save(fig, "fig2_polarity")


# ---------- Supplementary spectrum (not a certified eigenvalue plot) ----------
fig, ax = plt.subplots(figsize=(9.6, 5.6))
A = [0.6, 1.0]
# Session table, uncertified. Not an error bar and not a certified bracket.
ax.plot(A, [1.114, 1.977], "s-", color="#d7191c", label="|first even value| (session table)")
ax.plot(A, [0.732, 0.0134], "o-", color="#2b83ba", label="next even value (not a certified gap)")
ax.scatter([a - 0.04 for a in A], [0.697, 0.01315], marker="D", s=42, color="#1a9641", label="Ritz upper estimate (same A)", zorder=3)
ax.scatter([a + 0.04 for a in A], [0.6919, 0.0119], marker="v", s=42, color="#4a7c23", label="lower-inspired estimate (same A)", zorder=3)
ax.axvline(2.0, color="grey", ls=":")
ax.text(1.48, 0.02, "A = 2 unresolved\nnear-null cluster\nnot an eigenvalue\n|cosine| there is not certified", fontsize=8.5)
ax.set_yscale("log")
ax.set_xlim(0.4, 2.35)
ax.set_xlabel("window width A")
ax.set_ylabel("session value (log scale)")
ax.set_title("Supplementary. Estimates, not certified brackets.\n|cosine| 0.970, 0.991, 0.997 is not a squared overlap.", loc="left")
ax.legend(fontsize=8, loc="upper right")
fig.text(0.99, 0.012, FOOT, ha="right", color="#9b2c2c", fontsize=10)
fig.tight_layout(rect=(0, 0.04, 1, 1))
save(fig, "figS_moment_spectrum")


# ---------- Animation ----------
S = np.concatenate([np.linspace(1.0, 0.05, 40), np.full(8, 0.05)])
theta = np.linspace(0, 2 * np.pi, 360)


def draw(axes, s, clamp=10.0):
    left, right = axes
    for artist in axes:
        artist.cla()
    q_aff = 1.0 / s
    q_hom = -4.0 * s
    q_aff_value = -4.0 / s
    yy = np.clip(q_aff, -clamp + 0.4, clamp - 0.4)
    yp = np.clip(-q_aff, -clamp + 0.4, clamp - 0.4)
    left.plot(t, t**2 / 4, color="black", lw=2.0)
    left.fill_between(t, t**2 / 4, clamp, color="#1a9641", alpha=0.08)
    for p0 in np.linspace(-2, 2, 9):
        left.plot(t, p0 * t - p0**2, color="#b0b4b8", lw=0.45)
    left.plot([0], [yy], "o", color="#7b2d8e", ms=8, zorder=3)
    left.axhline(yp, color="#7b2d8e", ls="--", lw=1.0)
    left.set_xlim(-4, 4)
    left.set_ylim(-clamp, clamp)
    left.set_xlabel("affine t  (chart Z = 1)")
    left.set_ylabel("affine q")
    left.set_title(
        f"s = {s:.2f}    h_s = (0 : 1 : s)\n"
        f"homogeneous Q = {q_hom:.3g}     affine Q = {q_aff_value:.3g}\n"
        f"plotted q = 1/s = {q_aff:.3g} (clamped if outside the frame)",
        fontsize=9,
    )
    # Filled sublevel, then the level curve. Limit lines of the level set.
    ys = np.sin(theta) / (2 * np.sqrt(s))
    xs = np.cos(theta)
    right.fill(xs, ys, color="#7b2d8e", alpha=0.25, label="sublevel Q ≤ 1")
    right.plot(xs, ys, color="#7b2d8e", lw=1.6, label="level set Q = 1")
    right.axvline(1, color="#555555", ls=":", lw=1.0)
    right.axvline(-1, color="#555555", ls=":", lw=1.0)
    right.set_xlim(-3.2, 3.2)
    right.set_ylim(-3.4, 3.4)
    right.set_aspect("equal", adjustable="box")
    right.set_xlabel(r"$v_T$")
    right.set_ylabel(r"$v_Q$")
    right.set_title(
        "On v_Z = −s v_Q:  Q = v_T² + 4 s v_Q²\n"
        "level set → lines v_T = ±1;  filled sublevel → strip |v_T| ≤ 1",
        fontsize=9,
    )
    right.legend(loc="upper right", fontsize=8, frameon=True)
    right.text(
        0.02,
        0.02,
        "sign(Q) < 0 and the limit point x∞ are gauge-invariant",
        transform=right.transAxes,
        fontsize=8,
        color="#333333",
    )


fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.6))

wanted = {
    "s1.00": 1.0,
    "s0.50": 0.5,
    "s0.05": 0.05,
}
for stem, s_value in wanted.items():
    draw(axes, float(s_value))
    fig.text(0.99, 0.01, FOOT + "  Schematic algebra, not a recording.", ha="right", color="#9b2c2c", fontsize=8)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(HERE / f"frame_{stem}.png", dpi=140)
    fig.savefig(HERE / f"frame_{stem}.svg")
    # clear the footer text so the next save does not stack
    fig.texts.clear()

fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.6))
fig.text(0.99, 0.01, FOOT + "  Schematic algebra, not a recording.", ha="right", color="#9b2c2c", fontsize=8)
images = []
for i, s_value in enumerate(S):
    draw(axes, float(s_value))
    if i >= 40:
        axes[0].set_title(axes[0].get_title() + f"\nhold {i - 39} of 8", fontsize=9)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=80)
    buf.seek(0)
    images.append(Image.open(buf).convert("RGB"))
images[0].save(
    HERE / "anim_polarity.gif",
    save_all=True,
    append_images=images[1:],
    duration=125,
    loop=0,
    optimize=False,
    disposal=2,
)
plt.close(fig)
print("frames", wanted)
print("gif", len(images))
