import decorators
import random

# @decorators.timer
# def example_function(n):
#     odds_total = sum([i for i in range(n)])

#     return odds_total

@decorators.timer
def example_function():
    # Simulating some time-consuming operation
    total = 0
    for i in range(1000000):
        total += i
    return total

example_function()

@decorators.progress_bar
def example_iterable_function(n):
    odds_total = 0
    for i in range(n**2):
        for j in range(n):
            odds_total += sum(i*j)
    return odds_total

example_iterable_function(50_000)

# @decorators.progress_bar
# def example_iterable_function():
#     # Simulating an iterable generating operation
#     iterable = range(1000)
#     return iterable

# # Iterate through the result of the function
# for item in example_iterable_function():
#     # Simulate processing each item
#     pass

a = random.randint(1,100)
b = random.randint(1,100)

@decorators.debug
def example_function(x, y):
    return x + y

result = example_function(a, b)
