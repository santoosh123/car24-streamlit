import streamlit as st

st.title("Hello Streamlit 👋")
st.write("This is my first Streamlit app in the car24-streamlit project 🚗💨")
agree = st.checkbox("Want to know something important")

if agree:
    st.write("Sweta is bevkuf")