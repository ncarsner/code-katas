import random


# One-liner
round_to_nearest = lambda x, n=5: (  # noqa: E731
    [round(i / n) * n for i in x] if hasattr(x, "__iter__") else round(x / n) * n
)


# Function
def round_to_nearest_func(value, n=5):
    if hasattr(value, "__iter__"):
        return [round(i / n) * n for i in value]
    return round(value / n) * n


# Lambda
round_to_nearest_lambda = lambda x, n=5: (  # noqa: E731
    [round(i / n) * n for i in x] if hasattr(x, "__iter__") else round(x / n) * n
)


if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(5)]
    nearest = random.randint(2, 5)

    print(f"\n{nums=}")
    print(f"{nearest=}")

    print(f"\nOne-liner: {round_to_nearest(nums, nearest)}")
    print(f"Function: {round_to_nearest_func(nums, nearest)}")
    print(f"Lambda: {round_to_nearest_lambda(nums, nearest)}")
