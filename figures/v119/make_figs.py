#!/usr/bin/env python3
"""Diagrams for atlas v1.19. Text is SVG text. RH is not proved.

Figure 1 draws the window couplings and the two reproduced K=8 minima.
The counterterm is the finite M_N, N >= exp(A). No trend line is drawn.
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INK = "#1c1915"
PAPER = "#f7f4ee"
GREEN = "#145c3a"
GREEN_BG = "#e5f2ea"
AMBER = "#7a4a06"
AMBER_BG = "#f8efd8"
BLUE = "#163a66"
BLUE_BG = "#e7eef6"
RED = "#7a2e2e"
RULE = "#1c1915"
MUTED = "#4a453c"
FONT = "DejaVu Serif, Liberation Serif, serif"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def text(x, y, s, size=18, fill=INK, weight="400", anchor="start"):
    fw = f' font-weight="{weight}"' if weight != "400" else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" '
            f'font-family="{FONT}"{fw} text-anchor="{anchor}">{esc(s)}</text>')


def svg_doc(w, h, title, desc, body):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{esc(title)}</title>
<desc id="desc">{esc(desc)}</desc>
<rect width="{w}" height="{h}" fill="{PAPER}"/>
{body}
</svg>
'''


def panel(b, x, y, w, h, fill, stroke):
    b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')


def fig1():
    w, h = 720, 1280
    b = []
    b.append(f'<rect x="24" y="20" width="672" height="64" fill="{INK}"/>')
    b.append(text(40, 48, "Springs on a window, and two computed margins", 22, PAPER, "700"))
    b.append(text(40, 72, "The counterterm is finite. The points are the data.", 16, "#f3efe4"))

    # --- coupling diagram ---
    panel(b, 24, 100, 672, 250, "#fff", RULE)
    b.append(text(40, 128, "Couplings inside a window of full width A", 18, INK, "700"))
    y0 = 230
    xs = [70, 155, 240, 325, 410, 495, 580]
    b.append(f'<line x1="60" y1="{y0}" x2="640" y2="{y0}" stroke="{INK}" stroke-width="2"/>')
    b.append(text(60, y0 + 22, "−A/2", 14, MUTED))
    b.append(text(600, y0 + 22, "A/2", 14, MUTED))
    # archimedean density as a band under the line
    b.append(f'<rect x="70" y="{y0 + 28}" width="510" height="22" fill="{GREEN}" opacity="0.28"/>')
    b.append(text(70, y0 + 68, "archimedean density k(a) ≥ 0 along the window", 14, GREEN))
    # prime couplings: arcs of two lags
    def arc(x1, x2, lift, color):
        mid = (x1 + x2) / 2
        b.append(f'<path d="M {x1:.1f} {y0} Q {mid:.1f} {y0 - lift:.1f} {x2:.1f} {y0}" fill="none" stroke="{color}" stroke-width="2.2"/>')
    for i in range(len(xs) - 2):
        arc(xs[i], xs[i + 2], 36, GREEN)
    for i in range(len(xs) - 3):
        arc(xs[i], xs[i + 3], 62, "#2e7d4f")
    for x in xs:
        b.append(f'<circle cx="{x}" cy="{y0}" r="5" fill="{INK}"/>')
    b.append(text(70, y0 - 78, "arcs: prime springs aₙ ||F − T_{log n} F||² ≥ 0", 14, GREEN))
    b.append(text(430, 156, "schematic of the lags, not a mode", 14, MUTED))

    # --- identity ---
    panel(b, 24, 366, 672, 210, GREEN_BG, GREEN)
    b.append(text(40, 396, "Finite cutoff. The sum over all n would diverge.", 18, GREEN, "700"))
    for i, line in enumerate([
        "F is zero outside the window. Take N ≥ exp(A).",
        "W(F) = P(F) + E_N(F) − M_N ||F||²",
        "M_N = −K(0) + 2 Σ_{n≤N} aₙ",
        "E_N = ∫ k(a) ||F−T_a F||² da + Σ_{n≤N} aₙ ||F−T_{log n} F||²",
        "Pieces of E_N are ≥ 0. Terms past the window cancel.",
    ]):
        b.append(text(40, 428 + i * 26, line, 16 if i != 1 else 18, INK, "700" if i == 1 else "400"))

    # --- two points ---
    panel(b, 24, 592, 672, 430, "#fff", RULE)
    b.append(text(40, 624, "K = 8, exact E0. Two minima, no fitted curve.", 18, INK, "700"))
    # axes
    left, right, top, bot = 110, 640, 680, 900
    b.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bot}" stroke="{INK}" stroke-width="1.5"/>')
    b.append(f'<line x1="{left}" y1="{bot}" x2="{right}" y2="{bot}" stroke="{INK}" stroke-width="1.5"/>')
    # log10 from 0 down to -8
    def Y(logv):
        return top + (0 - logv) / 8 * (bot - top)
    def X(A):
        return left + (A - 0.6) / 1.8 * (right - left)
    for tick in (0, -2, -4, -6, -8):
        yy = Y(tick)
        b.append(f'<line x1="{left - 6}" y1="{yy:.1f}" x2="{left}" y2="{yy:.1f}" stroke="{INK}"/>')
        b.append(text(left - 12, yy + 5, str(tick), 14, MUTED, anchor="end"))
    for A in (1, 2):
        xx = X(A)
        b.append(f'<line x1="{xx:.1f}" y1="{bot}" x2="{xx:.1f}" y2="{bot + 6}" stroke="{INK}"/>')
        b.append(text(xx, bot + 24, f"A = {A}", 16, INK, "700", "middle"))
    pts = [(1, 0.0673395762411, "0.06734"), (2, 1.65055568024e-8, "1.65×10⁻⁸")]
    for A, mu, label in pts:
        xx, yy = X(A), Y(math.log10(mu))
        b.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="7" fill="{INK}"/>')
        b.append(text(xx + 14, yy - 10, label, 16, INK, "700"))
    b.append(text(left, top - 16, "log10 of the smallest Rayleigh quotient", 14, MUTED))
    b.append(text(40, 960, "Full width A of the interval [−A/2, A/2].", 16, INK))
    b.append(text(40, 986, "Positive values are upper bounds, not a certificate.", 16, INK))

    # signed reminder, one line, not a second essay
    panel(b, 24, 1040, 672, 120, AMBER_BG, AMBER)
    b.append(text(40, 1072, "After M_N takes the diagonal, the prime term is signed.", 18, AMBER, "700"))
    b.append(text(40, 1104, "−2 aₙ ρ(log n) helps or hurts with ρ.", 16, INK))
    b.append(text(40, 1130, "The spring energy E_N stays nonnegative either way.", 16, INK))

    b.append(text(40, 1200, "On E0 the pole term is off, so domination of M_N by E_N is the target.", 16, INK))
    b.append(text(40, 1232, "RH is not proved. No J or metric matching W is constructed.", 16, MUTED))

    desc = ("Window couplings: archimedean density and prime springs, each nonnegative. "
            "Identity uses finite M_N = -K(0)+2 sum_{n<=N} a_n with N at least exp(A), "
            "F zero outside the window, and tails past the window cancelling. "
            "Two K=8 exact-E0 minima: 0.06734 at full width A=1 and 1.65e-8 at A=2. "
            "No curve is drawn. Upper bounds, not a certificate. RH is not proved.")
    open(os.path.join(HERE, "fig1_spring_balance.svg"), "w", encoding="utf-8").write(
        svg_doc(w, h, "Finite spring energy and two Galerkin margins", desc, "\n".join(b)))


def fig2():
    w, h = 720, 1320
    b = []
    b.append(f'<rect x="24" y="18" width="672" height="58" fill="{BLUE}"/>')
    b.append(text(40, 54, "Two function spaces, one smearing map", 22, PAPER, "700"))

    # Tate box
    panel(b, 24, 92, 300, 168, BLUE_BG, BLUE)
    b.append(text(40, 122, "Tate data", 18, BLUE, "700"))
    for i, line in enumerate([
        "Schwartz–Bruhat f",
        "b(f) = (f(0), ∫ f)",
        "Fourier swaps them.",
        "Scaling: |a|^(∓1/2).",
    ]):
        b.append(text(40, 150 + i * 24, line, 15, INK))

    # arrow
    b.append(f'<line x1="336" y1="170" x2="384" y2="170" stroke="{INK}" stroke-width="1.6" marker-end="url(#arr)"/>')
    b.append(text(360, 158, "Θ_F", 14, INK, "700", "middle"))

    # log-line box — height fits every line
    panel(b, 396, 92, 300, 168, "#fff", RULE)
    b.append(text(412, 122, "Log-line test F", 18, INK, "700"))
    for i, line in enumerate([
        "ev₀ = ∫ F e^(−u/2) du",
        "ev₁ = ∫ F e^(u/2) du",
        "E0: both moments zero.",
        "Not the same as b(f).",
    ]):
        b.append(text(412, 150 + i * 24, line, 15, INK))

    # smearing line, its own band so it cannot collide
    panel(b, 24, 274, 672, 72, "#fff", RULE)
    b.append(text(40, 304, "Smearing links them: b(Θ_F f) = diag(ev₀ F, ev₁ F) b(f).", 16, INK))
    b.append(text(40, 328, "Θ_F preserves the kernel of b for every f precisely when F is in E0.", 15, MUTED))

    # hyperbola of b, first quadrant, n = 0,1,2
    panel(b, 24, 360, 420, 430, "#fff", RULE)
    b.append(text(40, 388, "b-plane, form b₀ b₁", 16, BLUE, "700"))
    ox, oy, s = 70, 740, 62
    def X(x): return ox + s * x
    def Y(y): return oy - s * y
    # axes 0 to 5.4
    b.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(5.3):.1f}" y2="{Y(0):.1f}" stroke="{INK}" stroke-width="1.4"/>')
    b.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(0):.1f}" y2="{Y(5.2):.1f}" stroke="{INK}" stroke-width="1.4"/>')
    b.append(text(X(4.6), Y(0) + 18, "b₀ = f(0)", 13, MUTED))
    b.append(text(X(1.15), Y(5.05), "b₁ = ∫ f", 13, INK))
    pts = []
    for i in range(80):
        x = 0.22 + (5.1 - 0.22) * i / 79
        y = 1 / x
        if y <= 5.15:
            pts.append((X(x), Y(y)))
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    b.append(f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="2"/>')
    b.append(text(X(1.6), Y(0.85), "b₀ b₁ = 1", 14, BLUE))
    q = 5.0
    for n in (0, 1, 2):
        bx, by = q ** (-n / 2), q ** (n / 2)
        b.append(f'<circle cx="{X(bx):.1f}" cy="{Y(by):.1f}" r="5.5" fill="{AMBER}" stroke="{INK}"/>')
        dy = 16 if n == 2 else -8
        b.append(text(X(bx) + 10, Y(by) + dy, f"n={n}", 13, AMBER, "700"))
    b.append(text(40, 768, "q = 5, Frobenius iterates n = 0, 1, 2.", 14, AMBER))

    # signature box sized to its lines
    sig_lines = [
        "Invariant forms on b",
        "are real multiples of",
        "the off-diagonal matrix.",
        "Nonzero: signature (1, 1).",
        "Zero multiple: degenerate.",
        "This boundary does not",
        "give a positive sign.",
    ]
    sig_top, sig_h = 360, 36 + 24 * len(sig_lines) + 20
    panel(b, 460, sig_top, 236, sig_h, BLUE_BG, BLUE)
    for i, line in enumerate(sig_lines):
        weight = "700" if i == 0 else "400"
        b.append(text(476, sig_top + 32 + i * 24, line, 15, BLUE if i == 0 else INK, weight))

    # two topology panels, explicit lines, boxes tall enough
    g_lines = [
        "Global L² of the log line",
        "ev₀ and ev₁ are unbounded",
        "on L²(du), so E0 is dense.",
        "Smooth E0 is not closed.",
        "No global orthogonal",
        "projection removes them.",
        "These moments are not b(f).",
    ]
    w_lines = [
        "One fixed log window",
        "e^(±u/2) lie in L² there,",
        "so the kernel is closed",
        "and has codimension 2.",
        "The projection depends",
        "on that window.",
    ]
    row = 860
    gh = 28 + 22 * len(g_lines) + 16
    wh = 28 + 22 * len(w_lines) + 16
    panel(b, 24, row, 330, gh, "#fff", RULE)
    panel(b, 366, row, 330, max(gh, wh), "#fff", RULE)
    for i, line in enumerate(g_lines):
        b.append(text(40, row + 32 + i * 22, line, 15, INK, "700" if i == 0 else "400"))
    for i, line in enumerate(w_lines):
        b.append(text(382, row + 32 + i * 22, line, 15, INK, "700" if i == 0 else "400"))

    foot = row + max(gh, wh) + 36
    b.append(text(40, foot, "A is the full width of [−A/2, A/2]. In the boundary", 15, MUTED))
    b.append(text(40, foot + 22, "checks, L is the half-width of [−L, L].", 15, MUTED))
    b.append(text(40, foot + 48, "RH is not proved. II₁,₁ for the pole plane is an analogy.", 15, MUTED))

    desc = ("Tate boundary values b(f)=(f(0), integral f) and log-line moments ev0, ev1 are different. "
            "Smearing links them. The invariant form on b is hyperbolic or zero. "
            "Amber points are q=5 Frobenius iterates n=0,1,2, not an inverse graph and not Mellin moments. "
            "On the log line, E0 is dense in L2; on one window it is closed of codimension 2. RH is not proved.")
    marker = '''<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#1c1915"/></marker></defs>'''
    open(os.path.join(HERE, "fig2_boundary_topology.svg"), "w", encoding="utf-8").write(
        svg_doc(w, h, "Tate boundary and log-line moments", desc, marker + "\n".join(b)))


def fig3():
    w, h = 720, 1180
    b = []
    b.append(f'<rect x="24" y="18" width="672" height="58" fill="{INK}"/>')
    b.append(text(40, 54, "Where a sign would have to be carried from", 22, PAPER, "700"))

    # central target
    panel(b, 210, 96, 300, 88, AMBER_BG, AMBER)
    b.append(text(360, 130, "Sign for W", 20, AMBER, "700", "middle"))
    b.append(text(360, 158, "not constructed", 16, INK, "400", "middle"))

    sources = [
        (90, GREEN, "RS Gram", "state or weight"),
        (250, BLUE, "BPS norm", "Kähler metric"),
        (410, AMBER, "Hodge index", "finite field"),
        (570, INK, "No-ghost", "transverse norm"),
    ]
    for x, col, title, sub in sources:
        panel(b, x - 70, 230, 150, 78, "#fff", col)
        b.append(text(x + 5, 262, title, 16, col, "700", "middle"))
        b.append(text(x + 5, 286, sub, 13, INK, "400", "middle"))
        # arrow up toward the target box (target spans x 210-510, y 96-184)
        b.append(f'<line x1="{x + 5}" y1="230" x2="360" y2="184" stroke="{col}" stroke-width="1.6" marker-end="url(#arr)"/>')

    # geometric icons under the four labels, in a linked row
    # 1 ellipse
    b.append(f'<ellipse cx="100" cy="390" rx="36" ry="22" fill="none" stroke="{GREEN}" stroke-width="2.4"/>')
    # 2 ASD square
    b.append(f'<rect x="232" y="364" width="48" height="48" fill="none" stroke="{BLUE}" stroke-width="2.2"/>')
    b.append(f'<line x1="232" y1="412" x2="280" y2="364" stroke="{BLUE}" stroke-width="2"/>')
    # 3 inertia
    b.append(text(425, 386, "+", 22, GREEN, "700", "middle"))
    b.append(text(425, 412, "− − −", 16, RED, "700", "middle"))
    # 4 quotient arrow
    b.append(f'<line x1="540" y1="392" x2="620" y2="392" stroke="{INK}" stroke-width="2" marker-end="url(#arr)"/>')
    b.append(text(580, 380, "quotient", 13, INK, "400", "middle"))

    # explanations sized as full-width bands, lines hand-broken
    bands = [
        (GREEN, GREEN_BG, "Robertson–Schrödinger", [
            "The Gram is positive because a state or a weight is positive.",
            "A generic positive Gram need not include a commutator.",
            "A nonzero RS commutator needs noncommuting operators.",
            "W is a target for such a weight, not a weight already.",
        ]),
        (BLUE, "#fff", "BPS and the finite-field Hodge index", [
            "On a Kähler surface the norm is the metric square.",
            "Primitive real (1,1) forms there are anti-self-dual.",
            "Over a finite field the sign is an intersection form.",
            "Inertia sees it. Those are two geometries, linked here only as cousins.",
        ]),
        (INK, "#fff", "No-ghost", [
            "The quotient carries in a transverse norm that is already positive.",
            "It does not create the sign. The pole plane as a lattice is an analogy.",
        ]),
    ]
    y = 450
    for col, fill, title, rows in bands:
        bh = 36 + 24 * len(rows) + 18
        panel(b, 24, y, 672, bh, fill, col)
        b.append(text(40, y + 28, title, 17, col, "700"))
        for i, line in enumerate(rows):
            b.append(text(40, y + 56 + i * 24, line, 15, INK))
        y += bh + 14

    b.append(text(40, y + 8, "Connes 1999: the global trace formula matches RH for every", 15, INK))
    b.append(text(40, y + 28, "Grössencharakter L-function, not for ζ alone.", 15, INK))
    b.append(text(40, y + 48, "In char. p, Δ subtracts Q′ from S. Order gives the sign.", 15, INK))
    b.append(text(40, y + 72, "Rank 1 is still the missing compatible J. RH is not proved.", 16, MUTED))

    desc = ("Four architectures point at a sign for W that is not constructed: "
            "a Robertson-Schrodinger Gram of a positive state or weight "
            "(a commutator is optional for a generic positive Gram, and required for a nonzero RS term), "
            "a BPS metric square on a Kaehler surface, the finite-field Hodge index, "
            "and a no-ghost quotient. W is not asserted to be a positive weight. RH is not proved.")
    marker = '''<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#1c1915"/></marker></defs>'''
    # height must include the last caption
    h = y + 100
    open(os.path.join(HERE, "fig3_architectures.svg"), "w", encoding="utf-8").write(
        svg_doc(w, h, "Architectures linked to a missing sign", desc, marker + "\n".join(b)))


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("wrote three svg")
