import random

word_list = {
    "a": ['Absolution'],
    "b": ['Biscuit'],
    "c": ['Crimson', 'Carpaccio'],
    "d": ['Delinquent'],
    "e": ['Excellent', 'Effington'],
    # "f": [''],
    # "g": [''],
    # "h": [''],
    # "i": [''],
    # "j": [''],
    # "k": [''],
    "l": ['Libertarian'],
    # "m": [''],
    # "n": [''],
    # "o": [''],
    # "p": [''],
    # "q": [''],
    "r": ['Renegade'],
    "s": ['Subversive'],
    # "t": [''],
    # "u": [''],
    # "v": [''],
    # "w": [''],
    # "x": [''],
    # "y": [''],
    # "z": [''],
}

def generate_business_name(n):
    filtered_word_list = {k: v for k, v in word_list.items() if v}
    
    if n > len(filtered_word_list):
        raise ValueError("n is larger than the number of available letters")
    
    selected_keys = random.sample(list(filtered_word_list.keys()), n)
    business_name_parts = [random.choice(filtered_word_list[key]) for key in selected_keys]
    
    return ' '.join(business_name_parts)

# Example usage:
print(generate_business_name(random.randint(2, 3)))