def f():
    def fwew(a, b):
        return a * b

    return fwew


x = f()
print(x)
print(x(4, 6))