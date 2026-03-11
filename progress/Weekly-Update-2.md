# Weekly Progress Update #2

**Date:** March 11, 2026
**Course:** Research Methods - 693

---

## 1. What did you accomplish towards your research over the past week?

- Addressed Professor Wong's feedback from Update #1: added raw data source link, dataset version (palmerpenguins v0.1.0), and the derivation script to the `data/` folder.
- Built `stimuli/generate_stimuli.py`, which reads the raw penguins data and produces all three chart types that participants will see in the study:
  - Error bar chart (mean + 95% CI) — the baseline condition
  - Violin + box plot overlay — distributional summary condition
  - Static HOPs grid (20 bootstrap draws) — hypothetical outcome plots condition
- Saved output figures to `stimuli/figures/` and added a README explaining each one.

**Links to updates:**
- [Data README with source and methodology](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/data/README.md)
- [Stimuli generation script](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/stimuli/generate_stimuli.py)
- [Error bar figure](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/stimuli/figures/errorbar.png)
- [Violin/box figure](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/stimuli/figures/violin_box.png)
- [HOPs grid figure](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/stimuli/figures/hops_grid.png)

---

## 2. What (if anything) is blocking your progress?

The HOPs condition ideally uses animation, but for a static survey that might be tricky. Right now I'm using a grid of 20 bootstrap draws as a stand-in. I need to decide if that's good enough or if I should build an animated version.

---

## 3. What is your plan for the next week?

- Design the study tasks: define trial questions (ranking, estimation, decision selection) and the counterbalancing scheme.
- Start building the survey instrument — leaning toward a simple web page so I can embed the animated HOPs later if needed.
- Write up the study protocol (consent form, instructions, trial flow).
