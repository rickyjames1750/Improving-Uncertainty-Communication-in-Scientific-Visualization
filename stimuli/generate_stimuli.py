"""
Generate the three stimulus chart types for the uncertainty study:
  1. Error bars (mean + 95% CI)
  2. Box/violin overlay
  3. HOPs-style bootstrap grid

Reads ../data/penguins.csv and writes PNGs to figures/.
"""

import csv
import math
import os
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

SEED = 42
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "penguins.csv")
OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
SPECIES_ORDER = ["Adelie", "Chinstrap", "Gentoo"]
COLORS = {"Adelie": "#FF6F61", "Chinstrap": "#6B5B95", "Gentoo": "#88B04B"}


def load_bill_lengths(path):
    """Return {species: [bill_length_mm, ...]} with NAs dropped."""
    data = {sp: [] for sp in SPECIES_ORDER}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            sp = row["species"]
            val = row["bill_length_mm"].strip()
            if val and sp in data:
                data[sp].append(float(val))
    return data


def compute_ci(values, confidence=0.95):
    n = len(values)
    mean = sum(values) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in values) / (n - 1))
    se = std / math.sqrt(n)
    # approximate t-crit for large-ish n
    t_crit = 1.96 if n > 120 else 2.0
    return mean, t_crit * se


def make_errorbar_chart(data):
    fig, ax = plt.subplots(figsize=(7, 5))
    xs = range(len(SPECIES_ORDER))
    means, errs = [], []
    for sp in SPECIES_ORDER:
        m, e = compute_ci(data[sp])
        means.append(m)
        errs.append(e)

    bars = ax.bar(xs, means, yerr=errs, capsize=6, width=0.5,
                  color=[COLORS[sp] for sp in SPECIES_ORDER],
                  edgecolor="black", linewidth=0.6, alpha=0.85)
    ax.set_xticks(xs)
    ax.set_xticklabels(SPECIES_ORDER)
    ax.set_ylabel("Bill length (mm)")
    ax.set_title("Mean Bill Length with 95% CI")
    ax.set_ylim(30, 55)
    ax.yaxis.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "errorbar.png"), dpi=150)
    plt.close(fig)
    print("  wrote errorbar.png")


def make_violin_chart(data):
    fig, ax = plt.subplots(figsize=(7, 5))
    positions = range(len(SPECIES_ORDER))
    all_vals = [data[sp] for sp in SPECIES_ORDER]

    parts = ax.violinplot(all_vals, positions=positions, showmedians=False,
                          showextrema=False)
    for i, body in enumerate(parts["bodies"]):
        body.set_facecolor(COLORS[SPECIES_ORDER[i]])
        body.set_alpha(0.4)

    bp = ax.boxplot(all_vals, positions=positions, widths=0.15,
                    patch_artist=True, showfliers=False)
    for i, patch in enumerate(bp["boxes"]):
        patch.set_facecolor(COLORS[SPECIES_ORDER[i]])
        patch.set_alpha(0.8)
    for element in ["whiskers", "caps", "medians"]:
        plt.setp(bp[element], color="black", linewidth=1)

    ax.set_xticks(list(positions))
    ax.set_xticklabels(SPECIES_ORDER)
    ax.set_ylabel("Bill length (mm)")
    ax.set_title("Bill Length Distribution (Violin + Box)")
    ax.set_ylim(30, 65)
    ax.yaxis.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "violin_box.png"), dpi=150)
    plt.close(fig)
    print("  wrote violin_box.png")


def make_hops_grid(data, n_draws=12):
    """Static HOPs: 3x4 grid of bootstrap sample means as dot plots.

    Reduced from 20 to 12 panels after pilot feedback — participants found
    the 4x5 layout overwhelming and the smaller panels hard to read.
    """
    random.seed(SEED)
    fig, axes = plt.subplots(3, 4, figsize=(13, 9), sharex=True, sharey=True)
    axes_flat = axes.flatten()

    for idx in range(n_draws):
        ax = axes_flat[idx]
        xs = range(len(SPECIES_ORDER))
        boot_means = []
        for sp in SPECIES_ORDER:
            vals = data[sp]
            sample = [random.choice(vals) for _ in range(len(vals))]
            boot_means.append(sum(sample) / len(sample))

        for i, (x, m) in enumerate(zip(xs, boot_means)):
            ax.plot(x, m, "o", color=COLORS[SPECIES_ORDER[i]],
                    markersize=12, markeredgecolor="black", markeredgewidth=0.7)
            ax.vlines(x, 37, m, color=COLORS[SPECIES_ORDER[i]],
                      linewidth=1.8, alpha=0.5)
        ax.set_ylim(37, 52)
        ax.set_xticks(list(xs))
        if idx >= 8:
            ax.set_xticklabels([s[:3] for s in SPECIES_ORDER], fontsize=10)
        else:
            ax.set_xticklabels([])
        ax.tick_params(axis="y", labelsize=10)
        ax.set_title(f"Draw {idx+1}", fontsize=10, pad=4)
        ax.yaxis.grid(True, alpha=0.2)

    fig.suptitle("HOPs: 12 Bootstrap Draws of Mean Bill Length", fontsize=14)
    fig.text(0.03, 0.5, "Bill length (mm)", va="center", rotation="vertical",
             fontsize=11)
    fig.text(0.5, 0.01,
             "Each panel shows one plausible outcome from resampling the data.",
             ha="center", fontsize=10, style="italic", color="#555")
    fig.tight_layout(rect=[0.05, 0.04, 1, 0.95])
    fig.savefig(os.path.join(OUT_DIR, "hops_grid.png"), dpi=150)
    plt.close(fig)
    print("  wrote hops_grid.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"Loading data from {DATA_PATH}")
    data = load_bill_lengths(DATA_PATH)
    for sp in SPECIES_ORDER:
        print(f"  {sp}: n={len(data[sp])}")

    print("\nGenerating stimuli...")
    make_errorbar_chart(data)
    make_violin_chart(data)
    make_hops_grid(data)
    print("\nDone.")


if __name__ == "__main__":
    main()
