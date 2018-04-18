import tkinter as tk
import sqlite3
alle = tk.Tk()

listboxRezepte = tk.Listbox(alle, selectmode='browse')
listboxRezepte.pack()
connection = sqlite3.connect("Rezeptdatenbank.db")
cursor = connection.cursor()
cursor.execute("SELECT rezeptname FROM rezepte")
result = cursor.fetchall()
listboxRezepte.delete(0, tk.END)
for r in result:
    listboxRezepte.insert('end', r)
connection.commit()

alle.mainloop()