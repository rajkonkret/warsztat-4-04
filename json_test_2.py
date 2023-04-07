import json

person_dict = {'name': 'Radek', 'age': 39, 'czy_pali': None}

with open('dane_json.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=False)

with open('dane_json.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))
print(data['name'])
