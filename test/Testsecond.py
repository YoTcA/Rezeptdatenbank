import tkinter as tk
class Statusbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.option_add("*Font", "arial 20 bold")
        self.parent = parent
        self.test = tk.Button(parent, text="blub")
        self.test.pack()