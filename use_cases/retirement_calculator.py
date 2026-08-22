"""Estimate a retirement balance from monthly contributions and growth."""


def estimate_retirement_balance(
    annual_return: float,
    monthly_contribution: float,
    starting_balance: float,
    years: float,
    annual_contribution_increase: float = 0,
) -> float:
    """Return the estimated balance; raise contributions once per year."""
    if years < 0:
        raise ValueError("years cannot be negative")
    if starting_balance < 0 or monthly_contribution < 0:
        raise ValueError("balances and contributions cannot be negative")
    if annual_return <= -1:
        raise ValueError("annual return must be greater than -100%")
    if annual_contribution_increase <= -1:
        raise ValueError("contribution increase must be greater than -100%")

    monthly_rate = annual_return / 12
    balance = starting_balance

    for month in range(round(years * 12)):
        balance = balance * (1 + monthly_rate) + monthly_contribution
        if (month + 1) % 12 == 0:
            monthly_contribution *= 1 + annual_contribution_increase

    return balance


if __name__ == "__main__":
    estimated_balance = estimate_retirement_balance(
        annual_return=0.06,
        monthly_contribution=1500,
        starting_balance=100_000,
        years=20,
        annual_contribution_increase=0.015
    )
    print(f"Estimated retirement balance: ${estimated_balance:,.2f}")
