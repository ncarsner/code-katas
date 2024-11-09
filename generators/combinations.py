from itertools import combinations as cb
from collections import Counter
import random

n = 38
s = 5
target_sum_pop = 0.7
nums = [n for n in range(1, n + 1)]
combos = [c for c in cb(nums, s)]
combo_sums = [sum(c) // 5 * 5 for c in combos]
primes = [x for x in range(2, n) if not any(x % y == 0 for y in range(2, x))]
common_draws = Counter(combo_sums).most_common()

tgt_sums = []
total_sums = 0

for i in common_draws:
    total_sums += i[1]
    if total_sums / len(combos) < target_sum_pop:
        tgt_sums.append(i[0])

tgt_sum_combos = [c for c in combos if sum(c) // 5 * 5 in tgt_sums]

for i in range(10):
    # print(random.choice(tgt_sum_combos))
    # print(random.choice(combos))
    ...

# print(len(combos))


# print(len(tgt_sum_combos))
def evaluate_combinations(x):
    matches = {3: 0, 4: 0, 5: 0}
    random_selection = random.choice(tgt_sum_combos)
    for _ in range(x):
        random_combo = random.choice(tgt_sum_combos)
        match_count = len(set(random_combo) & set(random_selection))
        if match_count in matches:
            matches[match_count] += 1
    return matches, random_selection


x = 1_000
result = evaluate_combinations(x)[0]
print(f"Combination: {evaluate_combinations(x)[1]}")
print(f"Out of {x} combinations:")
print(f"3 matches: {result[3]}")
print(f"4 matches: {result[4]}")
print(f"5 matches: {result[5]}")
