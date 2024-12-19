# AI-Powered Personal Chef and Nutritionist

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from transformers import pipeline
import requests
from sklearn.cluster import KMeans

# ----------------------------
# Ingredient Recognition from Photo
# ----------------------------

def load_model():
    base_model = MobileNetV2(weights='imagenet', include_top=True)
    return base_model

def recognize_ingredients_from_photo(photo_path, model):
    """
    Recognizes ingredients from a photo of a fridge, pantry, or countertop.
    """
    image = load_img(photo_path, target_size=(224, 224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)

    predictions = model.predict(image_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)

    detected_ingredients = [pred[1] for pred in decoded_predictions[0]]
    return detected_ingredients

# ----------------------------
# Recipe Generation Using GPT
# ----------------------------

def generate_recipe(ingredients, preferences):
    recipe_generator = pipeline("text-generation", model="gpt-2")
    prompt = f"Create a healthy recipe using {', '.join(ingredients)} tailored for {preferences}."
    result = recipe_generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text']

# ----------------------------
# Nutritional Analysis API
# ----------------------------

NUTRITION_API_URL = "https://api.edamam.com/api/nutrition-details"
NUTRITION_API_ID = "your_api_id"
NUTRITION_API_KEY = "your_api_key"

def analyze_nutrition(recipe):
    data = {
        "title": recipe,
        "ingr": recipe.split('.')
    }
    response = requests.post(NUTRITION_API_URL, json=data, params={
        "app_id": NUTRITION_API_ID,
        "app_key": NUTRITION_API_KEY
    })
    return response.json()

# ----------------------------
# Personalized Meal Planning
# ----------------------------

def recommend_meal_plan(user_preferences, past_feedback):
    recipes_data = np.array([[calories, protein, fat] for calories, protein, fat in past_feedback])
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(recipes_data)
    cluster = kmeans.predict([user_preferences])[0]
    return [recipe for recipe, label in zip(recipes_data, kmeans.labels_) if label == cluster]

# ----------------------------
# Main Functionality
# ----------------------------

def main():
    print("Welcome to the AI Personal Chef!")

    # Load pre-trained model
    model = load_model()

    # Step 1: Recognize Ingredients
    photo_path = input("Enter the path to your fridge or pantry photo: ")
    detected_ingredients = recognize_ingredients_from_photo(photo_path, model)
    print(f"Detected ingredients: {', '.join(detected_ingredients)}")

    # Step 2: Generate Recipe
    preferences = input("Enter your dietary preferences (e.g., low-carb, vegan): ")
    recipe = generate_recipe(detected_ingredients, preferences)
    print(f"Generated Recipe:\n{recipe}")

    # Step 3: Nutritional Analysis
    analyze = input("Do you want to analyze the nutritional information? (yes/no): ")
    if analyze.lower() == "yes":
        nutrition = analyze_nutrition(recipe)
        print(f"Nutritional Information: {nutrition}")

    # Step 4: Personalized Meal Plan
    past_feedback = [
        [400, 15, 10],
        [600, 25, 20],
        [500, 20, 15]
    ]
    user_preferences = [
        float(input("Enter your preferred calorie intake: ")),
        float(input("Enter your preferred protein intake: ")),
        float(input("Enter your preferred fat intake: "))
    ]
    meal_plan = recommend_meal_plan(user_preferences, past_feedback)
    print(f"Recommended Meal Plan: {meal_plan}")

if __name__ == "__main__":
    main()
