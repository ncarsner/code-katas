import itertools

# itertools.count
for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)
# Output: 10, 12, 14, 16, 18, 20
# Use-case: Generate an infinite sequence with specific intervals.

# Function: Generates infinite sequence starting from a given value with a given step.
user_count = itertools.count(1001)
for _ in range(5):
    print(next(user_count))
# Use-case: Assigning unique ID numbers to new users in a system.


# itertools.cycle
counter = 0
for item in itertools.cycle("ABC"):
    if counter > 8:
        break
    print(item)
    counter += 1
# Output: A, B, C, A, B, C, A, B, C
# Use-case: Repeat a finite sequence indefinitely.

# Function: Cycles through an iterable indefinitely.
servers = itertools.cycle(["Server1", "Server2", "Server3"])
tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
for task in tasks:
    server = next(servers)
    print(f"{task} assigned to {server}")
# Use-case: Simple load balancer distributing tasks among servers.


# itertools.repeat
for item in itertools.repeat("A", 3):
    print(item)
# Output: A, A, A
# Use-case: Repeat a finite sequence indefinitely.

# Function: Repeats an item for the specified times.
default_values = list(itertools.repeat(0, 5))
print(default_values)
# Use-case: Initializing a list with default values.


# itertools.accumulate
print(list(itertools.accumulate([1, 2, 3, 4], lambda x, y: x * y)))
# Output: [1, 2, 6, 24]  # Factorial
# Use-case: Calculate running totals or products.

# Function: Returns accumulated results.
monthly_sales = [100, 150, 200, 250]
total_sales = list(itertools.accumulate(monthly_sales))
print(total_sales)
# Use-case: Calculating running total of monthly sales.


print(list(itertools.chain([1, 2], [3, 4])))
# Output: [1, 2, 3, 4]
# Use-case: Combine multiple sequences into one.

# Function: Chains iterables together.
system1_logs = ["Log1", "Log2"]
system2_logs = ["Log3", "Log4"]
all_logs = list(itertools.chain(system1_logs, system2_logs))
print(all_logs)
# Use-case: Consolidating logs from multiple systems.


print(list(itertools.chain.from_iterable([[1, 2], [3, 4]])))
# Output: [1, 2, 3, 4]
# Use-case: Flatten nested sequences.

# Function: Chains iterables from a single iterable.
comments_from_posts = [["Comment1", "Comment2"], ["Comment3", "Comment4"]]
all_comments = list(itertools.chain.from_iterable(comments_from_posts))
print(all_comments)
# Use-case: Merging lists of user comments from different blog posts.


data = ["A", "B", "C"]
selectors = [True, False, True]
print(list(itertools.compress(data, selectors)))
# Output: ['A', 'C']
# Use-case: Filter elements based on a secondary sequence.

# Function: Filters elements using selectors.
products = ["apple", "banana", "cherry"]
in_stock = [True, False, True]
available_products = list(itertools.compress(products, in_stock))
print(available_products)
# Use-case: Filtering available products based on a stock list.


print(list(itertools.dropwhile(lambda x: x < 5, [1, 3, 7, 6, 5, 8])))
# Output: [7, 6, 5, 8]
# Use-case: Skip elements until a condition is met.

# Function: Drops elements while predicate is true, then returns the rest.
pages = ["", "", "Page1_Content", "Page2_Content"]
content_pages = list(itertools.dropwhile(lambda x: not x, pages))
print(content_pages)
# Use-case: Skip pages without content when parsing a document.


print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))
# Output: [1, 3, 5, 7, 9]
# Use-case: Filter out elements based on a predicate.

# Function: Filters elements where the predicate is false.
hours = range(0, 24)
working_hours = list(itertools.filterfalse(lambda x: x < 9 or x > 17, hours))
print(working_hours)
# Use-case: Removing non-working hours from a list.


data = [("A", 1), ("B", 2), ("A", 3)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(key, list(group))
# Output: A [('A', 1)], B [('B', 2)], A [('A', 3)]
# Use-case: Group consecutive elements by a key function.

# Function: Groups consecutive elements by a key.
orders = [("C1", "Order1"), ("C2", "Order2"), ("C1", "Order3")]
for key, group in itertools.groupby(sorted(orders, key=lambda x: x[0]), lambda x: x[0]):
    print(key, list(group))
# Use-case: Grouping orders by customer ID.


print(list(itertools.islice(range(10), 2, 8, 2)))
# Output: [2, 4, 6]
# Use-case: Slice an iterable with start, stop, and step.

# Function: Slices an iterable.
lines = ["Line1", "Line2", "Line3", "Line4", "Line5"]
preview_lines = list(itertools.islice(lines, 0, 3))
print(preview_lines)
# Use-case: Displaying the first few lines of a large text file.


data = [(1, 2), (3, 4)]
print(list(itertools.starmap(lambda x, y: x * y, data)))
# Output: [2, 12]
# Use-case: Map a function that takes multiple arguments.

# Function: Maps function using arguments unpacked from iterable.
rectangles = [(2, 3), (4, 5), (6, 7)]  # Each tuple is (width, height)
areas = list(itertools.starmap(lambda w, h: w * h, rectangles))
print(areas)
# Use-case: Calculate areas of multiple rectangles.


print(list(itertools.takewhile(lambda x: x < 5, [1, 3, 7, 6, 5, 8])))
# Output: [1, 3]

# Function: Returns elements as long as the predicate is true.
lines = ["Content1", "Content2", "End", "MoreContent"]
content_up_to_end = list(itertools.takewhile(lambda x: x != "End", lines))
print(content_up_to_end)
# Use-case: Reading a document until a delimiter or specific line.


# Function: Returns n independent iterators from an input iterable.
data = range(5)
iter1, iter2 = itertools.tee(data, 2)
print(list(iter1), list(iter2))


# Function: Zips input iterables, filling missing values with a fillvalue.
data1 = ["A", "B", "C"]
data2 = [1, 2]
merged_data = list(itertools.zip_longest(data1, data2, fillvalue="N/A"))
print(merged_data)
# Use-case: Merging data from different sources with potential missing entries.


# Function: Returns r-length tuples of elements from iterable.
candidates = ["Alice", "Bob", "Charlie"]
pairs = list(itertools.combinations(candidates, 2))
print(pairs)
# Use-case: Finding potential pairs for a team project from a list of candidates.


# Function: Returns r-length tuples with repeated elements.
colors = ["Red", "Blue"]
combinations = list(itertools.combinations_with_replacement(colors, 2))
print(combinations)
# Use-case: Possible color combinations for a design with repetitions allowed.


# Function: Returns r-length tuples, all possible orderings, no repeated elements.
members = ["Eve", "Frank", "Grace"]
arrangements = list(itertools.permutations(members, 2))
print(arrangements)
# Use-case: All possible seating arrangements for a small committee.


# Function: Cartesian product of input iterables.
sizes = ["Small", "Medium"]
colors = ["White", "Black"]
configurations = list(itertools.product(sizes, colors))
print(configurations)
# Use-case: All possible product configurations for a customizable product.
