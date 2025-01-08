from string import ascii_lowercase
from datetime import datetime

current_day = datetime.now().day
letters = list(ascii_lowercase)
offset = current_day % len(letters) - 1
offset_letters = letters[offset:] + letters[:offset]

print(current_day)
print(letters)
print(offset)
print(offset_letters)

for i in range(len(offset_letters) // 2):
    print(offset_letters[i], offset_letters[-(i + 1)])
