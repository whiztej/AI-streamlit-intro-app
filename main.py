import streamlit as st

st.title("Chat With Teja")

add_selectbox = st.sidebar.selectbox(
    'Support',
    ('Email', 'Phone')
)

rating_slider = st.sidebar.slider('Rate our chatbot',0,10,(1,2,3,4,5,6,7,8,9))

with st.chat_message("assistant"):
    st.write("Hello Teja. Welcome!")

prompt = st.chat_input("Say Something...")
if prompt:
    st.write(f"Teja has sent the following message: {prompt}")
