from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

# Define your database connection and cursor
conn = sqlite3.connect('rockinRecipes.py')
c = conn.cursor()


@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    # Handle recipe submissions
    return jsonify({"message": "Recipe submitted successfully"})


@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    # Retrieve existing recipes from the database
    c.execute("SELECT * FROM recipes")
    recipes = c.fetchall()

    # Function to convert the data to a dictionary for JSON response
    def recipe_to_dict(recipe):
        return {
            "id": recipe[0],
            "name": recipe[1],
            "ingredients": recipe[2],
            "image_path": recipe[3]
        }

    recipes_dict = [recipe_to_dict(recipe) for recipe in recipes]

    return jsonify(recipes_dict)


if __name__ == '__main__':
    app.run(debug=True)


def recipe_request():
    response = requests.get("http://localhost:5000/get_recipes")  # future URL
    if response.status_code == 200:
        return response.json()
    else:
        return None



