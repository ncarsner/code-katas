from itertools import combinations
import random
from prettytable import PrettyTable


def get_user_choice(item1, item2):
    while True:
        choice = input(f"Which do you prefer? (1) {item1} or (2) {item2}: ")
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")


def calculate_completion(current, total):
    return (current / total) * 100


def additional_comparisons(ranked_items):
    return [
        (ranked_items[i], ranked_items[i + 1])
        for i in range(len(ranked_items) - 1)
        if ranked_items[i] == ranked_items[i + 1]
    ]


def rank_items(items):
    comparisons = list(combinations(items, 2))
    random.shuffle(comparisons)
    total_comparisons = len(comparisons)

    item_scores = {item: 0 for item in items}
    item_counts = {item: 0 for item in items}

    for completed_comparisons, (item1, item2) in enumerate(comparisons, start=1):
        print(
            f"Progress: {calculate_completion(completed_comparisons, total_comparisons):.2f}%"
        )
        choice = get_user_choice(item1, item2)
        if choice == 1:
            item_scores[item1] += 1
        else:
            item_scores[item2] += 1
        item_counts[item1] += 1
        item_counts[item2] += 1

    final_ranking = sorted(items, key=lambda item: item_scores[item], reverse=True)

    additional_comps = additional_comparisons(final_ranking)
    for item1, item2 in additional_comps:
        choice = get_user_choice(item1, item2)
        if choice == 1:
            final_ranking.remove(item2)
            final_ranking.insert(final_ranking.index(item1) + 1, item2)
        else:
            final_ranking.remove(item1)
            final_ranking.insert(final_ranking.index(item2) + 1, item1)

    return create_pretty_table(final_ranking, item_scores, item_counts)


def create_pretty_table(final_ranking, item_scores, item_counts):
    table = PrettyTable()
    table.field_names = ["Item", "Rank", "Score", "Comparisons"]

    for rank, item in enumerate(final_ranking, start=1):
        table.add_row([item, rank, item_scores[item], item_counts[item]])

    return table


if __name__ == "__main__":
    movies = [
        "Elf",
        "Die Hard",
        "A Christmas Story",
        "Klaus",
        "Scrooged",
        "Christmas Vacation",
        "The Family Stone",
        "Home Alone",
        "Bad Santa",
        "Love Actually",
    ]
    ranked_table = rank_items(movies)
    print("Final ranking of movies:")
    print(ranked_table)
