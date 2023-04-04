def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew


@dekor
def hej():
    print("Hej!")


def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


hej()
print(wykonaj(dodaj, 2, 3))
print(wykonaj(odejmij, 2, 3))
