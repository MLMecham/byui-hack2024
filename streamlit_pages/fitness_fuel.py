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

    # st.write(st.session_state.profile["food"])

    def base_metabolic_rate():
        age = st.session_state.profile['age']
        height = st.session_state.profile['height']
        weight = st.session_state.profile['weight']
        if st.session_state.profile['gender'] == "Male":
            return  66 +  (6.23 * int(weight)) + (12.7 * int(height)) - (6.8 * int(age))
        elif st.session_state.profile['gender'] == "Female":
            return  665 +  (4.35 * int(weight)) + (4.7 * int(height)) - (4.7 * int(age))

    st.image("streamlit_pages\images\FitFuel.png")

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

    st.write(ask_api("TEST"))