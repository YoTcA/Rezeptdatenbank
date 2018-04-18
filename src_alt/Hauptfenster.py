import tkinter as tk
import StartUp

"""Fenstereigenschaften"""
main = tk.Tk()
main.title("Rezeptdatenbank V0.1")

def comRezeptsuche():
    import Rezeptsuche
def comRezeptneu():
    import Rezeptneu
def comRezeptedit():
    print("LOL")
def comRezeptalle():
    import RezeptAlle


tk.Button(main, text="Rezept suchen", command=comRezeptsuche, width=40).pack()
tk.Button(main, text="neues Rezept eingeben", command=comRezeptneu, width=40).pack()
tk.Button(main, text="Rezept bearbeiten", command=comRezeptedit, width=40).pack()
tk.Button(main, text="Alle Rezepte anzeigen", command=comRezeptalle, width=40).pack()
tk.Button(main, text="Beenden", command=main.quit, width=40).pack()

main.mainloop()