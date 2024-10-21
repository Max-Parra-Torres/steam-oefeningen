import json

#---------------------------------------------------------------------------

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)
# You can turn a JSON string into a python dict with json.loads()
# We do this so we can actually read the JSON file in python

print( person_dict)

print(person_dict['languages'])
