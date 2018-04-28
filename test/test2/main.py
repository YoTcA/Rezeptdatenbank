import tkinter as tk
import SecondPage


class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        # Initialize Window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        pages = (StartPage, SecondPage.SecondPage)
        # Load all pages
        for F in pages:
            frame = F(container, self, pages)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)


        self.show_frame(StartPage)

    # shows the desired frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        return True

    # passes text to the window StartPage
    def pass_on_text(self, text):
        self.frames[StartPage].get_text(text)

    # passes text to the window SecondPage
    def pass_on_text2(self, text):
        self.frames[SecondPage.SecondPage].get_text(text)


class StartPage(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)

        # define GUI elements
        self.label = tk.Label(self, text="test")
        button = tk.Button(self, text="2nd Page", command=lambda: controller.show_frame(pages[1]))
        but_change2nd = tk.Button(self, text="Change Label on SecondPage", command=lambda: send_text("Hello, too!"))

        # place GUI elements
        self.label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        but_change2nd.grid(row=2, column=0)

        # send text to SecondPage
        def send_text(text):
            controller.pass_on_text2(text)

    # get information and change the displayed text
    def get_text(self, text):
        self.label.config(text=text)


app = TestApp()
app.mainloop()