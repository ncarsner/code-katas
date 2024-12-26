from random import choice


def generate_coin_flips(num_flips=1000):
    coin = ["H", "T"]
    flips = [choice(coin) for _ in range(num_flips)]
    return flips


def consecutive_flips(flips, threshold=5):
    count = 0
    current_streak = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
        else:
            if current_streak >= threshold:
                count += 1
            current_streak = 1

    # Check the last streak
    if current_streak >= threshold:
        count += 1

    return count


if __name__ == "__main__":
    total_flips = 0
    total_sequences = 0

    number_of_flips = 1000
    consecutive_flips_threshold = 8

    for i in range(10):
        flips = generate_coin_flips(number_of_flips)
        sequences = consecutive_flips(flips, consecutive_flips_threshold)

        total_flips += number_of_flips
        total_sequences += sequences

        # print(f"Events: {''.join([i for i in flips])}")
        # print(f"{consecutive_flips_threshold}+ Flips: {sequences}")

print(f"{total_flips = :,}")
print(f"{total_sequences = :,}")
print(f"{total_sequences / (total_flips / consecutive_flips_threshold) = :.1%}")
