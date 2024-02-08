from faker import Faker
import re


def split_street_address(street_address):
    # Regular expression to find secondary address indicators
    secondary_address_pattern = r"\b(suite|apt|unit|apartment|room|floor)\b"

    match = re.search(secondary_address_pattern, street_address, re.IGNORECASE)
    if match:
        # Split the address at the found secondary address indicator
        split_index = match.start()
        address = street_address[:split_index].strip()
        address_2 = street_address[split_index:].strip()
    else:
        # If no secondary address indicator is found, return the full address
        address = street_address
        address_2 = ""

    return address, address_2


# Testing the function
fake = Faker()
fake_street_address = fake.street_address()
address_1, address_2 = split_street_address(fake_street_address)
