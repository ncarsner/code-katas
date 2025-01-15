import random

adjectives = {
    # "a": [],
    # "b": [],
    "c": ["Crimson", "Cross-Eyed"],
    "d": ["Delinquent", "Diversive"],
    "e": ["Excellent", "Effington"],
    "f": ["Fetid", "Ferrous", "Foolish"],
    # "g": [],
    # "h": [],
    # "i": [],
    # "j": [],
    # "k": [],
    "l": ["Libertarian", "Leaping"],
    # "m": [],
    "n": ["Nefarious"],
    "o": ["Oblivious"],
    "p": ["Pernicious"],
    # "q": [],
    "r": ["Renegade"],
    "s": ["Subversive"],
    "t": ["Tranquil", "Topaz"],
    # "u": [],
    # "v": [],
    # "w": [],
    # "x": [],
    # "y": [],
    # "z": [],
}

nouns = {
    "a": ["Absolution", "Aficionado", "Amethyst"],
    "b": ["Biscuit"],
    "c": ["Carpaccio"],
    "d": ["Delinquent"],
    "e": ["Eucharist"],
    # "f": [],
    # "g": [],
    # "h": [],
    # "i": [],
    # "j": [],
    # "k": [],
    "l": ["Libertarian"],
    "m": ["Maelstrom"],
    # "n": [],
    "o": ["Oblivion"],
    "p": [],
    # "q": [],
    "r": ["Renegade"],
    # "s": [],
    "t": ["Topaz"],
    # "u": [],
    # "v": [],
    # "w": [],
    # "x": [],
    # "y": [],
    # "z": [],
}

def generate_business_name(n):
    if n < 2:
        raise ValueError("n must be at least 2")

    filtered_adjectives = {k: v for k, v in adjectives.items() if v}
    filtered_nouns = {k: v for k, v in nouns.items() if v}

    if n > len(filtered_adjectives) + 1:
        raise ValueError("n is larger than the number of available words")

    selected_adjective_keys = random.sample(list(filtered_adjectives.keys()), n - 1)
    selected_noun_key = random.choice(list(filtered_nouns.keys()))

    business_name_parts = [
        random.choice(filtered_adjectives[key]) for key in selected_adjective_keys
    ]
    business_name_parts.append(random.choice(filtered_nouns[selected_noun_key]))

    return " ".join(business_name_parts)

if __name__ == "__main__":
    names = 5
    for i in range(names):
        print(generate_business_name(random.randint(2, 3)))
