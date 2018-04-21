import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import messagebox
import ToolBar
import ShowEditRecipe
import NewRecipe
import SearchRecipe

import sqlite3
import re
import database_files

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 8)
SMALL_FONT = ("Verdana", 6)



def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



class Recipedb(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Adjust Title and Icon
        tk.Tk.iconbitmap(self, default="auge_ava_50_Q5O_icon.ico")
        tk.Tk.wm_title(self, "Rezeptdatenbank V 0.1")

        # Initial window size
        #self.geometry('400x400')
        #self.wm_minsize(200,200)

        pages = (StartPage, NewRecipe.NewRecipe, SearchRecipe.SearchRecipe, ShowEditRecipe.ShowEditRecipe)

        toolbar = ToolBar.Toolbar(self, pages)
        toolbar.pack()

        #Initialize Window
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}


        # Load all pages
        for F in pages:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    # jump to next selection on Tab instead of indenting the text
    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    def show_frame(self, cont):
        # shows the desired frame
        frame = self.frames[cont]
        frame.tkraise()

'''class Toolbar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        toolbar = tk.Frame(parent)
        butt_new = ttk.Button(toolbar, text="Neues Rezept", command=lambda: parent.show_frame(NewRecipe))
        butt_new.pack(side=tk.LEFT, padx=2, pady=2)
        butt_search = ttk.Button(toolbar, text="Rezept suchen", command=lambda: parent.show_frame(SearchRecipe))
        butt_search.pack(side=tk.LEFT, padx=2, pady=2)
        butt_display = ttk.Button(toolbar, text="Rezept anzeigen", command=lambda: parent.show_frame(ShowEditRecipe))
        butt_display.pack(side=tk.LEFT, padx=2, pady=2)
        butt_edit = ttk.Button(toolbar, text="Rezept bearbeiten", command=lambda: parent.show_frame(ShowEditRecipe))
        butt_edit.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)'''



class StartPage(tk.Frame):
    # create the startpage
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome", font=LARGE_FONT)
        label.pack(pady=10, padx=10)



app = Recipedb()

app.mainloop()