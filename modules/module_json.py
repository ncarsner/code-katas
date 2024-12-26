import json

# Convert a Python dictionary to a JSON string
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print("JSON string:", json_string)

# Convert a JSON string to a Python dictionary
json_data = '{"name": "Jane", "age": 25, "city": "Los Angeles"}'
python_dict = json.loads(json_data)
print("Python dictionary:", python_dict)

# Write JSON data to a file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Read JSON data from a file
with open("data.json", "r") as json_file:
    file_data = json.load(json_file)
    print("Data read from file:", file_data)
