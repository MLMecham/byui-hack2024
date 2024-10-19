import streamlit as st

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
            st.error("Please enter a message.")