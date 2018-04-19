import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import messagebox

import sqlite3
import re
import database_files

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 8)
SMALL_FONT = ("Verdana", 6)


# check if there is already a recipe with the inputed recipe name in the database
def check_recipe_name():
    recipe_name = NewRecipe.sv.get()
    for recipe in database_files.cursor.execute('SELECT recipename FROM recipe'):
        if recipe_name.strip() in recipe:
            tmp_value = messagebox.askyesno("Rezeptname bereits vergeben.",
                                            "Rezeptname bereits vergeben. Rezept zum Bearbeiten öffnen?")
            if tmp_value:
                print("rezept öffnen")
            else:
                print("nicht öffnen")
    return True

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

        # Toolbar
        toolbar = tk.Frame(self)
        butt_new = ttk.Button(toolbar, text="Neues Rezept", command=lambda: self.show_frame(NewRecipe))
        butt_new.pack(side=tk.LEFT, padx=2, pady=2)
        butt_search = ttk.Button(toolbar, text="Rezept suchen", command=lambda: self.show_frame(SearchRecipe))
        butt_search.pack(side=tk.LEFT, padx=2, pady=2)
        butt_edit = ttk.Button(toolbar, text="Rezept bearbeiten", command=lambda: self.show_frame(ShowEditRecipe))
        butt_edit.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Initial window size
        #self.geometry('400x400')
        #self.wm_minsize(200,200)

        #Initialize Window
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # Load all pages
        for F in (StartPage, NewRecipe, SearchRecipe, ShowEditRecipe):
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


class StartPage(tk.Frame):
    # create the startpage
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


class NewRecipe(tk.Frame):
    # create the page to input a new recipe
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        NewRecipe.sv = tk.StringVar()

        self.preparation_results = []
        self.ingredient_results = []

        def clear_entries():
            ent_recipe_name.delete(0, tk.END)
            ent_duration.delete(0, tk.END)
            txt_ingredients.delete('1.0', tk.END)
            txt_preparation.delete('1.0', tk.END)

        '''GUI Elemente definieren'''
        '''Label'''
        lab_recipe_name = tk.Label(self, text="Rezeptname: ")
        lab_duration = tk.Label(self, text="Dauer: ")
        lab_minutes = tk.Label(self, text="min")
        lab_preparation = tk.Label(self, text="Zubereitung: ")
        lab_ingredients = tk.Label(self, text="Zutaten: ")
        '''Entryboxes'''
        ent_recipe_name = tk.Entry(self, width=40, textvariable=NewRecipe.sv, validate="focusout",
                                   validatecommand=check_recipe_name)
        ent_duration = tk.Entry(self, width=10)
        txt_ingredients = tk.Text(self, width=40, height=10)
        txt_ingredients.bind("<Tab>", controller.focus_next_window)
        txt_preparation = tk.Text(self, width=40, height=10)
        txt_preparation.bind("<Tab>", controller.focus_next_window)
        '''Buttons'''
        but_check = tk.Button(self, text="Prüfen",
                               command= lambda: self.getingredients(ent_recipe_name.get(),
                                                                    ent_duration.get(),
                                                                    txt_preparation.get("1.0", "end-1c"),
                                                                    txt_ingredients.get("1.0", "end-1c")))
        but_save = tk.Button(self, text="Speichern",
                                  command= lambda: database_files.write_data(self.preparation_results,
                                                                             self.ingredient_results))
        but_read = tk.Button(self, text="Text", command=database_files.readall)
        but_clear = tk.Button(self, text="Neues Rezept", command=clear_entries)

        '''GUI Elemente positionieren'''
        lab_recipe_name.grid(row=0, column=0, sticky=tk.NE)
        ent_recipe_name.grid(row=0, column=1,columnspan=2, padx=2, pady=2, sticky=tk.W)
        lab_duration.grid(row=1, column=0, sticky=tk.NE)
        ent_duration.grid(row=1, column=1, padx=2, pady=2, sticky=tk.NSEW)
        lab_minutes.grid(row=1, column=2, sticky=tk.NW)
        lab_ingredients.grid(row=2, column=0, sticky=tk.NE)
        txt_ingredients.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        lab_preparation.grid(row=3, column=0, sticky=tk.NE)
        txt_preparation.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        but_check.grid(row=4, column=0)
        but_save.grid(row=4, column=1)
        but_read.grid(row=4, column=2)
        but_clear.grid(row=4, column=3)
        '''
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(SearchRecipe))
        button2.pack()'''



    def doublespace(self, text):
        while "  " in text:
           text = text.replace("  ", " ")
        return text

    def getingredients(self, recipename, duration, preparation, ingredienttext):
        #text = textfeld.get("1.0", "end-1c")
        if not recipename == "":
            unitlist = ["l", "ml", "g", "kg", "gr", "kl", "cup", "st", "pc", "liter", "gramm", "kilo", "stück", "große",
                        "kleine", "großes", "kleines"]
            quantities = []
            units = []
            ingredients = []
            ingredientlist = []
            recipelist = []
            rows = ingredienttext.splitlines()

            for row in rows:
                if row == "":
                    continue
                a = 0  #parameter to count the parts
                quantity = ""
                unit = ""
                ingredient = ""
                row = self.doublespace(row)
                parts = row.split()
                # when there are more than 1 part, the first is treated as a quantity
                if len(parts) > 1:
                    a = 1
                    quantity = parts[0]
                    # savety to replace decimal , with decimal .
                    quantity = quantity.replace(",", ".")
                    # check if the quantity was given as float
                    if not isfloat(quantity):
                        messagebox.showinfo("Menge falsch", "Menge als Zahl angeben")

                if len(parts) > 2:
                    a = 2
                    unit = parts[1]

                # assign the last so far untreated part as ingredient
                ingredient = parts[a]
                a += 1

                # append remaining parts of the ingredient to the string
                while a < len(parts):
                    ingredient = ingredient + " " + parts[a].strip()
                    a += 1

                # if the unit is not unit treat it as an part of the ingredient
                if len(parts) > 2 and unit.lower() not in unitlist:
                    ingredient = unit + " " + ingredient
                    unit = ""

                quantities.append(quantity)
                units.append(unit)
                ingredients.append(ingredient)
            for i in quantities:
                print("Menge:" +  i)
            for i in units:
                print("Einheiten:" + i)
            for i in ingredients:
                print("Zutaten:" + i)
            ingredientlist.append(recipename)
            ingredientlist.append(quantities)
            ingredientlist.append(units)
            ingredientlist.append(ingredients)
            print(ingredientlist)
            recipelist.append(recipename)
            recipelist.append(duration)
            recipelist.append(preparation)
            print(recipelist)
            self.ingredient_results = ingredientlist
            self.preparation_results = recipelist
        else:
            messagebox.showerror("Fehlender Rezeptname", "Bitte einen Rezeptnamen eingeben.")


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

        def open_recipe():
            print(map(int, lbx_recipelist.curselection()))

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
        but_open = ttk.Button(self, text="Anzeigen", command=open_recipe)
        # GUI-Elemente positionieren
        lbl_recipe_name.grid(row=0, column=0, sticky=tk.E)
        ent_recipe_name.grid(row=0, column=1, sticky=tk.NSEW)
        but_search.grid(row=0, column=2)
        lbl_ingredients.grid(row=2, column=0, sticky=tk.E)
        txt_ingredients.grid(row=2, column=1, sticky=tk.W)
        lbl_result_list.grid(row=3, column=0, sticky=tk.E)
        lbx_recipelist.grid(row=3, column=1, sticky=tk.NSEW)
        but_open.grid(row=4, column=0)


