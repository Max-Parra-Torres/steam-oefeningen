import json

# You can use json.load() to read a file containing JSON object
with open('files/person.json', 'r') as person:
    data = json.load(person)

print(data)
