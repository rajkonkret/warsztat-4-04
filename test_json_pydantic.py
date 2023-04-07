from pydantic import BaseModel

json_string = '{"name":"Jan", "age": 30, "city": "Lodz"}'


class Person(BaseModel):
    name: str
    age: int
    city: str


person = Person.parse_raw(json_string)
print(person)
