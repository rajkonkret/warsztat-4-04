import json

json_string = '{"name":"Jan", "age": 30, "city": "Lodz"}'


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.city}"


def dict_to_person(person_dict):
    return Person(person_dict['name'], person_dict['age'], person_dict['city'])


person = json.loads(json_string, object_hook=dict_to_person)
print(person)
print(type(person))
