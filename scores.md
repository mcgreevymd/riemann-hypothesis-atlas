# How the RH Atlas is ordered

**Label: Heuristic.** The scores below are judgment calls made by deterministic rules. They are shown component by component in every entry so that a reader can see exactly why a concept sits where it does, and disagree.

## The idea

The question that matters for the Riemann Hypothesis is not whether a structure is beautiful or true, but whether it can *tell ζ apart from functions that violate RH*. Such functions exist and behave like ζ in many ways: the Davenport–Heilbronn function has a functional equation of the same shape but zeros off the critical line, and “ghost” models insert hypothetical off-line zeros by hand. These serve as negative controls, in the way a diagnostic test is checked against healthy cases.

That suggests borrowing the language of diagnostic testing:

- **Sensitivity**: does the statement hold for ζ? (Is it necessary for RH, or implied by it?)
- **Specificity**: does the statement *fail* for the fakes? A statement that holds equally for Davenport–Heilbronn cannot be what forces RH.

A concept is a genuine RH-detector only if it scores high on both.

## The components

| Component | Rule |
|---|---|
| **Gap significance** | 1.0 if the concept *is* one of the ten missing pieces; 0.8 if it is directly related to one (a relation in either direction); 0.5 at distance 2 in the relation graph; 0.2 otherwise. The maximum over the ten missing pieces is used, and the nearest missing piece is named in the entry. |
| **Sensitivity** | 1.0 for Theorem, Cited, Numerical, Restatement and Open-target statements; 0.7 for Heuristic; 0.6 for Analogy. |
| **Specificity** | 1.0 if the concept is ghost-sensitive, is a restatement equivalent to RH, or is a missing piece; 0.05 if it is ghost-blind (known to hold for the fakes); 0.5 otherwise (not yet tested against the fakes). |
| **Tractability** | Numerical 0.7; Theorem / Cited 0.6; Heuristic 0.5; Analogy 0.4; Restatement 0.3; missing piece 0.25; other Open 0.2. |
| **Evidence** | Theorem / Cited / Restatement 1.0; Numerical 0.8; Heuristic 0.6; Analogy / Open 0.5; multiplied by 0.8 if the entry carries a “not verified” note. Shown for information; not part of the composite. |

## The formula

  **significance = gap significance × √(sensitivity · specificity)**

  **priority = 0.6 · significance + 0.4 · tractability**

The square root is a geometric mean: a concept with sensitivity 1 but specificity near 0 (true for ζ, but equally true for the fakes) gets almost no significance, however close it sits to a missing piece. The 0.6 / 0.4 weighting of significance against probability of progress is the convention used throughout the TAA programme.

**Rank** is the position in descending priority. Ties are broken by gap significance, then by the number of relations the concept has, then alphabetically by id, so the order is reproducible.

## The diagnostic quadrants

| | specificity ≥ 0.8 | specificity < 0.8 |
|---|---|---|
| **sensitivity ≥ 0.8** | **RH-sharp**: true for ζ and fails for the fakes | **True but ghost-blind / untested** |
| **sensitivity < 0.8** | **Sharp but interpretive** | **Background** |

The large “true but ghost-blind” corner is the atlas’s main lesson in one picture: most correct and elegant structure around ζ does not touch the sign that RH is about.

## Caveats

- One gap is scored per concept (the nearest missing piece). A concept that bears on several gaps is credited only for the closest.
- Specificity 0.5 means “not tested”, not “half specific”.
- Many entries tie at the same priority; within a tie the order carries no meaning beyond the stated tie-breaks.
- The scores will be revised as new results come in; overrides of individual values will be recorded in the changelog.
