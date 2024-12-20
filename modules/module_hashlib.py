import hashlib


def hash_string(input_string, algorithm="sha256"):
    """
    Hashes a string using the specified algorithm.

    :param input_string: The string to hash.
    :param algorithm: The hashing algorithm to use (default is sha256).
    :return: The resulting hash in hexadecimal format.
    """
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(input_string.encode("utf-8"))
    return hash_obj.hexdigest()


def hash_file(file_path, algorithm="sha256"):
    """
    Hashes a file using the specified algorithm.

    :param file_path: The path to the file to hash.
    :param algorithm: The hashing algorithm to use (default is sha256).
    :return: The resulting hash in hexadecimal format.
    """
    hash_obj = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


if __name__ == "__main__":
    # Example usage
    input_string = "Hello, World!"
    print(f"SHA256 hash of '{input_string}': {hash_string(input_string)}")

    # Hashing a file (make sure to replace 'example.txt' with a valid file path)
    file_path = "./data/raw/speech_day_of_infamy.txt"
    try:
        print(f"SHA256 hash of file '{file_path}': {hash_file(file_path)}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
