from decimal import Decimal, getcontext

from _decimal import ROUND_HALF_UP

a = 0.2
b = 0.7
print(a + b)
# decimal uzywane np.: do obliczen finansowych
getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP  # .5 zaokragla w gore

a = Decimal('0.2')
print(a)
b = Decimal('0.7')
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)

liczba = Decimal('2.5')
zaokr = liczba.quantize(Decimal('0.01'))
print(zaokr)

# $1,234.00
cena = "$1,234.00"


def clean_decimal(text: str):
    if text is None: return None
    return Decimal(
        text.replace("$", "").replace(",", "")
    )


print(clean_decimal(cena))


# print(clean_decimal(""))


def f_remove(str: str, chars: str) -> str:
    if chars:
        return f_remove(str.replace(chars[0], ""), chars[1:])
    return str


print(f_remove("$1,234.50", "$,"))
