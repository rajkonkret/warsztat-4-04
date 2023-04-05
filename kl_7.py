import pickle
from kl_6 import Person

# pickle - biblioteka do zapisywania w formie obiekty a nie tekstu jak standardowe metody pythona
with open('data.pickle', 'rb') as stream:
    p = pickle.load(stream)

for person in p:
    # print(type(person))
    person.greet()

with open('data.txt', 'r') as stream:
    p2 = stream.read()

print(type(p2))
print(p2)
