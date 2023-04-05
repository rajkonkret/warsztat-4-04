def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()


if __name__ == '__main__':
    print(get_formatted_name("radek", 'kowalski', 'nowak'))
