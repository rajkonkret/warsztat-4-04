slownik = {"name": "Radek"}


def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person


while True:
    print("Podaj imie i nazwisko")
    print("Wpisz q by zakonczyc")
    f_name = input("IMIE: ")
    if f_name == 'q':
        break
    l_name = input("NAZWISKO: ")
    if l_name == 'q':
        break
    age = input("wiek: ")
    if age == "q":
        break
    print(build_person(f_name, l_name, int(age)))
