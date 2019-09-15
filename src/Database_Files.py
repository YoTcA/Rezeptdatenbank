import sqlite3
from pathlib import Path



def create_connection(db_file):
    # Create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQliteversion: " + sqlite3.version)
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(e)
    else:
        cur.execute("""CREATE TABLE IF NOT EXISTS recipes (
                            recipe_name TEXT COLLATE NOCASE,
                            duration INTEGER,
                            portions INTEGER,
                            effort INTEGER,
                            rating INTEGER,
                            instructions TEXT,
                            CONSTRAINT recipe_name_unique UNIQUE (recipe_name))
                            """)
        cur.execute("""CREATE TABLE IF NOT EXISTS ingredients (
                            recipe_name TEXT COLLATE NOCASE,                    
                            quantity REAL,
                            unit TEXT,
                            ingredient TEXT COLLATE NOCASE)
                            """)
        conn.commit()
    finally:
        if conn:
            conn.close()

def readall_recipes(db_file):
    # read all data from database
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(e)
    else:
        for row in cur.execute('SELECT * FROM recipes'):
            print(row)

def readall_ingredients(db_file):
    # read all data from database
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(e)
    else:
        for row in cur.execute('SELECT * FROM ingredients'):
            print(row)

def add_recipe(db_file, recipe, ingredients):
    # input: (recipe_name, duration, portions, effort, rating, instructions)
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        sql = "INSERT INTO recipes (recipe_name, duration, portions, effort, rating, instructions) VALUES(?,?,?,?,?,?)"
        cur.execute(sql, recipe)
    except sqlite3.Error as e:
        print(e)
    else:
        try:
            sql = "INSERT INTO ingredients (recipe_name, quantity, unit, ingredient) VALUES(?,?,?,?)"
            cur.execute(sql, ingredients)
        except sqlite3.Error as e:
            print(e)
        else:
            conn.commit()
    finally:
        if conn:
            conn.close()

def add_ingredients(db_file, value):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(e)
    else:
        sql = "INSERT INTO ingredients (recipe_name, quantity, unit, ingredient) VALUES(?,?,?,?)"
        cur.execute(sql, value)
        conn.commit()
    finally:
        if conn:
            conn.close()

create_connection("Rezeptdatenbank.db")
readall_recipes("Rezeptdatenbank.db")
readall_ingredients("Rezeptdatenbank.db")
add_recipe("Rezeptdatenbank.db", ["Test", 10, 2, 3, 4, "Test3"], ["Test", 1, "TL", "Milch"])





'''
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

def search_exact_recipe_name(recipe_name):
    results = []
    if recipe_name:
        for row in cursor.execute('SELECT recipename FROM recipe WHERE recipename=?', (recipe_name.strip(),)):
                    results.append(row[0])
    return results

def search_recipe_name(recipe_name):
    results = []
    # allow the usage of * as wildcard
    if recipe_name == "*":
        recipe_name = "%"

    # search for recipe name similar to the input
    if recipe_name:
        for row in cursor.execute('SELECT recipename FROM recipe WHERE recipename LIKE ?', ('%' + recipe_name + '%',)):
                    results.append(row[0])
    return results

def search_ingredients(ingredients):
    results = []
    if ingredients:
        for ingredient in ingredients:
            for row in cursor.execute('SELECT recipename FROM ingredients WHERE ingredient=? COLLATE NOCASE', (ingredient,)):
                results.append(row[0])
    return results

def get_duration(recipe_name):
    result = cursor.execute('SELECT duration FROM recipe WHERE recipename=?', (recipe_name,)).fetchone()
    if result:
        return result[0]
    else:
        return False

def get_all_recipe_name():
    result = cursor.execute('SELECT recipename FROM recipe')
    return result

def get_preparation(recipe_name):
    result = cursor.execute('SELECT preparation FROM recipe WHERE recipename=?', (recipe_name,)).fetchone()
    if result:
        return result[0]
    else:
        return False

def get_ingredients(recipe_name):
    result = []
    for row in cursor.execute('SELECT quantity, unit, ingredient from ingredients WHERE recipename=?', (recipe_name,)):
        print(row[0])
        ingredient = ""
        i = 0
        if row[0]:
            if float(row[0]) % 1 == 0:
                ingredient = str(int(row[0])) + "\t"
                i = 1
        for item in row[i:]:
            ingredient = ingredient + str(item) + "\t"
        result.append(ingredient.rstrip("\t"))
    return result
'''