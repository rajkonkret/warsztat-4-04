import json

with open('dane_2.json', 'r') as f:
    data = json.load(f)

print(data)
print(data['members'])
print(data['members'][0])
print(data['members'][0]['name'])
print(data['members'][0]['age'])
print(data['members'][0]['powers'])
print(data['members'][0]['powers'][0])


for i in data['members']:
    print(i)