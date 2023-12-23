"""
GOAL: iterate list items across specified range
"""

from random import choice, shuffle

diet_items = [
 'alcohol', 'beef', 'beer', 'brown liquor', 'butter',
 'coffee', 'caffeine', 'carbs', 'cheese',
 'chocolate', 'dairy', 'fast food', 'fried foods',
 'gluten', 'packaged foods', 'pork', 'processed foods',
 'red meat', 'salt', 'spirits', 'sugar', 'sweets',
 '', # intentionally blank for BREAK
]

weeks = 52
increment = weeks // len(diet_items)
shuffle(diet_items)

### to generate a list with a randomly selected item for each week of the year

def one_item_each_week():
    for c, i in enumerate(range(weeks), start=1):
      selection = choice(diet_items)
    if selection == '':
      print(f'Week {c}: BREAK')
    else:
      print(f'Week {c}: no {selection}')

# to generate a list of all items, evenly distributed through the year

def all_items_distributed():
    i = 1
    while len(diet_items):
        if diet_items[0] == '':
            print(f'Week {i}: BREAK')
            i += increment
            diet_items.pop(0)
        else:
            print(f'Week {i}: no {diet_items[0]}')
            i += increment
            diet_items.pop(0)

if __name__ == '__main__':
    # one_item_each_week()
    all_items_distributed()