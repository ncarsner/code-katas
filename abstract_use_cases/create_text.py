import random
import string

def random_line(length=80):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length)) + '\n'

with open('./data/raw/large_file.txt', 'w', encoding='utf-8') as f:
    for _ in range(1_000_000):  # 1 million lines
        f.write(random_line())