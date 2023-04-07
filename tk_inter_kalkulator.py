import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Kalkulator")
        self.geometry("300x300")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.result_entry = tk.Entry(self, textvariable=self.result_var, width=25)
        self.result_entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]
        for (text, row, column) in buttons:
            self.create_button(text, row, column)

    def create_button(self, text, row, column):
        button = tk.Button(self, text=text, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, pady=5, padx=5, sticky="NSEW")

    def on_button_click(self, text):
        if text.isdigit() or text == ".":
            self.result_var.set(self.result_var.get() + text)
        elif text == "=":
            try:
                expression = self.result_var.get()
                self.result_var.set(eval(expression))
            except Exception as e:
                self.result_var.set("Błąd")
        else:
            self.result_var.set(self.result_var.get() + text)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
