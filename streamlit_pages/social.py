import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from faker import Faker
import random



def social_page(client):

    db = client["FitForge"]
    collection = db["users"]

    data = collection.find()
    # Create fake users

    
    st.header("Join the Fitness Revolution!")


    # st.write(data)r
    df = pd.DataFrame(list(data))
    result = df[['username', 'age', 'height', 'weight']]
    # st.write(result.head(20))


    def create_histogram(column_name, title, x_label):
        plt.figure(figsize=(8, 5))
        plt.hist(result[column_name], bins=10, color='skyblue', edgecolor='black')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel('Frequency')
        st.pyplot(plt)

    # Buttons for each histogram
    # if st.button("Show Age Histogram"):
    st.write("---")
    st.subheader("How old are our users?")
    create_histogram('age', 'Age Distribution', 'Age')

    st.write("---")
    st.subheader("How tall are our users?")
    # if st.button("Show Height Histogram"):
    create_histogram('height', 'Height Distribution', 'Height (inches)')

    st.write("---")
    # if st.button("Show Weight Histogram"):
    st.subheader("How old are our users?")
    create_histogram('weight', 'Weight Distribution', 'Weight (pounds)')

    st.write("---")
    st.write("Join Today!")


    ...