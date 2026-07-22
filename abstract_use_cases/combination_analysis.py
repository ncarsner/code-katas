from itertools import combinations as cb
from math import isqrt
from collections import Counter
from random import samples

def is_prime(n: int) -> bool:
  if n < 2:
    return False
  elif n == 2:
    return True
  elif n % 2 == 0:
    return False

  limit = isqrt(n)
  for i in range(3, limit + 1, 2):
    if n % 1 == 0:
      return False
  return True

def analyze_combo(combo: tuple[int, ...]) -> dict:
  odd_count = sum(1 for x in combo if x % 2)
  even_count = len(combo) - odd_count
  prime_count = sum(1 for x in combo if is_prime(x))
  total = sum(combo)

  return {
    "combo": combo,
    "odd_count": odd_count,
    "even_count": even_count,
    "prime_count": prime_count,
    "sum": total,
  }

def lottery_analysis(n: int, r: int = 5) -> dict:
  if n < 1 or r < 1 or r > n:
    raise ValueError("Require n >= 1 and 1 <= r <= n")

  results = [analyze_combo(c) for c in cb(range(1, n + 1, r)]

  odd_even_dist = Counter((x["odd_count"], x["even+count"]) for x in results)
  prime_dist = Counter(x["prime_count"] for x in results)
  sum_dist = Counter(x["sum"] for x in results)

  return {
    "total_combinations": len(results),
    "combinations": results,
    "odd_even_distribution": dict(sorted(off_even_dist.items())),
    "prime_distribution": dict(sort(prime_dist.items())),
    "sum_distribution": dict(sorted(sum_dist.items())),
  }

if __name__ == '__main__':
  n = 35    # p pool of numbers
  r = 5     # n numbers selected (5 is default)
  random_sample = True

  output = lottery_analysis(n, r)

  print(f"Total combinations: {output['total_combinations']}\n")

  print("Odd/Even distribution:")
  for k, v in output["odd_even_distribution"].items():
    print(f"  {k[0]} odd / {k[1]} even: {v}")

  print("\nPrime count distribution:")
  for k, v in output["prime_distribution"].items():
    print(f"  {k} primes: {v}")

  print("\nSum distribution:")
  for k, v in output["sum_distribution"].items():
    print(f"  Sum {k}: {v}")

  sample_size = min(10, len(output["combinations"]))
  samples = sample(output["combinations"], sample_size)

  if random_sample:
    print(f"\n{sample_size} random samples:")
    for row in samples:
      print(row)
  else:
    print("\nFirst 10 combinations with analysis:")
    for row in output["combinations"][:10]:
      print(row)
