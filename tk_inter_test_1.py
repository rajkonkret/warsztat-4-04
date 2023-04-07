import tkinter as tk


def on_click():
    print("Przycisk został nacisniety")


app = tk.Tk()  # utworz okienko
app.title("Przykład 1")  # nadanie tytułu

button = tk.Button(app, text="Kliknij mnie!", command=on_click)  # stworzenie przycisk

button.pack()  # dodanie przycisku do okna

app.mainloop()
