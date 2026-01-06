import streamlit as st
st.set_page_config(page_title="TEXT_NUMBER_INPUT",
                  page_icon="🖨️",
                  layout="centered")
st.title("Text and Number Input Methods")
name = st.text_input("Enter your Name")
comments = st.text_area("Enter any comments")


st.write("Live Output")
if name:
    st.write(f" Name : {name}")

if comments:
    st.write("Your Comments: ")
    st.write(comments)
    
age = st.number_input("Enter your Age",min_value=0,max_value=100,value=18)

ratings = st.slider("Enter Ratings(0-10)",min_value=0,max_value=10,value=5)
