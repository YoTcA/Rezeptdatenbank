import tkinter as tk
from tkinter import ttk

class Toolbar(tk.Frame):
    def __init__(self, controller, page):
        tk.Frame.__init__(self, controller)
        toolbar = tk.Frame(controller)
        butt_new = ttk.Button(toolbar, text="Neues Rezept", command=lambda: controller.show_frame(page["NewRecipe"]))
        butt_new.pack(side=tk.LEFT, padx=2, pady=2)
        butt_search = ttk.Button(toolbar, text="Rezept suchen", command=lambda: controller.show_frame(page["SearchRecipe"]))
        butt_search.pack(side=tk.LEFT, padx=2, pady=2)
        butt_display = ttk.Button(toolbar, text="Rezept anzeigen", command=lambda: controller.show_recipe())
        butt_display.pack(side=tk.LEFT, padx=2, pady=2)
        butt_edit = ttk.Button(toolbar, text="Rezept bearbeiten", command=lambda: controller.edit_recipe())
        butt_edit.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
