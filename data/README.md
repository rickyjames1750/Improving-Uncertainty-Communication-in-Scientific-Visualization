# Data

## Source

The raw dataset is the **Palmer Penguins** dataset, originally collected by
Dr. Kristen Gorman at Palmer Station, Antarctica, and made widely available
through the `palmerpenguins` R package by Allison Horst, Alison Hill, and
Kristen Gorman.

- **R package:** https://allisonhorst.github.io/palmerpenguins/
- **GitHub:** https://github.com/allisonhorst/palmerpenguins
- **Citation:** Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer
  Archipelago (Antarctica) penguin data. R package version 0.1.0.
  https://doi.org/10.5281/zenodo.3960218

The CSV used here (`penguins.csv`) contains 344 observations across three
species (Adelie, Chinstrap, Gentoo) with columns for species, island, bill
length/depth, flipper length, body mass, and sex. It is identical to the
`penguins` dataset distributed with the R package (version 0.1.0).

## Summary file

`penguins_summary_errors.csv` contains per-species **mean bill length (mm)**
and asymmetric 95% confidence-interval error bounds.

| Column | Description |
|--------|-------------|
| `species` | Penguin species (Adelie, Chinstrap, Gentoo) |
| `mean` | Sample mean of `bill_length_mm` (NAs excluded) |
| `err_plus` | Upper error bound: `ci_high - mean` |
| `err_minus` | Lower error bound: `mean - ci_low` |

### How the error bounds were calculated

1. For each species, drop rows with missing `bill_length_mm`.
2. Compute the sample mean and sample standard deviation.
3. Build a two-sided 95% t-interval:
   `CI = mean ± t_{0.025, n-1} × (std / √n)`
4. Split into asymmetric error bars:
   `err_plus = ci_high - mean`, `err_minus = mean - ci_low`.

The slight asymmetry comes from rounding in the t critical values.

## Reproducibility

To regenerate `penguins_summary_errors.csv` from the raw data:

```bash
cd data/
python derive_summary.py
```

The script (`derive_summary.py`) reads `penguins.csv`, computes the
statistics described above, and writes the summary CSV. It uses only the
Python standard library (no external dependencies).
