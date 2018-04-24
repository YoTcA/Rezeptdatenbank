import tkinter as tk
import Database_Files

class ShowEditRecipe(tk.Frame):
    def test(self):
        print("ok")

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
        self.ent_duration = tk.Entry(self, width=10)
        self.txt_ingredients = tk.Text(self, width=40, height=10)
        self.txt_ingredients.bind("<Tab>", controller.focus_next_window)
        self.txt_preparation = tk.Text(self, width=40, height=10)
        self.txt_preparation.bind("<Tab>", controller.focus_next_window)
        '''Buttons'''
        but_check = tk.Button(self, text="Prüfen")
        but_save = tk.Button(self, text="Speichern")
        but_read = tk.Button(self, text="Text", command=Database_Files.readall)
        but_clear = tk.Button(self, text="Neues Rezept")

        '''GUI Elemente positionieren'''
        lab_recipe_name.grid(row=0, column=0, sticky=tk.NE)
        ent_recipe_name.grid(row=0, column=1, columnspan=2, padx=2, pady=2, sticky=tk.W)
        lab_duration.grid(row=1, column=0, sticky=tk.NE)
        self.ent_duration.grid(row=1, column=1, padx=2, pady=2, sticky=tk.NSEW)
        lab_minutes.grid(row=1, column=2, sticky=tk.NW)
        lab_ingredients.grid(row=2, column=0, sticky=tk.NE)
        self.txt_ingredients.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        lab_preparation.grid(row=3, column=0, sticky=tk.NE)
        self.txt_preparation.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        but_check.grid(row=4, column=0)
        but_save.grid(row=4, column=1)
        but_read.grid(row=4, column=2)
        but_clear.grid(row=4, column=3)
        ent_recipe_name.config(state="readonly")

        ent_recipe_name.config(state="normal")
        ent_recipe_name.insert(tk.END, "Testname")
        ent_recipe_name.config(state="readonly")

def get_data(Page, recipe_name, duration, ingredient_list, preparation):
    print(recipe_name)
    print(duration)
    print(ingredient_list)
    print(preparation)
    Page.ent_recipe_name.config(state="normal")
    Page.ent_recipe_name.insert(tk.END, recipe_name)
    Page.ent_recipe_name.config(state="readonly")