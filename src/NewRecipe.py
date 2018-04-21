import tkinter as tk
from tkinter import messagebox
import database_files


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


class NewRecipe(tk.Frame):
    # create the page to input a new recipe
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        NewRecipe.sv = tk.StringVar()

        self.preparation_results = []
        self.ingredient_results = []

        def clear_entries():
            if messagebox.askyesno("Neues Rezept", "Alle nicht gespeicherten Daten gehen verloren. Fortfahren?"):
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
        '''but_check = tk.Button(self, text="Prüfen",
                               command= lambda: self.getingredients(ent_recipe_name.get(),
                                                                    ent_duration.get(),
                                                                    txt_preparation.get("1.0", "end-1c"),
                                                                    txt_ingredients.get("1.0", "end-1c")))'''
        but_save = tk.Button(self, text="Speichern",
                                  command= lambda: self.save_recipe(ent_recipe_name.get(),
                                                                    ent_duration.get(),
                                                                    txt_preparation.get("1.0", "end-1c"),
                                                                    txt_ingredients.get("1.0", "end-1c")))
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
        '''but_check.grid(row=4, column=0)'''
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

    def save_recipe(self, recipe_name, duration, preparation, ingredient_txt):
        if recipe_name:
            unitlist = ["l", "ml", "g", "kg", "gr", "kl", "cup", "st", "pc", "liter", "gramm", "kilo", "stück", "große",
                        "kleine", "großes", "kleines"]
            quantities = []
            units = []
            ingredients = []
            ingredientlist = []
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
                    if not isfloat(quantity):
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
            ingredientlist.append(recipe_name)
            ingredientlist.append(quantities)
            ingredientlist.append(units)
            ingredientlist.append(ingredients)
            recipelist.append(recipe_name)
            recipelist.append(duration)
            recipelist.append(preparation)
            database_files.write_data(recipelist, ingredientlist)
        else:
            messagebox.showerror("Fehleneder Rezeptname", "Bitte einen Rezeptnamen eingeben.")






    def doublespace(self, text):
        while "  " in text:
           text = text.replace("  ", " ")
        return text

    '''def getingredients(self, recipename, duration, preparation, ingredienttext):
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
            messagebox.showerror("Fehlender Rezeptname", "Bitte einen Rezeptnamen eingeben.")'''
