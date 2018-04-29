import tkinter as tk
import TopBar

import ShowEditRecipe
import NewRecipe
import SearchRecipe


LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 8)
SMALL_FONT = ("Verdana", 6)


class Recipedb(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Adjust Title and Icon
        tk.Tk.iconbitmap(self, default="auge_ava_50_Q5O_icon.ico")
        tk.Tk.wm_title(self, "Rezeptdatenbank V 0.1")

        # Initial window size
        # self.geometry('400x400')
        # self.wm_minsize(200,200)

        self.pages = {"StartPage": StartPage,
                 "NewRecipe": NewRecipe.NewRecipe,
                 "SearchRecipe": SearchRecipe.SearchRecipe,
                 "ShowEditRecipe": ShowEditRecipe.ShowEditRecipe}

        topbar = TopBar.Toolbar(self, self.pages)
        topbar.pack(side="top", fill=tk.X)

        # Initialize Window
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.button_bar = tk.Frame(self)
        self.button_bar.pack()
        testbutton = tk.Button(self.button_bar, text="Test")
        testbutton.pack()

        self.frames = {}

        # Load all pages
        for key, F in self.pages.items():
            frame = F(container, self, self.pages)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    # jump to next selection on Tab instead of indenting the text
    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    # shows the desired frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def double_space(self, text):
        while "  " in text:
           text = text.replace("  ", " ")
        return text

    def show_recipe(self):
        frame = self.frames[self.pages["ShowEditRecipe"]]
        frame.tkraise()
        fields = [frame.ent_recipe_name, frame.ent_duration, frame.txt_ingredients, frame.txt_preparation]
        for field in fields:
            if field.winfo_class() == "Entry":
                field.config(state="readonly")
            elif field.winfo_class() == "Text":
                field.config(state="disabled")
        return True

    def edit_recipe(self):
        frame = self.frames[self.pages["ShowEditRecipe"]]
        frame.tkraise()
        fields = [frame.ent_recipe_name, frame.ent_duration, frame.txt_ingredients, frame.txt_preparation]
        for field in fields:
            field.config(state="normal")
        return True


class StartPage(tk.Frame):
    # create the startpage
    def __init__(self, parent, controller, pages):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        label = tk.Label(self, text="Welcome", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


if __name__ == "__main__":
    app = Recipedb()
    app.mainloop()
