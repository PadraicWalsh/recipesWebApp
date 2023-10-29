import streamlit as st

st.title("Rockin' Recipes")
st.subheader("Share your favourite recipes with us")
st.write("If you're good in the kitchen, we want to know!")

# Create a form to allow users to upload recipes
recipe_name = st.text_input("Recipe Name, "
                            "e.g Maria's magic muffins!", "")
ingredients = st.text_area("Ingredients", placeholder="Add ingredients here...")
uploaded_image = st.file_uploader("Upload a Photo of Your Dish", type=["jpg", "png", "jpeg"])

if st.button("Submit Recipe"):
    # Save the recipe and photo if provided
    if recipe_name and ingredients:
        # Save the recipe details in a database or data file
        st.success("Recipe submitted successfully!")
        # You can also save the uploaded image if provided

# Display existing recipes from the community
st.subheader("Explore Rockin' Recipes")
# Here, you can display recipes that users have previously uploaded
# You can retrieve and display them from your database or data file