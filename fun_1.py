def example(a, b, **kwargs):
    return a * b - kwargs


print(type(example))
print(example.__code__.co_varnames)  # krotka z argumentami funkcji
print(example.__code__.co_argcount)  # liczba argumentow

# labda - funkcja jednolinijkowa

liczymy = lambda x, y: x * y - 1
print(liczymy(200, 99))

r_0 = {'miasto': "Kielce"}  # para klucz:wartosc
r_1 = {'miasto': "Kielce", "ZIP": "25-900"}

d_zip = lambda row: row.setdefault('ZIP', '00-000')  # dodanie defaultowej wartosci gdy nie ma takiego kluczA
print(d_zip(r_0))
print(r_0)
print(d_zip(r_1))
print(r_1)


#  __missing__
# a + b
def dodaj(a, b):
    return a + b


dodaj_2 = lambda a, b: a + b
print(dodaj_2(3, 4))

lata = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
        (2004, 31.33), (2008, 32.84), (2009, 33.02), (2010, 32.92)]

print(max(lata))
print(max(lata, key=lambda c: c[1]))
print(max(map(lambda c: (c[1], c), lata))[1])
# (32.92, (2010, 32.92))
# [1] - (2010, 32.92)
#  [0] - 32.92

lista = [1, 2, 3, 5, 8, 20, 55]
print(f"Uzycie map() {list(map(lambda x: x * 2, lista))}")
# map(lambda x: x * 2, lista) - pobiera elementy z listy i poprzez lambde przelicza
# list(map(lambda x: x * 2, lista)) - wrzuca do listy
# print(f"Uzycie map() {list(map(lambda x: x * 2, lista))}") - formatuje wynik f{}
# 11:30