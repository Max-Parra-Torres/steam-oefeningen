import json

# To write JSON to a file in python, we can use json.dump()

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('files/person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)
  