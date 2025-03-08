from collections import defaultdict
import csv


def aggregate_data(file_path, group_by_column, metrics):
    aggregated_data = defaultdict(lambda: defaultdict(list))
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            group_key = row[group_by_column]
            for key, value in row.items():
                if key != group_by_column:
                    aggregated_data[group_key][key].append(float(value))

    result = {}
    for group_key, values in aggregated_data.items():
        result[group_key] = {}
        for key, value_list in values.items():
            if "sum" in metrics:
                result[group_key][f"{key}_sum"] = sum(value_list)
            if "average" in metrics:
                result[group_key][f"{key}_average"] = sum(value_list) / len(value_list)
            if "max" in metrics:
                result[group_key][f"{key}_max"] = max(value_list)
            if "min" in metrics:
                result[group_key][f"{key}_min"] = min(value_list)
    return result


if __name__ == "__main__":
    file_path = "data/raw/data.csv"
    group_by_column = "category"
    metrics = ["sum", "average", "max", "min"]

    aggregated_result = aggregate_data(file_path, group_by_column, metrics)
    for group, data in aggregated_result.items():
        print(f"Group: {group}")
        for metric, value in data.items():
            print(f"  {metric}: {value}")
