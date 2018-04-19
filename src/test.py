import sqlite3

# connect to database Rezeptdatenbank.db
connection = sqlite3.connect("Rezeptdatenbank.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS recipe (
            recipename TEXT COLLATE NOCASE,
             duration INTEGER,
              preparation TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ingredients (
            recipename TEXT COLLATE NOCASE,
             quantity REAL,
              unit TEXT,
               ingredient TEXT COLLATE NOCASE)""")
connection.commit()

for row in cursor.execute('SELECT ? FROM recipe WHERE recipename=?', ("duration", "asdf",)):
    print(row)
