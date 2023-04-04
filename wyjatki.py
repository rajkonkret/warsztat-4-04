# def multi(a, b):
#     try:
#         return int(a) * int(b)
#     except TypeError:
#         return "Błędne dane"
#     except ValueError:
#         return 0
#
#
# def multi_2(a, b):
#     try:
#         return int(a) * int(b)
#     except (TypeError, ValueError):
#         return "błędne dane"
#
#
# def multi_3(a, b):
#     try:
#         return int(a) * int(b)
#     except Exception as e:
#         return f"błedne dane - bład {e.args}"
#
#
# print(multi("a", "b"))
# print(multi("3", "3"))
# print(multi((3,), "3"))
# print(multi_2("a", "b"))
# print(multi_2(3, 3))
# print(multi_3("a", "b"))
# print(multi_3(3, 3))
# print(multi_3((3,), 3))  # (3,) - tupla jednoelementowa
# # 13:30


valid_data = [{'name': 'Jan', 'age': '10'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_data = [{}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_data_2 = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except Exception as e:
            print(f"Niepoprawne dane: {user, e.args} ")
        else:   # wykona sie gdy nie ma błedu
            count += 1 if user_age < age else 0
        finally:        # wykonuje sie zawsze
            print(f"{i}-{user}")
    return f"Ilośc osób spełniająca kryteria: {count}"


print(check_age(valid_data, 15))
print(check_age(invalid_data, 15))
print(check_age(invalid_data_2, 15))
