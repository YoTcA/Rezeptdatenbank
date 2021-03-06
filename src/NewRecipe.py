import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Database_Files
import Functions


# check if there is already a recipe with the inputed recipe name in the database



class NewRecipe(tk.Frame):
    # create the page to input a new recipe
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.pages = pages

        self.sv = tk.StringVar()
        self.preparation_results = []
        self.ingredient_results = []

        # GUI Elemente definieren
        # Label
        self.lab_recipe_name = tk.Label(self, text="Rezeptname: ")
        self.lab_duration = tk.Label(self, text="Dauer: ")
        self.lab_minutes = tk.Label(self, text="min")
        self.lab_preparation = tk.Label(self, text="Zubereitung: ")
        self.lab_ingredients = tk.Label(self, text="Zutaten:\n (Bitte Einzahl\nverwenden)", justify=tk.RIGHT)
        # Entryboxes
        self.ent_recipe_name = tk.Entry(self, width=40, textvariable=self.sv, validate="focusout",
                                   validatecommand=self.check_input_exists)
        self.ent_duration = tk.Entry(self, width=10)
        self.txt_ingredients = tk.Text(self, width=40, height=10)
        self.txt_ingredients.bind("<Tab>", controller.focus_next_window)
        self.txt_preparation = tk.Text(self, width=40, height=10)
        self.txt_preparation.bind("<Tab>", controller.focus_next_window)

        # Frame for Buttons
        self.frame_buttons = tk.Frame(self)

        # Buttons
        self.but_save = ttk.Button(self.frame_buttons, text="Speichern", width=12,
                                   command= lambda: self.save_recipe(self.ent_recipe_name.get(),
                                                                     self.ent_duration.get(),
                                                                     self.txt_preparation.get("1.0", "end-1c"),
                                                                     self.txt_ingredients.get("1.0", "end-1c")))
        self.but_read = ttk.Button(self.frame_buttons, text="Text", width=12,
                                   command=Database_Files.readall)
        self.but_clear = ttk.Button(self.frame_buttons, text="Neues Rezept", width=12,
                                    command=self.clear_entries)

        # GUI Elemente positionieren
        self.lab_recipe_name.grid(row=0, column=0, sticky=tk.NE)
        self.ent_recipe_name.grid(row=0, column=1,columnspan=2, padx=2, pady=2, sticky=tk.W)
        self.lab_duration.grid(row=1, column=0, sticky=tk.NE)
        self.ent_duration.grid(row=1, column=1, padx=2, pady=2, sticky=tk.NSEW)
        self.lab_minutes.grid(row=1, column=2, sticky=tk.NW)
        self.lab_ingredients.grid(row=2, column=0, sticky=tk.NE)
        self.txt_ingredients.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        self.lab_preparation.grid(row=3, column=0, sticky=tk.NE)
        self.txt_preparation.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        # get the grid size, to always pack the buttons on the buttom
        column, row = self.grid_size()
        self.frame_buttons.grid(row=row, column=0, columnspan=column + 2, sticky=tk.EW)
        # but_check.grid(row=4, column=0)
        self.but_save.grid(row=0, column=0, padx=2, pady=2, sticky=tk.EW)
        self.but_read.grid(row=0, column=1, padx=2, pady=2, sticky=tk.EW)
        self.but_clear.grid(row=0, column=2, padx=2, pady=2, sticky=tk.EW)
        # get the grid size, to always pack the buttons on the buttom
        column, row = self.frame_buttons.grid_size()
        for i in range(column):
            self.frame_buttons.columnconfigure(i, weight=1)

    def clear_entries(self):
        if messagebox.askyesno("Neues Rezept", "Alle nicht gespeicherten Daten gehen verloren. Fortfahren?"):
            self.ent_recipe_name.delete(0, tk.END)
            self.ent_duration.delete(0, tk.END)
            self.txt_ingredients.delete('1.0', tk.END)
            self.txt_preparation.delete('1.0', tk.END)
        return True

    def check_input_exists(self):
        recipe_name = self.sv.get()
        result = self.check_recipe_name2(recipe_name)
        if result == 1:
            print("noch nicht vergeben")
            return True
        elif result == 2:
            print("Name bereits vergeben")
            tmp_value = messagebox.askyesno("Rezeptname bereits vergeben.",
                                            "Rezeptname bereits vergeben. Rezept anzeigen?")
            if tmp_value:
                self.controller.frames[self.pages["SearchRecipe"]].open_recipe(recipe_name)
                return 1
            else:
                print("nicht öffnen")
                return 2
        elif result == 3:
            print("bitte Name eingeben")
            return True

    def check_recipe_name2(self, recipe_name):
        if recipe_name:
            if Database_Files.search_exact_recipe_name(recipe_name):
                return 2 # recipe name already in use
            else:
                return 1 # recipe name not in use
        return 3 # no input


    def check_recipe_name(self, *args):
        if args:
            recipe_name = args[0]
        else:
            recipe_name = self.sv.get()
        for recipe in Database_Files.get_all_recipe_name():
            if recipe_name.strip() in recipe:
                tmp_value = messagebox.askyesno("Rezeptname bereits vergeben.",
                                                "Rezeptname bereits vergeben. Rezept anzeigen?")
                if tmp_value:
                    self.controller.frames[self.pages["SearchRecipe"]].open_recipe(recipe_name)
                    return 1
                else:
                    print("nicht öffnen")
                    return 2
        return True

    def save_recipe(self, recipe_name, duration, preparation, ingredient_txt):

        if recipe_name:
            if self.check_recipe_name2(recipe_name) == 1:
                unitlist = ["l", "ml", "g", "kg", "gr", "kl", "cup", "st", "pc", "liter", "gramm", "kilo", "stück", "große",
                            "kleine", "großes", "kleines"]
                quantities = []
                units = []
                ingredients = []
                # ingredientlist = []
                recipelist = []
                ingredients_rows = ingredient_txt.splitlines()
                for row in ingredients_rows:
                    if not row:
                        continue
                    a = 0
                    quantity = ""
                    unit = ""
                    row = self.doublespace(row)
                    parts = row.split()
                    # when there are more than 1 part, the first is treated as a quantity
                    if len(parts) > 1:
                        a = 1
                        quantity = parts[0]
                        # savety to replace decimal , with decimal .
                        quantity = quantity.replace(",", ".")
                        # check if the quantity was given as float
                        if not Functions.isfloat(quantity):
                            messagebox.showinfo("Menge falsch", "Menge als Zahl eingeben.")

                    if len(parts) > 2:
                        a = 2
                        unit = parts[1]

                    ingredient = parts[a]
                    a += 1

                    while a < len(parts):
                        ingredient = ingredient + " " + parts[a].strip()
                        a += 1

                    # if the unit is not a unit from unitlist, treat it as an part of the ingredient
                    if len(parts) > 2  and unit.lower() not in unitlist:
                        ingredient = unit + " " + ingredient
                        unit = ""

                    quantities.append(quantity)
                    units.append(unit)
                    ingredients.append(ingredient)
                ingredientlist = [recipe_name, quantities, units, ingredients]
                recipelist = [recipe_name, duration, preparation]
                Database_Files.write_data(recipelist, ingredientlist)
        else:
            messagebox.showerror("Fehleneder Rezeptname", "Bitte einen Rezeptnamen eingeben.")


    def doublespace(self, text):
        while "  " in text:
           text = text.replace("  ", " ")
        return text

if __name__ == "__main__":
    import Rezeptdatenbank
