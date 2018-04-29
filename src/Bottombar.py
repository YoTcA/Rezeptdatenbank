import tkinter as tk
from tkinter import ttk

class Bottombar(tk.Frame):
    def __init__(self, controller, pages):
        super().__init__(controller)
        butt_save = ttk.Button(self, text="Speichern")
