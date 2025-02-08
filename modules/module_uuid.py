import uuid
import random


def generate_uuid1():
    """Generate a UUID based on the host ID and current time.

    Returns:
        UUID: A UUID object generated using uuid1."""
    return uuid.uuid1()


def generate_uuid3(namespace, name):
    """Generate a UUID using an MD5 hash of a namespace UUID and a name.

    Args:
        namespace (UUID): The namespace UUID.
        name (str): The name to hash.

    Returns:
        UUID: A UUID object generated using uuid3."""
    return uuid.uuid3(namespace, name)


def generate_uuid4():
    """Generate a random UUID.

    Returns:
        UUID: A UUID object generated using uuid4."""
    return uuid.uuid4()


def generate_uuid5(namespace, name):
    """Generate a UUID using a SHA-1 hash of a namespace UUID and a name.

    Args:
        namespace (UUID): The namespace UUID.
        name (str): The name to hash.

    Returns:
        UUID: A UUID object generated using uuid5."""
    return uuid.uuid5(namespace, name)


if __name__ == "__main__":
    top_level_domain = ["com", "org", "net", "int", "edu", "gov", "mil", "io", "co",]
    domain_a = random.choice(top_level_domain)
    domain_b = random.choice(top_level_domain)

    print(f"{generate_uuid1()=}")
    print(f"{generate_uuid3(uuid.NAMESPACE_DNS, f'example.{domain_a}')=}")
    print(f"{generate_uuid4()=}")
    print(f"{generate_uuid5(uuid.NAMESPACE_DNS, f'example.{domain_b}')=}")
