import streamlit as st

with st.chat_message("assistant"):
    st.write("Hello Teja. Welcome!")

prompt = st.chat_input("Say Something...")
if prompt:
    st.write(f"User has sent the following message: {prompt}")
