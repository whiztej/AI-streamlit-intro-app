import streamlit as st

st.title("Chat With Teja")

with st.chat_message("assistant"):
    st.write("Hello Teja. Welcome!")

prompt = st.chat_input("Say Something...")
if prompt:
    st.write(f"Teja has sent the following message: {prompt}")
