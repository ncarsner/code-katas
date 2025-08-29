import csv
import json
import pandas as pd
import os


def convert_file(input_file_path, output_file_path):
    input_extension = os.path.splitext(input_file_path)[1][1:]
    output_extension = os.path.splitext(output_file_path)[1][1:]

    if input_extension == 'csv':
        if output_extension == 'xlsx':
            df = pd.read_csv(input_file_path)
            df.to_excel(output_file_path, index=False)
        elif output_extension == 'json':
            with open(input_file_path, 'r') as f:
                csv_reader = csv.DictReader(f)
                data_file = [row for row in csv_reader]
            with open(output_file_path, 'w') as f:
                json.dump(data_file, f, indent=4)
        else:
            return "Invalid output file extension."
    elif input_extension == 'xlsx':
        if output_extension == 'csv':
            df = pd.read_excel(input_file_path)
            df.to_csv(output_file_path, index=False)
        elif output_extension == 'json':
            df = pd.read_excel(input_file_path)
            df.to_json(output_file_path, orient='records')
        else:
            return "Invalid output file extension."
    elif input_extension == 'json':
        if output_extension == 'csv':
            with open(input_file_path, 'r') as f:
                data = json.load(f)
            with open(output_file_path, 'w', newline='') as f:
                csv_writer = csv.DictWriter(f, fieldnames=data[0].keys())
                csv_writer.writeheader()
                for row in data:
                    csv_writer.writerow(row)
        elif output_extension == 'xlsx':
            df = pd.read_json(input_file_path)
            df.to_excel(output_file_path, index=False)
        else:
            return "Invalid output file extension."
    else:
        return "Invalid input file extension."


if __name__ == '__main__':
    file_input = r'C:\Users\myUser\Documents\test_file.csv'
    file_output = r'C:\Users\myUser\Documents\test_file.json'

    convert_file(file_input, file_output)
