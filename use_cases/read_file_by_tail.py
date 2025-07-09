from pathlib import Path
from collections import deque
import random
from functions import timer

# Setup (result is a 100 million line file ~270 MB)
path = Path("./data/raw/bigfile.txt")
if not path.exists():
    with path.open("w") as f:
        for i in range(100_000_000):
            f.write(f"Line {i}\n")


# Approach 1: read entire file
@timer
def tail_read_all(p: Path, n: int):
    return p.read_text().splitlines()[-n:]


# Approach 2: stream with deque
@timer
def tail_stream(p: Path, n: int):
    with p.open() as f:
        return list(deque(f, maxlen=n))


# Approach 3: reverse reading
@timer
def tail_reverse(path: Path, n: int) -> list[str]:
    with path.open("rb") as f:
        f.seek(0, 2)
        end = f.tell()
        lines = []
        line = bytearray()
        pos = end - 1

        while pos >= 0 and len(lines) < n:
            f.seek(pos)
            byte = f.read(1)
            if byte == b"\n":
                if line:
                    lines.append(line[::-1].decode())
                    line.clear()
            else:
                line.append(byte[0])
            pos -= 1

        if line:
            lines.append(line[::-1].decode())

        return lines[::-1]


# Get total number of lines in the file
with path.open() as f:
    total_lines = sum(1 for _ in f)

# Choose a random percentage (e.g., between 1/2 and 1%)
last_n = random.choice([10, 100, 1_000, 2_000, 5_000, 10_000, 50_000, 100_000])
# last_n = 50_000  # performance lags around 50,000 last lines (0.5%)
percent = last_n / total_lines

print(f"\nGetting last {last_n:,} lines ({percent:.1%}) of {path}:")
tail_read_all(path, last_n)
tail_stream(path, last_n)
tail_reverse(path, last_n)

"""
Bob Belderbos benchmarks:
Read all: 4.671550874998502
Streamed: 2.7067494580041966
Reversed: 0.0006466670020017773
"""
