"""
GOAL: Calculate a monthly savings target from a user-friendly input array of savings goal
starting balance, monthly savings rate and number of months over which to save.
"""

input_error = "Please enter a valid number."
range_error = "Please enter months between 1 and 10,000"
negative_error = "Please enter a value greater than 0"

goal = g = 0
principal = p = -1
rate = r = 0
periods = n = 0

while not 0 < g:
    try:
        g = int(input("Savings goal balance? "))
    except ValueError as e:
        print(e, input_error)
while not 0 <= p < g:
    try:
        p = int(input("Current balance? "))
    except ValueError as e:
        print(e, input_error)
while not 0 < r:
    try:
        r = float(input("Interest rate? (e.g. 2.25) "))
        r /= 100
    except ValueError as e:
        print(e, input_error)
while not 0 < n < 10000:
    try:
        n = int(input("Number of months to save? "))
    except ValueError as e:
        print(e, range_error)

d = (r / 12 * (g - p * (1 + (r / 12)) ** n)) / ((1 + (r / 12)) ** n - 1)
print(f"\nGoal: $ {p:,} to $ {g:,} over {n} months at {r:.2%}")
print(f"Save $ {d:,.2f} per month")


# SAMPLE OUTPUT
# Savings goal balance? 5000
# Current balance? 250
# Interest rate? (e.g. 2.25) 1.75
# Number of months to save? 18

# Goal: $ 250 to $ 5,000 over 18 months at 1.75%
# Save $ 260.27 per month
