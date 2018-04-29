import tkinter as tk
from tkinter import ttk

class Toolbar(tk.Frame):
    def __init__(self, controller, pages):
        tk.Frame.__init__(self, controller)
        butt_new = ttk.Button(self, text="Neues Rezept", command=lambda: controller.show_frame(pages["NewRecipe"]))
        butt_new.pack(side=tk.LEFT, padx=2, pady=2)
        butt_search = ttk.Button(self, text="Rezept suchen", command=lambda: controller.show_frame(pages["SearchRecipe"]))
        butt_search.pack(side=tk.LEFT, padx=2, pady=2)
        butt_display = ttk.Button(self, text="Rezept anzeigen", command=lambda: controller.show_recipe())
        butt_display.pack(side=tk.LEFT, padx=2, pady=2)
        butt_edit = ttk.Button(self, text="Rezept bearbeiten", command=lambda: controller.edit_recipe())
        butt_edit.pack(side=tk.LEFT, padx=2, pady=2)
