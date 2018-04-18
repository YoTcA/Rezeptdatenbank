import tkinter as tk
from tkinter import messagebox as msgbx
from tkinter import Text


import sqlite3
connection = sqlite3.connect("Rezeptdatenbank.db")
cursor = connection.cursor()
cursor2 = connection.cursor()


"""Funktionen"""
def actionSpeichern():
    global zutaten, rezept
    if entRezeptname.get()!= "":
        print(entRezeptname.get())
        rezept = (entRezeptname.get().strip(), entDauer.get().strip(), entZubereitung.get().strip())
        cursor2.execute('INSERT INTO rezepte VALUES (?,?,?)', rezept)
        x = 0
        while x < zutatenzahl:
            if variablesMenge[x].get() != "" or variablesEinheit[x].get() != "" or variablesZutat[x].get() != "":
                zutaten = (entRezeptname.get().strip(), variablesMenge[x].get().strip(), variablesEinheit[x].get().strip(), variablesZutat[x].get().strip())
                print(zutaten)
                cursor.execute('INSERT INTO zutaten VALUES (?,?,?,?)', zutaten)
            x += 1
        connection.commit()
    else:
        msgbx.showinfo("Fehler", "Rezeptname eingeben")




def actionReset():
    if msgbx.askyesno("Zurücksetzen", "Alle Eingaben löschen?"):
        for i in entriesMenge:
            i.delete(0, tk.END)
        for i in entriesEinheit:
            i.delete(0, tk.END)
        for i in entriesZutat:
            i.delete(0, tk.END)
        entRezeptname.delete(0, tk.END)
        # entMenge1.delete(0, tk.END)
        # entEinheit1.delete(0, tk.END)
        # entZutat1.delete(0, tk.END)
        # entMenge2.delete(0, tk.END)
        # entEinheit2.delete(0, tk.END)
        # entZutat2.delete(0, tk.END)
        # entMenge3.delete(0, tk.END)
        # entEinheit3.delete(0, tk.END)
        # entZutat3.delete(0, tk.END)
        # entZubereitung.delete(1.0, tk.END)

def actionQuit():
    if msgbx.askyesno("Beenden", "Anwendung schließen?"):
        tkrezept.destroy()


tkrezept = tk.Toplevel()
#main.geometry("500x100")

"""Objekte"""

buttonSpeicher = tk.Button(tkrezept, text="Speichern", command=actionSpeichern)
buttonReset = tk.Button(tkrezept, text="Zurücksetzen", command=actionReset)
buttonExit = tk.Button(tkrezept, text="Beenden", command=actionQuit)
labelWarnung = tk.Label(tkrezept, text="Test")
entRezeptname = tk.Entry(tkrezept, width=40)
entDauer = tk.Entry(tkrezept, width=10)
entZubereitung = tk.Text(tkrezept, width=40, height=10)



def comNeuezeile():
    global zutatenzahl, vaM, vaE, vaZ, enM, enE, enZ
    zutatenzahl += 1
    vaM = tk.StringVar()
    enM = tk.Entry(tkrezept, textvariable=vaM)
    enM.grid(row=zutatenzahl + zeile, column=0)
    variablesMenge.append(vaM)
    entriesMenge.append(enM)
    vaE = tk.StringVar()
    enE = tk.Entry(tkrezept, textvariable=vaE)
    enE.grid(row=zutatenzahl + zeile, column=1)
    variablesEinheit.append(vaE)
    entriesEinheit.append(enE)
    vaZ = tk.StringVar()
    enZ = tk.Entry(tkrezept, textvariable=vaZ)
    enZ.grid(row=zutatenzahl + zeile, column=2)
    variablesZutat.append(vaZ)
    entriesZutat.append(enZ)







"""Anordnung der default Objekte im Fenster"""
zeile=0
spalte=0
buttonSpeicher.grid(row=zeile, column=spalte, sticky=tk.E)
buttonReset.grid(row=zeile, column=spalte+2, sticky=tk.W)
buttonExit.grid(row=zeile, column=spalte+1)
zeile += 1
tk.Label(tkrezept, text="Rezeptname").grid(row=zeile, column=spalte, sticky=tk.E)
entRezeptname.grid(row=zeile, column=spalte+1, sticky=tk.W, columnspan=2)
zeile += 1
tk.Label(tkrezept, text="Dauer").grid(row=zeile, column=spalte, sticky=tk.E)
entDauer.grid(row=zeile, column=spalte+1, sticky=tk.W)
zeile += 1
tk.Label(tkrezept, text="Zubereitung").grid(row=zeile, column=spalte, sticky=tk.NE)
entZubereitung.grid(row=zeile, column=spalte+1, sticky=tk.W, columnspan=2)
zeile += 1
tk.Label(tkrezept, text="Menge").grid(row=zeile, column=spalte, sticky=tk.E)
tk.Label(tkrezept, text="Einheit").grid(row=zeile, column=spalte + 1)
tk.Label(tkrezept, text="Zutat").grid(row=zeile, column=spalte + 2, sticky = tk.W)
tk.Button(tkrezept, text="Neue Zutat", command=comNeuezeile).grid(row=zeile, column=spalte + 3)
zeile += 1

"""Zutatenliste"""
zutatenzahl=1
variablesMenge = []
entriesMenge = []
variablesEinheit = []
entriesEinheit = []
variablesZutat = []
entriesZutat = []
for i in range(zutatenzahl):
    global vaM, vaE, vaZ, enM, enE, enZ
    vaM = tk.StringVar()
    enM = tk.Entry(tkrezept, textvariable=vaM)
    enM.grid(row=i + zeile, column=0)
    variablesMenge.append(vaM)
    entriesMenge.append(enM)
    vaE = tk.StringVar()
    enE = tk.Entry(tkrezept, textvariable=vaE)
    enE.grid(row=i + zeile, column=1)
    variablesEinheit.append(vaE)
    entriesEinheit.append(enE)
    vaZ = tk.StringVar()
    enZ = tk.Entry(tkrezept, textvariable=vaZ)
    enZ.grid(row=i + zeile, column=2)
    variablesZutat.append(vaZ)
    entriesZutat.append(enZ)


tkrezept.mainloop()