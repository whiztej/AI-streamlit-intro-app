import streamlit as st

st.title("Chat With Teja")

x = st.slider('x')
st.write(x,'squared is', x*x)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

with st.chat_message("assistant"):
    st.write("Hello Teja. Welcome!")

prompt = st.chat_input("Say Something...")
if prompt:
    st.write(f"Teja has sent the following message: {prompt}")
