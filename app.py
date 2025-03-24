import streamlit as st

# Define a function
def my_function(user_input):
    return f"Hello, {user_input}!"

# Streamlit interface
st.title("My Railway App")
user_input = st.text_input("Enter your name:")
if st.button("Submit"):
    result = my_function(user_input)
    st.success(result)
