import tkinter as tk


class Statusbar(tk.Frame):
    def __init__(self):
        super().__init__()
        self.test = tk.Button(self, text="blub")
        self.test.pack()


class MainApplication(tk.Tk):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.statusbar = Statusbar(self)

root = MainApplication()
#scnd = Secondpage(root)
#button = tk.Button(Mainpage.container, text="hello")

root.mainloop()