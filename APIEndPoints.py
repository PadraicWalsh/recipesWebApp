from flask import Flask, request, jsonify, send_file
import sqlite3
import os

app = Flask(__name__)

# Define the path to the SQLite database
db_path = 'recipes.db'


def initialize_database():
    # Create a connection and cursor to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create the recipes table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            ingredients TEXT,
            image_path TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


initialize_database()


@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    data = request.json
    if 'name' not in data or 'ingredients' not in data:
        return jsonify({"error": "Recipe data is incomplete"}), 400

    name = data['name']
    ingredients = data['ingredients']

    # Insert the new recipe into the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO recipes (name, ingredients) VALUES (?, ?)", (name, ingredients))
    conn.commit()
    conn.close()

    return jsonify({"message": "Recipe submitted successfully"})


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


@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Handle image upload and save it to a specified directory
    # You can use a library like Flask-Uploads for this purpose
    # Ensure the uploaded image is stored securely and has a unique filename
    # Return the path to the uploaded image or an error message

    # Example code for saving an image (customize this part)
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            image.save(os.path.join('image_uploads', image.filename))
            return jsonify({"message": "Image uploaded successfully"})

    return jsonify({"error": "Image upload failed"}), 400


@app.route('/get_image/<filename>', methods=['GET'])
def get_image(filename):
    # Serve the uploaded image to the frontend
    return send_file(os.path.join('image_uploads', filename))


if __name__ == '__main__':
    app.run(debug=True)
