"""
Analyze the main study responses.

Reads study/responses.csv and computes per-encoding:
  - Decision accuracy (proportion correct)
  - Mean confidence rating
  - Mean response time (seconds)
  - Brier score (confidence calibration)
  - Overconfidence index (mean confidence minus mean accuracy)

Runs Friedman tests with exact p-values for repeated-measures comparisons
across the three encodings. Reports Kendall's W as an effect size. Runs
post-hoc pairwise Wilcoxon signed-rank tests where the overall test is
significant. Flags outliers using an IQR rule.
"""

import csv
import math
import os

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
    """Mean Brier score with confidence mapped to [0.2, 1.0] via Likert/5."""
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


def chi2_sf_df2(x):
    """Survival function of chi-square with df=2. Closed form: exp(-x/2)."""
    if x <= 0:
        return 1.0
    return math.exp(-x / 2.0)


def friedman_chi2(groups):
    """Friedman chi-square for k related samples with tie correction.

    groups: list of k lists, each of length n (one value per participant).
    Returns (chi2, k, n, df, p_value).
    """
    k = len(groups)
    n = len(groups[0])
    ranks = []
    tie_correction_terms = []
    for i in range(n):
        vals = [(groups[g][i], g) for g in range(k)]
        vals.sort()
        # assign average ranks for ties
        r = [0.0] * k
        j = 0
        while j < k:
            h = j
            while h + 1 < k and vals[h + 1][0] == vals[j][0]:
                h += 1
            avg_rank = (j + 1 + h + 1) / 2.0
            for m in range(j, h + 1):
                r[vals[m][1]] = avg_rank
            tie_len = h - j + 1
            if tie_len > 1:
                tie_correction_terms.append(tie_len ** 3 - tie_len)
            j = h + 1
        ranks.append(r)

    rank_sums = [sum(ranks[i][g] for i in range(n)) for g in range(k)]
    chi2 = (12.0 / (n * k * (k + 1))) * sum(rs ** 2 for rs in rank_sums) \
        - 3 * n * (k + 1)

    # tie correction
    T = sum(tie_correction_terms)
    denom = 1 - T / (n * (k ** 3 - k))
    if denom > 0:
        chi2 = chi2 / denom

    df = k - 1
    p = chi2_sf_df2(chi2) if df == 2 else None
    return chi2, k, n, df, p


def kendalls_w(chi2, n, k):
    """Kendall's coefficient of concordance from the Friedman chi-square."""
    return chi2 / (n * (k - 1))


def wilcoxon_signed_rank(x, y):
    """Two-sided Wilcoxon signed-rank test. Returns (W, n_nonzero, p_approx).

    Normal approximation with continuity correction. Fine for n >= 10; our
    n is 16.
    """
    diffs = [a - b for a, b in zip(x, y) if a - b != 0]
    n_nz = len(diffs)
    if n_nz == 0:
        return 0.0, 0, 1.0
    abs_sorted = sorted(enumerate(diffs), key=lambda t: abs(t[1]))
    ranks = [0.0] * n_nz
    i = 0
    while i < n_nz:
        j = i
        while j + 1 < n_nz and abs(abs_sorted[j + 1][1]) == \
                abs(abs_sorted[i][1]):
            j += 1
        avg = (i + 1 + j + 1) / 2.0
        for m in range(i, j + 1):
            ranks[abs_sorted[m][0]] = avg
        i = j + 1
    W_plus = sum(r for r, d in zip(ranks, diffs) if d > 0)
    W_minus = sum(r for r, d in zip(ranks, diffs) if d < 0)
    W = min(W_plus, W_minus)

    mu = n_nz * (n_nz + 1) / 4.0
    sigma = math.sqrt(n_nz * (n_nz + 1) * (2 * n_nz + 1) / 24.0)
    if sigma == 0:
        return W, n_nz, 1.0
    z = (W - mu + 0.5) / sigma
    p = 2 * 0.5 * math.erfc(abs(z) / math.sqrt(2))
    return W, n_nz, p


