import random

letters = {
    "a": ["ay", "eigh"],
    "b": ["be", "bee"],
    "c": ["see", "sea", "ce"],
    "d": ["dee", "de"],
    "e": ["ee", "eye"],
    "f": ["ef", "eff"],
    "g": ["gee", "je"],
    "h": ["aitch"],
    "i": ["eye"],
    "j": ["jay"],
    "k": ["kay", "kai"],
    "l": ["el", "ell"],
    "m": ["em", "emm"],
    "n": ["en", "enn"],
    "o": ["oh"],
    "p": ["pee"],
    "q": ["cue", "queue"],
    "r": ["are", "ar"],
    "s": ["ess", "es"],
    "t": ["tea", "tee", "te"],
    "u": ["you", "ou"],
    "v": ["vee", "ve"],
    "w": ["uu"],
    "x": ["ex"],
    "y": ["why"],
    "z": ["zee", "zed"],
}


def generate_combinations(n):
    keys = list(letters.keys())
    combinations = []

    for _ in range(n):
        int_min = 2
        int_max = 4
        selected_keys = random.sample(keys, random.randint(int_min, int_max))
        combination = "".join(random.choice(letters[key]) for key in selected_keys)
        combinations.append(combination)

    return combinations


if __name__ == "__main__":
    n = 10
    result = generate_combinations(n)
    for combo in result:
        print(combo)
