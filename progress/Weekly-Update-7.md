# Weekly Progress Update #7

**Date:** April 22, 2026

## What did you accomplish this week?

Most of the week was spent going point-by-point through Shelley's
feedback on the Update #6 draft and reworking the paper around it. The
revised draft lives at
[`paper/Final Research Paper.pdf`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/Final%20Research%20Paper.pdf)
and the source is in
[`paper/paper.tex`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/paper.tex).

### Statistics, re-run at the participant level

Shelley asked whether the analysis was at the participant level
(n = 16) or the trial level (n = 144), and suggested reporting
Kendall's W / Cochran's Q alongside Friedman. Going back into
[`analysis/analyze_responses.py`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/analysis/analyze_responses.py)
I realized my Friedman implementation wasn't handling ties properly,
which matters a lot here because most participants were at 100% on
error bars and HOPs (so many tied ranks across conditions). Once I
fixed the tie handling and kept the analysis at the participant
level, the numbers changed in a meaningful way:

- **Accuracy (tie-corrected Friedman, participant level):**
  χ² = 6.50, df = 2, *p* = 0.039, Kendall's *W* = 0.203 (medium effect).
- **Response time:** χ² = 4.63, df = 2, *p* = 0.099, *W* = 0.145
  (small effect, not significant).
- **Post-hoc pairwise Wilcoxon signed-rank tests** on accuracy with
  Bonferroni α = 0.017: no pair crossed threshold
  (err vs vb *p* = 0.18, err vs hops *p* = 1.00, vb vs hops *p* = 0.10).

So the story is now honest: the omnibus accuracy test is significant
but barely, and no single pairwise comparison survives correction.
That is consistent with the ceiling Shelley flagged, and I say so
directly in Results and Discussion.

### Paper edits I made for each feedback point

- **Ceiling effect / high accuracy / small n.** Softened claims
  throughout. Added an explicit ceiling-effect paragraph in Results
  (§4.1) and again in Discussion (§5.1, §5.2). Conclusion now frames
  the findings as "pilot-scale, directional evidence" rather than a
  recommendation.
- **Exact p-value for Friedman.** All three Friedman tests now report
  p to three decimals (0.039 and 0.099 respectively) plus Kendall's W.
- **"Standardized interpretation task" was vague.** Introduction now
  lists the three concrete tasks (ranking, estimation, decision),
  gives the ground-truth rule for each, and notes the pre-specified
  ±2 mm tolerance up front.
- **Palmer Penguins justification.** Added a paragraph in Introduction
  explaining *why* Palmer Penguins is appropriate for an uncertainty
  study: the three species means (38.8, 47.5, 48.8 mm) are close
  enough that the Gentoo/Chinstrap comparison genuinely requires
  attention to uncertainty, but the ground truth is still unambiguous.
- **Hypotheses aligned with RQs.** Rewrote Hypotheses as H1/H2/H3,
  each explicitly mapped to RQ1/RQ2/RQ3, and each stating the measure
  (Brier score, proportion correct, per-trial completion time).
- **Pilot vs main study.** Added a short paragraph explaining exactly
  what changed between the n = 4 pilot (where HOPs looked slow and
  slightly worse) and the n = 16 main run (where HOPs came out on
  top): parallel task sets, arithmetic distractors between blocks,
  and the end-of-study recognition check.
- **"15 seconds additional" threshold.** Reframed as an a priori
  block-budget calculation: the 9-trial survey was advertised as
  ~10 min, which leaves ~3 min per 3-trial encoding block; a
  per-trial overhead above 15 s would push a distributional block
  past that budget and become a noticeable cost.
