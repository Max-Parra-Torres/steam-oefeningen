import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
# To write JSON to a file in python, we can use the json.dump() method as shown below
person_json = json.dumps(person_dict)

print(person_json)
