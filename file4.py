import json
import csv 
text = '{"name1": "John", "age": 30, "city": "New York", "name2": "Jane", "age": 25, "city": "Los Angeles", "name3": "Mike", "age": 35, "city": "Chicago"}'
file_path = "data.json"

with open(file_path, "w") as json_file:
    json.dump(json.loads(text), json_file)
    print(f"JSON data written to {file_path}") 
with open(file_path, "r") as json_file:
    data = json.load(json_file)
    print(f"JSON data read from {file_path}: {data}")
    