import streamlit as st

prompt = st.chat_input("Say Something...")
if prompt:
    st.write(f"User has sent the following message: {prompt}")