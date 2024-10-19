# import streamlit as st

# def register_page():
#     st.title("Create New User")

#     new_username = st.text_input("Username", key="register_username")
#     new_password = st.text_input("Password", type="password", key="register_password")

#     if st.button("Create Account"):
#         # Here you should implement your own logic to store new users
#         if new_username and new_password:
#             # In a real application, you would save this to a database
#             st.session_state['users'][new_username] = new_password
#             st.success("Account created successfully! You can now log in.")
#             st.session_state['current_page'] = "Login"  # Navigate back to login
#         else:
#             st.error("Please fill in both fields.")

#     if st.button("Back to Login"):
#         st.session_state['current_page'] = "Login"
        