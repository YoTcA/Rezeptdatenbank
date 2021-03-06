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