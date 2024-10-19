import streamlit as st

# Initialize the page state if not already in session
# if 'current_page' not in st.session_state:
#     st.session_state['current_page'] = 'home'

# # Define a function to switch between pages
# def switch_page(page_name):
#     st.session_state['current_page'] = page_name

# # Define pages based on session state
# if st.session_state['current_page'] == 'home':
#     st.title("Home Page")
#     st.write("Welcome to the home page!")

#     # Button to go to the workout page
#     if st.button("Go to Workouts"):
#         switch_page('workouts')

# elif st.session_state['current_page'] == 'workouts':
#     st.title("Workouts Page")
#     st.write("This is the workouts page.")

#     # Button to go back to home
#     if st.button("Go to Home"):
#         switch_page('home')

def navigate_to(page):
    st.experimental_set_query_params(page=page)

# Get current URL parameters
query_params = st.experimental_get_query_params()
current_page = query_params.get("page", ["home"])[0]  # Default to 'home'

# Define different pages based on parameter
if current_page == "home":
    st.image("images/FitForge.png")
    st.title("Home Page")
    st.write("Welcome to the home page!")

    # Button to navigate to the workout page
    if st.button("Go to Workouts"):
        navigate_to("workouts")

elif current_page == "workouts":
    st.title("Workouts Page")
    st.write("This is the workouts page.")

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
    
    # Button to go back to home
    if st.button("Go to Home"):
            # running = False
            # cycling = False
            # weightlifting = False
            navigate_to("home")