import json


def flatten_json(nested_json, parent_key="", sep="_"):
    flattened_dict = {}
    for key, value in nested_json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_json(value, new_key, sep=sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                flattened_dict.update(
                    flatten_json({f"{new_key}{sep}{i}": item}, "", sep=sep)
                )
        else:
            flattened_dict[new_key] = value
    return flattened_dict


if __name__ == "__main__":
    file_path = "./data/raw/nested_json.json"
    with open(file_path, "r") as file:
        nested_json = json.load(file)
    flattened_json = (
        {
            f"root_{i}": flatten_json(item) if isinstance(item, dict) else item
            for i, item in enumerate(nested_json)
        }
        if isinstance(nested_json, list)
        else flatten_json(nested_json)
    )
    print(flattened_json)
