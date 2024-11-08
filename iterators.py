iterable_list = [i for i in range(11) if i % 2 == 0]
iterable_tuple = ("apple", "banana", "cherry", "daikon")
iterable_dict = dict(a="alpha", b="bravo", c="charlie", d="delta", e="echo")


def iterable_oceans():
    yield "Arctic"
    yield "Atlantic"
    yield "Indian"
    yield "Pacific"
    yield "Antarctic"


iterable_squares = (x * 2 for x in range(10))

next(iterable_list)
