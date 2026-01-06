import streamlit as st
from datetime import date,time
st.set_page_config(page_title="DATE/TIME",
                  page_icon="🖨️",
                  layout="centered")
st.title("DATE AND TIME INPUTS")

exam_date = st.date_input("Select Exam Date",value=date.today())

exam_time = st.time_input("Select Time: ",value=time(9,0))
