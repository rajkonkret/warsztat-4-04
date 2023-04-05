from name_function import get_formatted_name

print("wpisz 'q' aby zakończyć")
while True:
    first = input("Podaj imie")
    if first == 'q':
        break
    second = input("Podaj drugie imie")
    if second == 'q':
        break
    last = input("Podaj nazwisko")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last, second)
    print(f"Sformatowane {formatted_name}")