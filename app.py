import streamlit as st
from streamlit_pages import user_info, lift_lab, login, fitness_fuel

# Function to set the query parameter based on the page
def navigate_to(page):
    st.experimental_set_query_params(page=page)

# Get current page from query parameters
query_params = st.experimental_get_query_params()
current_page = query_params.get("page", ["Home"])[0]  # Default to 'Home'

# Initialize session state for the page if not already set
if 'page' not in st.session_state:
    st.session_state.page = current_page
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Sidebar for page navigation
with st.sidebar:
    page = st.sidebar.selectbox(
        "Navigate to:",
        ["Home", "Info", "Lift Lab", "Fitness Fuel", "Login", "Settings"],
        index=["Home", "Info", "Lift Lab", "Fitness Fuel", "Login", "Settings"].index(st.session_state.page)  # Use session state for default value
    )



# Update the page in both session state and query parameters
if page != st.session_state.page:
    st.session_state.page = page
    navigate_to(page)  # Update the URL query parameter

# Render the current page based on session state
if st.session_state.page == "Home":
    st.write("home") 
elif st.session_state.page == "Info":
    user_info.info_page()  
elif st.session_state.page == "Lift Lab":
    lift_lab.lift_lab_page()  
elif st.session_state.page == "Login":
    login.login()  
elif st.session_state.page == "Fitness Fuel":
    fitness_fuel.fitness_fuel_page()  
elif st.session_state.page == "About":
    st.write("about page")  
