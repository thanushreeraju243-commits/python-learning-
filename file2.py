import json 
text = '{"name": "John", "age": 30, "city": "New York"}'
with open("data.json", "w") as json_file:
    json.dump(json.loads(text), json_file)
    print("JSON data written to data.json")
    