"""
Analyze the main study responses.

Reads study/responses.csv and computes per-encoding:
  - Decision accuracy (proportion correct)
  - Mean confidence rating
  - Mean response time (seconds)
  - Brier score (confidence calibration)

Also prints per-task-type breakdowns and runs Friedman tests for
repeated-measures comparisons across the three encodings.
"""

import csv
import os
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "study", "responses.csv")


def load_data(path):
    rows = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            row["trial"] = int(row["trial"])
            row["correct"] = int(row["correct"])
            row["confidence"] = int(row["confidence"])
            row["time_ms"] = int(row["time_ms"])
            rows.append(row)
    return rows


def brier_score(trials):
    """Compute mean Brier score: (confidence/5 - correct)^2."""
    if not trials:
        return 0.0
    total = 0.0
    for t in trials:
        prob = t["confidence"] / 5.0
        total += (prob - t["correct"]) ** 2
    return total / len(trials)


def mean(values):
    return sum(values) / len(values) if values else 0.0


def std(values):
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return math.sqrt(sum((x - m) ** 2 for x in values) / (len(values) - 1))


def friedman_chi2(groups):
    """Friedman test (chi-square approximation) for k related samples.

    groups: list of lists, one per condition, same length (one value per
    participant). Returns (chi2, k, n).
    """
    k = len(groups)
    n = len(groups[0])
    ranks = []
    for i in range(n):
        vals = [(groups[g][i], g) for g in range(k)]
        vals.sort()
        r = [0] * k
        for rank_pos, (_, g) in enumerate(vals, 1):
            r[g] = rank_pos
        ranks.append(r)

    rank_sums = [sum(ranks[i][g] for i in range(n)) for g in range(k)]
    chi2 = (12.0 / (n * k * (k + 1))) * sum(rs ** 2 for rs in rank_sums) \
           - 3 * n * (k + 1)
    return chi2, k, n


def main():
    rows = load_data(DATA_PATH)
    participants = sorted(set(r["participant"] for r in rows))
    encodings = ["errorbar", "violin_box", "hops_grid"]

    print(f"Participants: {len(participants)}")
    print(f"Total trials: {len(rows)}\n")

    # --- Per-encoding summary ---
    print(f"{'Encoding':<14} {'Accuracy':>10} {'Avg Conf':>10} "
          f"{'Avg Time':>10} {'Brier':>8}")
    print("-" * 56)
    for enc in encodings:
        trials = [r for r in rows if r["encoding"] == enc]
        acc = mean([t["correct"] for t in trials])
        avg_conf = mean([t["confidence"] for t in trials])
        avg_time = mean([t["time_ms"] for t in trials]) / 1000
        bs = brier_score(trials)
        print(f"{enc:<14} {acc:>9.1%} {avg_conf:>10.2f} "
              f"{avg_time:>9.1f}s {bs:>8.3f}")

    # --- Per task type ---
    print(f"\n{'Task':<14} {'Encoding':<14} {'Accuracy':>10} {'Avg Time':>10}")
    print("-" * 52)
    for task in ["ranking", "estimation", "decision"]:
        for enc in encodings:
            trials = [r for r in rows
                      if r["encoding"] == enc and r["task_type"] == task]
            acc = mean([t["correct"] for t in trials])
            avg_time = mean([t["time_ms"] for t in trials]) / 1000
            print(f"{task:<14} {enc:<14} {acc:>9.1%} {avg_time:>9.1f}s")

    # --- Friedman test on accuracy ---
    print("\n--- Friedman test (accuracy by encoding) ---")
    acc_by_enc = {}
    for enc in encodings:
        per_p = []
        for p in participants:
            trials = [r for r in rows
                      if r["participant"] == p and r["encoding"] == enc]
            per_p.append(mean([t["correct"] for t in trials]))
        acc_by_enc[enc] = per_p

    groups = [acc_by_enc[e] for e in encodings]
    chi2, k, n = friedman_chi2(groups)
    print(f"  Chi2 = {chi2:.3f}, k = {k}, n = {n}")
    print(f"  (Compare to chi2 critical value at df={k-1}, alpha=0.05: 5.991)")
    if chi2 > 5.991:
        print("  -> Significant at p < 0.05")
    else:
        print("  -> Not significant at p < 0.05")

    # --- Friedman test on response time ---
    print("\n--- Friedman test (response time by encoding) ---")
    time_by_enc = {}
    for enc in encodings:
        per_p = []
        for p in participants:
            trials = [r for r in rows
                      if r["participant"] == p and r["encoding"] == enc]
            per_p.append(mean([t["time_ms"] for t in trials]))
        time_by_enc[enc] = per_p

    groups_t = [time_by_enc[e] for e in encodings]
    chi2_t, _, _ = friedman_chi2(groups_t)
    print(f"  Chi2 = {chi2_t:.3f}, k = {k}, n = {n}")
    if chi2_t > 5.991:
        print("  -> Significant at p < 0.05")
    else:
        print("  -> Not significant at p < 0.05")


if __name__ == "__main__":
    main()
