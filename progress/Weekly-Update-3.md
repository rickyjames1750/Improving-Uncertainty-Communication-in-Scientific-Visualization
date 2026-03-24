# Weekly Progress Update #3

**Date:** March 25, 2026

## What did you accomplish this week?

- Addressed Shelley's feedback from Update #2:
  - Added `requirements.txt` (matplotlib 3.9.4, numpy 2.0.2) so anyone can
    install deps and run the scripts without guessing.
  - Reworked the HOPs grid chart. Switched from bar charts to lollipop/dot
    plots and tightened the y-axis range so the per-draw differences are
    actually visible. The old bars all looked the same because the full axis
    washed out the bootstrap variation.
  - Regenerated all stimuli figures with the updated script.
- Designed the study task set: three task types (ranking, estimation,
  decision) crossed with the three encoding conditions. Wrote up the full
  task definitions and counterbalancing scheme in `study/tasks.md`.
- Built a self-contained HTML survey prototype (`study/survey.html`). It
  walks participants through consent, demographics, 9 trials (3 encodings x
  3 tasks), confidence ratings, and optional feedback. Records timing per
  trial. No server needed — everything runs client-side.
- Documented the study protocol in `study/README.md` (procedure, consent
  language, timing approach, platform notes).

**Updated files/folders:**
- `requirements.txt` (new)
- `stimuli/generate_stimuli.py` (HOPs fix)
- `stimuli/figures/hops_grid.png` (regenerated)
- `study/` (new folder — tasks.md, README.md, survey.html, figures/)

## What is blocking your progress?

Nothing major. I need to decide whether the survey stays as a standalone HTML
page or if I should move it to Google Forms for easier response collection.
The HTML prototype is nicer for timing data but Google Forms is simpler to
distribute. Leaning toward keeping the HTML version and just saving results
as a JSON download for now, since timing is one of my dependent variables.

## What is your plan for the next week?

- Run a small pilot (3-5 people) with the HTML survey to check:
  - Are the task prompts clear?
  - Can participants actually see the differences in the HOPs grid?
  - Rough time to complete (target ~10 minutes)
- Refine stimuli or wording based on pilot feedback.
- Start thinking about analysis scripts — at minimum, a Python script to
  parse the JSON output and compute accuracy/confidence per condition.
