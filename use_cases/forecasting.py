"""
GOAL: Forecast monthly city sales-tax revenue and score competing models with MAE and MAPE.

MAE  (Mean Absolute Error)            = mean(|actual - forecast|)
    -> error in the original units ($K here); easy to explain to a budget office.
MAPE (Mean Absolute Percentage Error) = mean(|actual - forecast| / |actual|) * 100
    -> scale-free percent error; comparable across series, but undefined when actual == 0.

Approach: hold out the final 12 months, fit each model on the earlier data,
forecast the holdout year, and compare errors. Lower is better for both metrics.

No model wins everywhere. The extra scenarios below are each shaped so a different model fits best:
    Naive (last value)   -> series that jumps to a new level and stays there (headcount)
    3-month moving avg   -> noisy series whose level drifts slowly (monthly new hires)
    Seasonal naive       -> strong seasonality whose shape recently changed (retail seasonal hiring)
    Trend + seasonality  -> stable seasonal shape + steady trend + noise (monthly temperatures)

WIN RATE: a single history can be lucky - noise alone may hand the win to the "wrong" model.
To see which model truly suits a data shape, each scenario is re-simulated SIMULATIONS times
with different random noise, and the win rate is the % of those runs in which a model had the
lowest MAPE. A model built for the data's shape should win the most often, not necessarily every time.
"""

import random
import statistics

# Fixes the global RNG so the headline sales-tax example prints the same numbers every run
random.seed(42)

MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
SEASON_LENGTH = 12  # months per seasonal cycle
HOLDOUT = 12  # final months hidden from the models and used to score their forecasts

# Multiplier applied to each calendar month (1.00 = an average month).
# Holiday shopping lifts Nov/Dec; post-holiday lull in Jan/Feb
SEASONAL_FACTORS = [
    0.88,
    0.85,
    0.97,
    0.98,
    1.02,
    1.04,
    1.03,
    1.01,
    0.97,
    0.99,
    1.08,
    1.18,
]
# Uncomment for a random seasonal shape each run (still multiplicative around 1.0)
SEASONAL_FACTORS = [random.uniform(0.5, 1.5) for _ in range(SEASON_LENGTH)]


def generate_tax_revenue(
    years=4, base=1_200.0, monthly_growth=0.004, noise=0.03, rng=random
):
    """Synthetic monthly sales-tax revenue in $K: growth trend x seasonality x noise."""
    revenue = []
    for t in range(years * SEASON_LENGTH):
        # Compound growth: 0.4%/month is roughly 4.9%/year
        trend = base * (1 + monthly_growth) ** t
        season = SEASONAL_FACTORS[t % SEASON_LENGTH]
        # Noise is multiplicative (gauss around 1), so a 3% wobble scales with the month's size
        revenue.append(round(trend * season * rng.gauss(1, noise), 1))
    return revenue


# ADDITIONAL SCENARIOS
# Every generator accepts `rng` so win_rates() can pass in a fresh random.Random(seed) and
# re-simulate the same *kind* of data with different noise. Defaulting to the global `random`
# keeps a plain call like generate_headcount() working without any setup.
def generate_headcount(months=48, start=250, rng=random):
    """Company headcount: lumpy steps (team spin-ups, layoffs) that persist, plus small churn.
    Best fit: Naive - the most recent level is the best guess for a series that shifts and holds."""
    level, headcount = start, []
    for _ in range(months):
        # ~15% of months bring a sizable jump up or down that becomes the new normal
        if rng.random() < 0.15:
            level += rng.choice([-1, 1]) * rng.randint(15, 40)
        # Everyday attrition/backfill noise is small relative to the jumps
        level += rng.randint(-2, 2)
        headcount.append(float(level))
    return headcount


def generate_new_hires(months=48, base=40, rng=random):
    """Monthly new hires: hiring pace wanders slowly, buried under heavy month-to-month noise.
    Best fit: Moving average - averaging recent months cancels noise yet still tracks the drift."""
    level, hires = base, []
    for _ in range(months):
        # The true hiring pace drifts a little each month (a random walk)...
        level += rng.gauss(0, 1.5)
        # ...but each month's observed count is scattered widely around it.
        # max(1, ...) keeps counts positive so MAPE never divides by zero
        hires.append(float(max(1, round(rng.gauss(level, 8)))))
    return hires


