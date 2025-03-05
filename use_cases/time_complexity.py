import collections
import time
from functools import wraps


def time_complexity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result

    return wrapper


@time_complexity
def calculate_living(person: tuple[int, int], living_per_year: collections.Counter) -> None:
    birth, death = person
    for year in range(birth, death):
        living_per_year[year] += 1


@time_complexity
def count_living_per_year(population: list[tuple[int, int]]) -> dict[int, int]:
    living_per_year = collections.Counter()
    list(map(lambda person: calculate_living(person, living_per_year), population))
    return living_per_year


if __name__ == "__main__":
    population = [(1900, 1950), (1910, 1955), (1920, 1960), (1930, 1970), (1940, 1980)]
    print(count_living_per_year(population))
