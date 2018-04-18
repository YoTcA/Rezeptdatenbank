import sqlite3
connection = sqlite3.connect("Rezeptdatenbank.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM zutaten")
result = cursor.fetchall()
for r in result:
    print(r)