import streamlit as st
import pandas as pd
import numpy as np

def save_data(client, weight, height, age, gender, option):
    """ Saves the data to the account.
        Args():
        client (MongoDB): MongoDB Client
        weight (string): Weight in pounds.
        height (string): Height in inches.
        age (int): Age.
        gender (string): Gender.
    """
    # Get the connection going.
    db = client["FitForge"]
    collection = db["users"]
    # Update the profile
    st.session_state.profile["height"] = height
    st.session_state.profile["weight"] = weight
    st.session_state.profile["age"] = age
    st.session_state.profile["gender"] = gender
    st.session_state.profile["body_goal"] = option
    onemg = st.session_state.profile['1mg']
    sixmg = st.session_state.profile['6mg']
    twelvemg = st.session_state.profile['12mg']

    collection.update_one(
        {"username": st.session_state.profile["username"]}, 
        {"$set": {"height": height, "weight": weight, "age": age, "gender": gender,
                  "body_goal": option, "1mg": onemg, "6mg": sixmg, "12mg": twelvemg}}
    )
    st.success("Changes Saved Succesfully")

def info_page(client):
    st.image("streamlit_pages\images\FitForge2.png")
    # st.title("Set User Info")
    st.markdown(
        """
        <h1 style='text-align: center;'>Set User Info</h1>
        """,
        unsafe_allow_html=True
    )

    st.write("---")
    st.subheader('''
             Welcome to your personal fitness journey! 🌟
                 
Here, you have the power to customize your profile and set yourself up for success. Remember, every step you take is a step closer to achieving your goals! Whether you're aiming to build strength, improve your endurance, or simply feel better in your own skin, this is the first step in that direction.

Believe in yourself! You have the ability to create the changes you want to see in your life. Embrace this moment as a chance to reflect on your goals, understand your body, and set meaningful targets.

Let's get started on this amazing adventure together. Input your information below, and let's make those fitness dreams a reality! 💪
             
             ''')


    st.write("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        old_age = int(st.session_state.profile['age'])
        st.write("Select Age")
        age = st.slider("", 0, 100, old_age)
        st.write("age: ", age)

    with col2:
        old_weight = int(st.session_state.profile['weight'])
        st.write("Select Weight Lbs")
        weight= st.slider("", 0, 350, old_weight)
        st.write("weight: ", weight)
        weight = str(weight)

    with col3:
        old_height = int(st.session_state.profile["height"])
        st.write("Select Height Inches")
        height = st.slider("", 40, 85, old_height)
        st.write("height: ", height)
        height = str(height)

    col4, col5, col6 = st.columns(3)
    with col5:
        old_gender = st.session_state.profile["gender"]
        if old_gender == "Male":
            old_index = 0
        else:
            old_index = 1
        gender = st.radio("Choose Your Gender",
                        ("Male", "Female"),
                        index = old_index)


    st.write("---")
    # default_index = 0  # Fallback to the first option
    options = (
    "Lean/Healthy (Beginner)", 
    "Slim/Toned (Beginner)", 
    "Athletic (Intermediate)", 
    "Curvy/Toned (Intermediate)", 
    "Muscular (Advanced)", 
    "Endurance (Advanced)"
)   
    # st.write(st.session_state.profile['body_goal'])
    if st.session_state.profile['body_goal'] == '':
         default_index = 0
    else:
         
        old_option = st.session_state.profile['body_goal']
        # Find the default index based on old_option
        for index, option in enumerate(options):  # Use 'option' here to avoid name conflict
            if old_option == option:  
                default_index = index  
                break  
    # st.write(default_index)
# Create the selectbox with the specified default option
    body = st.selectbox(
        "Choose your fitness goal",
        options,
        index=default_index  # Set the default option to the matched value
)   
    st.write("---")
    
    
    text_input_goal1 = st.text_input("Enter Your One Month Goal")
    if st.button("Set One Month Goal"):
        # st.write(text_input_goal1)
        st.session_state.profile['1mg'] = text_input_goal1
        ...
    text_input_goal2 = st.text_input("Enter Your Six Month Goal")
    if st.button("Set Six Month Goal"):
        # st.write(text_input_goal2)
                st.session_state.profile['6mg'] = text_input_goal2
    text_input_goal3 = st.text_input("Enter Your Twelve Month Goal")
    if st.button("Set Twelve Month Goal"):
        # st.write(text_input_goal3)
        st.session_state.profile['12mg'] = text_input_goal3

    # st.write("blank")
    

    st.write("---")
    # st.write("Choose the food you like")

    # pillar1, pillar2 = st.columns(2)

    # with pillar1:
    #     running = st.checkbox("Running")
    #     cycling = st.checkbox("Cycling")
    #     weightlifting = st.checkbox("Weightlifting")
        
    #     exercises = []
    # with pillar2:
    #     if running:
    #         st.write("You selected Running")
    #     if cycling:
    #         st.write("You selected Cycling")
    #     if weightlifting:
    #         st.write("You selected Weightlifting")

    # options = st.multiselect(
    #     "Select your favorite workout routines:",
    #     ['Running', 'Cycling', 'Weightlifting', 'Swimming', 'Yoga']
    # )
    # st.write("You selected:", options)

    if st.button("Save Changes"):
        # Save after this button is clicked
        save_data(client, weight, height, age, gender, body)