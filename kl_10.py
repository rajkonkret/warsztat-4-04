class Car:
    """
    klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole prywatne

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def __zmien_bieg(self):     # metoda prywatna. uzywan z wnetrza klasy
        print("zmian biegu")

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print("Predkosc:", self.__predkosc)


c_1 = Car('Opel', 2018)
c_1.gaz()
c_1.gaz()
c_1.gaz()
c_1.gaz()
c_1.gaz()
c_1.gaz()
c_1.licznik()
c_1.hamuj()
c_1.hamuj()
c_1.hamuj()
c_1.hamuj()
c_1.hamuj()
c_1.hamuj()
c_1.licznik()