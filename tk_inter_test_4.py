import tkinter as tk


def on_value_change(value):
    print(f"Zmieniona wartosc suwaka {value}")


app = tk.Tk()
app.title("Przykład suwaka")

slider = tk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, command=on_value_change)
slider.pack(side='bottom')

app.mainloop()
