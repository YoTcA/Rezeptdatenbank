import tkinter as tk
from tkinter import ttk
import database_files
import re


def openrecipe():
    print(SearchRecipe.get_active)

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
        #ShowEditRecipe.get_data(ShowEditRecipe.ShowEditRecipe, recipe_name, duration, ingredients, preparation)
        #ShowEditRecipe.ShowEditRecipe.test(ShowEditRecipe)
    # print(map(int, lbx_recipelist.curselection()))

class SearchRecipe(tk.Frame):
    def get_active(self):
        return self.lbx_recipelist.get(tk.ACTIVE)[0]

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
            self.lbx_recipelist.delete(0, tk.END)

            # eliminate double entries in results and add the unique values to the listbox
            for result in list(set(results)):
                self.lbx_recipelist.insert(0, result)
            return True



        # GUI-Elemente erstellen
        lbl_recipe_name = tk.Label(self, text="Rezeptname:")
        lbl_ingredients = tk.Label(self, text="Zutaten:\n (Bitte Einzahl\nverwenden)")
        lbl_result_list = tk.Label(self, text="Ergebnisse:")
        ent_recipe_name = tk.Entry(self)
        txt_ingredients = tk.Text(self, width=40, height=4)
        txt_ingredients.bind("<Tab>", controller.focus_next_window)
        self.lbx_recipelist = tk.Listbox(self, selectmode=tk.SINGLE)
        but_search = ttk.Button(self, text="Suchen",
                                command=lambda: search_recipes(ent_recipe_name.get(), txt_ingredients.get("1.0", "end-1c")))
        but_open = ttk.Button(self, text="Anzeigen",
                              command=openrecipe)#open_recipe(self.lbx_recipelist.get(tk.ACTIVE)[0]))
        # GUI-Elemente positionieren
        lbl_recipe_name.grid(row=0, column=0, sticky=tk.E)
        ent_recipe_name.grid(row=0, column=1, sticky=tk.NSEW)
        but_search.grid(row=0, column=2)
        lbl_ingredients.grid(row=2, column=0, sticky=tk.E)
        txt_ingredients.grid(row=2, column=1, sticky=tk.W)
        lbl_result_list.grid(row=3, column=0, sticky=tk.E)
        self.lbx_recipelist.grid(row=3, column=1, sticky=tk.NSEW)
        but_open.grid(row=4, column=0)
