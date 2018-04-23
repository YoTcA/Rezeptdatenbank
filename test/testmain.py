import tkinter as tk
import Testsecond



class Navbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.but1 = tk.Button(parent, text="1")
        self.but2 = tk.Button(parent, text="2")
        self.but1.pack(side="left")
        self.but2.pack(side="left")
        self.parent.statusbar.test.config(text="bla")

class Window1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
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