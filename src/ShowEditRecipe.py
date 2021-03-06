import tkinter as tk
import Database_Files
from tkinter import ttk



class ShowEditRecipe(tk.Frame):

    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.pages = pages




        # GUI Elemente definieren
        # Label
        self.lab_recipe_name = tk.Label(self, text="Rezeptname: ")
        self.lab_duration = tk.Label(self, text="Dauer: ")
        self.lab_minutes = tk.Label(self, text="min")
        self.lab_preparation = tk.Label(self, text="Zubereitung: ")
        self.lab_ingredients = tk.Label(self, text="Zutaten: ")
        # Entryboxes
        self.ent_recipe_name = tk.Entry(self, width=40)
        self.ent_duration = tk.Entry(self, width=10)
        self.txt_ingredients = tk.Text(self, width=40, height=10, tabs=('1.5c', '3c', '12c', '13c'))
        self.txt_ingredients.bind("<Tab>", controller.focus_next_window)
        self.txt_preparation = tk.Text(self, width=40, height=10)
        self.txt_preparation.bind("<Tab>", controller.focus_next_window)

        #Frame for Buttons
        self.frame_buttons = tk.Frame(self)

        # Buttons
        self.but_check = ttk.Button(self.frame_buttons, text="Prüfen", width=12,
                                   command=self.test)
        self.but_save = ttk.Button(self.frame_buttons, text="Speichern", width=12)
        self.but_read = ttk.Button(self.frame_buttons, text="Text", width=12,
                                  command=Database_Files.readall)
        self.but_clear = ttk.Button(self.frame_buttons, text="Neues Rezept", width=12)

        # GUI Elemente positionieren
        self.lab_recipe_name.grid(row=0, column=0, sticky=tk.NE)
        self.ent_recipe_name.grid(row=0, column=1, columnspan=2, padx=2, pady=2, sticky=tk.W)
        self.lab_duration.grid(row=1, column=0, sticky=tk.NE)
        self.ent_duration.grid(row=1, column=1, padx=2, pady=2, sticky=tk.NSEW)
        self.lab_minutes.grid(row=1, column=2, sticky=tk.NW)
        self.lab_ingredients.grid(row=2, column=0, sticky=tk.NE)
        self.txt_ingredients.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        self.lab_preparation.grid(row=3, column=0, sticky=tk.NE)
        self.txt_preparation.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky=tk.NW)
        # get the grid size, to always pack the buttons on the buttom
        column, row = self.grid_size()
        self.frame_buttons.grid(row=row, column=0, columnspan=column+2, sticky=tk.EW)
        self.but_check.grid(row=0, column=0, padx=2, pady=2, sticky=tk.EW)
        self.but_save.grid(row=0, column=1, padx=2, pady=2, sticky=tk.EW)
        self.but_read.grid(row=0, column=2, padx=2, pady=2, sticky=tk.EW)
        self.but_clear.grid(row=0, column=3, padx=2, pady=2, sticky=tk.EW)
        # get the grid size, to always pack the buttons on the buttom
        column, row = self.frame_buttons.grid_size()
        for i in range(column):
            self.frame_buttons.columnconfigure(i, weight=1)

        self.ent_recipe_name.insert(tk.END, "Testname")
        self.txt_preparation.insert(tk.END, "Testname")

    # def test(self):
    #     print("ok")
    #
    # def open_recipe(self, recipe_name, duration, ingredients, preparaition):
    #     fields = [self.ent_duration, self.ent_duration, self.txt_ingredients, self.txt_preparation]
    #     values = [recipe_name, duration, ingredients, preparaition]
    #     i = 0
    #     for field in fields:
    #         field.config(state="normal")
    #         field.insert(tk.END, values[i])
    #         i += 1
    #         if field.winfo_class() == "Entry":
    #             field.config(state="readonly")
    #         elif field.winfo_class() == "Text":
    #             field.config(state="disabled")
    def test(self):
        print(self.txt_ingredients.get("1.0", "end-1c"))
        a= self.controller.button_bar



def get_data(Page, recipe_name, duration, ingredient_list, preparation):
    print(recipe_name)
    print(duration)
    print(ingredient_list)
    print(preparation)
    Page.ent_recipe_name.config(state="normal")
    Page.ent_recipe_name.insert(tk.END, recipe_name)
    Page.ent_recipe_name.config(state="readonly")

if __name__ == "__main__":
    import Rezeptdatenbank

