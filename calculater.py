import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Helvetica", 30))
        self.entry.grid(row=0, column=0, columnspan=10)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        self.row = 1
        self.col = 0

        for button_text in self.buttons:
            self.create_button(button_text)

    def create_button(self, text):
        button = tk.Button(self.root, text=text, font=("Helvetica", 16), width=7, height=3,
                           command=lambda: self.on_button_click(text), bg="grey")
        button.grid(row=self.row, column=self.col, padx=5, pady=5)
        self.col += 1
        if self.col > 3:
            self.col = 0
            self.row += 1

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif text == "C":
            self.result_var.set("")
        else:
            self.result_var.set(self.result_var.get() + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
