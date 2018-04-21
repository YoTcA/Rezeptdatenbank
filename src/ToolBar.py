import tkinter as tk
from tkinter import ttk

class Toolbar(tk.Frame):
    def __init__(self, parent, page):
        tk.Frame.__init__(self, parent)
        toolbar = tk.Frame(parent)
        butt_new = ttk.Button(toolbar, text="Neues Rezept", command=lambda: parent.show_frame(page[1]))
        butt_new.pack(side=tk.LEFT, padx=2, pady=2)
        butt_search = ttk.Button(toolbar, text="Rezept suchen", command=lambda: parent.show_frame(page[2]))
        butt_search.pack(side=tk.LEFT, padx=2, pady=2)
        butt_display = ttk.Button(toolbar, text="Rezept anzeigen", command=lambda: parent.show_frame(page[3]))
        butt_display.pack(side=tk.LEFT, padx=2, pady=2)
        butt_edit = ttk.Button(toolbar, text="Rezept bearbeiten", command=lambda: parent.show_frame(page[3]))
        butt_edit.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)