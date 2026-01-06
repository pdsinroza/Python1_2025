import streamlit as st
st.set_page_config(page_title="BASICS",
                  page_icon="🖨️",
                  layout="wide")
st.header("Hello World")
st.title("STREAMLIT")
st.subheader("This is a subheader")
st.text("This is text mode")
st.write("This is _write mode_")
code = '''
def add(x,y):
    return x + y
z = add(3,5)
print(z)'''
st.code(code,language='python')
