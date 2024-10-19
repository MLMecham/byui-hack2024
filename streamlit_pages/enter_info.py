import streamlit as st
import pandas as pd
import numpy as np


st.title("Set Stats")

st.header("LiftLab")
st.subheader("What ")
st.write("sub")

if st.button("set stats"):
    st.write("Nice")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("this is the lift lab")
    age = st.slider("select your age", 0, 350, 180)
    st.write("age: ", age)

st.write(" ")
with col2:
    st.write("Select Your Weight!")
    weight= st.slider("select your age", 0, 100, 20)
    st.write("weight: ", weight)

with col3:
    st.write("Choose Your Gender")

    gender = st.radio("Select your gender:",
                      ("Male", "Female"))

    st.write("Gender: ", gender)
    # with st.expander("Expand"):
    #     st.write("cool explaination")


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