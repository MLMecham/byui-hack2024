import streamlit as st
from streamlit_pages import enter_info, lift_lab, login
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

client = mongo_init()

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
        ["Home", "Info", "Lift Lab", "Login", "Settings"],
        index=["Home", "Info", "Lift Lab", "Login", "Settings"].index(st.session_state.page)  # Use session state for default value
    )

# Update the page in both session state and query parameters
if page != st.session_state.page:
    st.session_state.page = page
    navigate_to(page)  # Update the URL query parameter

# Render the current page based on session state
if st.session_state.page == "Home":
    st.write("home")  # Replace with show_home() function
elif st.session_state.page == "Info":
    enter_info.info_page()  # Render Info page content
elif st.session_state.page == "Lift Lab":
    lift_lab.lift_lab_page()  # Replace with show_diet() function
elif st.session_state.page == "Login":
    login.login(client)  # Replace with show_stats() function
# elif st.session_state.page == "Register":
#     register.register_page()  # Replace with show_settings() function
elif st.session_state.page == "About":
    st.write("about page")  # Replace with show_about() function
