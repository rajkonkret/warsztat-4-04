generator_1 = (x for x in [1, 2, 3, 5])
print(generator_1)
print(type(generator_1))


def generator_2():
    i = 1
    while True:
        yield i * i
        i += 1


print(generator_2())
g = generator_2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# for num in generator_2():
#     if num > 100:
#         break
#     print(num)


# def read_csv_file(filname):
#     with open(filname, 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             yield row


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


# a, b = b, a
fib = fibo()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print("coś.....")
print("coś.....")
print("coś.....")
print(next(fib))


temp = next(fib)
print(next(fib) / temp)
fib_2 = fibo()  # wywołanie ponowne od zera
print(next(fib))
print(next(fib_2))

