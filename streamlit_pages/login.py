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
        "age": " ",
        "email": f"{email}",
        "height": " ",
        "weight": " ",
        "gender": " ",
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
        return True
    st.write("Invalid Username or Password")
    return False

def login(client):
    st.title("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    st.write("Stored Username: ", username)
    st.write("Stored Password: ", password)

    if st.button("Login"):
        authentication(client, username, password)

    # if st.button("Create New Account"):
    #     # st.session_state.page = "Register"
    #     # if st.session_state.page == "Register":
    #     register.register_page()  # Replace with show_settings() function

    st.title("Create New User")

    new_username = st.text_input("Username", key="register_username")
    new_password = st.text_input("Password", type="password", key="register_password")
    new_email = st.text_input("Email", key="register_email")

    st.write("Stored Username: ", new_username)
    st.write("Stored Password: ", new_password)

    if st.button("Create Account"):
        # Here you should implement your own logic to store new users
        account_creation(client, new_username, new_password, new_email)