import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Sklep:
    def __init__(self, master):
        self.master = master
        self.master.title("Gra Sklep")

        self.produkty = {
            "Chleb": 3,
            "Mleko": 2,
            "Jajka": 5
        }

        self.zakupy = {}

        ttk.Label(self.master, text="Produkty w sklepie:").grid(column=0, row=0, padx=5, pady=5)

        for index, produkt in enumerate(self.produkty):
            ttk.Label(self.master, text=f"{produkt}: {self.produkty[produkt]} zł").grid(column=0, row=index + 1, padx=5,
                                                                                        pady=5)
            self.zakupy[produkt] = tk.IntVar()
            ttk.Entry(self.master, textvariable=self.zakupy[produkt], width=5).grid(column=1, row=index + 1, padx=5,
                                                                                    pady=5)

        ttk.Button(self.master, text="Złóż zamówienie", command=self.zloz_zamowienie).grid(column=0, row=4,
                                                                                           padx=5, pady=5)

    def zloz_zamowienie(self):
        suma = 0
        for product in self.produkty:
            ilosc = self.zakupy[product].get()
            cena = self.produkty[product] * ilosc
            suma += cena
        tk.messagebox.showinfo("Podsumowanie zamówienia", f"Koszt : {suma} zł")


# 13:10

okno = tk.Tk()
sklep = Sklep(okno)
okno.mainloop()
