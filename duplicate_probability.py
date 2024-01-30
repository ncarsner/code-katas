from math import factorial
from prettytable import PrettyTable

pool = 69
drawn = 5
bonus = 26

# for factoring duplicates in randomly generated Powerball tickets
combos = factorial(pool) // (factorial(drawn) * factorial(pool - drawn)) * bonus
factors = [100, 5_000, 10_000, 25_000, 50_000]

# for factoring a shared birthday among a group of people
combos = 365.25
factors = [5, 10, 15, 20, 25, 30]

def duplicate_probability():
    results = []

    for factor in factors:
        probability = 1.0
        for i in range(factor):
            probability *= (combos - i) / combos
        probability = 1 - probability
        results.append((factor, probability))

    return results

results = duplicate_probability()

table = PrettyTable()
table.field_names = ["Factors", "Probability"]

for factor, probability in results:
    table.add_row([f"{factor:,}", f"{probability:.3%}"])

print(table)
