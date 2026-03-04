"""
CLI Binomial Distribution Probability Calculator

Calculates probabilities based on the binomial distribution using scipy.stats.binom.

Usage:
    python cli_binomial.py --n 10 --k 3 --p 0.5
    python cli_binomial.py --n 10 --k 3 --p 0.5 --target 4
    python cli_binomial.py --n 10 --k 3 --p 0.5 --min-prob 2
    python cli_binomial.py --n 10 --k 3 --p 0.5 --target 4 --min-prob 2

Arguments:
    --n         Total number of trials (positive integer)
    --k         Target number of successes (integer, 0 <= k <= n)
    --p         Probability of success per trial (float, 0.0 <= p <= 1.0)
    --target    Evaluate exact probability of achieving this many successes (optional)
    --min-prob  Compute probability of achieving at least this many successes (optional)

Examples:
    # Probability of exactly 3 successes in 10 trials with p=0.5
    python cli_binomial.py --n 10 --k 3 --p 0.5

    # Also evaluate the probability of exactly 4 successes
    python cli_binomial.py --n 10 --k 3 --p 0.5 --target 4

    # Also compute the probability of achieving at least 2 successes
    python cli_binomial.py --n 10 --k 3 --p 0.5 --min-prob 2

    # Full example with all flags
    python cli_binomial.py --n 10 --k 3 --p 0.5 --target 4 --min-prob 2
"""

import argparse
from scipy.stats import binom


def parse_binomial_args():
    parser = argparse.ArgumentParser(
        description="Calculate binomial distribution probabilities.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python cli_binomial.py --n 10 --k 3 --p 0.5\n"
            "  python cli_binomial.py --n 10 --k 3 --p 0.5 --target 4 --min-prob 2\n"
        ),
    )
    parser.add_argument(
        "--n",
        type=int,
        required=True,
        help="Total number of trials (positive integer).",
    )
    parser.add_argument(
        "--k",
        type=int,
        required=True,
        help="Target number of successes (integer between 0 and n, inclusive).",
    )
    parser.add_argument(
        "--p",
        type=float,
        required=True,
        help="Probability of success per trial (float between 0.0 and 1.0).",
    )
    parser.add_argument(
        "--target",
        type=int,
        default=None,
        help="Evaluate the exact probability of achieving this many successes (optional).",
    )
    parser.add_argument(
        "--min-prob",
        type=int,
        default=None,
        dest="min_prob",
        help="Compute the probability of achieving at least this many successes (optional).",
    )
    return parser.parse_args()


def validate_binomial_inputs(n, k, p, target, min_prob):
    errors = []

    if n <= 0:
        errors.append(f"--n must be a positive integer, got {n}.")
    if k < 0 or k > n:
        errors.append(f"--k must be between 0 and n ({n}), got {k}.")
    if p < 0.0 or p > 1.0:
        errors.append(f"--p must be between 0.0 and 1.0, got {p}.")
    if target is not None and (target < 0 or target > n):
        errors.append(f"--target must be between 0 and n ({n}), got {target}.")
    if min_prob is not None and (min_prob < 0 or min_prob > n):
        errors.append(f"--min-prob must be between 0 and n ({n}), got {min_prob}.")

    return errors


def main():
    args = parse_binomial_args()

    errors = validate_binomial_inputs(args.n, args.k, args.p, args.target, args.min_prob)
    if errors:
        for error in errors:
            print(f"Validation error: {error}")
        raise SystemExit(1)

    n, k, p = args.n, args.k, args.p

    print(f"\nBinomial Distribution Parameters:")
    print(f"  Trials (n)               : {n}")
    print(f"  Target successes (k)     : {k}")
    print(f"  Success probability (p)  : {p}")

    # Exact probability P(X = k)
    prob_exact_k = binom.pmf(k, n, p)
    print(f"\nP(X = {k})                  : {prob_exact_k:.6f}  ({prob_exact_k:.2%})")

    # Cumulative probability P(X <= k)
    prob_cumulative_k = binom.cdf(k, n, p)
    print(f"P(X <= {k})                 : {prob_cumulative_k:.6f}  ({prob_cumulative_k:.2%})")

    # Probability P(X >= k)
    prob_at_least_k = binom.sf(k - 1, n, p)
    print(f"P(X >= {k})                 : {prob_at_least_k:.6f}  ({prob_at_least_k:.2%})")

    if args.target is not None:
        t = args.target
        prob_exact_t = binom.pmf(t, n, p)
        prob_at_least_t = binom.sf(t - 1, n, p)
        print(f"\nTarget successes (--target): {t}")
        print(f"  P(X = {t})               : {prob_exact_t:.6f}  ({prob_exact_t:.2%})")
        print(f"  P(X >= {t})              : {prob_at_least_t:.6f}  ({prob_at_least_t:.2%})")

    if args.min_prob is not None:
        m = args.min_prob
        prob_at_least_m = binom.sf(m - 1, n, p)
        print(f"\nMinimum successes (--min-prob): {m}")
        print(f"  P(X >= {m})              : {prob_at_least_m:.6f}  ({prob_at_least_m:.2%})")

    print()


if __name__ == "__main__":
    main()
