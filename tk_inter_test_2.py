import tkinter as tk


def show_text():
    text = entry.get()
    print(f"Wprowadzamy tesks: {text}")


app = tk.Tk()
app.title("Przykład 2")
entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Pokaż tekst", command=show_text)
button.pack()

app.mainloop()
