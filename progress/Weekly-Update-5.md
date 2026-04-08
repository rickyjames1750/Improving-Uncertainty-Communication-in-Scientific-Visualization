# Weekly Progress Update #5

**Date:** April 8, 2026

## What did you accomplish this week?

- Revised the survey instrument based on Shelley's Update #4 feedback about
  task carryover. Three changes:
  1. **Parallel question sets** — instead of asking the same three questions
     for every encoding, each block now gets structurally identical but
     content-different questions (different species, different comparisons).
     Block 1 asks about the largest mean / Chinstrap estimation / Gentoo-vs-
     Chinstrap claim. Block 2 asks about the smallest mean / Gentoo estimation
     / Adelie-vs-Gentoo claim. Block 3 asks about the second-largest mean /
     Adelie estimation / Chinstrap-vs-Gentoo claim. This way a participant
     can't just recall their earlier answer.
  2. **Distractor task between blocks** — a quick arithmetic problem appears
     between encoding blocks to break short-term retention.
  3. **Recognition check** — added a question at the end asking whether
     participants felt they remembered answers from earlier charts. This
     gives us self-reported data on carryover even if it's still present.
- Opened data collection to 16 participants after deploying the updated
  survey. Walked most through it over FaceTime or Zoom — a few used the
  hosted link on their own. Saved the aggregated responses in
  `study/responses.csv`.
- Drafted the Introduction and Background sections of the paper in
  `paper/sections/introduction.md`. Covers motivation, research questions,
  hypotheses, the uncertainty pipeline (Mehta), encoding frameworks (Petek),
  modality comparisons (Stokes), and the applied sci-vis work (Saklani, Li).
  Tried to structure it so it flows from the broad problem down to the
  specific gap.

**Updated files/folders:**
- [`study/survey.html`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/study/survey.html) (updated — parallel tasks, distractors, recognition check)
- [`study/responses.csv`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/study/responses.csv) (new — 144 trial rows, 16 participants)
- [`paper/sections/introduction.md`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/sections/introduction.md) (new)

## What is blocking your progress?

Ended up with 16 participants instead of the 24 I originally planned. Recruiting
for a class project is harder than expected — most of my sample is friends
willing to hop on a call. 16 gives me about 2–3 per counterbalancing group,
which is workable for a within-subjects design where each person contributes
9 data points.

## What is your plan for the next week?

- Close data collection and clean the dataset (drop incomplete rows, check
  for obvious random clicking).
- Draft the Methods section of the paper — participants, materials, procedure,
  measures, analysis plan.
- Start writing analysis code to compute accuracy, calibration, and timing
  per condition. Will also include a block-position analysis to check for
  order effects — even with the parallel questions and distractors, it's
  worth checking if block 1 vs. 3 performance differs.
