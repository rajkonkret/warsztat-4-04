import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witaam, jestem {self.first_name} {self.last_name}, ID to {self.id}")


people = [
    Person("Jacek", "Kowalski", 1),
    Person("Mateusz", "Zegar", 2)
]

print(people)

with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)

with open('data.txt', 'w') as stream:
    stream.write(str(people))