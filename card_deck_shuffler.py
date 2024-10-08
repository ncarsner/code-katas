import random

# Define the suits and values
suits = ['♠️', '♥️', '♦️', '♣️']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Create the deck of cards
deck = [f"{value}{suit}" for suit in suits for value in values]
original_deck = deck.copy()

def perfect_shuffle(deck):
    half = len(deck) // 2
    shuffled_deck = []
    for i in range(half):
        shuffled_deck.append(deck[i])
        shuffled_deck.append(deck[half + i])
    return shuffled_deck

def display_deck(deck, n=5):
    print(f"First {n} cards: {deck[:n]}")
    print(f"Last {n} cards: {deck[-n:]}")

# Initial deck
print("Initial deck:")
display_deck(deck)

shuffle_count = 0
while True:
    deck = perfect_shuffle(deck)
    shuffle_count += 1
    print(f"\nAfter shuffle {shuffle_count}:")
    display_deck(deck)
    if deck == original_deck:
        print(f"\nDeck returned to original order after {shuffle_count} shuffles.")
        break