import json

# To analyze and debug JSON data, we may need to print it in a more readable format.
# This can be done by passing additional parameters indent and sort_keys to json.dumps()
# and json.dump() method.

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))

# In the above program, we have used 4 spaces for indentation. And, the keys are sorted in ascending order.
# By the way, the default value of indent is None. And, the default value of sort_keys is False.
