import streamlit as st
st.set_page_config(page_title="ADVANCED",
                  page_icon="🖨️",
                  layout="wide")
st.title("Student Profile")
st.markdown('This is used to get a demo of **sidebar**, **columns** and **expanders**')
st.sidebar.header('Profile Settings')
name = st.sidebar.text_input("Student Name","Parth")
enroll = st.sidebar.text_input("Enrollment Number")
branch = st.sidebar.selectbox('Branch',["IT","AIML","CSE_AI"])
st.sidebar.markdown("---")

col1,col2 = st.columns([1,2])

with col1:
    st.subheader("Basic Details")
    st.write(f"Name of Student : {name}")
    st.write(f"Enrollment No of Student : {enroll}")
    st.write(f"Branch : {branch}")
    
with col2:
    st.subheader("About")
    st.markdown("This is to display the info of Student")
    
with st.expander("Courses Studied"):
    st.write("1. Python")
    st.write("2. JAVA")