- **Static HOPs mentioned early.** Abstract, Introduction, and
  Stimuli all say "static HOPs grid" explicitly now. Added a
  reference to Hullman, Resnick & Adar 2015 ([PLoS ONE](https://doi.org/10.1371/journal.pone.0142444))
  to contrast static-grid HOPs with the original animated form.
- **Why general-purpose encodings matter.** Related Work §2.4 now
  explicitly says that domain-specific encodings (uncertainty tubes,
  DNN overlays) don't transfer to bar-chart-style group comparisons,
  and that practitioners reach for general-purpose encodings when
  their display is a handful of sample means.
- **"Three most common" → "three widely used".** Softened everywhere.
  Also added a sentence in Research Gap that explicitly defines what
  this paper means by *accuracy* and *calibration*.
- **Define "correct" per task.** Added bulleted definitions in
  Methodology: ranking = selected species matches the known target,
  estimation = within ±2 mm, decision = agree/disagree matches ground
  truth.
- **Participant-level vs trial-level.** Analysis section now states
  explicitly that all tests are at participant level (n = 16), with
  three paired values per participant per metric. Also reports the
  tie-correction bug fix.
- **±2 mm tolerance justification.** Chosen a priori to approximate
  one standard error of the species-level means at the dataset's
  sample sizes (n around 50 to 150 per species); tight enough to discriminate
  the three species, loose enough to absorb minor arithmetic.
- **Brier / Likert 0.2 to 1.0 issue.** Measures section now calls out
  both limitations Shelley raised: (a) Brier can't reach 0 for a
  wrong answer even at minimum confidence, (b) 5-step Likert is
  coarse. Added an **overconfidence index** (mean confidence/5 −
  mean accuracy) as a complementary metric. All three encodings came
  out slightly *under*confident (−0.050, −0.033, −0.100), which is
  what you'd expect against a ceiling.
- **Response-time scope.** Explicitly noted that response time is the
  interval between stimulus render and clicking Submit on a single
  trial. It does not include consent, demographics, instructions,
  arithmetic distractors, or survey setup.
- **IRB wording.** Rewrote from "classified as exempt from full IRB
  review" to "not submitted for IRB review … the exempt
  classification was self-assigned by the researcher rather than
  formally granted."
- **Outlier check.** New paragraph in §4.1 reporting the IQR-based
  outlier check on the violin/box ranking cell: three participants
  were flagged, and those three accounted for *every* ranking error
  in the violin/box condition. The other thirteen were at ceiling.
- **Richer discussion of why HOPs beat violin/box.** Discussion §5.1
  now offers four non-exclusive explanations: task-encoding
  alignment, density dominance in violin/box (density silhouette
  overwhelming the box-plot median), unfamiliarity-forces-attention
  for HOPs, and the obvious ceiling/task-simplicity caveat.
- **Response-time: anything to squeeze significance out of?** Honestly,
  no. Added a sentence noting the descriptive 15.6 s gap between
  error bars and violin/box, but did not run post-hocs because the
  omnibus wasn't significant and we didn't want to inflate Type I.
- **Threats to Validity expanded.** Added three new items: ceiling
  effect, sample composition (Bay Area / Silicon Valley peninsula
  social network with a high density of STEM grads and engineers
  (data literacy median 5/5), which almost certainly biases
  performance upward), and environmental inconsistency (Zoom/FaceTime
  proctoring vs self-guided).

### Other tangible artifacts

- Updated
  [`analysis/analyze_responses.py`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/analysis/analyze_responses.py)
  with: tie-corrected Friedman, Kendall's W, Wilcoxon signed-rank
  post-hoc, IQR-based outlier detection on the violin/box ranking
  cell, and an overconfidence-index column.
- Addressed the slide text-size feedback: bumped body text on the
  affected slides to at least 18 pt and re-exported
  [`presentation/CSCI 693 - Keynote.pdf`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/presentation/CSCI%20693%20-%20Keynote.pdf).
  The deck is also synced to the revised paper: Slide 3 and Slide 4
  now say "three widely used uncertainty encodings," Slide 12 reports
  the tie-corrected Friedman (χ² = 6.50, df = 2, *p* = 0.039,
  Kendall's *W* = 0.203), and Slide 14 reports the response-time
  Friedman (χ² = 4.63, df = 2, *p* = 0.099, *W* = 0.145).
- Submitted the final research paper PDF for the Update #7 deadline
  (same file as above:
  [`paper/Final Research Paper.pdf`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/Final%20Research%20Paper.pdf)).
- Recorded and submitted the pre-recorded research presentation video.
  Link: https://drive.google.com/file/d/1isnzGAjqixMhtMS279-TtbXtkO6o7hfw/view

## What is blocking your progress?

Nothing blocking.

## What is your plan for the next week?

- Incorporate anything useful I pick up from classmates'
  presentations into notes for future work.
