import streamlit as st

st.title("Streamlit Text input")

name=st.text_input("Enter your name")
age=st.slider("Select your age: " ,0,100,20)        #(range , minimum)

st.write(f"Your age is {age}")

options=["Python","Java","C++","JavaScript"]
choice=st.selectbox("Choose your favourite coding language: ", options)
st.write(f"Your selected option is {choice}")

if name:
    st.write(f"Hello , {name}")

#file uploader
uploader=st.file_uploader("Choose a csv file", type="csv")