# Stimuli

Charts used as study stimuli, all generated from the Palmer Penguins dataset
(`data/penguins.csv`). Each chart shows bill length (mm) by species.

## Figures

- **errorbar.png** — Bar chart of species means with 95% confidence interval
  error bars. This is the baseline condition.
- **violin_box.png** — Violin plot overlaid with a box plot, showing the full
  distribution shape plus median and quartiles.
- **hops_grid.png** — Static grid of 20 bootstrap draws. Each panel shows
  one resampled set of species means, giving viewers a sense of how the
  estimates could vary from sample to sample.

## Regenerating

```bash
cd stimuli/
python generate_stimuli.py
```

Requires matplotlib and its dependencies (`pip install matplotlib`).
