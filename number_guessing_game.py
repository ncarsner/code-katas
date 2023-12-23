"""
GOAL: Create a command line-executable number guessing game.
"""

from random import randint

max_number = randint(1, int(input("Maximum number? ")))
max_guesses = int(input("Maximum number of guesses? "))

c = 0

while c < max_guesses:
    guess = int(input(f"Guess {c+1}: "))
    if guess == max_number:
        if c == 0:
            print(f"You got it in {c+1} try!")
            break
        else:
            print(f"You got it in {c+1} tries!")
            break
    elif guess < max_number:
        c += 1
        print(f"Too low -- {max_guesses-c} guesses left")
    else:
        c += 1
        print(f"Too high -- {max_guesses-c} guesses left")

print(f"\nThe number was {max_number}.")

# SAMPLE OUTPUT
# >>> Maximum number? 20
# >>> Maximum number of guesses? 10
# >>> Guess 1: 10
# Too low -- 9 guesses left
# >>> Guess 2: 15
# Too high -- 8 guesses left
# >>> Guess 3: 12
# Too high -- 7 guesses left
# >>> Guess 4: 11
# You got it in 4 tries!

# The number was 11.
