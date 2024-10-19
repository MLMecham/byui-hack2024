import streamlit as st

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