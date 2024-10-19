import streamlit as st
def account_creation(client, username, password, email):
    """ Authenticates and Creates the account
        Args():
        client (MongoDB): The MongoDB client.
        username (string): The username to be tested.
        password (string): The password to be saved.
        email (string): The email to be saved.
    """
    # Connect to the collection
    db = client["FitForge"]
    collection = db["users"]

    # Test the username
    document = collection.find_one({"username": f"{username}"})
    if document == None:
        # Create and add the account
        account = {
        "username": f"{username}",
        "age": 18,
        "email": f"{email}",
        "height": "0",
        "weight": "0",
        "gender": "Male",
        "password": f"{password}"
        }
        
        collection.insert_one(account)
        st.write("Account Created!")
    
    else:    
        st.write("Username Already Taken")

def authentication(client, username, password):
    """ Authenticates and Creates the account
        Args():
        client (MongoDB): The MongoDB client.
        username (string): The username to be tested.
        password (string): The password to be tested.
    """
    # Connect to the collection
    db = client["FitForge"]
    collection = db["users"]

    document = collection.find_one({
        "username": username,
        "password": password
    })
    if document != None:
        st.write("Logged In Succesfully!")
        return document
    st.write("Invalid Username or Password")
    return False

def login(client):
    if 'profile' in st.session_state and st.session_state.profile is not None:
        st.subheader(f"You Are Already Logged In as {st.session_state.profile['username']}")
        if st.button("Sign Out"):
            st.session_state.profile = None  # Correctly log out the user
    else:

        st.title("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            profile = authentication(client, username, password)  # Capture the returned profile
            if profile:  # If authentication is successful
                st.session_state.profile = profile  # Store the profile in session state
                st.success("Logged in successfully!")
                return profile  # Return the profile for further use
            else:
                st.error("Invalid Username or Password")  # Show error message for invalid login

        st.title("Create New User")

        new_username = st.text_input("Username", key="register_username")
        new_password = st.text_input("Password", type="password", key="register_password")
        new_email = st.text_input("Email", key="register_email")

        if st.button("Create Account"):
            account_creation(client, new_username, new_password, new_email)

def logout():
    if st.session_state.profile is not None:
        if 'profile' in st.session_state and st.session_state.profile is not None:
            st.subheader(f"You Are Already Logged In as {st.session_state.profile['username']}")
            if st.button("Sign Out"):
                st.session_state.profile = None  # Correctly log out the user
                st.success("You have been logged out.")
