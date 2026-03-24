# Study Tasks

Each participant completes **9 trials** (3 encoding types x 3 task types),
presented in counterbalanced order.

## Encoding Conditions

| ID | Encoding | File |
|----|----------|------|
| E1 | Error bars (mean + 95% CI) | `stimuli/figures/errorbar.png` |
| E2 | Violin + box plot | `stimuli/figures/violin_box.png` |
| E3 | HOPs grid (20 bootstrap draws) | `stimuli/figures/hops_grid.png` |

## Task Types

### T1 — Ranking
> "Based on this chart, which species has the **largest** mean bill length?"
>
> Options: Adelie / Chinstrap / Gentoo
>
> Follow-up: "How confident are you?" (1 = not at all, 5 = very confident)

### T2 — Estimation
> "Estimate the mean bill length for Chinstrap penguins (in mm)."
>
> Free-text numeric entry.
>
> Follow-up: "How confident are you?" (1-5)

### T3 — Decision
> "A researcher claims Gentoo and Chinstrap penguins have the same mean
> bill length. Based on this chart, do you **agree** or **disagree**?"
>
> Options: Agree / Disagree
>
> Follow-up: "How confident are you?" (1-5)

## Counterbalancing

Latin square with 6 orderings (3! permutations of encoding). Each participant
is randomly assigned to one ordering. Task type order within each encoding
block is fixed (T1, T2, T3) to keep things simple.

| Group | Block 1 | Block 2 | Block 3 |
|-------|---------|---------|---------|
| A | E1 | E2 | E3 |
| B | E1 | E3 | E2 |
| C | E2 | E1 | E3 |
| D | E2 | E3 | E1 |
| E | E3 | E1 | E2 |
| F | E3 | E2 | E1 |

## Dependent Variables

- **Decision accuracy** (T1: correct species; T2: within 2mm of true mean;
  T3: correct agree/disagree)
- **Confidence** (1-5 Likert after each task)
- **Task completion time** (seconds, from stimulus display to response submit)
