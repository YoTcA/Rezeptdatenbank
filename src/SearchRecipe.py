import tkinter as tk
from tkinter import ttk
import Database_Files
import re
import ShowEditRecipe


def openrecipe():
    print(SearchRecipe.get_active)



class SearchRecipe(tk.Frame):
    def get_active(self):
        return self.lbx_recipelist.get(tk.ACTIVE)[0]

    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.pages = pages

        # GUI-Elemente erstellen
        self.lbl_recipe_name = tk.Label(self, text="Rezeptname:")
        self.lbl_ingredients = tk.Label(self, text="Zutaten:\n (Bitte Einzahl\nverwenden)")
        self.lbl_result_list = tk.Label(self, text="Ergebnisse:")
        self.ent_recipe_name = tk.Entry(self)
        self.txt_ingredients = tk.Text(self, width=40, height=4)
        self.txt_ingredients.bind("<Tab>", controller.focus_next_window)
        self.lbx_recipelist = tk.Listbox(self, selectmode=tk.SINGLE)
        self.but_search = ttk.Button(self, text="Suchen",
                                command=lambda: self.search_recipes(self.ent_recipe_name.get(), self.txt_ingredients.get("1.0", "end-1c")))
        self.but_open = ttk.Button(self, text="Anzeigen",
                              command=self.open_recipe)#open_recipe(self.lbx_recipelist.get(tk.ACTIVE)[0]))
        # GUI-Elemente positionieren
        self.lbl_recipe_name.grid(row=0, column=0, sticky=tk.E)
        self.ent_recipe_name.grid(row=0, column=1, sticky=tk.NSEW)
        self.but_search.grid(row=0, column=2)
        self.lbl_ingredients.grid(row=2, column=0, sticky=tk.E)
        self.txt_ingredients.grid(row=2, column=1, sticky=tk.W)
        self.lbl_result_list.grid(row=3, column=0, sticky=tk.E)
        self.lbx_recipelist.grid(row=3, column=1, sticky=tk.NSEW)
        self.but_open.grid(row=4, column=0)

    def search_recipes(self, recipe_name, ingredients):
        results = []
        # execute if a recipe_name is given
        print(recipe_name)
        if recipe_name:
            for row in Database_Files.search_recipe_name((recipe_name)):
                results.append(row)

        # divide the ingredients into single items
        ingredient_result = []
        if len(ingredients) > 0:
            rows = ingredients.splitlines()
            for row in rows:
                ingredient_result.append(re.split('\W+\s', row))
        ingredient_result = [item for sublist in ingredient_result for item in sublist]
        print(ingredient_result)

        # execute when ingredient_result is not empty
        '''if ingredient_result:
            results.append(database_files.search_ingredients(ingredient_result))'''

        if ingredient_result:
            for row in Database_Files.search_ingredients(ingredient_result):
                results.append(row)
        # empty the listbox before adding new items
        self.lbx_recipelist.delete(0, tk.END)

        # eliminate double entries in results and add the unique values to the listbox
        for result in list(set(results)):
            self.lbx_recipelist.insert(0, str(result))
        return True

    def open_recipe(self):
        selection = self.lbx_recipelist.curselection()
        recipe_name = self.lbx_recipelist.get(selection)
        target = self.controller.frames[self.pages["ShowEditRecipe"]]

        if recipe_name:
            # read the values from the database
            duration = Database_Files.get_duration(recipe_name)
            ingredients = Database_Files.get_ingredients(recipe_name)
            ingredient_list = ""
            # convert the database result to a line formated text
            for value in ingredients:
                ingredient_list = ingredient_list + self.controller.double_space(value.strip()) + "\n"
            preparation = Database_Files.get_preparation(recipe_name)
            print("ingredientresult: " + ingredient_list)
            values = [recipe_name, duration, ingredient_list, preparation]
            fields = [target.ent_recipe_name, target.ent_duration, target.txt_ingredients, target.txt_preparation]
            for field, value in zip(fields, values):
                if field.winfo_class() == "Entry":
                    field.config(state="normal")
                    field.delete(0, tk.END)
                    field.insert(tk.END, value)
                    field.config(state="readonly")
                elif field.winfo_class() == "Text":
                    field.config(state="normal")
                    field.delete('1.0', tk.END)
                    field.insert(tk.END, value)
                    field.config(state="disabled")

            # print("Rezeptname: " + str(recipe_name))
            # print("Dauer: " + str(duration))
            # print("Preparation: " + str(preparation))
            # print("Zutaten: " + str(ingredients))
        return True

