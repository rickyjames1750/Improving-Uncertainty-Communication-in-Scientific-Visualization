"""
Quick analysis of the pilot study results.

Reads pilot_results.json and prints per-encoding summaries for accuracy,
confidence, and response time. This is just for checking whether the tasks
and stimuli are working as intended before the real study.
"""

import json
import os

PILOT_PATH = os.path.join(os.path.dirname(__file__), "..", "study",
                          "pilot_results.json")

TRUE_RANKING = "Chinstrap"
TRUE_ESTIMATION = 48.8  # actual Chinstrap mean bill length
ESTIMATION_TOLERANCE = 2.0
TRUE_DECISION = "Disagree"


def score_trial(trial):
    """Return 1 if the trial answer is correct, 0 otherwise."""
    t = trial["task_type"]
    ans = trial["answer"]
    if t == "ranking":
        return 1 if ans == TRUE_RANKING else 0
    elif t == "estimation":
        if ans is None:
            return 0
        return 1 if abs(ans - TRUE_ESTIMATION) <= ESTIMATION_TOLERANCE else 0
    elif t == "decision":
        return 1 if ans == TRUE_DECISION else 0
    return 0


def main():
    with open(PILOT_PATH) as f:
        participants = json.load(f)

    print(f"Pilot participants: {len(participants)}\n")

    enc_stats = {}
    for p in participants:
        for trial in p["trials"]:
            enc = trial["encoding"]
            if enc not in enc_stats:
                enc_stats[enc] = {"correct": 0, "total": 0,
                                  "conf_sum": 0, "time_sum": 0}
            s = enc_stats[enc]
            s["correct"] += score_trial(trial)
            s["total"] += 1
            s["conf_sum"] += (trial["confidence"] or 0)
            s["time_sum"] += trial["time_ms"]

    print(f"{'Encoding':<14} {'Accuracy':>10} {'Avg Conf':>10} {'Avg Time (s)':>14}")
    print("-" * 52)
    for enc in ["errorbar", "violin_box", "hops_grid"]:
        s = enc_stats[enc]
        n = s["total"]
        acc = s["correct"] / n if n else 0
        avg_conf = s["conf_sum"] / n if n else 0
        avg_time = (s["time_sum"] / n) / 1000.0 if n else 0
        print(f"{enc:<14} {acc:>9.1%} {avg_conf:>10.1f} {avg_time:>13.1f}s")

    print("\n--- Per-participant feedback ---")
    for p in participants:
        print(f"  {p['participant']}: {p.get('feedback', '(none)')}")


if __name__ == "__main__":
    main()
