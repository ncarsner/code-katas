import random


class ReverseRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.current = self.start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

    def __reversed__(self):
        self.current = self.stop - self.step
        while (self.step > 0 and self.current >= self.start) or (self.step < 0 and self.current <= self.start):
            yield self.current
            self.current -= self.step


MAX_RANGE = ri(3, 10)

# Collect numbers in a list and join with commas for forward iteration
forward_numbers = [str(num) for num in ReverseRange(MAX_RANGE)]
print(", ".join(forward_numbers))

# Collect numbers in a list and join with commas for backward iteration
backward_numbers = [str(num) for num in reversed(ReverseRange(MAX_RANGE))]
print(", ".join(backward_numbers))
