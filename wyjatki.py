def multi(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        return "Błędne dane"
    except ValueError:
        return 0


def multi_2(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return "błędne dane"


def multi_3(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return f"błedne dane - bład {e.args}"


print(multi("a", "b"))
print(multi("3", "3"))
print(multi((3,), "3"))
print(multi_2("a", "b"))
print(multi_2(3, 3))
print(multi_3("a", "b"))
print(multi_3(3, 3))
print(multi_3((3,), 3))  # (3,) - tupla jednoelementowa
# 13:30