# class MyException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#         self.message = message


# raise MyException("Wystąpił bład!")

class MyException(ValueError):
    pass


try:
    x = int(input("Podaj liczbe całkowitą"))
    if x < 0:
        raise MyException("Liczba musi byc dodatnia")
except MyException as e:
    print("Wystapił moj własny wyjątek", e)
except ValueError as e:
    print("Wystapił bład ValueError", e)
