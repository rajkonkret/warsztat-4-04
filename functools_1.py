from functools import partial
from functools import


def muliply(x, y):
    return x * y


double = partial(muliply, y=2)
triple = partial(muliply, y=3)

print(double(5))
print(triple(5))


# mapowanie wartosci funkcji do listy
def squared(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
s = list(map(squared, numbers))

print(s)
# 11:55