def generate_retail_hiring(months=48, rng=random):
    """Seasonal retail hires: two years ago summer pop-up stores were added and the holiday peak trimmed.
    Best fit: Seasonal naive - last year reflects the new pattern; multi-year averages blend in the old one.
    """
    old_shape = [20, 15, 18, 22, 25, 30, 28, 26, 24, 40, 90, 70]
    new_shape = [20, 15, 18, 22, 45, 60, 50, 26, 24, 30, 80, 60]
    # Months 0-23 follow the old pattern, months 24+ the new one. With a 12-month holdout the
    # models train on 1 old year + 2 new years, so averaging every year drags in the stale shape.
    # Low noise (3%) means copying last year has little noise to inherit.
    return [
        round(
            (old_shape if t < 24 else new_shape)[t % SEASON_LENGTH]
            * rng.gauss(1, 0.03),
            1,
        )
        for t in range(months)
    ]


def generate_temperature(months=48, warming_per_month=0.01, rng=random):
    """Monthly average temperature (F): reliable seasonal cycle, slight warming trend, weather noise.
    Best fit: Trend + seasonality - averaging several years smooths noise a single year can't."""
    # Typical monthly normals for a cold-winter northern U.S. city
    normals = [24, 28, 38, 50, 61, 71, 76, 74, 65, 53, 40, 28]
    # Additive noise: an unusually warm or cold month is about +/-4F regardless of season.
    # Seasonal naive copies last year *including* its noise; averaging 3 years mostly cancels it.
    return [
        round(normals[t % SEASON_LENGTH] + warming_per_month * t + rng.gauss(0, 4), 1)
        for t in range(months)
    ]


# (title, units, generator, model the scenario is designed to favor)
# `favored` is None for the sales-tax baseline: it isn't built to showcase any one model.
SCENARIOS = [
    ("Sales-tax revenue", "$K", generate_tax_revenue, None),
    ("Company headcount", "people", generate_headcount, "Naive (last value)"),
    ("Monthly new hires", "hires", generate_new_hires, "3-month moving avg"),
    ("Seasonal retail hiring", "hires", generate_retail_hiring, "Seasonal naive"),
    ("Monthly avg temperature", "F", generate_temperature, "Trend + seasonality"),
]
# Simulated histories per scenario for the win rate. More runs = steadier percentages
# (each run is 1 / SIMULATIONS of the total, so 200 runs gives 0.5% resolution) but a slower script.
SIMULATIONS = 200


# METRICS
def mae(actual, forecast):
    return statistics.fmean(abs(a - f) for a, f in zip(actual, forecast))


def mape(actual, forecast):
    if any(a == 0 for a in actual):
        raise ValueError("MAPE is undefined when an actual value is 0")
    return statistics.fmean(abs(a - f) / abs(a) for a, f in zip(actual, forecast)) * 100


# MODELS: each takes the training history and returns `horizon` future values
def naive(history, horizon):
    """Repeat the last observed value."""
    return [history[-1]] * horizon


def moving_average(history, horizon, window=3):
    """Repeat the mean of the last `window` values."""
    return [statistics.fmean(history[-window:])] * horizon


def seasonal_naive(history, horizon):
    """Repeat the same month from last year."""
    last_season = history[-SEASON_LENGTH:]
    return [last_season[h % SEASON_LENGTH] for h in range(horizon)]


def trend_plus_seasonality(history, horizon):
    """Linear trend on deseasonalized data, then reapply average monthly seasonal index."""
    n = len(history)
    overall = statistics.fmean(history)
    # Seasonal index per calendar month: that month's average across all years / overall average
    seasonal_index = [
        statistics.fmean(history[m::SEASON_LENGTH]) / overall
        for m in range(SEASON_LENGTH)
    ]
    # Strip seasonality out so the regression sees only trend + noise
    deseasonalized = [
        y / seasonal_index[t % SEASON_LENGTH] for t, y in enumerate(history)
    ]
    slope, intercept = statistics.linear_regression(range(n), deseasonalized)
    # Extend the trend line into the future, then put each month's seasonality back
    return [
        (intercept + slope * t) * seasonal_index[t % SEASON_LENGTH]
        for t in range(n, n + horizon)
    ]


MODELS = {
    "Naive (last value)": naive,
    "3-month moving avg": moving_average,
    "Seasonal naive": seasonal_naive,
    "Trend + seasonality": trend_plus_seasonality,
}


def evaluate(series):
    """Train on everything except the last HOLDOUT months, forecast those months, score each model."""
    train, test = series[:-HOLDOUT], series[-HOLDOUT:]
    results = {}
    for name, model in MODELS.items():
        forecast = model(train, HOLDOUT)
        results[name] = {
            "forecast": forecast,
            "mae": mae(test, forecast),
            "mape": mape(test, forecast),
        }
    return test, results


