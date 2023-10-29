import sqlite3

# Database initialization and table creation


def initialize_database():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            ingredients TEXT,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Function to insert a new recipe into the database
def insert_recipe(name, ingredients, image_path):
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('INSERT INTO recipes (name, ingredients, image_path) VALUES (?, ?, ?)', (name, ingredients, image_path))
    conn.commit()
    conn.close()

# Function to retrieve existing recipes
def get_recipes():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM recipes')
    recipes = c.fetchall()
    conn.close()
    return recipes
