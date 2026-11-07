#!/usr/bin/env python3
"""Code-generated diagrams for atlas v1.19.

Geometric and typographic figures only. Text is SVG text (not outlined).
Outputs fig1_spring_balance.svg, fig2_boundary_topology.svg, fig3_architectures.svg.
RH is not proved. Numbers cited in fig. 1 are the K=8 reproduction only.
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
RED_BG = "#f8e8e6"
RULE = "#1c1915"
MUTED = "#4a453c"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def text(x, y, s, size=18, fill=INK, weight="400", anchor="start", style=""):
    fw = f' font-weight="{weight}"' if weight != "400" else ""
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
            f'font-family="DejaVu Serif, Liberation Serif, serif"'
            f'{fw} text-anchor="{anchor}"{style}>{esc(s)}</text>')


def lines(x, y, rows, size=18, fill=INK, leading=None, weight="400", anchor="start"):
    leading = leading or int(size * 1.35)
    return "\n".join(text(x, y + i * leading, s, size, fill, weight, anchor) for i, s in enumerate(rows))


def wrap(s, width):
    out, cur = [], ""
    for w in s.split():
        trial = w if not cur else cur + " " + w
        if len(trial) > width and cur:
            out.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        out.append(cur)
    return out


def svg_doc(w, h, title, desc, body):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{esc(title)}</title>
<desc id="desc">{esc(desc)}</desc>
<rect width="{w}" height="{h}" fill="{PAPER}"/>
{body}
</svg>
'''


def fig1():
    w, h = 680, 1160
    b = []
    b.append(f'<rect x="28" y="28" width="624" height="78" fill="{INK}"/>')
    b.append(lines(44, 58, ["The target is global spring domination."], 22, PAPER, weight="700"))
    b.append(lines(44, 88, ["A shrinking margin is a diagnostic, not a verdict."], 18, "#f3efe4"))
    body_y = 128
    b.append(lines(36, body_y, wrap(
        "On the pole annihilator the Weil form of ζ splits, exactly, as spring energy minus a counterterm. Every spring is nonnegative. Whether the springs win for every test function is the open comparison.",
        62), 18, leading=26))
    # identity card
    b.append(f'<rect x="28" y="250" width="624" height="168" rx="8" fill="#fff" stroke="{RULE}" stroke-width="1.5"/>')
    b.append(lines(44, 280, ["On E0, where the pole term is off"], 16, MUTED))
    b.append(lines(44, 318, ["W(F)  =  E_springs(F)  −  M ||F||²"], 24, INK, weight="700"))
    b.append(lines(44, 358, [
        "M = −K(0) + 2 Σ aₙ,    aₙ = Λ(n) · n^(−1/2)",
        "K(0) = Re ψ(1/4) − log π",
    ], 16, leading=24))
    # two columns
    b.append(f'<rect x="28" y="440" width="300" height="280" rx="8" fill="{GREEN_BG}" stroke="{GREEN}" stroke-width="1.5"/>')
    b.append(lines(44, 472, ["Springs, each ≥ 0"], 20, GREEN, weight="700"))
    b.append(lines(44, 508, [
        "Archimedean integral:",
        "k(a) ||F − T_a F||² da",
        "Each prime:",
        "aₙ ||F − T_{log n} F||²",
        "Both ≥ 0. M removes",
        "the diagonal.",
    ], 16, leading=22))
    # geometric bars
    b.append(f'<rect x="48" y="648" width="190" height="16" fill="{GREEN}"/>')
    b.append(f'<rect x="246" y="648" width="58" height="16" fill="{GREEN}" opacity="0.55"/>')
    b.append(text(48, 684, "archimedean", 14, GREEN))
    b.append(text(246, 684, "primes", 14, GREEN))

    b.append(f'<rect x="352" y="440" width="300" height="280" rx="8" fill="{AMBER_BG}" stroke="{AMBER}" stroke-width="1.5"/>')
    b.append(lines(368, 472, ["Net prime term, signed"], 20, AMBER, weight="700"))
    b.append(lines(368, 508, [
        "After M takes the diagonal,",
        "the quotient keeps",
        "−2 aₙ ρ(log n).",
        "ρ can help or hurt.",
        "That sign is not",
        "the spring energy.",
    ], 16, leading=22))
    # stem schematic
    axis_y = 648
    b.append(f'<line x1="380" y1="{axis_y}" x2="620" y2="{axis_y}" stroke="{INK}" stroke-width="1.5"/>')
    stems = [(430, 40, GREEN, "+"), (500, -36, RED, "−"), (575, 28, GREEN, "+")]
    for x, dy, col, lab in stems:
        y2 = axis_y - dy
        b.append(f'<line x1="{x}" y1="{axis_y}" x2="{x}" y2="{y2}" stroke="{col}" stroke-width="6" stroke-linecap="round"/>')
    b.append(text(500, 708, "up helps, down hurts", 14, MUTED, anchor="middle"))

    # near cancellation
    b.append(f'<rect x="28" y="742" width="624" height="270" rx="8" fill="#fff" stroke="{RULE}" stroke-width="1.5"/>')
    b.append(lines(44, 774, ["Near cancellation, one basis, not a certificate"], 20, weight="700"))
    b.append(lines(44, 810, wrap(
        "K = 8 exact-E0 Galerkin. A is the full width of the interval [−A/2, A/2]. Smallest Rayleigh quotient of W:",
        64), 16, leading=24))
    b.append(lines(44, 880, [
        "A = 1     0.06734",
        "A = 2     1.65 × 10⁻⁸",
    ], 22, leading=32, weight="700"))
    b.append(lines(44, 960, wrap(
        "Positive finite minima are upper bounds. They do not certify positivity, and they do not control K → ∞. K = 12 and K = 14 are a different legend.",
        68), 16, leading=24))
    b.append(lines(36, 1048, [
        "RH is not proved. No ample class, compatible J,",
        "or metric matching W is constructed.",
    ], 16, MUTED, leading=22))
    desc = ("On the pole annihilator, W equals nonnegative spring energy minus a counterterm M times the norm squared. "
            "That global comparison is the domination target and is open. Separately, after the counterterm, the prime contribution "
            "follows the sign of the autocorrelation. K=8 Galerkin minima 0.06734 at full width A=1 and 1.65e-8 at A=2 are upper bounds, not certificates. RH is not proved.")
    open(os.path.join(HERE, "fig1_spring_balance.svg"), "w", encoding="utf-8").write(
        svg_doc(w, h, "Spring energy versus the counterterm", desc, "\n".join(b)))


def hyperbola(c, x0, x1, n=80):
    pts = []
    for i in range(n):
        x = x0 + (x1 - x0) * i / (n - 1)
        if abs(x) < 1e-6:
            continue
        y = c / x
        pts.append((x, y))
    return pts


def fig2():
    w, h = 680, 1240
    b = []
    b.append(f'<rect x="28" y="24" width="624" height="78" fill="{BLUE}"/>')
    b.append(lines(44, 54, ["Two boundary numbers."], 24, PAPER, weight="700"))
    b.append(lines(44, 86, ["One hyperbolic form. Two different topologies."], 18, "#e7eef6"))

    # plane
    ox, oy, s = 340, 430, 78  # origin and scale: math (x,y) -> (ox+s*x, oy-s*y)
    def X(x): return ox + s * x
    def Y(y): return oy - s * y
    b.append(f'<rect x="48" y="124" width="584" height="470" fill="#fff" stroke="{RULE}" stroke-width="1.25"/>')
    # axes
    b.append(f'<line x1="{X(-2.6)}" y1="{Y(0)}" x2="{X(2.6)}" y2="{Y(0)}" stroke="{INK}" stroke-width="1.4"/>')
    b.append(f'<line x1="{X(0)}" y1="{Y(-2.5)}" x2="{X(0)}" y2="{Y(2.5)}" stroke="{INK}" stroke-width="1.4"/>')
    b.append(text(X(2.15), Y(0) - 10, "b₀ = f(0)", 16, INK, anchor="end"))
    b.append(text(X(0) - 8, Y(2.15), "b₁ = ∫ f", 16, INK, anchor="end"))
    # hyperbolas b0*b1 = ±1
    for c, col in ((1, BLUE), (-1, RED)):
        for branch in hyperbola(c, 0.38, 2.5):
            pass
        parts = []
        for x0, x1 in ((0.4, 2.45), (-2.45, -0.4)):
            pts = hyperbola(c, x0, x1, 60)
            d = "M " + " L ".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in pts if -2.55 <= y <= 2.55)
            parts.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2"/>')
        b.extend(parts)
    b.append(text(X(1.55), Y(0.78), "b₀ b₁ = 1", 15, BLUE))
    b.append(text(X(-1.7), Y(0.85), "b₀ b₁ = −1", 15, RED))
    # Fourier diagonal
    b.append(f'<line x1="{X(-2.2)}" y1="{Y(-2.2)}" x2="{X(2.2)}" y2="{Y(2.2)}" stroke="{INK}" stroke-width="1" stroke-dasharray="5 4"/>')
    b.append(text(X(1.15), Y(1.85), "Fourier swap", 15, INK))
    # discrete Fq samples on b0 b1 = 1: (q^{-n/2}, q^{n/2})
    q = 5
    for n in (-1, 0, 1):
        x = q ** (-n / 2)
        y = q ** (n / 2)
        if abs(x) < 2.4 and abs(y) < 2.4:
            b.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="5" fill="{AMBER}" stroke="{INK}"/>')
    b.append(text(56, 620, "Amber points: q = 5, n = −1, 0, 1. Discrete graph pairings.", 15, AMBER))
    b.append(text(56, 642, "Same diagonal law as scaling. Not Mellin integrals.", 15, AMBER))

    b.append(f'<rect x="28" y="668" width="624" height="150" rx="8" fill="{BLUE_BG}" stroke="{BLUE}"/>')
    b.append(lines(44, 698, ["Invariant Hermitian forms"], 20, BLUE, weight="700"))
    b.append(lines(44, 732, wrap(
        "The only Hermitian forms on these two numbers that stay fixed under every unitary scaling and under the Fourier swap are real multiples of the off-diagonal matrix. A nonzero multiple has signature (1, 1). The zero multiple is degenerate. The boundary does not supply a positive sign.",
        64), 16, leading=24))

    b.append(f'<rect x="28" y="836" width="300" height="230" rx="8" fill="#fff" stroke="{RULE}"/>')
    b.append(lines(44, 866, ["Global L²"], 20, weight="700"))
    b.append(lines(44, 900, wrap(
        "The two moment functionals are unbounded. E0 is dense. Smooth functions in E0 are not an L²-closed subspace. There is no global orthogonal projection onto a pole-free subspace.",
        30), 16, leading=24))
    b.append(f'<rect x="352" y="836" width="300" height="230" rx="8" fill="#fff" stroke="{RULE}"/>')
    b.append(lines(368, 866, ["One fixed window"], 20, weight="700"))
    b.append(lines(368, 900, wrap(
        "On a finite interval both exponentials are square-integrable, so the kernel is closed and has codimension 2. That projection depends on the window. It is not translation-covariant.",
        30), 16, leading=24))
    b.append(lines(36, 1090, wrap(
        "A is the full width of [−A/2, A/2]. In the boundary checks, L is the half-width of [−L, L]. Read the interval. Prior: the operator d²/du² − 1/4 sends smooth functions of compact support bijectively onto E0 in that class (Connes–Consani 2021, Lemma 3.3).",
        70), 16, leading=24))
    b.append(lines(36, 1200, ["RH is not proved. The pole plane as an II₁,₁ lattice is an analogy only."], 16, MUTED))
    desc = ("Boundary data (f(0), integral of f) carry a hyperbolic Hermitian form of signature (1,1), or zero. "
            "Globally E0 is dense in L2 and not closed. On a fixed window the kernel is closed of codimension 2. "
            "Finite-field points on the same hyperbola are discrete samples, not Mellin integrals. RH is not proved.")
    open(os.path.join(HERE, "fig2_boundary_topology.svg"), "w", encoding="utf-8").write(
        svg_doc(w, h, "Boundary form and two topologies", desc, "\n".join(b)))


def card(b, x, y, w, hgt, title, rows, accent):
    b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{hgt}" rx="8" fill="#fff" stroke="{accent}" stroke-width="2"/>')
    b.append(f'<rect x="{x}" y="{y}" width="8" height="{hgt}" fill="{accent}"/>')
    b.append(lines(x + 24, y + 32, [title], 20, accent, weight="700"))
    b.append(lines(x + 24, y + 64, rows, 16, leading=23))


def fig3():
    w, h = 680, 1240
    b = []
    b.append(f'<rect x="28" y="24" width="624" height="78" fill="{INK}"/>')
    b.append(lines(44, 54, ["Related architectures."], 24, PAPER, weight="700"))
    b.append(lines(44, 86, ["Not one identity."], 22, "#f3efe4"))
    b.append(f'<rect x="28" y="120" width="624" height="110" rx="8" fill="{RED_BG}" stroke="{RED}"/>')
    b.append(lines(44, 150, ["Not a theorem:"], 16, RED, weight="700"))
    b.append(lines(44, 180, ["“Every mechanism is  Q = ‖Φ‖²  +  indefinite boundary.”"], 18, RED, weight="700"))
    b.append(lines(44, 208, ["A family resemblance is not a universal formula."], 16, RED))

    # four small geometric marks + text
    # 1 positive ellipse
    b.append(f'<rect x="28" y="250" width="624" height="168" rx="8" fill="#fff" stroke="{GREEN}" stroke-width="1.5"/>')
    b.append(f'<ellipse cx="92" cy="334" rx="48" ry="32" fill="none" stroke="{GREEN}" stroke-width="2.5"/>')
    b.append(lines(160, 286, ["Robertson–Schrödinger"], 20, GREEN, weight="700"))
    b.append(lines(160, 318, wrap(
        "A positive Gram of a state or a weight. The commutator is optional: a commutative positive functional can be independent. W is unbounded, so the object is a weight on test functions, not a normalized state on bounded translations.",
        48), 16, leading=23))

    b.append(f'<rect x="28" y="434" width="624" height="168" rx="8" fill="#fff" stroke="{BLUE}" stroke-width="1.5"/>')
    # ASD icon: square and a diagonal
    b.append(f'<rect x="60" y="478" width="64" height="64" fill="none" stroke="{BLUE}" stroke-width="2"/>')
    b.append(f'<line x1="60" y1="542" x2="124" y2="478" stroke="{BLUE}" stroke-width="2"/>')
    b.append(text(92, 560, "ASD", 13, BLUE, "700", "middle"))
    b.append(lines(160, 470, ["BPS, on a complex surface"], 20, BLUE, weight="700"))
    b.append(lines(160, 502, wrap(
        "The norm is the metric square. Primitive real (1,1) forms on a Kähler surface are anti-self-dual. Topological charge labels a sector. This is Riemannian geometry of a complex surface.",
        48), 16, leading=23))

    b.append(f'<rect x="28" y="618" width="624" height="168" rx="8" fill="#fff" stroke="{AMBER}" stroke-width="1.5"/>')
    # inertia icon + - 
    b.append(text(78, 690, "+", 28, GREEN, "700", "middle"))
    b.append(text(78, 724, "− − −", 18, RED, "700", "middle"))
    b.append(lines(160, 654, ["Hodge index, over a finite field"], 20, AMBER, weight="700"))
    b.append(lines(160, 686, wrap(
        "The intersection form on an algebraic surface. Inertia sees the sign. A positive determinant can belong to a negative-definite block. Not the same object as the Kähler anti-self-dual equation.",
        48), 16, leading=23))

    b.append(f'<rect x="28" y="802" width="624" height="168" rx="8" fill="#fff" stroke="{INK}" stroke-width="1.5"/>')
    b.append(f'<line x1="56" y1="886" x2="130" y2="886" stroke="{INK}" stroke-width="1.5" marker-end="url(#arr)"/>')
    b.append(text(70, 870, "quotient", 14, INK, anchor="start"))
    b.append(lines(160, 838, ["No-ghost"], 20, weight="700"))
    b.append(lines(160, 870, wrap(
        "A quotient. Positivity is carried in from an already positive transverse space. Calling the pole plane an II₁,₁ lattice is an analogy. No arithmetic lattice is constructed.",
        48), 16, leading=23))

    b.append(lines(36, 1000, wrap(
        "Connes 1999: in characteristic p the trace comparison is positive because of projection order. The number-field statement is equivalent to RH. Subtraction alone is not a sign. Semilocal Sonin is one candidate energy condition, not the unique one.",
        70), 16, leading=24))
    b.append(lines(36, 1100, wrap(
        "The sought arithmetic correspondence geometry — a polarization whose compatible metric reproduces W — is not built. Rank 1 is still that missing J. RH is not proved.",
        70), 16, leading=24))
    # arrow marker
    marker = '''<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
<path d="M0,0 L6,3 L0,6 Z" fill="#1c1915"/></marker></defs>'''
    desc = ("Robertson–Schrödinger, BPS on a Kähler surface, the Hodge index over a finite field, and the no-ghost quotient are related architectures, not the single identity Q = norm squared plus an indefinite boundary. "
            "The arithmetic polarization that would match W is not constructed. RH is not proved.")
    open(os.path.join(HERE, "fig3_architectures.svg"), "w", encoding="utf-8").write(
        svg_doc(w, h, "Related positivity architectures", desc, marker + "\n".join(b)))


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("wrote three svg")
