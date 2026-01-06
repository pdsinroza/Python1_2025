import streamlit as st
st.set_page_config(page_title="WIDGETS",
                  page_icon="🖨️",
                  layout="centered")
st.title("WIDGETS DEMO")
subjects = st.selectbox("Subjects",['Python-1','FSD-1','DE','PS'])
days = st.multiselect("Preferred Days",['Mon','Tue','Wed','Thu','Fri','Sat'])

payment = st.radio("Payment Mode",['Online','Offline'])

subscription = st.checkbox("Is subscription taken?")
