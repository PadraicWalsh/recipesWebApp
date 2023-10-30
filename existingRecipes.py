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

#import streamlit as st
#import requests

# Streamlit app code (as in your original code)

# Function to get recipes from the Flask API
#def get_recipes():
#    response = requests.get("http://localhost:5000/get_recipes")  # Adjust the URL to your Flask app's URL
#    if response.status_code == 200:
#        recipes = response.json()
#       return recipes
#   else:
#       st.error("Failed to fetch recipes")

# Fetch recipes and display them
#recipes = get_recipes()
#if recipes:
#    st.subheader("Explore Rockin' Recipes")
#   for recipe in recipes:
#       st.write(f"Recipe Name: {recipe['name']}")
#       st.write(f"Ingredients: {recipe['ingredients']}")
#       st.image(f"http://localhost:5000/get_image/{recipe['image_path']}", caption="Recipe Image")
