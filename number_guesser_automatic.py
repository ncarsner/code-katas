import random
import timeit

congrats = [
    "Way to go!",
    "Good work!",
    "Well done!",
    "Very clever!",
    "Great work.",
    "Excellent deduction.",
]
shames = [
    "So close.",
    "Awwww.",
    "Guesses exhausted.",
    "Not this time!",
    "Incorrect.",
    "Just missed.",
    "Maybe next time.",
]
maxNum = int(input("Enter a max number: "))
secretNum = random.randint(1, maxNum)
guess = maxNum // 2  # first guess is half of max value
guesses_over = [maxNum]
guesses_under = [1]
list_of_guesses = [guess]
guess_index = 1

# execution start timer
starttime = timeit.default_timer()

for guessesTaken in range(1, 100):
    if guess > secretNum:
        guesses_over.append(guess)
        if (max(guesses_under) + guess) // 2 in list_of_guesses:
            guess -= 1
        else:
            guess = (max(guesses_under) + guess) // 2
    elif guess < secretNum:
        guesses_under.append(guess)
        if (min(guesses_over) + guess) // 2 in list_of_guesses:
            guess += 1
        else:
            guess = (min(guesses_over) + guess) // 2
    else:
        break  # this condition is the correct guess
    list_of_guesses.append(guess)

if guess == secretNum:
    message = random.randint(0, len(congrats) - 1)
    print(
        f"{congrats[message]} The number {secretNum:,} was guessed in {guessesTaken} tries"
    )
else:
    message = random.randint(0, len(shames) - 1)
    print(f"{shames[message]} The number was {secretNum:,}")

print(list_of_guesses)

# execution time calculator
print("Execution time: ", round((timeit.default_timer() - starttime) * 1000, 3), " ms")
