ludzie = ['Radek', 'Janek', 'Asia', 'Michał']
wiek = [47, 67, 32, 34]
jezyk = ["python", "java"]

for osoba, wiek, jezyk in zip(ludzie, wiek, jezyk):
    print(osoba, jezyk, wiek)

lista = zip(ludzie, str(wiek), jezyk)
print(lista)
# łaczenie danych z kilku list

# for i in range(len(ludzie)):
#     print(ludzie[i])
#     # print(wiek[i])
#     print(jezyk[i])
