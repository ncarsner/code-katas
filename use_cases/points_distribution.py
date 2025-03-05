import itertools

def combinations_adding_to_10():
    # Generate all combinations of numbers between 0 and 10 that add up to 10
    all_combinations = itertools.product(range(11), repeat=3)
    
    # Filter combinations where the sum is 10
    combinations_sum_10 = filter(lambda x: sum(x) == 10, all_combinations)
    
    # Convert combinations to list and sort them in reverse order
    sorted_combinations = sorted(combinations_sum_10, reverse=True)
    
    # Return the sorted combinations
    return list(sorted_combinations)

# Example usage:
result = combinations_adding_to_10()
for combo in result:
    print(combo)

# print(len(result))


def convert_to_letter_representations(tuple_of_tuples):
    letter_representations = []
    for t in tuple_of_tuples:
        max_values = [num for num in t if num == max(t)]
        min_nonzero_value = min(num for num in t if num != 0)
        converted = []
        for num in t:
            if num in max_values:
                converted.append('A')
            elif num == min_nonzero_value and t.count(num) > 1:
                converted.append('B')
            elif num == 0:
                converted.append('D')
            else:
                converted.append('C')
        letter_representations.append(tuple(converted))
    return tuple(letter_representations)


# Example usage:
result = combinations_adding_to_10()
for combo in result:
    print(combo, convert_to_letter_representations((combo,)))



