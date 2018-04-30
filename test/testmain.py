import tkinter as tk
import Testsecond
from tkinter.font import Font

# myFont = Font(family="Helvetia", size=10)

class Navbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.option_add("*Font", "arial 20 bold")
        self.parent = parent
        self.but1 = tk.Button(parent, text="1")
        self.but2 = tk.Button(parent, text="2")
        self.but1.pack(side="left")
        self.but2.pack(side="left")
        self.parent.statusbar.test.config(text="bla")
        self.entry = tk.Entry(parent, state="disabled")
        self.entry.pack()
        self.entry2 = tk.Entry(parent, bg="#F0F0F0")
        self.entry2.pack()


class Window1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.option_add("*Font", "arial 20 bold")
        self.parent = parent
        self.test = tk.Button(parent, text="blub")
        self.test.pack()

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.statusbar = Testsecond.Statusbar(self)
        self.navbar = Navbar(self)
        self.statusbar.pack()
        self.navbar.pack()



class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)


if __name__ == "__main__":
    root = MainApplication()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()