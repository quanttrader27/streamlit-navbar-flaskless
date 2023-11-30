import streamlit as st
    
def load_view():
    st.title('Analysis Page')

    with st.sidebar:
        st.write("Filter")
        st.text_input("Name")