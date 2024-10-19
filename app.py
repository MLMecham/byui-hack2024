import streamlit as st
from streamlit_pages import user_info, lift_lab, login, fitness_fuel
from pathlib import Path
import pymongo

# Function to initialize the MongosDB
@st.cache_resource
def mongo_init():
    # Get the current file's directory
    current_dir = Path(__file__).resolve()
    print(current_dir)

    # Construct the path to mongokey.txt
    secrets_file_path = current_dir.parent / ".streamlit" / "mongokey.txt"

    # Open the mongokey.txt file
    with secrets_file_path.open('r') as f:
        key = f.read()
        return pymongo.MongoClient(key)
    
def display_profile():
    if st.session_state.profile is not None:
        st.write("Profile Information:")
        st.write(st.session_state.profile)
    else:
        st.write("Welcome to the Fit Forge.")
        st.write("Are you ready to begin a journy a a body in the image of the Gods and forged in the flames of effort?")
        st.write("No user is logged in. Please go to the login tab to begin the fun.")



client = mongo_init()

# Function to set the query parameter based on the page
def navigate_to(page):
    st.experimental_set_query_params(page=page)

# Get current page from query parameters
# profile = None
query_params = st.experimental_get_query_params()
current_page = query_params.get("page", ["Home"])[0]  # Default to 'Home'

# Initialize session state for the page if not already set
if 'page' not in st.session_state:
    st.session_state.page = current_page
if 'profile' not in st.session_state:
    st.session_state.profile = None

# Sidebar for page navigation
with st.sidebar:
    page = st.sidebar.selectbox(
        "Navigate to:",
        ["Home", "Login", "Info", "Lift Lab", "Fitness Fuel", "Settings"],
        index=["Home", "Login", "Info", "Lift Lab", "Fitness Fuel", "Settings"].index(st.session_state.page)  # Use session state for default value
    )





# Update the page in both session state and query parameters
if page != st.session_state.page:
    st.session_state.page = page
    navigate_to(page)  # Update the URL query parameter

# Render the current page based on session state
if st.session_state.page == "Home":
    display_profile()
    
elif st.session_state.page == "Info":
    if st.session_state.profile is not None:
        user_info.info_page(client)  
    else:
        st.error("Please log in to use this feature.")

elif st.session_state.page == "Lift Lab":
    if st.session_state.profile is not None:
        lift_lab.lift_lab_page()  
    else:
        st.error("Please log in to use this feature.")

elif st.session_state.page == "Login":
    st.session_state.profile = login.login(client)  # This will update the profile in session state

elif st.session_state.page == "Fitness Fuel":
    if st.session_state.profile is not None:
        fitness_fuel.fitness_fuel_page()  
    else:
        st.error("Please log in to use this feature.")

elif st.session_state.page == "About":
    st.write("about page")


