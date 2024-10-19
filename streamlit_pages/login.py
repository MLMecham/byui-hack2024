import streamlit as st
from streamlit_pages import register

def login():
    st.title("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    st.write("Stored Username: ", username)
    st.write("Stored Password: ", password)

    if st.button("Login"):
        if username == "admin" and password == "password":  # Replace with your authentication logic
            st.session_state['logged_in'] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

    # if st.button("Create New Account"):
    #     # st.session_state.page = "Register"
    #     # if st.session_state.page == "Register":
    #     register.register_page()  # Replace with show_settings() function

    st.title("Create New User")

    new_username = st.text_input("Username", key="register_username")
    new_password = st.text_input("Password", type="password", key="register_password")

    st.write("Stored Username: ", new_username)
    st.write("Stored Password: ", new_password)

    if st.button("Create Account"):
        # Here you should implement your own logic to store new users
        if new_username and new_password:
            # In a real application, you would save this to a database
            st.session_state['users'][new_username] = new_password
            st.success("Account created successfully! You can now log in.")
            st.session_state['current_page'] = "Login"  # Navigate back to login
        else:
            st.error("Please fill in both fields.")

    