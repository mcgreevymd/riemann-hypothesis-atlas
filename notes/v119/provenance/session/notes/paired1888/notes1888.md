# paired1888 — pole-respecting conjugate pair via L = ∂² − ¼ (scratch; RH is not proved)
J. W. McGreevy; work by Grok Bot. Read-only on atlas/STATE/lemmas. Verified in verify1888.py (sympy + grid).
THM (elementary): L: C_c^∞(R) → E0 = {∫f e^{±u/2}=0} bijective; supp L^{-1}f ⊂ hull(supp f); L^{-1}f = −e^{-|u|/2} * f.
 Fourier: L ↔ s(s−1), s=½+iξ (Riemann-ξ pole factor). Unique translation-invariant bijection up to c·T_a (Paley–Wiener + Hadamard).
THM: Q0 = LQL^{-1} = Q + 2∂L^{-1} = u + (sgn·e^{-|·|/2}) * , D0 = D; preserve E0; [Q0,D] = iħ; symmetric for G0 = <L^{-1}·,L^{-1}·>, not for L².
 G0 symbol (ξ²+¼)^{-2}; translation-invariant; (E0,G0)-completion ≅ L² unitarily (Stone–von Neumann: Schrödinger rep relabelled).
THM: L W L kills pole kernel (L cosh((x−y)/2)=0); W|E0 ≥ 0 ⇔ LWL ≥ 0 on C_c^∞ (unconstrained, window-preserving). Equivalent to Weil on ker P, NOT a proof.
Kähler: X⊕X*, ω=<q,p'>−<q',p>, J(q,p)=(−G^{-1}p,Gq), g=G⊕G^{-1}=ω(·,J·); pure Gaussian V=(ħ/2)g, V+iħΩ/2 ≥0 rank n; RS saturates on Riesz pairs p=Gq.
ANALOGY/PROPOSAL: Q_F = F Q F^{-1}, correction −[Q,F]F^{-1} has Mellin symbol ∓F'/F: F=s(s−1) rigorous; Γ, ζ formal (Z Q Z^{-1} = Q − ΣΛ(n)n^{-1/2}T_{log n});
 F=ξ: correction symbol Σ_ρ 1/(s−ρ) — explicit formula as equality of position corrections.
Prior art: keyword search STATE/NOTATION/atlas v1.18 found no ∂²−¼ bijection; s(s−1) is classical (NOTATION ξ; atlas pole_plane r145, no_ghost_template r949).