class ShowEditRecipe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        '''GUI Elemente definieren'''
        '''Label'''
        lab_recipe_name = tk.Label(self, text="Rezeptname: ")
        lab_duration = tk.Label(self, text="Dauer: ")
        lab_minutes = tk.Label(self, text="min")
        lab_preparation = tk.Label(self, text="Zubereitung: ")
        lab_ingredients = tk.Label(self, text="Zutaten: ")
        '''Entryboxes'''
        ent_recipe_name = tk.Entry(self, width=40)
        ent_duration = tk.Entry(self, width=10)
        txt_ingredients = tk.Text(self, width=40, height=10)
        txt_ingredients.bind("<Tab>", controller.focus_next_window)
        txt_preparation = tk.Text(self, width=40, height=10)
        txt_preparation.bind("<Tab>", controller.focus_next_window)
        '''Buttons'''
        but_check = tk.Button(self, text="Prüfen")
        but_save = tk.Button(self, text="Speichern")
        but_read = tk.Button(self, text="Text", command=database_files.readall)
        but_clear = tk.Button(self, text="Neues Rezept")

        '''GUI Elemente positionieren'''
        lab_recipe_name.grid(row=0, column=0, sticky=tk.NE)
        ent_recipe_name.grid(row=0, column=1, columnspan=2, padx=2, pady=2, sticky=tk.W)
        lab_duration.grid(row=1, column=0, sticky=tk.NE)
        ent_duration.grid(row=1, column=1, padx=2, pady=2, sticky=tk.NSEW)
        lab_minutes.grid(row=1, column=2, sticky=tk.NW)
        lab_ingredients.grid(row=2, column=0, sticky=tk.NE)
        txt_ingredients.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        lab_preparation.grid(row=3, column=0, sticky=tk.NE)
        txt_preparation.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        but_check.grid(row=4, column=0)
        but_save.grid(row=4, column=1)
        but_read.grid(row=4, column=2)
        but_clear.grid(row=4, column=3)
        ent_recipe_name.config(state="readonly")

        ent_recipe_name.config(state="normal")
        ent_recipe_name.insert(tk.END, "Testname")
        ent_recipe_name.config(state="readonly")


app = Recipedb()

app.mainloop()