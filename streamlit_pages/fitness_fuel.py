import streamlit as st
from ai.gemini import GeminiAI

def ask_api(message):
    """ Creates the AI chat and receives a response from the message.
        args():
        message (string): The message to ask the AI.
        
        returns:
            response (string): The response from the AI.
    """
    model_name = "gemini-1.5-pro"
    fit_forge_ai = GeminiAI(model_name=model_name)
    return fit_forge_ai.single_message(message)

def fitness_fuel_page():
    st.image("streamlit_pages\images\FitFuel.png")

    st.write("Good diet produces results")

    # List to hold the items (liked foods)
    # TODO make this list initialize from the database with foods the user likes
    if 'liked_foods' not in st.session_state:
        st.session_state.liked_foods = []

    # Input box to add new liked foods
    new_food = st.text_input("Add a new liked food:")

    # Button to add the liked food to the list
    if st.button("Add Liked Food"):
        if new_food:
            if new_food not in st.session_state.liked_foods:
                st.session_state.liked_foods.append(new_food)
                st.success(f"Added '{new_food}' to your liked foods list!")
            else:
                st.error("Please do not duplicate foods.")
        else:
            st.error("Please enter a valid food. No duplicates allowed.")

    # Display the current list of liked foods
    if st.session_state.liked_foods:
        st.subheader("Your Liked Foods:")
        food_to_remove = st.selectbox("Select a food to remove:", st.session_state.liked_foods)

        if st.button("Remove Liked Food"):
            st.session_state.liked_foods.remove(food_to_remove)
            st.success(f"Removed '{food_to_remove}' from your liked foods list!")

    else:
        st.write("No liked foods added yet.")

    st.write("---")
    # Chatbox section (input area for user messages)
    st.subheader("Chatbox:")
    chat_input = st.text_input("Type your message here...")
    if st.button("Send Message"):
        if chat_input:
            st.write(f"You: {chat_input}")
            # You can implement chatbot logic here for more interactive responses
            st.write("Bot: Thank you for sharing your thoughts!")
        else:
            st.error("Please enter a message.")

age = st.session_state.profile["age"]
height = st.session_state.profile["height"]
weight = st.session_state.profile["weight"]
gender = st.session_state.profile["gender"]
body_goal = st.session_state.profile["body_goal"]
one_rm_goal = st.session_state.profile["1mg"]
six_rm_goal = st.session_state.profile["6mg"]
twelve_rm_goal = st.session_state.profile["12mg"]
preferred_foods = st.session_state.profile["food"]

# Properly format the string for the API call
query = f"""
    Create a personalized meal prep plan based on the following parameters:
    
    Age: {age}, Height: {height}, Weight: {weight}, Gender: {gender}, 
    Body Goal: {body_goal} (Specify whether the goal is to lose weight, build muscle, improve endurance, or tone the body),
    1-Rep Max Goal (1mg): {one_rm_goal} (Target weight the user wants to lift for one repetition in key exercises such as bench press, squat, or deadlift),
    6-Rep Max Goal (6mg): {six_rm_goal} (Target weight for a set of six repetitions),
    12-Rep Max Goal (12mg): {twelve_rm_goal} (Target weight for a set of twelve repetitions),
    Preferred Foods/Ingredients: {preferred_foods} (List any dietary preferences or restrictions, such as vegetarian, high-protein, low-carb, or specific foods the user enjoys or avoids).

    Design the meal prep plan to help the user achieve their body goal, complementing their workout program, and incorporating their preferred foods or dietary restrictions. The plan should include:

    - Daily Meal Breakdown: Provide specific meal plans for each day (breakfast, lunch, dinner, and snacks), with exact ingredients and quantities for each meal.
    - Nutritional Information: Include the total number of calories for each meal, along with a breakdown of macronutrients (protein, carbs, fats) to align with the user’s fitness goals.
    - Meal Prep Duration: Indicate how long each meal prep batch should last (e.g., meal prep for 3 days, or individual meals for same-day consumption).
    - Exercise Alignment: Explain how each meal supports their workout goals. For example, offer higher protein meals on strength-training days, higher carbs for endurance-focused days, and light meals for rest days.
    - Shopping List: Provide a detailed grocery list based on the ingredients for the week, categorizing items for easy shopping.
    - Special Notes: Suggest portion adjustments based on the intensity of workouts on a given day, offer quick snack ideas for pre- or post-workout fuel, and provide storage tips to keep meals fresh for longer.

    The meal plan should be flexible but supportive of the user’s fitness and nutrition goals, ensuring they hit their daily caloric and nutritional targets while making the process efficient and enjoyable.
"""

# Call your ask_api function with the properly formatted query
st.write(ask_api(query))
