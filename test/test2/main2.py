import tkinter as tk

class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        pages = (StartPage, SecondPage)
        for F in pages:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)


        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        return True

    def pass_on_text(self, text):
        self.frames[StartPage].get_text(text)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="test")
        button = tk.Button(self, text="2nd Page", command=lambda: controller.show_frame(SecondPage))
        self.label.grid(row=0, column=0)
        button.grid(row=1, column=0)
    def get_text(self, text):
        self.label.config(text=text)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        label = tk.Label(self, text="test2")
        button = tk.Button(self, text="1st Page", command=lambda: controller.show_frame(StartPage))
        but_change = tk.Button(self, text="Change Label on Startpage", command=lambda: send_text("Hello"))
        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        but_change.grid(row=2, column=0)

        def send_text(text):
            controller.pass_on_text(text)


app = TestApp()
app.mainloop()