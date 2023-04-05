from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @staticmethod  # oznaczenie metody jako statyczna
    def format_string():
        return '%d'

    @abstractmethod
    def drukuj(self):
        pass

    @classmethod
    def from_other(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartosć nie może przekroczyc MAX")
        super(BoundedCounter, self).__init__(values)

    def increment(self, by=1):
        super(BoundedCounter, self).increment()
        self.values = min(self.values, self.MAX)  # min() - wartosc minimalna

    def drukuj(self):
        print("Drukuje....", self.values)


# c = Counter()
# c.increment()
# print(c)
# c.format_string()
# Metoda statyczna - metoda ktora mozna wywołac na klasie a nie na obiekcie klasy
Counter.format_string()
b = BoundedCounter()
# b2 = BoundedCounter(101) - rzuci nam wyjątek
# 11:30
# klasa abstrakcyjna - nie mozna utworzyc obiektu takiej klasy
# klasy dziedziczace musza nadpisac metody abstrakcyjne
b.increment(10)
b.drukuj()
c = BoundedCounter.from_other(b)
b.drukuj()
c.drukuj()
