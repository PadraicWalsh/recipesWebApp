from flask import Flask, request, jsonify, send_file
import sqlite3
import os

app = Flask(__name__)

# Define the path to the SQLite database
db_path = 'recipes.db'

# ... (Previous code)

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM recipes")
    recipes = c.fetchall()
    conn.close()

    recipes_dict = []
    for recipe in recipes:
        recipe_id, name, ingredients, image_path = recipe
        recipe_info = {
            "id": recipe_id,
            "name": name,
            "ingredients": ingredients,
            "image_path": image_path
        }
        recipes_dict.append(recipe_info)

    return jsonify(recipes_dict)

@app.route('/get_image/<filename>', methods=['GET'])
def get_image(filename):
    # Serve the uploaded image to the frontend
    return send_file(os.path.join('image_uploads', filename))

# ... (Rest of your code)

if __name__ == '__main__':
    app.run(debug=True)
