title_str = " This Is A Title "
"""
Prefix and Suffix Validation Methods:
- startswith(prefix): Checks if the string starts with the specified prefix.
- endswith(suffix): Checks if the string ends with the specified suffix.

Search and Replace Methods:
- find(sub): Finds the first occurrence of the substring.
- replace(old, new): Replaces occurrences of a substring with another substring.
- count(sub): Counts the occurrences of a substring.
- index(sub): Finds the first occurrence of the substring and raises an error if not found.
- rfind(sub): Finds the last occurrence of the substring.
- rindex(sub): Finds the last occurrence of the substring and raises an error if not found.
"""

### Prefix and suffix validation
print(title_str.startswith("This"))  # True
print(title_str.endswith("Title"))  # True

### Search and replace
print(title_str.find("Title"))  # 10
print(title_str.replace("Title", "Heading"))  # This Is A Heading
print(title_str.count("i"))  # 2
print(title_str.index("i"))  # 2
print(title_str.rfind("i"))  # 5
print(title_str.rindex("i"))  # 5
