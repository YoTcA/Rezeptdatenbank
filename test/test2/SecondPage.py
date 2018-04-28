import tkinter as tk


class SecondPage(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # define GUI elements
        self.label = tk.Label(self, text="test2")
        button = tk.Button(self, text="1st Page", command=lambda: controller.show_frame(pages[0]))
        but_change1st = tk.Button(self, text="Change Label on Startpage", command=lambda: send_text("Hello"))

        # place GUI elements
        self.label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        but_change1st.grid(row=2, column=0)

        # send text to StartPage
        def send_text(text):
            controller.pass_on_text(text)

    # get information and change the displayed text
    def get_text(self, text):
        self.label.config(text=text)

