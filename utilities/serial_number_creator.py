import random
import string

def generate_serial_number(prefix: str, length: int) -> str:
    """
    Generate a serial number with a given prefix and total length.
    
    Parameters:
    - prefix (str): The prefix for the serial number.
    - length (int): The total length of the serial number including the prefix.
    
    Returns:
    - str: The generated serial number.
    
    Raises:
    - ValueError: If the length is less than or equal to the length of the prefix.
    """
    if length <= len(prefix):
        raise ValueError("Length must be greater than the length of the prefix.")
    
    # Calculate the number of random characters needed
    num_random_chars = length - len(prefix)
    
    # Generate random alphanumeric characters
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num_random_chars))
    
    # Combine prefix and random characters to form the serial number
    serial_number = prefix + random_chars
    
    return serial_number

def generate_license_number(sections: int=4, section_length: int=8, separator: str='-') -> str:
    """
    Generate a license number consisting of uppercase letters and digits.
    
    Parameters:
    - sections (int): The number of sections in the license number.
    - section_length (int): The length of each section.
    - separator (str): The separator between sections.
    
    Returns:
    - str: The generated license number.
    """

    characters = string.ascii_uppercase + string.digits
    license_parts = []
    for _ in range(sections):
        part = ''.join(random.choices(characters, k=section_length))
        license_parts.append(part)

    return separator.join(license_parts)

if __name__ == "__main__":
    prefix = "SN-"
    total_length = 12
    serial_number = generate_serial_number(prefix, total_length)
    print(f"Generated Serial Number: {serial_number}")

    license_number = generate_license_number(sections=4, section_length=8, separator='-')
    print(f"Generated License Number: {license_number}")