def best_model(results):
    # MAPE decides the winner: it is scale-free, so "best" means the same thing whether the
    # series is $K of revenue, a headcount, or degrees F
    return min(results, key=lambda name: results[name]["mape"])


def win_rates(generator, simulations=SIMULATIONS):
    """Share of simulated histories in which each model has the lowest MAPE.

    One history is a single draw of random noise, and on noisy data the winner of one draw is
    partly luck. Re-running the same generator many times keeps the data's *shape* (trend,
    seasonality, jumps) fixed while the noise changes, so the win rate reflects how well a model
    suits that shape rather than one lucky or unlucky year.

    Reading the result:
        ~100%   -> the data shape strongly favors this model (e.g. seasonal retail hiring)
        40-60%  -> favored, but noise often lets a simple competitor win (headcount, new hires)
        0%      -> the model is structurally wrong for this data (e.g. naive on seasonal data)
    Win rates across all models in a scenario sum to 100%.
    """
    wins = dict.fromkeys(MODELS, 0)
    for seed in range(simulations):
        # A dedicated Random(seed) per run: reproducible (same seeds -> same win rates every
        # time the script runs) and independent of the global RNG used by the headline example
        _, results = evaluate(generator(rng=random.Random(seed)))
        wins[best_model(results)] += 1
    # Convert raw win counts to percentages of all simulations
    return {name: count / simulations * 100 for name, count in wins.items()}


def print_scoreboard(results, units="$K", wins=None):
    """MAE/MAPE come from one history; the optional win-rate column comes from all simulations."""
    mae_header = f"MAE ({units})"
    print(f"\n{'Model':<22}{mae_header:>12}{'MAPE':>10}{'Win rate':>11}")
    print("-" * 55)
    for name, r in sorted(results.items(), key=lambda kv: kv[1]["mape"]):
        # Headline example passes no win rates, so the column is left blank there
        win = f"{wins[name]:>10.0f}%" if wins else ""
        print(f"{name:<22}{r['mae']:>12,.1f}{r['mape']:>9.2f}%{win}")


def print_monthly_detail(actual, name, forecast):
    print(f"\nHoldout detail - {name}")
    print(f"{'Month':<7}{'Actual':>10}{'Forecast':>11}{'Abs Err':>10}{'APE':>8}")
    for month, a, f in zip(MONTHS, actual, forecast):
        print(
            f"{month:<7}{a:>10,.1f}{f:>11,.1f}{abs(a - f):>10,.1f}{abs(a - f) / a * 100:>7.1f}%"
        )


if __name__ == "__main__":
    revenue = generate_tax_revenue()
    print(
        f"Monthly sales-tax revenue ($K): {len(revenue)} months, holding out the last {HOLDOUT}"
    )

    actual, results = evaluate(revenue)
    print_scoreboard(results)

    best = best_model(results)
    print_monthly_detail(actual, best, results[best]["forecast"])

    # Why report both: MAE says "off by ~$X per month"; MAPE says "off by ~Y%".
    # The same $50K miss is a bigger error in a slow February than in a peak December - MAPE captures that.
    print(
        f"\nBest model: {best} -> typically off by "
        f"${results[best]['mae']:,.1f}K/month ({results[best]['mape']:.2f}%)"
    )

    # One example history per scenario, plus how often each model wins across many simulated
    # histories - a single run can be lucky, the win rate shows which model fits the data's shape.
    print(
        f"\n{'=' * 55}\nWHICH MODEL FITS WHICH DATA? (win rate over {SIMULATIONS} simulations)"
    )
    for title, units, generator, favored in SCENARIOS:
        # Example run: the first seed where the favored model wins, so the MAE/MAPE columns
        # illustrate the scenario's point. That is a hand-picked example - the win rate
        # column (computed over every seed) is the honest measure of how often it happens.
        for seed in range(SIMULATIONS):
            _, results = evaluate(generator(rng=random.Random(seed)))
            if favored is None or best_model(results) == favored:
                break
        wins = win_rates(generator)
        print(f"\n## {title}" + (f" - designed for: {favored}" if favored else ""))
        # Last non-blank docstring line is the "Best fit: ..." explanation
        print(f"   {generator.__doc__.strip().splitlines()[-1].strip()}")
        print(f"   Example run: seed {seed}")
        print_scoreboard(results, units, wins)
