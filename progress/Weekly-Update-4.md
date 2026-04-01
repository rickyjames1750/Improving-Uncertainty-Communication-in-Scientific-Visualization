# Weekly Progress Update #4

**Date:** April 1, 2026

## What did you accomplish this week?

- Addressed Shelley's feedback from Update #3:
  - **HOPs readability:** Bumped the axis font sizes on the HOPs grid so the
    y-axis values and species labels are easier to read. Also increased dot
    size slightly. The chart is still a 3x4 grid of 12 draws, just more
    legible now.
  - **Results collection:** Updated `study/survey.html` to include "Copy to
    clipboard" and "Download JSON" buttons on the thank-you page. After each
    participant finishes, I copy the JSON output and save it to a file. No
    server needed — everything stays client-side.
  - **Random group assignment:** Each session shuffles the three encodings
    uniformly (same as picking one of the six Latin-square rows at random).
    Each participant gets a unique session id so JSON files do not
    collide. This also works when the link is opened on separate phones ---
    localStorage would not have worked for that.
  - **Task carryover concern:** Shelley flagged that using identical tasks
    across all three encodings means participants could remember answers
    from earlier blocks. I considered using different questions per encoding,
    but that introduces a confound (different question difficulty). Decided
    to keep the same tasks and rely on counterbalancing to distribute any
    learning effect evenly across conditions. Will acknowledge this as a
    limitation in the paper.
- Ran a pilot study with 4 participants (2 CS, 1 Bio, 1 Stats). Saved raw
  results in `study/pilot_results.json` and observations in
  `study/pilot_notes.md`.
- Main pilot finding: HOPs still took longer and was less accurate than
  error bars and violin/box. One participant with low data literacy got the
  HOPs ranking wrong (Gentoo instead of Chinstrap) and agreed with the bogus
  "same mean" claim on the decision task.
- Wrote `analysis/analyze_pilot.py` to compute per-encoding accuracy, mean
  confidence, and response time from the pilot JSON.
- Hosted the same static files on a tiny Google Cloud VM so participants can
  open the survey from a browser without sending me a file first. Public link:
  **http://104.197.114.1/** (same `index.html` and `figures/` as in the repo).
  I reserved a **static external IP** on that instance so the URL does not
  change when I stop or start the VM to save credits; it only works while the
  VM is running.

**Updated files/folders:**
- `study/survey.html` (updated — copy/download, session id, shuffle groups)
- `study/pilot_results.json` (new)
- `study/pilot_notes.md` (new)
- `study/session_exports/` (five full-session JSON downloads from the hosted survey)
- `analysis/analyze_pilot.py` (new)
- `stimuli/generate_stimuli.py` (larger axis fonts on HOPs)
- `stimuli/figures/hops_grid.png` (regenerated)
- `study/figures/hops_grid.png` (regenerated)

## What is blocking your progress?

The task carryover issue bugs me. Counterbalancing helps but doesn't fully
solve it — by the second and third block, participants probably remember
the answers. I think this is acceptable for a class project and I'll discuss
it honestly in the paper. Not much I can do about it without a much more
complex task set.

## What is your plan for the next week?

- Open data collection to a larger group (~12 participants). Planning to
  walk friends through the survey over FaceTime/Zoom.
- Start drafting the Introduction and Background sections while responses
  come in.
