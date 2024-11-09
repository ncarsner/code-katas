import random
# import itertools

random_generations = []
random_guesses = []

no_of_guesses = random.randint(20, 200)
guess_exact = 0
guess_included = 0

max_number = 35

# list_of_possibilities = ['Alex','Blake','Chris','Dylan','Elliott','Flynn','Gene','Henri','Irene','Julio']
list_of_possibilities = [i for i in range(1, max_number + 1)]

for i in range(no_of_guesses):
    random_generations.append(random.choice(list_of_possibilities))

for j in range(no_of_guesses):
    random_guesses.append(random.choice(list_of_possibilities))

for m, n in zip(random_generations, random_guesses):
    if m == n:
        guess_exact += 1
    if n in random_generations:
        guess_included += 1

# print(random_generations)
# print(random_guesses)

print(f"Number of guesses: {no_of_guesses}")
# print(f'Exact guesses by position: {guess_exact}')
print(f"Exact guesses by position: {guess_exact/no_of_guesses:.1%}")

# print(f'Guess included in list: {guess_included}')
print(f"Guess included in list: {guess_included/no_of_guesses:.1%}")
