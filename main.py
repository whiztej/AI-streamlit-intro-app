import streamlit as st

st.title("Chat With Teja")

add_selectbox = st.sidebar.selectbox(
    'Support',
    ('Email', 'Phone')
)

rating_slider = st.sidebar.slider('Rate our chatbot',0,10)

with st.chat_message("assistant"):
    st.write("Hello Teja. Welcome!")

prompt = st.chat_input("Say Something...")
if prompt:
    st.write(f"Teja has sent the following message: {prompt}")
