# UTF-8: variable-width encoding that can represent every character in the Unicode character set.
# Efficient for ASCII characters. Can use more bytes for characters outside the ASCII range.

texts = ["Good afternoon!", "Hello, 世界", "Grüß Gott", "¡Hola, señor!", "こんにちは世界", "Привет, мир"]

for text in texts:
    print(f"Original Text: {text}")
    utf8_encoded = text.encode("utf-8")
    print(f"UTF-8 Encoded: {utf8_encoded}")
    print(f"UTF-8 Decoded: {utf8_encoded.decode('utf-8')}\n")

# UTF-16 variable-width encoding that uses 2 or 4 bytes for each character.
# More efficient for characters outside the ASCII range but uses more space for ASCII characters.

for text in texts:
    print(f"Original Text: {text}")
    utf16_encoded = text.encode("utf-16")
    print(f"UTF-16 Encoded: {utf16_encoded}")
    print(f"UTF-16 Decoded: {utf16_encoded.decode('utf-16')}\n")


# UTF-32: fixed-width encoding that uses 4 bytes for each character.
# Simple and fast for random access but uses more memory.

for text in texts:
    print(f"Original Text: {text}")
    utf32_encoded = text.encode("utf-32")
    print(f"UTF-32 Encoded: {utf32_encoded}")
    print(f"UTF-32 Decoded: {utf32_encoded.decode('utf-32')}\n")


# ASCII: limited to 128 characters. Cannot represent characters outside the ASCII range.
# Efficient for plain English text. Not suitable for internationalization.

for text in texts:
    try:
        ascii_encoded = text.encode("ascii")
        print(f"ASCII Encoded: {ascii_encoded}")
        print(f"ASCII Decoded: {ascii_encoded.decode('ascii')}\n")
    except UnicodeEncodeError as e:
        print(f"ASCII Encoding Error: {e}\n")

# Tradeoffs Summary:
# - UTF-8: Efficient for ASCII, variable-width, widely used.
# - UTF-16: Efficient for non-ASCII, variable-width, more complex.
# - UTF-32: Fixed-width, simple, uses more memory.
# - ASCII: Limited to 128 characters, efficient for plain English, not suitable for international text.
