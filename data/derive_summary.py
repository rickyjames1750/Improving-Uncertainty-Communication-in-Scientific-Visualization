"""
Derive summary statistics from the raw Palmer Penguins dataset.

Reads penguins.csv (344 observations, 3 species) and computes per-species
mean bill length with 95% confidence interval error bounds.

Error bounds are asymmetric because the CI is built around the sample mean:
    err_plus  = ci_high - mean
    err_minus = mean - ci_low

where ci_low and ci_high come from a two-sided 95% t-interval:
    ci = mean +/- t_{0.025, n-1} * (std / sqrt(n))

Output: penguins_summary_errors.csv
"""

import csv
import math

RAW_FILE = "penguins.csv"
OUT_FILE = "penguins_summary_errors.csv"
ALPHA = 0.05

# Hardcoded t critical values for 95% CI (two-tailed) at relevant df.
# Looked up from standard t-tables; avoids needing scipy.
T_CRIT = {
    150: 1.976,   # Adelie  (n=151, df=150)
    67:  1.996,   # Chinstrap (n=68, df=67)
    122: 1.980,   # Gentoo (n=123, df=122)
}

def read_bill_lengths(path):
    """Return dict mapping species -> list of bill_length_mm floats."""
    species_data = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sp = row["species"]
            raw = row["bill_length_mm"].strip()
            if raw == "":
                continue
            species_data.setdefault(sp, []).append(float(raw))
    return species_data

def summarize(values, t_crit):
    n = len(values)
    mean = sum(values) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in values) / (n - 1))
    se = std / math.sqrt(n)
    ci_low = mean - t_crit * se
    ci_high = mean + t_crit * se
    return {
        "n": n,
        "mean": mean,
        "std": std,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "err_plus": ci_high - mean,
        "err_minus": mean - ci_low,
    }

def main():
    data = read_bill_lengths(RAW_FILE)

    print(f"{'Species':<12} {'n':>4} {'Mean':>10} {'Std':>10} "
          f"{'CI Low':>10} {'CI High':>10} {'err+':>10} {'err-':>10}")
    print("-" * 82)

    rows = []
    for sp in ["Adelie", "Chinstrap", "Gentoo"]:
        vals = data[sp]
        df = len(vals) - 1
        s = summarize(vals, T_CRIT[df])
        rows.append((sp, s))
        print(f"{sp:<12} {s['n']:>4} {s['mean']:>10.4f} {s['std']:>10.4f} "
              f"{s['ci_low']:>10.4f} {s['ci_high']:>10.4f} "
              f"{s['err_plus']:>10.6f} {s['err_minus']:>10.6f}")

    with open(OUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["species", "mean", "err_plus", "err_minus"])
        for sp, s in rows:
            writer.writerow([sp, s["mean"], s["err_plus"], s["err_minus"]])

    print(f"\nWrote {OUT_FILE}")

if __name__ == "__main__":
    main()
