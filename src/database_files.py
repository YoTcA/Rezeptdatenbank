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

def readall():
    # read all data from database
    for row in cursor.execute('SELECT * FROM ingredients'):
        print(row)
    for row in cursor.execute('SELECT * FROM recipe'):
        print(row)

def write_data(preparation_list, ingredient_list):
    # write input to database
    for i in range(len(ingredient_list[3])):
        ingredients = []
        ingredients.append(ingredient_list[0])
        for a in range(1, 4):
            ingredients.append(ingredient_list[a][i])
        cursor.execute('INSERT INTO ingredients VALUES (?,?,?,?)', ingredients)
    connection.commit()
    cursor.execute('INSERT INTO recipe VALUES (?,?,?)', preparation_list)
    connection.commit()

