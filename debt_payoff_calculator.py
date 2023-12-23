"""
GOAL: Calculate a monthly debt repayment amount
including starting balance, target end balance, additional monthly spend,
interest rate and number of periods over which to pay off the debt based on user inputs.
"""

try:
    balance = int(input("Current balance in whole dollars? ").replace(",", ""))
    target = int(input("Target end balance in whole dollars? ").replace(",", ""))
    rate = float(input("Percentage Rate? (e.g. 19.99) ").replace(",", "."))
    rate /= 100
    periods = int(input("Number of months to pay across? "))
    accrued = int(input("Additional spend per period? "))
    payment = (
        rate / 12 * (1 / (1 - (1 + rate / 12) ** (-periods)) * (balance - target))
        + accrued
    ) - (rate / periods)

except (ValueError, NameError):
    print("Please enter a valid value: ")
finally:
    print(f"\nStarting balance: $ {balance:,}")
    print(f"End balance: $ {target:,}")
    print(f"Monthly payment: $ {payment:,.2f}")


# # SAMPLE OUTPUT
# >>> Current balance in whole dollars? 5,000
# >>> Target end balance in whole dollars? 250
# >>> Percentage Rate? (e.g. 19.99) 24.99
# >>> Number of months to pay across? 24
# >>> Additional spend per period? 175

# >>> Starting balance: $ 5,000
# >>> End balance: $ 250
# >>> Monthly payment: $ 428.48
