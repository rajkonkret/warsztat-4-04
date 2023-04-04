from pakiet import drukarka

# ctrl alt l - formatuje nam kod

design = ['telefon', 'robot', 'szescian']
models = []
drukarka.print_models(design, models)
drukarka.show_completed(models)
print(models.pop())  # pobiera element z listy
copy_2 = models.copy()  # tworzy kopie listy
models.append("1")  # dodanie elementu do listy
models.extend(design)  # rozszerza liste o elementy z innej listy
print(models)
models.insert(1, "radek")  # wstawienie elementu w danym indeksie
print(models)
models.remove('1')  # usuwa pierwsze wystapienie elementu z listy
print(models)
print(models.index("robot"))
print(models.count("radek"))  # zlicza ilosc wystapien elementu w liscie
models.sort()  # sortuje liste
models.reverse()  # odwraca kolejnosc listy
models.clear()  # usuwa wszystkie elementy z listy
print(models)


def some_fun(a: float, b: float, t: float) -> float:
    return a + b * t


print(some_fun(2, 3, 4))
