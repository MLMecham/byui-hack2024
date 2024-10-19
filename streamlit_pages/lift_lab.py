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

def lift_lab_page(client):

    db = client["FitForge"]
    collection = db["users"]

    exercises = st.session_state.profile['exercises']
    # st.write(exercises)

    def sendAPI():
        ...

    st.image("streamlit_pages\images\LiftLab2.png")

    # st.title("Lift Lab")
    st.markdown(
    """
    <h1 style="text-align: center;">Let's Make Gains</h1>
    """, 
    unsafe_allow_html=True
)
    st.write("---")

    # Explanation text
    st.write(
        "Welcome to the Lift Lab! Here, you can track your weightlifting exercises, "
        "manage your workout routines, and keep a record of your progress. "
        "Add your preferred exercises to the list, and the chatbot will remember them for future reference. "
        "Feel free to remove any exercises that you no longer need."
    )

    # List to hold the items (exercises)
    # TODO make this list initialize from the database excersizes the user likes
    # if 'exercises' not in st.session_state:
    #     st.session_state.exercises = []

    # Input box to add new exercises
    new_exercise = st.text_input("Add a new exercise:")

    # Button to add the exercise to the list
    if st.button("Add Exercise"):
        if new_exercise:
            if new_exercise not in st.session_state.profile['exercises']:
                st.session_state.profile['exercises'].append(new_exercise)
                st.success(f"Added '{new_exercise}' to your list!")
                collection.update_one(
                {"username": st.session_state.profile["username"]}, 
                {"$set": {"exercises": st.session_state.profile['exercises']
                  }}
                )
            else:
                st.error("Please do not duplicate exercises.")
        else:
            st.error("Please enter a valid exercise. No duplicates allowed.")

    # Display the current list of exercises
    if st.session_state.profile['exercises']:
        st.subheader("Current Exercises:")
        exercise_to_remove = st.selectbox("Select an exercise to remove:", st.session_state.profile['exercises'])

        if st.button("Remove Exercise"):
            st.session_state.profile['exercises'].remove(exercise_to_remove)
            st.success(f"Removed '{exercise_to_remove}' from your list!")
            collection.update_one(
                {"username": st.session_state.profile["username"]}, 
                {"$set": {"exercises": st.session_state.profile['exercises']
                  }}
                )
        # Display the list of exercises
        # st.write(st.session_state.exercises)
    else:
        st.write("No exercises added yet.")

    st.write("---")
    st.subheader("Power Move Challenge")
    st.write("🔥 **Are you feeling unstoppable today?** 🔥")
    st.write("Do you want to push your limits and take on a serious challenge? 💪 **Hit the **Power Move** button and unlock a workout that'll test your strength and endurance.** Let's make today the day you crush your goals and set new records!")
    
    
    if st.button("Power Move"): 
        st.success("Bring on the pain!")

    # Chatbox section (input area for user messages)
    st.subheader("Chatbox:")
    chat_input = st.text_input("Type your message here...")
    if st.button("Send"):
        if chat_input:
            st.write(f"You: {chat_input}")
            # Here, you could implement logic to handle the user's message
            st.write("Bot: Thank you for your message!")
        else:
            st.error("Please enter a message.weight")
            
age = st.session_state.profile["age"]
height = st.session_state.profile["height"]
weight = st.session_state.profile["weight"]
gender = st.session_state.profile["gender"]
body_goal = st.session_state.profile["body_goal"]
one_rm_goal = st.session_state.profile["1mg"]
six_rm_goal = st.session_state.profile["6mg"]
twelve_rm_goal = st.session_state.profile["12mg"]
exercises = st.session_state.profile["exercises"]

# Properly format the string for the API call
query = f"""
    Create an in-depth, personalized fitness plan based on the following parameters:
    Age: {age}, Height: {height}, Weight: {weight}, Gender: {gender}, 
    Body Goal: {body_goal} (Specify whether the goal is to lose weight, build muscle, improve endurance, tone the body, etc.),
    1-Rep Max Goal (1mg): {one_rm_goal} (Target weight the user wants to lift for one repetition in key exercises such as bench press, squat, or deadlift),
    6-Rep Max Goal (6mg): {six_rm_goal} (Target weight for a set of six repetitions),
    12-Rep Max Goal (12mg): {twelve_rm_goal} (Target weight for a set of twelve repetitions),
    Preferred Exercises: {exercises} (List any exercises or routines the user prefers to include, or highlight specific exercises like running, cycling, yoga, bench press, squats, etc.)
    
    The fitness plan should be designed to help the user reach their body goal and rep max targets over time, incorporating a balance of strength training and cardiovascular exercises.
    For each exercise, provide detailed workout sets, reps, rest periods, and progression tips. 
    Align the workout plan with the user’s fitness goals, tailoring specific muscle group exercises for strength, endurance, or hypertrophy.
    If information is incorrect or is missing do your best to just give them a workout plan based on their needs with the information provided. Do not discuss recovery strategies and supplementation, we will provide that information elsewhere.Only talk about important considerations that talk about the exercise aspect (Warm-up, Listen to your body, and Progressive overload.).Be as specific as possible for when it comes to cardio, static stretches and exercises. Add a time frame of about how long this workout will take for the level of difficulty they choose. Make sure every component gives an explicit stretch and exercise. They should not have to come up with their own stretches or exercisses.
"""

# Call your ask_api function with the properly formatted query
st.write(ask_api(query))