# 1. Introduction

Scientific visualizations routinely present results that come from
measurement, modeling, or sampling, all of which carry uncertainty. When
that uncertainty is left out or poorly conveyed, viewers can draw
overconfident conclusions or misjudge how strong the evidence really is
(Mehta, 2022). The trouble is not a lack of encoding options: error bars,
box plots, violin plots, and hypothetical outcome plots (HOPs) are all
readily available in modern charting libraries. The trouble is that we do not
have great empirical guidance on which option actually helps people the most,
especially when the goal is not just "get the right answer" but also "know
how sure you should be about it."

This study runs a controlled, within-subjects comparison of three common
uncertainty encodings: error bars, distributional summaries (violin + box
plots), and HOPs, on a set of standardized interpretation tasks. We measure
decision accuracy, confidence calibration, and response time. The dataset
used for all stimuli is the Palmer Penguins dataset (Horst et al., 2020),
chosen because it is small, clean, well-documented, and has real group
differences that make the tasks meaningful.

## 1.1 Motivation

Surveys like Mehta (2022) map how uncertainty enters the visualization
pipeline and catalog the encoding strategies people use, but they stop short
of recommending one strategy over another because the empirical evidence is
thin. Petek et al. (2025) offer a formal framework: treat the visualization
as a function of uncertain inputs and propagate that uncertainty into a
distribution over images, but their focus is on the math, not on whether
end users actually benefit from seeing the result. On the empirical side,
Stokes et al. (2024) compare speech, text, and visualization as modalities
for communicating uncertainty and find that visualization supports rational
decision-making, but they do not break the "visualization" category down
further into encoding types. That gap, between knowing that visualization
works and knowing which specific encoding works best, is what we are trying
to fill.

Applied work in scientific visualization reinforces the gap from a different
angle. Saklani et al. (2024) show that adding uncertainty overlays to
DNN-based volume renderings increases trust among domain scientists, and Li
et al. (2025) design bespoke uncertainty tubes for particle trajectories.
Both suggest that showing uncertainty helps, but neither tests
general-purpose encodings like error bars or HOPs on common tasks. Our study
takes the opposite approach: rather than designing a new encoding for a
specific domain, we take three existing general-purpose encodings and test
them head-to-head on straightforward tasks.

## 1.2 Research Questions

1. Which uncertainty encoding (error bars, distributional summaries, or
   HOPs) produces the highest decision accuracy?
2. Which encoding best supports confidence calibration, the alignment
   between a participant's stated confidence and their actual correctness?
3. Do distributional encodings (violin/box, HOPs) incur a measurable cost
   in task completion time compared to error bars?

## 1.3 Hypotheses

We expect that both distributional encodings will produce higher decision
accuracy and better confidence calibration than error bars, because they
give viewers more information about the shape and spread of the underlying
data. Between the two, we expect violin/box plots to yield slightly better
calibration than HOPs, since the continuous density shape maps more
naturally onto "how sure should I be?" judgments, whereas HOPs present
discrete draws that may be harder to mentally aggregate. HOPs, on the other
hand, may produce higher raw accuracy on ranking and decision tasks, because
each draw shows the between-group difference explicitly, making it visually
obvious whether two groups overlap. We also expect distributional encodings
to require more time per trial than error bars, but on the order of a few
additional seconds, not a meaningful barrier to use. For this study we
treat a per-trial difference of more than 15 seconds as practically
significant; anything below that threshold represents an acceptable
trade-off for improved comprehension. The pilot data (n = 4) showed a
preliminary pattern consistent with this: error bars and violin/box had
similar accuracy and timing, while HOPs were slower and slightly less
accurate, likely because the static grid format was harder to parse.


# 2. Background and Related Work

## 2.1 Uncertainty in the Visualization Pipeline

Mehta (2022) breaks the visualization pipeline into four stages: data
collection, preprocessing, visualization, and inference, and surveys how
uncertainty enters at each one. The key takeaway for our study is that even
when the data itself is clean, the visualization stage introduces
representational choices that affect how viewers interpret uncertainty. A bar
chart with error bars communicates something different than a violin plot of
the same data, and both communicate something different than an animated
sequence of plausible outcomes. Mehta's survey calls for more empirical work
measuring how these choices affect viewer judgment, which is exactly what we
set out to do.

## 2.2 Formal Frameworks for Uncertainty Encoding

Petek et al. (2025) propose treating a visualization as a function of
uncertain inputs. If the inputs carry a probability distribution, the output
is a distribution over images rather than a single image. Familiar
representations like confidence intervals and prediction bands fall out
naturally from this framework, and the authors release an open-source Python
implementation. We use a simplified version of their resampling approach to
generate the HOPs stimuli: for each "draw," we resample the raw data with
replacement and plot the resulting species means, giving viewers a grid of
plausible outcomes.

## 2.3 Modality Comparisons

Stokes et al. (2024) run two crowdsourced experiments comparing speech,
text, and visualization for communicating data uncertainty. Visualization
and text supported rational decision-making, while speech inspired more
trust but also riskier choices. Their study measures both decision quality
and confidence, which we adopt. The limitation, from our perspective, is
that "visualization" is treated as a single category, they do not vary the
encoding within it. We extend their approach by holding the modality
constant (all visual) and varying the encoding.

## 2.4 Uncertainty in Scientific Visualization Applications

Saklani et al. (2024) tackle uncertainty-aware volume rendering using Deep
Ensembles and Monte Carlo Dropout. They show that surfacing prediction
uncertainty in neural-network-based visualizations makes the outputs more
trustworthy for domain scientists. Li et al. (2025) work on a different
data type, particle trajectories, and propose an "uncertainty tube" with a
superelliptical cross-section that can represent nonsymmetric error. Both
papers demonstrate that domain-specific encodings help, but neither tests
the general-purpose encodings (error bars, box/violin, HOPs) that most
researchers reach for when they want to add uncertainty to a plot. Our study
fills that gap by testing these common tools on common tasks.

## 2.5 Gap in the Literature

Taken together, the literature shows that (a) uncertainty is pervasive and
ignoring it misleads viewers, (b) formal tools exist for encoding it, and
(c) the choice of representation matters for viewer behavior. What is
missing is a controlled comparison of the three most common encodings on the
same tasks, measuring both accuracy and calibration. That is what this study
provides.
