from typing import Optional


class Sample:

    def __init__(
            self,
            a: int,
            b: int,
            c: int,
            d: int,
            e: Optional[str] = None  # podstawia wartosć, ktora przyszła lub opcjonalnie None
    ) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __repr__(self):  # nadpisanie  metody __repr__ - wypisanie klasy w sposoób ładny
        if self.d is None:
            self.d = "nieznany"
        if self.e is None:
            self.e = "nieznany"
        return (
            f"a = {self.a},"
            f" b = {self.b},"
            f" c = {self.c},"
            f" d = {self.d},"
            f" e = {self.e}"
        )
        # return(
        #     f"""
        #      a = {self.a}
        #      b = {self.b}
        #      c = {self.c}
        #      d = {self.d}
        #      e = {self.e}
        #     """
        # )


wyn = Sample(1, 2, 3, 4)
print(wyn)
print(repr(wyn))

wyn2 = Sample(5, 6, 7, None)
print(wyn2)
