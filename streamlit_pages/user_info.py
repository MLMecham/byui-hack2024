import streamlit as st
import pandas as pd
import numpy as np


def info_page():
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

    # st.header("LiftLab")
    # st.subheader("What ")
    # st.write("sub")

    # if st.button("set stats"):
    #     st.write("Nice")

    st.write("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Select Your Age")
        age = st.slider("", 0, 100, 20)
        st.write("age: ", age)

    with col2:
        st.write("Select Your Weight")
        weight= st.slider("", 0, 350, 180)
        st.write("weight: ", weight)

    with col3:
        st.write("Choose Your Gender")

        gender = st.radio("",
                        ("Male", "Female"))

        st.write("Gender: ", gender)
        # with st.expander("Expand"):
        #     st.write("cool explaination")

    st.write("---")
    option = st.selectbox("Choose your fitness goal",
                        ("Lean", "Bulk", "cut", "tone"))

    st.write("Choose the food you like")

    pillar1, pillar2 = st.columns(2)

    with pillar1:
        running = st.checkbox("Running")
        cycling = st.checkbox("Cycling")
        weightlifting = st.checkbox("Weightlifting")

    with pillar2:
        if running:
            st.write("You selected Running")
        if cycling:
            st.write("You selected Cycling")
        if weightlifting:
            st.write("You selected Weightlifting")

    # options = st.multiselect(
    #     "Select your favorite workout routines:",
    #     ['Running', 'Cycling', 'Weightlifting', 'Swimming', 'Yoga']
    # )
    # st.write("You selected:", options)

    if st.button("Save Changes"):
        # Save after this button is clicked
        ...













# st.write("""
#          Myfirstapp
#          SUP
#          """)

# st.write("Hello, *World!* :sunglasses:")

# "sup dawg"


# data_frame = pd.DataFrame(
#         {
#             "first column": [1, 2, 3, 4],
#             "second column": [10, 20, 30, 40],
#         }
#     )

# st.write("1 + 1 = ", 2)
# st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")


# if st.button("Click Me"):
#     st.write("YOU SHOULD NOT HAVE COME")