def iqr_outliers(values):
    """Return indices of values outside 1.5*IQR."""
    if len(values) < 4:
        return []
    s = sorted(values)
    q1 = s[len(s) // 4]
    q3 = s[(3 * len(s)) // 4]
    iqr = q3 - q1
    lo = q1 - 1.5 * iqr
    hi = q3 + 1.5 * iqr
    return [i for i, v in enumerate(values) if v < lo or v > hi]


def main():
    rows = load_data(DATA_PATH)
    participants = sorted(set(r["participant"] for r in rows))
    encodings = ["errorbar", "violin_box", "hops_grid"]
    n_part = len(participants)

    print(f"Participants: {n_part}")
    print(f"Total trials:  {len(rows)}\n")

    # ---- Per-encoding summary ----
    print(f"{'Encoding':<14} {'Accuracy':>10} {'AvgConf':>9} "
          f"{'AvgTime':>10} {'Brier':>7} {'OC Index':>9}")
    print("-" * 64)
    acc_by_enc_p = {}
    time_by_enc_p = {}
    for enc in encodings:
        trials = [r for r in rows if r["encoding"] == enc]
        acc = mean([t["correct"] for t in trials])
        avg_conf = mean([t["confidence"] for t in trials])
        avg_time = mean([t["time_ms"] for t in trials]) / 1000
        bs = brier_score(trials)
        oc = (avg_conf / 5.0) - acc
        print(f"{enc:<14} {acc:>9.1%} {avg_conf:>9.2f} "
              f"{avg_time:>9.1f}s {bs:>7.3f} {oc:>+9.3f}")
        per_p_acc, per_p_time = [], []
        for p in participants:
            pt = [t for t in trials if t["participant"] == p]
            per_p_acc.append(mean([t["correct"] for t in pt]))
            per_p_time.append(mean([t["time_ms"] for t in pt]))
        acc_by_enc_p[enc] = per_p_acc
        time_by_enc_p[enc] = per_p_time

    # ---- Per task type ----
    print(f"\n{'Task':<12} {'Encoding':<14} {'Accuracy':>10} {'AvgTime':>10}")
    print("-" * 50)
    for task in ["ranking", "estimation", "decision"]:
        for enc in encodings:
            trials = [r for r in rows
                      if r["encoding"] == enc and r["task_type"] == task]
            acc = mean([t["correct"] for t in trials])
            avg_time = mean([t["time_ms"] for t in trials]) / 1000
            print(f"{task:<12} {enc:<14} {acc:>9.1%} {avg_time:>9.1f}s")

    # ---- Friedman: accuracy ----
    print("\n--- Friedman test (participant-level accuracy) ---")
    groups = [acc_by_enc_p[e] for e in encodings]
    chi2, k, n, df, p = friedman_chi2(groups)
    W = kendalls_w(chi2, n, k)
    print(f"  chi2 = {chi2:.3f}, df = {df}, n = {n}")
    print(f"  p = {p:.3e}   (Kendall's W = {W:.3f})")

    # ---- Post-hoc pairwise Wilcoxon on accuracy ----
    print("\n--- Post-hoc (Wilcoxon signed-rank, two-sided) ---")
    pairs = [("errorbar", "violin_box"),
             ("errorbar", "hops_grid"),
             ("violin_box", "hops_grid")]
    for a, b in pairs:
        W_stat, n_nz, pw = wilcoxon_signed_rank(
            acc_by_enc_p[a], acc_by_enc_p[b])
        print(f"  {a:<11} vs {b:<11} W = {W_stat:>6.1f}, "
              f"n(nonzero) = {n_nz:>2}, p = {pw:.3e}")

    # ---- Friedman: response time ----
    print("\n--- Friedman test (participant-level mean response time) ---")
    groups_t = [time_by_enc_p[e] for e in encodings]
    chi2_t, _, _, _, p_t = friedman_chi2(groups_t)
    W_t = kendalls_w(chi2_t, n, k)
    print(f"  chi2 = {chi2_t:.3f}, df = {df}, n = {n}")
    print(f"  p = {p_t:.3e}   (Kendall's W = {W_t:.3f})")

    # ---- Outlier check on violin ranking accuracy ----
    print("\n--- Outlier check: violin/box ranking task accuracy ---")
    per_p_rank_vb = []
    for p in participants:
        pt = [r for r in rows
              if r["participant"] == p and r["encoding"] == "violin_box"
              and r["task_type"] == "ranking"]
        if pt:
            per_p_rank_vb.append(mean([t["correct"] for t in pt]))
    out_idx = iqr_outliers(per_p_rank_vb)
    n_wrong = sum(1 for v in per_p_rank_vb if v < 1.0)
    print(f"  Participants with at least one error on this task: {n_wrong}")
    print(f"  IQR-based outliers: {len(out_idx)} "
          f"(participant indices: {out_idx})")


if __name__ == "__main__":
    main()
