"""ggf Datenbank erstellen und Tabellen anlegen"""
import sqlite3
connection = sqlite3.connect("Rezeptdatenbank.db")
cursor = connection.cursor()

#cursor.execute("""DROP TABLE rezepte;""")
#cursor.execute("""DROP TABLE zutaten;""")

cursor.execute("""CREATE TABLE IF NOT EXISTS rezepte (
    rezeptname TEXT, dauer TEXT, zubereitung TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS zutaten (
    rezeptname TEXT, menge INTEGER, einheit TEXT, zutat TEXT)""")

connection.commit()