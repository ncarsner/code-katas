import pandas as pd


def calculate_balance(balance, monthly_payment, term, apr):
    """Calculates the balance reduction over time given a ficurrent_balanceed payment and daily compounding interest rate."""
    daily_rate = apr / 365
    records = []

    for month in range(1, term + 1):
        days_in_month = int(365 / 12)
        for _ in range(days_in_month):
            balance += balance * daily_rate

        balance = max(0, balance - monthly_payment)
        records.append((month, round(balance, 2)))

        if balance == 0:
            break

    return records


def analyze_balance_transfer(current_balance, current_payment, transfer_payment):
    """Analyzes and compares the two repayment scenarios."""
    original_balance = current_balance
    transferred_balance = current_balance * 1.03  # 3% increase on transfer

    original_plan = calculate_balance(original_balance, current_payment, 15, 0.0929)
    transferred_plan = calculate_balance(transferred_balance, transfer_payment, 15, 0.0099)

    df_original = pd.DataFrame(original_plan, columns=["Month", "Balance (Original)"])
    df_transferred = pd.DataFrame(
        transferred_plan, columns=["Month", "Balance (Transferred)"]
    )

    df_result = pd.merge(df_original, df_transferred, on="Month", how="outer").fillna("-")

    print("Balance Transfer Analysis:")
    print(df_result.to_string(index=False))

    total_cost_original = sum(current_payment for _ in original_plan)
    total_cost_transferred = sum(transfer_payment for _ in transferred_plan)

    final_balance_original = df_original.iloc[-1, 1] if not df_original.empty else 0
    final_balance_transferred = (
        df_transferred.iloc[-1, 1] if not df_transferred.empty else 0
    )
    balance_savings = final_balance_original - final_balance_transferred

    print(f"Total cost of original: ${total_cost_original:,.2f}")
    print(f"Total cost of transfer: ${total_cost_transferred:,.2f}")
    print(f"Final balance of original: ${final_balance_original:,.2f}")
    print(f"Final balance of transfer: ${final_balance_transferred:,.2f}")
    print(f"Balance reduction with the transfer: ${balance_savings:,.2f}")

    return df_result, total_cost_original, total_cost_transferred, balance_savings


if __name__ == "__main__":
    current_balance = 10_000
    current_payment = 500
    transfer_payment = 500
    df, cost_original, cost_transferred, balance_savings = analyze_balance_transfer(current_balance, current_payment, transfer_payment)
