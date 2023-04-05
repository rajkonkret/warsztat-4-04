from abc import ABC


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @staticmethod  # oznaczenie metody jako statyczna
    def format_string():
        return '%d'


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartosć nie może przekroczyc MAX")
        super(BoundedCounter, self).__init__(values)


c = Counter()
c.increment()
print(c)
c.format_string()
# Metoda statyczna - metoda ktora mozna wywołac na klasie a nie na obiekcie klasy
Counter.format_string()
print(Counter().format_string())
b = BoundedCounter()
# b2 = BoundedCounter(101) - rzuci nam wyjątek
# 11:30