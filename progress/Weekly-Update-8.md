# Weekly Progress Update #8

**Date:** April 29, 2026

## What did you accomplish this week?

Most of this week was a polish-and-respond pass.  Shelley's Update #7
feedback flagged that even after the tie-correction fix, some of my
language around the 100% accuracy and "perfect accuracy" cases was
still too confident given the small sample and the ceiling effect.  I
revised the paper to soften those framings throughout.

### Updated framing of the 100% accuracy result

The HOPs grid still produces zero observed errors in the data, but I
no longer describe that as "perfect accuracy" anywhere it is not
immediately qualified.  Specific changes in
[`paper/paper.tex`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/paper.tex)
and reflected in the recompiled
[`paper/Final Research Paper.pdf`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/paper/Final%20Research%20Paper.pdf):

- **Abstract:** the HOPs result now reads "100% of 48 trials" with an
  explicit caveat that this means "no errors observed in this small,
  high-data-literacy sample on these specific tasks," not a universal
  claim about the encoding.
- **Results §4.1:** rewrote the opening paragraph to put the 100%
  number in its narrow descriptive sense, denominator included
  (48/48, 47/48, 44/48), and explicitly noted that estimation
  accuracy at 100% across all encodings makes that task uninformative
  for separating conditions.
- **Table 1 caption:** added that cells at 100% reflect zero observed
  errors in this sample on these specific tasks, not a universal
  claim about the encoding.
- **Figure 1 caption:** added the same caveat for the bars sitting
  at 1.0.
- **Conclusion:** rewrote the opening so the headline is "no observed
  errors in this sample" rather than "outperformed."  Added a
  sentence stating that we deliberately avoid framing the 100% HOPs
  result as "perfect accuracy" and read it instead as "zero errors
  observed on these specific tasks, in this specific sample."

The Limitations section already lists ceiling effects, small sample,
and task simplicity as the three reasons not to over-interpret the
numbers, so I did not duplicate that material; I just made the body
of the paper stop sounding more confident than the limitations admit.

### Other small revisions

- Reread the Discussion top-to-bottom and trimmed two phrasings that
  edged toward overclaiming.
- Confirmed every Friedman/Wilcoxon/Kendall number in the paper still
  matches what
  [`analysis/analyze_responses.py`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/analysis/analyze_responses.py)
  prints.  No analysis changes this week, just text.
- Verified the final paper PDF is the version submitted under the
  Final Research Paper link, byte-for-byte.

### Slides for the May 11 in-class talk

The pre-recorded video (submitted Apr 21) and the
[`presentation/CSCI 693 - Keynote.pdf`](https://github.com/rickyjames1750/Improving-Uncertainty-Communication-in-Scientific-Visualization/blob/main/presentation/CSCI%20693%20-%20Keynote.pdf)
on GitHub still use the older, more confident wording that Shelley
flagged ("HOPs: perfect accuracy on all 3 task types," "HOPs grid
produced perfect accuracy" on the Key Takeaways slide).  Plan for next
week is to swap those exact strings on Slides 12, 13, and 15 to match
the paper's new framing ("100% in this sample, zero errors observed,"
"ceiling effect: see paper §4.1") and re-export the deck before the
in-class presentation.  I will use the revised deck for the in-class
talk on May 11, even though the pre-recorded video stays as it is.

## What is blocking your progress?

Nothing blocking.

## What is your plan for the next week?

- Apply the 100%/perfect-accuracy wording fix on Slides 12, 13, and 15
  of the Keynote deck, re-export, and push the new
  `CSCI 693 - Keynote.pdf` to the repo.
- Sit through Wednesday's presentations day, take notes, and watch
  for anything that sharpens the framing of my own talk.
- Do the in-class presentation on May 11 with the updated deck.
- Submit the Research Presentation Feedback assignment after class
  on May 11.
