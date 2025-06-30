from math import factorial as f
from pprint import pprint
from typing import List, Tuple, Optional
from collections import OrderedDict
from prettytable import PrettyTable

# ----------------------
# CONFIGURATION
# ----------------------
USE_LOTTERY = False  # True uses lottery combinations, False uses classic birthday (365.25)
USE_THRESHOLDS = True  # True uses thresholds, False uses factors

# ----------------------
# FUNCTIONS
# ----------------------
def combinations(n: int, r: int, b: int) -> int:
    """Compute n choose r with bonus."""
    return f(n) // (f(r) * f(n - r)) * b


def probability_for_n(n: int, total_outcomes: float) -> float:
    """Calculate the probability of at least one duplicate in n draws."""
    probability: float = 1.0
    for i in range(n):
        probability *= (total_outcomes - i) / total_outcomes
    return 1 - probability


def find_thresholds(total_outcomes: float, thresholds: List[float]) -> dict[float, int | None]:
    """Find sample sizes where duplicate probability exceeds thresholds."""
    results = {}
    max_n: int = int(total_outcomes) if total_outcomes < 1e6 else int(1e6)

    for threshold in thresholds:
        n: int = 1
        while n <= max_n:
            prob: float = probability_for_n(n, total_outcomes)
            if prob >= threshold:
                results[threshold] = n
                break
            n += 1
        else:
            results[threshold] = None  # No threshold reached
    return results


def calculate_elements(elements: List[int], total_outcomes: float) -> List[Tuple[int, float]]:
    """Calculate the probability of duplicates for specified elements."""
    results = []
    for element in elements:
        prob: float = probability_for_n(element, total_outcomes)
        results.append((element, prob))
    return results


def print_results(config: dict, threshold_results: Optional[dict[float, int | None]] = None,
    element_results: Optional[list[tuple[int, float]]] = None) -> None:
    """Print results in a formatted table."""
    print("\n---Configuration---")
    pprint(config)

    mode = "Lottery" if config["USE_LOTTERY"] else "Classic Birthday"

    if config["USE_THRESHOLDS"]:
        print(f"\nDuplicate Probability [{mode}]")
        table = PrettyTable()
        table.field_names = ["Threshold", "Sample Size"]

        if threshold_results is not None:
            for threshold, sample_size in threshold_results.items():
                if sample_size is not None:
                    n_str = f"{sample_size:,}"
                else:
                    n_str = "Not found"
                table.add_row([f"{threshold:.0%}", n_str])
    else:
        print(f"\nDuplicate Probability [{mode}]")
        table = PrettyTable()
        table.field_names = ["Elements", "Probability"]

        if element_results is not None:
            for element, prob in element_results:
                table.add_row([f"{element:,}", f"{prob:.1%}"])

    print(table)
    # print(f"\nTotal combinations (p): {config['total_outcomes_p']:,}\n")

# ----------------------
# MAIN SCRIPT
# ----------------------
if __name__ == "__main__":

    # Define lottery drawing variables
    pool_size = 38  # Total numbers in the lottery pool
    draw_size = 5  # Numbers drawn in the lottery
    bonus_pool = 1  # Bonus number drawn

    classic_p = 365.25  # Average days in a year for classic birthday problem

    thresholds = [0.1, 0.25, 0.5, 0.75, 0.9]  # Duplicate probability thresholds
    elements = [100, 500, 1_000, 2_500, 5_000]

    # Compute total possible outcomes (p)
    if USE_LOTTERY:
        total_outcomes_p = combinations(pool_size, draw_size, bonus_pool)
        p = total_outcomes_p
    else:
        p = classic_p

    # Build configuration dictionary
    config = OrderedDict([
        ("USE_LOTTERY", USE_LOTTERY),
        ("USE_THRESHOLDS", USE_THRESHOLDS),
        ("classic_p", classic_p),
        ("pool_size", pool_size),
        ("draw_size", draw_size),
        ("bonus_pool", bonus_pool),
        ("thresholds", thresholds),
        ("elements", elements),
        ("total_outcomes_p", p)
    ])

    # Run chosen mode
    if USE_THRESHOLDS:
        threshold_results = find_thresholds(p, thresholds)
        print_results(config, threshold_results=threshold_results)
    else:
        element_results = calculate_elements(elements, p)
        print_results(config, element_results=element_results)

"""
Duplicate Probability [Lottery: Powerball]
Pool: 69, Draw: 5, Bonus: 26
Total combinations (p): 292,201,338
+-----------+-------------+
| Threshold | Sample Size |
+-----------+-------------+
|    10%    |    7,848    |
|    25%    |    12,967   |
|    50%    |    20,127   |
|    75%    |    28,464   |
|    90%    |    36,683   |
+-----------+-------------+

Duplicate Probability [Lottery: TN Daily]
Pool: 38, Draw: 5, Bonus: 1
Total combinations (p): 501,942
+-----------+-------------+
| Threshold | Sample Size |
+-----------+-------------+
|    10%    |     326     |
|    25%    |     538     |
|    50%    |     835     |
|    75%    |    1,180    |
|    90%    |    1,521    |
+-----------+-------------+

Duplicate Probability [Classic Birthday]
+-----------+-------------+
| Threshold | Sample Size |
+-----------+-------------+
|    10%    |      10     |
|    25%    |      15     |
|    50%    |      23     |
|    75%    |      32     |
|    90%    |      41     |
+-----------+-------------+
"""
