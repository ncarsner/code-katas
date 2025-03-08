import csv
import argparse


def find_and_remove_duplicates(file_path, output_path):
    seen = set()
    duplicates = []

    with open(file_path, "r") as infile, open(output_path, "w", newline="") as outfile:
        csv_reader = csv.DictReader(infile)
        csv_writer = csv.DictWriter(outfile, fieldnames=csv_reader.fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            row_tuple = tuple(row.items())
            if row_tuple in seen:
                duplicates.append(row)
            else:
                seen.add(row_tuple)
                csv_writer.writerow(row)

    return duplicates


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and remove duplicates from a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_file", help="Path to the output CSV file.")
    args = parser.parse_args()

    duplicates = find_and_remove_duplicates(args.input_file, args.output_file)
    if duplicates:
        print(f"Found {len(duplicates)} duplicates.")
    else:
        print("No duplicates found.")
