from collections import defaultdict
import sys


def count_word_frequency(file_path):
    word_frequency = defaultdict(int)
    with open(file_path, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_frequency[word] += 1
    return dict(word_frequency)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    word_counts = count_word_frequency(file_path)

    for word, count in word_counts.items():
        print(f"{word}: {count}")
