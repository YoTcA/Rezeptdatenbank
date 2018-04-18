import tkinter as tk
suche= tk.Tk()
#suche = tk.Toplevel()
import sqlite3


def actionRezeptsuche():
    suchbegriff = enRezeptname.get().strip()
    print(suchbegriff)
    connection = sqlite3.connect("Rezeptdatenbank.db")
    cursor = connection.cursor()
    cursor.execute("SELECT rezeptname FROM rezepte WHERE rezeptname=?", (suchbegriff,))
    result = cursor.fetchall()
    listboxRezepte.delete(0, tk.END)
    for r in result:
        listboxRezepte.insert('end', r)
    connection.commit()


enRezeptname = tk.Entry(suche, width=40)
enZutat = tk.Entry(suche, width=40)
zeile = 1
spalte = 1
tk.Label(suche, text="Rezeptname").grid(row=zeile, column=spalte, sticky=tk.E)
enRezeptname.grid(row=zeile, column=spalte+1)
zeile += 1
tk.Label(suche, text="Zutat").grid(row=zeile, column=spalte, sticky=tk.E)
enZutat.grid(row=zeile, column=spalte+1)
zeile += 1
tk.Button(suche, text="Suchen", command=actionRezeptsuche).grid(row=zeile, column=spalte, columnspan=2)
zeile += 1
listboxRezepte = tk.Listbox(suche, selectmode='browse')
#listboxRezepte.insert('end', 'Bernd')
#listboxRezepte.insert('end', 'Bernd')
#listboxRezepte.insert('end', 'Clara')
#listboxRezepte.insert('end', 'Dominik')
listboxRezepte.grid(row=zeile, column=spalte, columnspan=2)
suche.mainloop()