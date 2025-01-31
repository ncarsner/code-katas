import random

adjectives = {
    "a": ["Atomic"],
    # "b": [],
    "c": ["Crimson", "Cross-Eyed", "Cryptic"],
    "d": ["Delinquent", "Diversive", "Deluded", "Diluted"],
    "e": ["Excellent", "Effington", "Ephemeral"],
    "f": ["Fetid", "Ferrous", "Foolish"],
    "g": ["Gibbous"],
    "h": ["Hapless"],
    "i": ["Indifferent"],
    "j": ["Jovial"],
    # "k": [],
    "l": ["Libertarian", "Leaping", "Lefty"],
    "m": ["Misspellled"],
    "n": ["Nefarious"],
    "o": ["Oblivious", "Obvious"],
    "p": ["Pernicious", "Phosphorescent", "Prostrated", "Polymorphic"],
    # "q": [],
    "r": ["Renegade"],
    "s": ["Subversive", "Seeting", "Sanguine", "Seething"],
    "t": ["Tranquil", "Topaz"],
    # "u": [],
    "v": ["Vermillion"],
    # "w": [],
    # "x": [],
    "y": ["Yapping"],
    "z": ["Zesty"],
}

nouns = {
    "a": ["Absolution", "Aficionado", "Amethyst"],
    "b": ["Biscuit"],
    "c": ["Carpaccio", "Cranberry"],
    "d": ["Delinquent", "Duck"],
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
    "p": ["Pickle", "Poly Blend"],
    # "q": [],
    "r": ["Renegade", "Rage Mouth"],
    "s": ["Sauce"],
    "t": ["Topaz", "Toboggan"],
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
