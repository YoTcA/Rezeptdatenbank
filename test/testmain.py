import tkinter as tk
import Testsecond


class Mainpage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for row in args:
            print(row)
        toolbar = tk.Frame(self)
        toolbar.pack()
        self.container = tk.Frame()
        self.container.pack()

app = Mainpage()
button = tk.Button(Mainpage.container, text="hello")

app.mainloop()