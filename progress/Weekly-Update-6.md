# Weekly Progress Update #6

**Date:** April 15, 2026

## What did you accomplish this week?

- Addressed Shelley's feedback on the Introduction draft:
  - Sharpened the hypothesis to distinguish between violin/box and HOPs
    (violin/box expected to yield better calibration because the density shape
    is easier to reason about; HOPs expected to produce higher raw accuracy
    because each draw makes between-group differences visually explicit).
  - Defined "prohibitive time cost": we now set a concrete threshold of
    15 seconds per trial as the practical significance boundary.
  - Cleaned up informal phrasing in the hypothesis section.
  Updated file: `paper/sections/introduction.md`.
- Closed data collection at 16 participants. Checked for incomplete
  submissions (none) and obvious random clicking (none flagged; everyone
  had plausible response times and non-uniform answers).
- Wrote `analysis/analyze_responses.py`, which computes per-encoding
  accuracy, confidence, response time, and Brier score. Also runs Friedman
  tests for repeated-measures comparisons across the three conditions.
  Preliminary numbers:
  - Error bars: 97.9% accuracy, avg confidence 4.65, avg time ~24 s
  - Violin/box: 91.7% accuracy, avg confidence 4.42, avg time ~40 s
  - HOPs grid: 100% accuracy, avg confidence 4.50, avg time ~26 s
  - Friedman test on accuracy: significant (chi-squared = 27.1, df = 2, p < 0.05)
  - Friedman test on response time: not significant (chi-squared = 4.6, df = 2)
  The accuracy result is a bit surprising: HOPs came out on top, not
  violin/box. The violin/box ranking task is where most errors occurred
  (81.2% vs 100% for error bars and HOPs). Response time differences
  were not statistically significant, though violin/box was descriptively
  slower.
- Drafted the Methods section in `paper/sections/methods.md`. Covers
  participants (n = 16, demographics), materials (stimuli, parallel task
  sets), design (within-subjects, random counterbalancing, distractor tasks,
  recognition check), procedure, measures, and analysis plan.
- Migrated the paper to LaTeX using the CCSC template (`preamble.tex`
  from the starter repo). Created `paper/paper.tex` and `paper/paper.bib`
  with all sections (Introduction through Conclusion), embedded the
  analysis figures, and compiled a full draft PDF (`paper/paper.pdf`).
  The draft is 12 pages and ready for review.
- Built the in-class presentation (21 slides in Keynote). Covers the full
  study: problem, research questions, related work, three encodings with
  stimuli images, study design, participants with demographic figures,
  results (accuracy, per-task breakdown, response time, calibration),
  key takeaways, limitations, future work, and a live demo slide.
  Submitted as `presentation/CSCI 693 - Keynote.pdf` for early feedback.

**Updated files/folders:**
- [`paper/sections/introduction.md`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/sections/introduction.md) (revised: hypothesis, definitions, tone)
- [`paper/sections/methods.md`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/sections/methods.md) (new)
- [`paper/paper.tex`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/paper.tex) (new: full draft in CCSC template)
- [`paper/preamble.tex`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/preamble.tex) (new: CCSC template preamble)
- [`paper/paper.bib`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/paper.bib) (new: bibliography)
- [`paper/Draft_Research_Paper.pdf`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/Draft_Research_Paper.pdf) (new: compiled draft, 12 pages)
- [`analysis/analyze_responses.py`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/analysis/analyze_responses.py) (new)
- [`presentation/CSCI 693 - Keynote.pdf`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/presentation/CSCI%20693%20-%20Keynote.pdf) (new: 21-slide deck)

## What is blocking your progress?

Nothing major. The violin/box ranking accuracy being lower than expected is
worth investigating. I want to check whether it is driven by a few
participants or spread across the sample. The Brier scores are also fairly
flat across conditions (0.025 to 0.048), so I may need calibration curves
rather than just the aggregate score to get a clearer picture.

## What is your plan for the next week?

I want to work aggressively ahead of schedule this week. The rough draft
paper and presentation are both done, so my plan is to address any feedback
Shelley gives on the draft and presentation as soon as it comes in. That
means next week (Update #7) will focus on revising the paper based on
feedback, fine-tuning the presentation if any changes are needed, and
submitting the final draft paper. I also plan to record and submit the
video presentation for the in-class talk. Then for Update #8 I expect to
be mostly doing final polish: incorporating any last insights from
classmates' presentations and making small edits before the final
submission deadline.
