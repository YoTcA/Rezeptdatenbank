import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import messagebox
import ToolBar
import ShowEditRecipe
import NewRecipe

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

def open_recipe(recipe_name):
    if recipe_name:
        print("Rezeptname: " + recipe_name)
        duration = database_files.get_duration(recipe_name)
        preparation = database_files.get_preparation(recipe_name)
        ingredients = database_files.get_ingredients(recipe_name)
        '''if recipe_name:
        ShowEditRecipe.ent_recipe_name(state="normal")
        ShowEditRecipe.ent_recipe_name(tk.END, recipe_name)
        ShowEditRecipe.ent_recipe_name(state="readonly")'''
        print("Dauer: " + str(duration))
        print("Preparation: " + str(preparation))
        print("Zutaten: " + str(ingredients))
        ShowEditRecipe.ShowEditRecipe.get_data(recipe_name, duration, ingredients, preparation)
    # print(map(int, lbx_recipelist.curselection()))

class Recipedb(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Adjust Title and Icon
        tk.Tk.iconbitmap(self, default="auge_ava_50_Q5O_icon.ico")
        tk.Tk.wm_title(self, "Rezeptdatenbank V 0.1")

        # Initial window size
        #self.geometry('400x400')
        #self.wm_minsize(200,200)

        pages = (StartPage, NewRecipe.NewRecipe, SearchRecipe, ShowEditRecipe.ShowEditRecipe)

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




class SearchRecipe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def search_recipes(recipe_name, ingredients):
            results = []
            # execute if a recipe_name is given
            print(recipe_name)
            if recipe_name:
                for row in database_files.search_recipe_name((recipe_name)):
                    results.append(row)

            # divide the ingredients into single items
            ingredient_result = []
            if len(ingredients) > 0:
                rows = ingredients.splitlines()
                for row in rows:
                    ingredient_result.append(re.split('\W+\s', row))
            ingredient_result = [item for sublist in ingredient_result for item in sublist]
            print(ingredient_result)

            #execute when ingredient_result is not empty
            '''if ingredient_result:
                results.append(database_files.search_ingredients(ingredient_result))'''


            if ingredient_result:
                for row in database_files.search_ingredients(ingredient_result): #database_files.cursor.execute('SELECT recipename FROM ingredients WHERE ingredient=? COLLATE NOCASE', (ingredients,)):
                    results.append(row)
            # empty the listbox before adding new items
            lbx_recipelist.delete(0, tk.END)

            # eliminate double entries in results and add the unique values to the listbox
            for result in list(set(results)):
                lbx_recipelist.insert(0, result)
            return True



        # GUI-Elemente erstellen
        lbl_recipe_name = tk.Label(self, text="Rezeptname:")
        lbl_ingredients = tk.Label(self, text="Zutaten:\n (Bitte Einzahl\nverwenden)")
        lbl_result_list = tk.Label(self, text="Ergebnisse:")
        ent_recipe_name = tk.Entry(self)
        txt_ingredients = tk.Text(self, width=40, height=4)
        txt_ingredients.bind("<Tab>", controller.focus_next_window)
        lbx_recipelist = tk.Listbox(self, selectmode=tk.SINGLE)
        but_search = ttk.Button(self, text="Suchen",
                                command=lambda: search_recipes(ent_recipe_name.get(), txt_ingredients.get("1.0", "end-1c")))
        but_open = ttk.Button(self, text="Anzeigen",
                              command=lambda: open_recipe(lbx_recipelist.get(tk.ACTIVE)[0]))
        # GUI-Elemente positionieren
        lbl_recipe_name.grid(row=0, column=0, sticky=tk.E)
        ent_recipe_name.grid(row=0, column=1, sticky=tk.NSEW)
        but_search.grid(row=0, column=2)
        lbl_ingredients.grid(row=2, column=0, sticky=tk.E)
        txt_ingredients.grid(row=2, column=1, sticky=tk.W)
        lbl_result_list.grid(row=3, column=0, sticky=tk.E)
        lbx_recipelist.grid(row=3, column=1, sticky=tk.NSEW)
        but_open.grid(row=4, column=0)


app = Recipedb()

app.mainloop()