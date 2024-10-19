import streamlit as st
import re

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

    # Validate the Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use re.match() to check if the email matches the pattern
    if re.match(email_regex, email):
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
            "password": f"{password}",
            "body_goal": "",
            "1mg": "",
            "6mg": "",
            "12mg": "",
            "exercises": [],
            "food": []
            }
            
            collection.insert_one(account)
            st.write("Account Created!")
        
        else:    
            st.write("Username Already Taken")
    else:
        st.write("Invalid Email")



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
