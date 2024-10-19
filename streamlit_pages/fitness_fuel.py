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

def fitness_fuel_page(client):
    db = client["FitForge"]
    collection = db["users"]
    generated = False

    # st.write(st.session_state.profile["food"])

    def base_metabolic_rate():
        age = st.session_state.profile['age']
        height = st.session_state.profile['height']
        weight = st.session_state.profile['weight']
        if st.session_state.profile['gender'] == "Male":
            return  66 +  (6.23 * int(weight)) + (12.7 * int(height)) - (6.8 * int(age))
        elif st.session_state.profile['gender'] == "Female":
            return  665 +  (4.35 * int(weight)) + (4.7 * int(height)) - (4.7 * int(age))

    st.image("streamlit_pages/images/FitFuel.png")

    st.subheader("Let's Count Calories")
    st.write("""
            Your basic metabolic rate (BMR) is the amount of calories your body burns 
            just to keep you alive. This is important ot know because it helps you achieve
            your dream physique. If you want to slim, you need to go into a calory deficit,
            if you are bulking, you will need a calory surplus along with some moderate workouts.
            We found your metablic rate to help you get started. If your rate looks off, make sure to check your stats in user info
            """)
    st.write(f"Your BMR is around  {base_metabolic_rate()}   calories a day.")

    st.write("---")
    st.subheader("Good Diets Produces Results")
    st.write("""
            Now that you have your BMR, Let's plan some meals to help you reach your goals in no time.
            List some of your favorite foods, and we will find some recipies for you that use those foods
            and will keep you in your caloric goals.
            """)

    # List to hold the items (liked foods)
    # TODO make this list initialize from the database with foods the user likes
    # if 'liked_foods' not in st.session_state:
    #     st.session_state.liked_foods = []

    # Input box to add new liked foods
    new_food = st.text_input("Add a new liked food:")

    # Button to add the liked food to the list
    if st.button("Add Liked Food"):
        if new_food:
            if new_food not in st.session_state.profile["food"]:
                st.session_state.profile["food"].append(new_food)
                st.success(f"Added '{new_food}' to your liked foods list!")
                collection.update_one(
                {"username": st.session_state.profile["username"]}, 
                {"$set": {"food": st.session_state.profile['food']
                  }}
                )
            else:
                st.error("Please do not duplicate foods.")
        else:
            st.error("Please enter a valid food. No duplicates allowed.")

    # Display the current list of liked foods
    if st.session_state.profile["food"]:
        st.subheader("Your Liked Foods:")
        food_to_remove = st.selectbox("Select a food to remove:", st.session_state.profile["food"])

        if st.button("Remove Liked Food"):
            st.session_state.profile["food"].remove(food_to_remove)
            st.success(f"Removed '{food_to_remove}' from your liked foods list!")
            collection.update_one(
                {"username": st.session_state.profile["username"]}, 
                {"$set": {"food": st.session_state.profile['food']
                  }}
                )
    else:
        st.write("No liked foods added yet.")
    
    st.write("---")

    st.subheader("Current Meal Plan")
    document = collection.find_one({"username": st.session_state.profile["username"]})
    st.write(document["meal_plan"])

    st.write("---")

    if st.button("Generate Meal Plan!"):
        generated = True

    if generated == True:
        st.write("Generating...")
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
        response = ask_api(query)
        st.write(response)
        collection.update_one(
            {"username": st.session_state.profile["username"]}, 
            {"$set": {"meal_plan": response}}
        )
