# { 'name' : 'Radek"}
# 13:20
import json

json_string = '{"name":"Jan", "age": 30, "city": "Lodz"}'
data = json.loads(json_string)
print(data)
print(type(json_string))
print(type(data))

data_2 = {
    "name": "Jan",
    "age": 30,
    "city": "LODZ"
}

json_string = json.dumps(data_2)
print(json_string)

data = json.loads(json_string)
print(data['name'])
print(data['age'])
data['country'] = 'Polska'

del data['city']
print(data)

modifed_json = json.dumps(data)
print(modifed_json)
print(type(data))
print(type(modifed_json))