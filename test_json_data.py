import json


def test_uniform_json_keys():

    with open("json_data.json", "r") as file:
        json_data = json.load(file)

    key_counts = [
        len(address.keys())
        for student in json_data["students"]
        for address in student["addresses"]  # noqa: E501
    ]

    # Do all "students.addresses" contain the same number of elements?
    assert all(
        count == key_counts[0] for count in key_counts
    ), "Not all student addresses have the same number of keys"


def test_all_facts_have_addy_year_end():
    with open("json_data.json", "r") as file:
        json_data = json.load(file)

    no_addy_year_end_count = 0

    for student in json_data["students"]:
        if not all("addy_year_end" in address for address in student["addresses"]):
            no_addy_year_end_count += 1
        # add more field details (counter required above)

    # Do all expected addresses details exist in "students.addresses" ?
    #     Do any student addresses contain additional field? e.g. "address_2"
    #     Are any student addresses missing expected fields? e.g. "zip_code"
    assert no_addy_year_end_count == 0, f"{no_addy_year_end_count} students missing addy_year_end" # noqa: E501


def test_all_facts_have_addy_nickname():
    with open("json_data.json", "r") as file:
        json_data = json.load(file)

    no_addy_nickname_count = 0

    for student in json_data["students"]:
        if not all("addy_nickname" in address for address in student["addresses"]):
            no_addy_nickname_count += 1
        # add more field details (counter required above)

    # Do all expected addresses details exist in "students.addresses" ?
    #     Do any student addresses contain additional field? e.g. "address_2"
    #     Are any student addresses missing expected fields? e.g. "zip_code"
    assert no_addy_nickname_count == 0, f"{no_addy_nickname_count} students missing addy_nickname" # noqa: E501


# pytest is executed in cmd line
