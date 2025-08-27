import random


def get_operations():
    return {
        "add": ("+", lambda x, y: x + y),
        "sub": ("-", lambda x, y: x - y),
        "mul": ("*", lambda x, y: x * y),
        "div": ("/", lambda x, y: f"{x // y}" if x % y == 0 else f"{x // y}r{x % y}"),
        "exp": ("**", lambda x, y: x**y),
    }


def math_dictionary(operator, x, y):
    operations = get_operations()
    symbol, operation = operations.get(operator, ("", lambda x, y: None))
    return operation(x, y), symbol


# Now you can get the list of operators like this:
operators = list(get_operations().keys())


for i in range(10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    selected_operator = random.choice(operators)

    result, symbol = math_dictionary(selected_operator, a, b)

    # Format result with thousands separator if it's a number
    if isinstance(result, (int, float)):
        formatted_result = f"{result:,}"
    else:
        formatted_result = result

    print(f"{a:,} {symbol} {b:,} = {formatted_result}")
