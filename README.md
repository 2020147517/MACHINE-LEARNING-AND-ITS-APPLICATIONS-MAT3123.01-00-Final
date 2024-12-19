# MACHINE-LEARNING-AND-ITS-APPLICATIONS-MAT3123.01-00-Final

# AI-Powered Personal Chef

## Project Overview
The AI-Powered Personal Chef is an innovative project designed to simplify your cooking experience. By analyzing a photo of your fridge, pantry, or countertop, the AI identifies available ingredients and generates personalized recipes tailored to your dietary preferences. Additionally, it provides nutritional analysis for the generated recipes and recommends meal plans based on your health goals and feedback. This project leverages machine learning and deep learning techniques, including:

- Ingredient recognition using a pre-trained MobileNetV2 model.
- Recipe generation using GPT-2.
- Nutritional analysis via external APIs.
- Meal planning with clustering algorithms (K-Means).

## Features
- **Ingredient Recognition:**
  - Automatically detects ingredients from a photo of your fridge, pantry, or countertop using a computer vision model (MobileNetV2).

- **Recipe Generation:**
  - Creates unique recipes based on the detected ingredients and your dietary preferences using GPT-2.

- **Nutritional Analysis:**
  - Provides detailed nutritional information (calories, protein, fats, and carbs) for the generated recipes using the Edamam Nutrition API.

- **Meal Planning:**
  - Recommends personalized meal plans based on your dietary goals and historical feedback using K-Means clustering.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/ai-powered-personal-chef.git
   cd ai-powered-personal-chef
   ```

2. **Install Dependencies:**
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys:**
   - Obtain API credentials for the Edamam Nutrition API from [Edamam](https://developer.edamam.com/).
   - Replace `your_api_id` and `your_api_key` in the script with your actual API credentials.

## How to Run
1. **Run the Script:**
   Execute the main script to start the application:
   ```bash
   python app.py
   ```

2. **Provide Input:**
   - When prompted, enter the path to a photo of your fridge or pantry.
   - Specify dietary preferences (e.g., "low-carb", "vegan").

3. **Receive Output:**
   - View detected ingredients.
   - Review the generated recipe with step-by-step instructions.
   - Optionally, analyze the nutritional information of the recipe.
   - Get personalized meal plan recommendations.

## Example Usage
1. **Ingredient Recognition:**
   - Upload a photo of your fridge containing items like zucchini and tomatoes.
   - Output:
     ```
     Detected ingredients: zucchini, tomato
     ```

2. **Recipe Generation:**
   - Input dietary preference: "low-carb".
   - Output:
     ```
     Recipe: Grilled Zucchini and Tomato Salad with Olive Oil and Herbs
     ```

3. **Nutritional Analysis:**
   - Output:
     ```
     Nutritional Information:
     - Calories: 250 kcal
     - Protein: 8g
     - Carbs: 15g
     - Fats: 10g
     ```

4. **Meal Planning:**
   - Input preferences: 500 calories, 20g protein, 15g fat.
   - Output:
     ```
     Recommended Meal Plan:
     - Breakfast: Scrambled eggs with zucchini
     - Lunch: Tomato soup with grilled chicken
     - Dinner: Grilled zucchini salad with a side of quinoa
     ```

## Technical Details
- **Ingredient Recognition:**
  - Pre-trained MobileNetV2 model identifies ingredients from images.

- **Recipe Generation:**
  - GPT-2 model generates context-aware recipes based on input ingredients and preferences.

- **Nutritional Analysis:**
  - Edamam Nutrition API provides detailed nutritional breakdowns of recipes.

- **Meal Planning:**
  - K-Means clustering groups similar recipes to recommend balanced meal plans.


