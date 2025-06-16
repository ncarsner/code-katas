import random

first_names = [
    "ALEX", "BARBARA", "CHARLES", "DAVID", "ELIZABETH",
    "JAMES", "JEFFREY", "JOHN", "PATRICIA", "ROBERT",
]
last_names = [
    "BROWN", "DAVIS", "GARCIA", "JOHNSON", "JONES",
    "LEE", "MARTINEZ", "MILLER", "SMITH", "WILLIAMS",
]
titles = [", M.D.", "DR. ", ""]
middle_initials = [chr(i) + "." for i in range(ord("A"), ord("Z") + 1)]
facilities = [
    "CLINIC", "HEALTH", "HEALTHCARE", "HEALTH SYSTEM",
    "HOSPITAL", "MEDICAL CENTER", "MEDICAL GROUP", "PHYSICIANS",
]
ownerships = [
    "WEST TENNESSEE", "CENTRAL TENNESSEE", "EAST TENNESSEE",
    "SOUTHERN TENNESSEE", "MIDDLE TENNESSEE", "NORTH TENNESSEE",
    "MUSIC CITY", "VOLUNTEER", "VOLUNTEER STATE", "TENNESSEE VALLEY",
]

def random_physician():
    title, first, last = (
        random.choice(titles),
        random.choice(first_names),
        random.choice(last_names),
    )
    middle = (
        f" {random.choice(middle_initials)}" if random.choice([True, False]) else ""
    )
    if title == "DR. ":
        return f"{title}{first}{middle} {last}"
    elif title == ", M.D.":
        return f"{first}{middle} {last}{title}"
    else:
        return f"{first}{middle} {last}"


def random_facility():
    return f"{random.choice(ownerships)} {random.choice(facilities)}"


if __name__ == "__main__":
    for _ in range(10):
        print(random_physician() if random.choice([True, False]) else random_facility())
