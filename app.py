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
        st.image("streamlit_pages\images\FitForge2.png")

        # st.write("Profile Information:")
        # st.write(st.session_state.profile)
        header = ("Welcome " + st.session_state.profile['username'])
        st.header(header)
        st.write('Review your personal specs before finding a workout for today.')
        st.write('---')
        age = st.session_state.profile['age']
        weight = st.session_state.profile['weight']

        st.write(f"Username: {st.session_state.profile['username']}")
        st.write(f"Age: {age}")
        st.write(f"Weight: {weight}")
        st.write(f"Body Goal: {st.session_state.profile['body_goal']}")

        st.write(f'1 Month Goal: {st.session_state.profile["1mg"]}')
        st.write(f'6 Month Goal: {st.session_state.profile["6mg"]}')
        st.write(f'12 Month Goal: {st.session_state.profile["12mg"]}')

        st.write("---")
        st.write("Does that information look correct?")
        st.write("If not head to User Info to enter goals and details.")
        st.write("Head over to the Lift Lab or the Fitness Fuel station to see get imediate feedback on how to achieve your goals.")
        st.write(f"{st.session_state.profile}")
        
    else:
        st.write("### Time to Fulfill Your Destiny!")
        st.write("**At Fit Forge, you are about to embark on a transformative adventure!**")
        st.write("Imagine sculpting your body into a masterpiece, inspired by the gods and forged in the fires of dedication.")
        st.write("**Are you ready to take the first step towards your fitness revolution?** What goals ignite your passion? What challenges are you prepared to conquer on your path to greatness?")
        st.write("**Are you willing to unleash your full potential?** Visit the **Login** tab to begin your journey, and together, we will forge the body you've always envisioned!")




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
    if st.session_state.profile is None:
        st.session_state.profile = login.login(client)  # This will update the profile in session state
    else:
        login.logout()
elif st.session_state.page == "Fitness Fuel":
    if st.session_state.profile is not None:
        fitness_fuel.fitness_fuel_page()  
    else:
        st.error("Please log in to use this feature.")

elif st.session_state.page == "About":
    st.write("about page")


